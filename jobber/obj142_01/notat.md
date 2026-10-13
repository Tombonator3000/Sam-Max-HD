# Passasjen ved karnevalet, objekt 142 tilstand 01

Dato: 13. oktober 2026. Produksjonsagent Astra.

## Kildeanalyse

Jobbmetadata plasserer utsnittet ved 520,24 i rom 15 med mål 112x144. Originalen viser blå telt, rød/gul del av en attraksjon i bakgrunnen, himmel, gråfiolett teltkant, mark med skyggestriper, plugg/tau og busk. Ingen lesbare skilt eller personer er synlige. Generisk romprompt nevner skilt som ligger utenfor utsnittet; disse ble uttrykkelig ikke lagt til. Tilstand 01 er metadatafakta, men nøyaktig skriptutløser er ikke undersøkt.

Uendrede original_1x.png, referanse.png, jobb.json og prompt.txt ble lest og alle kildebilder åpnet visuelt. ANALYSE.md, GRUNNLAG.md og origin/main:docs/gpt-romnotater.csv styrer innholdet. Godkjent stil/rom007_del1av2.png er brukt bare for strek og penselføring.

## Produksjon

Innebygd ChatGPT-bildegenerator image_gen__imagegen. Eksakt bildemodellversjon er ikke eksponert. Originalprompt brukt ordrett med separate kildepresiseringer. Begge romprompter er bevart ordrett i fullsceneprompten; felles fullscene overstyrer bare instruksen om separat generering.

Ett bildeverktøyforsøk. Generert innholdsrektangel 476,122,1060,898 beskåret og skalert med Lanczos til 448x576 ved 544,224. Grå padding satt til RGB128.

Råforsøk, full brukt prompt og reproduksjonsoppskrift ligger i rapporter/bestilling004-20261013/.

## Egenkontroll

1536x1024 PNG med bilde_i_lerret [544, 224, 448, 576] og eksakt RGB128-padding. Uendret verktoy/sjekk_leveranse.py: OK, se obj142_01-kontroll.txt. Endelig fil er åpnet visuelt. SHA-256: `fabdf164985b8f80d1e9b4cb238c649ccc798a67c4e71a591706c9491627c697`.

Dette er teknisk og visuell egenkontroll. Motorimport, spilltest, tilstandsskifte og Toms visuelle sluttgodkjenning er ikke utført. Detaljenes mikrokonturer er ikke bevist pikselidentiske; ukjente montrers art er ikke fastslått utover originalens synlige utforming.
