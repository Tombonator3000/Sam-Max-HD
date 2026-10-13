# Uavhengig C-kontroll av rom090 og obj901_01

Read-only kontroll av kandidatene, kildebildene i samlet før/etter-ark og motiv-PNG i full størrelse, SVG-struktur, kjedegeometri, kildehash og checkerkloner. Bare denne rapporten er skrevet. Metodevalget er uttrykkelig autorisert av Tom og dokumentert i TOMS-METODEVALG.json; dette er en vektorrekonstruksjon, ikke et nytt imagegen-forsøk.

## Motiv og synlig resultat

Rom090 bevarer Sam-hodet med hatt og Max sine to separate ører i det lyse midtfeltet. Ingen kropper, våpen eller nye sammenbindende figurdeler er fullført. De tette, forskjellige dekor-/silhuettformene på alle hyllene er beholdt, inklusive små mellomrom og asymmetrier som den tidligere imagegen-kandidaten forenklet. Blå lagdelte flater, mørk takkant med uregelmessige hengende buer og forhengets kantforløp beholdes. Resultatet er fortsatt kantet og detaljtett ved native visning; vektoriseringen må ikke omtales som fri, malerisk nytegning. Ingen ny lyssetting/gradient er observert.

Obj901_01 bevarer det store tomme røde feltet, den skjeve mørkrøde/brune høyrekanten og den lave, avklipte mørkebrune sokkeltoppen nederst. Det er ingen hårtust, ny støtte eller oppreist gjenstand. Den tidligere imagegen-versjonens avrundede/materialmodellerte kant er erstattet av kildens flate geometri. Små trinn/knekk finnes fortsatt i grensen; dette følger det begrensede forenklingsvalget, ikke en påstand om en matematisk ellipse.

## Uavhengige tall- og strukturkontroller

Alle åtte beskyttede kildehash er beregnet på nytt og stemmer. Begge PNG- og SVG-kandidaters manifesthash stemmer. SVG har bare svg/g/path/rect-elementer: 41 fargepaths for rom090, 8 for obj901_01, ingen innebygd bitmap, gradient eller filter. Flere regionløkker ligger som subpaths under én flatfarge.

Jeg har separat beregnet kildepunktets nærmeste avstand til sin vektorkjede og sammenlignet alle kjedeendepunkter:

- Rom090: 5680 delte kjeder, 9319 linjesegmenter, samtlige endepunkter uendret, maks avstand 0,8000000000000028 originalpiksler (flyttallsavrunding rundt 0,8).
- Obj901_01: 30 kjeder, 97 linjesegmenter, endepunkter uendret, maks avstand 0,7999999999999986.

Separat romlig søk etter strengt kryssende segmentpar fant null i begge. Dette omfatter egentlige kryssinger, ikke en full formell analyse av alle kollineære berøringer. Kilde- og vektorregiontall er henholdsvis 2274/2274 og 11/11 i geometrien. Delte grensers endepunkter og synlig sammenheng stemmer; ingen ny omkryssing er funnet. Det tidligere rom077-unntaket på 1,6 brukes ikke her.

Canvas er 1536 × 1024. Eksakt grå 128 utenfor [128,272,1280,480] for rom090 og [512,256,512,512] for obj901_01 er kontrollert på alle piksler. Ingen ekstra farget rad/kolonne utenfor motivfeltet er funnet. Kilde-/vektorbbox er [0,0,320,120] og [0,0,128,128]. Rasteret bruker antialiasing av kantdekning; ekstra mellomtoner ved grensene er derfor forventet selv om SVG-fyllene bruker de 41/8 kildefargene.

Uendret checker i rapportklonene: rom090 OK 0,01 / 0,03 / 1,00; obj901_01 OK 0,02 / 0,15 / 1,00. Disse tallene erstatter ikke motivkontrollen over.

## Kandidathash og mottak

- Rom090 PNG: `06ae2400e4bd3a42b6f11b48add3d5f94b4d4078eedc1d5284fa419b25ad1570`
- Rom090 SVG: `0075e497d9c664c6080ec0ca0cb1f4502fdb6ff9eab669196a5a2970d1c42e31`
- Obj901_01 PNG: `e46386ff15656606dba8bbf30c09c75b55230b5172f1f042d1fa103f8a252cac`
- Obj901_01 SVG: `c0810894ba68099003e157515484aea6d87a0d742a1ebf4327791e0d52be050e`

Ingen konkret avgjørende motiv- eller geometrifeil funnet i disse kandidatene. De er klare for roots mottaksvurdering under det valgte vektorprinsippet. Jobbleveranse, motorimport, runtime og ny individuell bildegodkjenning er ikke verifisert av denne kontrollen.
