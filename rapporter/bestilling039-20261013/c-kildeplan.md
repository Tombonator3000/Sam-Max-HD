# Bestilling 39 – kildeplan, ingen generering

40 kildefiler for lag044_01–10 er låst i kildehash.json. Åtte kontekstfiler for 11–12 er låst i c-ekstra-kildehash.json. Alle tolv originaler, metadata og prompter er lest. Tre originalkontaktark og fire feltark er visuelt kontrollert. Rom044-notat og det opprinnelige gpt-romnotater-registeret er undersøkt; sistnevnte inneholder bare overskriften. Originalnavnene er deretter verifisert direkte i konsept/2026-10-12/objektbilder-959.csv, linje 373–394: ox-mouth/eye/ear, flamingo-eye/mouth, jackalope-eye/nose/mouth/ear/ear-2 og racoon-body/ears/mouth. Stavemåten racoon er bevart fra registeret. Dette avklarer identitet; runtime og detaljert funksjon er fortsatt ikke bevist.

Dette er full RGB-romkomposisjon, ikke atlas/alfaark. Canvas 1536 × 1024, motiv [128,112,1280,800], grå padding 128. Originalrom 320 × 200. Canvasfelt beregnes som [128+4x,112+4y,4w,4h]. Eksakte felt og endringsbokser står i c-mikrobevis.json. Alle første elleve tilstander har null kildeavvik utenfor sine metadatafelt. Bakgrunnen kan derfor gjenbrukes fra rom044-HD utenfor faktisk endrede felter.

## Motiver og tilstander

410_01/02 er nedre munn-/snutefelt på stort grått hornhode. 01 åpen munn med rød innside; 02 mindre/lukket åpning. 411_01 er øyefelt med lukket/skrå øyestrek. 412_01 er venstre øre under horn, langt smalt utsnitt. Registerets ox-mouth, ox-eye og ox-ear dokumenterer oksehode, ikke bøffel. Nytegning skal fortsatt følge originalens former, ikke et realistisk artsreferansebilde.

413_01 er flamingoens øye (flamingo-eye); 414_01 er flamingoens lange gule nebb (flamingo-mouth) i åpen tilstand med mørk åpning. Ikke tegn tenner eller nytt nebb. 415_01 er jackalopens øyefelt ved venstre dør (jackalope-eye), ikke vanlig hjort. 416_01 er jackalope-nose og 417_01 jackalope-mouth, med ulike rektangler; bevar hvitt/rosa og mørk åpning. 418_01 og 419_01 er venstre og høyre øre-/gevirnære felt, egne utsnitt, ikke to komplette hoder.

420_01–07 viser den samme grå, svartmaskerte dyrefiguren i tønnen: ulike høyder og munn-/kroppsposisjoner. Originalnavnet racoon-body dokumenterer vaskebjørn; 421 er racoon-ears og 422 racoon-mouth. Identiteten er dermed kildeavklart uten nytt brukerspørsmål. Funksjon og animasjonsrekkefølge er ikke utledet av navnet. Ikke gjør den til Max, katt eller vanlig ny figur. Bevar to spisse ører, svart ansiktsmaske, grå kropp, lys snute og rød munn. Figuren og tønnekanten overlapper; tegn ikke nye hender eller synlig full underkropp.

421_01–03 er bare 40 × 8 originalpiksler øverst ved figurens ører/hode. De skal ikke erstattes med en full ny figur. 421_02 (lag08) endrer bare TO kildepiksler mot grunnrommet; konkret liste og RGB står i c-mikrobevis.json. 421_01/03 endrer 46/48 piksler. 422_01 (lag11) er et 16 × 16 snute-/munnfelt med 29 endringer, lukket/flat munn sammenlignet med åpent grunnrom. Hele familien må kontrolleres samlet med utsnitt fra samme HD-identitet, og de små øreendringene må påvises visuelt, ikke bare ved høy feltkorrelasjon.

## Siste kontekstjobb: 408 og 409

Lag044_12 har obj409_01 i underlag. Det forklarer 5 350 kildepiksler utenfor 408-rektangelet. Eksakt kildekomposisjon er bevist: rom044 + obj409 original ved [136,0,184,96] + 408 ved [200,48,40,40] gir hele lag12 byte-identisk. 408 er det tomme lyse vegg-/panelfeltet som dekker midten av skiltet og har liten mørk merkeform øverst, ikke et nytt portrett. Skiltets synlige EDU...MENT skal bli avklippet bak feltet; ingen fullføring av skjulte bokstaver. Eksisterende nytegnet obj409 kan undersøkes for gjenbruk ved produksjon, med SHA og riktig plassering. Ikke påstå null avvik utenfor 408 alene.

## Palett, tomrom og risiko

Originalene har 112 farger, unntatt lag03 med 113 og lag12 med 115. De er rompaletter, ikke krav om å kopiere piksler eller automatisk begrense HD til samme antall. Bevar brun vegg/tønne, grålilla hornhode, rosa/gult nebb, brun/rosa hjortedetalj, grå/svart maskert figur og røde munnflater. Svarte forgrunnsformer og tak er bakgrunn som ikke skal gis nye identiteter. Generisk prompt nevner EDU-skiltet også når det faktisk mangler i lag01–11; kildene bestemmer synligheten.

Anbefaling: samme eier for hele 044-familien over 39/40. Lag én konsistent ny figuridentitet og behold egne 420-, 421- og 422-tilstander. Dyras øye/munn/ørekomponenter kan produseres lokalt fra egne originalfelt og HD-romkontekst. Hold 408/409-underlagskomposisjonen separat. Identiteten er avklart i originalnavnregisteret. Ingen generering før root har lest og bekreftet planen. Runtime, animasjonsrekkefølge, lydkobling og spillfunksjon er uverifisert; nummerrekkefølge alene beviser dem ikke.

## Jobbfordeling og eksakte originalrektangler

- lag044_01: obj410_01 [72, 32, 32, 24]; obj412_01 [40, 8, 24, 48]; obj414_01 [112, 48, 32, 24]; obj415_01 [16, 72, 16, 8]; obj420_01 [88, 80, 40, 32]
- lag044_02: obj410_02 [72, 32, 32, 24]; obj416_01 [24, 80, 16, 8]; obj420_02 [88, 80, 40, 32]
- lag044_03: obj411_01 [64, 16, 24, 16]; obj413_01 [96, 40, 24, 16]; obj417_01 [16, 80, 24, 16]; obj420_03 [88, 80, 40, 32]
- lag044_04: obj418_01 [0, 48, 24, 32]; obj420_04 [88, 80, 40, 32]
- lag044_05: obj419_01 [24, 48, 16, 32]; obj420_05 [88, 80, 40, 32]
- lag044_06: obj421_01 [88, 80, 40, 8]
- lag044_07: obj420_06 [88, 80, 40, 32]
- lag044_08: obj421_02 [88, 80, 40, 8]
- lag044_09: obj420_07 [88, 80, 40, 32]
- lag044_10: obj421_03 [88, 80, 40, 8]
- lag044_11: obj422_01 [104, 88, 16, 16]. Kontekst fra bestilling 40.
- lag044_12: obj408_01 [200, 48, 40, 40]. Kontekst fra bestilling 40.
