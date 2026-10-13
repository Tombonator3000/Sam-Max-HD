"""Figurark: animasjonsrutene i et kostyme pakket på ett lerret til ChatGPT, og kontrollen av dem.

Å male hver kostymerute for seg gir for mange jobber, og figurene flimrer fordi hver rute blir
tegnet litt ulikt. Her pakkes rutene som hører sammen, på figurark (jobb-ID figCCC_KK: kostyme
CCC, ark KK). Arket er 4x på det vanlige lerretet (1536 x 1024 med grå kant), og rutene står på
en flat bakgrunnsfarge som ikke finnes i kostymet, med god avstand mellom dem. ChatGPT maler hele
arket på en gang, og rutene klippes ut igjen etter posisjon med gjennomsiktigheten fra originalen.

Rekkefølgen kommer fra animasjonene i kostymet (costumes.json; for COST i v6 leser eksport_v6.py dem): først
stående i alle retninger (som et modellark), så gange mot høyre og venstre, snakking, gange i de andre
retningene, og til slutt resten. Ruter i samme animasjon og retning står etter hverandre på
samme rad, og en animasjon deles ikke mellom ark når den får plass på et tomt ark. Ruter som
ikke får plass på et ark i 4x, blir egne jobber i stedet for å skaleres ned, og er de bredere
eller høyere enn lerretet, deles de som rommene.

Kontrollen i gpt-inn: arket som helhet (plassering, som rommene), hver rute for seg (mangler,
omriss og kantlikhet inne i omrisset), og flimmer: nabo-ruter i samme animasjon skal ikke skille
seg mer fra hverandre i HD enn originalrutene gjør. Ark i glatt stil med ekte alfa tas inn av myk.py.

Sam & Max (13. oktober 2026):
- Skyggepiksler (palettindeks 13, som ScummVM tegner gjennom skyggetabellen) står ikke på arkene. Rene
  skyggekostymer får ingen ark; motoren tegner skyggen selv.
- Ruter større enn MAX_CEL (to skjermer) er feil i dataene: animasjoner som peker utenfor kostymet, og
  som dekoderen leser som tilfeldige ruter. De males ikke.
- Kostymer med en hovedperson (kolonnen hovedark i docs/figurer.csv) får det godkjente hovedarket
  (hovedark/<navn>.png) som bilde to på alle arkene, så figuren blir lik på tvers av kostymene.
- Prompten sier hvor store rutene er i referansen, og at hver rute skal holde den størrelsen.
"""
from __future__ import annotations

import csv
import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

from . import gpt

FIG_SHEET = (352, 240)       # arket i originalpiksler, midt på lerretet (384 x 256) med grå kant rundt
FIG_MARGIN = 4               # originalpiksler fra arkets kant til rutene
FIG_PAD = 8                  # originalpiksler mellom rutene (32 HD-piksler)
FIG_PILOT: dict[int, int] = {2: 1, 3: 1}  # kostyme: antall ark i stilpiloten (Sam og Max, første ark)
MAX_CEL = (640, 400)         # ruter større enn dette er feil i dataene og males ikke (i Sam & Max 4163 til 6189
                             # piksler brede eller 4924 til 5257 høye; ekte ruter er høyst 320 x 200)
SHADOW_INDEX = 13            # palettindeks som tegnes gjennom skyggetabellen (base-costume.cpp, pcolor == 13)
MAIN_FIGURES = {"sam": "Sam", "max": "Max"}  # hovedark: navn i filnavnet og i prompten
# Bakgrunnsfarger å velge mellom. Den som ligger lengst fra alle fargene i kostymet, brukes.
FIG_BACKGROUNDS = gpt.SHEET_BACKGROUNDS

# Kontroll per rute og flimmer. Grensene er satt med kunstige ark og justeres etter ekte leveranser.
FIG_MIN_PIXELS = 40          # ruter med færre synlige piksler kontrolleres ikke enkeltvis
FIG_COVER = 0.5              # under denne andelen av rutens piksler malt som figur: ruten mangler
FIG_OUTLINE = 0.80           # overlapp (snitt / union) mellom omrisset i HD og i originalen, i 4x
FIG_EDGES = gpt.OBJ_EDGES    # kantlikhet inne i omrisset, for ruter med tydelige kanter
FIG_REDRAWN_EDGE = gpt.OBJ_REDRAWN_EDGE
FIG_ALIGN = 6                # originalpiksler å lete i når to nabo-ruter legges over hverandre
FIG_FLICKER = 30.0           # flimmer: største ekstra forskjell mellom nabo-ruter i HD (0 til 255)
FIG_FLICKER_MIN = 20         # nabo-ruter med færre felles piksler sammenlignes ikke
FIG_BLEED = 0.12             # utklipp: HD-piksler så langt mot bakgrunnsfargen fylles innenfra (clean_edges)
FIG_BLEED_BAND = 8           # bare så mange HD-piksler (2 originalpiksler) innenfor omrisset

# Retninger: 8 (simple dir i ScummVM: 0 nord, 2 øst, 4 sør, 6 vest) eller 4 (gamle: 0 vest, 1 øst,
# 2 sør, 3 nord). Rekkefølgen på arkene: høyre, venstre, mot oss, bort, så de skrå.
DIR_ORDER = {8: [2, 6, 4, 0, 3, 5, 1, 7], 4: [1, 0, 2, 3]}
DIR_NO = {8: {0: "bort", 1: "bort mot høyre", 2: "mot høyre", 3: "mot oss til høyre", 4: "mot oss",
              5: "mot oss til venstre", 6: "mot venstre", 7: "bort mot venstre"},
          4: {0: "mot venstre", 1: "mot høyre", 2: "mot oss", 3: "bort"}}
DIR_EN = {8: {0: "away from the viewer", 1: "away to the right", 2: "right", 3: "toward the viewer to the right",
              4: "toward the viewer", 5: "toward the viewer to the left", 6: "left", 7: "away to the left"},
          4: {0: "left", 1: "right", 2: "toward the viewer", 3: "away from the viewer"}}
ANIM_NO = {1: "start", 2: "gange", 3: "stående", 4: "snakking", 5: "slutt på snakking"}
ANIM_EN = {1: "start pose", 2: "walking", 3: "standing", 4: "talking", 5: "end of talking"}

