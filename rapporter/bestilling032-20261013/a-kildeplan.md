# Kildeplan, bestilling 32

Kun analyse. Ingen bilder er generert, ingen jobbfiler er endret, og ingen runtime eller ny individuell godkjenning påstås. Alle ti originaler, deres metadata og tolv objektfelt er sammenholdt med relevante originalrom, tidligere HD-bakgrunner og registerets ressursnavn. Førti beskyttede jobbkilder og seksten ekstra kontekstfiler er låst; [sluttkontrollen](a-kildehashkontroll.json) bekrefter alle 56 uendret.

## Bevis og format

[Originalkontaktark](original-kontaktark.png), [objektfelt 1](a-objektfelt-1.png), [objektfelt 2](a-objektfelt-2.png), [grunnrom mot lag](a-grunnromsfelt.png), [metadata og differanser](a-lagbevis.json), [felt, bokser og paletter](a-feltbevis.json), [familiebevis](a-familiebevis.json) og [ankrenes SHA](a-ankerhash.json). Analyseoppskriftene er bevart som a-analyse.py.txt, a-familieanalyse.py.txt og a-avklaringsbevis.py.txt.

Leveranser skal være opake RGB-kompositter på 1536 × 1024 med padding RGB 128. Rom 027 og 030 bruker bildeområdet [0,112,1536,800]. Rom 028 og 029 bruker [128,112,1280,800]. Bokser nedenfor er [x,y,bredde,høyde]; kildebokser bruker romkoordinater. Hvert metadatafelt må kontrolleres, også når checker ikke skriver sine beståtte felt. Ingen originalmasker eller originalpiksler skal brukes som ferdig HD-kunst.

## Rom 027: bilfravær, trikkabin og egen dørstripe

| Jobb | Objekt og faktisk tilstand | Kildeboks | HD-boks i leveransen |
| --- | --- | --- | --- |
| lag027_01_del1av2 | 277_01: bilen er borte; grå parkering med hvite linjer og egne mørke flekker | [0,136,104,48] | [0,656,416,192] |
| lag027_01_del2av2 | 281_01: brun/oransje trikkabin, mørkt tak, blå/svarte vinduer, tynne stolper og forbindelse til kabelen | [304,24,120,96] | [864,208,480,384] |
| lag027_02_del2av2 | 283_01: smal utskåret dør-/kabinstripe; resten av stasjonen følger grunnrommet uten hel kabin | [376,40,16,64] | [1152,272,64,256] |

01-paret krever én master på **1888 × 800**, klipp x=0 og x=352, og byte-identisk overlapp på **1184 × 800**. Originalrommet er 472 × 200, ikke 480 × 200. Originaloverlappens RGB-bytes er identiske. [Sammensatt originalmaster](a-027-master-kilde.png) er bare analyseforstørrelse.

De to delene viser begge endringer i overlappen, selv om metadata bare lister ett objekt per del. Del 1 har 3350 endrede kildepiksler utenfor sin bilboks fra kabinen; del 2 har 205 utenfor kabinboksen fra bilfraværet. Hele masteren har 6685 endringer og null utenfor samlet 277/281-union. Et separat grunnrom pluss bare hver dels egen boks vil derfor være feil.

02 er ikke neste komplette kabinbilde: 501 endrede piksler, null utenfor den smale 283-boksen. Behold kildens avkutting og ikke fullfør kabinen rundt stripen. TRAM-skiltet og dets retning skal beholdes. Kildepalettene i feltene har henholdsvis 65, 104 og 66 RGB-farger. Tallene er beskrivelse av pixelkilden, ikke krav om palettkvantisering av ny HD.

## Rom 028: åpen museumsdør

lag028_01, obj284_01: [16,64,32,88] blir [192,368,128,352]. Gul lukket dør erstattes av åpen passasje med blå himmel, grønn vegetasjon og brun ramme. Ingen person skal tilføyes. 1461 kildepiksler endres, null utenfor boksen; feltet har 93 farger. Resten av levert rom028-HD er riktig basis, inklusive glass, utstillinger og tekst.

## Rom 029: humørring og sammensatt redskap

[Merket sammenligning A til F](a-029-avklaring-A-F.png) viser det avskårne feltet og hele konteksten. Bestilling 7 sin [kilde-QA](../bestilling007-20261013/a-kilde-qa.md) identifiserer grønn golfballhenter, Jesse James' inntørkede hånd og rød fiskformet magnet med to grå poler. Hintbokens trykte side 43 ble dokumentert gjennom søkbart tekstutdrag, ikke runtime. Brune rynkede flater er hånd/fingre, ikke hyssing.

**A, obj292_01:** [0,0,80,56], HD [128,112,320,224], 60 farger. Sammenlignet med B til D er dette et avskåret felt av samme redskap: to grå magnetpoler, liten rød del, grønt leddverk og brun hånd med gule detaljer. Det skal ikke tegnes som en slange ut fra registerets navn snake-m-1, eller fullføres til en hel figur. Visuell identitet er nå tilstrekkelig støttet av flere visninger; det tidligere generelle identitetsspørsmålet om A er dermed snevret inn til komposisjonen omtalt nedenfor.

