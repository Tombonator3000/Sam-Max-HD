# Kildeplan for fig325_01 og fig325_02

Motivet er Max, ikke Sam. Originalbildene, jobbnavn, prompt og RGB-identiske donorkilder samsvarer om dette. Ingen nye klær eller rekvisitter vises. Ark 01 har 29 cels:27 hoder og 2 små separate skjøtecels. Hver skjøt inneholder to adskilte lyse former, så de fire synlige små merkene er to cels, ikke fire nye ruter. Ark 02 har 3 bakhoder og 1 hel stående Max. Alle 33 cels er visuelt sett i b-kilder-*.png. Ingen produksjon eller generering er startet.

## Geometri og lag

Begge originale atlas er 352 x 240 med cyan bakgrunn(0,200,200). HD-lerret er 1536 x 1024, innhold[64,32,1408,960]. Hver synlig-boks skaleres 4x med offset(64,32). Hoder ligger på lag 3, skjøtene 512/513 pålag 4, helfigur 0 pålag 0. Kildemetadata for kostyme 325 er rom 66, format 0 x 58,16 farger, rom66-palett 0, fire retninger og speil=false. Bevar originalens lyse kremfarge, beige skygge, rosa nese/ører og hver sorte/hvite/røde munnstilling.

Alle 33 valgte donorers originale synlig-RGBA er byte-identiske, også RGB-paletten, med 325 kilden. Original w/h er også identisk. Rel-koordinatene er IKKE like:325 har gjennomgående x-1,y+19 originalpiksler relativt til donor. Dette tilsvarer(-4,+76)HD ved lagplassering, ikke en beskjed om å flytte atlasruten.325 metadata beholdes. Ingen antatt lik timing/runtime. Tabellen og b-donorbevis.json gir alle utsnitt og koordinater.

## Kontekst og donorer

Registeret skript-kostymekoblinger.tsv har 325 i globale/scrp_065.txt:375 aktør 9, globale/scrp_066.txt:195 aktør 11, rom_022/inngang.txt:127 aktør 6 og rom_042/lokal_201.txt:17 aktør 7. Registerkoblinger er ikke lest fullscript eller bevist hendelsesforløp. Ingen konkret funksjonsfortelling er nødvendig for å bevare de identiske Max-cellene.

Valgte nye donorer er fig003_01, fig003_02 og fig005_03. De 32 første kan kopieres fra levert Max-kunst; helfigur 0 har eksakt kildepartner fig005_03:0.386 og 423 har samme originale synlig-RGBA; planen bruker 003_01:386 for begge. Andre kildeidentiske kandidater finnes i b-ruteregister.json, men donorbytte må ikke være tilfeldig. b-donorhash.json låser 12 donor-/kildefiler. Åtte 325 kildefiler er låst i b-kildehash.json. Fig 326 er ikke endret.

## Viktig visuell donorbegrensning

Alle fem b-donorer-ark er sett. RGB-identisk original gir grunnlag for gjenbruk, men godkjenner ikke automatisk tidligere HD-tolkninger. Tre konkrete fargeforbehold:donor 395 har en rød liten munnform der original 395 har svart/hvitt;donor 402 har rød strek nederst i munnen mens original 402 ikke har rødt;donor 418 har rød liten munnform mens original 418 ikke har rødt. Dette skal avklares med rot før kopiering som ferdigleveranse. Øvrige hoder har renere, rundere øyne og bredere glatte munnkonturer.413/419 s tidligere neserettede donorer har én rosa nese hver, egne o-munner;411 har ingen rød tunge etter rettingen.

512/513 er 14x 2 originalpiksler og skal leveres 56 x 8 med de to små adskilte nye formene beholdt. Checker kan hoppe over så små kildearealer; særskilt alfa-/pikselunion og donorhash kreves. Ikke slett dem for å fåOK. Helfigur 0 må ikke få ekstra hode pålag 3 uten faktisk animasjons-/sammensettingsbevis. Ingen Sam-hovedark brukes; Max-hovedarket er relevant identitetsanker.

## Foreslått behandling

Etter rotgjennomgang:presis bytekopiering av dokumenterte NYE donorutsnitt til hver 325 synlig-boks, uten generering der donor er motivmessig korrekt, uten originalsiluettmasker, skalering eller warp. Lokale native imagegen-rettinger bare for reelle arvede motivavvik, uten å endre fryste donorfiler. Kontroller alle 33 cels, de to skjøtene særskilt, rel-lagplassering og uendrede kilder. Runtime og ny individuell brukergodkjenning forblir false.

