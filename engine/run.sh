#!/usr/bin/env bash
# Starter Sam & Max med en HD-mod.
#
# Bruk:  engine/run.sh [modnavn] [flere ScummVM-valg]
#        engine/run.sh hd
#        engine/run.sh ingen          (uten mod, slik spillet går nå)
#
# Modmappen er mods/<modnavn>. Spillfilene ligger i game/ (tools/hent_spilldata.sh).
# Talen: tools/hent_spilldata.sh setter sammen MONSTER.SOU i game/.
#
# Merk: HD-delen av patchen (DigHD) er bare slått på for The Dig til den er portet til
# SCUMM v6. Til da kjører Sam & Max som originalen, også med en mod.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
SRC="${SCUMMVM_SRC:-$HERE/scummvm}"
MOD="${1:-hd}"
shift || true

[ -x "$SRC/scummvm" ] || { echo "Fant ikke $SRC/scummvm. Kjør engine/build.sh først."; exit 1; }
[ -f "$ROOT/game/SAMNMAX.001" ] || { echo "Fant ikke spillfilene. Kjør tools/hent_spilldata.sh først."; exit 1; }
[ -f "$ROOT/game/MONSTER.SOU" ] || echo "Merk: MONSTER.SOU mangler i game/, spillet blir uten tale."

if [ "$MOD" != "ingen" ]; then
	[ -d "$ROOT/mods/$MOD" ] || { echo "Fant ikke mods/$MOD. Lag den med: smhd build-mod --name $MOD (eller bruk engine/run.sh ingen)"; exit 1; }
	export DIGHD_MOD="$ROOT/mods/$MOD"
fi
exec "$SRC/scummvm" --path="$ROOT/game" --gfx-mode=opengl --aspect-ratio "$@" samnmax
