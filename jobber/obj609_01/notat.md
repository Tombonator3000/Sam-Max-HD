# Leveransenotat

To omtegningsforsøk. Første resultat FEIL, råforsøk bevart. Gjeldende SJEKK: skift 0.97, blokk 1.98, kantlikhet 0.94. Stripeenden og veikant har små lokale avvik. Ikke kalt teknisk OK. Innebygd ChatGPT imagegen; eksakt bildemodell er ikke eksponert. Ordrett jobbprompt med separat lagpresisering.

Kilde er et lavt Highway Surfing-veisegment, ikke HUD eller skilt. Ulike sidevinkler og den ene gulstripen er bevart uten biler, tekst eller nye markører. Genererte mørke felt har svake tonevariasjoner; de er motiv og ikke transparens.

Canvas 1536 × 1024, motivfelt [240, 464, 1056, 96], eksakt RGB 128-padding. Kun helskalering og rektangulær plassering. Ingen vektortrace, originalsilhouette eller lokal warp.

Egenkontroll: SJEKK. Resultat SHA256: 4aef30307991ca6282d71b853a50e81d2c5f567ccfeae80122d60b10105bdc72

Låste kildehash: [{"fil": "jobber/obj609_01/referanse.png", "sha256": "3eb0b00ca502ce8292bf256c7a2e7f678c440489e00542ff83b9ec4521242bbe"}, {"fil": "jobber/obj609_01/original_1x.png", "sha256": "01ce82869573092ecfe0707e803b6febc58d9bbf05bdc23baaa94e8e53273530"}, {"fil": "jobber/obj609_01/prompt.txt", "sha256": "22be51eece88fc43c19646db70310a56c8723555e5024e1aac4c7af1d44dfad6"}, {"fil": "jobber/obj609_01/jobb.json", "sha256": "9866cc84a7b96b5cc44b41430e794f81280466d52909e45223be94579ea145c7"}]

Runtime: false. Ny individuell brukergodkjenning: false. Se b-kilde-qa.md og b-familie.png.


Avgrenset lokalforsøk 3: imagegen ble bedt om å korte inn stripen med originalen som kilde. Et fast rektangel [730,464,45,52] ble satt inn i en diagnostisk kandidat; alt utenfor ble verifisert byte-identisk. Uendret checker ga fortsatt SJEKK, blokk 1.98. Gulområdet endte fortsatt på y507 mot originalens y503 (inklusive), og flyttet seg ett HD-piksel til høyre. Lengdeavviket ble dermed ikke rettet. Forsøk 2 beholdes som beste leveranse, SHA uendret. Forsøk 3 og kontroll er bevart, men ikke brukt. Ingen warp eller originalkonturmaske.


## Komponentretting av gul stripe
Generert stripe er alfasegmentert fra tidligere valgt HD, helskalert fra [500, 0, 525, 45] til [500, 0, 524, 40] i lokale HD-koordinater. Nytt imagegen-underlag fjerner tidligere stripe. Ingen originalkonturmaske eller lokal geometriwarp. Endret lerretsboks [738, 464, 767, 511]; alle piksler utenfor boksen er byte-identiske. Veikanter og øvrig vei er uendret. Kontroll: SJEKK. SHA-256: 6113b6c363e13927ba5b95e51740937e2e9746e58b0f1251cbdad68fe63f8fdd. Se rapporter/bestilling015-20261013/c-609-kontroll-etter.txt. Runtime og ny brukergodkjenning er false.

## Endelig presis helkomponentskalering
Root har helskalert den nytegnede veiflaten fra rektangel [10,0,1024,96] til [8,0,1016,96] lokalt, og beholdt den nye gulstripen i [500,0,524,40]. Rent nygenerert underlag fra forrige retting fjerner gammel stripe før skalering. Originalen bidrar bare med målerektangel og kontrollpunkter, ingen bilde- eller konturpiksler. Ingen originalmaske, trace eller lokal warp. 40 kantmålinger: middel absolutt HD-avvik 5.2 til 1.775, maksimum 12 til 5. Små lokale avvik består. Ny uendret kontroll OK 0.14 / 0.52 / 0.98. Endelig SHA256: f7776c25709e9e3e2402871aa691b8769d2aeab0fa6450fbdc334bed28d84d7e. Se root-609-overstyring.json og root-609-veikomponent-bevis.json i bestilling015-rapporten. Tidligere SJEKK-avsnitt beskriver bevarte tidligere kandidater. Runtime og ny individuell godkjenning er fortsatt false.
