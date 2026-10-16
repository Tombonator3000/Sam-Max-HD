# Videre figurproduksjon, 16. oktober 2026

Tom ba om å hente/flette og deretter lage gjenværende figurer og inventarikon. Main og grafikkgrenen er hentet; alle tidligere kode-PR-er var flettet.

Ordren fra 08:44 var utdatert. Fig249_04 til 08 og rettet munndel i fig249_02 var allerede levert i 417f4ff9 og dokumentert i 2606fad0. De fem arkene gir 32 nye ruter, munndelen én. Ingen av disse 33 nye rutene var med i publisert hd-mod a6c286bd.

Codex tegnet derfor fig249_04 på nytt unødvendig i bfb3480e. Ny variant a358d18a består egenkontroll og lokalt mottak for fem ruter, men den tidligere leveransen 44112cd1 beholder hoderetningen bedre. Den tidligere leveransen og notatet er gjenopprettet i jobbmappen. Begge bilder, råbilde, prompt, faktisk klargjøring og hasher er bevart her. Kandidatens kart heter nå kandidat-rutekart-fig249_04.json og kandidaten står ikke i leveranser, så den blir ikke valgt av vanlig mottak.

De tidligere leveransene er sammenlignet med originalene i tidligere-leveranser-kontroll.png. Sam, dragehjerte, nøkkel, sverd og originale sprut-/bevegelsesstreker er bevart. Teknisk prøve av seks ark ga 39 ruter OK og null til sjekk, men brukte den nye fig249_04-varianten. Prøven må gjentas med den gjenopprettede leveransen før dette teller som mottak for gjeldende filer. 39 inkluderer seks allerede importerte gangeruter og 33 nye ruter. Hele animasjonene er ikke avspilt i motoren.

Inventarikonet: de native HD-filene for objekt 888 finnes allerede. Den separate tegningsveien ScummEngine::drawVerbBitmap har ingen DigHD-kobling i dagens patch, mens ordinære romobjekter har noteObject. Dette er et kodefunn, foreløpig ikke en bygget eller spillverifisert retting. Inventarets store eske og de nye kortene er andre ressurser.

Brukte bibliotekskilder ved gjenopptakelsen: losninger/grafikk/figurark-fast-storrelse.md, losninger/bygg/publisert-mod-er-fasit.md og losninger/testing/logg-over-det-som-mangler-hd.md. De gjelder DigHD/ScummVM, men testene i opphavet er ikke automatisk bevis for Sam & Max. Målprosjektets låste ScummVM-base og eksisterende myk.py brukes. Ingen ny løsning, biblioteksendring eller motorbytte er gjort.

Produksjonen ble avbrutt etter første arks lokale mottak. Ved gjenopptakelse kjørte ingen nattevakt eller samarbeid-prosess. Ingen ny bakgrunnsproduksjon er startet. Fremdrift.json skiller levert, kontrollert, importert og godkjent. Neste faktiske manglende Sam-ark er fig249_09. Rundt 1655 figurark mangler fortsatt nytegning; et gammelt ordreantall er ikke en opptelling av faktiske leveranser.
