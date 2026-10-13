# Kildeplan for bestilling 18

Dato: 2026-10-13. Dette er kildeanalyse før produksjon. Ingen nye bilder er laget. Alle ti originaler er undersøkt visuelt i originalkontaktarket og de ni objektoriginalene også enkeltvis. Jobbmetadata, promptenes motivnoter og ressursregisteret `konsept/2026-10-12/objektbilder-959.csv` er lest. Alle 40 beskyttede filer stemmer med `kildehash.json` ved avslutning. GRUNNLAG foreligger ennå ikke.

## Canvas, lag og klipp

Alle leveranser skal være 1536 × 1024 med uendret nøytral padding. Rektangler oppgis som x, y, bredde, høyde i HD-piksler.

| Jobb | Original | Motivfelt på canvas | Ressursens plass i rommet |
| --- | --- | --- | --- |
| rom077_del2av2 | 384 × 200 | [0,112,1536,800] | region [256,0,384,200] |
| obj774/775/776/777/780_01 | 320 × 72 hver | [128,368,1280,288] | [0,0,320,72] |
| obj781_01 | 320 × 72 | [128,368,1280,288] | [320,112,320,72] |
| obj811_01 | 320 × 88 | [128,336,1280,352] | [0,40,320,88] |
| obj812_01 | 320 × 40 | [128,432,1280,160] | [0,0,320,40] |
| obj813_01 | 320 × 72 | [128,368,1280,288] | [0,128,320,72] |

Alle objektene er registrert som SMAP, tilstand 01. Felles romnavn er ikke tilstrekkelig til å bestemme motiv eller motoroppførsel.

## Rom077 del2

Denne delen skal klippes fra C sin kommende låste master i bestilling 17, ikke genereres separat. Fullrommet er 640 × 200, HD-master 2560 × 800. Delskift 1024 og overlapp 512 × 800; del2 er masterens x[1024,2560). C-manifestet fantes ikke ved denne kontrollen. Før klipp må faktisk master-SHA, proveniens, del1-overlapp og uendret checker kontrolleres.

Del2 inneholder et mørkt perspektivveifelt ved lokal originalposisjon [64,67,320,66], ellers svart. Det gir felt [256,380,1280,264] på leveransecanvas. Kilden har bare svart, grå 23/39/55/71 og rød (207,0,0). Bevar røde vannrette randlinjer, lave horisontformer og midtmarkeringer. Ingen bil, rulletekst eller navn finnes i dette bakgrunnslaget. Promptens generiske «Credit panels» må presiseres med faktisk veifelt og tomrom. Se også bestilling 17 sin a-kildeplan.

## Seks selvstendige grå kredittillustrasjoner

Registeret identifiserer 774,775,776,777,780,781 som credit-panel-1 til 6. Dette er seks forskjellige komposisjoner, ikke deler av ett panorama. Ingen av dem har lesbar kreditttekst. Bevar gråtoner, mørke felt, hver figurstilling og den konkrete innrammingen. Hovedark kan støtte identitet, men normale pels-, klær- og bakgrunnsfarger skal ikke importeres. Ingen neonlys eller fargelegging.

* 774: Max med lange ører og åpent tannglis til venstre/midt, Sam med hatt og snute til høyre; utstrakte hender, bøyde armer og ben foran skarpt svart/grått stjerneutslag. Ikke bytt plass på figurene eller normaliser lemmenes tegneseriepositur.
* 775: nattlig gate med bygning/lykt til venstre, lav bil, Sam som mørk hatt-/frakksilhuett mot høyre og Max med lange ører lengst til høyre. Stjerner og månesigd bak dem. Bevar skrå svarte sideflater og de svært mørke figurene; ikke legg til lyse ansikter.
* 776: bysilhuett med mange vindusrekker, skybånd og rund lysskive med langøret mørk figurform. Max står med ryggen mot utsikten i nedre midtparti og Sam med hatt til høyre. Ikke gjør figurformen i lysskiven til skrift eller en ny fullfigur på himmelen.
* 777: nærbilde gjennom åpen bil med diagonale vindusrammer, Sam bak rattet til venstre/midt og Max foran til høyre, med ørene strukket bakover. Bevar tannrekken, håndgrep og alle overlapp mellom ramme, figurer og bilinteriør. Ikke lag en ny bilvinkel.
* 780: dynamisk sammenstøtkomposisjon, Max midt/venstre, Sam til høyre, store hender/føtter, buede bevegelsesstreker, stjerner og runde småformer til venstre. Småformenes eksakte fortellingsbetydning er ikke bevist; behold formene uten å oppfinne navngitte rekvisitter eller nye ansikter.
* 781: skrå by-/bilkomposisjon til venstre, Max nær midten og svært stort Sam-hode med hatt/snute/tenner i høyre forgrunn. Bevar skrå perspektivlinjer, klipping og størrelsesforskjellene. Ikke lysne panelet til et vanlig dagslysbilde.

