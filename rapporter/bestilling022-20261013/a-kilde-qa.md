# Bestilling 22 A

Tre lag er produsert med ett innebygd imagegen-forsøk hver. [Manifest](a-leveranser.json), [samlet kontaktark](a-samlet-kontaktark.png) og [objektnærbilder](a-objekt-naerbilder.png) dokumenterer de valgte resultatene. Eksakt modellnavn er ikke eksponert. Alle 40 bestilte og fire ekstra beskyttede kilder er uendret, se [kildehashkontroll](a-kildehashkontroll.json).

## Motiv og tilstand

Lag003_01 har forskerhodet med oransje hårkrøll, gul/oransje hud, to asymmetriske lyse brilleglass, svarte pupiller, lang nese, ører og tung hake. Hodet sitter i kildens vinkel mot den eksisterende frakkekragen. Bakgrunn, apparater og frakk følger levert rom003-HD. Ingen ny kropp eller mekanisk rekvisitt er lagt til.

Lag004_01 viser faktisk FIRE lange ørefliker som to overlappende par i originalkomposisjonen. Dette ble oppdaget ved ny inspeksjon og korrigert i a-kildeplan.md før mottak. Nytegningen beholder alle fire fliker, med kildens ulike høyder, vinkler og rosa/brune innfelt. Sam får sitt konkrete brune hode med små øyestreker, snuteparti og svart nese. Figurenes kropp, hatt, drakt, slips og bakgrunn viderefører rom004-HD.

Lag004_02 har ingen lange Max-ører; vegg og bjelker er synlige over hodet. Sam er fortsatt uten hodeinnhold under hatten: kildens mørkeblå felt og brune sidebiter beholdes. Ingen anatomisk fullføring er gjort. Dette er en annen komposittilstand enn lag004_01, ikke en påstått animasjonsrekkefølge.

Den leverte romgrafikken er brukt som bilde to og stil-/bakgrunnsreferanse. Dette er ikke ny individuell godkjenning av romankeret. Hver lagoriginal styrer de konkrete endringene og posene. Ingen avvist kandidat brukes som anker.

## Kontroller

| Lag | Globalt skift | Blokkskift | Kantlikhet | Utfall |
|---|---:|---:|---:|---|
| lag003_01 | 0.04 | 0.18 | 0.97 | OK |
| lag004_01 | 0.05 | 0.22 | 0.96 | OK |
| lag004_02 | 0.10 | 0.35 | 0.95 | OK |

Uendret sjekk_leveranse.py ble kjørt på alle resultatene. Checkerens egne kantfunksjoner ble i tillegg brukt til en eksplisitt rapport over metadatafeltene: obj058_01 0.954202, obj059_01 0.970543, obj061_01 0.928645 og obj060_01 0.961714. Alle fire har tilstrekkelig størrelse og kantvariasjon; ingen ble hoppet over. [Objektkontroll](a-objektkontroll.json) inneholder eksakte rektangler og standardavvik. OK-feltene skrives normalt ikke enkeltvis i checkerloggen.

Samlet bilde og alle fire objektutsnitt er visuelt sammenlignet med kilden. Særlig sjekket: asymmetrisk forskeransikt, fire ørefliker, brun Sam-snute, fravær av ører og fortsatt tomt Sam-felt i lag004_02. Objektboksene er komposittfelt inklusive bakgrunn, ikke alfasilhuetter. Nærbildene er kontrollbilder, ikke produksjonsmasker.

## Etterbehandling og begrensninger

Alle råforsøk kom som 1536 x 1024. Motivrektangelet [128,112,1280,800] er klippet og lagt uten skalering på nøytral RGB 128-padding. Resten av motivet kommer fra nygenereringen. Ingen originalpiksler, originalkonturmasker, alfa-/nøkkelfargemasker, lokal flytting eller warp er brukt. [Plassering](a-plassering.py.txt) og [sluttkontroll](a-sluttkontroll.py.txt) er etterprøvbare rapportoppskrifter; produktkode er ikke endret.

Sporing av råbilder, ordrette prompter med separat kildeføring, leverte romanker og SHA-256 ligger i manifestet. Teknisk OK og denne motivkontrollen er ikke importbevis, runtime eller ny individuell brukergodkjenning. Den senere motorens originale maskekomposisjon er ikke testet. Root gjør samlet mottak og levering.
