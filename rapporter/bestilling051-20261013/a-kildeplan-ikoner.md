# Kildeplan for ikon01 til ikon09, bestilling 51 og 52

Kun analyse. Ingen ikonbilder er generert eller jobbmapper endret. Alle 163 kildefelt er sett som nærbilder, og metadata og originalnavn er gjennomgått. Ni ark har 6, 8, 10, 7, 8, 7, 22, 47 og 48 felt. De 36 beskyttede ikonfilene er låst i [a-ikon-kildehash.json](a-ikon-kildehash.json), separat fra rotens bestilling 51-lås. Dette låser ikke de seks figurjobbene i bestilling 52.

## Format og kontrakt

Alle ni ark er 352 × 240 originalpiksler. Eksakt leveransecanvas er 1536 × 1024; motivfeltet er [64,32,1408,960], skala 4. Grå padding er RGB [128,128,128]. Selve arkets tomme bakgrunn er RGB [255,0,255]. Jobbmetadata har type ikon, ikke figur. Jobbprompten krever flat magenta, ingen rammer eller glød som legges til rundt motivene. Faktisk eksisterende kortkant, bakgrunn og rød kant inne i et ikon er derimot kildeinnhold og skal bevares.

Ikonruter er atlasplasseringer, ikke koordinater i kilderommet. Hver rektangel i jobb.json skal skaleres og forskyves med [64,32]. Mellomrommene og avkuttingen er funksjonelle. En metadatarektangel kan inneholde et helt landskapsutsnitt, et avskåret skilt, en helt tom magentarute, eller en ugjennomsiktig beige kortbakgrunn. Svart er faktisk motivfarge og skal ikke gjøres transparent.

Den leste origin/main-versjonen av pipeline/smhd/gpt.py er bevart som a-ikon-importkontrakt-kilde.py.txt, med Git-ref og SHA i a-ikon-konteksthash.json. icon_sheet_image setter originale RGBA-objekter over opak valgt bakgrunn og returnerer RGB. _finish_pieces klipper metadatarektangler og håndterer senere tilstander med match_state. _with_alpha legger på originalens oppskalerte alfa ved import. Dette er observert importkode, ikke en ny tillatelse til originalsilhuettmasker under tegning. Ingen import eller runtime er utført. Et fremtidig ønske om nye glatte alfakanter må samordnes med motoransvarlig; ikke anta at levering som RGBA alene erstatter denne importveien.

Uendret sjekk_leveranse.py bruker check_picture på ikonark: helbilde-fase/kantkontroll og hver faktisk metadatarektangel. Perfelt OK ved kantkorrelasjon minst 0.60, SJEKK minst 0.50, ellers FEIL. Små eller nesten kantløse kildefelt kan hoppes over. Skriptet krever ikke figurarkets ekte alfa for type ikon og beviser ikke ikonidentitet, tekst eller korrekt tomtilstand. Egen detalj-QA er nødvendig.

## Motivfamilier og konkrete tilstander

Fullt register med hver av de 163 identitetene/visuelle beskrivelsene: [a-ikon-motivregister.md](a-ikon-motivregister.md). Eksakte ruter, palettantall, dominerende RGB, synlige bokser og hver rutebildehash: [a-ikon-feltbevis.json](a-ikon-feltbevis.json). Nærbilder: a-ikon01-felt.png til a-ikon09-felt.png; 08 og 09 er også delt i tre leselige sider hver.

