# Kildeplan for bestilling 27

Ti jobber og 40 beskyttede kildefiler er låst i kildehash.json. Sluttkontroll viser null kildeavvik. Alle ti jobbmetadata har sha256_prompt som avviker fra den faktiske promptfilen allerede ved analysestart. Faktiske promptbytes er låst og skal brukes ordrett; årsaken er ikke fastslått her, og ingen beskyttede filer er korrigert. Se b-kildehashkontroll.json. Dette er bare kildeanalyse. Ingen jobbresultater, produktkode, Git eller globale logger er endret. Alle ti originalkompositter, 24 metadataobjektfelt og de seks relevante leverte HD-grunnrommene er visuelt kontrollert. Registeret konsept/2026-10-12/objektbilder-959.csv er lest for objektidentitet; faktisk RGB-kilde styrer synlig tilstand foran navnet.

Kildebilder: [b-originalkontaktark.png](b-originalkontaktark.png), b-objektkontaktark-1..3.png, [b-HD-grunnrom.png](b-HD-grunnrom.png). Målinger: [b-kildebevis.json](b-kildebevis.json), [b-objektdifferanser.json](b-objektdifferanser.json), [b-bakgrunnsbevis.json](b-bakgrunnsbevis.json). Oppskrifter er bevart som b-analyse.py.txt, b-tilstandsbevis.py.txt og b-saerutsnitt.py.txt. Ingen differansemasker er brukt som erstatningsgrafikk.

## Felles lerret og bakgrunn

Alle jobber er opake RGB-kompositter på 1536 × 1024, med motiv [0,112,1536,800]. Originaldelene er 384 × 200. HD-boks beregnes som originalens romkoordinat minus delens regionstart, ganger fire, pluss lerretsfeltets start. Metadata nevner bare objektene tilordnet den aktuelle delen; det betyr ikke alltid at andre deler av samme lag er usynlige.

Åtte av de ti komposittene er byte-identiske med riktig grunnrom utenfor egne metadatarektangler. To unntak er kildebevist og må bevares:

* lag012_05_del1av2 har 5006 endrede originalpiksler utenfor obj133, alle forklart av underlag obj989_01. Bakgrunnen utenfor 133 er byte-identisk med lag012_03/04 i bestilling 26. Gjenbruk den samordnede nye bakgrunnen fra disse, ikke vanlig rom012 med grønne fjellformasjoner. Ingen forskjeller finnes utenfor unionen av 133 og 989.
* lag017_01_del2av2 har 426 endrede originalpiksler utenfor sin egen objektliste, fordi del 1 sine motiver også synes i overlappen. Unionen av begge delers metadata dekker alle endringer. Originaloverlappen er byte-identisk: 136 × 200. Bruk én fullmaster på 2528 × 800 med klipp 0 og 992 og identisk overlapp 544 × 800. De eksisterende HD-grunnrommene har også byte-identisk overlapp. Ikke produser delene uavhengig.

Rom 016 sine eksisterende HD-grunnrom har tilsvarende byte-identisk overlapp 1152 × 800. Kranfeltet i siste jobb på del 1 skal følge samme identitet som de fire foregående på del 2.

## Rom 012: tredje attraksjonsskulptur

Obj133_03 er en grønn kaktusskulptur på lav grå sokkel, med brun sombrero, rødt trekantet tørkle, to løftede armer og kildens små ansiktstrekk. Den skal forbli en skulptur. Ikke bytt til levende kaktus, menneskekropp eller andre rekvisitter. Sammenlign med bestilling 26 sine to andre konkrete skulpturer, ikke bruk dem som generisk anatomi. Bakgrunnstilstanden har røde steinformasjoner, med bevart bensinpumperekke, Snuckey's-skilt og tom vei. Obj989_01 er uttrykkelig metadataunderlag. Kopp på fortauet og øvrige grunnromsdetaljer skal følge kilden, uten ekstra bil.

## Rom 015: trykkplate og liten vekt

Obj144_01, carny-strength-meter, er den lave treplattformen med grønn pute/platedel ved foten av styrkemåleren. Hele plattformens perspektiv og putehøyde avviker litt fra grunnrommet; 329 kildepiksler endres. Det er ikke en ny stående figur eller hele målerstolpen.

Obj145_01, carny-strength-weight, er en liten mørk grålilla vektform som dekker deler av målerens svarte strek ved foten. Bare 54 originalpiksler endres, i lokal boks [5,1,7,11]. Ikke gjenbruk lag 01 sin plattformtilstand eller legg til nye tall. Hall of Oddities, CREEPY og øvrig romtekst skal bevares fra riktig grunnrom. Se [b-saerutsnitt-1.png](b-saerutsnitt-1.png).

## Rom 016: fjernede utstillingsdeler og faktiske mikrotilstander

