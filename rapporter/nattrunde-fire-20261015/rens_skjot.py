"""Fjern små RGB-sprang på felles flater ved skjøten etter bildeverktøyets retting."""
from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
R = Path(__file__).resolve().parent
raw = Image.open(R / 'obj307_01-raa-2.png').convert('RGB')
part = np.asarray(raw.crop((128, 256, 1408, 416))).astype(float).copy()
below = np.asarray(Image.open(ROOT / 'jobber/obj304_01/resultat.png').convert('RGB').crop((128, 336, 1408, 688))).astype(float)
source_top = np.asarray(Image.open(ROOT / 'jobber/obj307_01/referanse.png').convert('RGB').crop((128, 432, 1408, 592))).astype(float)
source_bottom = np.asarray(Image.open(ROOT / 'jobber/obj304_01/referanse.png').convert('RGB').crop((128, 336, 1408, 688))).astype(float)
# Kun flater som faktisk fortsetter i originalen. Ikke flytt åpningen eller legg
# inn hender fra neste objekt. Bildeverktøyet har allerede tegnet geometrien.
same_surface = np.max(np.abs(source_top[-1] - source_bottom[0]), axis=1) < 10
mask = Image.fromarray((same_surface[None, :] * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1))
weight = np.asarray(mask).astype(float)[0, :, None] / 255
correction = (below[0] - part[-1]) * weight
for i in range(8):
    part[-8 + i] += correction * ((i + 1) / 8) ** 2
part = np.clip(np.rint(part), 0, 255).astype('uint8')
canvas = Image.new('RGB', (1536, 1024), (128, 128, 128))
canvas.paste(Image.fromarray(part), (128, 432))
canvas.save(ROOT / 'jobber/obj307_01/resultat.png')
joined = Image.new('RGB', (1536, 1024), (128, 128, 128))
joined.paste(Image.fromarray(part), (128, 256))
joined.paste(Image.fromarray(below.astype('uint8')), (128, 416))
joined.save(R / 'obj307-skjot-ferdig.png')
