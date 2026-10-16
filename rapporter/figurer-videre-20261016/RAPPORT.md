# Videre figurproduksjon, 16. oktober 2026

Tom ba om å hente/flette og deretter lage gjenværende figurer og inventarikon. Main og grafikkgrenen er hentet; alle tidligere kode-PR-er var flettet.

Ordren fra 08:44 var utdatert. Fig249_04 til 08 og rettet munndel i fig249_02 var allerede levert i 417f4ff9 og dokumentert i 2606fad0. De fem arkene gir 32 nye ruter, munndelen én. Ingen av disse 33 nye rutene var med i publisert hd-mod a6c286bd.

Codex tegnet derfor fig249_04 på nytt unødvendig i bfb3480e. Ny variant a358d18a består egenkontroll og lokalt mottak for fem ruter, men den tidligere leveransen 44112cd1 beholder hoderetningen bedre. Den tidligere leveransen og notatet er gjenopprettet i jobbmappen. Begge bilder, råbilde, prompt, faktisk klargjøring og hasher er bevart her. Kandidatens kart heter nå kandidat-rutekart-fig249_04.json og kandidaten står ikke i leveranser, så den blir ikke valgt av vanlig mottak.

De tidligere leveransene er sammenlignet med originalene i tidligere-leveranser-kontroll.png. Sam, dragehjerte, nøkkel, sverd og originale sprut-/bevegelsesstreker er bevart. Teknisk prøve av seks ark ga 39 ruter OK og null til sjekk, men brukte den nye fig249_04-varianten. Prøven må gjentas med den gjenopprettede leveransen før dette teller som mottak for gjeldende filer. 39 inkluderer seks allerede importerte gangeruter og 33 nye ruter. Hele animasjonene er ikke avspilt i motoren.

Inventarikonet: hypotesen om drawVerbBitmap var feil for denne knappen. Et bygget lokalt forsøk endret ikke den lille esken. Originaluttrekk, figurer.csv og spillprøven viser at knappen er kostyme 1, rute 2, tegnet av aktør 1. Objekt 888 er kortet inne i inventaret. Det lokale motorforsøket er reversert, og ingen motorkode publiseres fra denne runden.

Fig001_01 er nå nytegnet med riktig beige kort og egen alfa. Egenkontroll og separat mottak OK, IoU 0,975. Inventar åpnet og lukket med den native esken, 280 bilder, null skjermbufferavvik. Før/etter i inventory-knapp-for-etter.png og helt spillbilde i inventory-i-spillet.png.

Fig249_09 er nytegnet med seks Sam-poser og det flate gule VR-sverdet. Egenkontroll fire OK og to SJEKK, ingen FEIL. Separat mottak gir seks OK innen eksisterende tilpasningsgrenser. Raw, prompt, rensing, kildehasher og rutekart for begge nye ark er bevart. Tre bildekall i denne økten: det dupliserte arket, dette Sam-arket og esken. To nye ark, sju nye ruter. Eldre fig249_04 til 08 gir ytterligere 32 nye ruter for modden.

De 38 nye Sam-rutene fra fig249_04 til 09 er logget tegnet og sett i kontaktark fra motoren i rom49. Animasjon 6 og 9 mot høyre bruker en lokal, valgfri QA-utvidelse for retning, som ikke publiseres i motorpatchen. Skjermbildene tas etter den loggede tegningen; etiketter og motor-ruter.json viser den faktiske skjermdumpen. Dette er tvunget avspilling, ikke naturlig gjennomspilling av gåten.

Munndelen costume249_257 består teknisk mottak, men viser tydelige pikseltrinn og en dårlig skjøt med hodet i motoren. Den holdes derfor fortsatt utenfor hd-mod. Kandidaten og hele forsøksarket er bevart her; fig249_02 er gjenopprettet til den tidligere godkjente leveransen fra 1666a2c5. De seks tidligere gangerutene skal beholdes. Ny mottaksrunde må rette bare munndelen og se den sammen med hodet.

Kjent begrensning: de kunstige romhoppene gir 160 skjermbufferavvik ved frame36, før den valgte animasjonen starter. Den publiserte modden gir åtte ved samme kontroll. Etter testhoppet er alle målte bilder uten skjermbufferavvik. Det ekstra avviket er ikke forklart eller løst, og naturlige rombytter er ikke kontrollert her. Det registreres i todo og er ikke grunnlag for å kalle hele motoren feilfri.

Publiseringsgrunnlag: additiv arbeidsmodd fra a6c286bd med 39 nye native PNG-er, 38 Sam-ruter og inventory-esken. Ingen tidligere grafikkfil er endret eller fjernet. Tre eksisterende gangeruter som mottaket ville skrive med ny tilpasning, er beholdt byteidentiske med publisert modd. Modmetadata får ny dato, kostyme001 og 1134 native figurruter. Bevaringskontroll og alle tilleggshasher ligger i bevaringskontroll.json. Ny nedlastingspakke er ikke bygget i denne runden.

Brukte bibliotekskilder ved gjenopptakelsen: losninger/grafikk/figurark-fast-storrelse.md, losninger/bygg/publisert-mod-er-fasit.md og losninger/testing/logg-over-det-som-mangler-hd.md. De gjelder DigHD/ScummVM, men testene i opphavet er ikke automatisk bevis for Sam & Max. Målprosjektets låste ScummVM-base og eksisterende myk.py brukes. Ingen ny løsning, biblioteksendring eller motorbytte er gjort.

Produksjonen ble avbrutt etter første arks lokale mottak. Ved gjenopptakelse kjørte ingen nattevakt eller samarbeid-prosess. Ingen ny bakgrunnsproduksjon er startet. Fremdrift.json skiller levert, kontrollert, importert og godkjent. Direkte opptelling etter de to nye arkene: 105 av 1758 figurjobber har resultat.png, 1653 mangler resultat. Dette teller også eldre ark som må rettes og er derfor ikke antall godkjente ark. Neste ordinære Sam-jobb er fig117_01, Sam på alligatorene ved Gator Golf. Originalen er sett, men arket er ikke generert.