PROMPT_FIGURE = """Task: faithful HD remaster of a sheet of animation frames from the 1993 adventure game Sam & Max Hit the Road (LucasArts). This is a production asset. Every frame replaces one original frame in the game, at the same size and position, and the frames are played one after another.

Input: the attached image is the original low-resolution sheet enlarged exactly 4x with hard pixel edges. The frames stand apart on a plain flat {color} background ({hex}). Around the sheet is a plain gray (#808080) border. The background and the border are only padding.

What the sheet shows: {who}. The description is only a help; the input image decides. On this sheet, row by row from left to right: {content}.

Size rule (most important): draw every frame at exactly the size it has in the input, with the same height, the same width and the same proportions of head, body, arms, legs and props. One input pixel is 4 output pixels for every frame on this sheet and on every other sheet of this character, so the character never grows, shrinks or changes shape between frames. {sizes}

Do:
- Repaint every frame in high resolution with clean, natural detail: smooth shading instead of dithering, smooth anti-aliased outlines (no pixel steps), in the bold-outlined cartoon style of the original.
- Keep the original design: the same character, the same colors, light direction, shadows and contrast as in the input.
- Make all frames look identical apart from the pose: the same face, eyes, hat, clothes, colors and light in every frame. Any difference between frames flickers in the game.
- Keep the pose and silhouette of every frame, and keep each frame in its place on the sheet, in the same rows and the same order.
- Glowing effects (light, lightning, sparks, fire) are painted as soft glow that fades into transparency.

Do not:
- Do not add, remove, merge, split or redesign frames.
- Do not add anything that is not in the input: no new props, accessories, patterns, logos, text, shadows, floor, numbers, labels, frames or grid lines.
- Do not change colors, clothes or proportions, and do not make heads, hands or eyes bigger than in the input.
- Some frames show only part of the character (a body without a head, a head alone, an arm), because the game draws the parts separately. Paint them as they are and do not complete them.
- Do not let frames touch or overlap each other.
- No photorealism, no modern 3D look, no film grain, no vignette, no watermark, no signature.

Output: one PNG image, exactly 1536 x 1024 pixels, with a fully transparent background (real alpha: no background color and no gray border) and every frame in the same place as in the input. Before delivering, run python3 verktoy/sjekk_leveranse.py jobber/{job}/resultat.png and redo the frames it reports as too big, too small, moved or missing. List the delivery with its sha256 in the fremdrift.json of your report and add a rutekart (the box around each frame's drawing, alpha above 128)."""

PROMPT_FIGURE_STYLE = """If a second image is attached, it is the approved master sheet (hovedark) of this character, or an already approved HD sheet of the same character, or an approved HD picture from the same game. Paint the character exactly as in that image: the same face, hair, clothes, colors and level of detail. Take every pose, size and position from the first image. If a third image is attached, it is the master sheet of the second character on the sheet."""

PROMPT_FIGURE_PART = """This is part {part} of {parts} of one large frame. The other parts are made separately and joined afterwards, so keep the edges of the picture natural, with no vignette, frame or fading."""

FIG_RETRY = ("Precise correction of the attached sheet. Some animation frames did not match the original: they were "
             "missing, had a different outline or were painted differently. Start again from referanse.png. Keep every "
             "frame exactly where it is, with exactly the same outline and size, and paint every frame the same way: "
             "the same face, hair, clothes, colors and light. Keep the background plain and flat. Do not zoom, shift, "
             "crop or reframe. Keep the gray border plain gray. Same size 1536 x 1024.")

FIG_FLICKER_RETRY = ("Precise correction of the attached sheet. The frames are in the right place, but some of them are "
                     "painted differently from the frames next to them (face, hair, clothes, colors or light), so the "
                     "animation flickers in the game. Start again from referanse.png and paint all frames as the same "
                     "person in the same light. Only the pose may differ, exactly as in the input. Keep every outline "
                     "and position. Same size 1536 x 1024 with the plain gray border.")


# ---------------------------------------------------------------- liste over kostymene

def read_figure_list(path: Path | None) -> dict[int, dict]:
    """docs/figurer.csv: kostyme -> {"figur", "rekkefolge", "prompt_en", "hovedark"}. Rekkefølgen er hvor mye
    kostymet vises. prompt_en er en kort engelsk beskrivelse til prompten, hovedark navnene på hovedarkene
    (sam, max eller sam+max) som legges ved som bilde to og tre."""
    if not path or not Path(path).exists():
        return {}
    out = {}
    with Path(path).open(newline="", encoding="utf-8") as f:
        for n, row in enumerate(csv.DictReader(f)):
            cid = (row.get("kostyme") or "").strip()
            if cid.isdigit():
                rank = (row.get("rekkefolge") or "").strip()
                masters = [m.strip().lower() for m in (row.get("hovedark") or "").split("+") if m.strip()]
                out[int(cid)] = {"figur": (row.get("figur") or "").strip(),
                                 "rekkefolge": int(rank) if rank.isdigit() else n + 1,
                                 "prompt_en": (row.get("prompt_en") or "").strip(),
                                 "hovedark": [m for m in masters if m in MAIN_FIGURES]}
    return out


def select_costumes(arg, meta: dict[int, dict], names: dict[int, dict]) -> tuple[list[int], bool]:
    """Kostymene figurark skal lages for, i rekkefølgen fra figurer.csv, og om bare piloten skal med.

    arg: "pilot" (standard), "alle", "ingen", eller et sett kostyme-ID-er.
    """
    if arg in (None, "ingen") or arg == set():
        return [], False
    if arg == "pilot":
        return [c for c in FIG_PILOT if c in meta], True
    ids = list(meta) if arg == "alle" else [c for c in arg if c in meta]
    return sorted(ids, key=lambda c: (names.get(c, {}).get("rekkefolge", 10 ** 6), c)), False


# ---------------------------------------------------------------- planlegging

@dataclass
class Cel:
    rute: int
    w: int
    h: int
    box: tuple[int, int, int, int]                 # synlige piksler (x0, y0, x1, y1) i ruten
    animasjon: int | None = None
    retning: int | None = None
    lag: int | None = None
    nr: int = 0                                    # plass i animasjonen (for flimmerkontrollen)

    @property
    def vw(self) -> int:
        return self.box[2] - self.box[0]

    @property
    def vh(self) -> int:
        return self.box[3] - self.box[1]


@dataclass
class Sheet:
    size: tuple[int, int]
    cels: list[tuple[Cel, int, int]] = field(default_factory=list)   # rute og hjørnet til hele ruten på arket
    stor: bool = False                                                # egen jobb for én stor rute


def _rank(a: dict, dirs: int) -> tuple:
    """Rekkefølgen animasjonene pakkes i: stående i alle retninger, gange mot høyre og venstre,
    snakking, gange i de andre retningene, slutt på snakking, og så resten etter nummer."""
    order = DIR_ORDER.get(dirs, DIR_ORDER[4])
    d = order.index(a["retning"]) if a["retning"] in order else len(order)
    anim, lag = a["animasjon"], a["lag"]
    if anim in (1, 3):
        return (0, lag, anim != 3, d)
    if anim == 2 and d < 2:
        return (1, d, lag)
    if anim == 4:
        return (2, d, lag)
    if anim == 2:
        return (3, d, lag)
    if anim == 5:
        return (4, d, lag)
    return (5, anim, d, lag)


def groups_of(info: dict, boxes: dict[int, tuple[int, int, int, int] | None]) -> list[list[Cel]]:
    """Rutene i et kostyme gruppert etter animasjon, retning og lag, i pakkerekkefølge.

    Hver rute er med én gang, i den første gruppen den hører til. Ruter uten synlige piksler er
    ikke med. Ruter som ingen animasjon viser, kommer til slutt.
    """
    sizes = {c["cel"]: (c["w"], c["h"]) for c in info["cels"]}
    dirs = info.get("retninger", 4)
    taken: set[int] = set()
    out: list[list[Cel]] = []
    for a in sorted(info.get("animasjoner", []), key=lambda a: _rank(a, dirs)):
        group = []
        for c in a["ruter"]:
            if c in taken or c not in sizes or not boxes.get(c):
                continue
            taken.add(c)
            group.append(Cel(c, *sizes[c], boxes[c], a["animasjon"], a["retning"], a["lag"], len(group)))
        if group:
            out.append(group)
    rest = [Cel(c, *sizes[c], boxes[c], nr=i) for i, c in enumerate(c for c in sizes if c not in taken and boxes.get(c))]
    if rest:
        out.append(rest)
    return out


