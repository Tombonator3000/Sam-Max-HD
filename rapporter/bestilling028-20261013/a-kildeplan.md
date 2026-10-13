# Kildeplan for bestilling 28

Kun analyse. Ingen bildeproduksjon eller jobbfiler er endret. Ti jobber er låst med 40 beskyttede kildefiler i `kildehash.json`. To neste 019-tilstander er låst med åtte ekstra filer i `a-ekstra-konteksthash.json`. Alle ti originaler og samtlige 27 metadatafelt, inkludert ekstra kontekst, er sett i originalkontaktarket og `a-objektfelt-1.png` til `a-objektfelt-4.png`. Source-faithful-production, metadata, originalregister og relevante romnotater er brukt.

C skal senere produsere de seks 017-jobbene. A skal senere produsere de fire jobbene lag018_01, lag018_02, lag018_03 og lag019_01. Ingen generering før root har lest og samordnet planen.

## Format og kildebevis

Alle leveranser er opake RGB-kompositter på 1536 x 1024 med padding RGB 128. Rom 017 har motiv [0,112,1536,800]; minispillene har [128,112,1280,800]. Ingen svart nøkkelfarge eller alfa er påvist som leveransekrav. Kildens svarte hull, tellefelt og mørke gardiner er synlig innhold.

`a-lagbevis.json` dokumenterer metadata og forskjeller mot grunnrom. `a-feltbevis.json` inneholder hver boks, faktiske RGB-paletter, fargetellinger og registerrad. `a-familiebevis.json` dokumenterer panoramalikhet og forskjeller mellom tilstander. `a-ankerhash.json` låser de eksisterende rom-HD-referansene; dette er konsistensreferanser, ikke ny individuell brukergodkjenning.

## Rom 017: tre sammenhengende panoramatilstander

Hver av tilstandene 02, 03 og 04 har originalmaster 632 x 200. Delene starter ved x=0 og x=248, med identisk originaloverlapp 136 x 200. Produksjon skal bruke én 2528 x 800-master per tilstand, klipp x=0 og x=992 med 544 x 800 byte-identisk overlapp. Tre originale analysemasters er lagret i rapporten.

Endringer utenfor hver dels lokale objektliste er legitime bidrag fra den andre delen. Lag02 del2 har 350 slike piksler, lag03 del2 har 167, lag04 del1 har 103 og lag04 del2 har 70. Etter union av begge delers metadata er det NULL kildeendringer utenfor objektfeltene i alle tre tilstander. Samlede endringer mot grunnrommet er 3372, 413 og 376 piksler.

Tilstand 02 har rødt WIN-frontfelt med sin egen gule åpning/plate i 169_02. Felt173_01 er fravær av den røde kjeglen: bare den gule stjernekransen og tomme brune midten ligger foran gjerde og skog. Ikke fyll inn en kjegle. Felt172_01 er den lille grå metall-låsemekanismen på den lilla vogndøren. Ikke sett inn en ny dør eller et større håndtak.

180, 181 og 182 er henholdsvis rød, gul og grønn vimpelfamilie. 02 har brede sammenhengende bølgeformer. 03 og 04 har kildeegne smale, oppbrutte fliker og enkeltpunkter. Dette skal ikke normaliseres til fylte tekstilduker eller generisk vindbevegelse. Antall synlige biter og brudd følger hvert nærbilde. 183 er rødbrun propell på den grønne fugleliknende attraksjonen, med forskjellige bladretninger i 02, 03 og 04; bevar også avklipping ved bildets topp. 184_02 viser to røde spaktopper og de egne mørke skrå stengene i kontrollkassen. Antall/feste må sammenlignes med 27 sin tilstand01.

C har fått disse målingene og skal bruke sitt samordnede grunnlag fra bestilling 27. `c-017-fullmaster.png` er sett som kontekst, men dens aktive objektstillinger fra lag01 skal ikke blindt gjenbrukes som bakgrunn i 02 til 04. Riktig generelt romunderlag og hver kildeegne tilstand må holdes adskilt. Fullscene må bevare CONE OF TRAGEDY, WAK A RAT, WIN, TRIXIE og GUN, gjerder, ledningen langs bakken og øvrige romobjekter.

