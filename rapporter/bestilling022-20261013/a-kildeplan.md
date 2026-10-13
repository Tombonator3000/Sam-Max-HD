# Kildeplan og lagkontrakt for bestilling 22

Kun analyse, 13. oktober 2026. Ingen generering, produktkode, Git, globale logger eller jobbfiler er endret. De ti lagjobbene etter bestilling 21 er identifisert i GRAFIKKLISTE.md. 40 beskyttede filer er låst i kildehash.json. Fire ekstra kilder for lag007_02_del2av2 fra bestilling 23 er låst i ekstra-kildehash.json for sammenhengskontroll, ikke bestilt produksjon.

BESTILLING.md, jobbmetadata, prompter, originaler, ressursregister og relevante romnotater er lest. source-faithful-production-skill og origin/main:docs/skills/scumm-hd-remake/SKILL.md er brukt. C har parallelt kontrollert lag002_01 og bekreftet kontrakten; se bestilling 021-20261013/c-kildeplan.md og c-lag002-rutekart.json.

## Dette er ikke spriteatlas

Lagtypen er et helt ROMBILDE med valgte små objektbilder allerede tegnet på sine opprinnelige romposisjoner. Det er ingen ny rutegrid, ingen felles cellestørrelse og ingen tillatelse til å omplassere objekter for bedre utnyttelse. Lagnummeret er pakkefordeling av tilstander og ikke-overlappende synlige objektområder, ikke dokumentert runtime-rekkefølge.

Kontraktkilder: BESTILLING.md avsnitt «Lagjobber», origin/main:pipeline/smhd/gpt.py plan_layers rundt 525, assign_parts 634, objektimport 1460 og _with_alpha 1532; uendret verktoy/sjekk_leveranse.py check_picture 188 til 221. Linjenumre gjelder den leste versjonen.

- Lever full opak 1536 × 1024 RGB-komposisjon med nøytral padding RGB128.
- Rom 002/003/004 har motivfelt [128,112,1280,800], region [0,0,320,200].
- Rom 007-delene har motivfelt [0,112,1536,800], region henholdsvis [0,0,384,200] og [104,0,384,200].
- Hvert objekts metadata-rekt er [x,y,bredde,høyde] i HELE rommets originalpiksler. HD-boks på leveranselerret er [padding_x+4×(x-region_x), padding_y+4×(y-region_y), 4×bredde, 4×høyde].
- Objektrektanglet kan inneholde både synlig objekt og uendret rombakgrunn. Det er ikke et krav om å fylle hele rektanglet med ny solid figur.
- Alle undersøkte lag har underlag=[]; det kreves ikke et ekstra stort objektbilde som bakgrunn i disse jobbene.
- Svart er en faktisk motivfarge i laboratoriet, hodehull, døråpning og skygger. Ikke fjern svart med chroma-key. Ekte alfa og alfarutekart gjelder figurark, ikke disse lagleveransene.

Den senere importøren klipper objektbilder fra komposisjonene i 4×, bruker match_state for senere tilstander der originalene er like, og _with_alpha legger originalobjektets alfa på importresultatet. Dette er observert pipelinekode og IKKE autorisasjon til å maskere vår nytegning med originalkonturen. Ingen import eller motor er kjørt her.

## Kontrollkrav og forskjell fra faktisk mottak

Uendret checker konverterer lagresultat til RGB og måler hele motivet. Deretter undersøker den hver objektrekt med kantkorrelasjon: OK minst 0,60, SJEKK minst 0,50, FEIL under 0,50. Rektangler under 4 originalpiksler i bredde/høyde og områder med kantstandardavvik under 1,0 hoppes over. Objekter med OK skrives ikke i loggen. Det er derfor feil å si at lag bare får helbildekontroll, men også feil å lese en stille logg som semantisk objektgodkjenning.

