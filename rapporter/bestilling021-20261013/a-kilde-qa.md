# Bestilling 21 A: kilde og resultat

Fire kandidater er kontrollert samlet i [kontaktarket](a-samlet-kontaktark.png). Rom089 er OK, rom092 er SJEKK. Rom090 og obj901_01 er fortsatt FEIL og ikke klare for mottak. [Manifestet](a-leveranser.json) skiller disse statusene. Ingen runtime, import eller ny individuell brukergodkjenning er utført.

## Identitet og kildekorrigering

Originalreferanse, original_1x, metadata og C sin kildeplan styrer motivet. Alle 40 beskyttede filer er uendret, dokumentert i [hashkontrollen](a-kildehashkontroll.json). Kildekorreksjonen står separat etter den ordrette jobbprompten i hvert lagret genereringsprompt. Første forsøk brukte godkjent stil/rom007_del1av2.png; andre forsøk for 090 og 901 brukte bare riktig originalreferanse.

* Rom089: hyssingnøstet fra egen vinkel, øvre trikkeplattform, sti og høyre tretrapp. TRAM, to MUSEUM-skilt og røde venstrepiler er beholdt. Utydelig liten tekst ved foten er ikke tillagt nye ord. Skiltet på nederste høyre felt er rødt som i kilden.
* Rom090: avskåret Sam-hode med hatt og to separate Max-ører i blått felt. Hyllemotivene er mørke silhuetter. Ingen hele figurer, Max-ansikt eller pistoler er lagt til. Det generiske navnet med pistoler er ikke bildebevis. Nederste midtre draperi har ny foldfordeling og er det målte problemfeltet.
* Rom092: oransjebrun hårform med enkel krøll på skrå støtte og brun sokkel i varmt rødt lys. Ingen levende øyne, person eller kropp. SJEKK: skift 0.26, blokk 1.26, kant 0.91.
* Obj901_01: egen tom tilstand uten hår eller støtte. Ikke en blind utklipping av rom092. Nytegningen har en for jevn mørk søm og tydeligere oval sokkelrand enn kilden. Kandidaten er derfor uavklart både teknisk og visuelt.

## Forsøk og fargebehandling

089 og 092 har ett fullforsøk hver. 090 og 901 har to fullforsøk hver. Alle råbilder, prompter og SHA-er er bevart i manifestet. Eksakt bildemodell er ikke eksponert av image_gen.imagegen.

Én kildebegrunnet global fargeforenkling ble prøvd etter egen autorisasjon. Kildens faktiske 41 henholdsvis 8 RGB-farger bekrefter de flate feltene. Hver NYGENERERT motivpiksel fikk nærmeste palettfarge etter euklidsk RGB-avstand. Det ble ikke brukt kildekoordinater, originalpiksler som billedinnhold, konturmasker, lokale flytt eller gjentatte terskelsøk. Grå padding ble ikke endret. [Oppskrift](a-palettoppskrift.py.txt) og [alle tall/paletter](a-palettbehandling.json) er bevart.

090 gikk fra 34 413 til 41 farger; 614 288 piksler ble endret, gjennomsnittlig absolutt RGB-endring 6.10385. Kontroll før: FEIL 0.38/5.28/0.95. Etter: FEIL 0.29/21.27/0.93. 901 gikk fra 7 637 til 8 farger; 262 002 piksler endret, gjennomsnitt 2.85130. Før: FEIL 0.66/35.37/0.96. Etter: FEIL 8.15/2.29/0.97. Rekkefølgen er globalt skift, maksimalt blokkskift og kantlikhet.

Mapping endrer ikke pikselposisjoner, men fjerner antialiasingens mellomtoner og gir hardere, enkelte steder hakkete synlige overganger. Den løste ikke kontrollfeilene. Før-palettvariantene er derfor gjeninnsatt som lagrede, uavklarte kandidater. Palettkandidatene er bevart separat som a-rom090-palettkandidat.png og a-obj901_01-palettkandidat.png.

[Blokkdiagnosen](a-blokkdiagnose.json) viser 090 sitt største avvik i originalrektangelet [106,60,106,60], nederste midtfelt. 901 har særlig ustabil korrelasjon i svært flate rødfelt, men det fritar ikke den synlige sokkel-/sømforskjellen. Tallene er ikke runtime-bevis og dokumenterer ikke at motivet er godkjent.

## Format og etterprøving

Alle fire er RGB 1536 x 1024 med nøyaktig RGB 128 utenfor metadatarektangelet. Valgte råforsøk hadde korrekt canvas, så motivet er klippet etter bilde_i_lerret og lagt uendret på ny nøytral bakgrunn. Første, forkastede 090-forsøk hadde motivboks [36,256,1500,802] som ble helskalert til 1280 x 480; dette forsøket er bevart, men ikke valgt. Ingen lokal warp eller originalkonturmaskering er gjort.

Uendret sjekk_leveranse.py er kjørt på de endelig lagrede kandidatene. [Sluttføringsoppskriften](a-sluttforing.py.txt) dokumenterer kandidatvalg, kontroll, padding, kildehash og manifest. Root håndterer videre samlet mottak og eventuell avklaring av FEIL-jobbene.
