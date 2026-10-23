"""Tapsfri migrering av en ferdig mod. Kildemappen endres aldri.

Fargebilder blir WebP når det sparer plass. Palettindekser og dekningsmasker
kopieres byte for byte som PNG. Hver WebP dekodes på nytt og alle RGBA-byte
sammenlignes, også RGB under alfa 0. En ufullført konvertering publiseres ikke.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil

from PIL import Image, features


COLOUR = re.compile(
    r"(?:rooms/room\d+|objects/obj\d+_[0-9a-fA-F]{2}(?:_hd)?|"
    r"costumes/costume\d+_\d+(?:_hd)?|fonts/[a-z0-9-]+|san/[^/]+/\d+)\.png"
)


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def convert_image(source: Path, target: Path) -> dict:
    """Encode a colour PNG, verify pixels, and keep the smaller representation."""
    original_hash = sha256(source)
    original_size = source.stat().st_size
    with Image.open(source) as image:
        if image.n_frames != 1 or image.mode not in {"1", "L", "LA", "P", "RGB", "RGBA"}:
            raise ValueError(f"Ustøttet PNG-type: {source} ({image.mode})")
        if max(image.size) > 16383:
            raise ValueError(f"Bildet er for stort for WebP: {source} {image.size}")
        rgba = image.convert("RGBA")
        # exact is essential: the default discards RGB under fully transparent pixels.
        rgba.save(target, format="WEBP", lossless=True, quality=100, method=6, exact=True)
        with Image.open(target) as decoded:
            if decoded.format != "WEBP" or decoded.size != rgba.size or decoded.convert("RGBA").tobytes() != rgba.tobytes():
                raise ValueError(f"WebP endret RGBA-piksler: {source}")
        pixel_hash = hashlib.sha256(rgba.tobytes()).hexdigest()
        dimensions = list(rgba.size)
    if sha256(source) != original_hash:
        raise ValueError(f"Kilden ble endret under konvertering: {source}")
    if target.stat().st_size >= original_size:
        target.unlink()
        target = target.with_suffix(".png")
        shutil.copy2(source, target)
    return {
        "source_sha256": original_hash, "target_sha256": sha256(target),
        "source_bytes": original_size, "target_bytes": target.stat().st_size,
        "rgba_sha256": pixel_hash, "dimensions": dimensions,
        "rgba_exact": True, "extension": target.suffix,
    }


def convert_mod(source: Path, destination: Path, workers: int = 2) -> dict:
    source, destination = source.resolve(), destination.resolve()
    if destination == source or source in destination.parents or destination in source.parents:
        raise ValueError("Kilde og mål må være atskilte mapper utenfor hverandre")
    if destination.exists():
        raise FileExistsError(f"Målmappen finnes allerede: {destination}")
    if not features.check("webp"):
        raise RuntimeError("Pillow mangler WebP-støtte")
    metadata = json.loads((source / "mod.json").read_text())
    if metadata.get("format") != 1 or metadata.get("scale") != 4:
        raise ValueError("Forventer en DigHD-mod i format 1 med skala 4")
    files = sorted(source.rglob("*"))
    if any(path.is_symlink() for path in files):
        raise ValueError("Symbolske lenker er ikke tillatt i modden")
    files = [path for path in files if path.is_file() and ".git" not in path.relative_to(source).parts]
    # Reject a stale/ambiguous pair instead of replacing an existing WebP silently.
    for path in files:
        if COLOUR.fullmatch(path.relative_to(source).as_posix()) and path.with_suffix(".webp").exists():
            raise ValueError(f"Både PNG og WebP finnes: {path}")
    destination.mkdir(parents=True)
    report = {"created_utc": datetime.now(timezone.utc).isoformat(), "pillow_webp": features.version("webp"),
              "lossless": True, "exact": True, "files": [], "complete": False}

    def one(path: Path) -> dict:
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if COLOUR.fullmatch(relative.as_posix()):
            row = convert_image(path, target.with_suffix(".webp"))
            target = target.with_suffix(row.pop("extension"))
            row["colour_image"] = True
        else:
            shutil.copy2(path, target)
            original_hash = sha256(path)
            if sha256(target) != original_hash:
                raise ValueError(f"Kopieringen endret {relative}")
            row = {"source_sha256": original_hash, "target_sha256": original_hash,
                   "source_bytes": path.stat().st_size, "target_bytes": target.stat().st_size,
                   "colour_image": False}
        return {"source": relative.as_posix(), "target": target.relative_to(destination).as_posix(), **row}

    # The manifest is flushed incrementally, so an interrupted run remains auditable.
    manifest = destination / "webp-migration.json"
    try:
        with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
            for row in pool.map(one, [p for p in files if p.name not in {"SHA256SUMS", "webp-migration.json"}]):
                report["files"].append(row)
                if len(report["files"]) % 100 == 0:
                    manifest.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        report["source_bytes"] = sum(row["source_bytes"] for row in report["files"])
        report["target_bytes"] = sum(row["target_bytes"] for row in report["files"])
        report["converted"] = sum(row["target"].endswith(".webp") and row["source"].endswith(".png") for row in report["files"])
        report["complete"] = True
    finally:
        manifest.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    checksums = []
    for path in sorted(destination.rglob("*")):
        if path.is_file() and path.name != "SHA256SUMS":
            checksums.append(f"{sha256(path)}  {path.relative_to(destination).as_posix()}\n")
    (destination / "SHA256SUMS").write_text("".join(checksums))
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()
    report = convert_mod(args.source, args.destination, args.workers)
    print(json.dumps({k: v for k, v in report.items() if k != "files"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
