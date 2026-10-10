#!/usr/bin/env bash
# Lager den komplette Linux-pakken: én AppImage med ScummVM med HD-patchen, spillfilene,
# talen og HD-modden. Pakken starter rett i spillet.
#
# Merk: HD-delen av patchen er bare slått på for The Dig til den er portet til SCUMM v6, og det
# finnes ingen HD-mod for Sam & Max ennå. Til da gir pakken originalspillet i den samme motoren.
#
#   tools/pakke_linux.sh [utmappe]          standard out/linux
#
# Krever:
#   engine/scummvm/scummvm (eller SCUMMVM_SRC)   bygget med engine/build.sh
#   game/ med SAMNMAX.000, SAMNMAX.001 og MONSTER.SOU   (tools/hent_spilldata.sh)
#   mods/gpt, hvis den finnes                 (tools/mod_gren.sh hent)
#   LINUXDEPLOY og APPIMAGETOOL: stier til linuxdeploy og appimagetool. Uten dem lages bare
#   AppDir-mappen (den kan startes med AppDir/AppRun).
#
# Pakken inneholder spillet, som tilhører Disney/Lucasfilm. Den ligger som release i dette repoet.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${SCUMMVM_SRC:-$ROOT/engine/scummvm}"
OUT="${1:-$ROOT/out/linux}"
APPDIR="$OUT/AppDir"
NAVN="SamMaxHD-x86_64.AppImage"

[ -x "$SRC/scummvm" ] || { echo "Fant ikke $SRC/scummvm. Kjør engine/build.sh først."; exit 1; }
for f in SAMNMAX.000 SAMNMAX.001 MONSTER.SOU; do
	[ -f "$ROOT/game/$f" ] || { echo "Fant ikke game/$f. Kjør tools/hent_spilldata.sh først."; exit 1; }
done
MED_MOD=0
[ -f "$ROOT/mods/gpt/mod.json" ] && MED_MOD=1 || echo "Merk: ingen HD-mod i mods/gpt. Pakken lages uten."

echo "Sjekker spillfilene ..."
(cd "$ROOT/game" && sha256sum --quiet -c SHA256SUMS)
if [ "$MED_MOD" = 1 ] && [ -f "$ROOT/mods/gpt/SHA256SUMS" ]; then (cd "$ROOT/mods/gpt" && sha256sum --quiet -c SHA256SUMS); fi

rm -rf "$APPDIR"
DATA="$APPDIR/usr/share/sam-max-hd"
mkdir -p "$APPDIR/usr/bin" "$DATA/game" "$DATA/mods"

echo "Kopierer motoren, spillet, talen og HD-modden ..."
install -m 755 "$SRC/scummvm" "$APPDIR/usr/bin/scummvm"
strip "$APPDIR/usr/bin/scummvm" 2>/dev/null || true
cp "$ROOT/game/SAMNMAX.000" "$ROOT/game/SAMNMAX.001" "$ROOT/game/MONSTER.SOU" "$DATA/game/"
if [ "$MED_MOD" = 1 ]; then
	cp -r "$ROOT/mods/gpt" "$DATA/mods/gpt"
	rm -f "$DATA/mods/gpt/README.md"
fi
# ScummVM sine temaer og hjelpefiler (menyene i ScummVM selv), samme liste som engine/build-pages.py
for name in achievements.dat classicmacfonts.dat encoding.dat gui-icons.dat helpdialog.zip macgui.dat \
	residualvm.zip scummclassic.zip scummmodern.zip scummremastered.zip shaders.dat translations.dat; do
	for dir in gui/themes dists/engine-data dists; do
		[ -f "$SRC/$dir/$name" ] && { cp "$SRC/$dir/$name" "$DATA/"; break; }
	done
done
cp "$SRC/COPYING" "$DATA/COPYING-ScummVM.txt"
cp "$SRC/COPYRIGHT" "$DATA/COPYRIGHT-ScummVM.txt"