**Lag 01:** Obj150_01 viser at den brune/grå resten på gulvet foran Bruno er borte. Gulv og hvit ellipse ved isområdet er fortsatt synlige. Obj152_01 viser at både den brune hånden og glassbeholderen er borte; mørk bakvegg og blå underlagsflate står igjen. Ikke tegn hånden tilbake fordi registeret heter freak-jj-hand. Samtidig er kran 01 og glassfigur 01 aktive.

**Lag 02:** Obj153_01 er Insect Lad, samme karikerte person med briller, orangebrunt hår, hvit skjorte, grønne bukser og hvite sko. Hode/kroppstilling endres i forhold til grunnrommet. Bevar alle kildelemmer og håndplasseringer, uten ny identitet. Obj167_01 fjerner hele den hvite/blå isformen og sokkelen med BRUNO-skiltet; gulv og svart gardin erstatter feltet. Den separate blanke kulen på pidestall står igjen, og skiltet over feltet ligger utenfor selve fjerningsrektangelet. Ikke fyll det tomme feltet med Bruno, annen figur eller ny dekor. Se [b-saerutsnitt-2.png](b-saerutsnitt-2.png).

**Obj154, Human Enigma:** Dette er figurens grå kranhode over eksisterende dresskropp, ikke et nytt rør installert i rommet. Tilstand 01/02/03 har samme krangeometri og ulik blå dråpe ved venstre tut. Mot grunnrommet er bare 4/6/14 kildepiksler endret i samme lille region. Mellom 01 og 02 endres 3 piksler; mellom 02 og 03 endres 14. Tilstand 04/05 vrir/løfter kranen og har ingen hengende dråpe; topphåndtakets vinkel endres også. Bevar kropp/hodekoblingen og kranens topphåndtak. Ikke dedupliser de første små tilstandene eller skaler hodet for å lage dråpebevegelse. [b-obj154-familie.png](b-obj154-familie.png) og b-obj154-differanser.json viser alle fem.

**Obj155, figuren i grønt glass:** Bevar den spesifikke runde hudfargede karikaturen, grønne konturlinjer, lemmer og glassform. Tilstand 01 har fire hvite boblepunkter; 02 har tre; 03 har ett. 02 og 03 skiller bare 4 originalpiksler i boblefeltet, ikke kroppen. 01 til 02 flytter også kropp/hode litt. 04 har to boblepunkter, lokalt (33,7) og (32,10), men endrer arm-/hånd- og kroppsfelt, totalt 356 piksler fra 03. Ikke normaliser figuren til et vanlig menneske, mat eller et nytt monster. [b-obj155-familie.png](b-obj155-familie.png) og b-obj155-differanser.json viser dette.

Lag 03/04 har bare respektive 154/155-tilstand, og må ha grunnrommets håndglass, gulvrester og Bruno-is tilbake. Lag 05 har bare 154_05 og grunnrommets øvrige tilstander. Lagnummer er eksportpakking, ikke dokumentert hendelsesrekkefølge.

## Rom 017: én sammenhengende kompositt

Del 1 tilføyer obj169_01,178_01,180_01,181_01 og 184_01. Del 2 tilføyer 171_01,182_01 og 183_01, men viser også avklipte del 1-felter i overlappen. Åtte unike metadataobjekter skal derfor finnes i fullmasteren.

* 169: WIN-maskinens nedre grønne frontfelt er åpnet/avdekket med et lite rødt, lyst og mørkt innhold. Bevar den konkrete formen uten å gjette et dyr eller nytt premieskilt. De svarte spillhullene ovenfor skal beholdes.
* 178: Det rødlige runde linsefeltet er borte fra den blå/grå holderen. Tomt mørkt/ blått felt er tilsiktet; navnet magnifying-lens betyr ikke at linsen skal tegnes inn.
* 184: Spaken på den røde/grå kontrollboksen er løftet, med to synlige røde grep i den aktuelle posisjonen, mot grunnrommets ene lavere grep. Bevar sporene og sølvkanten.
* 171: Trixies dør er åpen. Bevar svart innside, rødt innvendig felt, terskel og dørkant. Ingen figur står i åpningen.
* 180/181/182: Rød, gul og grønn vimpel, hver med sin konkrete bølgeform og spissretning. Ikke bruk samme kurve i tre farger. Fargene, stangplassene og flaggtoppene skal bevares.
* 183: Den orangebrune propellen på den grønngule anda har den konkrete skrå posisjonen i 01. Hele anda eller skiltet skal ikke nytolkes.

[b-saerutsnitt-3.png](b-saerutsnitt-3.png) viser fjernet linse, premiefelt og spak. [b-midway-familiekontekst.png](b-midway-familiekontekst.png) viser 20 motiver fra alle åtte eksisterende lag017-kildejobber som kontekst for senere tilstander. Kildens senere 03/04-vimpler har synlig fragmenterte felter. Ikke fyll dem til hele flagg eller finn på revet stoff uten ytterligere bevis. Propellens senere tilstander har egne synlige bladposisjoner. Ingen runtime eller timing er fastslått.

