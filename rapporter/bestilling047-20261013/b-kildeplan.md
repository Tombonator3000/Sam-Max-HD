# Kildeplan for antrekksfamilien 070/071, bestilling 47 til 49

Bare analyse. Omfanget er 21 jobber: ni i47 uten A sin lag068_12, alle ti i48 og lag071_15/16 fra49. Ingen generering eller produksjonsfiler er endret. Alle helscener, elleve objektsider, originalt utvalgsark070, begge49-originaler og levert HD071 er sett. Kildebeviset kontrollerer 108 låsoppføringer i47/48, 104 unike filer, uten avvik. Åtte kildefiler for49 er separat låst i b-049-konteksthash.json, siden root sin49-mappe ennå ikke fantes.

## Geometri og faktisk tilstand

070 er et 480 × 200 panorama. Lag01 og02 krever hver en felles 1920 × 800 master, klipp0/384, overlapp1152 × 800. Begge originalpar er byteidentiske i overlappen. Begge deler skal ha unionen fra begge metadatafiler: lag02del1 inneholder også synlige fraværsfelt fra del2, selv om egen metadata bare nevner pilen. Lag03 har bare del1 i oppdraget, med høyrepilen og ellers riktig grunnrom. Canvas er1536 × 1024, motiv[0,112,1536,800].

071 er320 × 200, canvas1536 × 1024 og motiv[128,112,1280,800]. Sam står til venstre, Max til høyre. Rød/oransje tagget bakgrunn og uendrede kroppsfragmenter skal følge levert grunnrom. Alle21 originaler har null endringer utenfor sin faktiske samlede kildeunion. Tilstandene er selvstendige kombinasjoner, ikke en kumulativ påkledning. Lag07103 skal eksempelvis ikke arve hatt/knapp fra02.

07001 erstatter21 felt med tilsiktede flate grålilla fraværssilhuetter, med enkelte fargede nabofragmenter inne i rektanglene. 07002 har fem andre slike felt og venstrepil. Silhuettformene må nytegnes fra kilden; ingen kopiert originalmaske. Ikke fyll dem med antrekk eller gi dem ansikt/tekst/skyggelegging. Registeret kaller de fleste asd og er ikke en identitetsbeskrivelse. Tabellen nedenfor kobler hver fraværsform til originalt farget grunnrom.

## Tekst og avklaringer før produksjon

LeChuck Pizza er brukeravklart tekst. 07001 fjerner hele esken;07002/03 skal bevare den korrekt merkede HD-grunnromsesken. 07106 har en annen kropp/eske-komposisjon. root-pizza-gjenbruksbevis.json måler3281 ulike originalpiksler og ingen identisk etikettcrop. Bare skrivemåte og tegnstil kan brukes som støtte; hver kropp, hånd, eskevinkel og avklipping følger egen kilde.

PUSH ME på771 er leselig. 01/02-knappene har egne farge-/lysflater og skal ikke dedupliseres. 770 har rødt1¢ og fargede små former, ikke en vanlig hjelm. Ikke skriv ny reklame. Prislappen719 har liten prisdel og EACH-lignende bokstavrekke; eksakte tall er ikke sikkert fastslått her. Behold glyffformene eller innhent roots lesning før tekstnormalisering. Bispelue744 har svart tegnform som beholdes uten ny bokstavtolkning.

735 har internt navn sam-sword-image, men bare et kompakt gyllent grep med korsformet topp ses i det lille feltet. Ingen full klingelengde er synlig. Bevar utsnittet uten oppfunnet sverd eller omtolkning til pokal. Dette er meldt root som konkret tolkningsgrense. 716 er synlig prestedrakt selv om navnet sier apron;731 er synlig spade selv om navnet sier cane. Tegn det viste motivet. Ingen øvrig avgjørende identitetsuklarhet funnet; små mønster- og pristegn krever fortsatt kildepresis formkontroll.

## Arbeidsdeling og uavhengighet

07001/02 skal behandles som hver sin helmaster med samlet feltunion. Mange metadatafelt overlapper, og fargede naboer skal ikke slettes. 07003 kan behandles uavhengig fra riktig grunnrom. Hver071-jobb kan tegnes uavhengig, men bør beholde én eier og felles Sam/Max-stil. Innen en jobb må overlappende hånd/kropp/rekvisitt behandles sammen:717+725,718+740,723+728,753/757+763,724+730,755+765,756+766,758+762+769. Rektangeloverlapp er ikke automatisk grafikkoverlapp, men krever samlet kontroll. Full liste med eksakt areal finnes i b-familiebevis.json.