* Ikon01: LucasArts-logo, liten avskåret dinosaurhodeflate og tre bakfra-vinkler av den svart/hvite politibilen. Ikke tegn bilene som samme bilde speilet. 560s blågrønne hode og grå åpne munn er visuelt samme dinosaurattraksjon som i de to rom058-originalene. Et fullstendig byteidentisk 24 × 24 utsnitt ble ikke funnet der, så den konkrete egenvarianten må bevares. Ingen hel dinosaur skal fullføres.
* Ikon01 til 03: seks store grønne Highway Surfing-skilt har hver sin kildehumor, skjold og pil. Teksten er skrevet ut i motivregisteret; glyfform er fasit for apostrof og små bokstaver. De små høyrefragmentene er egne utsnitt. 677, 679 og 681 er fullstendig tomme, alle tre byteidentiske og uten synlige piksler. Det er feil å fylle dem med et skilt fordi navnet antyder det.
* Ikon03 til 06: rom078s landskapsbiter er selvstendige blå/grønne utsnitt med trær, skyer og avklipping. Navnene mt/mv/mr beviser ikke en bestemt runtime-rekkefølge. Stubbe, regnsky, argyletrær, brennende dekkhaug og himmellys er tydelige særegne motiv. Ikke gjør dem til én generisk skog eller sett trestrimler sammen som et vanlig panoramapar. Ingen kildebevist sammenhengende master er etablert.
* Ikon07: skrå del med grå hånd/arm og forstørrelsesglass, to tilstander av hver glassgruppe, tre separate brune slange-/hodefragmenter, deretter handlingspekere. 825_01/02 skiller 458 RGB-piksler, 826_01/02 skiller 1064. 826_02 har også egen magenta avkutting. Ingen av disse parene er duplikater. Nøyaktig overlay/runtime er ikke testet.
* Ikon07 og 08: pekere har øye, knyttet/åpen hånd, åpen/lukket munn, grønn gjenstand i hånd, blå kortflater, eske, fingerstillinger, blyant og telefon. Rene hvite 891/892 og noen grønne symbolers presise funksjon er ikke kildeavklart. Ingen sort kontur eller indre detaljer skal oppfinnes.
* Ikon08 og 09: beige inventar-/samtalekort med røde markeringskonturer, brun/svart avkuttet ramme og egne motivvarianter. Henter, inntørket hånd og fiskemagnet stemmer visuelt med tidligere kildeavklart familie fra bestilling 7. Flere små inventarmotiver trenger fortsatt funksjonsavklaring før nytegning, se spørsmålene nedenfor. Ingen uklar glyf skal gjøres til gjettet tekst.

## Identiske og tomme felt

[a-ikon-duplikater-og-kontekst.json](a-ikon-duplikater-og-kontekst.json) viser byteidentiske felt: 677/679/681; 1000/1002/1003; 1007/1012/1014; 1064/1065/1066/1067. Den sistnevnte gruppen er tomme BEIGE kort med eksisterende ramme, ikke transparent bakgrunn. 1000/1002/1003 viser samme avskårne svarte fragment på venstre side og brune fragment på høyre side. Dette er faktiske kildebytes, ikke en feil i kontaktarket. Det må ikke normaliseres til et helt motiv uten avklaring.

## Avklaringsbehov før produksjon

Det er fortsatt semantiske spørsmål, og brukerens instruksjon om å spørre ved uklare motiv gjelder. [a-ikon-sporsmal-1.png](a-ikon-sporsmal-1.png) og [a-ikon-sporsmal-2.png](a-ikon-sporsmal-2.png) gir A til H med entydige objekt-ID-er. De er kildeutsnitt, ikke nye tolkningsforslag.

A: Hva representerer de rent hvite pekerformene 891 og 892? Skal de fortsatt være helt hvite uten indre detaljer?

B: Er de delte/avskårne kortene 1000, 1002 og 1003 tilsiktede overgangs-/plassholderbilder som skal bevares nøyaktig slik? Kilden er identisk i alle tre.

C: Hva er de tre brune/røde sammensatte formene 1026 til 1028, og hvilke deler skiller variantene?

D: Hva forestiller gullformen 1024, den brune/gylne gruppen 1029 og den rullede brune bunten 1030?

E: Hvilke kort/ark/bok er 1041, 1043 og 1044? Hvis teksten er meningsbærende, trengs den eksakte teksten eller beskjed om å bevare uleste glyfer.

F: Hva er de to gule formene 1053/1054 og den gule hår-/hjelmformen 1055? Ikke lås en sverd-/nøkkeltolkning ut fra silhuett alene.

G: Hva er håndtakene med rett/sikksakkspiss 1057/1058 og den brune blokken 1060?

H: Hva er skålen 1075 og betydningen av de fire konkrete totemsymbolene 1076 til 1079? Symbolene kan bevares som synlige former, men skal ikke nytolkes til andre dyr eller personer.

Øvrige konkrete uavklarte funksjoner er merket i motivregisteret, særlig 1009, 1017, 1038, 1045 og 1080. Disse bør spores gjennom inventartekst eller original gameplay før samlet produksjonsstart; A til H er første samlede kildeark, ikke en påstand om at alle andre felt er funksjonsbevist. Kildenes originalnavn for rom093/094 er blanke og løser ikke spørsmålene.

## Foreslått produksjonsdeling etter avklaring

Hold bilene som én identitetsfamilie, skiltene som én tekstfamilie, landskapsbitene som én palettfamilie, og små peker-/inventarsymboler som egne serier. Nytegn hvert motiv uten å fullføre kildeavkuttede deler. Bruk én valgt ny tegning for faktisk byteidentiske kilder, med presis plassering i hver egen rute. Bevar forskjellige kortkanter og fargefelt der kildebytes varierer. Magenta skal være flat og bare tilhøre arket. Ingen originalpiksler eller originalkonturmasker i de nye tegningene. Ingen produksjon er startet; rot skal lese planen og håndtere nødvendige brukeravklaringer først.
