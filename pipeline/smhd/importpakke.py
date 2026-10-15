"""Mottak for importpakken fra grafikeren (rapporter/import-grafikk-*/manifest.json på arbeidsgrenen).

Manifestet kobler hvert bilde til filen i repoet (`repo_fil`), sjekksum og `behandling`:

- `egen_ikon_alfa`: ikonene. Tas inn av `smhd myke-ikoner` (ikonmanifest.json), hoppes over her.
- `alias`: navngitte kopier for verbhjulet, ikke spillobjekter. Hoppes over.
- `helt_motiv_for_lappklipp`: et helt, malt objektmotiv i 4x av tilstanden. Erstatter bildet gpt-inn klippet
  ut av lagjobben (der lappens alfa er brukt for tidlig), så build-mod kan klippe en lapp-tilstand med
  lappens maske (`_patch_from_full_painting`). Andre tilstander brukes som de er.
- `rom54_palett_og_lappklipp`: det samme for objektene 833, 834 og 836, som ligger i rom 83 men tegnes i rom 54.
- `indekspiksler_original_palett_rom54`: indeksbildet med rom 54-paletten. Pikslene må være de samme som i
  uttrekket; da brukes det i stedet for uttrekkets (som har rom 83-paletten), så motoren toner fargene
  mot riktig palett.
- `egen_alfa`: objektbilder med egen myk alfa (inventaresken obj995, LucasArts-logoen obj049). Legges som
  objNNN_SS_hd.png (motorens myke bilde for blast-objekter og pekeren) og som objNNN_SS.png.

Objektmanifest (`rapporter/*/objektleveranser.json`, 15. oktober 18:06) med hele tegninger tas inn som
`helt_motiv_for_lappklipp`.

Bilder i `avventer` tas ikke inn. Avvisninger i docs/gpt-avvisninger.csv (jobb = bildenavnet) gjelder.
Står samme bilde i flere manifester, vinner det siste (mappene sortert etter navn).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

from .ikoner import SCALE, margin

FULL = ("helt_motiv_for_lappklipp", "rom54_palett_og_lappklipp")
IDX = ("indekspiksler_original_palett_rom54",)
SOFT = ("egen_alfa",)
SKIP = ("egen_ikon_alfa", "alias")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entries(gren: Path) -> tuple[dict[str, dict], set[str]]:
    """Importmanifestene og objektmanifestene (rapporter/*/objektleveranser.json: en liste med bilde, fil,
    sha256 og heltegning; et helt motiv behandles som helt_motiv_for_lappklipp). Alle sorteres etter sti,
    og det siste vinner."""
    out: dict[str, dict] = {}
    waiting: set[str] = set()
    files = sorted(list(gren.glob("rapporter/import-grafikk-*/manifest.json")) +
                   list(gren.glob("rapporter/*/objektleveranser.json")))
    for f in files:
        try:
            m = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        rel = str(f.relative_to(gren))
        if isinstance(m, list):
            for r in m:
                if isinstance(r, dict) and r.get("bilde") and r.get("fil") and r.get("heltegning"):
                    out[r["bilde"]] = {"repo_fil": r["fil"], "pakke_fil": r["fil"], "sha256": r.get("sha256"),
                                       "behandling": "helt_motiv_for_lappklipp", "navn": r["bilde"], "manifest": rel}
            continue
        waiting |= set(m.get("avventer", []))
        for r in m.get("filer", []):
            if r.get("repo_fil") and r.get("pakke_fil") and r.get("behandling"):
                name = Path(r["pakke_fil"]).stem
                out[name] = {**r, "navn": name, "manifest": rel}
    return out, waiting


def _rejected(rej: dict | None, sha: str) -> bool:
    return bool(rej) and rej.get("status", "avvist").strip() in ("", "avvist") and \
        rej.get("sha256_resultat", "").strip() in ("*", sha)


def import_all(gren: Path, extract: Path, ut: Path, rejections: dict[str, dict] | None = None) -> dict:
    rejections = rejections or {}
    (ut / "objects").mkdir(parents=True, exist_ok=True)
    rows, waiting = entries(gren)
    report: dict = {"bilder": {}, "ok": 0, "hoppet_over": 0, "avventer": sorted(waiting)}

    def skip(name: str, why: str, r: dict) -> None:
        report["bilder"][name] = {"status": "hoppet over", "grunn": why, "behandling": r["behandling"],
                                  "manifest": r["manifest"]}
        report["hoppet_over"] += 1

    for name, r in sorted(rows.items()):
        kind = r["behandling"]
        if kind in SKIP:
            continue
        base = name[:-4] if name.endswith("_idx") else name
        if base in waiting:
            skip(name, "avventer avklaring", r)
            continue
        src = gren / r["repo_fil"]
        if not src.exists():
            skip(name, "filen finnes ikke", r)
            continue
        sha = _sha(src)
        if r.get("sha256") and r["sha256"] != sha:
            skip(name, "sjekksummen stemmer ikke med manifestet", r)
            continue
        if _rejected(rejections.get(base), sha):
            skip(name, f"avvist: {rejections[base].get('grunn', '').strip()}", r)
            continue
        if kind in IDX:
            orig = extract / "objects" / f"{name}.png"
            if not orig.exists():
                skip(name, "ingen originalt indeksbilde", r)
                continue
            a, b = Image.open(src), Image.open(orig)
            if a.mode != "P" or a.size != b.size or not np.array_equal(np.asarray(a), np.asarray(b)):
                skip(name, "indekspikslene er ikke de samme som i uttrekket", r)
                continue
            a.save(ut / "objects" / f"{name}.png")
            report["bilder"][name] = {"status": "ok", "behandling": kind, "fil": f"objects/{name}.png", "sha256": sha,
                                      "manifest": r["manifest"]}
            report["ok"] += 1
            continue
        if kind not in FULL + SOFT:
            skip(name, f"ukjent behandling {kind}", r)
            continue
        orig = extract / "objects" / f"{name}.png"
        if not orig.exists():
            skip(name, "ingen originalbilde med det navnet", r)
            continue
        im = Image.open(src)
        if im.mode != "RGBA":
            skip(name, f"ikke RGBA ({im.mode})", r)
            continue
        with Image.open(orig) as o:
            osize = o.size
        if kind in FULL:
            if im.size != (osize[0] * SCALE, osize[1] * SCALE):
                skip(name, f"er {im.width}x{im.height}, skal være {osize[0] * SCALE}x{osize[1] * SCALE}", r)
                continue
            im.save(ut / "objects" / f"{name}.png")
            files = [f"objects/{name}.png"]
        else:
            m = margin(im.size, osize)
            if m is None:
                skip(name, f"er {im.width}x{im.height}, skal være ({osize[0]} + 2 * marg) x ({osize[1]} + 2 * marg) ganger {SCALE}", r)
                continue
            im.save(ut / "objects" / f"{name}_hd.png")
            files = [f"objects/{name}_hd.png"]
            if m == (0, 0):
                im.save(ut / "objects" / f"{name}.png")
                files.append(f"objects/{name}.png")
        report["bilder"][name] = {"status": "ok", "behandling": kind, "filer": files, "sha256": sha,
                                  "manifest": r["manifest"]}
        report["ok"] += 1
    (ut / "importpakke.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    return report
