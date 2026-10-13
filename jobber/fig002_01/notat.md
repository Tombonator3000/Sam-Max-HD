# Sam, figurark 1

Levert 13. oktober 2026 som stilpilotkandidat etter Toms godkjenning av hovedarkene. Arket er ikke importert i motoren eller visuelt godkjent av Tom.

## Kilde og identitet

Originalen er `referanse.png` og `original_1x.png` i denne jobben, med ruter og synlige bokser fra uendret `jobb.json`. Kostyme 2 er Sam. `hovedark/sam.png`, som Tom godkjente i samtalen, er stilreferanse. Farger og kroppsdeler følger originalarket: blågrå dress og hatt, hvit skjorte, svart og blått stripet slips og brun pels. Føttene er poter.

Arket har ni ruter: tre hodeløse kropper, én håndrute med to atskilte deler, tre hoder og to øyelokkruter. Lag 4 er blink. Dette er kontrollert ved at originalens små brune flekker ligger over svarte øyepiksler når `rel_x` og `rel_y` fra `konsept/2026-10-12/kostymer-originalmetadata.json` brukes. De små rutene er ikke munner.

## Fremstilling og presis retting

Ett forsøk med innebygd ChatGPT-bildegenerator, med originalreferansen som bilde 1 og godkjent Sam-hovedark som bilde 2. Verktøyet bekreftet ikke et bestemt modellnavn eller versjonsnummer. Råbildet og prompten er bevart i `rapporter/stilpilot-fortsettelse-20261013/fig002_01-forsok-01.png` og tilhørende promptfil.

Generatoren tegnet delene større og flyttet, og laget bare ett øyelokkpar. Vanlig bildebehandling er brukt innen Toms valg om presis skalering og plassering. Hver sammensatte rute er skalert med forhåndsmultiplisert Lanczos og plassert slik at boksen med alfa minst 128 er nøyaktig originalens synlige boks ganger fire. Figurene er ikke klippet med originalens pikselmaske. Genererte konturer og myke kanter beholdes. Lav alfa fra en diffus bakgrunnsglød er fjernet rundt de genererte figurkjernene. Håndrutens tomrom mellom de to delene er bevart.

De to øyelokkrutene er rekonstruert fra de to nye flekkformene i generatorens ene par. Hver flekk er tilpasset 8 × 8 HD-piksler og lagt på originalens to fester innen rutens 24 × 8 piksler, med lokal hudgradient fra riktig HD-hode. Ingen oppskalert originalrute er brukt. De genererte øynene var for høye og litt forskjøvet til at kildeplasserte øyelokk dekket dem. De nye øyeformene er derfor presist skalert og flyttet til originalens fester, med hud fra samme hode interpolert bak. Øyelokkenes egne alfaformer er supplert med de justerte genererte øyeformene for å dekke hele øyet. Første sammenstilling ga synlige hudlapper fordi én konstant hudfarge og et mørkt skyggetrinn lå over hudens egen fargevariasjon. Dette er rettet ved å hente hudfargen lokalt for hver piksel. En svak lukket fold nederst er bare tre RGB-trinn mørkere. Dette er dokumentert i `sam-presis-kontroll.json` og den kjørbare oppskriften `sam-bildebehandling.py.txt` i rapportmappen.

## Kontroll

Uendret `verktoy/sjekk_leveranse.py` gir OK, 7 av 7 målte ruter. Skriptet hopper over de to øyelokkrutene fordi de er svært små. En separat kontroll måler derfor alle ni rutene og bekrefter eksakt bredde, høyde og plassering. Håndruten og hver øyelokkrute har fremdeles to atskilte alfakjerner. Hele arket er 1536 × 1024 med ekte alfa.

Kropp, hode og hender er sett sammen i tre retninger med originalens relative koordinater. Åpne øyne og blink er kontrollert separat, og ingen svarte piksler står igjen i de fire øyekerner når riktig øyelokk legges på. Kontaktarkene `sam-kropp-hode-kontaktark.png`, `sam-blink-overlay.png` og `sam-blink-naerbilde.png` viser kontrollen. Dette er diagnostiske stillbilder. Rutelistene er dedupliserte, så de beviser ikke originaltiming, blinkaktivering eller motoravspilling.

Rutekartet er `rapporter/stilpilot-fortsettelse-20261013/rutekart-sam.json`. SHA-256 og målinger finnes i `sam-egenkontroll.json`. Import, motorvisning og Toms vurdering av det nye figurarket gjenstår.
