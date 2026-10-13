# Trixies vogn innvendig

Dato: 13. oktober 2026. Produksjonsagent Astra.

## Kildegrunnlag

Rom 20 har ingen levende figurer i bakgrunnen. Rosa seng, pute og garderobeskap, lilla gardiner, oransje benker, bord med lilla vase og hvite/gule blomster, hyllerekvisitter, veggplakater og blå boks med gul stjerne er kildemotivet. RICE er synlig på hylleboksen. Plakatene er beholdt som veggbilder. De små motivene er visuelt tolket fra originalen; navn/arter er ikke kildebekreftet.

Jobbens uendrede original_1x.png, referanse.png, jobb.json og prompt.txt er kontrollert. Alle bildeinput er åpnet visuelt. ANALYSE.md, GRUNNLAG.md og origin/main:docs/gpt-romnotater.csv gir kontekst. Godkjent stil/rom007_del1av2.png brukes kun for strek/pensel.

## Produksjon og retting

Innebygd ChatGPT-bildegenerator image_gen__imagegen. Eksakt bildemodellversjon er ikke eksponert. Originalprompten ble brukt ordrett med separat kildepresisering. Antall forsøk: 2. Alle råforsøk, komplette prompter og oppskrifter er bevart i rapporter/bestilling005-20261013/.

To generatorforsøk. Første forsøk avvist for komposisjonsavvik: FEIL, skift 1.00, blokk 15.04, kantlikhet 0.33. Forsøk 2 brukte originalen igjen, med konkrete geometriankere. Andre råforsøk ble beskåret ved 128,112,1408,912 og satt tilbake på korrekt lerret med RGB128-padding. Endelig OK: skift 0.08, blokk 0.18, kantlikhet 0.97.

## Leveransekontroll

1536x1024 PNG. Bilde_i_lerret [128, 112, 1280, 800]. Padding målt eksakt RGB128. Uendret verktoy/sjekk_leveranse.py gir OK. Sluttresultatet er visuelt åpnet etter retting. SHA-256: `9059c5f05db03cd763c12e1aa387d2c3bf7c793284859e675f28d89ffc93e7d0`.

Teknisk og visuell egenkontroll er utført; motorimport, spilltest, tilstandsskifte og Toms individuelle visuelle godkjenning er ikke utført. Mikrokonturer og lesningen av små plakatfigurer er ikke bevist semantisk perfekte.
