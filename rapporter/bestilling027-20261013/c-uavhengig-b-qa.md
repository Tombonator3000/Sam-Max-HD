# Uavhengig kontroll av 27 B – foreløpig

Kontrollen er read-only av B sine kandidater. B har varslet at bobleunderlagenes rektangelgrenser og lag04-motiver fortsatt rettes. Dette er ikke en sluttfriskmelding. Nåværende SHA for problemtilstanden er i c-b-forelopig-hash.json; konkrete utsnitt er i c-b-motivavvik-foer.png.

Både kilde- og HD-familiearkene er lest samlet. Dråpeprogresjonen 154_01/02/03 viser liten, middels og lang dråpe; 04/05 er uten dråpe. Glassfigurens korrigerte bobleantall er 4/3/1/2. Det andre punktet i 155_04 ligger nær hodet og må beholdes; det skal ikke fjernes for å følge den eldre kildeplanens feilaktige ettpunktsbeskrivelse. 155_02/03 har lik kropp og egne boblefelt.

To konkrete motivavvik er meldt direkte til B:

- `lag016_04_del2av2`, `obj154_04`, lerretsboks [480,368,160,128]: det nytegnede utløpet peker tydelig oppover/opp-venstre og ligger høyere enn originalens nesten vannrette ytre åpning. Kilden har en egen hevet form, men den nye tegningen overdriver vinkelen. 154_05 er nærmere kildens vinkel; den skal likevel ikke kopieres blindt fordi originalene har ulike tilstander.
- Samme jobb, `obj155_04`, lerretsboks [672,304,192,224]: venstre hånd er en høy vinkehånd i HD, mens originalen holder hånden lavt nær skulder-/brystlinjen, med egen armendring. Håndposisjonen trenger kildepresis retting. Dette er et motivavvik selv om objektkorrelasjonen er OK.

Fullscenefamilien er også kontrollert. Lag01 har fjernet hånd/glassbeholder og brungrå gulvrest; lag02 har tomt felt der Bruno/is/sokkel stod, mens den separate kulepidestallen og overhengende skilt står. Lag03/04 har igjen grunnrommets håndbeholder og isfelt. Dette samsvarer overordnet med de separate kildelagene. Boblefeltenes synlige små underlagsruter avventer B sin pågående retting før endelig kontroll. Runtime er ikke testet.

## Etterkontroll av lokal motivretting

Oppdaterte 154/155-familieark viser nå 154_04 med nesten vannrett utløp og 155_04 med lav hånd til siden. De to konkrete motivavvikene ovenfor er rettet. 155_04 har fortsatt to bobler. Figuren i 04 har skarpere/svartere omriss enn01–03, et synlig stilforbehold. Boblefeltenes tidligere små mørke rektangler er ikke lenger tydelige i familievisningen.

Bruno-fraværsfeltet er undersøkt separat i c-b-gulvrest.png (kilde / faktisk HD / grunnrom). Originalen inneholder en liten delvis avklippet brun/grå rest til venstre for167boksen, x<1088; det er ikke riktig å slette alt der. HD-grunnrommets hvite biter er mer markerte, men følger det bevarte feltet. Et annet konkret avvik gjenstår: ved y=880, nedre kant av167innklippet, har gulvplankene en rett horisontal tonegrense. Meldt B for fargetonesammenpassing. Sluttkontroll avventer denne rettingen og endelig manifest.

## Sluttkontroll etter gulvretting

Den faktiske nye lag02-filen er lest i c-b-gulv-etter.png. Den rette horisontale grensen ved y=880 er borte; planketoner går nå sammenhengende over innklippskanten. Den kildebegrunnede avklippede resten til venstre er bevart.

Alle fem sluttfiler stemmer med b-leveranser.json. Uavhengig bytekontroll viser null avvik utenfor B sine dokumenterte komposisjonsbokser. Det finnes henholdsvis 31/52/52 HD-piksler utenfor bare metadataunionen i lag 01/02/03, fordi boblerensing går noen piksler over 155-feltet; dette er eksplisitt dokumentert av B. Lag 04/05 har null slike avvik. Ingen feilaktig påstand om null utenfor bare metadata beholdes.

Uavhengig komponenttelling i faktiske sluttbilder bekrefter 4/3/1/2 separate hvite bobler ved riktige kildeposisjoner. Hver komponent har 11 lyse HD-piksler i 4 × 4-boksen; dette beskriver den nye tegnede komponenten, ikke kopierte originalpiksler. SHA, bokser og bytekontroll står i c-b-sluttkontroll.json, med reproduserbar read-only-oppskrift som .py.txt.

De konkrete motiv- og skjøteavvikene som ble meldt i denne kontrollen er rettet. De tidligere nevnte avrundingene/blankere metallkantene, tydeligere gulvresten og stilforskjellen i 04 står som kvalitetsforbehold. Uendret teknisk kontroll er OK for alle fem og 13 felt ifølge de SHA-tilknyttede B-kontrollene. Denne uavhengige motivkontrollen er ikke runtime eller ny brukergodkjenning.