def _is_big(c: Cel) -> bool:
    return c.vw + 2 * FIG_MARGIN > FIG_SHEET[0] or c.vh + 2 * FIG_MARGIN > FIG_SHEET[1]


class _Shelf:
    """Ruter på rader: venstre mot høyre, nederst på raden (føttene på en linje)."""

    def __init__(self):
        self.rows: list[dict] = []

    def copy(self) -> "_Shelf":
        s = _Shelf()
        s.rows = [{**r, "items": list(r["items"])} for r in self.rows]
        return s

    def place(self, c: Cel, new_row: bool) -> bool:
        W, H = FIG_SHEET
        row = self.rows[-1] if self.rows else None
        if row and not new_row and row["x"] + c.vw + FIG_MARGIN <= W and row["y"] + max(row["h"], c.vh) + FIG_MARGIN <= H:
            row["items"].append((c, row["x"]))
            row["x"] += c.vw + FIG_PAD
            row["h"] = max(row["h"], c.vh)
            return True
        y = row["y"] + row["h"] + FIG_PAD if row else FIG_MARGIN
        if FIG_MARGIN + c.vw + FIG_MARGIN > W or y + c.vh + FIG_MARGIN > H:
            return False
        self.rows.append({"y": y, "h": c.vh, "x": FIG_MARGIN + c.vw + FIG_PAD, "items": [(c, FIG_MARGIN)]})
        return True

    def place_group(self, group: list[Cel], new_row: bool) -> bool:
        for i, c in enumerate(group):
            if not self.place(c, new_row and i == 0):
                return False
        return True

    def sheet(self) -> Sheet:
        s = Sheet(FIG_SHEET)
        for r in self.rows:
            for c, x in r["items"]:
                # hjørnet til hele ruten, så de synlige pikslene står nederst på raden
                s.cels.append((c, x - c.box[0], r["y"] + r["h"] - c.vh - c.box[1]))
        return s


def plan_sheets(groups: list[list[Cel]]) -> list[Sheet]:
    """Pakker gruppene på ark i rekkefølge.

    En gruppe med flere ruter (en animasjon) starter på ny rad. Grupper med én rute i samme
    animasjon og lag (stående i hver retning) står etter hverandre på samme rad. Får ikke en
    gruppe plass på resten av arket, men på et tomt ark, starter den et nytt ark. Ellers fylles
    arket og gruppen fortsetter på neste. Store ruter blir egne ark (egne jobber).
    """
    sheets: list[Sheet | _Shelf] = []
    cur: _Shelf | None = None
    prev_key = None
    for group in groups:
        key = (group[0].animasjon, group[0].lag)
        new_row = len(group) > 1 or key != prev_key
        prev_key = key
        small = [c for c in group if not _is_big(c)]
        if cur is not None and cur.rows and small and not cur.copy().place_group(small, new_row) \
                and _Shelf().place_group(small, True):
            cur = None
        first = True
        for c in group:
            if _is_big(c):
                M = FIG_MARGIN
                sheets.append(Sheet((c.vw + 2 * M, c.vh + 2 * M), [(c, M - c.box[0], M - c.box[1])], stor=True))
                continue
            if cur is None:
                cur = _Shelf()
                sheets.append(cur)
            if not cur.place(c, new_row and first):
                cur = _Shelf()
                sheets.append(cur)
                cur.place(c, True)
            first = False
    return [s.sheet() if isinstance(s, _Shelf) else s for s in sheets]


def shadow_mask(extract: Path, name: str, rgba: np.ndarray) -> np.ndarray:
    """Skyggepikslene i en rute: palettindeks SHADOW_INDEX i indeksbildet (name_idx.png). Uten indeksbilde:
    fargen ScummVM-paletten har for indeks 13 (255, 87, 255) og nære farger, som myk.technical."""
    idx_path = extract / "costumes" / f"{name}_idx.png"
    visible = rgba[..., 3] > 0
    if idx_path.exists():
        with Image.open(idx_path) as im:
            idx = np.asarray(im)
        if idx.shape == visible.shape:
            return visible & (idx == SHADOW_INDEX)
    r, g, b = (rgba[..., k].astype(np.int16) for k in range(3))
    return visible & (r >= 230) & (b >= 230) & (g <= 120)


def cel_rgba(extract: Path, name: str) -> Image.Image | None:
    """Ruten (costumeCCC_NNN) som RGBA uten skyggepiksler, slik den står på figurarket. None når filen mangler."""
    p = extract / "costumes" / f"{name}.png"
    if not p.exists():
        return None
    with Image.open(p) as im:
        a = np.asarray(im.convert("RGBA")).copy()
    a[shadow_mask(extract, name, a)] = 0
    return Image.fromarray(a, "RGBA")


def valid_cel(c: dict) -> bool:
    """Ruter større enn MAX_CEL er feil i dataene."""
    return 0 < c["w"] <= MAX_CEL[0] and 0 < c["h"] <= MAX_CEL[1]


def cel_boxes(extract: Path, cid: int, info: dict) -> dict[int, tuple[int, int, int, int] | None]:
    """De synlige pikslene i hver rute, uten skyggepiksler (None for helt gjennomsiktige ruter, rene
    skyggeruter og ugyldige ruter)."""
    out = {}
    for c in info["cels"]:
        im = cel_rgba(extract, f"costume{cid:03d}_{c['cel']:03d}") if valid_cel(c) else None
        out[c["cel"]] = im.getchannel("A").getbbox() if im is not None else None
    return out


def costume_colours(extract: Path, cid: int, info: dict) -> np.ndarray:
    """Alle fargene (N x 3) i de synlige pikslene i rutene til et kostyme."""
    colours: set[tuple[int, int, int]] = set()
    for c in info["cels"]:
        im = cel_rgba(extract, f"costume{cid:03d}_{c['cel']:03d}") if valid_cel(c) else None
        if im is not None:
            a = np.asarray(im)
            colours |= set(map(tuple, np.unique(a[a[..., 3] > 0][:, :3], axis=0).tolist()))
    return np.array(sorted(colours), dtype=np.float64).reshape(-1, 3)


def background_for(extract: Path, cid: int, info: dict, colours: np.ndarray | None = None
                   ) -> tuple[tuple[int, int, int], str, float]:
    """Bakgrunnsfargen for arkene til et kostyme: den i FIG_BACKGROUNDS som ligger lengst fra alle
    fargene i rutene. Gir fargen, navnet og avstanden til nærmeste farge i kostymet."""
    arr = costume_colours(extract, cid, info) if colours is None else colours
    if not len(arr):
        return FIG_BACKGROUNDS[0][0], FIG_BACKGROUNDS[0][1], 255.0
    best = max(FIG_BACKGROUNDS, key=lambda b: np.linalg.norm(arr - b[0], axis=1).min())
    return best[0], best[1], float(np.linalg.norm(arr - best[0], axis=1).min())


