# Bestilling 8, kildeplan før produksjon

Dato: 2026-10-13. Kun kildeanalyse. Ingen bilder, jobbmetadata, originaler eller prompter er endret. Ingen generering, teknisk leveransekontroll eller runtime-test er utført i denne planen. Runtime = false; nybildegodkjenning = false.

## Omfang og kilder

De neste ti jobbene i GRAFIKKLISTE.md er obj304_01, obj307_01, obj308_01, rom032_del1av2, rom032_del2av2, rom033, rom034, rom035_del1av2, rom035_del2av2 og rom036_del1av2. rom036_del2av2 står først i neste gruppe, men må med som originalgrunnlag allerede nå.

Visuelt inspisert: de ti referansebildene, rom036_del2av2/referanse.png og rom031_del1av4/referanse.png. Lest: tilhørende jobb.json, originalprompter, BESTILLING.md, ANALYSE.md og GRAFIKKLISTE.md. Originaldelers overlapp er sammenlignet som RGB-byteverdier i minnet uten å skrive bilder. Ekstern kilde i repoet: origin/main ved 3df35f636f123584e4a8d454871fb9318f995d35, særlig docs/rom-oversikt.csv, docs/gpt-romnotater.csv og pipeline/smhd/gpt.py. Sistnevnte dokumenterer at store objektjobbers referanse er objektet komposittlagt over rommet: gjennomsiktige deler viser bakgrunnen (linje 11–14 og funksjonen ved linje 271–275). Dette er avgjørende for kikkertens åpning.

## Kikkertrommet: tre sammenhengende deler, én oppgitt tilstand

Alle tre metadata sier rom 31, romstørrelse 1104×200, tilstand 01. De er forskjellige objekt-ID-er og utfyller samlet venstre 320×200 av rommet; de er ikke tre alternative helbilder eller en dokumentert animasjonssekvens.

| Jobb | Objektets originalrektangel i rommet x,y,b,h | Motivfelt på leveranselerret |
|---|---|---|
| obj307_01 | 0,0,320,40 | 128,432,1280,160 |
| obj304_01 | 0,40,320,88 | 128,336,1280,352 |
| obj308_01 | 0,128,320,72 | 128,368,1280,288 |

obj307: øvre lilla/grå kikkertkapsling med to mørke skruehoder, blå himmel på sidene og svart åpning under. Ikke tegn et nytt komplett apparat i stripen.

obj304: midtre kapsling, svart dobbelbuet synsåpning og to brune hender langs ytterkantene. Landskapet i åpningen er grønne åkre/høyder, barskog, lys vei, blå himmel og et lite eksisterende skilt. Samme landskap finnes i rom031-bakgrunnen: det er gjennomlysende romkontekst, ikke en ny illustrasjon på apparatet. Ikke legg til landemerker eller lesbar tekst på det vesle skiltet.

obj308: nedre kapsling med 25¢-merking, loddrett myntsliss, sentral spak på en vifteformet skala, fire lyse skruehoder og en svart rektangulær åpning avklipt nederst. Lyseblå ermer og hvite mansjetter på sidene fortsetter hendene i midtfeltet. Farge/klær støtter at dette er Sams førstepersonshender, men kildefilene her navngir ikke eieren direkte. Det trengs ingen oppdiktet kropp/ansikt for å gjengi utsnittet riktig.

Produksjonsplan: sett de tre originalfeltene sammen i rekkefølgen 307→304→308 til ett 320×200 motiv (1280×800 HD). Bruk én felles nytegnet master, og klipp y=0..160, 160..512 og 512..800 til de respektive leveransefeltene. Bevar panelkanter, hendekontakter og skrueplassering over skjøtene. Gjengi synlig romkontekst trofast i jobbreferansen, men ikke behandle dette som bevis for at sluttobjektets åpning skal være ugjennomsiktig. Eksakt alfamaskerute/import og panoramabevegelse må kontrolleres separat i integrasjonen; planen har ikke åpnet originale RGBA-objektfiler eller kjørt spillet. Nytegnet rom031-HD med egenkontroll OK, uten individuell ny brukergodkjenning, kan brukes som konsistensreferanse ved produksjon, aldri som erstatning for originalens form.

## Rom 32–34: hyssingnøstet og bevisst tomme områder

rom032 er fiskedekket på toppen av nøstet, 480×200. Delene starter x=0 og 96 og er hver 384×200. Bevar den enorme beige/brune hyssingflaten foran, de parallelle buede trådene, metallstøtter, gjerder, lille bod med rødt tak/dør og fiskeskilt, mørkt servicevindu, små beholdere til venstre, rødhvit stang, oransje taubanevogn med kabel til høyre, og den avklipte mørke undersiden av restauranten/akselen øverst. Himmelen og skyene er rolige flater. Ingen nye personer, fiskeutstyr eller operatør i taubanen. Romnotatet bekrefter fisk, stang, taubane og rekkverk. Senere lag032_01..04 dokumenterer at objektbilder kommer separat; ikke fyll disse plassene med nytt innhold.

rom033 er toppen av nøstet fra lavere/nærmere vinkel, 320×200. Bevar den store trådmassen og den løse tråden som bøyer ned foran, bod/fiskeskilt/rød dør og rekkverk øverst, sentral grå aksel og svart restaurantunderside. Ikke legg gjester på den tomme plattformen. lag033_01 har to separate objektbilder. Motivfelt 128,112,1280,800 på 1536×1024.

