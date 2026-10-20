"""Source drawing coverage must survive export and HD mod assembly."""
import struct

from PIL import Image
import pytest

from smhd import eksport_v6, modpack, v6grafikk


def test_v6_coverage_keeps_opaque_black_beside_transparent_black(tmp_path):
    # Both source strips contain palette index zero. RAW paints it; TPIX
    # skips it. A palette-colour comparison cannot recover this distinction.
    body = struct.pack("<II", 16, 25) + bytes([1] + [0] * 8) + bytes([149] + [0] * 8)
    smap = b"SMAP" + struct.pack(">I", len(body) + 8) + body
    bitmap = v6grafikk.decode_smap(smap, 0, 16, 1, 0)
    transparent = eksport_v6._transparent_index(bitmap.pixels, bitmap.mask, 0)
    eksport_v6._save_pair(tmp_path, "obj001_01", 16, 1, bitmap.pixels, bitmap.mask,
                          bytes(768), transparent, coverage=True)
    with Image.open(tmp_path / "obj001_01_mask.png") as mask:
        assert mask.tobytes() == bytes([255] * 8 + [0] * 8)
    with Image.open(tmp_path / "obj001_01.png") as source:
        assert source.getpixel((0, 0)) == (0, 0, 0, 255)
        assert source.getpixel((8, 0)) == (0, 0, 0, 0)


@pytest.mark.parametrize("explicit_mask", [False, True])
def test_mod_coverage_uses_original_not_transparent_hd_art(tmp_path, explicit_mask):
    extract, own, out = (tmp_path / p for p in ("extract", "own", "mod"))
    for directory in (extract, own, out):
        (directory / "objects").mkdir(parents=True)
    name = "obj901_01"
    idx = Image.new("P", (8, 2), 1)
    idx.putpalette([0, 0, 0, 200, 40, 10] + [0] * 762)
    idx.save(extract / "objects" / f"{name}_idx.png")
    # An opaque red erase tile can have the very same original index as
    # the room. It must still claim its full area in the HD renderer.
    source = Image.new("RGBA", (8, 2), (200, 40, 10, 255))
    source.save(extract / "objects" / f"{name}.png")
    if explicit_mask:
        source.getchannel("A").save(extract / "objects" / f"{name}_mask.png")
    Image.new("RGBA", (32, 8), (0, 0, 0, 0)).save(own / "objects" / f"{name}.png")
    modpack._copy_idx(extract, own, out, name)
    with Image.open(out / "objects" / f"{name}_mask.png") as mask:
        assert mask.size == (8, 2) and mask.getextrema() == (255, 255)
    if explicit_mask:
        assert (out / "objects" / f"{name}_mask.png").read_bytes() == \
               (extract / "objects" / f"{name}_mask.png").read_bytes()


def test_mod_rejects_coverage_for_different_source_dimensions(tmp_path):
    extract, out = tmp_path / "extract", tmp_path / "mod"
    for directory in (extract, out):
        (directory / "objects").mkdir(parents=True)
    idx = Image.new("P", (8, 2))
    idx.putpalette([0] * 768)
    idx.save(extract / "objects/obj001_01_idx.png")
    Image.new("L", (4, 2), 255).save(extract / "objects/obj001_01_mask.png")
    with pytest.raises(ValueError, match="tegnedekning"):
        modpack._copy_idx(extract, None, out, "obj001_01")
