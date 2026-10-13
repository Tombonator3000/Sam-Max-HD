# Hull i laboratorieveggen (objekt 50, tilstand 01, rom 2)

Dato: 13. oktober 2026. Produksjonsagent Astra.

## Kilder og motiv

Metadata plasserer objektet i rom 2 ved 104,64 med mål184x120. Referansen viser samme apparat, forgrunnsskalle, pære og ledninger som rom002, men med tagget åpning og nedrast blå murstein. Oransjefeltet tolkes visuelt som bakgrunnen gjennom hullet, ikke ild eller en skapning. Denne semantikken ble presisert i prompten. Ingen hendelsesavspilling er utført.

Kildegrunnlaget er jobbens uendrede referanse.png, original_1x.png, jobb.json og prompt.txt, ANALYSE.md og den godkjente stil/rom007_del1av2.png. Alle benyttede bilder ble åpnet visuelt før generering. Hovedfarger og innhold tas fra originalen; stilankeret brukes bare til pensel og strek.

## Verktøy og etterbehandling

Ett generatorforsøk med innebygd ChatGPT-bildegenerator, image_gen__imagegen. Eksakt bildemodellversjon eksponeres ikke. Ordrett originalprompt er beholdt i den komplette brukte prompten med separat kildepresisering i rapporter/bestilling002-20261013/obj050_01-prompt.txt. Råresultatet er bevart som obj050_01-forsok01.png.

Generatoren forstørret motivrektangelet til omtrent930x608. Det ble beskåret til x303,y194,x1233,y802 og skalert med Lanczos til736x480, deretter plassert ved400,272 på1536x1024. Ingen originalpikselmaske. Murkant og haug er nytegnet; enkeltsteiners mikrokontur er ikke verifisert som identisk.

## Kontroll og leveranse

1536 x 1024 RGB PNG, bilde_i_lerret [400, 272, 736, 480], padding målt eksakt RGB128. Uendret verktoy/sjekk_leveranse.py: OK, se obj050_01-kontroll.txt i rapportmappen. Resultatet er også åpnet visuelt etter etterbehandling. Identitet, komposisjon og sentrale rekvisitter er sammenlignet med originalen.

SHA-256: `dc83d735fe93ba7bafd70df681783e764839af41246af9e824233030f6c45a48`.

Dette er en HD-grafikkleveranse med teknisk egenkontroll og visuell egenvurdering. Motorimport, spillvisning, animasjon/tilstandsskifte og Toms visuelle godkjenning av denne jobben gjenstår. Automatisk OK beviser ikke pikselidentiske mikrokonturer eller godkjenning i spillet.
