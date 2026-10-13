# Kildeplan for bestilling 24

Kun analyse, 13. oktober 2026. Ingen generering, jobbfiler, Git, globale logger eller produktkode er endret. Ti jobber fra GRAFIKKLISTE.md er låst med 40 SHA-256 i [kildehash.json](kildehash.json). [Originalkontaktark](original-kontaktark.png), [objektbokser](a-objektbokser.png) og [TV-nærbilder med nabotilstander](a-tv-naerbilder.png) er visuelt lest. Kildeanalyse følger source-faithful-production, BESTILLING.md og den allerede avklarte lagkontrakten i bestilling 22.

## Jobber og konkrete motiver

Alle er opake romkompositter, ikke atlas eller alfaark. Hele rommet er 488 x 200, men denne bestillingen bruker bare region [0,0,384,200], motiv [0,112,1536,800] på 1536 x 1024. Delnavnet 1av2 betyr ikke at et nytt par må bestilles eller en fullmaster må genereres for disse uttrekkene. Metadata eier én konkret objektboks per jobb.

| Jobb | Ressurs | Originalrekt | HD-rekt på lerret | Synlig tilstand |
|---|---|---|---|---|
| lag007_12_del1av2 | obj071_0C | 144,88,24,24 | 576,464,96,96 | To små hudfargede former på grønn TV-flate; venstre oransje/brun med blått nederst, høyre lys krem med mørkerød/hvit ringform |
| lag007_13_del1av2 | obj078_01 | 144,88,24,24 | 576,464,96,96 | Grønt/grått uregelmessig stripemønster i TV |
| lag007_14_del1av2 | obj067_01 | 136,64,40,24 | 544,368,160,96 | Tynn mørk bøyd antenne med bred kantet løkke og kort nedre feste |
| lag007_15_del1av2 | obj071_0D | 144,88,24,24 | 576,464,96,96 | Samme motivfamilie som 0C, konkret endret øye-/ansiktsfelt |
| lag007_16_del1av2 | obj078_02 | 144,88,24,24 | 576,464,96,96 | Annen grønngrå stripefordeling enn 078_01 |
| lag007_17_del1av2 | obj067_02 | 136,64,40,24 | 544,368,160,96 | Annen bred kantet antenneløkke, annen venstre kant og øvre retning |
| lag007_18_del1av2 | obj071_0E | 144,88,24,24 | 576,464,96,96 | Kildekompositt er identisk med 0D |
| lag007_19_del1av2 | obj078_03 | 144,88,24,24 | 576,464,96,96 | Grønne/grå vertikale brudd blandet med fersken, brune, røde og blå motivrester |
| lag007_20_del1av2 | obj067_03 | 136,64,40,24 | 544,368,160,96 | Antennen mangler; bare grålilla vegg, skygge og eksisterende små veggmerker |
| lag007_21_del1av2 | obj071_0F | 144,88,24,24 | 576,464,96,96 | Kildekompositt er identisk med 0D og 0E |

Registeret konsept/2026-10-12/objektbilder-959.csv kaller 071 office-tv, 078 office-tv-static og 067 antenna, alle smap. Dette støtter komponentidentiteten, men ikke navn på TV-film/figurer, replikk eller faktisk avspillingsrekkefølge. Ingen slik historie er bevist. Bevar konkrete fargeformer og antall uten å legge til lesbar tekst, ansiktsdetaljer eller moderne støyeffekt.

TV-kassen rundt skjermen er den samme lyse grå/lilla, skrå avrundede formen med mørkere knapper til høyre. 067-lagene har kildens grå, tomme/reflekterende TV-skjerm, ikke det fargede motivet fra 071 eller 078. Antenne067_03 må ikke få en ny antenne bare fordi registeret heter antenna.

## Grense mot bestilling 23 og ekte mikroforskjeller

B sin kildeanalyse 23 er samordnet. Siste 23-ressurs er obj071_0B i lag11; første 24 er obj071_0C i lag12. Tilstandene er hexstrenger. Lag12 til lag21 er ikke ti desimaltrinn i samme TV-ressurs, men veksler mellom tre objektfamilier.

Målt 071-familie: 0B til 0C endrer 22 originalpiksler; alle ligger i TV-boksen. Det venstre lille oransje/brune motivets kontur, svarte punkt og blå felt endres. 0C til 0D endrer syv piksler: (158,94), (159,95), (160,95), (150,100), (151,100), (148,101), (151,101) i romkoordinater. Høyre brune øyestreker blir blant annet svarte/kremfargede, og venstre nedre motivfelt endres. Alle før/etter RGB finnes i [familiedifferansene](a-familiedifferanser.json).