Helbildegrenser: OK skift≤0,75, blokk≤1,0, kant≥0,55; SJEKK≤1,5/≤2,0/≥0,40. Ett dårlig objekt kan gi FEIL for hele laget. Den fullstendige importørens synlighetsmasker/bakgrunnssammenligning er mer omfattende enn denne lokale checkerens rektangelkontroll. Ingen egen terskel skal endres.

[a-bokstabell.md](a-bokstabell.md) og [a-formatbevis.json](a-formatbevis.json) inneholder alle 22 bestilte objektbokser og den ene ekstra fra 23, eksakt romrekt/HD-rekt, registerfelt, palettantall og antall piksler som avviker fra grunnrommet. Palettantallet gjelder komposittboksen inklusive bakgrunn, ikke et isolert RGBA-objekt. De tre a-objektbokser-kontaktarkene viser hver faktisk boks.

## Laboratoriet: fire lag, sju konkrete objektbilder

### lag002_02

Fire objekter:

- obj051_01 lab-car: mørk blå/lilla bilfront med fire runde brun/gule lykter, skrå grill, støtfanger, frontrute og konkret silhuett. Plassert [144,96,136,56], ikke gjort større. Den er ikke den identiske bilen i 057.
- obj054_01 lab-rock-2: liten mørk løs stein i gulvfeltet [112,184,40,16]. Bare 37 piksler skiller komposittboksen fra grunnrommet; behold den lille formen og tomrommet rundt.
- obj992_01 lab-light-1: grønt opplyst hodeskalleparti og lysende lime kule/lyspære i forgrunnen [168,152,72,48]. Originalen har konkret grønn lyssetting og skalle, ikke en ny person eller dekorativ gnist.
- obj897_02 lab-light-3 tilstand 02: taggete lime/gulgrønn lyskrans rundt den blå/hvite apparatkula [104,40,56,48]. Ikke kopier den rundere kransen fra grunnrommet eller fra tilstand 01 i bestilling 21.

### lag002_03

obj052_02 car-windshield, [176,104,64,16]. Bare et lavt mørkt bilrute-/takstykke i det blå veggfeltet, med sine lysstreker. Det ser svevende ut i komposisjonen fordi resten av bilen er egne objekter. Ikke tegn bilfront, hjul eller et nytt hull under det. Sammenlign mot 052_01 i bestilling 21 ved produksjon, ikke anta duplikat.

### lag002_04

obj056_01 car-door, [240,96,56,56]. Konkret avklipt åpen bildør-/bilsidekomponent med brun/gul stjerne på blå/lilla dørflate, lys blå kant og oransje/rosa lysfelt bak. Den står alene over laboratorieveggen og er delvis skjult av panelstenger i komposisjonen. Ikke fullfør bilen eller erstatte stjernen med lesbar polititekst.

### lag002_05

obj057_01 lab-car-2 har samme metadatarekt som 051, men er en annen konkret biltegning/tilstand. Målt 2615 av 7616 komposittpiksler er forskjellige innen boksen; konturer/lys/grilldetaljer er ikke en trygg duplikat. Begge skal sammenlignes ved siden av hverandre. Øvrige lys og gulv følger dette lagets original, ikke automatisk lag002_02.

Alle fire bakgrunner må følge levert rom002 i detaljnivå, men beholde de faktiske objektene/tilstandene fra hver lagreferanse. Den blå steinveggen, maskiner, kabler, plattform og panel skal ikke flyttes. Små lysforskjeller må ikke bli borte ved blind kopiering av HD-rommet.

## Nærbildene: hoder og bevisst tomme felt

lag003_01: obj058_01 scientist-head, [96,24,104,104]. Gul/oransje forskerhode med oransje hårkrøll, stor asymmetrisk brille/øyeparti, lang nese, hake og ører, over den eksisterende gulgrønne frakken. Grunnrom 003 er bevisst uten hodet. Nytegningen skal gi hodet riktig feste mot kragen, ikke legge til en ny kropp eller forsker i en annen pose.

