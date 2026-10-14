#!/usr/bin/env bash
# Lager Windows-pakken: én zip med ScummVM med HD-patchen, bibliotekene den trenger, spillfilene,
# talen og HD-modden. Pakk ut og start «Sam og Max HD.bat».
#
#   tools/pakke_windows.sh [utmappe]          standard out/windows
#
# Kjøres i MSYS2 (MINGW64) på Windows, slik arbeidsflyten Windows-pakke gjør. Krever:
#   engine/scummvm/scummvm.exe          bygget med engine/build.sh i MSYS2
#   game/ med SAMNMAX.000, SAMNMAX.001 og MONSTER.SOU   (tools/hent_spilldata.sh)
#   mods/gpt                             (tools/mod_gren.sh hent)
#
# Pakken inneholder spillet og HD-grafikken, som tilhører Disney/Lucasfilm. Den legges som release
# i dette repoet etter Toms beslutning 14. oktober 2026 (se AGENTS.md).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${SCUMMVM_SRC:-$ROOT/engine/scummvm}"
OUT="${1:-$ROOT/out/windows}"
NAVN="SamMaxHD-Windows"
DIR="$OUT/$NAVN"

[ -f "$SRC/scummvm.exe" ] || { echo "Fant ikke $SRC/scummvm.exe. Kjør engine/build.sh i MSYS2 først."; exit 1; }
for f in SAMNMAX.000 SAMNMAX.001 MONSTER.SOU; do
	[ -f "$ROOT/game/$f" ] || { echo "Fant ikke game/$f. Kjør tools/hent_spilldata.sh først."; exit 1; }
done
[ -f "$ROOT/mods/gpt/mod.json" ] || { echo "Fant ikke mods/gpt. Kjør tools/mod_gren.sh hent først."; exit 1; }

echo "Sjekker spillfilene og HD-modden ..."
(cd "$ROOT/game" && sha256sum --quiet -c SHA256SUMS)
(cd "$ROOT/mods/gpt" && sha256sum --quiet -c SHA256SUMS)

rm -rf "$OUT"
mkdir -p "$DIR/game" "$DIR/mod"

echo "Kopierer motoren og bibliotekene ..."
cp "$SRC/scummvm.exe" "$DIR/"
strip "$DIR/scummvm.exe" 2>/dev/null || true
# DLL-ene fra MSYS2 som motoren lenker mot (SDL2, libpng, zlib, FreeType og det de trenger)
ldd "$DIR/scummvm.exe" | awk '/\/mingw64\// {print $3}' | sort -u | while read -r dll; do cp "$dll" "$DIR/"; done
ls "$DIR"/*.dll > /dev/null 2>&1 || { echo "Fant ingen DLL-er fra MSYS2. Er motoren bygget i MINGW64?"; exit 1; }

# ScummVM sine temaer og hjelpefiler (menyene i ScummVM selv), samme liste som Linux-pakken
for name in achievements.dat classicmacfonts.dat encoding.dat gui-icons.dat helpdialog.zip macgui.dat \
	residualvm.zip scummclassic.zip scummmodern.zip scummremastered.zip shaders.dat translations.dat; do
	for dir in gui/themes dists/engine-data dists; do
		[ -f "$SRC/$dir/$name" ] && { cp "$SRC/$dir/$name" "$DIR/"; break; }
	done
done
cp "$SRC/COPYING" "$DIR/COPYING-ScummVM.txt"
cp "$SRC/COPYRIGHT" "$DIR/COPYRIGHT-ScummVM.txt"

echo "Kopierer spillet, talen og HD-modden ..."
cp "$ROOT/game/SAMNMAX.000" "$ROOT/game/SAMNMAX.001" "$ROOT/game/MONSTER.SOU" "$DIR/game/"
cp -r "$ROOT/mods/gpt"/. "$DIR/mod/"
rm -f "$DIR/mod/README.md"

# Startfila må ha CRLF på Windows
sed 's/\r*$/\r/' "$ROOT/tools/windows/Sam og Max HD.bat" > "$DIR/Sam og Max HD.bat"

{
	echo "Sam & Max HD for Windows"
	echo "Bygget: $(date -u '+%Y-%m-%d %H:%M UTC')"
	echo "ScummVM: $(cat "$ROOT/engine/SCUMMVM_COMMIT") med engine/patches/"
	echo "Sam-Max-HD: $(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo ukjent)"
	echo "hd-mod: $(git -C "$ROOT" rev-parse --verify -q refs/remotes/origin/hd-mod || echo ukjent)"
	echo "HD-mod laget: $(sed -n 's/.*"created": *"\([^"]*\)".*/\1/p' "$ROOT/mods/gpt/mod.json")"
} | sed 's/$/\r/' > "$DIR/BYGG.txt"

cat <<'EOF' | sed 's/$/\r/' > "$DIR/LES MEG.txt"
Sam & Max HD for Windows

Start "Sam og Max HD.bat". Spillet starter rett, i fullskjerm, med HD-grafikk, musikk og tale.

I spillet:
  F5            spillets meny, med valget HD Graphics
  Ctrl+H        bytter mellom HD og originalgrafikk (valget huskes)
  Ctrl+Shift+H  gult felt der HD mangler
  Alt+Enter     vindu og fullskjerm

HD-grafikken lages fortsatt. Det som ikke er tegnet i HD ennå, vises som originalen.
Innstillinger og lagrede spill: %APPDATA%\SamMaxHD

Spillet og grafikken tilhører Disney/Lucasfilm. Motoren er ScummVM (GPL), se COPYING-ScummVM.txt.
EOF

echo "Lager zip ..."
(cd "$OUT" && rm -f "$NAVN.zip" && zip -qr -9 "$NAVN.zip" "$NAVN" && sha256sum "$NAVN.zip" > "$NAVN.zip.sha256")
echo "Ferdig: $OUT/$NAVN.zip ($(du -h "$OUT/$NAVN.zip" | cut -f1))"