def has_markers(colours: np.ndarray) -> bool:
    """Om kostymet har lyse magenta skyggemerker (i The Dig hadde for eksempel Boston Low 255, 87, 255), som
    prompten må forklare."""
    if not len(colours):
        return False
    r, g, b = colours[:, 0], colours[:, 1], colours[:, 2]
    return bool(((r >= 200) & (b >= 200) & (g <= 140)).any())


def sheet_image(extract: Path, cid: int, sheet: Sheet, bg: tuple[int, int, int]) -> Image.Image:
    """Arket i originalpiksler: rutene uten skyggepiksler på den flate bakgrunnsfargen."""
    image = Image.new("RGBA", sheet.size, (*bg, 255))
    for c, x, y in sheet.cels:
        im = cel_rgba(extract, f"costume{cid:03d}_{c.rute:03d}")
        if im is not None:
            gpt._paste_over(image, im, x, y)
    return image.convert("RGB")


def main_limb(info: dict, boxes: dict[int, tuple[int, int, int, int] | None]) -> int | None:
    """Laget med mest synlig tegning i kostymet (kroppen). I The Dig (AKOS) var det lag 0; i Sam & Max
    (klassiske kostymer) er det oftest lag 1. De andre lagene beskrives som egne deler."""
    area: dict[int, int] = {}
    for c in info["cels"]:
        b = boxes.get(c["cel"])
        if b:
            area[c.get("lag", 0)] = area.get(c.get("lag", 0), 0) + (b[2] - b[0]) * (b[3] - b[1])
    return max(area, key=lambda k: (area[k], -k)) if area else None


def _describe(cels: list[dict], dirs: int, english: bool, main: int | None = 0) -> str:
    """Hva som står på arket: animasjonene i rekkefølge, med retninger og antall ruter. main er laget med
    kroppen; ruter i andre lag beskrives som egne deler."""
    anim_names, dir_names = (ANIM_EN, DIR_EN) if english else (ANIM_NO, DIR_NO)
    dn = dir_names.get(dirs, dir_names[4])
    parts: list[list] = []                       # [animasjon, lag, [retninger], antall]
    for c in cels:
        key = (c.get("animasjon"), c.get("lag"))
        if parts and (parts[-1][0], parts[-1][1]) == key:
            if c.get("retning") not in parts[-1][2]:
                parts[-1][2].append(c.get("retning"))
            parts[-1][3] += 1
        else:
            parts.append([key[0], key[1], [c.get("retning")], 1])
    out = []
    for anim, lag, ds, n in parts:
        if anim is None:
            out.append(f"other frames ({n})" if english else f"andre ruter ({n})")
            continue
        name = anim_names.get(anim, f"animation {anim}" if english else f"animasjon {anim}")
        if lag is not None and lag != main:
            name += " (a separate part the game draws on top of the body, such as the head)" if english else \
                f" (lag {lag}, tegnes over kroppen)"
        where = ", ".join(dn.get(d, str(d)) for d in ds if d is not None)
        if len(ds) == dirs and len(ds) > 2 and n == len(ds):
            where = f"in all {dirs} directions" if english else f"i alle {dirs} retninger"
            out.append(f"{name}, {where} ({n} frames, in this order: " + ", ".join(dn[d] for d in ds) + ")"
                       if english else f"{name} {where} ({n} ruter i rekkefølgen " + ", ".join(dn[d] for d in ds) + ")")
            continue
        if english:
            out.append(f"{name}, facing {where} ({n} {'frame' if n == 1 else 'frames'})" if where else f"{name} ({n})")
        else:
            out.append(f"{name} {where} ({n} {'rute' if n == 1 else 'ruter'})" if where else f"{name} ({n})")
    return "; ".join(out)


MAIN_CHARACTERS = ("Sam", "Max")  # navnene må stå i figurlisten (docs/figurer.csv) for å bli brukt


def _who(label: str, description: str = "") -> str:
    """Hva arket viser, til den engelske prompten: beskrivelsen i figurlisten (prompt_en) når den finnes,
    ellers hovedpersonenes navn fra figurlisten, ellers en nøytral setning."""
    if description:
        return description
    people = [n for n in MAIN_CHARACTERS if n in label]
    if len(people) == 1:
        return f"animation frames of the same character ({people[0]})"
    if people:
        return f"animation frames of the same characters ({', '.join(people[:-1])} and {people[-1]}), as one scene"
    return "animation frames of one costume in the game (a character, an object or an effect)"


def size_text(cels: list[dict]) -> str:
    """Hvor store rutene på arket er i referansen (synlige piksler, 4x), til prompten."""
    ws = [(c["synlig"][2] - c["synlig"][0]) * gpt.SCALE for c in cels]
    hs = [(c["synlig"][3] - c["synlig"][1]) * gpt.SCALE for c in cels]
    if not ws:
        return ""
    if len(cels) == 1:
        return f"The frame on this sheet is {ws[0]} x {hs[0]} pixels in the input (the box around its visible pixels)."
    return (f"On this sheet the frames are from {min(hs)} to {max(hs)} pixels tall and from {min(ws)} to {max(ws)} "
            "pixels wide in the input (the box around each frame's visible pixels); jobb.json lists every frame's box "
            "under ruter (synlig, in original pixels: multiply by 4).")


def figure_prompt(who: str, bg: tuple[int, int, int], colour: str, content: str, part: int, parts: int,
                  note: str | None, markers: bool = False, sizes: str = "", job: str = "<jobb>") -> str:
    """Prompten til et figurark. markers er med for eldre kall; skyggepikslene står ikke på arkene lenger."""
    prompt = PROMPT_FIGURE.format(color=colour, hex="#%02X%02X%02X" % bg, who=who, content=content,
                                  sizes=sizes, job=job)
    if note:
        prompt += "\n\nNote for this character: " + note
    if parts > 1:
        prompt += "\n\n" + PROMPT_FIGURE_PART.format(part=part, parts=parts)
    return prompt + "\n\n" + PROMPT_FIGURE_STYLE


def master_refs(entry: dict) -> list[str]:
    """Hovedarkene for et kostyme (hovedark/sam.png og så videre), i rekkefølgen i figurlisten."""
    return [f"hovedark/{m}.png" for m in entry.get("hovedark", [])]