Målte originalpaletter er rent grå, R=G=B i alle piksler. Antall unike toner og min/maks: 774 17/0–99; 775 17/0–107; 776 19/0–131; 777 17/0–99; 780 17/0–99; 781 22/11–147. Dermed har 781 ingen absolutt svart piksel i originalen. En felles automatisk kontraststrekking ville endre tilsiktede forskjeller. Tallene er kildebeskrivelse, ikke krav om at nytegning skal være kvantisert til samme palett.

## Kikkertstriper 811,812,813

Navnene er mag-viewer-scope, mag-viewer-top-scope og mag-viewer-bot-scope, rom078. De danner et fullt 320 × 200-panel i rekkefølgen topp812 y[0,40), midt811 y[40,128), bunn813 y[128,200). Ny master kan være 1280 × 800. HD-klipp blir henholdsvis y[0,160), [160,512), [512,800). Klipp skal rekonstruere masteren byte-identisk; det er ingen overlapp mellom stripene.

Apparatet er grålilla med lys blå bakgrunn, brune avkuttede hender i midten og lyse mansjetter/blå ermer nederst. Den store synsåpningen er svart og tom. En tydelig rød/gul ring følger åpningen, med lyse bånd/fester over øvre del. Bevar alle ringbrudd, båndvinkler, metallformer og skruer. Nederst står 25¢ ved myntslissen, ved siden av spak og vifteformet skala; svart åpning klippes i underkant. Ingen landskapsutsikt eller ny tekst skal legges i det svarte feltet. Navneprefikset «mag» beviser ikke alene en bestemt skripthendelse eller skjult rekvisittfunksjon.

Direkte sammenligning med bestilling 8 er utført på filbytes og dekodede RGBA-piksler. Ingen av de tre parene er identiske:

| Eldre → nye | Ulike piksler | Hele feltet |
| --- | ---: | ---: |
| 304 → 811 | 16 855 | 28 160 |
| 307 → 812 | 7 609 | 12 800 |
| 308 → 813 | 1 490 | 23 040 |

304 har landskapsutsikt der 811 er svart med ring. 307 mangler den nye ring-/båndkonstruksjonen. 813 har ringrest ved toppen som ikke finnes i 308. Dette er synlige motivavvik, ikke bare ulike PNG-metadata. Gammel fullmaster er derfor ikke grunnlag for direkte gjenbruk. Den gamle topp307 hadde dessuten FEIL med blokkavvik 19,94 i a-kilde-qa fra bestilling 8. FFT-diagnosen friskmelder verken gammel eller ny grafikk. Ny panelproduksjon må vurderes og kontrolleres selvstendig.

## Forbehold før produksjon

Alle ti jobbmetadata har sha256_prompt som avviker fra nåværende promptbytes. Dette er observert metadataavvik; årsaken er ikke undersøkt her. Bruk dagens låste promptbytes ordrett med separat kildepresisering og la beskyttede filer stå urørt. Tidligere historikkbevis for andre batcher kan ikke alene bevise historikken for disse ti.

Originalene viser komposittlag, men ingen runtime, transparensmaske, skriptstyrt plassering, kredittrekkefølge eller palettbytte er testet. Objektplassering i metadata er ikke en animasjonsplan. Semantisk og visuell QA må kontrollere gråpanelenes individuelle identitet, mørkhet og overlappende lemmer, samt kikkertens tomme åpning, ring, bånd, 25¢ og sammensettingsgrenser. Teknisk kontroll, runtime og ny individuell brukergodkjenning forblir separate tilstander.
