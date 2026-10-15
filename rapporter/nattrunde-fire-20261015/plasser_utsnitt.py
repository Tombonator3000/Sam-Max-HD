"""Presis plassering av nytegnede utsnitt. Ingen nytegning i Python."""
from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
R = Path(__file__).resolve().parent


def vimpel(navn, box, farge):
    raw = Image.open(R / f'{navn}-detalj-raa.png').convert('RGB')
    a = np.asarray(raw).astype(float)
    red, green, blue = a[..., 0], a[..., 1], a[..., 2]
    if farge == 'rod':
        m = (red > 60) & (red > green * 1.15) & (red > blue * 1.2)
        m[:, :284] = False  # Behold den godkjente stolpen og kulen.
    elif farge == 'gul':
        m = (red > 70) & (green > 55) & (blue < green * .78) & (red > green * .85)
    else:
        m = (green > 35) & (green > red * 1.1) & (green > blue * 1.2)
    # Skyen og stolpen tas fra det godkjente rommet. Masken følger nytegningen,
    # ikke originalens pikseltrapper. Nedskaleringen gir myk alfa.
    mask = Image.fromarray((m * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(.55))
    patch = raw.convert('RGBA')
    patch.putalpha(mask)
    return patch.crop(box)


def main():
    base1 = Image.open(ROOT / 'jobber/rom017_del1av2/resultat.png').convert('RGBA')
    base2 = Image.open(ROOT / 'jobber/rom017_del2av2/resultat.png').convert('RGBA')
    p180 = vimpel('obj180_04', (192, 224, 1344, 800), 'rod').resize((192, 96), Image.Resampling.LANCZOS)
    p181 = vimpel('obj181_04', (128, 128, 1408, 896), 'gul').resize((160, 96), Image.Resampling.LANCZOS)
    p182 = vimpel('obj182_04', (128, 256, 1408, 768), 'gronn').resize((160, 64), Image.Resampling.LANCZOS)
    # Den lille oppstikkeren på høyre remse hører sammen med remsen i kilden.
    # Flytt den nytegnede delen én HD-piksel ned for å lukke et utilsiktet gap.
    bit = p182.crop((130, 30, 138, 36))
    p182.paste((0, 0, 0, 0), (130, 30, 138, 36))
    p182.alpha_composite(bit, (130, 31))
    base1.alpha_composite(p180, (896, 144))
    # Overlappet mellom delene er 136 originalpiksler. Samme nytegning i begge.
    base1.alpha_composite(p181, (1120, 208))
    base2.alpha_composite(p180.crop((96, 0, 192, 96)), (0, 144))
    base2.alpha_composite(p181, (128, 208))
    base2.alpha_composite(p182, (896, 144))
    p183 = Image.open(R / 'obj183_04-detalj-raa.png').convert('RGBA').crop((256, 128, 1280, 896)).resize((128, 96), Image.Resampling.LANCZOS)
    # Bare kantovergangen i den rektangulære lappen tones mot godkjent rom.
    yy, xx = np.mgrid[:96, :128]
    alpha = np.minimum.reduce([xx, yy, 127 - xx, 95 - yy]).clip(0, 2) / 2
    # Ved øvre kant går propellbladet ut av rommet. Behold det helt frem til kanten.
    alpha[:2, :70] = 1
    p183.putalpha(Image.fromarray((alpha * 255).astype('uint8')))
    base2.alpha_composite(p183, (544, 112))
    for j, im in [('lag017_04_del1av2', base1), ('lag017_04_del2av2', base2)]:
        im.convert('RGB').save(ROOT / f'jobber/{j}/resultat.png')
    for navn, patch in [('obj180_04', p180), ('obj181_04', p181), ('obj182_04', p182), ('obj183_04', p183)]:
        patch.save(R / f'{navn}-nytegnet-4x.png')


if __name__ == '__main__':
    main()
