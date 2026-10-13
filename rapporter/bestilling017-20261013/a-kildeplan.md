# Kildeplan for bestilling 17

13. oktober 2026. Kun analyse og denne rapporten er skrevet. Ingen generering, bildeendring, produktkode eller Git-mutasjon. Alle ti bestilte originaler og ekstra rom077 del2 er undersøkt i original-kontaktark.png; 4x-visninger av rom070 begge deler, rom071, rom073 del2, obj772, rom076, obj773 og rom077 del2 er også sett separat. Rom016 begge deler er undersøkt som sammenligningskilde. Jobbmetadata, promptenes romnoter og konsept/2026-10-12/objektbilder-959.csv er lest. origin/main:docs/gpt-romnotater.csv, docs/rom-oversikt.csv og docs/ANALYSE.md er lest uten endring. Alle 40 + 4 låste kildefiler stemmer med SHA256. GRUNNLAG.md fantes ikke ved analysestart.

## Geometri og lag

| Jobb | Originalregion | HD-motiv [x,y,b,h] |
| --- | --- | --- |
| obj684_01 | [0,0,320,24] | [128,464,1280,96] |
| rom070_del1av2 | [0,0,384,200] | [0,112,1536,800] |
| rom070_del2av2 | [96,0,384,200] | [0,112,1536,800] |
| rom071 | [0,0,320,200] | [128,112,1280,800] |
| rom073_del1av2 | [0,0,384,200] | [0,112,1536,800] |
| rom073_del2av2 | [152,0,384,200] | [0,112,1536,800] |
| obj772_01 | [0,0,320,200] | [128,112,1280,800] |
| rom076 | [0,0,320,200] | [128,112,1280,800] |
| obj773_01 | [0,0,128,184] | [512,144,512,736] |
| rom077_del1av2 | [0,0,384,200] | [0,112,1536,800] |
| ekstra rom077_del2av2 | [256,0,384,200] | [0,112,1536,800] |

Alle leveranselerret er 1536 × 1024 med grå RGB128-padding. Svarte felter innen motivrektanglene tilhører kilden og må beholdes. Obj773 har objekt_i_rom [176,0,128,184]; det er posisjonen i rom076, ikke plasseringen på leveranselerretet. Rom073 har også svarte vannrette felt over og under landskapet innen selve motivet.

## Panoramaer og bevis

De tre parene er sammenlignet som dekodet RGB ved skala1. Antall ulike piksler i overlappen er null for alle tre. Én fullscene per rom og felles klipp gir konsistent HD-overlapp. Hashene nedenfor gjelder rå RGB-bytes, ikke PNG-filbytes.

| Rom | Fullmaster HD | Del1-klipp | Del2-klipp | Overlapp HD |
| --- | --- | --- | --- | --- |
| 070 | 1920 × 800 | [0,0,1536,800] | [384,0,1536,800] | 1152 |
| 073 | 2144 × 800 | [0,0,1536,800] | [608,0,1536,800] | 928 |
| 077 | 2560 × 800 | [0,0,1536,800] | [1024,0,1536,800] | 512 |

Klippene er [x,y,b,h] fra fullmaster; deretter plasseres hvert klipp ved (0,112) på lerretet. Rom077 del2 er ekstra analysekilde, ikke en ellevte bestilt levering uten egen ordre. En bevart fullmaster kan senere brukes til del2 uten en uavhengig nytegning som skaper søm.

- Rom070 overlapp 288 × 200: 7284192e88930009791ef99dc1c731787b62487575359679a9a3276be56754e0. Samlet original 480 × 200: b41d5dd15c1dd91a1d491515aa23c8711ed2ec8cc8cc845a6c68a30c8dc801ae.
- Rom073 overlapp 232 × 200: dede684531a98a99a419294b39c877cb6363f65d38307effa4d101c70c62971b. Samlet original 536 × 200: 7906019a9ff2323e13dc17e6bba992ea94198d32100e5bcea013b3683493feff.
- Rom077 overlapp 128 × 200: c54080dacfdc7c42148e1da578fc83e6b0c93466b4e29df62bcd8de181664e88. Samlet original 640 × 200: 6dc7f0bf39c372f146a1e2e222a3d1d0a776dac3fd91f94431cdd1f24defd665.

## Motiver og nødvendige promptkorreksjoner

### Obj684: tredje horisontkontur

