#!/usr/bin/env python3
"""Styrer Sam & Max HD uten skjerm, for gjennomspillingsagenten (DIGHD_STYRING i motoren).

Spillet går i bakgrunnen. Hvert kall sender noen kommandoer, venter til motoren har gjort dem,
og skriver en kort status: rom, om spilleren har kontrollen, markøren, replikken som vises,
tingene på skjermen med navn og hvor de skal klikkes, inventaret og det som vises uten HD.
Bilder lagres i bilder/ med HD, originalpikslene og gult der HD mangler, og styr.py sier fra
om felter der HD-bildet avviker mye fra originalen.

    tools/styr.py start                 starter spillet fra begynnelsen
    tools/styr.py start --slot 3        starter fra lagret spill 3
    tools/styr.py klikk 120 80          venstreklikk på 120,80 (originalpiksler, 320 x 200)
    tools/styr.py klikkting 82          klikk på ting 82 der den står på skjermen akkurat nå
    tools/styr.py hoyreklikk 1 1        neste markør (gå, se, hånd, snakk, ...)
    tools/styr.py "klikk 20 124" "kontroll" bilde
                                        flere kommandoer etter hverandre, og bilde til slutt
    tools/styr.py markor se             bytter til se-markøren (gå, se, hånd, snakk, figur)
    tools/styr.py status                siste status på nytt
    tools/styr.py utsnitt 12 100 80 40 30 max-hode
                                        HD, original og gult side om side for bilde 12, felt 100,80
                                        40 x 30 originalpiksler, til funnbilder/ (bevis i FUNN.md)
    tools/styr.py stopp                 avslutter spillet

Kommandoer til motoren: klikk X Y, klikkting NR (klikker på ting NR der den er nå, også når
bildet ruller), hoyreklikk X Y, flytt X Y, pek X Y, tast COMBO (escape,
period, f5, ctrl+h ...), vent N (bilder, omtrent 60 per sekund), kontroll [N] (til spilleren
har kontrollen igjen), bilde [NAVN], lagre SLOT TEKST, last SLOT, avslutt.
Et ord alene uten tall (som "bilde" eller "kontroll") går også.

Alt ligger i work/gjennomspill (eller --mappe): ctl/ (kommando og status), bilder/, lagret/
(samnmax.sNN, kan brukes med tools/romtest.sh --lagret, og dighd-uten-hd.txt med alt som er
vist uten HD) og scummvm.log.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Markørene i Sam & Max er objekter i rom 93. Over noe som kan brukes, viser spillet en annen variant.
# Sett 17. oktober 2026 med høyreklikk og flytting i kontoret (rom 7).
MARKOR_VALG = {
    "gå": {889, 890}, "ga": {889, 890},
    "se": {883, 875},
    "hånd": {884, 876}, "hand": {884, 876}, "ta": {884, 876}, "bruk": {884, 876},
    "snakk": {885, 877},
    "figur": {886, 878},
}

MARKORER = {
    889: "gå", 890: "gå (over noe)",
    883: "se", 875: "se (over noe)",
    884: "hånd (ta eller bruk)", 876: "hånd (over noe)",
    885: "snakk", 877: "snakk (over noe)",
    886: "hånd med figur", 878: "hånd med figur (over noe)",
}


def mappe(args) -> Path:
    return Path(args.mappe).resolve()


def les_status(ctl: Path) -> dict | None:
    try:
        return json.loads((ctl / "status.json").read_text(encoding="utf-8", errors="replace"))
    except (OSError, ValueError):
        return None


def kjorer(m: Path) -> bool:
    try:
        pid = int((m / "pid").read_text())
    except (OSError, ValueError):
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    # En avsluttet prosess som ikke er ryddet bort (zombie) regnes som stoppet
    try:
        return "Z" not in Path(f"/proc/{pid}/stat").read_text().split(")")[-1].split()[0]
    except OSError:
        return True


def loggslutt(m: Path, n: int = 25) -> str:
    try:
        linjer = (m / "scummvm.log").read_text(errors="replace").splitlines()
    except OSError:
        return ""
    return "\n".join(linjer[-n:])


def neste_id(m: Path) -> int:
    f = m / "neste_id"
    try:
        n = int(f.read_text()) + 1
    except (OSError, ValueError):
        n = 1
    f.write_text(str(n))
    return n


def neste_bildenr(m: Path) -> int:
    return len(list((m / "bilder").glob("*_gult.png"))) + 1


def ventetid(kommandoer: list[str]) -> float:
    """Sekunder å vente på svar: vent og kontroll teller, med god margin."""
    t = 60.0
    for k in kommandoer:
        deler = k.split()
        if not deler:
            continue
        tall = int(deler[1]) if len(deler) > 1 and deler[1].lstrip("-").isdigit() else None
        if deler[0] == "vent":
            t += (tall or 1) / 30
        elif deler[0] == "kontroll":
            t += (tall or 900) / 30
        elif deler[0] in ("lagre", "last"):
            t += 10
    return t


def avvik(hd_fil: Path, flat_fil: Path) -> list[str]:
    """Felter på 16 x 16 originalpiksler der HD-bildet, skalert ned, er langt fra originalen."""
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return ["(numpy og Pillow mangler, avvik ikke målt)"]
    hd = np.asarray(Image.open(hd_fil).convert("RGB").resize((320, 200), Image.BOX), dtype=np.float32)
    fl = np.asarray(Image.open(flat_fil).convert("RGB").resize((320, 200), Image.BOX), dtype=np.float32)
    d = np.abs(hd - fl).max(axis=2)
    ut = []
    for by in range(0, 200, 16):
        for bx in range(0, 320, 16):
            blokk = d[by:by + 16, bx:bx + 16]
            andel = float((blokk > 60).mean())
            if andel > 0.35:
                ut.append(f"{bx},{by} til {bx + 16},{by + 16}: {round(andel * 100)} % av pikslene avviker sterkt")
    return ut


def skriv_status(st: dict, m: Path, bilder: list[tuple[str, Path]]) -> None:
    mk = st.get("markor_objekt") or {}
    mnr = mk.get("nr", 0)
    print(f"rom {st.get('rom')}   kontroll {'ja' if st.get('kontroll') else 'nei'}   "
          f"markør {mnr} {MARKORER.get(mnr, '')}   bilde nr {st.get('bilde')}")
    if st.get("tekst"):
        print(f"tekst: {' '.join(st['tekst'].split())}")
    obj = st.get("objekter") or []
    if obj:
        print("ting (klikk på x,y):")
        for o in obj:
            merk = "" if o.get("under_midten") == o.get("nr") else f"  (midten treffer {o.get('under_midten')}, klikk et annet sted i feltet)"
            if o.get("fra_annet_rom"):
                navn = (o['navn'] or "(uten navn)") + " [inventaret]"
            else:
                navn = o['navn'] or "(uten navn: ofte en utgang, trapp eller dør)"
            print(f"  {o['nr']:5} {navn:<32} {o['x']:3},{o['y']:3}  felt {o['venstre']},{o['topp']} {o['b']}x{o['h']}  tilstand {o['tilstand']}{merk}")
    if any(o.get("fra_annet_rom") for o in obj):
        print("Inventaret er åpent: knappene øverst er markørene (se, hånd, snakk, figur), esken lukker, resten er tingene.")
    fig = [f for f in st.get("figurer") or [] if f.get("synlig") and 0 <= f["x"] < 320 and 0 <= f["y"] <= 200]
    if fig:
        print("figurer på skjermen: " + ", ".join(f"{f['nr']}{(' ' + f['navn']) if f['navn'] else ''} ved {f['x']},{f['y']}" for f in fig))
    inv = st.get("inventar") or []
    print("inventar: " + (", ".join(f"{i['nr']} {i['navn']}" for i in inv) or "tomt"))
    for p in st.get("pekt") or []:
        print(f"under {p['x']},{p['y']}: {p['nr'] or 'ingenting'} {p['navn']}")
    uten = st.get("uten_hd") or []
    if uten:
        print("uten HD nå: " + ", ".join(f"{u['hva'].split(chr(9))[1]} ({u['px']} px)" for u in uten))
    if st.get("feil"):
        print(f"FEIL fra motoren: {st['feil']}")
    for navn, hd in bilder:
        flat = hd.with_name(hd.stem + "_flat.png")
        gult = hd.with_name(hd.stem + "_gult.png")
        print(f"bilde {navn}: {hd}")
        print(f"   original: {flat}")
        print(f"   gult der HD mangler: {gult}")
        if flat.exists():
            av = avvik(hd, flat)
            if av:
                print("   HD avviker mye fra originalen i: " + "; ".join(av[:12]) + (" ..." if len(av) > 12 else ""))


def start(args) -> int:
    m = mappe(args)
    if kjorer(m):
        print(f"Spillet går allerede (pid {(m / 'pid').read_text().strip()}). Kjør tools/styr.py stopp først.")
        return 1
    motor = Path(args.motor or ROOT / "engine/scummvm/scummvm")
    spill = Path(args.spill)
    mod = Path(args.mod)
    for hva, sti in (("motoren", motor), ("spillfilene", spill / "SAMNMAX.001"), ("HD-modden", mod / "mod.json")):
        if not sti.exists():
            print(f"Fant ikke {hva}: {sti}")
            return 1
    for d in ("ctl", "bilder", "lagret", "hjem"):
        (m / d).mkdir(parents=True, exist_ok=True)
    for f in (m / "ctl").glob("*"):
        f.unlink()
    (m / "neste_id").write_text("0")
    env = {k: v for k, v in os.environ.items() if not k.startswith(("DIGHD_", "SDL_"))}
    env.update({
        "HOME": str(m / "hjem"),
        "XDG_CONFIG_HOME": str(m / "hjem/.config"),
        "XDG_DATA_HOME": str(m / "hjem/.local/share"),
        "XDG_CACHE_HOME": str(m / "hjem/.cache"),
        "SDL_VIDEODRIVER": "dummy",
        "SDL_AUDIODRIVER": "dummy",
        "DIGHD_MOD": str(mod.resolve()),
        "DIGHD_STYRING": str(m / "ctl"),
        # Loggen over det som vises uten HD er en lagringsfil (lagret/dighd-uten-hd.txt). DIGHD_MANGLER
        # tar bare et filnavn; en hel sti stopper motoren (assert i posix-fs, funnet av agenten 17. oktober).
    })
    cmd = [str(motor), f"--path={spill.resolve()}", f"--savepath={m / 'lagret'}", "--debuglevel=1"]
    if args.slot is not None:
        cmd.append(f"--save-slot={args.slot}")
    cmd.append("samnmax")
    with open(m / "scummvm.log", "ab") as logg:
        logg.write(f"\n=== start {time.strftime('%Y-%m-%d %H:%M:%S')} {' '.join(cmd)}\n".encode())
        p = subprocess.Popen(cmd, env=env, cwd=m / "hjem", stdout=logg, stderr=subprocess.STDOUT,
                             stdin=subprocess.DEVNULL, start_new_session=True)
    (m / "pid").write_text(str(p.pid))
    time.sleep(2)
    print(f"Spillet er startet (pid {p.pid}){' fra lagret spill ' + str(args.slot) if args.slot is not None else ''}.")
    return send(args, ["kontroll 600", "bilde start"] if args.slot is not None else ["vent 30", "bilde start"])


def send(args, kommandoer: list[str], stille: bool = False) -> int:
    m = mappe(args)
    if not kjorer(m):
        print("Spillet går ikke. Start det med tools/styr.py start [--slot N].")
        slutt = loggslutt(m)
        if slutt:
            print("Slutten av scummvm.log:\n" + slutt)
        return 3
    ctl = m / "ctl"
    # Ord alene får standardverdier; bilder får et løpenummer og havner i bilder/
    ut, bildenavn = [], []
    nr = neste_bildenr(m)
    for k in kommandoer:
        deler = k.strip().split(maxsplit=1)
        if not deler:
            continue
        if deler[0] == "bilde":
            navn = f"{nr:04d}" + (f"_{deler[1].strip().replace(' ', '_')}" if len(deler) > 1 else "")
            nr += 1
            bildenavn.append(navn)
            ut.append(f"bilde {navn}")
        else:
            ut.append(k.strip())
    cid = neste_id(m)
    tmp = ctl / "kommando.tmp"
    tmp.write_text(f"id {cid}\n" + "\n".join(ut) + "\n", encoding="utf-8")
    os.replace(tmp, ctl / "kommando.txt")
    frist = time.monotonic() + ventetid(ut)
    st = None
    while time.monotonic() < frist:
        st = les_status(ctl)
        if st and st.get("id") == cid:
            break
        if not kjorer(m):
            print("Spillet har stoppet (krasj eller avslutning) før kommandoene var ferdige.")
            print("Slutten av scummvm.log:\n" + loggslutt(m))
            return 3
        time.sleep(0.25)
    else:
        print(f"Fikk ikke svar innen {round(ventetid(ut))} sekunder. Spillet kan ha hengt seg.")
        print("Slutten av scummvm.log:\n" + loggslutt(m, 10))
        return 4
    bilder = []
    for navn in bildenavn:
        for suffiks in ("", "_flat", "_gult"):
            kilde = ctl / f"{navn}{suffiks}.png"
            if kilde.exists():
                shutil.move(str(kilde), m / "bilder" / kilde.name)
        bilder.append((navn, m / "bilder" / f"{navn}.png"))
    if not stille:
        skriv_status(st, m, bilder)
    (m / "siste.json").write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


def utsnitt(args, k: list[str]) -> int:
    """HD, original og gult side om side fra ett av bildene, til funnbilder/."""
    from PIL import Image, ImageDraw
    m = mappe(args)
    if len(k) < 6 or not all(x.isdigit() for x in k[1:6]):
        print("Bruk: tools/styr.py utsnitt BILDENR X Y B H [navn]  (originalpiksler)")
        return 1
    nr, x, y, b, h = (int(v) for v in k[1:6])
    navn = k[6] if len(k) > 6 else "utsnitt"
    hd = sorted(p for p in (m / "bilder").glob(f"{nr:04d}*.png") if not p.stem.endswith(("_flat", "_gult")))
    if not hd:
        print(f"Fant ikke bilde {nr} i {m / 'bilder'}")
        return 1
    hd = hd[0]
    x, y = max(0, min(319, x)), max(0, min(199, y))
    b, h = max(4, min(320 - x, b)), max(4, min(200 - y, h))
    boks = (x * 4, y * 4, (x + b) * 4, (y + h) * 4)
    deler = [Image.open(hd.with_name(hd.stem + s)).convert("RGB").crop(boks) for s in (".png", "_flat.png", "_gult.png")]
    skala = max(1, min(4, 600 // max(deler[0].width, 1)))
    deler = [d.resize((d.width * skala, d.height * skala), Image.NEAREST) for d in deler]
    ut = Image.new("RGB", (sum(d.width for d in deler) + 20, deler[0].height + 16), (128, 128, 128))
    tegn = ImageDraw.Draw(ut)
    px = 0
    for d, tekst in zip(deler, ("HD", "original", "gult = uten HD")):
        ut.paste(d, (px, 16))
        tegn.text((px + 2, 2), tekst, fill=(255, 255, 255))
        px += d.width + 10
    (m / "funnbilder").mkdir(exist_ok=True)
    fil = m / "funnbilder" / f"{nr:04d}_{navn}.png"
    ut.save(fil)
    print(f"utsnitt: {fil}")
    return 0


def markor(args, k: list[str]) -> int:
    """Høyreklikker til markøren er den som er bedt om (gå, se, hånd, snakk, figur), ett klikk om gangen."""
    m = mappe(args)
    if len(k) < 2 or k[1].lower() not in MARKOR_VALG:
        print("Bruk: tools/styr.py markor gå|se|hånd|snakk|figur")
        return 1
    mal = MARKOR_VALG[k[1].lower()]
    # Over en ting hopper spillet over gå-markøren, så musen må stå på et tomt sted
    kandidater = [(300, 20), (160, 8), (12, 8), (308, 120), (160, 60), (60, 60), (250, 60), (160, 120)]
    kode = send(args, ["kontroll 600"] + [f"pek {x} {y}" for x, y in kandidater], stille=True)
    if kode:
        return kode
    pekt = (les_status(m / "ctl") or {}).get("pekt") or []
    tomme = [(p["x"], p["y"]) for p in pekt if not p.get("nr")]
    x, y = tomme[0] if tomme else kandidater[0]
    for _ in range(7):
        st = les_status(m / "ctl") or {}
        if (st.get("markor_objekt") or {}).get("nr") in mal and st.get("kontroll"):
            break
        kode = send(args, ["kontroll 600", f"flytt {x} {y}", f"hoyreklikk {x} {y}", "vent 4", f"flytt {x} {y}", "vent 3"], stille=True)
        if kode:
            return kode
    st = les_status(m / "ctl") or {}
    nr = (st.get("markor_objekt") or {}).get("nr")
    if nr not in mal:
        print(f"Fikk ikke markøren {k[1]} (står på {nr} {MARKORER.get(nr, '')}). Har du kontrollen, og er inventaret lukket?")
        return 1
    print(f"markør {nr} {MARKORER.get(nr, '')}")
    return 0


def stopp(args) -> int:
    m = mappe(args)
    if not kjorer(m):
        print("Spillet går ikke.")
        return 0
    try:
        tmp = m / "ctl" / "kommando.tmp"
        tmp.write_text(f"id {neste_id(m)}\navslutt\n")
        os.replace(tmp, m / "ctl" / "kommando.txt")
        for _ in range(40):
            if not kjorer(m):
                break
            time.sleep(0.25)
    finally:
        if kjorer(m):
            os.killpg(int((m / "pid").read_text()), signal.SIGTERM)
    print("Spillet er avsluttet.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("--mappe", default=os.environ.get("STYR_MAPPE", str(ROOT / "work" / "gjennomspill")),
                    help="arbeidsmappen (standard work/gjennomspill)")
    # tools/gjennomspill.sh setter STYR_MOTOR og STYR_MOD til kopier, så en ny modd fra natteskiftet ikke river bort filer midt i spillet
    ap.add_argument("--motor", default=os.environ.get("STYR_MOTOR"), help="ScummVM med HD-patchen (standard engine/scummvm/scummvm)")
    ap.add_argument("--spill", default=os.environ.get("STYR_SPILL", str(ROOT / "game")), help="spillfilene")
    ap.add_argument("--mod", default=os.environ.get("STYR_MOD", str(ROOT / "mods" / "gpt")), help="HD-modden")
    ap.add_argument("--slot", type=int, help="med start: lagret spill å starte fra")
    ap.add_argument("kommandoer", nargs="*", help="start, stopp, status, eller kommandoer til spillet")
    args = ap.parse_args()
    k = args.kommandoer
    if not k:
        ap.print_help()
        return 1
    if k[0] == "start":
        return start(args)
    if k[0] == "stopp":
        return stopp(args)
    if k[0] == "utsnitt":
        return utsnitt(args, k)
    if k[0] == "markor":
        return markor(args, k)
    if k[0] == "status" and len(k) == 1:
        st = les_status(mappe(args) / "ctl")
        if not st:
            print("Ingen status ennå.")
            return 1
        skriv_status(st, mappe(args), [])
        return 0
    # "klikk 120 80" som tre ord fra skallet blir én kommando
    samlet, i = [], 0
    while i < len(k):
        if k[i] in ("klikk", "hoyreklikk", "flytt", "pek") and i + 2 < len(k) and k[i + 1].isdigit() and k[i + 2].isdigit():
            samlet.append(" ".join(k[i:i + 3]))
            i += 3
        elif k[i] in ("vent", "kontroll", "last", "klikkting", "hoyreklikkting") and i + 1 < len(k) and k[i + 1].isdigit():
            samlet.append(" ".join(k[i:i + 2]))
            i += 2
        else:
            samlet.append(k[i])
            i += 1
    return send(args, samlet)


if __name__ == "__main__":
    sys.exit(main())
