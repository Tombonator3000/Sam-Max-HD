#!/usr/bin/env python3
"""Egenkontroll for grafikeren: sjekker et resultat mot jobben før det leveres.

Kjøres i grenen gpt-arbeid (der heter filen verktoy/sjekk_leveranse.py) eller fra main:

    python3 verktoy/sjekk_leveranse.py jobber/fig002_01/resultat.png
    python3 verktoy/sjekk_leveranse.py jobber/rom007_del1av2/resultat.png
    python3 verktoy/sjekk_leveranse.py hovedark/sam.png

Trenger bare Python 3, numpy og Pillow. Leser jobb.json, original_1x.png og referanse.png i samme mappe
som resultatet (for hovedark: hovedark/<navn>/).

Hva som sjekkes:
- Alle jobber: format (1536 x 1024 eller utsnittets sideforhold).
- Rom, objekter, lag og ikonark: om bildet ligger der originalen ligger (forskyvning i hele bildet og i
  blokker) og om formene er de samme (kantlikhet), med de samme grensene som mottaket (smhd gpt-inn).
  For lag og ikonark også hvert objekt i rektangelet sitt.
- Figurark (glatt stil med ekte alfa): hver rute for seg. Bredde og høyde på det som er tegnet, mot
  originalens synlige piksler ganger 4, hvor langt midten er flyttet, og hvor godt omrisset dekker
  originalen. Til slutt om rutene i samme animasjon er tegnet like store. Dette er regelen om fast
  størrelse: en rute som er tegnet større eller mindre enn originalen, får figuren til å vokse og krympe
  i spillet.
- Hovedark: ekte alfa, og høyden på hver figur mot originalens figurer ganger 4.

Utfall: OK, SJEKK eller FEIL for hver del og for hele leveransen. Avslutningskoden er 0 (OK), 1 (SJEKK)
eller 2 (FEIL). Mottaket hos Claude gjør de samme målingene og flere til, så OK her er ikke en godkjenning.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image

SCALE = 4
CANVAS = (1536, 1024)
TILE = (384, 256)

# Samme grenser som pipeline/smhd/gpt.py (judge)
OK_SHIFT, OK_BLOCK, OK_EDGES = 0.75, 1.0, 0.55
CHECK_SHIFT, CHECK_BLOCK, CHECK_EDGES = 1.5, 2.0, 0.40
OBJ_EDGES = 0.50

# Figurark: størrelse, plassering og omriss per rute
SIZE_OK, SIZE_CHECK = 0.06, 0.12       # avvik i bredde eller høyde fra originalen ganger 4
MOVE_OK, MOVE_CHECK = 1.5, 3.0         # flyttet midtpunkt, i originalpiksler
IOU_OK, IOU_CHECK = 0.75, 0.60         # snitt delt på union mellom tegningen og originalens omriss
SPREAD_CHECK = 0.05                    # ulik størrelse innen samme animasjon (største minus minste forhold)
CORE = 128                             # alfa for det som regnes som tegnet
WINDOW = 4                             # originalpiksler rundt ruten der tegningen letes etter (halve avstanden)

RANK = {"OK": 0, "SJEKK": 1, "FEIL": 2}


def worst(*levels: str) -> str:
    return max(levels, key=lambda v: RANK[v]) if levels else "OK"


# ---------------------------------------------------------------- bildeanalyse (som gpt.py)

def lum(a: np.ndarray) -> np.ndarray:
    return a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114


def box_blur(a: np.ndarray, r: int, axis: int) -> np.ndarray:
    if r <= 0:
        return a
    pad = [(0, 0)] * a.ndim
    pad[axis] = (r + 1, r)
    p = np.pad(a, pad, mode="edge")
    c = np.cumsum(p, axis=axis)
    n = a.shape[axis]
    hi = np.take(c, np.arange(2 * r + 1, 2 * r + 1 + n), axis=axis)
    lo = np.take(c, np.arange(0, n), axis=axis)
    return (hi - lo) / (2 * r + 1)


def blur(a: np.ndarray, sigma: float) -> np.ndarray:
    if sigma <= 0:
        return a
    r = max(1, int(round(math.sqrt(12 * sigma * sigma / 3 + 1) - 1) // 2))
    out = a.astype(np.float64)
    for _ in range(3):
        out = box_blur(box_blur(out, r, 0), r, 1)
    return out


def edges(l: np.ndarray) -> np.ndarray:
    gy, gx = np.gradient(blur(l, 0.8))
    return np.hypot(gx, gy)


def phase_shift(ref: np.ndarray, img: np.ndarray) -> tuple[float, float]:
    h, w = ref.shape
    win = np.outer(np.hanning(h), np.hanning(w))
    a = np.fft.fft2((ref - ref.mean()) * win)
    b = np.fft.fft2((img - img.mean()) * win)
    r = b * np.conj(a)
    r /= np.abs(r) + 1e-9
    c = np.fft.ifft2(r).real
    py, px = np.unravel_index(np.argmax(c), c.shape)
    peak = c[py, px]

    def sub(cm, c0, cp):
        d = cm - 2 * c0 + cp
        return 0.0 if abs(d) < 1e-12 else 0.5 * (cm - cp) / d

    dy = py + sub(c[(py - 1) % h, px], peak, c[(py + 1) % h, px])
    dx = px + sub(c[py, (px - 1) % w], peak, c[py, (px + 1) % w])
    if dy > h / 2:
        dy -= h
    if dx > w / 2:
        dx -= w
    return float(dx), float(dy)


def corr(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.corrcoef(a.ravel(), b.ravel())[0, 1]) if a.std() > 0 and b.std() > 0 else 0.0


def compare(original: Image.Image, part_4x: Image.Image) -> dict:
    w, h = original.size
    small = part_4x.resize((w, h), Image.BOX)
    o = np.asarray(original.convert("RGB"), dtype=np.float64)
    s = np.asarray(small.convert("RGB"), dtype=np.float64)
    eo, es = edges(lum(o)), edges(lum(s))
    dx, dy = phase_shift(eo, es)
    block = 0.0
    bw, bh = max(48, w // 3), max(48, h // 2)
    if w >= 96 or h >= 96:
        for by in range(0, max(1, h - bh + 1), bh):
            for bx in range(0, max(1, w - bw + 1), bw):
                a, b = eo[by:by + bh, bx:bx + bw], es[by:by + bh, bx:bx + bw]
                if a.std() < 1e-3 or b.std() < 1e-3:
                    continue
                bdx, bdy = phase_shift(a, b)
                block = max(block, math.hypot(bdx, bdy))
    return {"skift": round(math.hypot(dx, dy), 2), "skift_x": round(dx, 2), "skift_y": round(dy, 2),
            "blokk": round(block, 2), "kantlikhet": round(corr(eo, es), 3), "eo": eo, "es": es}


def judge(m: dict) -> tuple[str, list[str]]:
    why = []
    if m["skift"] > OK_SHIFT:
        why.append(f"forskjøvet {m['skift_x']:+.1f}, {m['skift_y']:+.1f} originalpiksler")
    if m["blokk"] > OK_BLOCK:
        why.append(f"deler av bildet er flyttet eller zoomet (opptil {m['blokk']:.1f} px)")
    if m["kantlikhet"] < OK_EDGES:
        why.append(f"formene ligner for lite på originalen (kantlikhet {m['kantlikhet']:.2f})")
    if not why:
        return "OK", why
    if m["skift"] <= CHECK_SHIFT and m["blokk"] <= CHECK_BLOCK and m["kantlikhet"] >= CHECK_EDGES:
        return "SJEKK", why
    return "FEIL", why


# ---------------------------------------------------------------- uttak av utsnittet

def layout(size: tuple[int, int], region: tuple[int, int]) -> str | None:
    aspect, canvas, own = size[0] / size[1], CANVAS[0] / CANVAS[1], region[0] / region[1]
    if abs(aspect - canvas) / canvas <= 0.02:
        return "lerret"
    if abs(aspect - own) / own <= 0.02:
        return "direkte"
    return None


def part_of(result: Image.Image, job: dict) -> tuple[Image.Image | None, str]:
    """Utsnittet i 4x (RGBA) slik mottaket tar det ut, og formatet."""
    x, y, w, h = job["region"]
    ox, oy = job["plassering"]
    kind = layout(result.size, (w, h))
    if kind is None:
        return None, f"feil sideforhold {result.width}x{result.height} (skal være 1536x1024 eller {w}:{h})"
    if kind == "lerret":
        sx, sy = result.width / CANVAS[0], result.height / CANVAS[1]
        box = (ox * SCALE * sx, oy * SCALE * sy, (ox + w) * SCALE * sx, (oy + h) * SCALE * sy)
        part = result.crop(tuple(round(v) for v in box))
    else:
        part = result
    return part.resize((w * SCALE, h * SCALE), Image.LANCZOS), kind


# ---------------------------------------------------------------- rom, objekter, lag og ikonark

def check_picture(res_path: Path, job: dict, d: Path) -> str:
    result = Image.open(res_path).convert("RGB")
    part, kind = part_of(result, job)
    if part is None:
        print(f"FEIL  {kind}")
        return "FEIL"
    original = Image.open(d / "original_1x.png").convert("RGB")
    m = compare(original, part)
    level, why = judge(m)
    print(f"{level:5s} hele bildet ({kind}): skift {m['skift']:.2f}, blokker {m['blokk']:.2f}, "
          f"kantlikhet {m['kantlikhet']:.2f}" + (f". {'; '.join(why)}" if why else ""))
    if min(result.width / (job['region'][2] * SCALE), result.height / (job['region'][3] * SCALE)) < 0.6:
        print("SJEKK lav oppløsning fra generatoren")
        level = worst(level, "SJEKK")
    rx, ry, rw, rh = job["region"]
    for p in job.get("objekter") or []:
        x, y, w, h = p["rekt"]
        x0, y0 = max(0, x - rx), max(0, y - ry)
        x1, y1 = min(rw, x - rx + w), min(rh, y - ry + h)
        if x1 - x0 < 4 or y1 - y0 < 4:
            continue
        a, b = m["eo"][y0:y1, x0:x1], m["es"][y0:y1, x0:x1]
        if a.std() < 1.0:
            continue
        c = corr(a, b)
        lv = "OK" if c >= OBJ_EDGES + 0.1 else ("SJEKK" if c >= OBJ_EDGES else "FEIL")
        if lv != "OK":
            print(f"{lv:5s} {p['bilde']}: kantlikhet {c:.2f} i rektangelet {p['rekt']} (mangler, flyttet eller tegnet om?)")
        level = worst(level, lv)
    return level


# ---------------------------------------------------------------- figurark

def original_mask(original: np.ndarray, bg: list[int], rect: tuple[int, int, int, int]) -> np.ndarray:
    """Originalens synlige piksler i et rektangel på arket (1x): alt som ikke er bakgrunnsfargen."""
    x0, y0, x1, y1 = rect
    sub = original[y0:y1, x0:x1, :3].astype(np.int16)
    return np.abs(sub - np.array(bg, dtype=np.int16)).sum(axis=2) > 24


def check_figure(res_path: Path, job: dict, d: Path) -> str:
    res = Image.open(res_path)
    if res.mode not in ("RGBA", "LA", "PA") and "transparency" not in res.info:
        print("FEIL  bildet har ingen alfakanal. Figurarkene leveres på gjennomsiktig bakgrunn med ekte alfa.")
        return "FEIL"
    rgba = res.convert("RGBA")
    if layout(rgba.size, tuple(job["region"][2:])) != "lerret":
        print(f"FEIL  figurarket skal leveres som hele lerretet, 1536 x 1024 (er {rgba.width} x {rgba.height})")
        return "FEIL"
    if rgba.size != CANVAS:
        rgba = rgba.resize(CANVAS, Image.LANCZOS)
    alpha = np.asarray(rgba)[..., 3]
    if (alpha < 16).mean() < 0.2:
        print("FEIL  bakgrunnen er ikke gjennomsiktig (under 20 prosent av bildet har alfa 0)")
        return "FEIL"
    original = np.asarray(Image.open(d / "original_1x.png").convert("RGB"))
    rx, ry, rw, rh = job["region"]
    ox, oy = job["plassering"]
    bg = job.get("bakgrunn") or [0, 177, 64]
    drawn = alpha >= CORE
    used = np.zeros_like(drawn)
    level = "OK"
    rows = []
    by_group: dict[tuple, list[tuple[str, float, float]]] = {}
    for c in job.get("ruter") or []:
        sx0, sy0, sx1, sy1 = c["synlig"]
        # Rektangelet i utsnittets 1x-koordinater og på lerretet i HD
        lx0, ly0, lx1, ly1 = sx0 - rx, sy0 - ry, sx1 - rx, sy1 - ry
        if lx0 < 0 or ly0 < 0 or lx1 > rw or ly1 > rh:
            continue                     # ruten står i en annen del av arket
        om = original_mask(original, bg, (lx0, ly0, lx1, ly1))
        if om.sum() < 20:
            continue
        ys, xs = np.nonzero(om)
        ow, oh = int(xs.max() - xs.min() + 1), int(ys.max() - ys.min() + 1)
        ocx, ocy = lx0 + (xs.min() + xs.max() + 1) / 2, ly0 + (ys.min() + ys.max() + 1) / 2
        wx0 = max(0, (ox + lx0 - WINDOW) * SCALE)
        wy0 = max(0, (oy + ly0 - WINDOW) * SCALE)
        wx1 = min(CANVAS[0], (ox + lx1 + WINDOW) * SCALE)
        wy1 = min(CANVAS[1], (oy + ly1 + WINDOW) * SCALE)
        win = drawn[wy0:wy1, wx0:wx1]
        used[wy0:wy1, wx0:wx1] |= win
        if not win.any():
            rows.append(("FEIL", c["bilde"], "ingenting er tegnet der ruten står"))
            level = worst(level, "FEIL")
            continue
        dys, dxs = np.nonzero(win)
        dw = (dxs.max() - dxs.min() + 1) / SCALE
        dh = (dys.max() - dys.min() + 1) / SCALE
        dcx = (wx0 + (dxs.min() + dxs.max() + 1) / 2) / SCALE - ox
        dcy = (wy0 + (dys.min() + dys.max() + 1) / 2) / SCALE - oy
        fw, fh = dw / ow, dh / oh
        move = math.hypot(dcx - ocx, dcy - ocy)
        touches = dxs.min() == 0 or dys.min() == 0 or dxs.max() == win.shape[1] - 1 or dys.max() == win.shape[0] - 1
        # Omrisset: originalen i 4x mot tegningen, med midtpunktene lagt over hverandre
        o4 = np.repeat(np.repeat(om, SCALE, axis=0), SCALE, axis=1)
        shift_x = round((dcx - ocx) * SCALE)
        shift_y = round((dcy - ocy) * SCALE)
        tx0, ty0 = (ox + lx0) * SCALE + shift_x, (oy + ly0) * SCALE + shift_y
        cut = np.zeros_like(o4)
        sx, sy = max(0, tx0), max(0, ty0)
        ex_, ey_ = min(CANVAS[0], tx0 + o4.shape[1]), min(CANVAS[1], ty0 + o4.shape[0])
        if ex_ > sx and ey_ > sy:
            cut[sy - ty0:ey_ - ty0, sx - tx0:ex_ - tx0] = drawn[sy:ey_, sx:ex_]
        inter, union = float((cut & o4).sum()), float((cut | o4).sum())
        iou = inter / union if union else 0.0
        size_dev = max(abs(fw - 1), abs(fh - 1))
        lv = "OK"
        why = []
        if size_dev > SIZE_OK:
            lv = worst(lv, "SJEKK" if size_dev <= SIZE_CHECK else "FEIL")
            why.append(f"størrelsen avviker: bredde {fw:.0%}, høyde {fh:.0%} av originalen")
        if move > MOVE_OK:
            lv = worst(lv, "SJEKK" if move <= MOVE_CHECK else "FEIL")
            why.append(f"flyttet {move:.1f} originalpiksler")
        if iou < IOU_OK:
            lv = worst(lv, "SJEKK" if iou >= IOU_CHECK else "FEIL")
            why.append(f"omrisset dekker originalen dårlig (snitt/union {iou:.2f})")
        if touches:
            lv = worst(lv, "SJEKK")
            why.append("tegningen går ut i avstanden mot naborutene")
        rows.append((lv, c["bilde"], f"bredde {fw:.0%}, høyde {fh:.0%}, flyttet {move:.1f} px, snitt/union {iou:.2f}"
                     + (f". {'; '.join(why)}" if why else "")))
        level = worst(level, lv)
        by_group.setdefault((c.get("animasjon"), c.get("retning"), c.get("lag")), []).append((c["bilde"], fw, fh))
    for lv, name, text in rows:
        if lv != "OK":
            print(f"{lv:5s} {name}: {text}")
    n_ok = sum(1 for lv, _, _ in rows if lv == "OK")
    print(f"      {n_ok} av {len(rows)} ruter OK")
    for key, items in by_group.items():
        if len(items) < 2:
            continue
        for k, label in ((1, "bredde"), (2, "høyde")):
            vals = [it[k] for it in items]
            spread = max(vals) - min(vals)
            if spread > SPREAD_CHECK:
                print(f"SJEKK animasjon {key[0]}, retning {key[1]}, lag {key[2]}: {label} varierer {spread:.0%} mellom rutene "
                      f"({', '.join(f'{it[0][-3:]} {it[k]:.0%}' for it in items)}). Figuren vil vokse og krympe.")
                level = worst(level, "SJEKK")
    stray = drawn & ~used
    if stray.sum() > 400:
        print(f"SJEKK {int(stray.sum())} piksler er tegnet utenfor rutene (streker, skygger eller ekstra figurer?)")
        level = worst(level, "SJEKK")
    return level


# ---------------------------------------------------------------- hovedark

def check_master(res_path: Path, job: dict) -> str:
    res = Image.open(res_path)
    if res.mode not in ("RGBA", "LA", "PA") and "transparency" not in res.info:
        print("FEIL  hovedarket har ingen alfakanal (skal ha gjennomsiktig bakgrunn)")
        return "FEIL"
    a = np.asarray(res.convert("RGBA").resize(CANVAS, Image.LANCZOS))[..., 3] >= CORE
    cols = a.any(axis=0)
    segments, start = [], None
    for x, on in enumerate(list(cols) + [False]):
        if on and start is None:
            start = x
        elif not on and start is not None:
            if x - start > 8:
                segments.append((start, x))
            start = None
    expected = [b[3] * SCALE for b in job.get("bokser", [])]
    level = "OK"
    print(f"      {len(segments)} figurer funnet, {len(expected)} i referansen")
    if len(segments) != len(expected):
        print("SJEKK antallet figurer er ikke det samme som i referansen (fire stående og ett nærbilde)")
        level = "SJEKK"
    for i, ((x0, x1), want) in enumerate(zip(segments, expected), 1):
        rows = np.nonzero(a[:, x0:x1].any(axis=1))[0]
        h = int(rows[-1] - rows[0] + 1)
        f = h / want
        lv = "OK" if abs(f - 1) <= SIZE_OK else ("SJEKK" if abs(f - 1) <= SIZE_CHECK else "FEIL")
        print(f"{lv:5s} figur {i}: høyde {h} px, originalen ganger 4 er {want} px ({f:.0%})")
        level = worst(level, lv)
    return level


# ---------------------------------------------------------------- hovedprogram

def find_job(res_path: Path) -> tuple[dict, Path]:
    d = res_path.parent
    if (d / "jobb.json").exists():
        return json.loads((d / "jobb.json").read_text(encoding="utf-8")), d
    # hovedark/sam.png -> hovedark/sam/jobb.json
    alt = d / res_path.stem
    if (alt / "jobb.json").exists():
        return json.loads((alt / "jobb.json").read_text(encoding="utf-8")), alt
    raise SystemExit(f"Fant ikke jobb.json ved {res_path}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Egenkontroll av en leveranse før den committes.")
    ap.add_argument("resultat", nargs="+", help="resultat.png i en jobbmappe, eller hovedark/<navn>.png")
    a = ap.parse_args(argv)
    total = "OK"
    for r in a.resultat:
        path = Path(r)
        job, d = find_job(path)
        kind = job.get("type", "rom")
        print(f"== {job.get('id', d.name)} ({kind}): {path}")
        if kind == "hovedark":
            level = check_master(path, job)
        elif kind == "figur":
            level = check_figure(path, job, d)
        else:
            level = check_picture(path, job, d)
        print(f"   Utfall: {level}")
        total = worst(total, level)
    return RANK[total]


if __name__ == "__main__":
    sys.exit(main())
