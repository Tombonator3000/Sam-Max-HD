"""Oppskaleringsmetoder.

Alle metoder tar et RGB-bilde og gir et RGB-bilde som er nøyaktig `scale` ganger større.
Motoren krever eksakt størrelse, så resultatet tilpasses hvis et eksternt verktøy gir noe annet.

Metoder:
  nearest       Hver piksel blir en blokk. Nyttig som referanse og for testing.
  lanczos       Myk oppskalering, rask, ingen ekstra programmer.
  lanczos-sharp Lanczos med litt skarphet etterpå.
  scale4x       Scale2x (EPX) to ganger: laget for pikselgrafikk, trappetrinn blir rette skrå kanter
                uten uskarphet. Bare for skala 4 (ellers lanczos).
  realesrgan    Real-ESRGAN via realesrgan-ncnn-vulkan (må være installert, bruker skjermkortet).
  cmd           Valgfri kommando, for eksempel et annet KI-verktøy. Malen får {inn}, {ut} og {skala}.
"""
from __future__ import annotations

import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageFilter

METHODS = ["nearest", "lanczos", "lanczos-sharp", "scale4x", "realesrgan", "cmd"]


def _fit(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    return im if im.size == size else im.resize(size, Image.LANCZOS)


def scale2x(a):
    """Scale2x (EPX) på et bilde som numpy-tabell (h, w) eller (h, w, kanaler): hver ut-piksel
    kopierer én inn-piksel, så fargene forblir de samme."""
    import numpy as np
    p = np.pad(a, ((1, 1), (1, 1)) + ((0, 0),) * (a.ndim - 2), mode="edge")
    P = p[1:-1, 1:-1]
    A, B = p[:-2, 1:-1], p[1:-1, 2:]   # over, høyre
    C, D = p[1:-1, :-2], p[2:, 1:-1]   # venstre, under

    def eq(x, y):
        return np.all(x == y, axis=-1) if a.ndim == 3 else x == y

    def pick(cond, x):
        return np.where(cond[..., None] if a.ndim == 3 else cond, x, P)
    o00 = pick(eq(C, A) & ~eq(C, D) & ~eq(A, B), A)
    o01 = pick(eq(A, B) & ~eq(A, C) & ~eq(B, D), B)
    o10 = pick(eq(D, C) & ~eq(D, B) & ~eq(C, A), C)
    o11 = pick(eq(B, D) & ~eq(B, A) & ~eq(D, C), D)
    h, w = a.shape[:2]
    out = np.empty((h * 2, w * 2) + a.shape[2:], a.dtype)
    out[0::2, 0::2], out[0::2, 1::2], out[1::2, 0::2], out[1::2, 1::2] = o00, o01, o10, o11
    return out


def scale4x_rgba(im: Image.Image) -> Image.Image:
    """Scale4x på et RGBA-bilde: farge og alfa skaleres sammen, så kantene følger tegningen."""
    import numpy as np
    a = np.asarray(im.convert("RGBA"))
    return Image.fromarray(scale2x(scale2x(a)), "RGBA")


def _external(im: Image.Image, scale: int, argv_template: list[str]) -> Image.Image:
    with tempfile.TemporaryDirectory() as tmp:
        src, dst = Path(tmp) / "inn.png", Path(tmp) / "ut.png"
        im.save(src)
        argv = [a.format(inn=src, ut=dst, skala=scale) for a in argv_template]
        subprocess.run(argv, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        out = Image.open(dst).convert("RGB")
        out.load()
    return out


def upscale(im: Image.Image, scale: int, method: str, *, tool: str | None = None,
            model: str = "realesrgan-x4plus", cmd: str | None = None) -> Image.Image:
    im = im.convert("RGB")
    size = (im.width * scale, im.height * scale)
    if method == "nearest":
        return im.resize(size, Image.NEAREST)
    if method == "lanczos":
        return im.resize(size, Image.LANCZOS)
    if method == "scale4x" and scale == 4:
        return scale4x_rgba(im).convert("RGB")
    if method == "scale4x":
        return im.resize(size, Image.LANCZOS)
    if method == "lanczos-sharp":
        return im.resize(size, Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=80, threshold=2))
    if method == "realesrgan":
        exe = tool or shutil.which("realesrgan-ncnn-vulkan")
        if not exe:
            raise SystemExit("Fant ikke realesrgan-ncnn-vulkan. Last ned fra "
                             "https://github.com/xinntao/Real-ESRGAN/releases og legg den i PATH, "
                             "eller bruk --tool STI.")
        out = _external(im, scale, [exe, "-i", "{inn}", "-o", "{ut}", "-s", "4", "-n", model])
        return _fit(out, size)
    if method == "cmd":
        if not cmd:
            raise SystemExit("Metoden cmd krever --cmd, for eksempel: --cmd 'mittverktoy {inn} {ut} {skala}'")
        return _fit(_external(im, scale, shlex.split(cmd)), size)
    raise SystemExit(f"Ukjent metode: {method}. Velg en av: {', '.join(METHODS)}")


def upscale_alpha(alpha: Image.Image, scale: int) -> Image.Image:
    """Alfakanalen skaleres med nærmeste nabo, så kantene blir like skarpe som i originalen."""
    return alpha.resize((alpha.width * scale, alpha.height * scale), Image.NEAREST)
