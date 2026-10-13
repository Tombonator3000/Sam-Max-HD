# Bestilling 14 C – samlet kilde-QA

Fire originalpaneler er undersøkt samlet før tegning, sammen med hovedark for Sam og Max. Originalenes sterke røde/grønne/lilla/brune farger og særskilte beskjæringer styrer. Identitetsanker skal ikke normalisere paletten. Obj601-tekst er kontrollert i eget nærbilde; småtelefonlinjen er tolket ut fra synlige glyfer og ikke bekreftet av runtime. Obj603-diagonalen er ikke gjort til et nytt ord.

**obj600_01:** Max til venstre og Sam til høyre med lange utstrakte armer. Rød/brun/purpur/grønn panelpalett er beholdt; den lille lyse ansiktsformen bak Sam er ikke gitt et nytt navn. Kildens positur, avkutting og overlapp er sammenlignet. Teknisk SJEKK: skift 0.88, blokk 1.19, kantlikhet 0.73.

**obj601_01:** Stor pistolform med Sam til høyre. HOW'S MY AIM? er nær lest; mindre linje er gjengitt som CALL 1-800-SAMNMAX etter synlige glyfer, men den lavoppløste småteksten har fortsatt tolkningsusikkerhet. Originalens grønne/turkise snute er gjeninnført med et lokalt imagegen-utsnitt, ikke vanlig blå/svart hundenese. Teknisk OK: skift 0.11, blokk 0.14, kantlikhet 0.90.

**obj602_01:** Uvanlig mekanisk scene med to mørke runde åpninger, røykbue, hjul og Sam/Max. Første forsøk avvist fordi Sam fikk vanlige blå klær og Max åpent smil. Andre forsøk gjenoppretter lilla klær og lukket Max-munn. Originalens komposisjon er beholdt, ingen vanlig bil er satt inn. Teknisk SJEKK: skift 0.85, blokk 0.99, kantlikhet 0.75.

**obj603_01:** Sam og Max med store hender og diagonal mønstret instrumentlignende detalj; ingen ord er skrevet på diagonalen. Første forsøk avvist for feil munnuttrykk. Andre forsøk beholder lukket Max-munn og åpen Sam-munn. Tredje forsøk korrigerte ikke snutefargen og er ikke brukt. Fjerde er lokal grønn snutekorreksjon. Max-munnens tidligere glatte frown er korrigert i lokalt forsøk 5, se tillegg nedenfor. Teknisk SJEKK: skift 0.12, blokk 1.54, kantlikhet 0.77.

Alle fire resultater er satt i kontraktens motivrektangel med eksakt RGB 128 utenfor. Hele tegnede motivflater er skalert/plassert uten lokal warp; topp-/bunnstripe er kildekonstant svart. Lokale korrigeringer er imagegen, ikke originalmasker. 601 bruker rektangel [1155,521,112,59] fra forsøk 2. 603 bruker [496,410,128,56] fra forstørret lokalforsøk 4 med 3 pikslers rett kantblending; resten er byte-uendret.

Ingen FEIL gjenstår, men tre SJEKK er ikke kalt OK. Samlet original/HD-kontaktark er c-samlet-qa.png. Råforsøk 602-1, 603-1 og 603-3 er avviste og bevart. Alle 44 beskyttede kilder er hashkontrollert uendret. Runtime og ny individuell brukergodkjenning er uverifisert.


## Lokal Max-korreksjon, forsøk 5

Originalnærbildet obj603_01-maxansikt-referanse.png er grunnlaget. Faktiske markeringer er lilla/purpur og oransje/røde på mørk brun ansiktsflate, ikke grønne. Ingen nye grønne øyne er innført. Imagegen restaurerte kildeknekk og falskfargede øye-/nesemerker. Utsnitt [952,456,216,104] med 3 pikslers rektangulær kantblending. Resten er kontrollert byte-identisk mot obj603_01-for-maxkorreksjon.png. Ingen silhuettmaske eller warp. Ny kontroll SJEKK: 0.12/1.54/0.77.
