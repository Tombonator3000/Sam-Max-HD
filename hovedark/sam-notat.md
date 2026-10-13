# Hovedark for Sam

Levert 2026-10-13 15:45 (norsk tid) av Codex, som stilpilotkandidat.

Verktøy: ChatGPTs innebygde bildegenerator. Eksakt modellnavn er ikke oppgitt av verktøyet. Antall forsøk: 5. Valgt forsøk: 4. Resultatet er kopiert direkte fra generatoren, uten etterfølgende tegning, maskering eller skalering. Alle rå forsøk er bevart lokalt under rapportmappen og i generatorens originalmappe.

Kilde: `hovedark/sam/referanse.png`, `original_1x.png`, `prompt.txt` og `jobb.json`. Kildehash finnes i `rapporter/hovedark-20261013/kildehash.json`. Originalreferansen bestemmer person, drakt, positurer, proporsjoner og normalpalett. Purcell-vedleggene brukes for strekens karakter. `ANALYSE.md` er fulgt for lettere, varierende kontur og skille mellom stil og spillinnhold. Ingen beskyttet jobbfil er endret.

De første promptene bevarer den bestilte teksten og presiserer at referanse.png allerede er 4x. For Max presiseres at han ikke har klær, hatt eller slips. Nærbildets scenebakgrunn fjernes og ståfigurenes normalpalett brukes. Senere kall er avgrensede størrelseskorreksjoner med originalen som fasit for identitet og geometri. Samtlige benyttede prompter ligger i `rapporter/hovedark-20261013/sam-forsok-*.prompt.txt`.

## Kontroll

PNG, RGBA, 1536 x 1024. Ekte alfa. 89.3% av lerretet har alfa under 16. Fem separate visninger funnet: forfra, mot høyre, bakfra, mot venstre og ansiktsnærbilde. Visuell gjennomgang bekrefter riktig hovedperson, drakt eller mangel på klær, fem visninger og ingen rekvisitter fra stilillustrasjonene. Figurenes ansiktstolkning og kontur er fortsatt en pilotprøve.

Egenkontroll: **SJEKK**, ingen FEIL i valgt fil. Kommando: appens medfølgende Python med `verktoy/sjekk_leveranse.py hovedark/sam.png`. Full utskrift i `rapporter/hovedark-20261013/sam-kontroll.txt`.

Faktiske bokser er målt på alfa minst 128, i lerretspiksler [x, y, bredde, høyde]. Egenkontrollen for hovedark måler antall og høyde, ikke alle disse plass- og breddeavvikene.

| Visning | Bestilt boks | Målt boks |
| --- | --- | --- |
| 1 | [224, 372, 192, 280] | [216, 367, 191, 299] |
| 2 | [448, 372, 160, 280] | [462, 371, 156, 297] |
| 3 | [640, 372, 180, 280] | [665, 372, 182, 294] |
| 4 | [852, 372, 160, 280] | [892, 373, 157, 295] |
| 5 | [1044, 444, 268, 208] | [1086, 447, 275, 212] |

Sam er 5 til 7 prosent for høy i ståvisningene. De to første står som SJEKK i egenkontrollen. Nærbildet er innenfor OK-grensen. Flere visninger er forskjøvet mot høyre og fotlinjen ligger for lavt.

Disse avvikene må avklares eller rettes før arket brukes som fast geometrisk referanse i figurproduksjon. SJEKK er ikke teknisk mottaksgodkjenning. Tom har ikke godkjent designet. Ingen import, spillavspilling eller publisert HD-mod er utført. Dette hovedarket er en designprøve, ikke en animasjonsleveranse, og har derfor ikke et kostymerutekart.

SHA-256: `a00c29a5ad3e1bab9be9dcb22ee866cd37b8cf04f379a9ca0f19a644919d1980`.
