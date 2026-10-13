# Bestilling 26 A: kilde- og leveransekontroll

Sju opake RGB-kompositter er produsert med innebygd imagegen i åtte faktiske genereringskall. Eksakt bildemodell er ikke eksponert. Alle sju har OK i uendret `verktoy/sjekk_leveranse.py`, og alle elleve metadatafelt er eksplisitt kontrollert med korrelasjon mellom 0,881 og 0,982. Dette er teknisk kontroll og egen visuell QA, ikke import, runtime eller ny individuell brukergodkjenning.

## Kilder og metode

[a-kildeplan.md](a-kildeplan.md), [a-feltbevis.json](a-feltbevis.json) og [a-sammenhengsbevis.json](a-sammenhengsbevis.json) dokumenterer originaler, register, paletter, objektbokser og faktisk grunnromslikhet. Alle 40 beskyttede jobbkilder og fire ekstra kontekstfiler fra neste kaktustilstand er fortsatt byte-uendret: [a-kildehashkontroll.json](a-kildehashkontroll.json). Kaktusen er bare analysekontekst i denne leveransen.

Hver generering bevarer den ordrette jobbpompten, etterfulgt av separat kildepresisering. Fullmasterens prompt inneholder begge ordrette delprompter. Genererte bilder, promptfiler, referanser og hash står i [a-leveranser.json](a-leveranser.json). Produksjonsrekkefølgen er `a-forbered-produksjon.py.txt`, `a-sammensetting.py.txt`, `a-feltretting.py.txt`, `a-felt126-fullkontekst.py.txt`, `a-kontroll.py.txt` og `a-manifest.py.txt`. Rapportoppskriftene endrer ikke motor eller produktpipeline.

Nye felt er klippet rektangulært og plassert på det allerede leverte HD-rommet. Der angitt er det en fire HD-pikslers rektangulær kantovergang mellom NYTEGNET felt og NYTEGNET grunnrom. Ingen originalpikselkopi, originalkonturmaske, vektortrace eller lokal geometriwarp er brukt. Råmasteren på 1942 x 809 er helskalert til 1920 x 800. Alle leveranser er 1536 x 1024 med motiv [0,112,1536,800] og eksakt padding RGB 128.

## Faktiske tilstander og rettinger

Innvendig 011_01 har sin egen dørstilling, grønn iskule med oransje kjeks og fravær av det åpne varebrettet. Første generering tolket den lange oransje esken som to like kuber. Et nytt lokalt forsøk bevarte eskeformen, men passet dårlig med den tilgrensende HD-geometrien. Tredje forsøk i full romkontekst beholdt lang eske og liten fremre eske. Det er valgt for 126-feltet; første forsøk brukes fortsatt for dør og glass. Alle tre råforsøk er bevart.

Ren klipp ved metadataens x=736 ga knekk i en eske som fortsetter til omtrent x=759 i HD-rommet. Valgt sammensetting bruker derfor [600,456,192,116], en litt større rektangulær kontekst som også bevarer eskens fortsettelse og blå hylle. Dette er dokumentert avvik fra streng byteidentitet utenfor 126-boksen, ikke påstått metadataendring. [a-obj126_01-valgt-naer.png](a-obj126_01-valgt-naer.png) viser den sammenhengende hyllen uten brett og uten tidligere klippegrense.

Innvendig 011_02 har diagonal oransje ispinne i glasset og øvrig grunnrom beholdt. De to innvendige jobbene er forskjellige tilstander, ikke ett panoramapar.

Utvendig 012_01 bruker én [fullmaster](a-lag012_01-fullmaster.png), klipp x=0 og x=384 og målt byte-identisk overlapp 1152 x 800. Masteren inneholder svart/blå bil, hvitt tak og dør, gul stjerne, fire gule frontlykter, åpen blå dør, grønn iskule i glassfeltet og tomt koppfelt. Alle synlige objekter følger med i begge deler uavhengig av lokal metadataeier. Bilen ligger ved venstre scenekant; generatorens aller ytterste halefinne er noen HD-piksler innenfor kanten, ikke påstått kildepikselidentisk avklipping. Dette er oppgitt for roots visuelle mottak.

Koppfeltets svake tonegrense ble rettet med et jevnt additivt RGB-felt beregnet fra NYTEGNET felt og NYTEGNET grunnrom langs rektangelkanten. Ingen gammel kopp blandes tilbake. Førmaster og fargefelt er bevart i `a-lag012_01-master-foer-feltretting.png`, `a-obj135_01-fargefelt.npy` og `a-feltretting-bevis.json`.

Utvendig 012_02 har oransje ispinne, men beholder grunnrommets kopp og lukkede dør. Den skal ikke få biltilstandens øvrige endringer.

Statue 133_01 har kildeegne brune segmenter, stor krummet fremre form, buet øvre form, tynne vedheng og gul stråhatt. Kildeplanens og promptens ord «skorpion» var en visuell formtolkning, ikke sikkert artsbevis. Formen kan også leses som et stilisert krepsdyr; tegningen er vurdert mot de faktiske kildeformene, ikke et påstått artsnavn. Statue 133_02 er den egne brune gevir-/hareliknende dekorfiguren med lange ører, lyst magefelt og store føtter. Det er ikke en animasjon av samme figur.

De to statuene følger originalens røde/oransje klipper. Den høye grønne vegetasjonen i grunnrommet er feil underlag her. [a-statue-felles-underlag.png](a-statue-felles-underlag.png) inneholder 133_01 og er felles bakgrunnsgrunnlag for 133_02; de to ferdige filene er byte-identiske utenfor 133-rektangelet. Filen er også gitt til C som konsistensgrunnlag for neste kaktusvariant, med SHA 99862986164f546199b6d27bef06e96d61e1cc3dabc0b1c8f09849556416cf01. Det betyr ikke ny bruker- eller runtime-godkjenning.

## Visuell kontroll og begrensninger

[Samlet original/HD](a-samlet-kontaktark.png), [feltkontroll 1](a-feltqa-1.png), [feltkontroll 2](a-feltqa-2.png), [perobjektmål](a-perobjektkontroll.json) og [geometri/kildekontroll](a-geometri-kildekontroll.json) er oppdatert etter siste retting. Jeg har sett alle fullscener, objektfelt og panoramamasteren. Kontrollen omfatter dørene, fravær av brett/kopp, forskjellige glassmotiver, bilens fire lykter og gul stjerne, dekorfigurenes forskjellige former og de røde klippene. Skilt og øvrig romtekst er beholdt fra rom-HD der grunnlaget gjenbrukes.

Små penselstreker, glassrutenes skygger og antialiasering er nytegnet og ikke identiske med originalpiksler. Artsnavn for 133_01, geografisk/motorstyrt betydning av klippevarianten og faktisk runtime-rekkefølge er ikke bevist. Root håndterer samlet visuell mottakskontroll, videre import og Git-levering.
