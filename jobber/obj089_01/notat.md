# Bilen utenfor kontoret

Dato: 13. oktober 2026. Produksjonsagent Astra.

## Kilder og motiv

Objekt89, tilstand01, rom9; objekt_i_rom248,104,232,88. Original1x og4x viser en parkert svart/hvit bil med lang svart panserform, fire gule frontlykter, kromgrill og støtfanger, hvitt tak og dør, gul stjerne, to synlige hjul og bakfinner. Rekvisitten er visuelt avklart som bilen, ikke et skilt. Spesifikt bilmodellnavn er ikke bekreftet fra skript. Bakgrunnen er et utsnitt av gaten. Rompromptens øvrige butikkskilt ble ikke introdusert i dette utsnittet.

Kildegrunnlag: jobbens uendrede original_1x.png, referanse.png, jobb.json og prompt.txt; ANALYSE.md; origin/main:docs/gpt-romnotater.csv; godkjent stil/rom007_del1av2.png for pensel/strek. Alle lokale bildeinput ble åpnet med view_image før generering. Originalens innhold og palett går foran stilankeret.

## Produksjon

Ett forsøk med innebygd ChatGPT-bildegenerator image_gen__imagegen. Eksakt bildemodellversjon eksponeres ikke. Originalprompten er brukt ordrett med dokumentert kildepresisering. Full prompt og råforsøk er bevart som obj089_01-prompt.txt og obj089_01-forsok01.png i rapporter/bestilling003-20261013/.

Generatorrektangelet107,276,1430,778 ble beskåret og skalert med Lanczos til928x352 ved304,336. Første kontroll gav SJEKK med globalt skift1.09 originalpiksler. Hele malte motivet ble flyttet4 HD-piksler til venstre med4 pikslers kantforlengelse av gatebakgrunnen til høyre. Dette rettet faktisk plassering uten originalpikselmaske. Endelig skift0.10, blokk0.63, kantlikhet0.95.

## Kontroll

Endelig 1536 x 1024 PNG, motivrektangel [304, 336, 928, 352], padding målt eksakt RGB128. Uendret verktoy/sjekk_leveranse.py: OK. Resultatet er visuelt åpnet etter etterbehandling. SHA-256: `bbb2ca4a34c259ce82ef9b7e5f4f17b6992bb63bbd9a43b1f15a0eb5bc212be5`.

Sentral identitet, form, farger, tekst og plassering er egenkontrollert. Teknisk OK er ikke Toms visuelle godkjenning. Motorimport, faktisk spillvisning, klikkflater og relevante tilstandsoverganger er ikke kjørt av denne agenten. Mikrokonturer er ikke bevist pikselidentiske.
