# Kostyme 207 — felles kildeplan for bestilling 55 og 56

Kun kildeanalyse, ingen ny grafikk eller resultatendring. Hele familien fig207_01–08 er sett visuelt, 45 ruter, hvorav 41 i bestilling 55 og fire i bestilling 56. 28 + 4 beskyttede kildefiler er låst i hver mappes c-kildehash.json. c-rutekart207.json inneholder eksakte rektangler, synlige bokser, lag, animasjon, rel, palettfrekvenser og bildehash for hver rute. Seks c-originalruter-ark og c-original-kontaktark.png viser familien samlet. 54 står frosset.

## Identitet og dokumentert kontekst

Dette er Mini Vortex-beholderen i den opp-ned-vendte gavebutikken, rom 040. Originalen i jobber/rom040/referanse.png viser samme sølv/blåglassaktige form, vridde sidekanter, bølget lyst innvendig felt og MINI VORTEX-skilt. Registeret objektbilder-959.csv linje 356–363 kaller 378 flipped-vortex og 379 flipped-drip; 382 er flipped-vortex-sign. Dette skal ikke tegnes som kjøkkenets isblokk, fryser eller isglass rundt Bruno.

Sam identifiseres visuelt i de befolkede rutene med brun hundesnute/ører, blågrå dress og hatt, hvit skjorte og mørkt diagonalt stripet slips; Max er hvit/kremfarget med to lange ører og bred tannmunn uten klær. Begge er opp ned. Actor-kobling alene beviser ikke dette, men skript-kostymekoblinger.tsv bekrefter kostyme 207 i rom_040/lokal_202.txt linje 22 på actor 2 og lokal_203.txt linjene 9, 54, 81, 97 på actor 5 og 126 på actor 2. Hele skriptene 202/203 ligger ikke i det tilgjengelige kildebevisutvalget; koblingstabellen er lest, ikke full kjøretid. Den eldre kostymer-348.csv-raden «Uavklart» er et uferdig register, ikke grunn til å overse de direkte bildene. Ingen ukjent figur eller rekvisitt er funnet.

Arket 06 er **tom beholder**, selv om generisk prompt sier Sam og Max sammen. Figurnavn gjelder ressursfamilien, ikke påbud om personer i hver rute. Skiltteksten finnes i rommet, ikke på selve disse 45 rutene: ingen nye ord skal legges inn.

## Sekvenser og tilstander

| Ark | Cels | Faktisk kildeinnhold |
|---|---|---|
| 01 | 1920–1924, 5 | Start 1920 og første fire a7-ruter. Sam og Max tett sammen opp ned bak glass; mørk blå/sølv og brune felt veksler med blekere lys. |
| 02 | 1925–1932, 8 | Fortsettelse a7. Egne gjentakelser av mørk, mellomlys og blek glass/persontegning. |
| 03 | 1933–1940, 8 | Fortsettelse a7. Lys- og detaljvarianter; 1936, 1938, 1939, 1940 er ikke eksakte tidligere dubletter. |
| 04 | 1941–1946, 6 | a7 mot nesten helt hvitt lysfelt. Personenes brune/blå konturer blir stadig svakere; ikke kontrastnormaliser. |
| 05 | 1947, 1 | a8. Eksakt samme RGB som 1946, svært lyst hvitt felt med svake personer. |
| 06 | 1948–1954, 7 | a9. Tomt bølget glassfelt, små ulike merker. Til slutt flyttes den lyse dør-/glassflaten mot høyre og et stort mørkt blått innvendig felt åpnes. Ingen personer skal tilføyes. |
| 07 | 1955–1960, 6 | a10. Befolket lukket til åpnet glassfelt; Sam synligere/brunere når glasset flyttes. Max skifter kropp/øreplass og kommer over beholderens øvre kant i bildeperspektivet. |
| 08 | 1961–1964, 4 | Siste fire a10-ruter. Max er høyere utenfor beholderfeltet, med fire egne øre-/arm-/munnplasseringer; Sam fortsatt opp ned inne. Egen høyde og rel, må ikke krympes til 100 pikslers beholder. |

