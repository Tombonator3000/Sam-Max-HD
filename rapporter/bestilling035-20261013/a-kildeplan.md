# Kildeplan for bestilling 35

Kun analyse, ingen generering eller jobbfiler endret. Alle ti helscener og 23 metadatafelt er sett mot grunnrom, register og egne varianter. Tre tidligere HD-rom er sett for sammenheng. Førti beskyttede bestillingsfiler, tolv grunnromsfiler og 28 filer fra neste bestillings syv periskop-/fisketilstander er låst. [Sluttkontroll](a-kildehashkontroll.json) viser alle 80 uendret.

[Originalkontaktark](original-kontaktark.png), [felt 1](a-objektfelt-1.png), [felt 2](a-objektfelt-2.png), [felt 3](a-objektfelt-3.png), [full metadata/differanse](a-lagbevis.json), [alle eksakte bokser/paletter/endringstall](a-felttabell.md), [familiebevis](a-familiebevis.json), [mikroendringer](a-mikroendringer.json), [anker-SHA](a-ankerhash.json).

Grunnrom mot lag: [ark 1](a-grunnromsfelt-1.png), [ark 2](a-grunnromsfelt-2.png), [ark 3](a-grunnromsfelt-3.png), [ark 4](a-grunnromsfelt-4.png). [Senere kildekontekst](a-037-nabokontekst.png) avklarer at den lille formen i den lilla dammen er begynnelsen på det samme grå periskopet, ikke en ny fot eller figur. Disse senere jobbene er bare kontekst, ikke autorisert produksjon gjennom denne planen.

## Felles kontrakt

Alle ti skal være opake RGB 1536 × 1024 med motiv [0,112,1536,800] og padding 128. Originalrommene er 480 × 200. Del 1 er rom x=0..384; del 2 er x=96..480. HD-koordinat er x=(romx-regionx)×4, y=112+romy×4. Registeret støtter identitet, men konkrete originale former og tilstander går foran generiske navn. Ingen originalkonturmasker, kildepiksler som ferdig HD, lokal warp eller vektorunntak. Uendret checker må suppleres med eksplisitt kontroll av alle 23 felt og de svært små endringene.

## Seks uthustilstander i rom 036

lag036_01 til 06 del 2 bruker obj334_01 til 06, kildeboks [256,8,56,56], leveranse [640,144,224,224]. Den flytende, skjeve lille uthusformen ligger over trærne. Gullgul/oransje front og kant, mørk fiolett side og sokkel, mørkt tak og en svart/svartbrun åpning følger kilden. I 01 er fronten mørk/åpen med den smale skrå dørflaten synlig; de øvrige viser en brun lukket dør med mørkt lite hull øverst og egne små forskyvninger av hele uthusformen. Ikke rett opp huset, legg til bakken, person, ben eller et moderne skilt.

Originalen har 51 feltfarger i 01 og 50 i de øvrige. Hele endringen ligger i egen metadatarektangel: 1442, 1439, 1436, 1440, 1436 og 1439 kildepiksler mot grunnrommet. Rommets MYSTERY VORTEX-skilt, svarte skjeve trær med gulrand, orange/røde flater, steiner, tauverk og bilavkutting beholdes fra riktig rom036 del 2.

**Bare fire unike kildekompositter:** 02 og 06 er byte-identiske i hele RGB-bildet; det samme gjelder 03 og 05. Gjenbruk av samme valgte NYTEGNEDE resultat er derfor mulig innen hvert dokumenterte par. 01, 02, 03 og 04 skal derimot ikke dupliseres. Deres parvise forskjeller er 747 til 1267 piksler, se familiebevis. Dette påviser likhet/ulikhet, ikke animasjonens avspillingsrekkefølge eller varighet.

## Escher-rommets 01-panorama

lag037_01 del 1 og del 2 er én felles kompositt og må leveres fra **1920 × 800 master**, klipp x=0/384 med **1152 × 800 byte-identisk overlapp**. Originaloverlappen er byte-identisk. [Sammensatt kilde](a-037-master-kilde.png) er kun analyseforstørrelse.

Del 1 lister bare 345, men viser i tillegg 720 endrede kildepiksler fra andre synlige objekter i overlappen, bbox rom [125,0,348,176]. Del 2 lister åtte felt. Samlet master har 4191 endrede kildepiksler og null utenfor unionen av alle ni feltene. Del 1 må derfor ikke fremstilles med bare sin egen dørendring. Se felttabellen for begge delers eksakte leveransebokser.

Fire dører har svarte åpninger i stedet for de gamle fargede dørbladene:

