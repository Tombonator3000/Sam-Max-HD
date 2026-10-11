#!/usr/bin/env python3
"""Dekompilerer alle skriptene i Sam & Max Hit the Road (SCUMM v6) til tekst med descumm.

Bruk (fra roten av repoet):
    tools/bygg_descumm.sh                         # bygger descumm til work/scummvm-tools/descumm
    .venv/bin/python tools/dekompiler_skript.py   # alle skript til work/skript/
    python3 tools/dekompiler_skript.py --descumm /sti/descumm --spill game --ut work/skript

descumm finnes slik: --descumm, ellers miljøvariabelen DESCUMM, ellers descumm i PATH,
ellers work/scummvm-tools/descumm (der tools/bygg_descumm.sh legger den).

Hva som leses (begge filene er kryptert med XOR 0x69; smhd.gamedata.load dekrypterer):
  SAMNMAX.000, DSCR: nummeret til hvert globale skript som (rom, offset fra ROOM-blokken).
  SAMNMAX.001, LOFF: romnummer og offset til ROOM-blokken for hver LFLF.
  LFLF: SCRP (globale skript).
  ROOM: LSCR (lokale skript, første byte er nummeret), ENCD (inngang), EXCD (utgang)
        og OBCD (objekter) med CDHD (objektnummer), VERB (verbtabell og kode) og OBNA (navn).

descumm får hele blokken med hodet på 8 byte og flagget -6. Den kjenner taggene SCRP, LSCR,
ENCD, EXCD og VERB (parseHeader i engines/scumm/descumm-tool.cpp). For VERB leser den
verbtabellen (verb 1 byte, offset 2 byte LE, avsluttet med 0) og begynner på den laveste
offseten. Offsetene i utskriften er da fra starten av VERB-blokken, som i verbtabellen.
For de andre er de fra starten av koden (etter hodet, for LSCR også etter nummeret).

Resultat (work/ er gitignorert; spilldata skrives ikke andre steder, heller ikke midlertidig):
  globale/scrp_NNN.txt        globalt skript NNN (nummer fra DSCR)
  rom_RRR/lokal_NNN.txt       lokalt skript NNN i rom RRR
  rom_RRR/inngang.txt         inngangsskriptet (ENCD)
  rom_RRR/utgang.txt          utgangsskriptet (EXCD)
  rom_RRR/obj_OOOO_verb.txt   verbskriptene til objekt OOOO. Objekter med tom verbtabell får ingen fil.
  OVERSIKT.md                 tellinger, og hvilke skript descumm ikke klarte, med feilmeldingen
  objekter.tsv                alle objektene: nummer, rom, verb og navn (OBNA)

Hver fil begynner med noen linjer som starter med ";" og sier hvor skriptet kommer fra.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    from smhd.gamedata import be32, children, find_child, le16, le32, load
except ImportError:  # smhd er ikke installert: bruk kildekoden i pipeline/
    sys.path.insert(0, str(ROOT / "pipeline"))
    from smhd.gamedata import be32, children, find_child, le16, le32, load

TIDSGRENSE = 60  # sekunder per descumm-kjøring
STABELFEIL = "ERROR: No items on stack to pop!"

# Hvor koden begynner i blokken, sett fra offsetene descumm skriver ut
KODESTART = {"globalt": 8, "lokalt": 9, "inngang": 8, "utgang": 8, "objekt": 0}

# Forklaringer på feil vi kjenner (nøkkel: tekst i feilmeldingen fra descumm)
KJENTE_FEIL = {
    "Unknown opcode 0xbd": "ScummVM (script_v6.cpp ved c9091321) kjører 0xBD som o6_dummy i v6, altså uten "
                           "virkning. descumm kjenner 0xBD bare i HE-spill (return med ett argument).",
}

SORTER = [
    ("globalt", "Globale skript (SCRP)"),
    ("lokalt", "Lokale skript (LSCR)"),
    ("inngang", "Inngangsskript (ENCD)"),
    ("utgang", "Utgangsskript (EXCD)"),
    ("objekt", "Objektskript (VERB med kode)"),
]


@dataclass
class Jobb:
    sort: str
    rom: int
    data: bytes
    filer: list[str]            # relativt til utmappen; samme utskrift til alle
    hode: list[str]
    status: str = ""            # ok, stabelfeil eller feilet
    melding: str = ""
    advarsler: list[str] = field(default_factory=list)
    innganger: list[tuple[int, int]] = field(default_factory=list)  # verbtabellen (objektskript)
    klasser: int | None = None  # klassebitene fra DOBJ (objektskript)
    merknader: list[str] = field(default_factory=list)


# ---------------------------------------------------------------- lesing

def les_dscr(idx: bytes) -> list[tuple[int, int]]:
    """(rom, offset) for hvert globale skriptnummer, fra DSCR i indeksfilen."""
    for tag, o, size in children(idx, 0, len(idx)):
        if tag == b"DSCR":
            n = le16(idx, o + 8)
            rom = idx[o + 10:o + 10 + n]
            return [(rom[i], le32(idx, o + 10 + n + 4 * i)) for i in range(n)]
    raise ValueError("Fant ikke DSCR i indeksfilen")


def les_dobj_klasser(idx: bytes) -> list[int]:
    """Klassebitene for hvert objekt, fra DOBJ i indeksfilen (antall, eiere, klasser)."""
    for tag, o, size in children(idx, 0, len(idx)):
        if tag == b"DOBJ":
            n = le16(idx, o + 8)
            return [le32(idx, o + 10 + n + 4 * i) for i in range(n)]
    return []


def klassebyte(rest: bytes) -> list[int] | None:
    """Byte etter verbtabellen: grupper på 01 + uint16 LE, som i setClass (0x80 + klasse = sett,
    klasse uten 0x80 = fjern). Gir verdiene, eller None hvis bytene ikke har den formen."""
    if len(rest) % 3:
        return None
    verdier = []
    for i in range(0, len(rest), 3):
        if rest[i] != 1:
            return None
        verdier.append(le16(rest, i + 1))
    return verdier


def klassebits(verdier: list[int]) -> int:
    bits = 0
    for c in verdier:
        if c & 0x80:
            bits |= 1 << ((c & 0x7F) - 1)
    return bits


def les_loff(d: bytes) -> dict[int, int]:
    """Romnummer -> offset til ROOM-blokken, fra LOFF i datafilen."""
    if d[:4] != b"LECF" or d[8:12] != b"LOFF":
        raise ValueError("Datafilen begynner ikke med LECF og LOFF")
    n = d[16]
    return {d[17 + 5 * i]: le32(d, 18 + 5 * i) for i in range(n)}


def blokk(d: bytes, o: int) -> bytes:
    return d[o:o + be32(d, o + 4)]


def verbtabell(v: bytes) -> tuple[list[tuple[int, int]], int]:
    """Verbtabellen i en VERB-blokk: [(verb, offset)] og offseten der tabellen slutter."""
    p = 8
    tabell = []
    while p < len(v) and v[p] != 0:
        tabell.append((v[p], le16(v, p + 1)))
        p += 3
    return tabell, p + 1


def finn_jobber(d: bytes, idx: bytes) -> tuple[list[Jobb], dict]:
    loff = les_loff(d)
    klasser = les_dobj_klasser(idx)
    info: dict = {"rom": len(loff), "obcd": 0, "verb": 0, "tom_verb": 0, "uten_verb": 0,
                  "dscr_plasser": 0, "dscr_brukt": 0, "felles": [], "dscr_feil": [],
                  "scrp_uten_nummer": 0, "doble_objekter": [], "mellomrom": 0, "mellomrom_klasser": 0,
                  "objekter": []}
    jobber: list[Jobb] = []

    # Globale skript: DSCR gir nummeret, SCRP-blokkene ligger i LFLF
    dscr = les_dscr(idx)
    info["dscr_plasser"] = len(dscr)
    nummer_for: dict[int, list[int]] = defaultdict(list)  # offset i filen -> skriptnumre
    for nr, (rom, off) in enumerate(dscr):
        if rom == 0:
            continue
        info["dscr_brukt"] += 1
        if rom not in loff:
            info["dscr_feil"].append(f"skript {nr}: rom {rom} finnes ikke i LOFF")
            continue
        a = loff[rom] + off
        if d[a:a + 4] != b"SCRP":
            info["dscr_feil"].append(f"skript {nr}: rom {rom} offset {off} er {d[a:a + 4]!r}, ikke SCRP")
            continue
        nummer_for[a].append(nr)

    for rom in sorted(loff, key=loff.get):
        room = loff[rom]
        lflf = room - 8
        for tag, o, size in children(d, lflf + 8, lflf + be32(d, lflf + 4)):
            if tag != b"SCRP":
                continue
            numre = nummer_for.get(o, [])
            if numre:
                filer = [f"globale/scrp_{nr:03d}.txt" for nr in numre]
                tekst = (f"; Globalt skript {' og '.join(map(str, numre))} "
                         f"(SCRP i rom {rom}, offset 0x{o - room:X} fra ROOM-blokken)")
                if len(numre) > 1:
                    info["felles"].append(numre)
                    tekst += ". Alle disse numrene i DSCR peker på denne samme blokken"
            else:
                info["scrp_uten_nummer"] += 1
                filer = [f"globale/scrp_uten_nummer_rom{rom:03d}_{o - room:06X}.txt"]
                tekst = f"; Globalt skript uten nummer i DSCR (SCRP i rom {rom}, offset 0x{o - room:X} fra ROOM-blokken)"
            jobber.append(Jobb("globalt", rom, d[o:o + size], filer, [tekst]))

    # Rommene: LSCR, ENCD, EXCD og OBCD/VERB
    for rom in sorted(loff):
        room = loff[rom]
        mappe = f"rom_{rom:03d}"
        brukte: Counter = Counter()
        for tag, o, size in children(d, room + 8, room + be32(d, room + 4)):
            if tag == b"LSCR":
                nr = d[o + 8]
                jobber.append(Jobb("lokalt", rom, d[o:o + size], [f"{mappe}/lokal_{nr:03d}.txt"],
                                   [f"; Lokalt skript {nr} i rom {rom} (LSCR)"]))
            elif tag == b"ENCD":
                jobber.append(Jobb("inngang", rom, d[o:o + size], [f"{mappe}/inngang.txt"],
                                   [f"; Inngangsskriptet til rom {rom} (ENCD)"]))
            elif tag == b"EXCD":
                jobber.append(Jobb("utgang", rom, d[o:o + size], [f"{mappe}/utgang.txt"],
                                   [f"; Utgangsskriptet til rom {rom} (EXCD)"]))
            elif tag == b"OBCD":
                info["obcd"] += 1
                cdhd = find_child(d, o, size, b"CDHD")
                obj = le16(d, cdhd + 8) if cdhd is not None else -1
                obna = find_child(d, o, size, b"OBNA")
                navn = blokk(d, obna)[8:].split(b"\0")[0].decode("latin1") if obna is not None else ""
                vo = find_child(d, o, size, b"VERB")
                if vo is None:
                    info["uten_verb"] += 1
                    continue
                info["verb"] += 1
                v = blokk(d, vo)
                tabell, slutt = verbtabell(v)
                info["objekter"].append((obj, rom, [vb for vb, _ in tabell], navn))
                if not tabell:
                    info["tom_verb"] += 1
                    continue
                brukte[obj] += 1
                if brukte[obj] > 1:
                    info["doble_objekter"].append((rom, obj, navn))
                ekstra = f"_{brukte[obj]}" if brukte[obj] > 1 else ""
                hode = [f'; Objekt {obj} "{navn}" i rom {rom} (OBCD/VERB)',
                        "; Verbtabell (verb: offset fra starten av VERB-blokken): "
                        + ", ".join(f"{vb}: 0x{off:04X}" for vb, off in tabell)]
                laveste = min(off for _, off in tabell)
                if laveste > slutt:
                    info["mellomrom"] += 1
                    rest = v[slutt:laveste]
                    verdier = klassebyte(rest)
                    if verdier is not None and obj < len(klasser) and klassebits(verdier) == klasser[obj]:
                        info["mellomrom_klasser"] += 1
                        hode.append(f"; Mellom verbtabellen og første inngang: {len(verdier)} x (01, uint16) = "
                                    f"{', '.join(map(str, verdier))}. Ingen inngang peker dit, og descumm hopper "
                                    "over dem. Satt som klasser gir de samme bitene som DOBJ har for objektet.")
                    else:
                        hode.append("; Byte mellom verbtabellen og første inngang (ingen inngang peker dit, "
                                    "descumm hopper over dem): " + rest.hex(" "))
                jobb = Jobb("objekt", rom, v, [f"{mappe}/obj_{obj:04d}_verb{ekstra}.txt"], hode,
                            innganger=tabell, klasser=klasser[obj] if 0 <= obj < len(klasser) else None)
                if laveste > 255:
                    # descumm begynner på min(255, laveste offset) (skipVerbHeader_V567)
                    jobb.advarsler.append(f"laveste inngang er 0x{laveste:X}, men descumm begynner på 0xFF")
                jobber.append(jobb)
    return jobber, info


# ---------------------------------------------------------------- descumm

def finn_descumm(valg: str | None) -> Path:
    def kjorbar(sti) -> bool:
        return bool(sti) and Path(sti).is_file() and os.access(sti, os.X_OK)

    # Er stien gitt med --descumm eller DESCUMM, brukes bare den
    for kilde, sti in (("--descumm", valg), ("DESCUMM", os.environ.get("DESCUMM"))):
        if sti:
            if not kjorbar(sti):
                sys.exit(f"{kilde} peker på {sti}, som ikke er en kjørbar fil.")
            return Path(sti).resolve()
    for sti in (shutil.which("descumm"), ROOT / "work" / "scummvm-tools" / "descumm"):
        if kjorbar(sti):
            return Path(sti).resolve()
    sys.exit("Fant ikke descumm. Bygg den med tools/bygg_descumm.sh, eller bruk --descumm eller DESCUMM.")


def descumm_commit(descumm: Path) -> str:
    """Commiten descumm er bygget fra, hvis den ligger i en git-klone fra bygg_descumm.sh."""
    head = descumm.parent / ".git" / "HEAD"
    try:
        tekst = head.read_text().strip()
    except OSError:
        return ""
    return tekst if re.fullmatch(r"[0-9a-f]{40}", tekst) else ""


def kjor(descumm: Path, jobb: Jobb, fil: Path) -> str:
    fil.write_bytes(jobb.data)
    try:
        r = subprocess.run([str(descumm), "-6", str(fil)], capture_output=True, timeout=TIDSGRENSE, check=False)
    except subprocess.TimeoutExpired as e:
        jobb.status, jobb.melding = "feilet", f"tidsgrensen på {TIDSGRENSE} s gikk ut"
        return (e.stdout or b"").decode("latin1")
    finally:
        fil.unlink(missing_ok=True)
    ut = r.stdout.decode("latin1")
    feil = r.stderr.decode("latin1").strip()
    linjer = ut.rstrip("\n").split("\n")
    if r.returncode != 0:
        jobb.status = "feilet"
        if r.returncode < 0:
            jobb.melding = f"descumm stoppet med signal {-r.returncode}"
        else:
            jobb.melding = feil.splitlines()[-1] if feil else f"descumm avsluttet med kode {r.returncode}"
    elif linjer[-1] != "END":
        jobb.status, jobb.melding = "feilet", "utskriften slutter ikke med END"
    elif STABELFEIL in ut:
        jobb.status = "stabelfeil"
        jobb.melding = f'{ut.count(STABELFEIL)} x "{STABELFEIL}"'
    else:
        jobb.status = "ok"
    if feil and jobb.status != "feilet":
        jobb.advarsler += feil.splitlines()
    sjekk_innganger(jobb, ut)
    return ut


def sjekk_innganger(jobb: Jobb, ut: str) -> None:
    """Merker verbinnganger som havner inne i en linje i utskriften.

    descumm skriver ikke en egen linje for push-instruksjoner; de blir en del av neste linje.
    Ligger det byte foran en inngang som bare er push (for eksempel klassebytene), begynner
    linjen før inngangen. Koden er den samme, men inngangen står ikke som egen linje.
    """
    linjer = sorted({int(x, 16) for x in re.findall(r"^\[([0-9A-F]{4,})\]", ut, re.MULTILINE)})
    for verb, off in jobb.innganger:
        if off in linjer or not linjer or off < linjer[0] or off >= len(jobb.data):
            continue
        start = max(x for x in linjer if x < off)
        foran = jobb.data[start:off]
        tekst = (f"; Inngangen til verb {verb} (0x{off:04X}) er inne i linjen [{start:04X}]. "
                 f"Byte foran den: {foran.hex(' ')}")
        verdier = klassebyte(foran)
        if verdier is not None and jobb.klasser is not None and klassebits(verdier) == jobb.klasser:
            tekst += (". descumm leser dem som push uten egen linje. Satt som klasser gir de samme "
                      "bitene som DOBJ har for objektet, så det er trolig ikke kode")
        else:
            tekst += ". descumm leser dem som en del av linjen"
        jobb.merknader.append(tekst + ".")


def skriv(utmappe: Path, jobb: Jobb, ut: str) -> None:
    hode = list(jobb.hode)
    if jobb.status == "feilet":
        hode.append(f"; descumm feilet: {jobb.melding}. Det som står under, er det den rakk.")
        for tekst, forklaring in KJENTE_FEIL.items():
            if tekst in jobb.melding:
                hode.append(f"; {forklaring}")
        siste = re.findall(r"^\[([0-9A-F]{4,})\]", ut, re.MULTILINE)
        if siste:
            fra = int(siste[-1], 16)
            rest = jobb.data[KODESTART[jobb.sort] + fra:]
            hode.append(f"; Byte fra siste viste offset 0x{fra:04X} til slutten ({len(rest)} byte): "
                        + rest[:96].hex(" ") + (" ..." if len(rest) > 96 else ""))
    elif jobb.status == "stabelfeil":
        hode.append(f"; descumm meldte feil underveis: {jobb.melding}")
    hode += jobb.merknader
    for a in jobb.advarsler:
        hode.append(f"; Advarsel: {a}")
    tekst = "\n".join(hode) + "\n\n" + ut
    if not tekst.endswith("\n"):
        tekst += "\n"
    for navn in jobb.filer:
        sti = utmappe / navn
        sti.parent.mkdir(parents=True, exist_ok=True)
        sti.write_text(tekst, encoding="utf-8")


# ---------------------------------------------------------------- oversikt

def oversikt(utmappe: Path, jobber: list[Jobb], info: dict, descumm: Path, spill: Path,
             md5: dict[str, str]) -> str:
    tid = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M")
    commit = descumm_commit(descumm)
    linjer = [
        "# Dekompilerte skript",
        "",
        f"Laget {tid} med tools/dekompiler_skript.py.",
        f"descumm: {descumm}" + (f" (scummvm-tools {commit})" if commit else "") + ", flagget -6.",
        f"Spillfiler: {spill}/SAMNMAX.000 (md5 {md5['000']}) og SAMNMAX.001 (md5 {md5['001']}).",
        "",
        "Uten feil: descumm avsluttet normalt med END og ingen feilmeldinger.",
        "Med stabelfeil: descumm skrev \"ERROR: No items on stack to pop!\" og fortsatte med",
        "\"**** INVALID DATA ****\" der verdien skulle stått. Resten av skriptet er med.",
        "Feilet: descumm stoppet (ukjent opkode eller annen feil). Filen har det den rakk.",
        "",
        "| Sort | Skript | Uten feil | Med stabelfeil | Feilet |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    sum_ = Counter()
    for sort, tittel in SORTER:
        js = [j for j in jobber if j.sort == sort]
        c = Counter(j.status for j in js)
        linjer.append(f"| {tittel} | {len(js)} | {c['ok']} | {c['stabelfeil']} | {c['feilet']} |")
        sum_.update(c)
        sum_["alle"] += len(js)
    linjer.append(f"| Sum | {sum_['alle']} | {sum_['ok']} | {sum_['stabelfeil']} | {sum_['feilet']} |")
    filer = sum(len(j.filer) for j in jobber)
    linjer += [
        "",
        f"Filer skrevet: {filer}.",
        "",
        "## Telling av blokkene",
        "",
        f"- Rom (LFLF i LOFF): {info['rom']}.",
        f"- DSCR: {info['dscr_brukt']} av {info['dscr_plasser']} plasser er i bruk.",
    ]
    for numre in info["felles"]:
        linjer.append(f"- DSCR-numrene {', '.join(map(str, numre))} peker på samme SCRP-blokk. "
                      "Den er dekompilert én gang og skrevet til en fil per nummer.")
    if info["scrp_uten_nummer"]:
        linjer.append(f"- SCRP-blokker uten nummer i DSCR: {info['scrp_uten_nummer']}.")
    for f in info["dscr_feil"]:
        linjer.append(f"- Feil i DSCR: {f}.")
    linjer += [
        f"- Objekter (OBCD): {info['obcd']}. Med VERB: {info['verb']}, uten VERB: {info['uten_verb']}.",
        f"- Tom verbtabell (ingen kode, ingen fil): {info['tom_verb']}. Med kode: {info['verb'] - info['tom_verb']}.",
        (f"- Objekter med byte mellom verbtabellen og første inngang: {info['mellomrom']} "
         "(står i hodet på filen). Av dem har "
         f"{info['mellomrom_klasser']} formen 01 + uint16 og gir samme klassebiter som DOBJ."),
    ]
    inne = [j for j in jobber if j.merknader]
    linjer.append(f"- Objektskript der en verbinngang havner inne i en linje i utskriften: {len(inne)} "
                  f"({sum(len(j.merknader) for j in inne)} innganger). Byte foran inngangen står i hodet på filen.")
    for rom, obj, navn in info["doble_objekter"]:
        linjer.append(f'- Objekt {obj} "{navn}" har mer enn én OBCD med kode i rom {rom}; '
                      "den andre har _2 i filnavnet.")
    feilet = [j for j in jobber if j.status == "feilet"]
    stabel = [j for j in jobber if j.status == "stabelfeil"]
    advarsler = [j for j in jobber if j.advarsler]
    linjer += ["", "## Feilet", ""]
    linjer += [f"- {j.filer[0]}: {j.melding}" for j in feilet] or ["Ingen."]
    kjente = {tekst: forklaring for tekst, forklaring in KJENTE_FEIL.items()
              if any(tekst in j.melding for j in feilet)}
    if kjente:
        linjer.append("")
        linjer += [f"Om \"{tekst}\": {forklaring}" for tekst, forklaring in kjente.items()]
    linjer += ["", "## Med stabelfeil", ""]
    linjer += [f"- {j.filer[0]}: {j.melding}" for j in stabel] or ["Ingen."]
    linjer += ["", "## Advarsler", ""]
    linjer += [f"- {j.filer[0]}: {'; '.join(j.advarsler)}" for j in advarsler] or ["Ingen."]
    tekst = "\n".join(linjer) + "\n"
    (utmappe / "OVERSIKT.md").write_text(tekst, encoding="utf-8")
    return tekst


def objektliste(utmappe: Path, info: dict) -> None:
    """Alle objektene (OBCD) med rom, verb og navn, så numrene i skriptene kan slås opp."""
    linjer = ["# objekt\trom\tverb\tnavn"]
    for obj, rom, verb, navn in sorted(info["objekter"]):
        linjer.append(f"{obj}\t{rom}\t{','.join(map(str, verb)) or '-'}\t{navn}")
    (utmappe / "objekter.tsv").write_text("\n".join(linjer) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- hoved

def rydd(utmappe: Path) -> None:
    """Fjerner det en tidligere kjøring laget, og ingenting annet."""
    for sti in utmappe.iterdir():
        laget = (sti.name == "globale" or re.fullmatch(r"rom_\d{3}", sti.name)
                 or sti.name.startswith("tmp_descumm_"))
        if sti.is_dir() and laget:
            shutil.rmtree(sti)
        elif sti.is_file() and sti.name in ("OVERSIKT.md", "objekter.tsv"):
            sti.unlink()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Dekompilerer alle skriptene i Sam & Max (SCUMM v6) med descumm.")
    ap.add_argument("--descumm", help="sti til descumm (ellers DESCUMM, PATH eller work/scummvm-tools/descumm)")
    ap.add_argument("--spill", type=Path, default=ROOT / "game", help="mappen med SAMNMAX.000 og .001 (game/)")
    ap.add_argument("--ut", type=Path, default=ROOT / "work" / "skript", help="utmappen (work/skript/)")
    ap.add_argument("--jobber", type=int, default=os.cpu_count() or 2, help="descumm-kjøringer samtidig")
    a = ap.parse_args(argv)

    utmappe = a.ut.resolve()
    work = (ROOT / "work").resolve()
    if utmappe.is_relative_to(ROOT) and not utmappe.is_relative_to(work):
        sys.exit(f"Utmappen {utmappe} er i repoet, men ikke under work/. Skriptene er spilldata og skal ikke inn i git.")
    descumm = finn_descumm(a.descumm)
    spill = a.spill.resolve()
    for navn in ("SAMNMAX.000", "SAMNMAX.001"):
        if not (spill / navn).is_file():
            sys.exit(f"Fant ikke {spill / navn}. Hent spillfilene med tools/hent_spilldata.sh.")

    md5 = {n: hashlib.md5((spill / f"SAMNMAX.{n}").read_bytes()).hexdigest() for n in ("000", "001")}
    idx, _ = load(spill / "SAMNMAX.000")
    d, _ = load(spill / "SAMNMAX.001")
    jobber, info = finn_jobber(d, idx)
    print(f"Fant {len(jobber)} skript i {info['rom']} rom. Kjører {descumm} -6 ...")

    utmappe.mkdir(parents=True, exist_ok=True)
    rydd(utmappe)
    tmp = Path(tempfile.mkdtemp(prefix="tmp_descumm_", dir=utmappe))
    try:
        def en(i_jobb):
            i, jobb = i_jobb
            ut = kjor(descumm, jobb, tmp / f"{i:04d}.bin")
            skriv(utmappe, jobb, ut)
        with ThreadPoolExecutor(max(1, a.jobber)) as pool:
            list(pool.map(en, enumerate(jobber)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    oversikt(utmappe, jobber, info, descumm, spill, md5)
    objektliste(utmappe, info)
    c = Counter(j.status for j in jobber)
    print(f"Ferdig: {c['ok']} uten feil, {c['stabelfeil']} med stabelfeil, {c['feilet']} feilet.")
    print(f"Resultat i {utmappe}, oversikt i {utmappe / 'OVERSIKT.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
