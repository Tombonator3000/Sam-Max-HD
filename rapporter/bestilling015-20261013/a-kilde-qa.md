# Bestilling 15 A: kilde og familiekontroll

Tre veisegmenter fra Highway Surfing er levert: obj604_01, obj605_01 og obj606_01. Kildenavnene i konsept/2026-10-12/objektbilder-959.csv er surf-street-11, surf-street-12 og surf-street-13. Alle er egne objekt-ID-er med tilstand 01. Dette dokumenterer ikke runtime-rekkefølge.

Originalene, 4x-referansene, jobbmetadata, ordrette promptfiler og b-kildeplan.md er lest og visuelt sammenlignet før produksjon. Stil/rom007_del1av2.png er godkjent referanse for malt kvalitet, ikke innhold. Romnotens HUD, Score, biler og skilt gjelder ikke disse utsnittene; dette er korrigert i separate produksjonsprompter uten endring av kildene.

Motivet er en svært lav grålilla veiflate med mørke sidefelt RGB (7,7,0) og én blekgul markering ved nedre kant. 604 er rett, 605 heller mot venstre nedover, 606 mot høyre. Toppen av veien flytter seg mellom variantene; de er ikke speilet fra samme bilde. Ingen HUD, biler, tekst, nye kjørefelt eller asfaltkorn er lagt til. Nytegningene har svak malt fargevariasjon og glattere gradient enn ditheringen, ikke pikselidentisk palett.

## Produksjon og teknisk kontroll

Innebygd ChatGPT-bildegenerator er brukt. Eksakt modellnavn er ikke eksponert. 604 og 606 har ett forsøk hver; 605 har to. Første 605 er bevart som a-obj605_01-kandidat01.png og ga FEIL: skift 0,12, blokk 3,05, kant 0,95. Nytt forsøk fra beskyttet original forbedret geometrien; avvist kandidat ble ikke brukt som anker.

Valgt råmotivs rektangel er beskåret og helskalert til 1280 × 96, deretter plassert ved (128,464) på 1536 × 1024 med eksakt padding RGB (128,128,128). Ingen lokale flytt, vektortrace, warp eller originalsilhuettmaske. Genererte piksler med alle kanaler under 40 er normalisert til sidefeltets RGB (7,7,0); dette er en fargeregel på nytegningen, ikke originalkontur. Antialias ved overgangen kan ha mellomfarger. a-oppskrift.py.txt rekonstruerer og sammenligner sluttresultatene fra råbildene.

| Jobb | Uendret egenkontroll | Global / blokk / kant |
| --- | --- | --- |
| obj604_01 | OK | 0,02 / 0,22 / 0,99 |
| obj605_01 | SJEKK | 0,05 / 1,13 / 0,98 |
| obj606_01 | OK | 0,09 / 0,13 / 0,99 |

## Presise gjenværende avvik

a-familiemaal.json måler lokale HD-koordinater innen motivfeltet, med inklusive x-endepunkter. Målingene er read-only og styrer ingen konturmaskering. Gulstripe velges ved rød minus blå over 35 og grønn over 130; vei ved blå over 40. Antialias påvirker grenseverdiene.

604: kildens stripe starter y60 og x620..655, og slutter i samme intervall. Dette samsvarer med HD. Øvre veikant er original 132..1151, HD 133..1149.

605: original stripe starter y60 x640..671, HD y59 x643..673. Nederst er original 620..655, HD 619..656. Øvre vei er original 176..1195, HD 174..1192. Venstrehellingen er bevart, men eksakt skulder og kantposisjon er ikke identiske. Leveransen er derfor uttrykkelig SJEKK.

606: original stripe starter y60 x608..643, HD y59 x609..642. Nederst er original 624..659, HD 624..663. Øvre vei er original 84..1103, HD 85..1102. Høyrehellingen er bevart; nedre høyrekant er fire HD-piksler bredere. Teknisk OK er ikke et løfte om identiske konturer.

Alle tre er visuelt sett samlet i [a-samlet-qa.png](a-samlet-qa.png). [a-leveranser.json](a-leveranser.json) har SHA256, råbilder, utsnitt og kontrollfiler. [a-kildebevis.json](a-kildebevis.json) bekrefter alle 40 låste kildefiler uendret. Metadataenes historiske prompt-hashavvik er ikke rettet; faktisk prompttekst er brukt ordrett.

Ingen motor, bygg, Highway Surfing-lagkomposisjon eller runtime er testet. Ingen ny individuell brukergodkjenning er innhentet. Parent håndterer samlet bestilling, kø og Git.
