#!/usr/bin/env python3
"""Bygg en WebP-mod og sammenlign faktisk avspilling med PNG i samme motor.

Kontrollerte scener med rom, objekter og myke figurer. Dette er en formattest,
ikke en ny godkjenning av tegningene eller en full gjennomspilling.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

from PIL import Image
from smhd import gamedata
from smhd.webp import convert_mod


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    source = Path(os.environ.get("WEBP_TEST_MOD", root / "mods/gpt")).resolve()
    game = Path(os.environ.get("WEBP_TEST_GAME", root / "game")).resolve()
    binary = Path(os.environ.get("WEBP_TEST_BINARY", root / "engine/scummvm/scummvm")).resolve()
    out = Path(os.environ.get("WEBP_TEST_OUT", root / "out/webp-test")).resolve()
    out.mkdir(parents=True, exist_ok=True)
    # Keep the real scene assets, without spending every CI run encoding the
    # entire production library. A full migration is verified separately.
    published = source
    rooms = gamedata.read_rooms(game / "SAMNMAX.001")
    object_ids = {obj.obj_id for room in (7, 9, 35) for obj in rooms[room].objects}
    source = out / "png-input"
    source.mkdir()
    for path in sorted(published.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(published).as_posix()
        object_match = re.match(r"objects/obj(\d+)_", relative)
        if not (relative == "mod.json" or relative.startswith("fonts/") or
                (object_match and int(object_match[1]) in object_ids) or
                re.fullmatch(r"rooms/room(?:007|009|035)(?:_idx|_mask)?\.(?:png|webp)", relative) or
                re.fullmatch(r"costumes/costume(?:001|178)_\d+(?:_hd|_idx|_mask)?\.(?:png|webp)", relative)):
            continue
        dest = source / relative
        dest.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".webp":
            with Image.open(path) as image:
                image.convert("RGBA").save(dest.with_suffix(".png"))
        else:
            shutil.copy2(path, dest)
    target = out / "mod-webp"
    print("Konverterer formatprøven", flush=True)
    migration = convert_mod(source, target, workers=min(4, os.cpu_count() or 2))
    scenes = [(7, 1), (9, 1), (35, 178)]
    comparisons = []
    for room, costume in scenes:
        images = []
        for kind, mod in (("png", source), ("webp", target)):
            print(f"Avspilling rom {room}, {kind}", flush=True)
            work = out / f"room{room}-{kind}"
            work.mkdir()
            (work / "saves").mkdir()
            env = {key: value for key, value in os.environ.items() if not key.startswith("DIGHD_")}
            env.update(HOME=str(work), XDG_CONFIG_HOME=str(work / ".config"), XDG_DATA_HOME=str(work / ".local/share"),
                       SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy", DIGHD_MOD=str(mod),
                       DIGHD_VERIFY="1", DIGHD_SKIP_VIDEO="1", DIGHD_QUIT_AT="200",
                       DIGHD_DUMP_DIR=str(work), DIGHD_DUMP_EVERY="20", DIGHD_DUMP_FLAT="1",
                       DIGHD_TEST_ROOM=str(room), DIGHD_TEST_AT="10", DIGHD_TEST_CAMX="160",
                       DIGHD_TEST_COSTUME=str(costume), DIGHD_TEST_ACTOR="29", DIGHD_TEST_STATIC_SCENE="1",
                       DIGHD_TEST_CHORE_EVERY="500", DIGHD_TEST_ANIMATION="1", DIGHD_TEST_POS="160,120",
                       DIGHD_TEST_SCALE="255", DIGHD_TEST_CLIP="0", DIGHD_MANGLER="0")
            command = [str(binary), "--config=" + str(work / "scummvm.ini"), "--path=" + str(game),
                       "--savepath=" + str(work / "saves"), "--gfx-mode=surfacesdl", "--no-fullscreen",
                       "--gui-theme=builtin", "--music-driver=null", "--random-seed=20261023", "--debuglevel=3", "samnmax"]
            with (work / "scummvm.log").open("wb") as log:
                subprocess.run(command, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=300, check=True)
            log = (work / "scummvm.log").read_text(errors="replace")
            if f"actor 29 with costume {costume}" not in log or f"room {room}" not in log:
                raise RuntimeError(f"Testscenen ble ikke nådd: {work}")
            if kind == "webp" and "DigHD: WebP " not in log:
                raise RuntimeError("Ingen WebP-bilder ble lastet av motoren")
            if "invalid WebP" in log or "Couldn't save file" in log:
                raise RuntimeError(f"Dekoding eller lagring feilet: {work}")
            images.append({p.name: p for p in work.glob(f"frame_*_room{room:03}.png") if int(p.name[6:12]) >= 100})
        shared = sorted(images[0].keys() & images[1].keys())
        if len(shared) < 4:
            raise RuntimeError(f"For få sammenlignbare bilder i rom {room}")
        for name in shared:
            with Image.open(images[0][name]) as a, Image.open(images[1][name]) as b:
                same = a.size == b.size and a.convert("RGBA").tobytes() == b.convert("RGBA").tobytes()
                comparisons.append({"room": room, "frame": name, "rgba_equal": same,
                                    "png_sha256": hashlib.sha256(images[0][name].read_bytes()).hexdigest(),
                                    "webp_sha256": hashlib.sha256(images[1][name].read_bytes()).hexdigest()})
    report = {"fixture_subset_of_published_mod": True,
              "colour_images_exact": sum(row.get("rgba_exact", False) for row in migration["files"]),
              "converted": migration["converted"], "comparisons": comparisons,
              "all_frames_equal": all(row["rgba_equal"] for row in comparisons)}
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    if not report["all_frames_equal"]:
        raise RuntimeError("PNG og WebP ga forskjellige motorbilder; se report.json")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
