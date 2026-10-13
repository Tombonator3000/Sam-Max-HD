# Sam004: kildeanalyse og plan for gjenbruk

Analyse av fig004_01 til fig004_06, uten produksjon eller kopiering. De 24 beskyttede kildefilene er låst i [a-kildehash.json](a-kildehash.json) og kontrollert uendret. C har meldt Sam002 frosset, men rotens mottak avventes før eventuell kopiering. Runtime er ikke testet.

## Resultat

Alle 71 Sam004-ruter har nøyaktig samme dimensjoner og RGB-piksler som tilsvarende cel i Sam002. Animasjon, retning, lag og sekvensnummer er også identiske for alle 71. Dette gir grunnlag for gjenbruk av de nye Sam002-tegningene, uten ny generering av like ruter. Det gir ikke grunnlag for å erstatte Sam004-metadata med Sam002-metadata.

| Målark | Ruter | Kildeark i Sam002 | Faktisk innhold og pakking |
| --- | ---: | --- | --- |
| fig004_01 | 9 | fig002_01 | Kroppsdeler, separate hender, hoder og svært små øyelokksfelt. Samme atlasplassering. |
| fig004_02 | 22 | fig002_02 | Åtte gåposer mot høyre og 14 snakkehoder mot høyre. Samme atlasplassering. |
| fig004_03 | 15 | fig002_03 | 13 snakkehoder forfra og to bakfra. Samme atlasplassering. |
| fig004_04 | 8 | fig002_04 | Åtte gåposer forfra. Samme atlasplassering. |
| fig004_05 | 11 | fig002_05 og fig002_06 | Åtte gåposer bakfra, deretter tre a10-poser. De tre siste må pakkes etter målarket. |
| fig004_06 | 6 | fig002_06 og fig002_07 | Tre a11-poser og tre a12-poser. Alle pakkes etter målarket. |

Sam har brun pels, blågrå hatt og dress samt mørkt stripet slips der delene er synlige. Avskårne hoder, hender, kroppsfragmenter og øyelokk er egne ressurser. Manglende kroppsdeler skal ikke fullføres. Sekvensnavnene angir originalressursenes gruppering, ikke verifisert avspillingsrekkefølge i motoren.

## To viktige forskjeller

Cel 169 og 170 har rel_x = -19 i kostyme 4, mot -18 i kostyme 2. Behold målmetadata. Den identiske rastertegningen skal ikke flyttes lokalt for å skjule forskjellen. Bildelikhet opphever ikke runtime-festene. Andre celmetadata er like.

Kostymepalettens indeks 14 viser 14 i kostyme 4 og 255 i kostyme 2. De øvrige palettverdiene er like. Dette gir ingen synlig RGB-forskjell i de 71 sammenlignede rutene, men palettmetadataene er ikke byte-identiske. Årsaken er ikke verifisert gjennom ny dekoding eller runtime.

Sam004 mangler Sam002-celene 171, 172, 173, 174, 175, 257, 258, 259, 260 og 261. De fem uavklarte a07-rutene hos C inngår derfor ikke i disse seks målarkene. Sam004 har gruppene a1, a2, a3, a4, a5, a10, a11 og a12. Det skal ikke tilføyes a6, a7 eller a8.

## Pikselbevis og begrensning

[a-sam004-kildebevis.json](a-sam004-kildebevis.json) dokumenterer hver RGB-rute, palett og metadata. Alle originalarkene er RGB. En diagnostisk RGBA-sammenligning der magenta blir alfa 0 er også identisk, men dette er ikke bevis for opprinnelig alfa og er ingen produksjonsmaske.

Tre arkiverte native originalcels, 141, 156 og 164, finnes som RGBA for begge kostymer. De har identiske filbytes, RGB-piksler og alfakanal. Det fullstendige originale uttrekket er ikke tilgjengelig via den eksisterende brutte extract-lenken. Nativ RGBA-identitet er derfor bare direkte verifisert for disse tre, ikke alle 71. [a-konteksthash.json](a-konteksthash.json) låser tilgjengelige sammenligningskilder og den avleste C-statusen.

## Konkret gjenbruksplan etter mottak

[a-gjenbrukskart.json](a-gjenbrukskart.json) inneholder alle 71 koblinger, kilde- og målrektangler som HD xywh, samt egne originalmetadata. Ark 01 til 04 kan bruke den tilsvarende nye komposisjonen når provenance og format er bekreftet. Ark 05 og 06 krever ompakking av hele nye cels, uten konturmaskering eller geometrisk endring. De seks godkjenningsventende rutene i C sin partielle fig002_06-kandidat dekker a10 og a11; ingen uavklart a07-rute behøves.

Rettet formatkrav: Figurleveransen er ekte RGBA, 1536 × 1024, med motivfelt [64,32,1408,960] og skala 4. Både magenta atlasbakgrunn og grå kildepadding skal være helt transparente i leveransen. Den tidligere formuleringen om magenta/grå leveransebakgrunn var feil. Det ordrette promptets Output-avsnitt og check_figure i verktoy/sjekk_leveranse.py krever ekte alfa; figurformatet skal ikke forveksles med RGB-ikonark. Ved produksjon kontrolleres målformat, hver cel og de to særegne rel-festene separat. Ingen nytegning, jobbfiler eller globale statusfiler er endret i denne analysen.

## Visuelle bevis

[Originalkontaktark med alle seks ark](a-original-kontaktark.png). Sekvensarkene a-sekvens-aNN-rN-lN.png viser alle 71 ruter gruppert etter animasjon, retning og lag, med celnummer og rel-verdier. Særlig [a10 bakfra, cel 169](a-sekvens-a10-r3-l1.png) og [a11 bakfra, cel 170](a-sekvens-a11-r3-l1.png) synliggjør rutene med forskjellige festepunkter. Måleoppskriftene er [a-sam004-analyse.py.txt](a-sam004-analyse.py.txt) og [a-gjenbrukskart.py.txt](a-gjenbrukskart.py.txt).

## Forberedt RGBA-oppskrift

[a-forbered-gjenbruk.py.txt](a-forbered-gjenbruk.py.txt) er kjørt i forberedelsesmodus uten å skrive PNG eller endre jobber. [a-rgba-forberedelseskontroll.json](a-rgba-forberedelseskontroll.json) bekrefter at alle syv aktuelle nye kildeark har RGBA, riktig canvas og transparent ytre padding. Hele nye rektangulære cels bevares med åtte HD-piksler rom rundt metadatafeltet; alfa når ikke klippegrensene. Ingen originalkontur brukes. Ompakking er bytekopiering uten skalering, og bevarer nytegningens eksisterende alfakanal. Oppskriften krever eksplisitt execute og rotens mottakscommit før PNG-skriving. Deretter kjøres uendret checker, med egen visuell kontroll og rutekart som neste leveransesteg. Checker hopper over svært små originalfelt under 20 kildepiksler; disse må også ses og dokumenteres særskilt. Festepunkt- og palettforskjellene ovenfor står uendret.