def figure_jobs(extract: Path, jobs_dir: Path, costumes: list[int], meta: dict[int, dict], names: dict[int, dict],
                rooms_meta: dict, notes: dict, style_ref: Path | None, pilot_only: bool) -> list[gpt.Job]:
    """Figurjobbene (figCCC_KK) for kostymene, i rekkefølge. Med pilot_only bare arkene i FIG_PILOT.

    Bilde to: hovedarket for kostymer med en hovedperson (alle arkene), ellers stilankeret for ark 01 og
    det godkjente ark 01 for de andre arkene. Står i bilde_to og referanser i jobb.json.
    """
    jobs: list[gpt.Job] = []
    for cid in costumes:
        info = meta[cid]
        boxes = cel_boxes(extract, cid, info)
        groups = groups_of(info, boxes)
        sheets = plan_sheets(groups)
        if pilot_only:
            sheets = sheets[:FIG_PILOT.get(cid, 0)]
        if not sheets:
            continue
        main = main_limb(info, boxes)
        # Uten egne venstreruter speilvender motoren ruten mot høyre (costume.cpp, _drawActorToRight)
        mirrored = info.get("speil") is False and info.get("retninger", 4) == 4
        colours = costume_colours(extract, cid, info)
        bg, colour, _ = background_for(extract, cid, info, colours)
        entry = names.get(cid, {})
        name = entry.get("figur") or f"kostyme {cid}"
        who = _who(name, entry.get("prompt_en", ""))
        masters = master_refs(entry)
        dirs = info.get("retninger", 4)
        home = info.get("room", 0)
        first_job = None
        for k, sheet in enumerate(sheets, 1):
            image = sheet_image(extract, cid, sheet, bg)
            cels = [{"bilde": f"costume{cid:03d}_{c.rute:03d}", "kostyme": cid, "rute": c.rute,
                     "rekt": [x, y, c.w, c.h], "synlig": [x + c.box[0], y + c.box[1], x + c.box[2], y + c.box[3]],
                     "animasjon": c.animasjon, "retning": c.retning, "lag": c.lag, "nr": c.nr}
                    for c, x, y in sheet.cels]
            sw, sh = sheet.size
            tiles = gpt.plan_tiles(sw, sh)
            pieces = [gpt.Piece(p["bilde"], cid, str(p["rute"]), home, tuple(p["rekt"]), tuple(p["synlig"])) for p in cels]
            where = gpt.assign_parts(pieces, tiles) if len(tiles) > 1 else {0: pieces}
            content_no = _describe(cels, dirs, english=False, main=main)
            content_en = _describe(cels, dirs, english=True, main=main)
            if mirrored:
                content_en += (". The game mirrors the frames facing right when the character faces left, so there "
                               "are no frames facing left; do not add any")
            pilot = pilot_only or (cid in FIG_PILOT and k <= FIG_PILOT[cid])
            refs = masters or ([f"jobber/{first_job}/resultat.png"] if first_job else [])
            for i, inside in where.items():
                x, y, w, h, ox, oy = tiles[i]
                jid = f"fig{cid:03d}_{k:02d}" + ("" if len(tiles) == 1 else f"_del{i + 1}av{len(tiles)}")
                names_in = {p.bilde for p in inside}
                mine = [p for p in cels if p["bilde"] in names_in]
                job = gpt.Job(jid, home, name, i + 1, len(tiles), (sw, sh), (x, y, w, h), (ox, oy), type="figur",
                              lag=k, kostyme=cid, ruter=mine, bakgrunn=list(bg), pilot=True if pilot else None,
                              rekkefolge=entry.get("rekkefolge"), innhold=content_no,
                              bilde_to=refs[0] if refs else None, referanser=refs or None)
                prompt = figure_prompt(who, bg, colour, content_en, i + 1, len(tiles), notes.get(f"fig{cid:03d}"),
                                       sizes=size_text(mine), job=jid)
                gpt._write_job(jobs_dir, job, image, prompt, style_ref)
                jobs.append(job)
                first_job = first_job or jid
    return jobs


def count_sheets(extract: Path, meta: dict[int, dict]) -> dict[int, dict]:
    """Antall ark per kostyme hvis alle rutene skulle males: {"ark", "store", "ruter", "synlige"}."""
    out = {}
    for cid, info in meta.items():
        boxes = cel_boxes(extract, cid, info)
        sheets = plan_sheets(groups_of(info, boxes))
        out[cid] = {"ark": len(sheets), "store": sum(s.stor for s in sheets),
                    "jobber": sum(len(gpt.plan_tiles(*s.size)) for s in sheets),
                    "ruter": len(info["cels"]), "synlige": sum(1 for b in boxes.values() if b)}
    return out


# ---------------------------------------------------------------- kontroll

def _cel_mask(extract: Path, cel: dict, region: tuple[int, int, int, int], grow: int = 0) -> np.ndarray:
    rx, ry, rw, rh = region
    with Image.open(extract / "costumes" / f"{cel['bilde']}.png") as im:
        alpha = im.convert("RGBA").getchannel("A")
    return gpt._mask_in((rw, rh), alpha, cel["rekt"][0] - rx, cel["rekt"][1] - ry, grow)


def _figure_threshold(original: np.ndarray, bg: np.ndarray) -> float:
    """Hvor langt fra bakgrunnsfargen en piksel må være for å regnes som figur: halve avstanden
    til den nærmeste fargen i originalrutene på arket, men minst 30."""
    d = np.linalg.norm(original - bg, axis=2)
    fig = d[d > 1]
    return max(30.0, 0.5 * float(fig.min())) if fig.size else 30.0


def check_cels(original: Image.Image, candidate_4x: Image.Image, job: gpt.Job, extract: Path) -> dict[str, dict | None]:
    """Kontroll per rute på et figurark, på rutens egne piksler.

    "dekning": andelen av rutens piksler (i 4x) som er malt som figur, ikke som bakgrunnsfargen.
    "omriss": overlappen mellom det som er malt som figur og originalens omriss (snitt / union),
    rundt rutens synlige piksler med en halv avstand rundt. "kantlikhet": kantlikheten inne i omrisset (1x),
    og "kanter" hvor tydelige kantene i originalen er. None: for få synlige piksler.
    """
    bg = np.array(job.bakgrunn or FIG_BACKGROUNDS[0][0], dtype=np.float64)
    o, _, eo, es = gpt._edge_maps(original, candidate_4x)
    hd = np.asarray(candidate_4x.convert("RGB"), dtype=np.float64)
    fg = np.linalg.norm(hd - bg, axis=2) > _figure_threshold(o, bg)
    rx, ry, rw, rh = job.region
    S = gpt.SCALE
    out: dict[str, dict | None] = {}
    for cel in job.ruter or []:
        m1 = _cel_mask(extract, cel, job.region)
        if m1.sum() < FIG_MIN_PIXELS:
            out[cel["bilde"]] = None
            continue
        m4 = np.repeat(np.repeat(m1, S, axis=0), S, axis=1)
        # De synlige pikslene og en halv avstand rundt: der står ingen andre ruter
        vx0, vy0, vx1, vy1 = cel.get("synlig") or [cel["rekt"][0], cel["rekt"][1], cel["rekt"][0] + cel["rekt"][2],
                                                    cel["rekt"][1] + cel["rekt"][3]]
        pad = FIG_PAD // 2
        x0, y0 = max(0, (vx0 - rx - pad) * S), max(0, (vy0 - ry - pad) * S)
        x1, y1 = min(rw * S, (vx1 - rx + pad) * S), min(rh * S, (vy1 - ry + pad) * S)
        a, b = m4[y0:y1, x0:x1], fg[y0:y1, x0:x1]
        inter = float((a & b).sum())
        me = _cel_mask(extract, cel, job.region, grow=1)
        out[cel["bilde"]] = {"dekning": round(inter / max(1.0, float(a.sum())), 3),
                             "omriss": round(inter / max(1.0, float((a | b).sum())), 3),
                             "kantlikhet": round(gpt._corr(eo[me], es[me]), 3),
                             "kanter": round(float(eo[me].std()), 1)}
    return out


