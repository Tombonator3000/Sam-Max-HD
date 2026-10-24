"""Regression checks for accidental developer payload and expanding archives."""
import importlib.util
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

import pytest

spec = importlib.util.spec_from_file_location(
    "package_size", Path(__file__).resolve().parents[2] / "tools/kontroller_pakkestorrelse.py"
)
package_size = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_size)


def test_measures_installed_and_download_separately(tmp_path):
    folder = tmp_path / "AppDir"
    folder.mkdir()
    (folder / "AppRun").write_bytes(b"runtime")
    archive = tmp_path / "game.AppImage"
    archive.write_bytes(b"compressed")
    result = package_size.check_package(folder, archive)
    assert result["ok"]
    assert result["utpakket_byte"] == 7
    assert result["nedlasting_byte"] == 10


def test_zip_expansion_counts_uncompressed_size(tmp_path):
    archive = tmp_path / "game.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        bundle.writestr("SamMaxHD/game/MONSTER.SOU", b"a" * 100_000)
    result = package_size.check_package(archive, max_unpacked=99_999)
    assert not result["ok"]
    assert result["utpakket_byte"] == 100_000
    assert result["nedlasting_byte"] < 1000


@pytest.mark.parametrize("name", [".git/objects/pack/data.pack", "work/job/raa.png",
                                   "out/old/frame.png", "rapporter/frame.png"])
def test_rejects_development_payload_in_zip(tmp_path, name):
    archive = tmp_path / "game.zip"
    with ZipFile(archive, "w") as bundle:
        bundle.writestr("SamMaxHD/" + name, b"x")
    assert not package_size.check_package(archive)["ok"]


def test_rejects_hidden_work_directory_in_appdir(tmp_path):
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git/config").write_text("developer checkout")
    assert not package_size.check_package(tmp_path)["ok"]


def test_download_limit_is_separate_from_installed_limit(tmp_path):
    archive = tmp_path / "game.zip"
    with ZipFile(archive, "w") as bundle:
        bundle.writestr("SamMaxHD/mod/picture.webp", b"x")
    assert not package_size.check_package(archive, max_download=10)["ok"]


def test_rejects_external_symlink_without_following_it(tmp_path):
    folder = tmp_path / "AppDir"
    folder.mkdir()
    (folder / "AppRun").symlink_to(tmp_path / "outside")
    assert not package_size.check_package(folder)["ok"]


def test_rejects_empty_runtime(tmp_path):
    assert not package_size.check_package(tmp_path)["ok"]
