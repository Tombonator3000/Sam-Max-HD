#!/usr/bin/env bash
# Bygger ScummVM med HD-patchen fra The Dig HD (DigHD) for nettleseren (WebAssembly med Emscripten).
# Patchen er foreløpig bare slått på for The Dig, så Sam & Max kjører uten HD i denne motoren.
#
# Resultatet kjøres lokalt med engine/run-web.sh på http://localhost:8000.
# engine/build-pages.py lager en egen offentlig motorpakke som leser private filer
# fra nettleserens lokale lagring. Spillfilene og HD-grafikken skal aldri publiseres.
#
# Følger ScummVM sin egen oppskrift (dists/emscripten/build.sh på den låste commiten):
# samme Emscripten-versjon, configure med --host=wasm32-unknown-emscripten, make og
# make dist-emscripten. Bare SCUMM-motoren, som i engine/build.sh.
#
# Krever: git, make, python3, pkg-config, tar, xz og zip. Emscripten (emsdk) installeres i
# engine/emsdk første gang (omtrent 350 MB). ScummVM sin configure bruker pkg-config for SDL3,
# og make dist-emscripten bruker zip.
#
# Bruk:  engine/build-web.sh        (kildekoden havner i engine/scummvm-web, resultatet i
#                                    engine/scummvm-web/build-emscripten)
#        SCUMMVM_WEB_SRC=/annen/mappe EMSDK_DIR=/annen/emsdk engine/build-web.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="${SCUMMVM_WEB_SRC:-$HERE/scummvm-web}"
EMSDK_DIR="${EMSDK_DIR:-$HERE/emsdk}"
COMMIT="$(cat "$HERE/SCUMMVM_COMMIT")"
JOBS="${JOBS:-$(nproc 2>/dev/null || echo 2)}"

# 1. Kildekoden: samme commit og samme patch som den vanlige motoren
if [ ! -d "$SRC/.git" ]; then
	echo "Henter ScummVM ($COMMIT) til $SRC ..."
	git init -q "$SRC"
	git -C "$SRC" remote add origin https://github.com/scummvm/scummvm
fi
git -C "$SRC" fetch -q --depth 1 origin "$COMMIT"
git -C "$SRC" checkout -q -f FETCH_HEAD
git -C "$SRC" clean -fdq engines/scumm

echo "Legger på patcher ..."
for p in "$HERE"/patches/*.patch; do
	git -C "$SRC" apply --whitespace=nowarn "$p"
	echo "  $(basename "$p")"
done

# 2. Emscripten: versjonen ScummVM sin egen byggeoppskrift bruker på denne commiten
EMSDK_VERSION="${EMSDK_VERSION:-$(sed -n 's/^EMSDK_VERSION="\${EMSDK_VERSION:-\([0-9.]*\)}"$/\1/p' "$SRC/dists/emscripten/build.sh")}"
EMSDK_VERSION="${EMSDK_VERSION:-4.0.10}"
if [ ! -x "$EMSDK_DIR/emsdk" ]; then
	echo "Henter emsdk til $EMSDK_DIR ..."
	git clone -q https://github.com/emscripten-core/emsdk "$EMSDK_DIR"
fi
if [ "$(cat "$EMSDK_DIR/.dighd-versjon" 2>/dev/null || true)" != "$EMSDK_VERSION" ]; then
	echo "Installerer Emscripten $EMSDK_VERSION (første gang laster den ned omtrent 350 MB) ..."
	(cd "$EMSDK_DIR" && { ./emsdk install "$EMSDK_VERSION" || { git pull -q && ./emsdk install "$EMSDK_VERSION"; }; } && ./emsdk activate "$EMSDK_VERSION") > "$EMSDK_DIR/install.log" 2>&1 \
		|| { tail -20 "$EMSDK_DIR/install.log"; echo "Installasjonen av Emscripten feilet, se $EMSDK_DIR/install.log"; exit 1; }
	echo "$EMSDK_VERSION" > "$EMSDK_DIR/.dighd-versjon"
fi
# shellcheck disable=SC1091
EMSDK_QUIET=1 source "$EMSDK_DIR/emsdk_env.sh"

# 3. Konfigurer og bygg
cd "$SRC"
if [ ! -f config.mk ] || [ "${RECONFIGURE:-0}" = "1" ]; then
	echo "Konfigurerer for nettleseren (bare SCUMM-motoren) ..."
	# Emscripten slår av valgfrie biblioteker som ikke er slått på; DigHD trenger PNG og zlib.
	# Sam & Max (SCUMM v6) trenger ikke scumm-7-8, men dighd.cpp bruker ScummEngine_v7 uten
	# #ifdef, og scumm_v7.h er tom uten ENABLE_SCUMM_7_8. Valget står derfor som før.
	# Valgene er ellers de samme som for The Dig, som ikke bruker MIDI. For Sam & Max, som har
	# MIDI-musikk, er de ikke vurdert eller testet: --disable-mt32emu betyr at MT32_CONTROL.ROM
	# og MT32_PCM.ROM ikke brukes, og --disable-fluidsynth at FluidSynth (General MIDI) ikke er
	# med. Nettsidene stopper i tillegg Web MIDI (requestMIDIAccess), så musikken faller trolig
	# tilbake til AdLib-emuleringen. Vurder --enable-mt32emu når musikken skal testes.
	emconfigure ./configure --host=wasm32-unknown-emscripten --build=wasm32-unknown-emscripten \
		--disable-all-engines --enable-engine=scumm,scumm-7-8 \
		--disable-engine=he,rebel2-psx --disable-detection-full \
		--disable-debug --enable-optimizations \
		--enable-png --enable-zlib \
		--disable-mt32emu --disable-fluidsynth --disable-cloud --disable-libcurl \
		--disable-sdlnet --disable-tts --disable-eventrecorder > configure.log 2>&1 \
		|| { tail -30 configure.log; echo "Konfigureringen feilet, se $SRC/configure.log"; exit 1; }
	rm -f scummvm-conf.*
fi

echo "Bygger med $JOBS tråder (første gang tar det noen minutter) ..."
emmake make -j"$JOBS" > build.log 2>&1 || { tail -30 build.log; echo "Bygging feilet, se $SRC/build.log"; exit 1; }
rm -rf build-emscripten
emmake make dist-emscripten >> build.log 2>&1 || { tail -30 build.log; echo "Pakkingen feilet, se $SRC/build.log"; exit 1; }
echo "Ferdig: $SRC/build-emscripten"