# Hva pakken er bygget av
{
	echo "Sam & Max HD for Linux"
	echo "Bygget: $(date -u '+%Y-%m-%d %H:%M UTC')"
	echo "ScummVM: $(cat "$ROOT/engine/SCUMMVM_COMMIT") med engine/patches/"
	echo "Sam-Max-HD: $(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo ukjent)"
	echo "hd-mod: $(git -C "$ROOT" rev-parse --verify -q refs/remotes/origin/hd-mod || echo ukjent)"
	if [ "$MED_MOD" = 1 ]; then
		echo "HD-mod laget: $(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("created", "ukjent"))' "$ROOT/mods/gpt/mod.json")"
	else
		echo "HD-mod: ingen (originalgrafikk)"
	fi
} > "$DATA/BYGG.txt"

# Oppstarten: rett i spillet, med innstillinger og lagrede spill i hjemmemappen
cat > "$OUT/AppRun" <<'EOF'
#!/bin/sh
# Sam & Max HD: starter spillet rett, med HD-grafikk (når den finnes), musikk og tale.
# Innstillinger: ~/.config/sam-max-hd/scummvm.ini. Lagrede spill: ~/.local/share/sam-max-hd/saves.
HERE="$(dirname "$(readlink -f "$0")")"
DATA="$HERE/usr/share/sam-max-hd"
CONF="${XDG_CONFIG_HOME:-$HOME/.config}/sam-max-hd"
SAVES="${XDG_DATA_HOME:-$HOME/.local/share}/sam-max-hd/saves"
mkdir -p "$CONF" "$SAVES"
if [ ! -f "$CONF/scummvm.ini" ]; then
	cat > "$CONF/scummvm.ini" <<INI
[scummvm]
fullscreen=true
aspect_ratio=true
subtitles=true
gui_return_to_launcher_at_exit=false
confirm_exit=false

[samnmax]
description=Sam & Max HD
engineid=scumm
gameid=samnmax
subtitles=true
INI
fi
[ -d "$DATA/mods/gpt" ] && export DIGHD_MOD="${DIGHD_MOD:-$DATA/mods/gpt}"
export LD_LIBRARY_PATH="$HERE/usr/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
exec "$HERE/usr/bin/scummvm" --config="$CONF/scummvm.ini" --path="$DATA/game" --savepath="$SAVES" \
	--themepath="$DATA" --extrapath="$DATA" "$@" samnmax
EOF
chmod 755 "$OUT/AppRun"

cat > "$OUT/sam-max-hd.desktop" <<'EOF'
[Desktop Entry]
Type=Application
Name=Sam & Max HD
Comment=Sam & Max Hit the Road med HD-grafikk, musikk og tale
Exec=sam-max-hd
Icon=sam-max-hd
Categories=Game;AdventureGame;
Terminal=false
EOF
cp "$SRC/icons/scummvm.svg" "$OUT/sam-max-hd.svg"

if [ -z "${LINUXDEPLOY:-}" ] || [ -z "${APPIMAGETOOL:-}" ]; then
	cp "$OUT/AppRun" "$OUT/sam-max-hd.desktop" "$OUT/sam-max-hd.svg" "$APPDIR/"
	echo "Ferdig: $APPDIR (uten LINUXDEPLOY og APPIMAGETOOL blir det ingen AppImage). Start med $APPDIR/AppRun"
	exit 0
fi

echo "Tar med bibliotekene motoren trenger (linuxdeploy) ..."
"$LINUXDEPLOY" --appdir "$APPDIR" --executable "$APPDIR/usr/bin/scummvm" \
	--desktop-file "$OUT/sam-max-hd.desktop" --icon-file "$OUT/sam-max-hd.svg" \
	--custom-apprun "$OUT/AppRun" > "$OUT/linuxdeploy.log" 2>&1 \
	|| { tail -20 "$OUT/linuxdeploy.log"; exit 1; }
cmp -s "$OUT/AppRun" "$APPDIR/AppRun" || { echo "AppRun i AppDir er ikke vår"; exit 1; }

echo "Lager AppImage ..."
rm -f "$OUT/$NAVN"
ARCH=x86_64 "$APPIMAGETOOL" --no-appstream "$APPDIR" "$OUT/$NAVN" > "$OUT/appimagetool.log" 2>&1 \
	|| { tail -20 "$OUT/appimagetool.log"; exit 1; }
(cd "$OUT" && sha256sum "$NAVN" > "$NAVN.sha256")
echo "Ferdig: $OUT/$NAVN ($(du -h "$OUT/$NAVN" | cut -f1))"