lag004_01: obj059_01 max-ears [56,8,120,104] og obj061_01 sam-head [176,48,80,56]. Produksjonskontrollen av selve kildekomposisjonen presiserer at FIRE lange hvite/rosa ørefliker er synlige, som to overlappende par. Den tidligere formuleringen «to ører» var for generell og skal ikke normalisere lagbildet anatomisk. Alle fire synlige fliker og øvre hodefelt følger denne varianten; Sam får sitt brune hundehode med svart nese under eksisterende hatt og over blågrå dress. Godkjente Sam/Max-hovedark kan styre identitet, men akkurat denne posen og kildepaletten har prioritet.

lag004_02: obj060_01 max-non-ears [40,8,120,104]. Ører er fjernet/erstattet med veggbakgrunn over Max' hode. Sam-hodet er samtidig fortsatt fraværende i komposisjonen, akkurat som i grunnrom 004. Ikke «reparer» den hodeløse Sam, ikke legg på Sam-hodet fra lag 01 og ikke sett Max-ører tilbake. Figurenes kropp, ansiktsrester og vegg er tilsiktede komponenter, ikke en anatomisk feil å fullføre.

## Kontoret: felles lagkomposisjoner og to forskjellige tilstandssett

lag007_01 og lag007_02 har hver samme romstørrelse 488 × 200. Regionene starter x0/x104. Overlapp 280 × 200 originalpiksler har målt NULL avvik for begge lag, selv om metadata lister ulike objekter i delene. Dette skyldes assign_parts: objektene tegnes i samlet romlag, og metadata velger hvilken del importøren skal klippe hver ressurs fra. Et objekt som er helt inne i flere deler tildeles normalt én av dem.

Dermed kan én master 1952 × 800 brukes PER LAG, klipp x0 og x416 med overlapp 1120 × 800. Dette er målt, ikke antatt ut fra vanlige romregler. Ikke bland lag 01 og 02 i én master. a-overlappsbevis.json dokumenterer nullavvikene. Ekstra lag007_02_del2av2 i neste bestilling er nødvendig kontekst for full lag 02-master og er derfor låst med fire filer; produksjon av denne ekstra jobben må avtales av root, ikke utledes av analysen.

### lag007_01_del1av2

Eier uttrekk av obj062_01 door [16,56,40,80]. Kilden viser ÅPEN mørk dør med synlig mørkt rom/gelender bak, ikke rom-HD-ankerets lukkede SAM/MAX-dørblad. Ikke behold bokstavskiltet fra lukkede døren. TV-bilde og øvrige lag 01-objekter er også synlige i romkomposisjonen der de faller innenfor utsnittet, selv om de klippes fra del 2.

### lag007_01_del2av2

Sju objekter:

- obj063_01 office black light [400,112,16,16]: konkret grå/mørk bryter-/lysflate over LOVE-plakaten, der grunnrommet har en lilla rund lyskilde. Det er ingen begrunnelse for å tegne en ny lommelykt ut fra navnet.
- obj065_01 roach food [320,136,24,24]: matrest-/gulvfeltet foran boksen er endret fra grunnrommet. Den konkrete komposittboksen er hovedsakelig brunt gulv og sparsomme grønne/brune rester. Ikke legg til en hel sandwich eller kakerlakk som navnet alene foreslår.
- obj071_01 office-tv [144,88,24,24]: TV-skjerm med grønn bakgrunn og små hudfargede/rødbrune figurer. Bevar de konkrete ansikts-/figurformene; ikke erstatt med generisk film, logo eller statisk støy.
- obj074_01 office-eyes-1 [408,32,16,16]: øyefelt i den rosa figuren på hyllen. Bare FIRE komposittpiksler avviker fra grunnrommet, resten av boksen er samme hode. Hold de faktiske øyefargene/formene, ikke ny figur eller flytting.
- obj077_01 office-dart-board [176,48,48,40]: dartskive UTEN de tre prosjektilene som finnes i grunnrommet. Ikke kopier pilene fra godkjent romanker.
- obj079_01 office-desk-papers [192,104,32,16]: lyse papirer på høyre skrivebordsflate. Hold antall/silhuett/rot.
- obj080_01 office-window [240,48,24,56]: konkret smal vindusvariant med ramme/glass og blå åpning, ikke grunnrommets standardvindu. Bevar åpningsretning og tverrstreker slik bildet viser.

