"""Gjenskap leveransene fra nytegningen. Kjør fra rotmappen i gpt-arbeid.

Bruk prosjektets eksisterende Python-miljø med numpy og Pillow.
Ingen originalpiksler brukes som erstatning for nytegningen.
"""
from pathlib import Path
import json

import numpy as np
from PIL import Image

R = Path('rapporter/natt-returer4-20261015')
J = Path('jobber')

for name, attempt, box in [
    ('lag052_11_del2av2', 3, (576, 752, 672, 816)),
    ('lag056_06', 1, (608, 528, 736, 656)),
    ('lag061_01_del1av2', 1, (1088, 464, 1376, 624)),
    ('lag068_08', 1, (736, 432, 832, 464)),
]:
    old = Image.open(R / f'{name}-forrige.png').convert('RGB')
    raw = Image.open(R / f'{name}-raa{attempt:02d}.png').convert('RGB')
    if name == 'lag052_11_del2av2':
        part = raw.resize((96, 64), Image.Resampling.LANCZOS)
        yy, xx = np.indices((64, 96))
        weight = np.minimum.reduce([xx, yy, 95 - xx, 63 - yy])
        weight = np.clip(weight / 4.0, 0, 1)[:, :, None]
        mixed = np.asarray(part) * weight + np.asarray(old.crop(box)) * (1 - weight)
        old.paste(Image.fromarray(np.rint(mixed).astype('uint8')), box)
    elif name == 'lag068_08':
        # Egen alfauttrekking fra nytegnet motiv, uten originalens konturmaske.
        part = raw.crop((736, 432, 832, 456))
        intensity = np.asarray(part).max(2)
        yy, xx = np.where(intensity < 100)
        bounds = (int(xx.min()), int(yy.min()), int(xx.max()) + 1, int(yy.max()) + 1)
        rgba = part.convert('RGBA')
        alpha = np.clip((160 - intensity.astype(float)) / 80, 0, 1) * 255
        rgba.putalpha(Image.fromarray(alpha.astype('uint8')))
        fitted = rgba.crop(bounds).resize((56, 8), Image.Resampling.LANCZOS)
        fitted.save(R / 'obj641_01-nytegnet-tilpasset.png')
        base = Image.open(J / 'rom068/resultat.png').convert('RGB')
        old.paste(base.crop(box), box)
        old.paste(fitted, (748, 440), fitted)
    else:
        old.paste(raw.crop(box), box)
    data = json.loads((J / name / 'jobb.json').read_text())
    x, y, w, h = data['bilde_i_lerret']
    # Rens bare den dokumenterte grå fyllrammen.
    canvas = Image.new('RGB', (1536, 1024), (128, 128, 128))
    canvas.paste(old.crop((x, y, x + w, y + h)), (x, y))
    canvas.save(J / name / 'resultat.png')
