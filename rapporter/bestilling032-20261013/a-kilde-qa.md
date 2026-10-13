# Kilde-QA og levering, bestilling 32 A

Seks leveranser er produsert med seks innebygde imagegen-kall. Eksakt modellnavn ble ikke eksponert. Originale prompter står ordrett i de bevarte promptfilene, fulgt av separat kildepresisering. Alle seks leveranser gir **OK** med uendret sjekk_leveranse.py. De seks metadatafeltene er i tillegg eksplisitt målt OK med kantkorrelasjon 0,8862 til 0,9722. Dette er teknisk kontroll, ikke runtime eller ny individuell brukergodkjenning.

[Manifest med SHA, råfiler, prompter og referanser](a-leveranser.json), [helscener original/HD](a-samlet-kontaktark.png), [objektfelt 1](a-objektqa-1.png), [objektfelt 2](a-objektqa-2.png), [skilt og kabin](a-027-tekst-kabinqa.png), [kildeplan](a-kildeplan.md), [56 uendrede kildefiler](a-kildehashkontroll.json).

## 027-paret

[Valgt master](a-027-fullmaster.png) er et helt nytegnet panorama på 1888 × 800. Klipp x=0 og x=352 settes på grå canvas ved y=112. [Overlappen på 1184 × 800 er byte-identisk](a-overlappbevis.json). Begge klipp viser riktig del av bilfraværet og den brune trikkabinen, uavhengig av at hver jobbs metadata bare nevner ett objekt.

Første rågenerering ble helskalert til eksakt masterstørrelse. Forsøk på å klippe bare parkerings-/kabinfelt inn i gammel HD-master ga synlige skykanter. Ett lokalt kabinforsøk ble også bevart, men ikke valgt. Den komplette første nygenereringen ble derfor valgt, etter at root uttrykkelig bekreftet helscenealternativet. Ingen mislykket feltkompositt er brukt som genereringsanker.

**Bakgrunnen er ikke byte-identisk utenfor objektunionen.** Hele panoramaet har nye penseldetaljer. Originalens hovedformer, hyssingnøste, takanlegg, trestammer, stier, gjerder, rekkverk, parkering og skilt er sammenholdt i fullscene og nærbilder. WORLD S i kontaktarkets beskrivende etikett er ikke et nytt skilt; selve bildet sier WORLDS, deretter LARGEST BALL OF TWINE. TRAM og begge MUSEUM-tekstene med venstrepekende piler er beholdt. Bokstavkonturene er malte og ikke pixelidentiske. Kabinen har tre synlige hjul, mørk takunderside, tynne stolper og de kildebestemte åpningene. Nye malte trestriper og glasshøylys er detaljering innen eksisterende flater; dette er ikke en motorverifisert dimensjonskontroll.

Teknisk sluttkontroll: del 1 skift 0,03, blokker 0,15, kantlikhet 0,96; del 2 skift 0,02, blokker 0,31, kantlikhet 0,96. Felt 277 korrelasjon 0,972190; 281 korrelasjon 0,965090.

## 027 dørstripe og 028 åpen dør

lag027_02_del2av2 bruker bare det nygenererte rektangelet [1152,272,64,256] over korrekt eksisterende rom027 del 2. Ingen full kabin er føyd til. Rekkverk, himmel og det avskårne tre-/takfeltet følger egen kilde. Fire HD-pikslers rektangulær overgang mellom nytegnet felt og tidligere nytegnet bakgrunn; ingen originalkonturmaske. Felt 283 korrelasjon 0,940711.

lag028_01 bruker rektangelet [192,368,128,352]. Åpningen viser blå himmel, grønn vegetasjon og brun ramme; den tidligere gule døren er borte. Ingen person er lagt til. Museets øvrige glassmonter, benker, plakater og tråder er beholdt fra eksisterende HD. Samme fire pikslers overgang. Felt 284 korrelasjon 0,948895.

## 029 ring og sammensatt redskap

Identiteten følger bestilling 7: grønn golfballhenter, Jesse James' inntørkede hånd og fiskformet rød magnet med to grå poler. Brun rynket form er hånd, ikke hyssing. Øvre avskårne 292 er deler av samme redskap. Ingen ny kropp eller slange er tegnet.

lag029_01 bygger på rom029-HD med den eksisterende obj294-tegningen flyttet fra eget canvas [272,208,992,608] til romcanvas [160,208,992,608]. En tolv HD-pikslers rektangulær kantovergang mellom disse NYTEGNEDE bildene demper de gamle objektkantene. Ringen er nygenerert i [1088,656,192,160] med fire pikslers kantovergang. Den har svart/sølv bånd, skrå blå/grønn/rosa flate og ingen oppdiktet tekst. Nytt høylys og bandmodellering er vurdert mot originalens synlige form. Felt 291 korrelasjon 0,886228.

lag029_02 bevarer begge store overlappende magnet/håndgrupper og de avskårne delene øverst til venstre. Ingen forenkling til én gruppe. Den nye kildekomposisjonen legges i [128,112,1024,704], som tilsvarer rom [0,0,256,176] og dekker både underlaget fra 293/294/295 og 292. Dette er et dokumentert samlet rektangel, større enn jobbens ene metadatafelt; den mislykkede rektangelprøven fra analysen er ikke brukt som anker. Tolv HD-pikslers overgang brukes bare ved indre rektangelgrenser. Ingen ring fra den andre tilstanden er malt inn. Felt 292 korrelasjon 0,941921.

029-variantene er sammenholdt i fullscene og nærfelt. Samme røde magnetidentitet, grønne deler, brune fingre med gule negler, grå poler og diagonal tildekking er bevart. Antallet synlige gjentatte grupper følger kildekompositten; dette hevder ikke at spillet viser hele denne kompositten samtidig i runtime.

## Kontroll og begrensninger

Alle bilder er opake RGB 1536 × 1024 med nøyaktig padding 128. De fire leveransene utenfor panoramaparet er byte-identiske med sine dokumenterte HD-grunnrom utenfor oppgitte sammensettingsrektangler. Ingen originalpiksler, originalmasker, vektortrace eller lokal geometriwarp er brukt som ferdig HD-kunst. Analyseforstørrelsene er bare kildebevis.

Oppskrifter, alle råforsøk, ikke valgt feltkompositt, promptfiler, SHA og faktiske checkerlogger er bevart. Ingen beskyttet kilde, produktkode eller Git er endret. Import, motorvisning og individuell brukergodkjenning gjenstår hos mottaker. Ferdigmarkeringen klar_for_mottak betyr at leveransene er klare for roots samlede kontroll, ikke at disse videre kontrollene er utført.