Et generert komponentark kan brukes hvis hver ny komponent og kildefelt spores og bare nye piksler/alfa inngår. Ingen originalkonturmaske eller warp. Hele kropper fra et annet kostyme er ikke en trygg erstatning for et lite felt. Leverte filer skal være opake romkompositter med faktisk uendret HD utenfor union. Runtime og ny individuell godkjenning er ikke utført. Ingen produksjon før root har vurdert planen og tekstspørsmålene.

## Eksakt felttabell

Rektangler oppgis som x,y,bredde,høyde i originalrommet. HD-rektangler er canvas-koordinater og ligger også i b-felttabell.json. Alle objekttilstander er01 bortsett fra771_02. Lagnumrene er desimale, ikke objektets tilstandsnummer.

| Jobb | Objekt | Originalrekt | HD-rekt | Identitet og tilstand |
| --- | --- | --- | --- | --- |
| lag070_01_del1av2 | obj685_01 | [72, 48, 64, 56] | [288, 304, 256, 224] | Grålilla fravær av speiderantrekk |
| lag070_01_del1av2 | obj686_01 | [0, 80, 112, 72] | [0, 432, 448, 288] | Grålilla fravær av rockeantrekk med store piggsko |
| lag070_01_del1av2 | obj687_01 | [136, 24, 104, 72] | [544, 208, 416, 288] | Grålilla fravær av brudekjole |
| lag070_01_del1av2 | obj688_01 | [176, 144, 96, 56] | [704, 688, 384, 224] | Grålilla fravær av vampyrantrekk; rød nabokappe og sølvbladfragment blir stående |
| lag070_01_del1av2 | obj690_01 | [288, 8, 96, 64] | [1152, 144, 384, 256] | Grålilla fravær av pizzabudantrekk OG eske; ingen etikett i denne tilstanden |
| lag070_01_del1av2 | obj692_01 | [216, 40, 104, 80] | [864, 272, 416, 320] | Grålilla fravær av dykkerantrekk |
| lag070_01_del1av2 | obj693_01 | [32, 152, 72, 48] | [128, 720, 288, 192] | Grålilla fravær av utslått lommekniv |
| lag070_01_del1av2 | obj694_01 | [72, 0, 136, 48] | [288, 112, 544, 192] | Grålilla fravær av gitar |
| lag070_01_del1av2 | obj697_01 | [0, 0, 64, 40] | [0, 112, 256, 160] | Grålilla fravær av flaggermus |
| lag070_01_del1av2 | obj700_01 | [0, 152, 32, 48] | [0, 720, 128, 192] | Grålilla fravær av pizzastykke |
| lag070_01_del1av2 | obj701_01 | [128, 112, 48, 56] | [512, 560, 192, 224] | Grålilla fravær av bamse; hvitt slørfragment i nedre venstre kant beholdes |
| lag070_01_del1av2 | obj702_01 | [168, 96, 56, 48] | [672, 496, 224, 192] | Grålilla fravær av vekkerklokke |
| lag070_01_del1av2 | obj703_01 | [288, 64, 80, 56] | [1152, 368, 320, 224] | Grålilla fravær av grønn speiderhatt/hakesnor |
| lag070_01_del1av2 | obj707_01 | [88, 104, 40, 16] | [352, 528, 160, 64] | Grålilla fravær av svart beret |
| lag070_01_del1av2 | obj708_01 | [128, 88, 40, 32] | [512, 464, 160, 128] | Grålilla fravær av rød/gul caps |
| lag070_01_del1av2 | obj709_01 | [16, 40, 56, 40] | [64, 272, 224, 160] | Grålilla fravær av gresskarhode |
| lag070_01_del1av2 | obj710_01 | [240, 0, 48, 40] | [960, 112, 192, 160] | Grålilla fravær av automat/glasshode |
| lag070_01_del2av2 | obj689_01 | [368, 0, 96, 64] | [1088, 112, 384, 256] | Grålilla fravær av matadorantrekk |
| lag070_01_del2av2 | obj691_01 | [328, 136, 104, 64] | [928, 656, 416, 256] | Grålilla fravær av blå/gul pyjamas; nabofragmenter beholdes |
| lag070_01_del2av2 | obj696_01 | [352, 96, 40, 40] | [1024, 496, 160, 160] | Grålilla fravær av bukett |
| lag070_01_del2av2 | obj706_01 | [352, 64, 40, 16] | [1024, 368, 160, 64] | Grålilla fravær av vampyrtenner |
| lag070_02_del1av2 | obj711_01 | [0, 0, 40, 24] | [0, 112, 160, 96] | Rød venstrepil over eksisterende flaggermusfelt |
| lag070_02_del2av2 | obj695_01 | [400, 112, 72, 56] | [1216, 560, 288, 224] | Grålilla fravær av grå høne med løse fjær |
| lag070_02_del2av2 | obj698_01 | [248, 152, 104, 48] | [608, 720, 416, 192] | Grålilla fravær av sverd |
| lag070_02_del2av2 | obj699_01 | [248, 120, 64, 56] | [608, 592, 256, 224] | Grålilla fravær av rød tyrefekterkappe |
| lag070_02_del2av2 | obj704_01 | [384, 56, 80, 64] | [1152, 336, 320, 256] | Grålilla fravær av svart pigghår og ørepynt |
| lag070_02_del2av2 | obj705_01 | [104, 160, 64, 40] | [32, 752, 256, 160] | Grålilla fravær av hvitt slør |
| lag070_03_del1av2 | obj712_01 | [0, 0, 40, 24] | [0, 112, 160, 96] | Rød høyrepil samme sted; ikke speil hele nabofeltet |
| lag071_01 | obj713_01 | [272, 0, 40, 24] | [1216, 112, 160, 96] | Rød høyrepil oppe til høyre |
| lag071_01 | obj714_01 | [0, 0, 40, 24] | [128, 112, 160, 96] | Rød venstrepil oppe til venstre |
| lag071_01 | obj715_01 | [64, 80, 72, 80] | [384, 432, 288, 320] | Sam med hvitt flekket forkle over hvite korte ermer, knyttede bånd og lommeinnhold |
| lag071_01 | obj736_01 | [80, 32, 40, 40] | [448, 240, 160, 160] | Hvit kokkelue på Sam |
| lag071_01 | obj745_01 | [200, 112, 56, 48] | [928, 560, 224, 192] | Max med grønn speiderdrakt, gul halsknute, brun skulderdel og merker |
| lag071_01 | obj767_01 | [208, 80, 40, 24] | [960, 432, 160, 96] | Liten svart beret mellom Max ører |
| lag071_01 | obj771_01 | [152, 64, 32, 32] | [736, 368, 128, 128] | Rund brun/rød PUSH ME-knapp med gul tekst; 01 og02 har forskjellige lys/flater |
| lag071_02 | obj716_01 | [56, 80, 88, 88] | [352, 432, 352, 352] | Sam med hvit lang prestedrakt og gulrammet dekorert stole; registerets apron-navn er feilvisende |
| lag071_02 | obj738_01 | [72, 48, 48, 24] | [416, 304, 192, 96] | Brun filthatt med mørkt bånd på Sam |
| lag071_02 | obj746_01 | [176, 112, 104, 64] | [832, 560, 416, 256] | Max med rød vest, blå bukser og enorme mørke piggsko |
| lag071_02 | obj768_01 | [200, 72, 40, 24] | [928, 400, 160, 96] | Rød/gul caps på Max, egen vinklet brem |
| lag071_02 | obj771_02 | [152, 64, 32, 32] | [736, 368, 128, 128] | Rund brun/rød PUSH ME-knapp med gul tekst; 01 og02 har forskjellige lys/flater |
| lag071_03 | obj717_01 | [64, 80, 88, 96] | [384, 432, 352, 384] | Sam i grønn flekket operasjonsdrakt med stetoskop og grønne føtter |
| lag071_03 | obj725_01 | [128, 72, 48, 64] | [640, 400, 192, 256] | Sams hånd holder gaffel med flammende rødbrun pølse; små dråper beholdes |
| lag071_03 | obj739_01 | [80, 56, 40, 16] | [448, 336, 160, 64] | Mørke grønne solbriller på Sam |
| lag071_03 | obj747_01 | [176, 104, 104, 72] | [832, 528, 416, 288] | Max med hvit brudekjole og puffede skuldre |
| lag071_04 | obj718_01 | [48, 72, 104, 104] | [320, 400, 416, 416] | Sam i brun slitt frakk, rød halsduk, lys skjorte, blå bukser og oppbrettede støvler |
| lag071_04 | obj740_01 | [56, 40, 80, 40] | [352, 272, 320, 160] | Brun cowboyhatt med gjennomgående pil; behold begge pilender |
| lag071_04 | obj748_01 | [184, 112, 96, 48] | [864, 560, 384, 192] | Max med svart/rød vampyrdrakt, hvit krage og gul kant |
| lag071_05 | obj719_01 | [48, 80, 96, 88] | [320, 432, 384, 352] | Sam i blågrå lang frakk med hengende salgsbrett, to mørke krus/briller og gul prislapp; små prisglyfer ikke sikkert lest |
| lag071_05 | obj741_01 | [72, 32, 56, 32] | [416, 240, 224, 128] | Høy blå/lilla flosshatt med lilla bånd |
| lag071_05 | obj749_01 | [184, 112, 96, 56] | [864, 560, 384, 224] | Max med rød/gul matadordrakt, hvite strømper og svarte sko |
| lag071_06 | obj720_01 | [48, 80, 104, 96] | [320, 432, 416, 384] | Sam i gul/grønn westernskjorte, stor beltespenne, blå bukser og brune støvler |
| lag071_06 | obj742_01 | [72, 40, 40, 32] | [416, 272, 160, 128] | Rød/hvit nattlue med hengende ende |
| lag071_06 | obj750_01 | [200, 104, 96, 64] | [928, 528, 384, 256] | Max i svart pizzabudantrekk med hvit krage og egen eske merket LeChuck Pizza; ikke kopier hele070felt |
| lag071_07 | obj721_01 | [48, 80, 96, 80] | [320, 432, 384, 320] | Sam i blågrå smoking, hvitt bryst og lilla magebelte; røde flekker beholdes |
| lag071_07 | obj743_01 | [72, 40, 56, 40] | [416, 272, 224, 160] | Gule spisse hårtuster og mørke solbriller |
| lag071_07 | obj751_01 | [176, 112, 104, 64] | [832, 560, 416, 256] | Max med blå pyjamas og gule smileansikter, spisse føtter |
| lag071_08 | obj722_01 | [48, 80, 104, 96] | [320, 432, 416, 384] | Sam i rød/hvit stripet nattdrakt og store lyse tøfler |
| lag071_08 | obj744_01 | [80, 24, 40, 48] | [448, 208, 160, 192] | Hvit spiss bispelue med gul kant og svart indre tegnform; ikke gjett ny tekst |
| lag071_08 | obj752_01 | [184, 88, 96, 80] | [864, 464, 384, 320] | Max med mørk blå dykkerdrakt, maske, munnstykke/slanger, grå kniv og svømmeføtter |
| lag071_09 | obj723_01 | [24, 48, 120, 128] | [224, 304, 480, 512] | Sam med svart/rød/gul surfebrett, gul/lilla shorts og sandaler; naboskjegget overlapper |
| lag071_09 | obj728_01 | [80, 64, 56, 40] | [448, 368, 224, 160] | Hvitt skjegg og bart på Sam, egen kontur over snute |
| lag071_09 | obj753_01 | [232, 120, 72, 40] | [1056, 592, 288, 160] | Max holder rød utslått flerfunksjonskniv med separate blader/verktøy |
| lag071_09 | obj757_01 | [168, 104, 56, 40] | [800, 528, 224, 160] | Max holder mørk flaggermus med utstrakte vinger, rødt ansikt og spisse ører |
| lag071_09 | obj763_01 | [192, 80, 72, 56] | [896, 432, 288, 224] | Max med bred grønn speiderhatt og hakesnor |
| lag071_10 | obj724_01 | [56, 80, 88, 80] | [352, 432, 352, 320] | Sam med grønn/oransje tatoveringsmønstre over bar overkropp, gullkjede og mørk bukse med hodeskallespenn |
| lag071_10 | obj730_01 | [120, 112, 40, 64] | [608, 560, 160, 256] | Sams hånd holder kort svart stokk med blått toppgrep |
| lag071_10 | obj754_01 | [192, 112, 128, 48] | [896, 560, 512, 192] | Max holder rød/gul elektrisk gitar med mørk hals og spisse kanter |
| lag071_11 | obj726_01 | [112, 104, 48, 56] | [576, 528, 192, 224] | Sams grønnlige hanske holder blodmerket håndsag |
| lag071_11 | obj727_01 | [40, 112, 40, 56] | [288, 560, 160, 224] | Sams hånd holder løs grå hodeskalle med mørke punkter under |
| lag071_11 | obj734_01 | [80, 80, 40, 24] | [448, 432, 160, 96] | Gullmedalje på svart/gul snor rundt Sams hals |
| lag071_11 | obj755_01 | [216, 112, 72, 56] | [992, 560, 288, 224] | Max holder grå høne med oransje nebb/føtter og separate fjær |
| lag071_11 | obj759_01 | [160, 120, 56, 56] | [768, 592, 224, 224] | Max holder rød tyrefekterkappe med hull og gul kant |
| lag071_11 | obj765_01 | [192, 80, 64, 40] | [896, 432, 256, 160] | Hvitt slør over Max ansikt, grå folder og bølget kant |
| lag071_12 | obj729_01 | [104, 104, 56, 56] | [544, 528, 224, 224] | Sams hånd holder brennjern med gul S-form nedover; ikke erstatt med sverd |
| lag071_12 | obj733_01 | [40, 104, 40, 56] | [288, 528, 160, 224] | Sams hånd med rød/hvit tannkremtube og hvit utpresset tannkrem |
| lag071_12 | obj737_01 | [80, 48, 48, 40] | [448, 304, 192, 160] | Grønn operasjonshette OG munnbind på Sam |
| lag071_12 | obj756_01 | [232, 112, 48, 40] | [1056, 560, 192, 160] | Max holder rosa/rød bukett med grønne detaljer |
| lag071_12 | obj760_01 | [184, 120, 32, 40] | [864, 592, 128, 160] | Max holder gul/oransje pizzatrekant med mørke runde fyllfelt og hengende ost |
| lag071_12 | obj766_01 | [208, 104, 40, 16] | [960, 528, 160, 64] | Max egen vampyrmunn med to lange lyse hoggtenner |
| lag071_13 | obj731_01 | [120, 64, 40, 112] | [608, 368, 160, 448] | Sams hånd holder spade med langt brunt skaft og grått blad; registerets cane-navn er feilvisende |
| lag071_13 | obj758_01 | [176, 120, 96, 48] | [832, 592, 384, 192] | Max holder langt sølvsverd med gyllent grep; overlapper klokkeområdet |
| lag071_13 | obj762_01 | [176, 112, 48, 40] | [832, 560, 192, 160] | Max holder gul/grønn vekkerklokke med svart/hvit urskive og separate små punkter under |
| lag071_13 | obj769_01 | [208, 80, 48, 40] | [960, 432, 192, 160] | Oransje gresskarhode rundt Max ansikt med grønn stilk; ører synlige |
| lag071_14 | obj732_01 | [120, 104, 40, 48] | [608, 528, 160, 192] | Sams hånd med blå tannbørste og lys bust |
| lag071_14 | obj761_01 | [224, 104, 48, 56] | [1024, 528, 192, 224] | Max holder brun bamse med rosa poter og gul sløyfe |
| lag071_15 | obj735_01 | [128, 96, 32, 40] | [640, 496, 128, 160] | Kompakt gullfarget håndholdt grep med korsformet topp i Sams hånd; register sam-sword-image, bare kildeavklippet skal tegnes |
| lag071_15 | obj764_01 | [192, 64, 72, 64] | [896, 368, 288, 256] | Max med svart pigghår og gul ørepynt; ører blir stående |
| lag071_16 | obj770_01 | [208, 88, 40, 32] | [960, 464, 160, 128] | Automat-/glasspreget hode over Max ansikt med rødt 1¢ og små fargede felt; originalnavn bubblegumhead |

Kilder: root-feltbevis/root-mikrobevis/root-lagbevis i47/48, konsept/2026-10-12/objektbilder-959.csv, alle faktiske jobb.json/original_1x/referansebilder, rom070-originaler og rom071-HD. Oppskrift og numerisk kontroll: b-familieanalyse.py.txt og b-familiebevis.json.