Register: surfin-horizon-3, rom69. En tynn ujevn gul/oransje kontur i svart 320 × 24-felt. Bevar avbrudd, små høyder og konkrete topper fra denne varianten; ikke kopier 682/683 eller lag nattehimmel, sol, fjelltekstur eller glød. Ingen tekst eller figurer. Det er visuelt en horisontlinje; faktisk scrolling og kobling til Highway Surfing er ikke motortestet.

### Rom070: fargede påkledningsdeler, ikke grå silhuetter

Begge originalhalvdelene viser fullt fargede klær og rekvisitter på lys kremfarget bakgrunn med grålilla slagskygger. Romnavnet og promptens flat-gray-instruksjon er derfor misvisende for disse bytes. Den må motsies uttrykkelig i separat kildepresisering.

Registeret har 26 objekter 685 til 710 kalt asd, som hver for seg ikke identifiserer motivet. De tilsvarende navngitte Max-delene i rom071, 745 til 770, gir vesentlig bedre tolkningsstøtte: scout, metal, bridal, vampire, bullfighter, dominos, pajamas, scuba; swiss-knife, guitar, chicken, bouquet, vampire-bat, bull-sword, bull-cape, pizza-scice, teddy-bear, alarm-clock, scout-hat, punk-hair, veil, fangs, beret, pizza-cap, pumpkinhead og bubblegumhead. Dette er kildebaserte ressursnavn, ikke bevis for klikkrutine eller dynamisk rekkefølge.

Synlig innhold samsvarer med blant annet flaggermus, rød/gul gitar, gresskarhode, grønt speiderantrekk, hvit brudekjole, mørkt dykkersett med svømmeføtter, rødt/gult tyrefekterantrekk, pizzaeske/budantrekk, piggete mørkt antrekk, fargerikt hode, rød/gul lue, svarte små ansikts-/hårdeler, grønn hatt med åpen ansiktsplass, bukett, teddybjørn, vekkerklokke, pizzastykke, flerbruksverktøy, hvitt slør, vampyrantrekk, rød kappe, sverd, blå/gul pysjamas og fugle-/kyllingrekvisitt. De tomme hals-/ansiktsfeltene skal ikke fylles med Max-kropper. Ikke legg til hender eller hoder i klær som er avklipt eller hule.

Små tegn på pizzaesken og andre rekvisitter er ikke sikkert lesbare her. Bevar glyffformer; ikke skriv et antatt merkenavn. Fullmaster er nødvendig for gitar, antrekk og sverd som krysser klippgrensen. Separate piler 711/712 finnes i registeret, men skal ikke tegnes inn i bakgrunnen.

### Rom071: to grunnfigurer uten betjeningsgrafikk

Sam står til venstre med brun pels og rødt lite plagg med gule detaljer; Max står til høyre med hvit pels, rosa øreinnside og bred tannrekke. Hendene er åpne, armene ut fra kroppen. Bevar konkrete kroppsproporsjoner og uttrykk, uten å kle Sam i standarddress eller legge på påkledningsvarianter. Bakgrunnen er kremfarget stjerneutslag med oransje kant på ferskenfarget felt.

Ingen PUSH ME!-tekst eller piler finnes i denne bakgrunnen. Registeret dokumenterer separate dolls-right-arrow 713, dolls-left-arrow 714 og dolls-button 771 med to tilstander. Dette støtter at romnotens betjeningsgrafikk tilhører egne objekter. Ingen skriptrekkefølge eller faktisk knapptekst er kontrollert i dette arbeidet.

### Rom073 og obj772: landskap og fiskemunnoverlegg må holdes atskilt

Rom073-panoramaet viser en fisker som står i elven. Han har brun hatt med grønn fjær/farget feste, mørke briller, varm hudfarge, grå vadere og fiskestang med lys snøre som går ned i vannet. Bevar begge henders grep, stangens bøy, snørets forløp, ringene rundt bena, grønn elvebredd, mørke trær og rosa/lyse fjernformer mot blå himmel. Figuren ligger i høyre del av fullscenen og går gjennom del1 sin høyrekant; den skal være én konsistent figur, ikke to fiskere. Personens egennavn er ikke fastslått.

Obj772 heter infish-heads. Det separate 320 × 200-bildet viser utsyn fra en mørk fiskemunn med tenner og innvendige folder. Max sine lange ører/hode er til venstre, Sam sin hatt/snute/skulder til høyre. Silhuettene er nesten svarte med kalde gråblå kanthøylys, ikke fullt belyste portretter. Landskapsåpningen viser samme miljøtype, men komposisjonen skal tas fra obj772 selv. Ikke sett fiskeren eller nye ansiktstrekk inn i åpningen. Antall og plassering av tenner/folder må telles fra den konkrete originalen før generering. Promptnotens fish-mouth-instruksjon gjelder dette objektet, ikke rom073-bakgrunnen.