rom034 er hyssingtråd i nærbilde, 320×200, ikke slange, ledning eller treplanker. En tykk tvunnet tråd kommer ovenfra venstre, bøyer nedover og ender frynset/todelt nær nedre midt. Bakgrunnen er lag av tettliggende parallelle tråder i ulike retninger, med mørke mellomrom. Bevar kildeantall trådforløp og hele den uvanlige kurven. Ikke legg til hånd, saks, ansikt, ekstra knuter eller dekor. Motivfelt 128,112,1280,800.

## World of Fish, rom 35

480×200; to deler x=0/96. Venstre del viser den kolossale grønne fisken med rød utstikkende munndetalj, krummet kropp/hale, lite fiskeskilt ved stien, sjøkant og stolpe i vannet. Midten har en skjev trekiosk formet rundt et tannbesatt fiskegap, takbokstavene BAIT, skiltet FISH FEED, en mindre uleselig skriftlinje, livbøye og to bøtter. Foran ligger et grunt brunt basseng med grønt innhold og slange, og til høyre et kantet glasskar med stor grønn fisk. Bak er fiskeskiltet WORLD of FISH; høyre del kompletterer den parkerte svart/hvite bilen og blå/grå fiskeformede varebilen med grønt fiskemotiv på taket. Bevar vannflatens mørke grønne og blå bånd, gress, stier, fjell og skog.

Hovedtekst bekreftet av docs/gpt-romnotater.csv: BAIT, WORLD of FISH, FISH FEED. Bevar bokstavenes form/plassering, også buet tekst på fiskeskiltet. Den lille linjen under FISH FEED og lite skilt ved stien skal følge synlige former, ikke oppdiktes. Fisken i glasskaret er et stort særpreget motiv; ikke gjør den til en ny tilfeldig fisk. Ingen ekspeditør i det tomme kioskvinduet, ingen nye besøkende. Senere lag035_01/02 inneholder separate objekter. Risiko: å normalisere fiskearkitekturen, rydde tennene eller erstatte bilene med generiske moderne kjøretøy.

## Mystery Vortex, rom 36, begge deler nødvendig

480×200. Lag fullmaster fra del1 OG del2 nå. Del1 viser svart solskive med taggete gul glød i oransje/rød himmel, skjeve svarte bartrær med lilla vridde stammer, delvis nedgravd/skjevt parkert bil, bølgende rød/oransje bakke og stolper med lilla tau. Del2 kompletterer den voldsomme grå/lilla klippeveggen, mørke inngangen, hele MYSTERY VORTEX-skiltet, det store deformerte klokkelignende skivefeltet og den tynne loddrette snor-/pendeldetaljen til høyre. Alle disse rare vinklene og fargene er tilsiktet, uttrykkelig bekreftet av romnotatet.

Ikke rett opp skilt, bil, trær, stolper eller vegger. Ikke omtolk den svarte solen som tomt hull som trenger fyll. Bevar den mørke inngangen og flate bakkeområder uten ekstra figurer. Små symboler i klokkelignende felt skal følge originalformen; ikke innfør normale klokketall eller ny mekanikk. Senere lag036_01..06 har egne objektbilder.

## Fellesmaster, klipp og kontroll

For rom032, rom035 og rom036: fullmotiv 1920×800, eventuelt på 1920×1024 med y=112 og grå padding. Leveranse del1 = x[0,1536), del2 = x[384,1920); begge hele høyden 1024. Motiv i hver leveranse er [0,112,1536,800]. Felles overlapp er 1152 HD-piksler og skal være byte-identisk, ikke bare visuelt lik. Sammenligning av original_1x.png bekrefter identisk overlapp 288×200 i alle tre rompar. Lagre én master per rom og bind begge deler til SHA256 og eksplisitt klippeoppskrift. Ingen geometrisk warp, lokal konturmaskering eller uavhengige genereringer som antas å være sømløse.

rom036_del2av2 leveres først i neste gruppe, men originalen må inngå i kildehashlisten nå. Hele masteren inkludert høyre region må vurderes før del1 låses; ellers risikerer neste gruppe å kreve omtegning av allerede levert fellesfelt.

Ekstra kilder som skal låses, faktiske SHA256 lest nå:
- jobber/rom036_del2av2/original_1x.png: 2c561ce047b450181014240a4e7022d7b1f47d9c27cb0dba8e3ab4d128d4ee9f
- jobber/rom036_del2av2/referanse.png: bc5a3098989791ddfe5493e40b936036bd212d06ea1190067c72094ab9b18f1c
- jobber/rom036_del2av2/prompt.txt: e0ca25eb64ef7debcfe0fd11d003899e649271065c447a0e55e81667cb809a1e
- jobber/rom036_del2av2/jobb.json: b2c7923166df4b97c81d331960b19138a393ea834e6b4ed9578e472f2faecc02

Ved produksjon: originalprompt ordrett med kildepresisering, innebygd imagegen og godkjente stilankere. Bevar råforsøk, master, prompt og presis klippeoppskrift. Se både normalisert helscene og detaljer; kontroller tekst, semantisk identitet, tomme flater, antall og sømmer før uendret sjekk_leveranse.py. Teknisk OK skal ikke omtales som runtime- eller menneskelig bildegodkjenning.