## Anbefalt samordning før produksjon

Samordne kaktusskulpturen med A sin obj989_01-bakgrunn fra 26. Behandle begge 015-jobbene samlet med samme styrkemåleranker. Én produksjonseier for 154/155-familiene sikrer at mikrotilstander beholder samme kranhode og glassfigur; den bør også kontrollere fjerningsfeltene 150/152/167 mot riktig grunnrom. Begge 017-delene må produseres fra felles master og vurderes mot hele vimpel-/propellfamilien før senere bestillinger.

Ordrette låste prompter kan suppleres med disse kildekorreksjonene. Seks ulike prompttekster er lest. Rom 017-promptens generiske formulering om separate deler må presiseres til én felles master, fordi kildeoverlappen er identisk. Rom 016-promptens beskjed om å bevare utstillingene gjelder det faktiske lagets synlige tilstand, inklusive fjernede objekter. Skilt utenfor utsnittet skal ikke legges inn for å oppfylle den generiske skiltlisten. Bildegenerering skal skape nytt innhold; kildepikselmasker, originalkonturkopi og lokal warp er ikke erstatning for det. Teknisk kontroll må suppleres med feltnær visuell kontroll, særlig mikrodråper, bobleantall, fjernede objekter og fragmenterte vimpler. Denne planen innebærer ingen produksjons-, runtime- eller individuell bildegodkjenning.

## Eksakte objektbokser

Bokser er [x,y,bredde,høyde]. Se b-kildebevis.json for bakgrunns-SHA og alle originalkoordinater.

| Jobb | Objekt | Originalrekt i rom | HD på leveranselerret |
|---|---|---|---|
| lag012_05_del1av2 | obj133_03 | [184, 64, 88, 96] | [736, 368, 352, 384] |
| lag015_01_del2av2 | obj144_01 | [432, 120, 56, 24] | [736, 592, 224, 96] |
| lag015_02_del2av2 | obj145_01 | [432, 120, 16, 16] | [736, 592, 64, 64] |
| lag016_01_del2av2 | obj150_01 | [360, 160, 32, 16] | [1056, 752, 128, 64] |
| lag016_01_del2av2 | obj152_01 | [136, 80, 32, 32] | [160, 432, 128, 128] |
| lag016_01_del2av2 | obj154_01 | [216, 64, 40, 32] | [480, 368, 160, 128] |
| lag016_01_del2av2 | obj155_01 | [264, 48, 48, 56] | [672, 304, 192, 224] |
| lag016_02_del2av2 | obj153_01 | [168, 48, 48, 64] | [288, 304, 192, 256] |
| lag016_02_del2av2 | obj154_02 | [216, 64, 40, 32] | [480, 368, 160, 128] |
| lag016_02_del2av2 | obj155_02 | [264, 48, 48, 56] | [672, 304, 192, 224] |
| lag016_02_del2av2 | obj167_01 | [368, 64, 112, 128] | [1088, 368, 448, 512] |
| lag016_03_del2av2 | obj154_03 | [216, 64, 40, 32] | [480, 368, 160, 128] |
| lag016_03_del2av2 | obj155_03 | [264, 48, 48, 56] | [672, 304, 192, 224] |
| lag016_04_del2av2 | obj154_04 | [216, 64, 40, 32] | [480, 368, 160, 128] |
| lag016_04_del2av2 | obj155_04 | [264, 48, 48, 56] | [672, 304, 192, 224] |
| lag016_05_del1av2 | obj154_05 | [216, 64, 40, 32] | [864, 368, 160, 128] |
| lag017_01_del1av2 | obj169_01 | [232, 112, 40, 32] | [928, 560, 160, 128] |
| lag017_01_del1av2 | obj178_01 | [256, 88, 24, 16] | [1024, 464, 96, 64] |
| lag017_01_del1av2 | obj180_01 | [224, 8, 48, 24] | [896, 144, 192, 96] |
| lag017_01_del1av2 | obj181_01 | [280, 24, 40, 24] | [1120, 208, 160, 96] |
| lag017_01_del1av2 | obj184_01 | [64, 112, 32, 32] | [256, 560, 128, 128] |
| lag017_01_del2av2 | obj171_01 | [408, 80, 56, 72] | [640, 432, 224, 288] |
| lag017_01_del2av2 | obj182_01 | [472, 8, 40, 16] | [896, 144, 160, 64] |
| lag017_01_del2av2 | obj183_01 | [384, 0, 32, 24] | [544, 112, 128, 96] |

## Rettet bobletelling ved produksjonskontroll

Den første visuelle analysen overså det nederste hvite punktet i155_04 nær hodet. Numerisk kontroll av original_RGB viser fire/tre/ett/to separate hvite punkter i155_01..04. I04 er de lokale koordinatene (33,7) og (32,10), begge RGB[251,251,251]. Kildeplanens tekst er korrigert; beskyttede originaler er uendret.