## Rom 018: ansiktsfelt og ufullstendige Max-detaljer

Ingen av disse tre originalene viser rotter i hullene eller en klubbe. Sam står til høyre i grålilla hatt og dress, lys skjorte, blåsvart slips, oransjebrun pels og med den nederste hånden avskåret av motivkanten. Fem svarte hull er tomme og skal forbli tomme. Poengpanelet øverst til venstre sier HIT 20 WIN og har to stjerner, men selve svarte tellefeltet er tomt. WAK-A-RAT på kassen beholder originalens avkutting.

| Jobb og objekt | Kilderekt [x,y,w,h] | HD-rekt på lerret | Synlig tilstand |
|---|---|---|---|
| lag018_01 / 194_01 |216,48,40,24|992,304,160,96|Sams tunge på høyre kinn; helt kildeidentisk med grunnrommets felt|
| lag018_01 / 195_01 |216,32,32,24|992,240,128,96|To åpne smale svarte øyne; helt kildeidentisk med grunnrommets felt|
| lag018_01 / 196_01 |24,112,56,16|224,560,224,64|To separate avskårne krem/grå felt med korte mørke øyestreker, blå bakgrunn mellom|
| lag018_02 / 194_02 |216,48,40,24|992,304,160,96|Annen, lavere og mer vannrett rødoransje tungeform|
| lag018_02 / 195_02 |216,32,32,24|992,240,128,96|Endret blikk med kort brun strek over høyre svarte øye|
| lag018_02 / 197_01 |48,120,16,16|320,592,64,64|Liten krem/grå firkant med rødoransje neseform og blå nedre del|
| lag018_03 / 194_03 |216,48,40,24|992,304,160,96|Rundere rødoransje tunge, lenger inn mot snuten|
| lag018_03 / 195_03 |216,32,32,24|992,240,128,96|Begge øynene lukket som tynne brune knekkstreker|

Registeret kaller 194 whack-tongue, 195 whack-sam-eyes, 196 whack-max-eyes og 197 whack-max-nose. De konkrete bildene bekrefter tunge-/øyebevegelsene og nese-/øyedetaljene. De små Max-feltene er imidlertid bare separate utsnitt i denne eksportkompositten: de har ingen hel hodekontur, lange ører eller kropp rundt seg. Ikke fullfør dem til et helt Max-ansikt, ikke tegn rotter eller reparer de merkelige avskjæringene. Den faktiske runtime-sammensetningen er ikke vist her.

194 og 195 overlapper i [216,48,32,8]. For hver tilstand anbefales ett sammenhengende ansiktsutsnitt [216,32,40,40], tilsvarende HD [992,240,160,160], slik at øyne/tunge ikke genereres med motstridende overlapp. I tilstand01 er begge feltene identiske med rom018-originalen og kan gjenbruke levert rom018-HD direkte. Bare 196 trenger nytegning der.

Alle tre 018-kompositter er identiske med grunnrommet utenfor egen metadataunion. Endringer totalt er 524, 347 og 219 piksler. Tilstand01 har alle 524 i 196; 194_01 og 195_01 har null endringer. Palettantallene er 12 farger i hver tungeboks, 10/9/9 i øyeboksene, 7 i Max-øyefeltet og 8 i nesefeltet. Dette inkluderer komposittbakgrunn, ikke alfa.

## Rom 019: Max ved brettkanten, uten poengpanel

Lag019_01 viser Max til venstre bak det oransje brettet. Han har kremhvit/grå pels, to lange bøyde ører med rosa innside, to små svarte øyne, liten rødoransje nese, hvit sikksakktannrekke og synlige poter ved venstre brettkant. Venstre øre og pote er avskåret ved scenekanten. Ingen full kropp skal konstrueres. Sam, fem tomme hull og den blå gardinbakgrunnen følger rom019. Det finnes IKKE poengpanel i dette rommet; panelet fra rom018 skal ikke kopieres inn.

