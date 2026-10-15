# Retting av Max-ikonet 15. oktober 2026

Tom avviste obj1008_01 fra ikon08: ansiktet lignet ikke Max. Toms vedlegg viser en generisk dobbeltbuet kaninmunn og rødt innslag i øynene. Den forrige leverte RGBA-eksporten hadde allerede svarte øyne og sikksakktenner, men hodet var fortsatt rundere og mer generisk enn originalikonet. Sammenligningen viser den faktiske forrige eksporten og den nye rettingen. Egenkontrollen bestod, men teknisk kontroll avgjør ikke figuridentitet.

## Grunnlag

- Original: jobber/ikon08/original_1x.png, rektangel [196, 76, 40, 24], objekt 1008 i rom 94. Forstørret referanse er max-original-20x.png.
- Godkjent figurreferanse: hovedark/max.png, godkjent av Tom 13. oktober 2026. Låser Max-identiteten.
- Stilreferanse: referanser/purcell-farge-20261013.png, levert av Tom. Låser strek og figurens særpreg.
- Toms vedlegg 1000053313.jpg påviser feil figuruttrykk, og brukes ikke som nytt stilanker.

Identiteten er avklart, Max. Walkthrough er derfor ikke nødvendig for å identifisere dette motivet. Originalens ørebøy, små svarte øyne, rosa nese, hvite hode, brede lukkede tannglis, røde markeringskant og beige kort med brun kant er bevart som motivgrunnlag. Ingen andre motiver er tolket på nytt i denne rettingen.

## Produksjon og kontroll

Ett nytt kall med innebygd image_gen og de tre referansene vedlagt. Eksakt modellnavn var ikke eksponert. Den sendte prompten er prompt01.txt; valgt råbilde er max-raa01.png. Ekte alfa fra generatoren er bevart. Med Toms tidligere uttrykkelige ja til Python er tegningen skalert med premultiplisert alfa og plassert etter originalens synlige boks. Ingen originalpiksler eller originalens konturmaske er brukt som tegning.

Reproduksjon: rapporter/ikoner-ui-20261015/klargjor-ikoner.py.txt. Hele ikon08/resultat.png og RGBA-eksporten obj1008_01.png er oppdatert. De andre 46 feltene på ikon08 og de øvrige 110 RGBA-ikonene er uendret. Ikon07 og ikon09 har identiske sjekksummer som før. Beskyttede jobbfiler er uendret. Alle tre ark består uendret sjekk_leveranse.py. Små svarte øyne og synlig tannglis er visuelt kontrollert både i 160 x 96 og forstørret sammenligning. Dette er ikke Toms godkjenning. Ingen motorimport eller spilltest.

Toms føring er dokumentert i AGENTS.md og ANALYSE.md: se alltid relevante godkjente stilreferanser før nytegning, spør Tom hvis motivet er usikkert, og bruk ved behov walkthroughs til å avklare gjenstander, steder og brukssituasjoner med kildehenvisning. En gjetning skal ikke bli produksjonsgrunnlag.
