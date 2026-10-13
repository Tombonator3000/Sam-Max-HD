# Bestilling 11 – kildeplan før produksjon

13. oktober 2026. Kun lesing og denne rapporten. Ingen generering, jobbendring, Git eller global loggendring. Source-faithful-production-reglene er brukt: originalens betydning, tilstand, palett og rare geometri styrer før stil.

## Omfang og dokumenterte rektangler

De neste ti ukryssede jobbene etter rom044 i GRAFIKKLISTE.md er listen nedenfor. Eldre avvik og pågående bestilling 9/10 er ikke del av denne planen. Alle ti referanser er visuelt undersøkt, jobbmetadata er lest, begge deler av rom051 og rom052 er undersøkt. Obj409 ble også undersøkt under kildeplan 10. Romnotater er lest fra origin/main:docs/gpt-romnotater.csv ved 3df35f636f123584e4a8d454871fb9318f995d35.

| Jobb | Faktisk lag og originalrektangel x,y,b,h | Motivrektangel på lerret |
|---|---|---|
| obj409_01 | Rom 44, objekt 409, tilstand 01; 136,0,184,96 i rommet; lokalt utsnitt 0,0,184,96 | 400,320,736,384 |
| rom045 | Soverom, bakgrunn 0,0,320,200 | 128,112,1280,800 |
| rom047 | Menasjeri/scenerom, bakgrunn 0,0,320,200 | 128,112,1280,800 |
| rom048 | VR-rom, bakgrunn 0,0,320,200 | 128,112,1280,800 |
| rom049 | Virtuell verden, bakgrunn 0,0,320,200 | 128,112,1280,800 |
| rom050 | Rengjøringsrobotens hjerne, bakgrunn 0,0,320,200 | 128,112,1280,800 |
| rom051_del1av2 | Hotell ute, 0,0,384,200 av 464×200 | 0,112,1536,800 |
| rom051_del2av2 | Hotell ute, 80,0,384,200 av 464×200 | 0,112,1536,800 |
| rom052_del1av2 | Lobby, 0,0,384,200 av 480×200 | 0,112,1536,800 |
| rom052_del2av2 | Lobby, 96,0,384,200 av 480×200 | 0,112,1536,800 |

Alle leveranselerret er 1536×1024 med RGB128 utenfor motivrektangelet. Rom051 krever master 1856×800, delskift 320 HD-piksler og overlapp 1216×800. Rom052 krever master 1920×800, delskift 384 og overlapp 1152×800. Originaloverlappene er målt byte-identiske. Begge delpar inngår i denne bestillingen; ingen ekstra romdel fra bestilling 12 trengs for masterne. Ingen geometriwarp eller uavhengige overlapp som bare antas like.

## Motiv og viktige kildepresiseringer

**Obj409 – separat Edutainment-skilt.** Referansen viser et stort hengende, brunrammet lysskilt med buet topp, røde/gule bokstaver og lysprikker, komposittlagt over troférommets bakgrunn. Den synlige teksten er EDUTAINMENT. Det generiske romnotatet om EDU...MENT og blank dekkplate stemmer ikke med dette objektets referanse: her er ingen blank plate over midten. Bevar de synlige bokstavformene og deres røde/gule fargefelt, ikke sett inn plate eller tre prikker. Toppen har fargede trekantfelt, to lange oppheng og kantlys som må telles fra kilden. Bakgrunn som ses rundt skiltet er romkontekst, ikke tillatelse til å flytte skiltet eller gjøre hele bildet til et ugjennomsiktig nytt romlag. Alfamaskeruten er ikke runtime-verifisert.

**Rom045 – monstertruck-seng.** Romnotatet bekrefter MA TRUK på skiltet. Den store røde truckformen er sengemøbel med store svarte/grå hjul, frontlykter/grill, hvit seng/pillow-form med grønt merke og en bratt grå trapp opp på høyre side. Bevar rødt teppe, trepanel, bokhylle/dør til venstre, bueåpning og liten beholder til høyre, spotlys og avklipte cowboyhatter i forgrunnen. Ikke gjør sengen til en vanlig kjørende bil eller legg en sovende person i den. Små bokrygger og merket på sengetøyet er former, ikke gjettet lesbar tekst.

**Rom047 – Bumpusville Sings.** Teksten BUMPUSVILLE SINGS er bekreftet. Tom grønn scene med skjev kant og lysprikker, rosa gardiner, mikrofoner, dyrehoder rundt scenen, høyttaler-/lysdetaljer og en åpen dør til høyre. Romnotatet sier at spillet animerer dyrehodenes øyne og munner; bakgrunnens konkrete tilstand og antall skal beholdes. Ikke gi dem nye arter/uttrykk, tenner eller ekstra øyne fra generisk dyrekunnskap. Bevar tom scene, mørke hull mellom hodene og skjeve gulvlys; ingen musikere eller publikum legges til. Eksakte artsnavn er ikke bevist av denne analysen.

