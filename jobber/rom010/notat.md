# USA-kartet før reisemål legges på

Dato: 13. oktober 2026. Produksjonsagent Astra.

## Kilder og motiv

Rom10,320x200. Jobbens original og origin/main:docs/gpt-romnotater.csv avklarer et destinasjonskart der spillet tegner nye destinasjoner over bakgrunnen. Dette basebildet har ingen destinasjonsikoner. Sam og Max er dekorative hoder øverst. Teksten GREETINGS from the USA og HI THERE! er bevart, uten nye ord eller ikoner. Landkontur, innsjøer, skrått rutenett og grønn/gul/blå palett er sammenlignet. Geografien er bevisst skjev og ikke rettet.

Kildegrunnlag: jobbens uendrede original_1x.png, referanse.png, jobb.json og prompt.txt; ANALYSE.md; origin/main:docs/gpt-romnotater.csv; godkjent stil/rom007_del1av2.png for pensel/strek. Alle lokale bildeinput ble åpnet med view_image før generering. Originalens innhold og palett går foran stilankeret.

## Produksjon

Ett forsøk med innebygd ChatGPT-bildegenerator image_gen__imagegen. Eksakt bildemodellversjon eksponeres ikke. Originalprompten er brukt ordrett med dokumentert kildepresisering. Full prompt og råforsøk er bevart som rom010-prompt.txt og rom010-forsok01.png i rapporter/bestilling003-20261013/.

Generatoren holdt motivrektangelet128,112,1280,800. Bare padding er normalisert til RGB128. Endelig skift0.10, blokk0.66, kantlikhet0.94.

## Kontroll

Endelig 1536 x 1024 PNG, motivrektangel [128, 112, 1280, 800], padding målt eksakt RGB128. Uendret verktoy/sjekk_leveranse.py: OK. Resultatet er visuelt åpnet etter etterbehandling. SHA-256: `4b2353dced80f95e2fd73233e66897fe010a62dd7d158479c02c7d40660861cb`.

Sentral identitet, form, farger, tekst og plassering er egenkontrollert. Teknisk OK er ikke Toms visuelle godkjenning. Motorimport, faktisk spillvisning, klikkflater og relevante tilstandsoverganger er ikke kjørt av denne agenten. Mikrokonturer er ikke bevist pikselidentiske.

## Videre retting 15. oktober 2026

Sams nedre tannrekke fullført etter Toms rettelse. Bare munnutsnittet er endret. Innebygd bildeverktøy; eksakt modellnavn ikke eksponert. Python brukt til rensing og plassering etter Toms tillatelse. Egenkontroll OK.

SHA-256: ea1060f834dfcc46139094e5ccb7f7e18673a556723fc8d64c8aa54c0ed5bdfa. Se [rapport, prompter, råbilder og kontroll](../../rapporter/videre-grafikk-20261015/RAPPORT.md). Ingen spilltest, ny runtimeimport eller Toms individuelle godkjenning.