lag029_01 har obj291_01, humørring med svart/sølv bånd og blå, grønn og rosa flate: [240,136,48,40], HD [1088,656,192,160], 69 farger. Ingen lesbare bokstaver skal legges til.

**Viktig basisavvik:** bilde_to er obj294_01/resultat.png, ikke rom029. Dets kilde er 248 × 152 ved rom [8,24,248,152]. HD-motivet må tas fra objektcanvas [272,208,992,608] og plasseres i romcanvas [160,208,992,608]. Hele objektcanvas kan ikke brukes som rombakgrunn. På kilden er rom029 pluss dette rektangelet identisk med lag029_01 utenfor ringboksen: alle 682 forskjeller ligger inni ringboksen.

**F, lag029_02:** metadata oppgir underlag 295, 294 og 293. Kilden viser faktisk flere overlappende hånd/magnetdeler, inklusive A øverst. Mot rom029 med 294-rektangelet er det 6668 forskjeller, hvorav **5432 utenfor 292-boksen**, i bbox [38,22,241,164]. Det holder ikke å nytegne A og ellers gjenbruke samme basis som lag029_01.

Alle seks rekkefølger av vanlige opake rektangelinnliminger av 293/294/295 er målt. Ingen gjenskaper kilden: beste kombinasjon har 1819 feil utenfor 292. [Rekonstruksjonsbildet](a-029-underlag-rekonstruert.png) er derfor en **mislykket diagnostisk prøve**, ikke en korrekt produksjonsbasis. Maskert original eksport eller annen sammensetting er en mulig forklaring, ikke påvist motoratferd.

Før produksjon må den fullstendige kildekomposisjonen F følges. Et nytt sammenhengende underlagsmotiv basert på hele F er mer forsvarlig enn blind innliming av tre gamle HD-rektangler. Ingen originalsilhuettmaske er autorisert. Dersom root ønsker å forenkle F til bare én magnet/hånd, må det først avklares; kilden gir ikke grunnlag for en slik forenkling. Et mulig konkret spørsmål ved fortsatt tvil er: «Skal de flere overlappende redskapsdelene i F beholdes akkurat som kildearket viser?» Identiteten til selve redskapet trenger ikke spørres på nytt.

## Rom 030: utsiktskikkert, ledninger og fire gnisttilstander

| Jobb | Felt | Kildeboks | HD-boks |
| --- | --- | --- | --- |
| lag030_01_del1av2 | 297_01, svart/grå utsiktskikkert med oransje kant rundt skråstilt åpning | [56,88,40,40] | [224,464,160,160] |
| lag030_01_del1av2 | 301_01, egen liten blå/hvit gnist | [112,136,40,32] | [448,656,160,128] |
| lag030_02_del1av2 | 300_01, lyse ledninger fra kikkertområdet ned mot midten | [64,104,88,64] | [256,528,352,256] |
| lag030_02_del1av2 | 301_02, egen gnist/ledning-komposisjon | [112,136,40,32] | [448,656,160,128] |
| lag030_03_del1av2 | 301_03, annen liten blå/hvit gnist | [112,136,40,32] | [448,656,160,128] |
| lag030_04_del1av2 | 301_04, egen svært liten gnist | [112,136,40,32] | [448,656,160,128] |

300 og 301_02 overlapper hele 301-boksen. De må tegnes som én sammenhengende komposisjon, ikke to konkurrerende rektangler. 301-registerets rotating-sparks støttes visuelt av de hvite/blå gnistene ved kikkertledningen. Ingen bestemt animasjonsrekkefølge eller elektrisk motorfunksjon er runtime-verifisert.

Samlede endringer mot originalrommet er henholdsvis 166, 813, 29 og 9 piksler; null utenfor hver samlet objektunion. 301_01 mot 03 skiller 41 piksler, 01 mot 04 skiller 21, og 03 mot 04 skiller 35. Sammenligninger mot 02 inneholder også ledningsforskjeller og må ikke kalles rene gnistanimasjoner. Alle fire er egne tilstander, ikke duplikater eller generisk støy. Feltpaletter er 80 farger for 297, 129 for 300, og 59/82/59/59 for 301-variantene.

Bruk levert rom030 del 1 som sammenhengende basis. Behold SEAFOOD/FRESH FISH, garn, røde seter, glass/metallapparat og de opprinnelig blå vindusfeltene. Ikke legg nytt landskap eller figurer i vinduene. Ingen hel panoramamaster trengs for disse fire lokale del 1-tilstandene, men deres avkutting ved delgrensen må beholdes.

## Neste steg og begrensninger

Root skal lese planen før generering. Originalnærbildene og de navngitte sammenligningene dokumenterer motiv og tilstand; de beviser ikke spillets timing, interaksjon eller dynamiske maskering. En teknisk bestått checker vil ikke alene godkjenne komposisjonen. Etter eventuell produksjon må alle tolv felt og hele scenene kontrolleres samlet, særlig 027-overlappen, 029-underlaget og 030s overlappende ledning/gnist.