### Rom076 og obj773: frossen Bruno og tom isrest

Rom076 er et tilbakeblikkutdrag fra freakshowet: Bruno står som gråblå langarmet Bigfoot inne i høy blåhvit is på høyre sokkel. Venstre grønne sylinder er tom i denne varianten, i motsetning til den synlige figuren i rom016. Bevar tomheten. Gardinåpningen er blålig; ikke importer rom016 sin grønnere dagslysutsikt. Gulv, sokkel, lampe/stativ og mørke felter beholdes.

Obj773 heter flashback-bruno og har metadata [176,0,128,184] i rom076. Originalen viser tom, lavere, uregelmessig isrest på sokkelen med vann på gulvet, uten Bruno inni. Ikke tegn en sittende Bigfoot eller fyll hulrommet. Sammenligning mot rom016 del2 støtter den tomme/smeltede isformen, men palett og bakgrunn er ikke byte-identiske. Beste rent numeriske toppjusterte plass i rom016-master er x352; 16621 av 23552 piksler avviker. Mot rom076 sitt metadataklipp avviker 9810 av 23552 piksler. Ingen av disse er grunnlag for blind kopiering.

Synlige tekstformer omfatter BRUNO på sokkelen, THE, FROZEN og BIG FOOT på øvre skilt, og venstre CHICKEN DUMPLING i rom076. Øvre BRUNO er delvis i mørke/avklipt; ikke fullfør skjulte bokstaver. Rom016 viser samme utstillingsskilt tydeligere, men det gir ikke tillatelse til å lysne eller utvide avklipt tekst i rom076/obj773. Motorovergang fra frossen til tom is, timing og palettstyring er ikke undersøkt.

### Rom077: svart bakgrunn med avgrenset perspektivveifelt

Fulloriginalen er 640 × 200. Alle ikke-svarte piksler ligger i [320,67,320,66]. Del1 viser bare de første 64 kildepikslene av dette feltet langs høyrekanten; del2 viser hele feltet fra sin lokale x64. Den andre delen gjør motivet lesbart: mørk grå perspektivvei med smal midtstrek, lave horisontformer og røde vannrette topp-/bunnlinjer.

Hele masteren har bare seks RGB-farger: svart (0,0,0), grå (23,23,23), (39,39,39), (55,55,55), (71,71,71) og rød (207,0,0). De røde linjene utgjør 640 piksler, forenlig med to 320-pikslers rader. Bevar feltets ekstreme mørkhet, den store svarte flaten, antall synlige midtmarkeringer og klippingen. Ikke gjør rommet til et lyst Highway Surfing-landskap eller legg inn biler, navn, rulletekst eller nye paneler.

Registeret har separate credit-panel-1 til 6 og credit-killer/-2, 774 til781. Det forklarer hvorfor rommet kan være navngitt rulletekst uten at selve bakgrunnen inneholder navn. Det beviser ikke at veifeltet er synlig i normal sluttsekvens eller nøyaktig hvordan panelene komponeres. Rapporten kaller det derfor synlig perspektivveifelt, ikke en motortestet sluttkredittfunksjon.

## Produksjonskrav og usikkerhet

Beskyttede promptfiler skal beholdes. Bruk ordrett tekst med tydelig kildekorreksjon for 070/071/073/077. Originalpalett og konkret lag overstyrer generiske romnavn. Godkjente stilankere må ikke tilføre rekvisitter eller fullføre tomme felt.

Uendret checker, presis plassering, padding, råforsøk, komplette prompter og SHA-sporing kreves. Panoramaenes valgte HD-overlapp må være byte-identisk fra én master. Samlet visuell kontroll skal særlig omfatte inventar/klær i 070, grunnfigurene i 071, fiskerens hender/snøre i 073, mørke silhuetter/tenner i 772 og forskjellen frossen/tom is i 076/773.

Ingen runtime, import, faktisk palettbytte, figur-/objektskript eller nye individuelle bildegodkjenninger er utført. Repositoryanalysen omtaler dekompilerte skript, men ingen passende lokalt lagrede skriptfiler ble funnet ved den avgrensede filnavnsøkingen her. Ressursregister og bildeobservasjon er ikke funksjonsbevis.
