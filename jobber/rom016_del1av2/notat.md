# Hall of Oddities, del 1 av 2

Dato: 13. oktober 2026. Produksjonsagent Astra.

## Kildeanalyse

Rom 16 er utstillingsteltet. Originalene viser Insect Lad med briller, hvit skjorte og grønne bukser; Human Enigma i brun dress med vannkran til hode; blek rund figur i grønn glassylinder; de små glassutstillingene; rektangulær glassmonter i forgrunnen; lyskastere, scenedraperier, teltåpninger og gulvskygger. Monterens lille brune vesen er tegnet fra synlig form; art/navn er ikke bekreftet. Ingen nye spillfigurer er lagt på gulvet.

Uendrede original_1x.png, referanse.png, jobb.json og prompt.txt ble lest og alle kildebilder åpnet visuelt. ANALYSE.md, GRUNNLAG.md og origin/main:docs/gpt-romnotater.csv styrer innholdet. Godkjent stil/rom007_del1av2.png er brukt bare for strek og penselføring.

## Produksjon

Innebygd ChatGPT-bildegenerator image_gen__imagegen. Eksakt bildemodellversjon er ikke eksponert. Originalprompt brukt ordrett med separate kildepresiseringer. Begge romprompter er bevart ordrett i fullsceneprompten; felles fullscene overstyrer bare instruksen om separat generering.

Ett felles fullsceneforsøk for begge romdelene. Originaldelene hadde byte-identisk overlapp og ble satt sammen til 1920x800 med grå marg i 1920x1280. Generatoren leverte 1536x1024 med scene 0,192,1536,832. Scenen ble skalert til 1920x800, og denne delen er utsnitt x0..1536 ved y112 på leveranselerretet.

Råforsøk, full brukt prompt og reproduksjonsoppskrift ligger i rapporter/bestilling004-20261013/.

## Egenkontroll

1536x1024 PNG med bilde_i_lerret [0, 112, 1536, 800] og eksakt RGB128-padding. Uendret verktoy/sjekk_leveranse.py: OK, se rom016_del1av2-kontroll.txt. Endelig fil er åpnet visuelt. SHA-256: `a41d2cf4aa2fb1dce1640f371e29c20ca1bbaf106f00c6c1cb5ce56b8e5dac09`.

Dette er teknisk og visuell egenkontroll. Motorimport, spilltest, tilstandsskifte og Toms visuelle sluttgodkjenning er ikke utført. Detaljenes mikrokonturer er ikke bevist pikselidentiske; ukjente montrers art er ikke fastslått utover originalens synlige utforming.
