# Kildeplan for bestilling 26

Kun analyse. Ingen nye produksjonsbilder eller jobbfiler er endret. Ti jobber er låst med 40 SHA-256 i kildehash.json. Én tilstand fra neste bestilling, lag012_05_del1av2, er lest og låst med fire ekstra hash som kontekst for statuefamilien, ikke ekstra produksjon. Source-faithful-production er lest og brukt. Originalkontaktark, hvert objektfelt, registerrader, faktiske paletter, metadata og leverte HD-anker er undersøkt.

## Omfang og format

Root eier senere kartproduksjon lag010_05,06,07, etter familieanalysen i bestilling25. De har henholdsvis fem, fire og to objektbilder, med null originalendringer utenfor metadataunionen. 1665,1531 og943 piksler endres mot grunnkartet. Root-kart-kildeplan.md og B sin familie-QA i25 er hovedgrunnlag, ikke en ny tolkning her. GREETINGS from the USA, HI THERE!, landkontur og grid skal beholdes. De elleve kartfeltene og deres 03-/02-tilstander finnes i a-feltbevis.json.

A sitt senere produksjonsomfang er de sju øvrige jobbene. Alle er opake RGB-kompositter, 1536 x 1024, motiv [0,112,1536,800], padding RGB128. Rom011 og012 er480 x200. Del1 starterx0, del2 starterx96. HD-bokser nedenfor er [x,y,bredde,høyde] på leveranselerret, med regionforskyvningen korrekt trukket fra. De er ikke nye atlasruter.

| Jobb/objekt | Original romrekt | HD-rekt | Faktisk motiv |
|---|---|---|---|
| lag011_01_del2av2 /118_01 |392,56,48,72|1184,336,192,288|Innvendig dørvariant med lys grå/blå flate, mørk karm og egen åpning/diagonal nedre kant; delvis tildekket av grønne/lyse skjorter|
| samme /126_01 |248,88,32,24|608,464,128,96|Hyllefelt med oransje/brune esker; den lille åpne beholderen fra grunnrommet er fraværende. Ikke legg til en ny matbit fordi navnet sier doug-treat|
| samme /129_01 |200,8,48,32|416,144,192,128|Halvrundt glassfelt med GRØNN iskule og oransje kjeks, varme gule/røde/hvite glassbiter|
| lag011_02_del1av2 /129_02 |200,8,48,32|800,144,192,128|Samme glassfelt med avlang ORANSJE ispinneliknende form, ikke grønn kule eller grunnrommets rosa smultring|
| lag012_01_del1av2 /132_01 |0,120,192,80|0,592,768,320|Stor lav svart/blå bil, hvitt tak/dør, gul stjerneform, fire runde gule lykter og bred skrå sølvgrill; avklipt ved venstre scenegrense|
| lag012_01_del2av2 /131_01 |272,80,32,72|704,432,128,288|Utvendig blå glassdør i egen åpen/skrå stilling; butikkhyller synlige bak|
| samme /134_01 |408,64,56,32|1248,368,224,128|Utvendig halvrundt glassfelt med grønn iskule/oransje kjeks. Det er et annet utsnitt og vinkel enn129|
| samme /135_01 |312,160,24,16|864,752,96,64|Tom grå fortausflate: grunnrommets lille hvite/cyan/røde kopp er fjernet|
| lag012_02_del2av2 /134_02 |408,64,56,32|1248,368,224,128|Utvendig glassfelt med avlang oransje ispinneliknende form; kopp og øvrig rom følger grunnrommet|
| lag012_03_del1av2 /133_01 |184,64,88,96|736,368,352,384|Brun dekorativ skorpionform med segmenter, stor kloform, bøyd hale og strå-/sombreroliknende gul hatt; ingen levende figur skal konstrueres|
| lag012_04_del1av2 /133_02 |184,64,88,96|736,368,352,384|Brun oppreist hareliknende dekorfigur med gevir, lange ører, lyse magefelt og store bakføtter|

Registeret kaller118/131 door,126 snuck-in-doug-treat,129 snuck-in-window,132 snuck-car,134 snuck-out-window,135 snuckeys-cup og133 snuck-statue. Ingen bryter finnes i disse sju metadataene. Navnene alene beviser ikke hva som skal tegnes: særlig126 og135 er fraværstilstander, og129/134 skifter konkret motiv. Ikke legg et generisk bryterobjekt eller en person inn i rommet.

Ekstrakontekst133_03 i neste bestilling viser grønn kaktusdekor med to armer, stor brun hatt, rødt halstørkle og grå sokkel. Dette avklarer at133-familien omfatter ulike dekorfigurer, ikke tre positurer av samme levende dyr. Den ekstra jobben skal ikke produseres i26.

