# lag041_01_del1av2

Dato: 16. oktober 2026. Verktøy: innebygd image_gen. Modellnavn er ikke oppgitt. To genereringsforsøk. Første forsøk brukte prompt.txt ordrett, referanse.png som bilde én og jobber/rom041_del1av2/resultat.png som bilde to. Andre forsøk brukte samme prompt og referanser, første kandidat som bilde tre og et rettingstillegg bevart i rapporter/natt-fire-lag-20261016/prompt-lag041_01_del1av2-forsok2.txt.

Grunnlag: originalen, HD-rommet, GJENNOMGANG.md, ANALYSE.md og originaluttrekket obj384_01 er undersøkt. Engelsk CD-utgave, rom 41, objekt 384, tilstand 01, rommets ene palett. Dette er en opak lapp som viser tom himmel og vei der bilen ellers står. Objektuttrekket er 144 x 48 med alfa 255 over hele flaten. Bildet skal derfor ha tom vei etter originalen, selv om HD-referansen viser DeSoto. FROG ROCK-skiltet, skrå vei og landskap beholdes.

Første forsøk ga SJEKK på hele bildet, skift 0,19 og største blokkavvik 1,06 originalpiksler. Ny generering strammet skyformene mot HD-rommet. Et forsøk på å legge den første kandidatens rektangel direkte over HD-rommet ga synlig skjøt og ble forkastet. Denne sammensettingen brukes ikke i leveransen.

Endelig bilde kommer fra andre generering. Pillow ble bare brukt til eksakt flat #808080-ramme over y=0..111 og y=912..1023. Lerretet er 1536 x 1024, uten skalering, geometriwarp eller originalpikselmaskering. Beskyttede kilder er uendret.

Endelig egenkontroll med prosjektets eksisterende Python-miljø: OK. Skift 0,17, største blokkavvik 0,60 originalpiksler, kantlikhet 0,92. Tom veitilstand, skilt og objektets plassering er visuelt kontrollert. Et lite brunt innslag på steinen helt til høyre finnes i originalreferansen, men mangler også i det eksisterende HD-rommet. Dette ligger utenfor obj384_01 og må følges opp med neste Frog Rock-lag. Det er ikke tolket som et nytt motiv i denne leveransen.

Levert og visuelt kontrollert av Codex for objekt 384. Import, motoravspilling og Toms godkjenning er ikke utført i denne økten. Ingen commit eller push fra økten.
