# fig312_02, strikkhopp i rom61

Laget 18. oktober 2026, sluttkontroll 2026-10-18 13:37 (norsk tid). Innebygd image_gen, 2 bildekall. Modellnavn ikke oppgitt. 11 ruter, SHA-256 53be1c944c7cd14e7c546af320225a4cfcd6071a92ab099543dd456c141e1cc6.

Kilder: jobbens uendrede originaler, kostyme312 fra originaluttrekket, rom61 i docs/GJENNOMGANG.md og docs/figurer.csv. Godkjent hovedark/sam.png er identitets-/stilanker; kostyme312 bruker også hovedark/max.png. Rød sele og gult hodeutstyr med lilla felt er bekreftet i det originale spillet. Dette lilla er tilsiktet utstyr, ikke magentarester.

Elleve ruter. Sam alene i de åtte første; han griper/løfter Max i de tre siste. Max har originalens lukkede øyelokk i rute 1938 og 1939. Andre hele generering endret også Sam og er avvist. Bare ett AI-tegnet øyelokkelement fra dette forsøket er plassert fire steder, med originalens øyelokkfarge og eksisterende malt hud. 630 RGB-piksler i fire avgrensede områder, all alfa og resten av Sam/Max uendret. Siste Max beholder åpne øyne. Se max-oynerens.json og rens-max-oyne.py.txt.

Råbilder og alle faktiske produksjons-/rettingsprompter ligger i rapporter/strikkhopp-20261018. Python-rensing/plassering bruker Toms tidligere uttrykkelige tillatelse. Ekte alfa beholdt; ingen ny figur er klippet med originalens harde pikselomriss. Rens og eventuell avgrenset hudtonejustering er dokumentert i klargjor.py.txt og rutekart-fig312_02.json.

Egenkontroll: 11 av 11 OK. Separat myke-figurer-mottak: alle 11 OK, null til sjekk, uendrede grenser. Alle rutene sett som native PNG mot originalen og som utsnitt fra motoren. Kostyme307 har fem siste stå-/taleprøver og tre tidligere gangeprøver med byteidentiske gangeruter; kostyme312 har to hele animasjonsprøver. Samlet alle 96 ruter observert, 340 skjermbufferkontroller fra figurstart uten avvik. Hver prøve har et kjent avvik på 160 ved frame 36 før figuren settes inn; publisert grunnlag 5212c395 gir samme avvik. Dette er ikke rettet av grafikkrunden. Z-kantmålingene er ikke null.

Prøvene er tvunget avspilling med lokal QA-krok, ikke naturlig gjennomspilling. Separat Claude-kontroll og Toms nye stilgodkjenning gjenstår. Import kvitteres per SHA i fremdrift.json etter publisering og tilbakehenting.
