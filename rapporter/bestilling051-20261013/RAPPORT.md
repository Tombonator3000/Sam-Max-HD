# Bestilling 51: fem lag og fem ikonark

Ti jobber er mottatt: åtte OK og to SJEKK. Fem 091-lag har 31 egne felt. Ikon01–05 har 39 felt, hvorav tre er beviselig tomme. Alle 67 ikke-tomme felt er målt OK; de tre tomme original- og HD-feltene er helt magenta. Ikon06 tilhører bestilling 52 og mottas separat.

## Lagene

Root har sett alle fem helscener og fire feltsider. De grålilla fraværsformene, beholdte antrekksdeler og to røde pilretninger følger hver sin kilde. Små svarte/fargede kantsømmer ved 871/866/858 er rettet fra nytegnet materiale. Ingen originale silhuettmasker er brukt til produksjon.

091_01 og 091_02 kommer fra hver sin 2656 × 800 fullmaster. Klippene ligger ved x=0/1120; begge 416 × 800 overlapper er byte-identiske. Feltunionen fra begge metadatautvalg er brukt i kontrollen. Alt utenfor faktisk feltunion er uendret.

091_03 trenger 850-underlaget: klipp [528,240,480,544] fra tidligere levert obj850_01 legges ved [352,368] på rom091 del 1. Nytegnet grålilla i dette kopierte underlaget var mørkere enn det nye 847-feltet og ble fargetilpasset etter farge/sammenheng i det NYE bildet. Tre naborektangler med sag/smoking er tilbakeført fra det NYE HD-grunnrommet fordi disse kildepikslene er identiske mellom originalgrunnrom og originallag. Selve obj850_01 er uendret. Førkopier, tonebevis, nabobevis og oppskrift er bevart. Root har uavhengig kontrollert at all behandling ligger innen underlagsfeltet og at naborektanglene er kildeuendrede og byte-identiske med HD-grunnrommet. Kontroll utenfor egen847-union er null mot dette dokumenterte faktiske underlaget.

## Ikonene

Root har sett samtlige felt i ikon01–05, alle helsider for 03–05, samt alle felt og helsiden for ikon06 som fortsatt venter eget mottak. Logo, tre egne DeSoto-vinkler og dinosaurens avskårne snute/kjeve er bevart. Det isolerte dinosaurforsøket fjernet oppdiktede øyne og tenner. Veiskiltene har lesbar kildebestemt tekst, tall og pilretning. «Placeholder Name Joke» er bevart ordrett. Ingen bred ny skiltinnramming er beholdt.

Root fant hvit i stedet for lysegrønn bunnstripe på 680. Dette er rettet; 380 nye piksler er endret, topp/pil og alt utenfor feltet er urørt. Før/etter og bevis ligger i rapporten. Ikon02/03 sine tre tomme ruter er ikke fylt med nye motiver.

Skog-/sletteutsnitt er selvstendige ruter. Stubbens perspektiv, regnsky, rutemønstrede trær, brennende dekkhaug og hvite ringgrupper over elvedalen er kontrollert. HD-utgavene har mettet himmel, tydeligere nåler, lys/skygge og tolket smågrafikk; eksakt antall nåler, årringer og røyklinjer er ikke sertifisert.

Ikon01 beholder SJEKK med blokkavvik 1,42 originalpiksel; ikon02 beholder SJEKK 1,65. Avvikene ommerkes ikke til OK. De øvrige arkene er teknisk OK. Ikonleveranser er opake RGB-ark med grå128-padding og magenta arkbakgrunn. Dette følger ikonimportkontrakten; figurarkenes RGBA-kontrakt er en annen.

## Verifikasjon og grenser

20 lagkildefiler, 12 ekstra kildefiler, alle 36 kildefiler for de ni ikonarkene og deres kontekst/HD-ankre er verifisert uendret. Det registrerte importkodeobjektet er SHA-verifisert fra sin faste Git-revisjon. De fem ikonleveransenes råbilder/prompter/referanser og oppskrifter er hashkontrollert. Ingen motor- eller pipelinekode er endret.

Uendret sjekk_leveranse.py er kjørt på alle ti faktiske PNG-filer. Fast format 1536 × 1024, plassering, RGB128-padding, feltresultater, panoramaoverlapper og tomme ikonfelt er kontrollert. Astra utfører produksjonsarbeidet; den innebygde ChatGPT-bildegeneratorens eksakte modellnavn er ikke eksponert. Toms eksisterende stilgodkjenning er videreført. Ingen ny individuell bildeaksept, motorimport eller runtime-test er hevdet. SHA-256 for de tidligere leveransene 47–50 er også bekreftet fra GitHub og lagret her.
