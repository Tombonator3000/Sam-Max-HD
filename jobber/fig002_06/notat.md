# fig002_06

Dato: 2026-10-16T04:23:52.797027+02:00

Verktøy: image_gen.imagegen, innebygd bildeverktøy. Eksakt modellnavn ble ikke vist. Antall bildeforsøk: 1. Python med Pillow, numpy og scipy er brukt til tillatt rensing og plassering.

## Grunnlag

Sam i hovedkostyme 2, med vanlig blaagraa dress, hatt og stripet slips. Fem ruter der hendene samles, tre ruter med utstrakt arm og tre boyde positurer, i retningene fra jobb.json. Hovedark/sam.png er godkjent designreferanse. Alle 11 ruter er hele figurer; ingen separate hoder eller nye venstreruter er lagt til.

Original_1x.png og referanse.png er sett før nytegning, sammen med stilreferansen. ANALYSE.md, GJENNOMGANG.md og remake-skillen fra lokal main er lest. Prompt.txt ble brukt ordrett i første forsøk. Beskyttede jobbfiler er uendret.

## Etterarbeid

Ett bildeforsok. Bildemodellen tegnet rutene for store og med for stor avstand. Python skilte de 11 genererte figurene ved egen alfa, skalerte hver heltegning til originalens synlige bredde og hoyde og plasserte den i riktig rute. Myk alfa rundt nytegningen er bevart. Originalens pikselmaske er ikke brukt til kantklipping. Tilpasningen og kildeboksene er lagret i tilpass.py.txt og fig002_06-plassering.json.

## Kontroll og usikkerhet

Egenkontroll: OK. Se [fig002_06-egenkontroll.txt](../../rapporter/natt-fire-20261016-0406/fig002_06-egenkontroll.txt). Resultatet er sammenlignet statisk med original og stilreferanse. Størrelse, retning, motiv og synlige tilstander er kontrollert som enkeltbilder. Ingen motoravspilling, import eller ny godkjenning fra Tom er utført. Claude må kontrollere sammensetting og tilstandsskifte i mottaket. Ingen uavklart motivbetydning ble brukt som nytt designgrunnlag.

SHA-256 resultat: `0743e1553aac20b1c7ab8fe0061799383cc82ff8c611fad1146ce52142d0df48`.