| Jobb | Cel | Lag | Rel | Donor | HD-målboks |
|---|---:|---:|---|---|---|
| fig325_01 | 385 | 3 | -19,-32 | fig003_01:385 | [80, 48, 192, 168] |
| fig325_01 | 384 | 3 | -15,-32 | fig003_01:384 | [224, 48, 336, 168] |
| fig325_01 | 386 | 3 | -15,-32 | fig003_01:386 | [368, 48, 484, 168] |
| fig325_01 | 513 | 4 | -6,-11 | fig003_01:513 | [80, 200, 136, 208] |
| fig325_01 | 512 | 4 | -8,-11 | fig003_01:512 | [168, 200, 224, 208] |
| fig325_01 | 390 | 3 | -18,-32 | fig003_01:390 | [80, 252, 188, 372] |
| fig325_01 | 392 | 3 | -18,-32 | fig003_01:392 | [220, 252, 328, 372] |
| fig325_01 | 389 | 3 | -18,-32 | fig003_01:389 | [360, 252, 468, 372] |
| fig325_01 | 395 | 3 | -19,-32 | fig003_01:395 | [500, 252, 612, 372] |
| fig325_01 | 397 | 3 | -19,-32 | fig003_01:397 | [644, 252, 756, 372] |
| fig325_01 | 394 | 3 | -19,-32 | fig003_01:394 | [788, 248, 900, 372] |
| fig325_01 | 402 | 3 | -13,-33 | fig003_01:402 | [932, 248, 1036, 372] |
| fig325_01 | 403 | 3 | -13,-33 | fig003_01:403 | [1068, 248, 1172, 372] |
| fig325_01 | 400 | 3 | -13,-33 | fig003_01:400 | [1204, 244, 1308, 372] |
| fig325_01 | 401 | 3 | -13,-33 | fig003_01:401 | [1340, 240, 1444, 372] |
| fig325_01 | 399 | 3 | -13,-33 | fig003_01:399 | [80, 404, 184, 528] |
| fig325_01 | 391 | 3 | -18,-32 | fig003_01:391 | [216, 408, 324, 528] |
| fig325_01 | 406 | 3 | -15,-30 | fig003_02:406 | [80, 572, 192, 684] |
| fig325_01 | 407 | 3 | -15,-30 | fig003_02:407 | [224, 572, 336, 684] |
| fig325_01 | 408 | 3 | -15,-30 | fig003_02:408 | [368, 572, 480, 684] |
| fig325_01 | 413 | 3 | -15,-32 | fig003_02:413 | [512, 564, 624, 684] |
| fig325_01 | 411 | 3 | -15,-32 | fig003_02:411 | [656, 564, 768, 684] |
| fig325_01 | 412 | 3 | -15,-32 | fig003_02:412 | [800, 560, 912, 684] |
| fig325_01 | 415 | 3 | -16,-30 | fig003_02:415 | [944, 572, 1060, 684] |
| fig325_01 | 417 | 3 | -16,-30 | fig003_02:417 | [1092, 564, 1208, 684] |
| fig325_01 | 418 | 3 | -16,-30 | fig003_02:418 | [1240, 572, 1356, 684] |
| fig325_01 | 416 | 3 | -16,-30 | fig003_02:416 | [80, 724, 196, 840] |
| fig325_01 | 419 | 3 | -16,-30 | fig003_02:419 | [228, 728, 344, 840] |
| fig325_01 | 410 | 3 | -15,-32 | fig003_02:410 | [376, 716, 488, 840] |
| fig325_02 | 424 | 3 | -13,-29 | fig003_02:424 | [80, 60, 188, 168] |
| fig325_02 | 423 | 3 | -15,-32 | fig003_01:386 | [220, 48, 336, 168] |
| fig325_02 | 422 | 3 | -14,-30 | fig003_02:422 | [368, 56, 480, 168] |
| fig325_02 | 0 | 0 | -14,-33 | fig005_03:0 | [80, 200, 204, 412] |

Nærbevis for de tre munnavvikene: b-munn395-402-418.png og b-munnbevis.json. Avgrensningene ligger under nesen, med null røde kildepiksler i munnfeltene. De røde HD-feltene skal ikke arves til325. Ingen fryste donorark er endret.
