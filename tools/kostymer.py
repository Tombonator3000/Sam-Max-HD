#!/usr/bin/env python3
"""Kartlegger kostymene i Sam & Max: hvor de brukes, av hvem, og hvor mange figurark de gir.

Leser uttrekket (work/extract: costumes.json, rooms.json og rutene) og de dekompilerte skriptene
(work/skript, fra tools/dekompiler_skript.py). For hvert kostyme:

- rommet det ligger i (hjemrom),
- rommene der skriptene laster eller setter det på en skuespiller (`loadCostume`, `actorOps.setCostume`
  med fast nummer), og hvor mange ganger,
- skuespillerne som får det, og noen replikker de sier i de samme skriptene (hjelp til å finne ut
  hvem figuren er),
- ruter, synlige ruter, animasjoner, største rute og antall figurark med pakkingen i figur.py,
- om paletten i hjemrommet gir andre farger enn paletten i rommet kostymet brukes mest i
  (forslag til docs/kostymefarger.csv).

Skriver work/kostymer/kostymer.csv og kostymer.json, og med --kontaktark et kontaktark per 48
kostymer (største rute i 2x) i work/kostymer/. Skuespiller 2 er Sam (VAR_EGO = 2), 3 er Max.

Med --figurliste oppdateres de beregnede kolonnene i docs/figurer.csv (rom, ruter, ark, skriptbruk og
så videre), mens de som er skrevet for hånd (gruppe, figur, hva, prompt_en, hovedark), beholdes.
Rekkefølgen er gruppe (1 hovedkostymene, 2 andre med Sam og Max, 3 navngitte figurer, 4 resten,
9 rene skygger), så flest ganger i skriptene, så flest ark.

Bruk: .venv/bin/python tools/kostymer.py [--kontaktark] [--figurliste docs/figurer.csv]
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipeline"))

import numpy as np  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

from smhd import figur, gamedata  # noqa: E402

RE_ACTOR = re.compile(r"actorOps\.setCurActor\(([^)]*)\)")
RE_COSTUME = re.compile(r"actorOps\.setCostume\((\d+)\)")
RE_LOAD = re.compile(r"resourceRoutines\.loadCostume\((\d+)\)")
RE_TALK = re.compile(r'talkActor\((?:sound\([^)]*\) \+ )?"(.*)",(\d+)\)\s*$')
RE_EGO = re.compile(r'talkEgo\((?:sound\([^)]*\) \+ )?"(.*)"\)\s*$')


def scan_scripts(skript: Path) -> dict:
    """Går gjennom alle skriptfilene. Gir per kostyme: rom -> antall, skuespillere, replikker."""
    uses: dict[int, Counter] = defaultdict(Counter)        # kostyme -> rom -> antall setCostume
    loads: dict[int, Counter] = defaultdict(Counter)       # kostyme -> rom -> antall loadCostume
    actors: dict[int, Counter] = defaultdict(Counter)      # kostyme -> skuespiller -> antall
    lines: dict[int, list[str]] = defaultdict(list)        # kostyme -> replikker
    files: dict[int, set[str]] = defaultdict(set)
    for f in sorted(skript.rglob("*.txt")):
        rel = f.relative_to(skript)
        m = re.match(r"rom_(\d+)", rel.parts[0])
        room = int(m.group(1)) if m else 0                  # 0: globalt skript
        cur = None
        set_in_file: dict[str, set[int]] = defaultdict(set)
        talk_in_file: dict[str, list[str]] = defaultdict(list)
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            a = RE_ACTOR.search(line)
            if a:
                cur = a.group(1).strip()
                continue
            c = RE_COSTUME.search(line)
            if c:
                cid = int(c.group(1))
                uses[cid][room] += 1
                files[cid].add(str(rel))
                if cur is not None:
                    actors[cid][cur] += 1
                    set_in_file[cur].add(cid)
                continue
            ld = RE_LOAD.search(line)
            if ld:
                cid = int(ld.group(1))
                loads[cid][room] += 1
                files[cid].add(str(rel))
                continue
            t = RE_TALK.search(line)
            if t:
                talk_in_file[t.group(2)].append(t.group(1))
                continue
            e = RE_EGO.search(line)
            if e:
                talk_in_file["2"].append(e.group(1))
        for actor, cids in set_in_file.items():
            if len(cids) == 1 and actor in talk_in_file:
                cid = next(iter(cids))
                for s in talk_in_file[actor]:
                    if len(lines[cid]) < 6 and s not in lines[cid]:
                        lines[cid].append(s)
    return {"uses": uses, "loads": loads, "actors": actors, "lines": lines, "files": files}


def palette_differs(pal_a: bytes, pal_b: bytes, indices: list[int]) -> int:
    """Hvor mange av indeksene (utenom 0 til 15) som har ulik farge i de to palettene."""
    return sum(1 for i in indices if i >= 16 and pal_a[i * 3:i * 3 + 3] != pal_b[i * 3:i * 3 + 3])


def palette_room(home: int, used: Counter, pal: dict[int, bytes], indices: list[int]) -> int:
    """Rommet med paletten kostymet skal vises med: fargene flest av bruksrommene har for kostymets
    indekser (utenom 0 til 15). Hjemrommet når det har de fargene, ellers det mest brukte rommet som har
    dem. Uten bruksrom: hjemrommet."""
    rooms = [r for r in used if r and r in pal]
    idx = sorted({i for i in indices if i >= 16})
    if not rooms or not idx or home not in pal:
        return home
    # Hjemrommet vinner når stemmene står likt (et kostyme brukt like mye i to rom)
    weight = Counter({r: used[r] + (0.5 if r == home else 0) for r in rooms})
    majority = {}
    for i in idx:
        votes = Counter()
        for r in rooms:
            votes[pal[r][i * 3:i * 3 + 3]] += weight[r]
        majority[i] = votes.most_common(1)[0][0]

    def fits(r: int) -> bool:
        return all(pal[r][i * 3:i * 3 + 3] == majority[i] for i in idx)

    if fits(home):
        return home
    for r, _ in weight.most_common():
        if fits(r):
            return r
    return weight.most_common(1)[0][0]


FIGURE_FIELDS = ["rekkefolge", "kostyme", "gruppe", "figur", "hva", "prompt_en", "hovedark", "rom", "romnavn", "palettrom",
                 "kodek", "ruter", "synlige_ruter", "retninger", "animasjoner", "storste_rute", "ark", "jobber",
                 "store_ruter", "skript_ganger", "skript_rom", "skyggeruter", "ugyldige_ruter", "tegnet_i_romtest"]
MANUAL = ("gruppe", "figur", "hva", "prompt_en", "hovedark", "tegnet_i_romtest")


def write_figure_list(path: Path, rows: list[dict], meta: dict, extract: Path, room_names: dict[int, str]) -> int:
    """Oppdaterer docs/figurer.csv: beregnede kolonner fra rows, håndskrevne fra filen som finnes."""
    old = {}
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            old = {int(r["kostyme"]): r for r in csv.DictReader(f) if (r.get("kostyme") or "").strip().isdigit()}
    out = []
    for r in rows:
        cid = r["kostyme"]
        info = meta[cid]
        shadow = invalid = 0
        for c in info["cels"]:
            if not figur.valid_cel(c):
                invalid += 1
                continue
            name = f"costume{cid:03d}_{c['cel']:03d}"
            p = extract / "costumes" / f"{name}.png"
            if p.exists():
                with Image.open(p) as im:
                    a = np.asarray(im.convert("RGBA"))
                vis = a[..., 3] > 0
                if vis.any() and figur.shadow_mask(extract, name, a).sum() == vis.sum():
                    shadow += 1
        keep = {k: (old.get(cid, {}).get(k) or "") for k in MANUAL}
        used = (info.get("colours") or {}).get("room", r["rom"])   # paletten uttrekket faktisk brukte
        home_name = "felles kostymer (rom 1)" if r["rom"] == 1 else room_names.get(r["rom"], "")
        out.append({**keep, "kostyme": cid, "rom": r["rom"], "romnavn": home_name,
                    "palettrom": used if used != r["rom"] else "", "kodek": r["format"],
                    "ruter": r["ruter"], "synlige_ruter": r["synlige_ruter"], "retninger": info.get("retninger", 4),
                    "animasjoner": r["animasjoner"], "storste_rute": r["storste_rute"], "ark": r["ark"],
                    "jobber": r["jobber"], "store_ruter": r["store_ruter"], "skript_ganger": r["skript_ganger"],
                    "skript_rom": r["skript_rom"], "skyggeruter": shadow, "ugyldige_ruter": invalid})
    out.sort(key=lambda x: (int(x["gruppe"] or 4), -int(x["skript_ganger"]), -int(x["ark"]), x["kostyme"]))
    for n, x in enumerate(out, 1):
        x["rekkefolge"] = n
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIGURE_FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    return len(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--extract", default=str(ROOT / "work" / "extract"))
    ap.add_argument("--skript", default=str(ROOT / "work" / "skript"))
    ap.add_argument("--game", default=str(ROOT / "game"))
    ap.add_argument("--ut", default=str(ROOT / "work" / "kostymer"))
    ap.add_argument("--kontaktark", action="store_true")
    ap.add_argument("--figurliste", help="oppdater denne figurlisten (docs/figurer.csv)")
    ap.add_argument("--romliste", default=str(ROOT / "docs" / "rom-oversikt.csv"), help="romnavnene")
    a = ap.parse_args()
    extract, out = Path(a.extract), Path(a.ut)
    out.mkdir(parents=True, exist_ok=True)
    meta = {int(k): v for k, v in json.loads((extract / "costumes.json").read_text()).items()}
    scan = scan_scripts(Path(a.skript))
    rooms = gamedata.read_rooms(Path(a.game) / "SAMNMAX.001")
    pal = {n: r.palettes[0] for n, r in rooms.items() if r.palettes}

    rows = []
    for cid in sorted(meta):
        info = meta[cid]
        boxes = figur.cel_boxes(extract, cid, info)
        sheets = figur.plan_sheets(figur.groups_of(info, boxes))
        visible = {c: b for c, b in boxes.items() if b}
        big = max(info["cels"], key=lambda c: c["w"] * c["h"], default=None)
        used = scan["uses"][cid] + scan["loads"][cid]
        script_rooms = sorted(r for r in used if r)
        home = info["room"]
        # Rommet der kostymet brukes mest (fast nummer i skriptene), hjemrommet hvis det er med
        main_room = home
        if script_rooms and home not in script_rooms:
            main_room = max(script_rooms, key=lambda r: (used[r], -r))
        # Paletten kostymet vises med: fargene flertallet av bruksrommene har
        colour_room = palette_room(home, used, pal, info["kostymepalett"])
        diff = 0
        if colour_room != home and colour_room in pal and home in pal:
            diff = palette_differs(pal[home], pal[colour_room], info["kostymepalett"])
        rows.append({
            "kostyme": cid, "rom": home, "format": info["format"], "ruter": len(info["cels"]),
            "synlige_ruter": len(visible), "animasjoner": len(info.get("animasjoner", [])),
            "storste_rute": f"{big['w']}x{big['h']}" if big else "",
            "ark": len(sheets), "jobber": sum(len(figur.gpt.plan_tiles(*s.size)) for s in sheets),
            "store_ruter": sum(s.stor for s in sheets),
            "skript_ganger": sum(scan["uses"][cid].values()),
            "skript_rom": " ".join(str(r) for r in script_rooms) + (" globalt" if used.get(0) else ""),
            "skuespillere": " ".join(f"{k}:{v}" for k, v in scan["actors"][cid].most_common(4)),
            "bruksrom": main_room, "palettrom": colour_room, "palettavvik": diff,
            "farger": " ".join(str(i) for i in sorted(set(info["kostymepalett"]))),
            "replikker": " | ".join(scan["lines"][cid][:4]),
        })
    fields = list(rows[0])
    with (out / "kostymer.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (out / "kostymer.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    n_sheets = sum(r["ark"] for r in rows)
    print(f"{len(rows)} kostymer, {sum(r['synlige_ruter'] for r in rows)} synlige ruter, {n_sheets} figurark. "
          f"Brukt i skript med fast nummer: {sum(1 for r in rows if r['skript_rom'])}. "
          f"Palett i hjemrommet avviker fra bruksrommet: {sum(1 for r in rows if r['palettavvik'])}. -> {out}")

    if a.figurliste:
        names = {}
        if Path(a.romliste).exists():
            with Path(a.romliste).open(newline="", encoding="utf-8") as f:
                names = {int(r["rom"]): r.get("navn", "") for r in csv.DictReader(f)}
        n = write_figure_list(Path(a.figurliste), rows, meta, extract, names)
        print(f"Figurlisten oppdatert: {n} kostymer -> {a.figurliste}")

    if a.kontaktark:
        per = 48
        for start in range(0, len(rows), per):
            part = rows[start:start + per]
            tiles = []
            for r in part:
                cid = r["kostyme"]
                info = meta[cid]
                best = None
                for c in info["cels"]:
                    p = extract / "costumes" / f"costume{cid:03d}_{c['cel']:03d}.png"
                    if p.exists() and (best is None or c["w"] * c["h"] > best[1]):
                        best = (p, c["w"] * c["h"])
                im = Image.open(best[0]).convert("RGBA") if best else Image.new("RGBA", (8, 8))
                s = 2 if max(im.size) <= 120 else 1
                im = im.resize((im.width * s, im.height * s), Image.NEAREST)
                tiles.append((f"{cid} r{r['rom']} a{r['ark']} {r['storste_rute']}", im))
            cw, ch = 250, 260
            sheet = Image.new("RGB", (cw * 8, ch * ((len(tiles) + 7) // 8)), (110, 110, 120))
            d = ImageDraw.Draw(sheet)
            for i, (label, im) in enumerate(tiles):
                x, y = (i % 8) * cw, (i // 8) * ch
                im.thumbnail((cw - 8, ch - 20))
                sheet.paste(im, (x + 4, y + 16), im)
                d.text((x + 4, y + 2), label, fill=(255, 255, 0))
            dest = out / f"kontakt_{part[0]['kostyme']:03d}-{part[-1]['kostyme']:03d}.png"
            sheet.save(dest)
            print(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
