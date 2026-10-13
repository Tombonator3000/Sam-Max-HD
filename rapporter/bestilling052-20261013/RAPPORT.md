# Bestilling 52 – fem Sam-ark og ikon06

14. oktober 2026. Seks hele grafikkjobber er mottatt: `fig002_02`, `fig002_03`, `fig002_04`, `fig002_05`, `fig002_07` og `ikon06`. Alle seks er OK i den uendrede leveransekontrollen. De inneholder 61 figurruter og sju ikonfelt. Seks ytterligere, avklarte ruter i `fig002_06` er kontrollert som separat delarbeid; dette arket er ikke levert eller krysset av.

## Kilde og motiv

Sam følger det godkjente hovedarket og piloten: brun pels og bare poter, blågrå dress og hatt, hvit skjorte og mørkt stripet slips. De 61 rutene bevarer gange i tre retninger, separate talehoder, håndlag og tre oppstrakte armstillinger. Alle sju rute-QA-ark og fem sammensettingsark er sett av rot. Hoder og hender er kontrollert over riktige pilotkropper etter originalens relative posisjoner. Ressursrekkefølge er ikke bevist animasjonstiming.

Fire synlige fotsåler fikk lokal nytegning til organiske poteputer. En dobbel buksekant i første retting ble fjernet med en rektangulær overgang mellom to nye bilder. Rot har sett siste resultat og uavhengig bevist at ingen piksler utenfor de fire dokumenterte rektanglene ble endret. Originalsilhuetter ble ikke brukt til å maskere produksjonen. De fem håndlagene har sine to brune deler; cel 259 har en liten original klynge innlemmet i den glatte hånden, dokumentert i C sin QA.

Ikon06 inneholder tre små skog-/fjellutsnitt og fire flate landskapsutsnitt, objekt 804–810. Alle sju er sett enkeltvis mot original og i helark. Kantkorrelasjon for hvert felt er over 0,92. Tekstur i trær og himmel følger den leverte stilen; teknisk samsvar er ikke individuell brukeraksept.

## Format og kontroll

Figurarkene er ekte RGBA 1536 × 1024. Padding og alt utenfor de 61 rutevinduene er helt transparent. Den strenge fargesøkingen fant seks antialiaspiksler med magentafarget RGB og alfa nøyaktig 1 av 255, fordelt over ark 02, 03 og 04. Ingen slik piksel har høyere alfa; dette er ubetydelige kantrester, ikke en synlig atlasbakgrunn. De konkrete tallene er bevart i `root-figurkontroll.json`.

Ikonarket er RGB 1536 × 1024 med grå padding 128 og magenta mellom de sju feltene, som denne jobbtypen krever. Det skal ikke forveksles med figurarkenes alfakontrakt.

Rot har kjørt checker på de faktiske seks leveransefilene, kontrollert alle 61 figurruter og alle sju ikonfelt, kontrollert kilde-/prompt-/referansehash og bevist den lokale potekorreksjonens avgrensning. 28 beskyttede kildefiler og sju ankerkilder er uendret. Sju generatoranrop for Sam og ett for ikon06 er registrert med eksakte råbilde- og prompthash. Den innebygde generatoren eksponerte ikke et eksakt bildemodellnavn.

## Delarbeid som holdes utenfor levering

`fig002_06` har seks avklarte a10/a11-ruter tegnet og kontrollert OK i et rapportbilde. De fem a07-rutene, cel 171–175, er fortsatt ubesvart i brukeravklaringen. Deres felt er bevist helt transparente i det partielle bildet. Ingen fullført-status for dette arket. Ikon07–09 venter fortsatt på tidligere motivavklaringer.

Ingen motorimport, faktisk avspilling, spilltest eller ny individuell visuell godkjenning er bekreftet. Grafikkleveranse, kontroll og spillets runtime holdes som ulike tilstander.
