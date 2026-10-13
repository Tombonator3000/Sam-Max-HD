# Kildeplan for fig091_01 til fig091_05

Kun kildeanalyse. Ingen produksjonsbilder eller jobbfiler er endret. Alle 49 ruter er visuelt gjennomgått på åtte detaljsider. De 20 beskyttede jobbfilene er låst i b-kildehash.json og kontrollert uendret. Kontekstfiler og Sam-hovedark er låst separat i b-konteksthash.json. Oppskriftene er b-analyse.py.txt og b-kontekst.py.txt.

## Identitet og rekvisitt

Dette er Sam i blågrå dress og hatt, hvit skjorte, mørkt stripet slips og brun pels. De brede snutene, hendene, de nakne føttene og hver egen hatt-/munnstilling skal følge originalrutene. Hovedarket hovedark/sam.png bestemmer tegneseriestrek og identitet, ikke nye positurer eller endrede klær.

Den blå flaten med gul stjerne i 1954 til 1964 er kistelokket fra rom020. Originalrommets lukkede kiste og lag020_02s oppslåtte lokk viser samme brede blå flate, store gule stjerne og mørkeblå kant. Se b-kontekst-kiste.png. Det originale objektregisteret navngir obj205 «trailer-hope-chest». Dette gir konkret grunnlag for lokk, uten å gjøre formen til bok, skjold eller gave. Stjernens perspektiv og avkutting skal følge hver rute. Ingen ekstra kistekropp eller innhold skal tilføyes.

Skriptregisteret kobler kostyme 91 til actor 2 i rom_020/inngang.txt og obj_0206_verb.txt. Obj206 heter «trailer-closet»; obj209/210 har også kostymereferanser til 91. Registerkobling er ikke et lest fullscript. Eksakt handlingsårsak, spilletiming og hvem som utløser sekvensen er ikke dokumentert her. Bildene og objektregisteret gir likevel tilstrekkelig identitet for rekvisitten. Ingen konkret uavklart motivdel krever nå brukerens gjetning.

## Rutegrupper og avkutting

| Ark | Ruter | Synlig handling og kritiske detaljer |
|---|---|---|
| 01 | 1920 til 1928, 9 | Frontal Sam med ulike løftede ben og armstillinger. Tidlige ruter har avkuttet nedre kropp. Ikke fyll ut det transparente feltet. |
| 02 | 1929 til 1942, 14 | Sam mot høyre, stående, løftede armer/ben og markert fremoverbøyd kropp. Hendene er tomme. Bevar faktisk balanse og snutevinkel. |
| 03 | 1943 til 1955, 13 | Først ulike sidevendte kroppsstillinger. Fra 1951 frontal, avkuttet nedre kropp med liten separat brun fotrest. Fra 1954 blått stjernelokk vannrett foran kroppen. |
| 04 | 1956 til 1961, 6 | Lokket går fra skrått til stående ved Sams venstre bildeside. Deretter bøyd hode og åpen hånd til høyre. Samme tilsiktede tomrom og separate fotrest. |
| 05 | 1962 til 1968, 7 | Kildeidentiske motstykker til 1957 tilbake til 1951. Ingen nye mellomstillinger eller tilfeldige småvariasjoner. |

Alle ruter er lag 15. Det er ikke separate hoder som skal settes på kroppene. Fraværende bukser/ben i de avkuttede rutene må ikke tegnes inn. Betydningen av fotrestens avkutting behøver ikke gjettes for å bevare den. Generiske jobbnavn som «start mot høyre» er ikke tilstrekkelig beskrivelse av alle motivene.

## Geometri, palett og kildeidentitet

Alle fem kildeark er 352 × 240. Leveringslerret er 1536 × 1024, skala 4, forskyvning 64,32 og motivfelt 1408 × 960. Rutenes synlig-bokser er endekoordinater; rekt-felt er x,y,bredde,høyde. Full tabell i b-felttabell.md og maskinregister i b-ruteregister.json. Originalenes rel_x/rel_y må bevares: første gruppe har negative x, senere grupper omtrent 86 til 135. Dette skal ikke normaliseres til en felles kroppsmidt. Flyttedelta er 0,0. b-sekvens-a01/a07/a08/a09/a10.png viser kildene ved egne rel-koordinater, uten påstått plassering eller timing i spillet.

Originalmetadata oppgir 32-fargers rom020-palett og transparent indeks 255. Jobbarkenes magenta er bakgrunn, ikke motiv. RGB-antall per cel er registrert. Originalalpha i analysen brukes kun for kildebevis og visningsark. Fremtidig produksjonsalpha skal avledes fra ny art. Leveransen skal være ekte RGBA.

49 ruter gir 35 forskjellige originale RGBA-bilder. Ti identiske grupper er bevist i b-familiebevis.json, inklusive 1929/1941/1942/1943 og 1958/1959/1960/1961. Hele 05 kan kopieres fra de tilsvarende korrekte nytegnede rutene i 03/04. Ingen eksakt originalmatch ble funnet blant leverte figurkomponenter. Nye 003/005-munnrettinger er derfor ikke en aktuell donoravhengighet for 091.

## Produksjonsforslag etter gjennomgang

Tegn de 35 unike kroppsrutene i avgrensede grupper med originalutsnitt og Sam-anker. Bruk ordrette jobbprompter med separat kildepresisering om kistelokk, tomme hender, lag 15 og tilsiktet avkutting. Kopier bare kildebeviste identiske nye komponenter. Kontroller særlig håndgrep, stjernens perspektiv, egne munn-/benstillinger og den separate fotresten. Bevar råbilder, mapping, rel-komposisjon og alle kildehasher. Uendret teknisk kontroll og visuell sekvenskontroll kreves før levering. Kildeplanen er ikke produksjons-, runtime- eller ny brukergodkjenning.