## Fellesmaster og bakgrunnsbevis

Lag012_01-delene har byte-identisk originaloverlapp288 x200. Bruk én1920 x800 HD-master og klipp1536bredde vedx0 og384, med1152 x800 identisk overlapp. a-lag012_01-original-master.png er analysemasteren. Bilen er synlig også i del2, selv om metadata eier uttrekket i del1. Dør og tomt koppfelt er synlige også i del1. Derfor er683 avvik utenfor del1s egen objektboks og3755 utenfor del2s lokale metadataunion tilsiktede deler av den ANDRE delens objekter. Ikke fjern dem ut fra lokalt eierskap.

Levert rom011- og rom012-HD har allerede byte-identisk1152 x800overlapp. De eksisterende1920 x800masterne er samlet i rapporten som konsistensreferanser, og kildehashene står i a-ankerhash.json/a-sammenhengsbevis.json. Dette betyr ikke ny individuell brukergodkjenning. Lag011_01del2 og011_02del1 er ULIKE tilstandssett; de skal ikke klippes fra samme nye master som om de var to deler av samme lag. Felles glassfelt kan sammenlignes i absolutt romkoordinat, men innholdet er ulikt.

Lag011_01del2 har2049endringer mot grunnrommet:1000 i dørfelt,313 i varefelt og736 i glassfelt; null utenfor unionen. Lag011_02del1 har692endringer, alle i glassfelt129_02. Lag012_02del2 har357endringer, alle i134_02. Her er gjenbruk av NYTEGNET grunnrom utenfor de konkrete feltene kildebevist.

VIKTIG: Lag012_03 og04 har også5006 endrede piksler UTENFOR statuefeltet. Den grønne høye vegetasjonen i grunnrommet er delvis erstattet med røde/oransjebrune klippeformasjoner. Endringene utenfor objektboksen er identiske i03,04 og ekstrakontekst05, innen samlet originalbbox[0,0,221,107]. Se a-statuer-bakgrunnsforskjell.png. Dette er ikke en ren palettendring: silhuetter/former endres. Det er heller ikke grunnlag for å kalle det et tilfeldig eksportavvik og kopiere grunnrommet blindt. Originalen styrer den synlige landskapsvarianten; faktisk motortilstand/geografisk betydning er ikke bevist her.

Statue03 og04 skiller4507piksler totalt;04 og05 skiller4222. Bakgrunnsfeltet utenfor133 er identisk, mens de forskjellige dekorfigurene og bakgrunnsdelene innenfor deres store boks følger hver variant. Lag03 har3400endringer innenfor133, lag04 har2910, lag05 har3822. Bruk ett konsistent nytt landskapsunderlag for denne familien hvis det genereres, men legg inn hver konkret figur og bevare alle form-/palettforskjeller. Det er ingen tillatelse til originalpikselmaskering eller vektortrace.

## Palett, tekst og videre produksjon

Objektboksene inneholder henholdsvis68,50,77,64,73,46,69,12,74,105 og87 RGB-farger i tabellrekkefølge. Disse antallene inkluderer komposittbakgrunn; de er ikke alfapaletter for isolerte objekter. Full RGB-liste med pikselantall finnes i a-feltbevis.json, sammen med registerbevis og eksakte koordinater. Ingen lilla/mørke bakgrunnsfarger skal tolkes som transparens.

Origin/main:docs/gpt-romnotater.csv krever fountain-skilt og alle vare-/hyllebokstaver beholdt i11, og begge Snuckey's-skiltene i12. Den allerede leverte butikkstilen, gulvfliser, glasshyller, stativer, stolantall, telefonfravær og pumpe-/tak-/vindustopologi skal bevares. Ingen ny lesbar merkevaretekst på utydelige esker. Originalens øvrige avklippinger er tilsiktet.

Anbefalt produksjon: innebygd imagegen med ordrett prompt pluss separat kildepresisering og riktig levert HD-basis. For enkeltfelt kan en ny rektangulær komponent settes presist inn i nytt HD-rom etter bevist bakgrunnslikhet. For012_01 brukes fellesmaster. For statue03/04 må også det dokumenterte landskapsfeltet nytegnes, med samlet kilde-/familiekontroll før levering. Ingen originalkonturmasker, originalpikselkopi, lokal warp eller antatt runtime-rekkefølge. Kontrollér spesielt tom koppflate, manglende vare, døråpning, glassmotiv og figuridentitet.

Alle felt må senere få nærbilder og eksplisitt perobjektkontroll i tillegg til uendret checker. Ingen generering er utført i denne analysen. Root skal lese/samordne før26produksjon. a-analyse.py.txt og a-sammenheng.py.txt er rapportoppskrifter; øvrige JSON/PNG er målebevis og analysebilder, ikke nye leveranser.
