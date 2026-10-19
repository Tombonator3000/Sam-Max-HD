# fig309_02, Sam og Max i strikksele

19. oktober 2026. 8 spillruter, 1536 x 1024 RGBA. Resultat-SHA256 `ee239c3f1a4888e2392a9fde0f42570777b0b19f1068a492e74855f1e9113f47`.

Motivet er kostyme309 i rom61, strikkhoppgrotten. Sam og Max kommer opp i strikken, Sam holder Max og setter ham ned. Sam har rød sele og kildebekreftede gule/purpur strikkbriller, blågrå dress/fedora, hvit skjorte og blått/svart slips. Max følger det godkjente hovedarket. Bare krok/strikk og delvise kroppsdeler i de første rutene er beholdt som kilden viser dem. Ingen nye figurer legges til i ruter der de er utenfor utsnittet eller Max er satt ned.

Før nytegning: alle fem originalark, begge godkjente hovedark, to originale motorforløp, ressursbankens rom61 og riktig kostyme309-rad i docs/figurer.csv er sett. Se KLARGJORT.md og premissretting.txt i rapporter/sam-max-sele-20261019. Beskyttede jobbfiler er uendret.

Innebygd image_gen, eksakt modellnavn ikke vist. Bunken har sju faktiske kall, sju bevarte råbilder, seks brukt i sluttresultatene. A01 er erstattet av A02 etter retting av oppdiktede ledd i strikken. Dette arket bruker unik-C-raa01.png. bildekall.json har faktiske prompter og råbilde-SHA-er.

Python er uttrykkelig godkjent til rensing og plassering. Generert alfa er bevart med myk kant. Kildekomponentenes rektangler styrer plassering; ingen hard original silhuettmaske klipper tegningen. Manglende små strikkdeler gjenbruker den genererte strikkdelen fra A02. Den lille blå jakkedelen i1928 og ørebevegelsesstrekene i1952 bruker generert materiale fra samme råbilde og kildefarge.1926/1927 følger originalens glattet strikksenter ved myk flytting av generert RGBA. Alt er ført i prototype-kvitteringer.json.

Egenkontroll OK. Alle rutene OK. Native mottak godtar alle rutene med uendrede grenser. Alle er visuelt sett mot original/native/motor og registrert tegnet. To animasjoner gir 132 skjermbufferkontroller fra figurstart uten avvik; to kjente oppstartsavvik er identiske med grunnlaget. Tvungne prøver, ikke naturlig gjennomspilling. Ingen ny Tom-godkjenning eller separat Claude-kontroll. Faktisk import/publisering bekreftes i mottak-publisert.json når den finnes.
