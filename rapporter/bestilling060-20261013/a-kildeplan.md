# Bestilling 60 A: fig209_01 til fig209_05

Kun analyse. Ingen nye bildekall eller jobbleveranser er laget. De fem arkene viser 36 ruter med Sam opp ned i glassapparatet fra rom040, senere sammen med Max. Dette er sammensatte figurer og apparat, ikke fem vanlige Sam-ark. Alle fem helark og alle 36 nærbilder er sett.

[Originalkontaktark](a-original-kontaktark.png), [feltark 1](a-feltark-1.png), [feltark 2](a-feltark-2.png), [feltark 3](a-feltark-3.png), [feltark 4](a-feltark-4.png), [feltark 5](a-feltark-5.png), [metadata og palett](a-kildebevis.json), [familiebevis](a-familiebevis.json), [20 låste jobbkilder](a-kildehash.json).

## Identitet og kontekst

Kilden viser brun Sam i blågrå dress og hatt, hvit skjorte og blått/svart slips. Hodet vender nedover; føtter og hender har egne bevegelser øverst og på sidene. Den brede hvite, blå og lyslilla glassformen med orange sidekanter og små nedre grå utstikkere er en del av hver figurcel. Den skal ikke erstattes med transparent tomrom eller en tilfeldig kabin.

Rom040-originalen viser samme apparat ved det opp ned skrevne VORTEX MINI-skiltet. Romnotatet i origin/main:docs/gpt-romnotater.csv bekrefter at gavebutikken med hensikt er opp ned. Ingen rotasjon eller speiling til vanlig orientering er tillatt. Registernavnet Sam er utilstrekkelig: cel1936 og senere viser også Max, med kremhvitt fargefelt, brune/beige konturer og egen øre-, kropps- og ansiktsstilling. Ikke erstatt rommets varme Max-palett med hvit/blå pilotpalett.

konsept/2026-10-12/kostymer-348.csv kobler 209 statisk til skuespiller 2 i rom040/lokal_201,202,203. Disse tre skriptene finnes ikke i det lagrede kildebevisutvalget. Det tilgjengelige rom040/inngang.txt laster kostyme209 ved offset0028/002E. Dette underbygger romtilhørighet, men beviser ikke eksakt handlingsnavn, fysikk eller timing. Motivet er visuelt sikkert som Sam, Max og glassapparatet; det kalles ikke teleportering, flaske eller annen ubekreftet funksjon.

## Sekvenser og identiske ruter

| Ark | Cels | Synlig innhold |
| --- | --- | --- |
| 01 | 1920 til 1927 | Sam alene, fra høyere ben-/håndstilling til samlet stilling inne i glassfeltet. |
| 02 | 1928 til 1935 | Nøyaktig omvendt kildebildeutvalg av 01. 1928=1927, videre par til 1935=1920. |
| 03 | 1936 til 1943 | Max først høyt med beina ned mot Sam, deretter samlet og rotert inn ved siden av Sam. Egne Sam-hender beholder kontakten. |
| 04 | 1944 til 1951 | Begge opp ned, Max til venstre i bildet; små ansikts-/øre- og håndforskjeller. |
| 05 | 1952 til 1955 | Egne lyse glassoverlegg som dekker figurene; 1954=1952, 1955=1950/1951. |

Det finnes 22 unike synlige RGB-utsnitt og 12 grupper med gjentakelser, dokumentert bytevis i familiebeviset. 1938=1939; 1945=1946=1947; 1950=1951=1955. Ingen av de 36 rutene matcher Sam002 som helt synlig RGB-utsnitt. Gjenbruk skal derfor skje mellom kildeidentiske 209-cels etter nytegning, ikke ved å lime vanlige oppreiste Sam-piloter inn i glasset.

## Mål, fester og farger

Alle rutene bruker lag 15 og arkretning 1. Kostymemetadata har samme ruteserier i fire retningsvalg, og animasjon 1/6 deler 1920 til 1927. Dette gir ikke tillatelse til å legge nye retninger på arket. Serien med animasjon 8 går over ark 03, 04 og starten av 05.

Synlig bredde varierer fra 68 til 84 kildepiksler, høyde fra 100 til 112. Rel_x varierer fra -84 til -69 og rel_y fra -112 til -100. Synlig utsnitt og rekt skal holdes adskilt, særlig 1952 til1954 med 68 synlige kolonner og rel_x=-69. Kroppen skal ikke strekkes for å fylle apparatets eller en annen rutes bredde. Alle source-bboxer matcher den målte ikke-magenta-boksen.

Rompalett040 brukes med 32 indekser; hver rute har 22 til 31 synlige RGB-farger. Full RGB-liste per rute finnes i kildebeviset. De bleke blå/lilla figurpartiene under glass er synlig kildemotiv. De skal ikke fjernes som feil alfa eller recoloreres til vanlig dress. Kun magenta og grå atlaspadding skal ende transparent. Selve glassets farger og refleksfelt skal bevares som motiv; ingen generell halvtransparent kabin skal oppfinnes.

## Produksjonsplan og kontroll

Bruk innebygd imagegen, beskyttet originalprompt ordrett og separat presisering om begge figurer, opp ned-retning, glass og varm palett. Sam- og Max-hovedark brukes til identitet, originalen til konkrete proporsjoner, fargefelt, overlapping og stillinger. Start med de åtte unike Sam-alene-komposisjonene og fortsett den sammenhengende Max-serien med de øvrige 14. Avgrensede kall må beholde samme apparatform og flate fargefelt uten oppdiktet tekst eller mekanikk. Originalens lyse glassoverlegg må følge de respektive rutene; ikke arves blindt til alle.

Vanlig helskalering av nye komponenter til hvert eksakte synligmål er autorisert arbeidsform. Ingen originalsilhuettmasker, lokal warp eller vektorrekonstruksjon. Lever 1536 × 1024 ekte RGBA. Bevar ordentlige synlig/rekt/rel-forskyvninger og lag en samlet relativvisning av hele familien før mottak. Uendret checker må kjøres på alle 36 ruter; visuell QA må i tillegg kontrollere glasskanter, Max-ører/munn, Sam-poter og små forskjeller i 04/05. Kildeidentiske celpar skal få byteidentiske nye komponenter.

Ingen avgjørende motivuklarhet er funnet i de synlige delene. Den eksakte scriptstyrte handlingen og timing er fortsatt ikke undersøkt i runtime. Planen sendes root før nye bildekall.

## Korrigering etter nærlesing under produksjon

1936 til 1942 viser Max bakfra. I originalretningen er føttene øverst, rumpen med liten rund hale under dem, og det store lyse ovale feltet er bakhodet. De lange nedhengende formene er ørene som Sam griper. 1942 viser sålene mer rett mot betrakteren, fortsatt uten Max-ansikt. Først 1943 viser ansiktet i dreid stilling. Se a-max-orienteringsdiagnose.png, som er en uttrykkelig rotert analysevisning, og a-1942-nar.png. Leveransen roteres ikke. Tidlige genereringsforsøk misforsto dette og er bevart som avviste forsøk, ikke ankere.

1941 har dessuten et separat lyseblått kildepunkt, RGB(127,159,195), ved atlas (81,186). Hovedkomposisjonen er 69 piksler bred fra lokal x9, mens synligboksen med punktet er 78. Hovedkomposisjon og nytt separat punkt plasseres hver for seg. Alle ruter har også et separat lite grått utstikkerfelt under apparatet, dokumentert i a-kildekomponenter.json.
