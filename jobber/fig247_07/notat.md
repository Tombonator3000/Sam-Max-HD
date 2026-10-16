# fig247_07

Dato: 2026-10-16T05:43:21.101068+02:00

Verktøy: innebygd image_gen.imagegen. Eksakt modellnavn vises ikke. Antall bildeforsøk: 1. Python med Pillow, numpy og scipy er brukt til rensing av alfa, kantfarger og presis plassering etter Toms uttrykkelige tillatelse. Ingen installasjon eller kodeendring.

Motivgrunnlag: kostyme 247 i rom 48, Sams VR-handling i Bumpusville. Seks ruter fra animasjon 8. Sam står, bøyer armen, løfter begge hendene ut til siden og legger dem på VR-hjelmen i de to siste rutene. Svart VR-hjelm, grønt ugjennomsiktig visir og grå kabler er originale. Referanse.png er sett sammen med hovedark/sam.png og hovedark/max.png før nytegning. Original_1x.png er også sammenlignet. Rom048-originalen og foregående fig247_05 er undersøkt for sammenheng. Originalen styrer geometri, palett og tilstand. De godkjente hovedarkene styrer identitet og strek.

Prompt.txt beskriver generisk fedora og begge figurene. Det stemmer ikke med disse rutene som viser Sam alene med VR-utstyr. Korrigert prompt og begrunnelse er bevart separat i rapporter/natt-fire-20261016-0540/korrigert-prompt-fig247_07.txt og log.md, etter regelen i remake-skillen om feil premiss. Beskyttede filer er uendret. Første bildeforsøk brukte originalen som bilde én, Sam som bilde to og Max som bilde tre. Ett bildeforsøk, deretter tillatt rensing og plassering.

Leveranse: hele lerretet 1536 x 1024 RGBA med ekte myk alfa. Nytegningens egne sammenhengende alfakomponenter er isolert. Svak bakgrunnssmitte er fjernet, og myke RGB-kanter er renset. Rutene er plassert etter synlig-boksene i jobb.json. Todelt høydejustering ved visiret holder forholdet mellom kabler og kropp nær originalen. På fig247_06 er visirets målhøyde lest visuelt, fordi den automatiske grønnmålingen ellers traff den smale stripen over visiret. Originalsilhuetten er ikke brukt som produksjonsmaske. Plasseringsoppskrift og kilde-/målankere ligger i rapporten.

Egenkontroll: OK for alle 6 ruter, ingen FEIL. Systemets python3 mangler numpy. Kontrollen er derfor kjørt med eksisterende /home/tom/Sam-Max-HD/.venv/bin/python3 uten installasjon. Full utskrift: rapporter/natt-fire-20261016-0540/fig247_07-egenkontroll.txt.

Statisk visuell egenkontroll er utført mot original og hovedark, med kontroll av figuridentitet, hjelm, håndstillinger, kabelretninger, munnstillinger og antall ruter. Sammenligning: rapporter/natt-fire-20261016-0540/fig247_07-sammenligning.png. Indre former og kablenes krumming er nytegnet og ikke pikselidentiske med originalen. Kontroll av faktisk animasjonstempo, overganger og motorvisning gjenstår hos Claude. Rutekartet bruker faktisk alfa over 128.

Levert til Claudes mottakskontroll. Importert: nei. Motoravspilt: nei. Godkjent av Tom: nei. Ingen usikker motividentitet gjenstår for dette arket, men teknisk OK er ikke en visuell godkjenning.

SHA-256: f9612b444385cedd0b094b558f10d07446d599b177231d70ce9cc6d2caf8d995