Alle cels er lag 15, move_x/move_y = 0. Jobbens toppnivå lag 1–8 er arknummer, ikke åtte samtidige figurkomponenter. Hver rute er en samlet beholder/person/lys-komposisjon. Metadata viser samme sekvens for retninger 0–3 og speil=false; promptens generiske tekst om høyre/venstrespeiling skal ikke utløse nye speilvarianter. Sekvensnumrene er dokumenterte; faktisk timing, retning i avspilling og hendelsesrekkefølge er ikke runtime-verifisert.

## Geometri, rel og pakking

Alle ark er RGBA 1536 × 1024 med transparent felt uten magenta/grå padding. Metadatafeltet [64,32,1408,960] er pakkeområdet. Hver synlig boks [x0,y0,x1,y1] pakkes ved [64 + 4x0,32 + 4y0] med 4× størrelse. Originalens magenta er nøkkelbakgrunn; hvite glass-/lysflater er motiv, ikke hull som skal fjernes.

1920–1953 og 1955–1956: 68 × 100, rel(-68,-100). 1954 og 1957–1959: 69 × 100, rel(-68,-100). 1960: 69 × 107, rel(-68,-107). 1961–1964: 69 × 126, rel(-68,-126). Dermed forblir nederste felles anker y=0 mens figuren strekker seg oppover. Ark 07 har egne y-posisjoner i andre rad; bruk synlig-boksen, ikke jevne rutenettantakelser. Små lyse/grå dråpe-/utstikkerformer under beholderen inngår i synlig-boksen og skifter; ikke klipp dem bort eller tilføy vannpynt.

## Dubletter og palett

45 ruter gir **24 unike RGB-bilder**, målt fra faktiske originalutsnitt. Eksakte grupper:

- 1920, 1926, 1927, 1932, 1933, 1937
- 1921, 1925, 1928, 1931, 1934
- 1922, 1923, 1924, 1929, 1930, 1935
- 1942, 1943, 1944
- 1946, 1947
- 1949, 1950, 1951, 1952
- 1957, 1958

Øvrige cels er unike. Dublettenes mål og rel er like, så en korrekt NY HD-komponent kan gjenbrukes i alle gruppens målplasseringer. Se c-dublettbevis.json. Ingen nytegning av identiske gjentakelser er nødvendig. En ekstra måling av fargeklasseinndelingen ga ingen ytterligere geometrisk identiske grupper; de ulike lysvariantene må derfor ikke ukritisk reduseres til én global fargekurve. c-fargeinndelingsbevis.json dokumenterer begrensningen.

Kostymeformat 0x61 med 32 palettindekser, rom 40 palett 0. Kildens blå/lilla/sølv, brune, kremhvite og sterkt utblekede tilstander styrer hver variant. Godkjente Sam/Max-hovedark er identitets- og strekankre, ikke tillatelse til å gjenopprette mettet brun hud eller svart slips i de lyse glassrutene. Eksakte RGB-frekvenser er lagret per cel. Ingen dynamisk palettavspilling er testet.

## Anbefalt produksjon og kontroll

Behold familien hos samme eier på tvers av bestilling 55/56. Tegn først den mørke befolkede beholderen 1920 som identitets- og beholdergrunnlag, deretter de kildeegne lysvariantene. Lag de tomme a9-tilstandene som egen gruppe, deretter a10 som én sammenhengende person- og åpningsfamilie inklusive alle fire fra ark 08. Arbeid i håndterbare imagegen-grupper, med originalutsnitt og godkjente hovedark; originalens orientering bestemmer, ikke automatisk oppretting av hoder eller beholder. Bevar hver ny råfil/prompt, alfakilde og komposisjon. Ingen originalkonturmaske eller lokal geometriwarp.

Etter hver gruppe: sammenlign alle unike kilder ved 1×/4×, personenes opp-ned-poser, to Max-ører, Sams hatt/slips, glassdørens side/åpning, hvite refleksflater og de små nederste formene. Kopier deretter eksakte NYE dublettkomponenter med hashbevis. Kontroller alle 45 pakkede ruter og rel-ankeret på tvers av de tre høydene; checker alene kan ikke oppdage feil lys/person i et korrekt beholderomriss. Sammenlign med rom 040 som kontekst, uten å male skilt eller ekstra romdeler inn i figurarket. Runtime, import og ny brukergodkjenning skal stå uverifisert.
