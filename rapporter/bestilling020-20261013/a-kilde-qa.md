# Produksjons-QA for bestilling 20 A

Les a-kildeplan.md for kildeidentitet, metadata, palett, laggrenser og usikkerhet. Kun rom083, obj832_01 og rom085 er produsert av A. Kilder, originalprompter og metadata er uendret. Innebygd imagegen er brukt; eksakt modellnavn er ikke eksponert.

## Forsøk og valg

Rom 083: to genereringer fra originalreferansen. Forsøk 1 fikk SJEKK med globalt skift 0,30, blokk 1,29 og kant 0,97. Skyene var mer hvite og blåfargen mer mettet enn originalen. Forsøk 2 presiserte den dempede kildepaletten og mindre intern detalj. Dette er valgt som mer kildenært, men beholder SJEKK som rapportert i a-rom083-kontroll.txt. Det store tomme himmelfeltet og alle hovedskyer er bevart. Ingen figurgruppe, port, tekst eller gulv er lagt til. Skyenes malte modellering er fortsatt mer markert enn originalens åtte flate farger; dette er synlig i samlet QA og ikke skjult av teknisk status.

Obj 832: tre separate genereringer fra originalreferansen. Forsøk 1 ga FEIL 3,12/4,56/0,51 etter heltilpasning av generert banner. Forsøk 2 ga FEIL1,26/2,86/0,77 etter heltilpasning. Begge bevares som råbilder og tidligere resultat 01/02, men er ikke valgt. Forsøk 3 brukte originalen alene som bildegrunnlag med strengere kontroll av silhuetter, ansikter, klær og den korte motivstripen. Denne gir OK0,03/0,12/0,95. Valgt råbilde har allerede korrekt 1536 × 1024-canvas og motivfelt, så ingen skalering eller lokal flytting er brukt i slutten.

De ti figurene er kontrollert samlet: to brune bak til venstre, grå pelsfigur bak Sam, Sam i blågrå dress/hatt, lav sentral figur med lyst skjegg/fjær/medaljong, høy mørk brun bakfigur, gyllenbrun mindre figur med hodepryd og rød/gul skål, langhalset kvinne med gul/oransje antrekk og rosa støvler, høy skjeggete stokkfigur og hvit furry høyrevariant med mørk ryggbekledning/brune hender/føtter. Ingen figur er utelatt eller lagt til. Høyre variant er ikke gjort til vanlig naken Max. Hvit port-/gitterstruktur, brune former til venstre og blå felt er bevart. HD-ansikter, pelsstrøk og hodepryd er tegnet fortolkning av lavoppløselige former, ikke identiske piksler; rotens karakterkontroll er derfor fortsatt nødvendig. Ingen identitetsnavn på de enkelte Bigfoots hevdes som dokumentert.

Rom 085: ett forsøk, OK0,07/0,90/0,97. Åtte synlige øvre og åtte nedre tanntupper er sammenlignet mot originalen. De øvre ligger omtrent ved original-x 82,105,131,168,195,220,245,265; de nedre omtrent 93,118,160,185,208,228,246,273. Dette er lesepunkter, ikke masker eller plasseringskoordinater. Kjølig grønn modelloverflate, sidesøm, mørke hulrom, svart munn, himmelgap og høyre/nedre avkutting er bevart. Ingen levende øyne, tunge, spytt, ny kropp/arm/hyssing eller separat 838-tann er malt inn. Ikke direkte upscale av tidligere rom059.

## Etterbehandling og bevis

Sluttbildene bruker kun rektangelklipp fra valgte nye 1536 × 1024-råbilder og nøytral RGB128-padding. Rom 083/085: [128,112,1280,800]. Obj 832: [128,288,1280,448]. Ingen originalsilhuettmaskering, lokal warp, korrelasjonsjakt eller kode-/checkerendringer.

Tidligere obj832-forsøk brukte hele genererte motivfelt: rå 01 klipp[156,116,1923,696] til 1280 × 448; rå 02 klipp[84,252,1452,754] til 1280 × 448. Begge er avvist. Sluttforsøk 3 trenger ingen slik skalering. Alle råforsøk og faktiske prompter er bevart.

a-oppskrift.py.txt reproduserer sluttresultater, kontrollfiler, manifest, notater og kontaktark fra de valgte råfilene. a-kildebevis.json bekrefter 40 av 40 låste kildehashes uendret. a-leveranser.json inneholder eksakte resultathashes og faktisk kontrollstatus. a-samlet-qa.png viser original til venstre og HD til høyre, i rekkefølge 083,832,085.

To OK og én SJEKK er klare for rotens mottak med ovennevnte synlige forbehold. Teknisk kontroll er ikke individuell brukergodkjenning, import eller runtime. Faktisk motoroverlegging og animasjon er ikke testet. Rom 083 og 832 er bevisst separate bildefiler; de er ikke slått sammen til en falsk ny bakgrunn.
