"""Mottak for ikoner i den glatte stilen: inventartingene og handlingspekerne med egen myk alfa.

Ikonarkene (ikonNN) klippes ut i gpt-inn med originalens alfa, så kantene blir trappetrinn i 4x.
ChatGPT/Codex leverer i tillegg hvert ikon som eget RGBA-bilde med myk alfa, oppført i
rapporter/*/ikonmanifest.json på arbeidsgrenen (bilde, fil, sha256, storrelse). Dette mottaket
legger dem i objects/objNNN_SS_hd.png. Motoren bruker _hd.png for blast-objekter (inventaret) og
for pekeren, med bildets egen alfa (docs/HD-MOTOR.md).

Et ikon tas bare inn når
- filen finnes og sjekksummen stemmer med manifestet,
- ikonarket det står på er godtatt i gpt-inn (det utklipte objects/objNNN_SS.png finnes i mottaket),
- størrelsen er originalen i 4x, eventuelt med like stor marg på begge sider i hele originalpiksler,
- det ikke er avvist i docs/gpt-avvisninger.csv (jobb = objNNN_SS, sha256_resultat = filens sjekksum eller *).
Står samme ikon i flere manifester, vinner det siste (rapportmappene sortert etter navn).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image

SCALE = 4


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def margin(hd_size: tuple[int, int], orig_size: tuple[int, int], scale: int = SCALE) -> tuple[int, int] | None:
    """Margen (x, y) i originalpiksler når HD-bildet er originalen i `scale` med lik marg på begge sider."""
    w, h = hd_size
    ow, oh = orig_size
    if w % scale or h % scale:
        return None
    px, py = (w // scale - ow), (h // scale - oh)
    if px < 0 or py < 0 or px % 2 or py % 2:
        return None
    return px // 2, py // 2


def manifest(gren: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in sorted(gren.glob("rapporter/*/ikonmanifest.json")):
        try:
            rows = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for r in rows if isinstance(rows, list) else []:
            if r.get("bilde") and r.get("fil"):
                out[r["bilde"]] = {**r, "manifest": str(f.relative_to(gren))}
    return out


def import_all(gren: Path, extract: Path, ut: Path, rejections: dict[str, dict] | None = None) -> dict:
    """Legger de myke ikonene i ut/objects/<bilde>_hd.png og skriver ut/myke_ikoner.json."""
    rejections = rejections or {}
    (ut / "objects").mkdir(parents=True, exist_ok=True)
    report: dict = {"ikoner": {}, "ok": 0, "hoppet_over": 0}
    for bilde, r in sorted(manifest(gren).items()):
        src = gren / r["fil"]
        dest = ut / "objects" / f"{bilde}_hd.png"
        why = None
        sha = _sha(src) if src.exists() else None
        orig = extract / "objects" / f"{bilde}.png"
        rej = rejections.get(bilde)
        if sha is None:
            why = "filen finnes ikke"
        elif r.get("sha256") and r["sha256"] != sha:
            why = "sjekksummen stemmer ikke med manifestet"
        elif not orig.exists():
            why = "ingen originalbilde med det navnet"
        elif not (ut / "objects" / f"{bilde}.png").exists():
            why = "ikonarket er ikke godtatt i gpt-inn"
        elif rej and rej.get("status", "avvist").strip() in ("", "avvist") and \
                rej.get("sha256_resultat", "").strip() in ("*", sha):
            why = f"avvist: {rej.get('grunn', '').strip()}"
        else:
            im = Image.open(src)
            with Image.open(orig) as o:
                osize = o.size
            m = margin(im.size, osize)
            if im.mode != "RGBA":
                why = f"ikke RGBA ({im.mode})"
            elif m is None:
                why = f"er {im.width}x{im.height}, skal være ({osize[0]} + 2 * marg) x ({osize[1]} + 2 * marg) ganger {SCALE}"
            elif im.getchannel("A").getextrema()[1] == 0:
                why = "helt gjennomsiktig"
        if why:
            dest.unlink(missing_ok=True)
            report["ikoner"][bilde] = {"status": "hoppet over", "grunn": why, "manifest": r["manifest"]}
            report["hoppet_over"] += 1
            continue
        im.save(dest)
        report["ikoner"][bilde] = {"status": "ok", "fil": f"objects/{bilde}_hd.png", "sha256": sha,
                                   "marg": list(m), "manifest": r["manifest"]}
        report["ok"] += 1
    (ut / "myke_ikoner.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    return report