### lag007_02_del1av2

Tre objekter: obj064_01 office phone [0,112,40,24] viser telefonens GRÅ base uten den røde hånddelen som ellers ligger over; ikke fyll telefonrøret tilbake. Obj 071_02 er en ny TV-tilstand, bare TRE komposittpiksler forskjellig fra 071_01 i samme 24 × 24-boks. Obj 080_02 har en tydelig større ubrutt blå vindusåpning og endret ramme;365 piksler avviker fra 080_01 innen 24 × 56-boksen. De konkrete få pikselforskjellene i TV/øyne er tilstandsbevis, men skal nytegnes, ikke kopieres som oppskalert original.

I lag 02 er døren lukket igjen, pilene tilbake i dartskiven og andre objekter følger lag 02-originalen. Ikke ta bort alt som laget ikke eier i metadata; full komposisjon er fasit.

Ekstra del 2 eier obj075_01 office-eyes-2 [416,48,16,8], i øyefeltet på den grå/hvite skallen på hyllen. Bare TRE komposittpiksler avviker fra grunnrommet. Denne ressursen er ikke samme ansikt som 074. Del 2 viser også samme TV/vindutilstand som del 1 i den identiske overlappen.

## Matching mot levert HD og begrensninger

a-rommatching-kontaktark.png viser original og nåværende HD for rom002/003/004 og begge rom007-delene. a-rommatching-hash.json låser disse referansehashene på analysetidspunktet. Bilder er levert i tidligere bestillinger; dette er ikke en påstand om ny individuell godkjenning av alle rom. Bruk metadatafeltet bilde_to til riktig romdel. Stilen i disse rommene kan gjenbrukes, men de endrede objektene skal følge lagoriginalen.

Kritiske avvik fra romankerne: laboratoriebil/stein/lys mangler i 002, forskerhode mangler i 003, Sam-hode mangler i 004, kontordør/vinduer/TV/telefon/piler/matrester/lys/øyne har egne tilstander. Bakgrunnsgjenbruk må aldri overskrive disse tilstandene.

Usikkerhet: små TV-figurers konkrete fortelling, øyeblikk/timing og navngitt funksjon til alle kontorrekvisitter er ikke bevist av registeret alene. Bevar synlig kildeform/palett fremfor å dikte ny tekst eller identitet. Kildenes fullkomposisjoner er RGB-bilder; separate originalobjekters alfamasker er ikke hentet eller brukt til ny grafikk. Runtime, import og motorkomposisjon er ikke utført.

Leveringsbevis bør senere omfatte uendret checker, alle objektnærbilder, sammenligning mot riktig HD-rom og tilstandspar, nøytral padding, resultathash/råforsøk/prompt/oppskrift og faktisk runtime=false. Originalmaskering og lokal geometriwarp er ikke en tillatt snarvei.

## Analysefiler

- original-kontaktark.png: alle ti bestilte lag.
- a-objektbokser-1.png til -3.png: hver objektboks inklusive ekstra 075.
- a-bokstabell.md / a-formatbevis.json: eksakte bokser og målinger.
- a-overlappsbevis.json: begge lag007-overlapper.
- a-variantbevis.json: bil-, TV- og vindusforskjeller.
- a-rommatching-kontaktark.png / a-rommatching-hash.json: allerede leverte romankere.
- kildehash.json og ekstra-kildehash.json:40 + 4 beskyttede kildebytes.
