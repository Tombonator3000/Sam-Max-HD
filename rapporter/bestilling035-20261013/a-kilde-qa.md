# Bestilling 35, A: seks uthustilstander

Seks leveranser, fem innebygde imagegen-kall inklusive lokal retting av 04. Eksakt modellnavn er ikke eksponert. Kildeanalyse finnes i a-kildeplan.md og a-familiebevis.json. Kildeidentiske helbilder 02/06 og 03/05 bruker byte-identiske nye resultater. Dette beviser ikke runtime-rekkefølge.

Alle seks uendrede leveransekontroller gir OK. Eksplisitt objektkorrelasjon er 0,9613 til 0,9838, dokumentert per jobb i a-leveranser.json. Canvas er 1536 × 1024, kunstfelt 1536 × 800 ved [0,112], padding nøyaktig RGB 128. Kildehashkontroll omfatter de 80 tidligere låste filene.

Helbildene og de seks original/HD-nærbildene er sett samlet i a-samlet-kontaktark.png og a-objektqa.png. Tilstand 01 beholder mørk åpen front og smal skrå dør. Øvrige beholder egne lukkede stillinger med buet mørk åpning, lilla side og gulbrun front. Perspektivet forblir skjevt. Tilstand 04 har en rundere nedre mørk åpning enn de øvrige nye variantene; kildens lille åpning er grovt pikselert og skrå/avrundet. Dette er en synlig detaljtolkning, ikke en ny gjenstand. Nærbildene viser også nye trelinjer og jevnere kanter; de er ikke pikselidentiske med kilden.

Kun feltet [640,144,224,224] er erstattet. Fire HD-pikslers rektangulær overgang mellom to nytegnede bilder, ingen originalmaske eller lokal geometriwarp. Utenfor dette feltet er grunnrommets nye HD-piksler byte-identiske. Skilt, trær, steiner, tau og øvrige romdetaljer bevares derfor. Ingen synlig rektangulær fargelapp funnet i samlet kontroll.

Råfiler, nøyaktige prompter, kilde- og resultat-SHA samt oppskrift finnes i a-leveranser.json og a-sammensetting.py.txt. Resultatene er klare for roots mottakskontroll. Ingen runtime-test eller ny individuell brukergodkjenning er utført.

## Retting etter roots mottakskontroll

Roots nærkontroll påviste at 04s nedre åpning var for oval. Min første vurdering av dette som detaljtolkning var for romslig. a-04-nedre-familiebevis.png sammenligner kildene 02/03/04, og et eget nytt imagegen-utdrag retter åpningen til en kantet skrå firkant. a-04-rettingsqa.png viser kilde, før og etter. Bare [760,307,60,38] er endret fra førbildet, resten byte-identisk. Ny checker er OK; oppdatert SHA/korrelasjon i manifest og a-04-rettingsbevis.json. Ingen originalmaske eller warp.
