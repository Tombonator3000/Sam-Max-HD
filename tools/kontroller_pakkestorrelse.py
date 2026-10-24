#!/usr/bin/env python3
"""Stopp spillerpakker som blir for store eller inneholder arbeidsdata."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PurePosixPath
import stat
from zipfile import ZipFile

MAX_DOWNLOAD = 1_000_000_000
MAX_UNPACKED = 2_000_000_000
DEVELOPMENT_DIRS = {
    ".git", ".github", ".venv", "node_modules", "__pycache__",
    "out", "work", "jobber", "rapporter", "hovedark", "kall",
}


def invalid_name(name: str) -> str | None:
    path = PurePosixPath(name.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts:
        return "Ugyldig pakkesti: " + name
    if any(part.casefold() in DEVELOPMENT_DIRS for part in path.parts):
        return "Arbeidsdata i spillerpakken: " + name
    return None


def check_package(package: Path, archive: Path | None = None,
                  max_download: int = MAX_DOWNLOAD,
                  max_unpacked: int = MAX_UNPACKED) -> dict:
    errors = []
    entries = []
    if package.is_dir():
        root = package.resolve()
        for parent, dirs, files in os.walk(root, followlinks=False):
            for name in dirs + files:
                path = Path(parent) / name
                relative = path.relative_to(root).as_posix()
                if error := invalid_name(relative):
                    errors.append(error)
                if path.is_symlink():
                    if not path.resolve().is_relative_to(root):
                        errors.append("Lenke utenfor spillerpakken: " + relative)
                    entries.append((relative, path.lstat().st_size))
                elif path.is_file():
                    entries.append((relative, path.stat().st_size))
        download = archive.stat().st_size if archive else None
    else:
        if archive is not None:
            raise ValueError("--arkiv brukes bare sammen med en utpakket mappe")
        with ZipFile(package) as bundle:
            for info in bundle.infolist():
                if error := invalid_name(info.filename):
                    errors.append(error)
                # A ZIP symlink can point outside the package after extraction.
                if stat.S_ISLNK(info.external_attr >> 16):
                    errors.append("Symbolsk lenke i Windows-pakken: " + info.filename)
                if not info.is_dir():
                    entries.append((info.filename, info.file_size))
        download = package.stat().st_size
    unpacked = sum(size for _, size in entries)
    if not entries:
        errors.append("Spillerpakken er tom")
    if unpacked > max_unpacked:
        errors.append(f"Utpakket pakke {unpacked} byte overstiger {max_unpacked}")
    if download is not None and download > max_download:
        errors.append(f"Nedlasting {download} byte overstiger {max_download}")
    return {
        "ok": not errors, "pakke": str(package), "filer": len(entries),
        "nedlasting_byte": download, "utpakket_byte": unpacked,
        "maks_nedlasting_byte": max_download, "maks_utpakket_byte": max_unpacked,
        "feil": sorted(set(errors)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pakke", type=Path, help="Pakkemappe eller Windows-ZIP")
    parser.add_argument("--arkiv", type=Path, help="Ferdig AppImage til pakkemappen")
    parser.add_argument("--rapport", type=Path)
    parser.add_argument("--maks-nedlasting-mb", type=int, default=1000)
    parser.add_argument("--maks-utpakket-mb", type=int, default=2000)
    args = parser.parse_args()
    if args.maks_nedlasting_mb <= 0 or args.maks_utpakket_mb <= 0:
        parser.error("Størrelsesgrensene må være positive")
    result = check_package(args.pakke, args.arkiv,
                           args.maks_nedlasting_mb * 1_000_000,
                           args.maks_utpakket_mb * 1_000_000)
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.rapport:
        args.rapport.write_text(text)
    print(text, end="")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
