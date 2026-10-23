#!/usr/bin/env bash
# Statisk libwebp for den låste Emscripten-versjonen. Ingen systembiblioteker
# eller ny Emscripten-port kreves. Kildearkivet er låst med SHA-256.
set -euo pipefail
DEST="${1:?Bruk: engine/build-webp.sh installasjonsmappe}"
WEBP_VERSION=1.6.0
WEBP_SHA=e4ab7009bf0629fd11982d4c2aa83964cf244cffba7347ecd39019a9e38c4564
STAMP="$WEBP_VERSION $(emcc --version | head -1)"
if [ -f "$DEST/lib/libwebp.a" ] && [ "$(cat "$DEST/.bygget" 2>/dev/null || true)" = "$STAMP" ]; then
  exit 0
fi
mkdir -p "$DEST"
BUILD="$(mktemp -d)"
trap 'rm -rf "$BUILD"' EXIT
curl --retry 3 -fsSL "https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-$WEBP_VERSION.tar.gz" -o "$BUILD/source.tar.gz"
echo "$WEBP_SHA  $BUILD/source.tar.gz" | sha256sum -c -
tar -xzf "$BUILD/source.tar.gz" -C "$BUILD"
cd "$BUILD/libwebp-$WEBP_VERSION"
emconfigure ./configure --prefix="$DEST" --disable-shared --enable-static \
  --disable-threading --disable-sdl --disable-gl --disable-libwebpmux \
  --disable-libwebpdemux --disable-png --disable-jpeg --disable-tiff --disable-gif
emmake make -j"${JOBS:-2}"
emmake make install
cp COPYING "$DEST/COPYING.libwebp"
printf '%s\n' "$STAMP" > "$DEST/.bygget"