def cel_problem(c: dict | None) -> str | None:
    """Hva som er galt med en rute etter check_cels, eller None når den er godt nok."""
    if c is None:
        return None
    if c["dekning"] < FIG_COVER:
        return f"mangler (dekning {c['dekning']:.2f})"
    if c["omriss"] < FIG_OUTLINE:
        return f"omrisset avviker (overlapp {c['omriss']:.2f})"
    if c["kantlikhet"] < FIG_EDGES and c.get("kanter", FIG_REDRAWN_EDGE) >= FIG_REDRAWN_EDGE:
        return f"tegnet om (kantlikhet {c['kantlikhet']:.2f})"
    return None


def _cel_arrays(extract: Path, cel: dict, region, hd_4x: np.ndarray, bg: np.ndarray):
    """Originalruten og HD-ruten i 1x (BOX), med bakgrunnsfargen der ruten er gjennomsiktig, og masken."""
    with Image.open(extract / "costumes" / f"{cel['bilde']}.png") as im:
        a = np.asarray(im.convert("RGBA"), dtype=np.float64)
    m = a[..., 3] > 0
    x, y, w, h = cel["rekt"]
    rx, ry = region[0], region[1]
    S = gpt.SCALE
    crop = hd_4x[(y - ry) * S:(y - ry + h) * S, (x - rx) * S:(x - rx + w) * S]
    hd = crop.reshape(h, S, w, S, 3).mean(axis=(1, 3))
    orig = np.where(m[..., None], a[..., :3], bg)
    hd = np.where(m[..., None], hd, bg)
    return orig, hd, m


def _box3(a: np.ndarray) -> np.ndarray:
    p = np.pad(a, 1, mode="edge")
    return sum(p[dy:dy + a.shape[0], dx:dx + a.shape[1]] for dy in range(3) for dx in range(3)) / 9.0


def _erode(m: np.ndarray) -> np.ndarray:
    p = np.pad(m, 1, constant_values=False)
    out = m.copy()
    for dy in range(3):
        for dx in range(3):
            out &= p[dy:dy + m.shape[0], dx:dx + m.shape[1]]
    return out


