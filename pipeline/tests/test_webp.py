import hashlib
import json

import pytest
from PIL import Image

from smhd.webp import convert_image, convert_mod


def test_rgba_lossless_including_transparent_rgb(tmp_path):
    image = Image.new("RGBA", (64, 64))
    image.putdata([(27, 183, i % 256, i % 4 * 85) for i in range(64 * 64)])
    source, target = tmp_path / "source.png", tmp_path / "target.webp"
    image.save(source, compress_level=0)
    original = source.read_bytes()
    row = convert_image(source, target)
    assert row["rgba_exact"] and row["extension"] == ".webp"
    with Image.open(target) as result:
        assert result.convert("RGBA").tobytes() == image.tobytes()
    assert source.read_bytes() == original


def test_mod_preserves_indices_masks_and_metadata(tmp_path):
    source, target = tmp_path / "source", tmp_path / "target"
    (source / "costumes").mkdir(parents=True)
    (source / "mod.json").write_text(json.dumps({"format": 1, "scale": 4, "costume_cels": 1}))
    index = Image.new("P", (20, 20), 7)
    index.putpalette([0, 0, 0] * 256)  # duplicate RGB entries must retain their indices
    index.save(source / "costumes/costume001_001_idx.png", transparency=9)
    mask = Image.new("L", (20, 20), 255)
    mask.save(source / "costumes/costume001_001_mask.png")
    Image.new("RGBA", (80, 80), (41, 19, 91, 85)).save(source / "costumes/costume001_001_hd.png", compress_level=0)
    report = convert_mod(source, target)
    assert report["complete"] and report["converted"] == 1
    assert (target / "mod.json").read_bytes() == (source / "mod.json").read_bytes()
    for suffix in ("idx", "mask"):
        relative = f"costumes/costume001_001_{suffix}.png"
        assert (target / relative).read_bytes() == (source / relative).read_bytes()
    assert not (target / "costumes/costume001_001_hd.png").exists()
    for line in (target / "SHA256SUMS").read_text().splitlines():
        digest, relative = line.split("  ")
        assert hashlib.sha256((target / relative).read_bytes()).hexdigest() == digest
    with pytest.raises(FileExistsError):
        convert_mod(source, target)
    with pytest.raises(ValueError):
        convert_mod(source, source / "nested")


def test_ambiguous_pair_and_16bit_are_rejected(tmp_path):
    source = tmp_path / "source"
    (source / "rooms").mkdir(parents=True)
    (source / "mod.json").write_text('{"format":1,"scale":4}')
    image = source / "rooms/room007.png"
    Image.new("I;16", (4, 4)).save(image)
    with pytest.raises(ValueError, match="PNG-type"):
        convert_image(image, tmp_path / "image.webp")
    image.with_suffix(".webp").touch()
    with pytest.raises(ValueError, match="Både"):
        convert_mod(source, tmp_path / "target")