**Rom048 – tom VR-kabin.** Et rundt, grønt opplyst gardinomsluttet felt med hengende svart/grønt VR-utstyr, ikke en person eller et akvarium. Rød sofa ved vinduene, liten brun puff, rødt rundt teppe, bokhyller, skjeve rammer, åpen dør og mørk vase på bord foran. Bevar grønn lysretning og tomt kabinfelt; ikke tegn bruker, avatar, hender, knapper eller ny skjermtekst som ikke finnes i referansen.

**Rom049 – bevisst flat polygonverden.** Romnotatet gir et uttrykkelig unntak fra vanlig malerisk HD-stil: flate, uteksturerte polygoner med skarpe kanter. Grønt fasettert landskap, lilla/mørk huleåpning, fjell, lilla borg mot magenta himmel, brune grunnflater og gult sverd i grå stein. Ikke glatt fasettene, legg gress/steintekstur, volumlys eller realistisk himmel på dem. Godkjente maleriske stilankere må ikke overstyre dette. Bevar sverdet og alle polygonhjørner på kildekoordinater; ingen ny avatar eller drage.

**Rom050 – rengjøringsrobotens hjerne og Bumpusville-plantegning.** Primærkilden er LucasArts-hintboka, trykt side 23: https://mocagh.org/lucasfilm/sammax-hintbook.pdf. Root har undersøkt kilden og bekrefter cleaning robot, robot brain og ledningsforbindelsen til venstre rom i plantegningen. Tidligere VR-maskin-identifikasjon var misvisende; VR-systemet inngår i en separat gåterelasjon. Dokumentert gåtebilde. Rosa hjerne i åpen grå maskin/skuff med grønn kant, rød ytre ramme, blå skjerm med BUMPUSVILLE og sammenhengende grønne blokkformer. Fem fargekodede kontakter er synlige i hjernen (blå, grønn, gul, grå/blålig og oransje), med tilsvarende fargede ender på skinnen over. Bevar antall, rekkefølge, forbindelse/avkoblet tilstand, kabler og skjermblokkenes topologi; ikke løs gåten visuelt eller koble til nye ledninger. Ingen ansiktstrekk i hjernen. Eksakt elektrisk funksjon og interaksjonssekvens er ikke testet.

**Rom051 – Savage Jungle Inn ute.** Kopier SAVAGE / JUNGLE / INN og WELCOME / PODIATRALLY / GIFTED, med kildens radbrudd og perspektiv. Stor grønn øgleform rundt skiltet med rød tunge, liten dekorativ vulkan med oransje innhold, takbygninger, mørke palmer, bro over blått vann, gress og tre parkerte biler i helscenen: DeSoto samt grå og rød bil mot høyre. Bevar skiltets delvise avkutting oppe, biljaktfri tom plass og den brede kildescenen på 464 originalpiksler. Ikke gjør skiltøglen levende eller legg gjester på broen. Vulkanens funksjon er ikke runtime-verifisert; gjengi det synlige dekorative motivet.

**Rom052 – lobby.** THE / REPTILE / QUEEN på plakaten er bekreftet; behold kvinneskikkelse/slangeillustrasjon og små uleselige tekstfelt uten å gjette krediteringer. Tukan på venstre benk-/diskområde, grønn øgle liggende på svart stein foran, stor grå steinhodeform over hylleskapet, tre-/bambusflater, gardinåpning, små rammer og glassdør mot høyre. Bevar øglens lukkede/hvilende uttrykk og krumme hale, tukanens nebbretning, steinhodets stive form og tomme åpninger. Det oransje mønsteret rundt forgrunnssteinen skal følge kildeform/farge; ikke innfør nye flammer, vannsprut eller mekanikk ut fra gjetning. Ingen resepsjonist tegnes inn.

## Verifikasjonsgrense

Motivnavn fra jobbmetadata/romnotater er dokumenterte; material-/funksjonsbeskrivelser som bare følger av bildet er visuell tolkning. Før produksjon må små bokstaver og antall detaljer sees i lokal 1×/4×-zoom; uleselig tekst forblir tegnformer. Kildens palett er sett i eksportene, mens dynamisk fargesykling, animasjonsutløsere, masker og faktisk motorvisning ikke er undersøkt. Denne planen påstår ingen nye tekniske leveransekontroller eller individuell godkjenning. Senere produksjon trenger ordrette prompter med presiseringer, råforsøk, master/klipp/hash og separat visuell og teknisk QA.