- 345 ved rom [48,80,24,56]: lilla/blå dør er borte innen rosa ramme, 551 endrede piksler.
- 346 ved [160,96,24,24]: liten grønn dør er borte inne i tempelaktig ramme, 130 piksler.
- 347 ved [384,120,32,72]: orange skrå gulvdør har svart åpning, 880 piksler.
- 348 ved [408,8,40,120]: lang gul dør har svart åpning, 1969 piksler.

Rammer, størrelser og umulig perspektiv bevares; ikke legg inn dørblad som svinger ut hvis kilden bare viser fravær/svart åpning. Ingen innhold eller figurer fylles inn i svarte felt.

De fem andre feltene:

- 350_01, rom [208,0,40,24]: bare en liten gulbrun avskåret fiskedel ved venstre kant av blått felt, 26 piksler mot grunnrom. Ikke fullfør fisken utenfor den synlige delen.
- 351_01, [440,72,40,24]: svart/fiolett andeformet paraplyhåndtak med litt annen åpen nebbvinkel, 71 piksler. Behold den svarte runde hodeformen og liten nedre runddel, ikke gjør dette til en levende hel and med øyne/fjær.
- 352_01, [144,0,48,56]: stor svart 8-ball avskåret ved øvre kant. Egen form/plass av grå 8-flate og blå/hvite høylys, 540 piksler. Behold tallet 8 og avkuttingen; ikke tegn komplett svevende kule med ekstra topp.
- 353_01, [120,152,48,32]: bare egen variant av flygelets tangenter, 23 piksler. Lokket, kropp og bein følger grunnrommet. Ikke legg til hender eller pianist.
- 354_01, [328,128,32,40]: lilla dam uten oppreist periskop. Faktisk **bare én endret kildepiksel**, rom [347,164], fra RGB [79,63,167] til [79,79,183]. Ikke bruk navnet parascope som grunn til å legge til et rør. Den lille toneendringen må fortsatt dokumenteres og behandles som egen tilstand, ikke automatisk dupliseres med grunnrommet.

## Escher 02 og 03, del 1

Hver har fire egne felter: 350, 352, 353 og 354. Null kildeendringer utenfor unionen. De fire dørene skal forbli grunnrommets fargede, lukkede dører, og 351-nebbvarianten fra 01 skal ikke arves inn. Ingen fellesmaster er nødvendig mellom disse to ulike tilstandene.

350 er en gulbrun fisk som blir mer synlig i det blå feltet. 02 viser mer hode/kropp ved venstre kant; 03 viser den mer komplette lille fiskeformen lenger mot høyre. Senere kilder 04/05/06 viser videre plasseringer og bekrefter fiskeidentiteten. Behold gulbrun palett og enkel avskåret form, uten nye skjell, store øyne eller oppdiktet art. 01/02/03 skiller henholdsvis 47, 69 og 90 parvise piksler.

352 har egne kule-/8-/høylysvarianter. 03 har tydelige doble lyse konturbuer rundt 8-feltet og kulekant i originalen. Dette skal ikke automatisk ryddes bort som feil eller erstattes med samme pene 8-ball fra 01. Parvis forskjell mellom 01/02/03 er 553, 583 og 748 piksler.

353 har egne mørke/lyse tangentsegmenter. Forskjellene mot grunnrommet er 21 piksler for 02 og 15 for 03. Alle tre tangentfelter er forskjellige: parvis 44, 38 og 36 piksler. Bevar eksisterende antall tangenter og kildebestemt plass for endret tone; ingen bevegelig hånd skal oppfinnes.

354_02 og 03 har en liten svart/grå topp i den lilla dammen, lavere i 02 og større i 03. Senere originaler 04 til 0A bekrefter et grått bøyd periskoprør med svart åpning og egne høyder/retninger. I disse tidlige fasene tegnes bare den lave synlige toppen, ikke det fullførte røret. 02 har 29 og 03 har 63 endrede kildepiksler mot rommet; 48 piksler skiller dem. Behold dammens lilla form og de små lyse kantene.

## Stil, usikkerhet og mottak

Originalenes varme rødbrune gulv, lilla og orange vegger, blå/svarte takruter, speil, trapper, ulogiske skygger og skjeve gjenstander er tilsiktet. Romnotatene fra origin/main bekrefter MYSTERY VORTEX og at Escher-perspektivet ikke skal rettes. Tidligere HD-rom er konsistensankre, ikke bevis på at en ny variant er individuelt godkjent.

Ingen ny avgjørende motivusikkerhet krever spørsmål ut fra den gjennomgåtte konteksten. Uthusets funksjon/avspilling og periskopets timing er ikke runtime-testet. Eventuelle nye detaljer som ikke støttes av de konkrete kildene må holdes tilbake, ikke gjettes. Før generering skal root lese planen. Etter produksjon må mikrofeltene kontrolleres med forstørrelse og målinger, og 037-paret med både alle ni motiver, hele masteren og overlappshash.