Obj200_01 er [0,32,96,128], på leveranselerret [128,240,384,512]. Boksen har 18 faktiske RGB-farger. Den endrer 5131 piksler mot rom019 og null utenfor objektboksen. Dette gjør eksisterende rom019-HD egnet som fast rombasis utenfor den konkrete nye Max-komponenten. Sams arm skal fortsatt være nede i denne tilstanden.

Nabojobben lag019_02 i bestilling29 har obj201_01, samme boks og 18 farger, med egen bøyning av ørene. Den skiller 3636 kildepiksler fra lag019_01. Den er ikke en duplikat og heller ikke bevis for animasjonens avspillingsrekkefølge.

Lag019_03 er kontekst med obj198_01 i samme boks og 18 farger, mer oppreiste lange ører og annet hodeuttrykk. Metadata oppgir underlag obj202_01 og obj199_01. Den synlige Sam-armen, knyttet hånd og rød klubbedel utenfor Max-boksen kommer fra denne sammensatte tilstanden, ikke fra et nytt krav til lag019_01. Det er 3676 endrede piksler UTENFOR Max-boksen, innen [96,32,204,115] angitt som venstre, topp, høyre, bunn. Derfor må denne varianten ikke brukes som identisk bakgrunn for lag019_01. Alle åtte ekstra kildefiler er låst kun som kontekst.

## Produksjonsgrunnlag og gjenstående usikkerhet

Bruk innebygd imagegen med ordrett jobbpompt og separat kildepresisering. Bevar originalens palett, avkutting og merkelige delkomposisjoner. Godkjente Sam/Max-hovedark kan støtte identitet, men skal ikke overstyre kildens uttrykk, manglende kroppsflater eller positur. Gjenbruk riktig allerede levert rom-HD der bakgrunnslikhet er målt. Vanlig helskalering og presis rektangulær plassering er tillatt; ingen originalmasker, pikseloppskalering som nytegning, lokal warp eller vektorrekonstruksjon.

Teknisk checker skal kjøres uendret på faktiske leveranser, med eksplisitt perobjektkontroll og nærbilder. Samlet visuell vurdering må sjekke fem hull, tomme poengtall, Sam-uttrykk, de ufullstendige små Max-feltene, og forskjellene mellom Max-ørene. Rom017 krever i tillegg fullmaster og alle tre vimpler/propelltilstander. Motivene er kildeavklart på eksportnivå; faktisk motorlagdeling, poenglogikk, timing og runtime-rekkefølge er ikke testet eller utledet fra navn alene.

## Samordnet beskjed fra C om bestilling 27

C har nå levert `rapporter/bestilling027-20261013/c-017-fullmaster.png`, SHA-256 `ddf404139b1b463c2d28399044f08336727aa43049a0f24c4604e07e90394aae`. Den viser alle åtte 01-objekter og er sett som fullscene. C oppgir kildeegne bølger for rød/gul/grønn vimpel og 01-propellens diagonal; avrundede/blankere profiler er dokumentert i deres QA. Skyfeltene er fargesammenpasset med jevnt bilineært RGB-felt uten warp.

C sitt tomme linsefelt178 krevde 12 ekstra HD-piksler oppover for å fjerne en gammel HD-ring som gikk utenfor metadata: faktisk masterfelt [1024,340,96,76]. Dette er relevant kontekst for senere 017-tilstander, men ingen tillatelse til å arve 01 sin tomme linse, åpne vogndør eller andre 01-felt ukritisk. De aktuelle originalene og fullsceneunionen styrer hvilke tilstander som skal beholdes eller gjenopprettes. C sine `c-objektqa-1.png` til `c-objektqa-3.png` og `c-komposisjonsbevis.json` gir videre produksjonsbevis.
