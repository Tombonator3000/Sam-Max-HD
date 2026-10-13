# Hovedark for Max

Levert 2026-10-13 15:45 (norsk tid) av Codex, som stilpilotkandidat.

Verktøy: ChatGPTs innebygde bildegenerator. Eksakt modellnavn er ikke oppgitt av verktøyet. Antall forsøk: 3. Valgt forsøk: 2. Resultatet er kopiert direkte fra generatoren, uten etterfølgende tegning, maskering eller skalering. Alle rå forsøk er bevart lokalt under rapportmappen og i generatorens originalmappe.

Kilde: `hovedark/max/referanse.png`, `original_1x.png`, `prompt.txt` og `jobb.json`. Kildehash finnes i `rapporter/hovedark-20261013/kildehash.json`. Originalreferansen bestemmer person, drakt, positurer, proporsjoner og normalpalett. Purcell-vedleggene brukes for strekens karakter. `ANALYSE.md` er fulgt for lettere, varierende kontur og skille mellom stil og spillinnhold. Ingen beskyttet jobbfil er endret.

De første promptene bevarer den bestilte teksten og presiserer at referanse.png allerede er 4x. For Max presiseres at han ikke har klær, hatt eller slips. Nærbildets scenebakgrunn fjernes og ståfigurenes normalpalett brukes. Senere kall er avgrensede størrelseskorreksjoner med originalen som fasit for identitet og geometri. Samtlige benyttede prompter ligger i `rapporter/hovedark-20261013/max-forsok-*.prompt.txt`.

## Kontroll

PNG, RGBA, 1536 x 1024. Ekte alfa. 94.7% av lerretet har alfa under 16. Fem separate visninger funnet: forfra, mot høyre, bakfra, mot venstre og ansiktsnærbilde. Visuell gjennomgang bekrefter riktig hovedperson, drakt eller mangel på klær, fem visninger og ingen rekvisitter fra stilillustrasjonene. Figurenes ansiktstolkning og kontur er fortsatt en pilotprøve.

Egenkontroll: **SJEKK**, ingen FEIL i valgt fil. Kommando: appens medfølgende Python med `verktoy/sjekk_leveranse.py hovedark/max.png`. Full utskrift i `rapporter/hovedark-20261013/max-kontroll.txt`.

Faktiske bokser er målt på alfa minst 128, i lerretspiksler [x, y, bredde, høyde]. Egenkontrollen for hovedark måler antall og høyde, ikke alle disse plass- og breddeavvikene.

| Visning | Bestilt boks | Målt boks |
| --- | --- | --- |
| 1 | [264, 408, 136, 208] | [302, 428, 113, 184] |
| 2 | [432, 408, 144, 208] | [494, 427, 106, 187] |
| 3 | [608, 408, 124, 208] | [647, 427, 108, 186] |
| 4 | [764, 408, 144, 208] | [793, 425, 116, 188] |
| 5 | [940, 416, 328, 200] | [989, 424, 283, 189] |

Max er 10 til 12 prosent for lav i ståvisningene. Alle fire står som SJEKK. Nærbildet er innenfor OK-grensen for høyde. Bredde og plassering avviker også fra originalboksene.

Disse avvikene må avklares eller rettes før arket brukes som fast geometrisk referanse i figurproduksjon. SJEKK er ikke teknisk mottaksgodkjenning. Tom har ikke godkjent designet. Ingen import, spillavspilling eller publisert HD-mod er utført. Dette hovedarket er en designprøve, ikke en animasjonsleveranse, og har derfor ikke et kostymerutekart.

SHA-256: `8e562e60240f6caa7c7d46749af17c01ab57cb5267d6bfd14f6cd1f216fdc2ab`.