0D, 0E og 0F har null ulike RGB-piksler i HELE kompositten. [Palett- og likhetsbevis](a-palett-og-likhetsbevis.json) inneholder hash av dekodet original-RGB og filbytes. Dette er dokumentert likhet i disse eksportene, ikke bevis på lik runtime-betydning eller tillatelse til å slå ressurs-ID-ene sammen. En nygenerert, kontrollert HD-komposisjon kan senere gjenbrukes for disse tre med separat proveniens per jobb.

078_01 til 02 endrer 100 piksler; 02 til 03 endrer 128. Naboressurs078_04 i bestilling 25 er bare lest som kontekst og har 167 endringer fra 03. 067_01 til 02 endrer 102 piksler; 02 til 03 endrer 65. Ingen av disse skal blindkopieres. B påviste dessuten en én-pikselforskjell mellom 071_04 og 09 i bestilling 23; den observasjonen må ikke feilaktig overføres til alle familier som generell duplikatregel.

## Bevis for riktig bakgrunn

Alle ti originale lagkompositter er BYTE-IDENTISKE i dekodet RGB med rom007_del1av2/original_1x.png UTENFOR egen metadatarekt. Dette er målt separat for hvert felt i [a-feltbevis.json](a-feltbevis.json), ikke antatt ut fra romnavnet. Levert jobber/rom007_del1av2/resultat.png er derfor riktig bilde_to og egnet HD-basis. Ankeret er visuelt sett og SHA-låst i a-konteksthash.json. Brukes som levert referanse, ikke ny individuell brukergodkjenning.

Telefonen skal ha rødt rør og standardvinduene skal beholdes, med lukket SAM/MAX-dør, dartprosjektiler, papirer, gulvrot og resten av grunnrommets innhold. Origin/main:docs/gpt-romnotater.csv for rom7 understreker all denne uordenen. Tekst som faller utenfor dette venstre utsnittet skal ikke flyttes inn.

Lag03 i bestilling 23 har seks egne indikatorpiksler på telefonpanelet utenfor TV-boksen. Bruk derfor ikke hele lag03 som blind basis for 24. For TV-jobbene her er det seks RGB-avvik mot lag03 utenfor TV. Lag02 fra bestilling 22 avviker i 975 piksler utenfor TV ved sammenligning med TV-jobbene i24, særlig telefon/vindu. For antennejobbene kan heller ikke farget TV fra lag04 brukes: det gir 199 avvik utenfor antenneboksen. Den egne boksen, ikke en fast TV-maske, må være sammenligningsgrunnlaget.

## Anbefalt senere produksjon

Gjenbruk det NYTEGNEDE grunnrom007-HD utenfor en dokumentert rektangulær lokal tegneflate, fordi kildelikheten nå er bevist. Bruk innebygd imagegen til nye TV-/antennekomponenter med riktig originalkompositt og levert HD-rom som referanser. Kopier ikke originale piksler, trace ikke sourcekonturen og bruk ikke originalsilhuettmaske. Ved presis plassering kan et helt nygenerert rektangel skaleres og legges på riktig HD-boks; søm mot eksisterende HD-bakgrunn må kontrolleres visuelt. En større generert kontekstflate kan brukes til tegnehjelp, men importboksen og alle synlige tilstander er fortsatt faste.

071-familien bør kontrolleres samlet: delte nye detaljer kan holdes stabile, mens de dokumenterte øye-/konturendringene nytegnes. 078 har egne konkrete stripemønstre og fargefragmenter, ikke generisk tilfeldig statisk støy. 067 har to ulike løkker og ett fravær; bakgrunnens merker i fraværstilstanden beholdes. For 0D/0E/0F kan samme verifiserte nye bilde gjenbrukes, men bevar tre jobber og henvis til null-differansebeviset.

Lever senere full RGB 1536 x 1024, nøytral padding RGB128, hvert objektnærbilde og uendret sjekk_leveranse.py med eksplisitt perobjektkantmåling. Checkerens stille OK-løkke og mulige hopp ved svak kant må rapporteres korrekt. Teknisk kontroll er ikke visuell godkjenning, import eller runtime. Ingen produksjon er utført i denne analysen.

## Analysefiler

a-analyse.py.txt og a-feltanalyse.py.txt dokumenterer målingene. a-tilstandsbevis.json inneholder metadata, registerrader, TV-paletter, parvise sammenligninger og RGB-endringer mellom kønaboer. For ANTENNE-jobber gjelder TV-paletten bare kontekst; a-palett-og-likhetsbevis.json har korrekt palett for hvert faktisk objektfelt. a-feltbevis.json bruker riktig metadatarekt ved bakgrunnskontroll. Køkobling er analyseorden og ikke runtime-rekkefølge. Eksterne kontekstfiler er bare låst i a-konteksthash.json; de er ikke ekstra produksjonsjobber.