def compare_pair(a: tuple, b: tuple, box_a, box_b, bg: np.ndarray) -> dict | None:
    """Sammenligner to nabo-ruter: legger dem over hverandre der originalene passer best (bunnen og
    midten av de synlige pikslene, og inntil FIG_ALIGN piksler rundt), og måler hvor mye mer de
    skiller seg i HD enn i originalen der begge har figur.

    Gir {"original", "hd"} (snittforskjell, 0 til 255) og "flimmer": den største ekstra forskjellen
    i HD jevnet ut over 3 x 3 originalpiksler. None når rutene har for lite felles.
    """
    (oa, ha, ma), (ob, hb, mb) = a, b
    R = FIG_ALIGN
    H = max(ma.shape[0], mb.shape[0]) + 2 * R + abs(box_a[3] - box_b[3])
    W = max(ma.shape[1], mb.shape[1]) + 2 * R + abs((box_a[0] + box_a[2]) // 2 - (box_b[0] + box_b[2]) // 2)

    def put(arr, m, x, y):
        out = np.empty((H, W, 3))
        out[:] = bg
        mm = np.zeros((H, W), bool)
        out[y:y + arr.shape[0], x:x + arr.shape[1]] = arr
        mm[y:y + m.shape[0], x:x + m.shape[1]] = m
        return out, mm

    # B fast, A flyttes: bunnen og midten av de synlige pikslene på samme sted, så +-R rundt
    bx0 = R + max(0, (box_a[0] + box_a[2]) // 2 - (box_b[0] + box_b[2]) // 2)
    by0 = R + max(0, box_a[3] - box_b[3])
    OB, MB = put(ob, mb, bx0, by0)
    HB, _ = put(hb, mb, bx0, by0)
    ax0 = bx0 + (box_b[0] + box_b[2]) // 2 - (box_a[0] + box_a[2]) // 2
    ay0 = by0 + box_b[3] - box_a[3]
    best = None
    for dy in range(-R, R + 1):
        for dx in range(-R, R + 1):
            x, y = ax0 + dx, ay0 + dy
            if x < 0 or y < 0 or x + ma.shape[1] > W or y + ma.shape[0] > H:
                continue
            OA, MA = put(oa, ma, x, y)
            u = MA | MB
            d = float(np.abs(OA - OB).mean(axis=2)[u].mean()) if u.any() else 0.0
            if best is None or d < best[0]:
                best = (d, x, y)
    if best is None:
        return None
    _, x, y = best
    OA, MA = put(oa, ma, x, y)
    HA, _ = put(ha, ma, x, y)
    # Der begge rutene har figur, en piksel inn fra omrisset (kantene er myke i HD)
    both = _erode(MA & MB)
    if both.sum() < FIG_FLICKER_MIN:
        return None
    do = np.abs(OA - OB).mean(axis=2)
    dh = np.abs(HA - HB).mean(axis=2)
    # Snittet av den ekstra forskjellen i hvert 3 x 3-felt, bare over felles piksler (minst 8 av 9,
    # ellers gir myke kanter der posen endrer seg, utslag også når HD-rutene er like)
    share = _box3(both.astype(np.float64))
    excess = _box3(np.where(both, dh - do, 0.0))
    valid = both & (share >= 8 / 9)
    if not valid.any():
        return None
    return {"original": round(float(do[both].mean()), 1), "hd": round(float(dh[both].mean()), 1),
            "flimmer": round(float((excess[valid] / share[valid]).max()), 1)}


def check_flicker(locked_4x: np.ndarray, job: gpt.Job, extract: Path) -> list[dict]:
    """Flimmer mellom nabo-ruter i samme animasjon, retning og lag på arket (etter fargelåsen,
    slik spillet viser dem). Bare ruter som står helt inne i utsnittet."""
    bg = np.array(job.bakgrunn or FIG_BACKGROUNDS[0][0], dtype=np.float64)
    rx, ry, rw, rh = job.region
    inside = [c for c in job.ruter or [] if c["rekt"][0] >= rx and c["rekt"][1] >= ry
              and c["rekt"][0] + c["rekt"][2] <= rx + rw and c["rekt"][1] + c["rekt"][3] <= ry + rh]
    by_group: dict[tuple, list[dict]] = {}
    for c in inside:
        if c.get("animasjon") is not None:
            by_group.setdefault((c["animasjon"], c.get("retning"), c.get("lag")), []).append(c)
    out = []
    for cels in by_group.values():
        cels.sort(key=lambda c: c.get("nr", 0))
        arrays = {c["bilde"]: _cel_arrays(extract, c, job.region, locked_4x, bg) for c in cels}
        for a, b in zip(cels, cels[1:]):
            if b.get("nr", 0) != a.get("nr", 0) + 1:
                continue
            box_a = [v - o for v, o in zip(a["synlig"], a["rekt"][:2] * 2)]
            box_b = [v - o for v, o in zip(b["synlig"], b["rekt"][:2] * 2)]
            r = compare_pair(arrays[a["bilde"]], arrays[b["bilde"]], box_a, box_b, bg)
            if r:
                out.append({"ruter": [a["bilde"], b["bilde"]], **r})
    return out


def judge_sheet(checks: dict[str, dict | None], flicker: list[dict]) -> tuple[list[str], list[str]]:
    """Ruter som er feil, og nabo-par som flimrer."""
    bad = [f"{n} {cel_problem(c)}" for n, c in checks.items() if cel_problem(c)]
    flick = [f"{p['ruter'][0]} og {p['ruter'][1]} (HD {p['flimmer']:.0f} mer enn originalen)"
             for p in sorted(flicker, key=lambda p: -p["flimmer"]) if p["flimmer"] > FIG_FLICKER]
    return bad, flick


# ---------------------------------------------------------------- utklipp

def clean_edges(hd: np.ndarray, original: Path, bg: tuple[int, int, int] | list[int]) -> np.ndarray:
    """Tar bort bakgrunnsfargen fra arket som har blandet seg inn langs omrisset av en utklippet rute.

    Kantene i et malt ark er myke, og ruten klippes ut med originalens omriss. Uten dette får
    figuren en glorie i arkets bakgrunnsfarge i spillet. En HD-piksel inne i omrisset, høyst
    FIG_BLEED_BAND HD-piksler fra kanten, regnes som blandet når den ligger mer enn FIG_BLEED av
    veien fra originalfargen på samme sted mot bakgrunnsfargen. Slike piksler fylles innenfra med
    snittet av de gode nabopikslene, ring for ring. Andre piksler røres ikke.
    """
    with Image.open(original) as im:
        o = im.convert("RGBA")
    S = gpt.SCALE
    o4 = np.asarray(o.resize((o.width * S, o.height * S), Image.NEAREST), dtype=np.float64)
    inside = o4[..., 3] > 0
    outside = Image.fromarray(np.pad(~inside, FIG_BLEED_BAND, constant_values=True).astype(np.uint8) * 255)
    near = np.asarray(outside.filter(ImageFilter.MaxFilter(2 * FIG_BLEED_BAND + 1)))[
        FIG_BLEED_BAND:-FIG_BLEED_BAND, FIG_BLEED_BAND:-FIG_BLEED_BAND] > 0
    c = hd.astype(np.float64)
    d = np.asarray(bg, dtype=np.float64) - o4[..., :3]
    t = ((c - o4[..., :3]) * d).sum(axis=2) / np.maximum((d * d).sum(axis=2), 1.0)
    bad = inside & near & (t > FIG_BLEED)
    good = inside & ~bad
    out = c.copy()
    H, W = bad.shape
    for _ in range(4 * S):
        if not bad.any():
            break
        acc = np.zeros_like(out)
        cnt = np.zeros((H, W))
        pg = np.pad(good, 1)
        po = np.pad(out * good[..., None], ((1, 1), (1, 1), (0, 0)))
        for dy in range(3):
            for dx in range(3):
                acc += po[dy:dy + H, dx:dx + W]
                cnt += pg[dy:dy + H, dx:dx + W]
        fill = bad & (cnt > 0)
        out[fill] = acc[fill] / cnt[fill][:, None]
        good |= fill
        bad &= ~fill
    out[bad] = o4[..., :3][bad]                 # langt inne og ingen gode naboer: originalfargen
    return np.clip(np.rint(out), 0, 255).astype(np.uint8)


def finish_cels(name: str, parts: list[tuple[gpt.Job, np.ndarray | None]], results: dict[str, dict], jobs_dir: Path,
                extract: Path, out: Path, settings: dict) -> tuple[list[str], list[str], dict]:
    """Klipper ut rutene på et figurark som er ferdige, til costumes/costumeCCC_NNN.png i 4x med
    gjennomsiktigheten fra originalen (som `smhd build-mod --kostymer`). En rute er ferdig når alle
    delene den står i, er godtatt. Gir (ferdige, ikke ferdige, provenance)."""
    first = parts[0][0]
    kept = {j.id: t for j, t in parts if t is not None}
    cels: dict[str, dict] = {}
    holders: dict[str, list[gpt.Job]] = {}
    for j, _ in parts:
        for c in j.ruter or []:
            cels.setdefault(c["bilde"], c)
            holders.setdefault(c["bilde"], []).append(j)
    (out / "costumes").mkdir(parents=True, exist_ok=True)
    done, not_done, prov = [], [], {}
    for bilde, c in cels.items():
        if any(j.id not in kept for j in holders[bilde]):
            not_done.append(bilde)
            continue
        src = extract / "costumes" / f"{bilde}.png"
        hd = gpt._cut(first.storrelse, [(j.region, kept[j.id]) for j in holders[bilde]], c["rekt"], src)
        hd = clean_edges(hd, src, first.bakgrunn or FIG_BACKGROUNDS[0][0])
        dest = out / "costumes" / f"{bilde}.png"
        gpt._with_alpha(hd, src).save(dest)
        done.append(bilde)
        made_by = []
        for j in holders[bilde]:
            r = {k: v for k, v in results[j.id].items() if k not in ("figurkontroll", "flimmer")}
            meta = json.loads((jobs_dir / j.id / "jobb.json").read_text())
            pairs = [p for p in results[j.id].get("flimmer", []) if bilde in p["ruter"]]
            made_by.append({"jobb": j.id, **r, "rutekontroll": results[j.id].get("figurkontroll", {}).get(bilde),
                            "flimmer": pairs,
                            **{k: v for k, v in meta.items()
                               if k in ("sha256_referanse", "sha256_prompt", "laget", "stilreferanse")}})
        prov[bilde] = {
            "fil": f"costumes/{bilde}.png", "sha256": gpt._sha(dest),
            "storrelse": [c["rekt"][2] * gpt.SCALE, c["rekt"][3] * gpt.SCALE],
            "type": "figur", "kostyme": c["kostyme"], "rute": c["rute"], "ark": name, "rekt_i_ark": c["rekt"],
            "animasjon": c.get("animasjon"), "retning": c.get("retning"), "lag": c.get("lag"),
            "fargelås": settings, "jobber": made_by,
        }
    return done, not_done, prov


# ---------------------------------------------------------------- hovedark (master-figurark)

# Hovedarkene for hovedpersonene: kostymet de står og går i, og et nærbilde av ansiktet. Grafikeren lager
# hovedark/<navn>.png etter referansen, Tom godkjenner, og så legges det ved som bilde to i alle figurarkene
# for personen (kolonnen hovedark i docs/figurer.csv). Slik som Full Throttle sitt hovedark per figur.
MASTERS = {"sam": {"kostyme": 2, "naerbilde": 27}, "max": {"kostyme": 3, "naerbilde": 28}}
DIR_FRONT_SIDE_BACK = [(2, "front"), (1, "right side"), (3, "back"), (0, "left side")]

PROMPT_MASTER = """Task: master character sheet (model sheet) for {name} from the 1993 adventure game Sam & Max Hit the Road (LucasArts), for a faithful HD remaster. Every later animation sheet of {name} gets this sheet as the reference for the design, so it must match the original exactly and be consistent with itself.

Input: the attached image shows the original low-resolution frames of {name}, enlarged exactly 4x with hard pixel edges, on a plain flat {color} background ({hex}) inside a gray (#808080) border: {content}.

Who it is: {who}.

Draw on one sheet, in the clean high-resolution cartoon style of the game (bold dark outlines, smooth shading, no dithering, no pixel steps):
- the full figure from the front, from the right side, from behind and from the left side, in the same standing poses as the input,
- a close-up of the face, as in the close-up frame,
- the same proportions as the input frames: the same height of head, body and legs, the same width, and the same size of eyes, nose, mouth, hands and feet. Use the input frames as the exact measure, so the figures on this sheet are 4 times the size of the input frames.

Keep the design exactly: the same face, colors, clothes, hat, tie and every mark as in the input. Do not add accessories, logos, text, patterns or details that are not in the input, do not make the head bigger or the body slimmer, and do not modernize the design. Take the colors from the standing frames; the close-up comes from a scene with its own light and background, so use it for the shape of the face only.

Output: one PNG image, exactly 1536 x 1024 pixels, with a fully transparent background (real alpha), the figures standing on one line and not touching each other. No labels, numbers or text on the sheet. Save it as hovedark/{file}.png and write hovedark/{file}-notat.md with tool, date, number of attempts and what was uncertain. Tom approves the sheet before it is used."""


def pose_image(extract: Path, cid: int, info: dict, anim: int, direction: int) -> Image.Image | None:
    """Figuren slik spillet viser den i animasjonen (anim, retning): første rute i hvert lag, satt sammen etter
    rel_x og rel_y, lag 0 nederst, slik ClassicCostumeRenderer tegner dem. En animasjon endrer bare lagene den
    har; de andre beholder ruten fra startanimasjonen (1), som setter hodet. Derfor legges start og så anim
    oppå hverandre. Mot venstre (retning 0) speilvendes bildet når kostymet ikke har egne venstreruter (speil
    er usann), som _drawActorToRight i costume.cpp. None når det ikke finnes noe."""
    cels = {c["cel"]: c for c in info["cels"]}
    limbs: dict[int, int] = {}
    for step in ((1, anim) if anim != 1 else (1,)):
        for a in info.get("animasjoner", []):
            if a["animasjon"] == step and a["retning"] == direction and a["ruter"]:
                limbs[a["lag"]] = a["ruter"][0]
    parts = []
    for lag, cel in limbs.items():
        c = cels.get(cel)
        if not c or not valid_cel(c):
            continue
        im = cel_rgba(extract, f"costume{cid:03d}_{c['cel']:03d}")
        if im is not None and im.getchannel("A").getbbox():
            parts.append((lag, c.get("rel_x", 0), c.get("rel_y", 0), im))
    if not parts:
        return None
    x0 = min(rx for _, rx, _, _ in parts)
    y0 = min(ry for _, _, ry, _ in parts)
    x1 = max(rx + im.width for _, rx, _, im in parts)
    y1 = max(ry + im.height for _, _, ry, im in parts)
    canvas = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    for _, rx, ry, im in sorted(parts, key=lambda p: p[0]):
        canvas.alpha_composite(im, (rx - x0, ry - y0))
    if direction == 0 and not info.get("speil"):
        canvas = canvas.transpose(Image.FLIP_LEFT_RIGHT)
    box = canvas.getchannel("A").getbbox()
    return canvas.crop(box) if box else None


def closeup_image(extract: Path, cid: int, info: dict) -> Image.Image | None:
    """Første rute i kostymets første animasjon (nærbildene av ansiktet har bare noen få animasjoner)."""
    cels = {c["cel"]: c for c in info["cels"]}
    for a in sorted(info.get("animasjoner", []), key=lambda a: (a["animasjon"], a["retning"])):
        for r in a["ruter"]:
            c = cels.get(r)
            if c and valid_cel(c):
                im = cel_rgba(extract, f"costume{cid:03d}_{r:03d}")
                if im is not None and im.getchannel("A").getbbox():
                    return im
    return None


def master_jobs(extract: Path, out: Path, meta: dict[int, dict], names: dict[int, dict]) -> list[str]:
    """Skriver hovedark/<navn>/ (referanse.png, original_1x.png, prompt.txt, jobb.json) for hovedpersonene i
    MASTERS. Gir navnene som ble laget. Leveransen er hovedark/<navn>.png på arbeidsgrenen."""
    made = []
    for key, spec in MASTERS.items():
        cid, close = spec["kostyme"], spec["naerbilde"]
        if cid not in meta:
            continue
        info = meta[cid]
        poses = []
        for d, label in DIR_FRONT_SIDE_BACK:
            im = pose_image(extract, cid, info, 3, d)
            if im is not None:
                poses.append((label, im))
        face = closeup_image(extract, close, meta[close]) if close in meta else None
        if not poses:
            continue
        # Figurene på én linje (føttene nederst), nærbildet til høyre for dem
        items = [im for _, im in poses] + ([face] if face is not None else [])
        W = FIG_MARGIN * 2 + sum(im.width for im in items) + FIG_PAD * (len(items) - 1)
        H = FIG_MARGIN * 2 + max(im.height for im in items)
        if W > gpt.TILE[0] or H > gpt.TILE[1]:
            continue
        colours = np.array(sorted({tuple(p[:3]) for im in items for p in np.asarray(im).reshape(-1, 4) if p[3]}),
                           dtype=np.float64).reshape(-1, 3)
        bg, colour = gpt.sheet_background(colours)
        sheet = Image.new("RGBA", (W, H), (*bg, 255))
        x = FIG_MARGIN
        boxes = []
        for im in items:
            y = H - FIG_MARGIN - im.height
            sheet.alpha_composite(im, (x, y))
            boxes.append([x, y, im.width, im.height])
            x += im.width + FIG_PAD
        content = ", ".join(f"standing, {label}" for label, _ in poses)
        if face is not None:
            content += ", and on the right a close-up frame of the face"
        entry = names.get(cid, {})
        who = entry.get("prompt_en") or MAIN_FIGURES[key]
        d = out / "hovedark" / key
        d.mkdir(parents=True, exist_ok=True)
        ox, oy = (gpt.TILE[0] - W) // 2, (gpt.TILE[1] - H) // 2
        canvas = Image.new("RGB", gpt.CANVAS, gpt.BORDER)
        canvas.paste(sheet.convert("RGB").resize((W * gpt.SCALE, H * gpt.SCALE), Image.NEAREST),
                     (ox * gpt.SCALE, oy * gpt.SCALE))
        canvas.save(d / "referanse.png")
        sheet.convert("RGB").save(d / "original_1x.png")
        prompt = PROMPT_MASTER.format(name=MAIN_FIGURES[key], color=colour, hex="#%02X%02X%02X" % bg,
                                      content=content, who=who, file=key)
        (d / "prompt.txt").write_text(prompt + "\n", encoding="utf-8")
        (d / "jobb.json").write_text(json.dumps({
            "id": f"hovedark_{key}", "type": "hovedark", "figur": MAIN_FIGURES[key], "kostyme": cid,
            "rekkefolge": list(MASTERS).index(key) + 1,
            "naerbilde": close if face is not None else None, "leveranse": f"hovedark/{key}.png",
            "notat": f"hovedark/{key}-notat.md", "plassering": [ox, oy], "storrelse": [W, H],
            "bokser": boxes, "bakgrunn": list(bg),
            "sha256_referanse": gpt._sha(d / "referanse.png"),
            "sha256_prompt": __import__("hashlib").sha256(prompt.encode()).hexdigest(),
        }, indent=1, ensure_ascii=False))
        made.append(key)
    return made
