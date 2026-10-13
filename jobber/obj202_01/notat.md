# obj202_01

Dato: 2026-10-13. Innebygd ChatGPT-bildegenerator; eksakt bildemodellnavn er ikke eksponert. Tre fullstendige genereringsforsøk. Astra håndterer produksjonen.

Motivet er det tomme Wak-A-Rat-brettet med fem hull og avkuttet del av Sams grålilla jakke og blå/svarte slips. Ingen klubbe, hånd, Max, rotter eller scorefelt finnes i dette utsnittet. Kildeoriginalen er byte-identisk med rom019-utklippet (24,72,232,192); det er dokumentert uavhengig av root og agent A.

De to første forsøkene fikk FEIL i blokk-FFT, mens helhetsskift og kantlikhet var nær originalen. Et direkte utklipp av nytt rom019 fikk også FEIL i samme blå bakgrunn. Root lokaliserte avviket til øvre venstre blokk, med høy kantkorrelasjon men ustabilt forskyvningsestimat. Dette støtter en hypotese om bakgrunnsgradient/dithering som årsak, men beviser ikke en algoritmefeil. Ingen kontrollterskel eller pipelinekode er endret.

Tredje forsøk tegnet hele motivet på nytt med originalprompt ordrett og tillegg om kildens blå fargeplatå, gardinspiss, tomme felt og eksakte avkutting. Generatorens motivrektangel (351,261,835,498) ble normalisert samlet til (352,272,832,480) med Lanczos på eksakt RGB128-lerret. Ingen lokal warp eller originalpikselmaske. Et separat forsøk på fire HD-pikslers samlet plassering forbedret globalt skift, men forverret blokkmålet; det er bevart som forkastet kandidat og brukes ikke.

Sluttleveransen har 1536 x 1024 og egenkontroll SJEKK: globalt skift 0.93 originalpiksler, blokk 1.11, kantlikhet 0.91. Den er levert for mottakskontroll med dette forbeholdet, ikke erklært teknisk OK. Fem tomme hull, riktig blå bakgrunn, brett, avkuttet tekst og Sam-del er visuelt kontrollert.

Råforsøk, fullprompt, kandidater, diagnose og normaliseringsmetadata finnes i rapporter/bestilling005-20261013/root202-*. Ingen beskyttede kilder er endret.

SHA-256 resultat: e667644fc5c575671d928edfc6aae2279234c56eb2b8df44b440eeea8498812d

Motorimport, maskesamspill, spilltest og individuell ny Tom-godkjenning er uverifisert.
