# Kilde- og motiv-QA, Bestilling 18 C

Bare obj780_01 og obj781_01 er endret. Bestilling 15, 17 og ulåst 077-master er urørt. GRUNNLAG.md manglet ved første lesing; direkte bestilling og b-kildeplan ga tilstrekkelig avgrensning.

Originalene er 320 × 72, begge motivfelt [128,368,1280,288] på 1536 × 1024 RGB128. Ressursregisteret angir credit-panel-5 og -6. Dette er selvstendige gråillustrasjoner uten tekst, ikke en samlet scene. Source-promptmetadata har tidligere registrert hashavvik; nåværende låste promptbytes er brukt ordrett, beskyttede filer er urørt.

780: Max i dynamisk sammenstøt med kurver, stjerner og tre runde småformer til venstre, Sam med bok til høyre. Småformenes fortellingsrolle er usikker. Sam/Max-identitet, klipp og store overlapper er bevart. Første raw var for lyst; source-only andre raw er valgt og tonet globalt. Kontroll OK 0.07 / 0.13 / 0.93.

781: skrå by-/bilbakgrunn, Max i midten og Sams store forgrunnshode med hatt/snute/tenner. Ingen nye figurer eller tekst. SJEKK 1.12 / 1.95 / 0.72. Det betyr reelt usikker lokal justering; ikke oppgradert til OK. Ingen global flytting/warp for å jage FFT. Hovedkomposisjon er visuelt bevart; fin plassering/konturer er ikke identiske.

Begge genereringer var for lyse. Root autoriserte global monoton tonekomprimering av nygenerert motiv. Formler og faktiske min/maks er bevart i c-tonebevis.json. 780 før 1.33–138, etter 0–99; 781 før 0–178.33, etter 11–147. Hele RGB-bildet er grått etterpå. Ingen kildepiksler/masker er brukt i sluttmotivet. Min/maks alene beviser ikke fordeling: median 780 er 24 mot original35, 781 er 55 mot original47. Samlet visuell QA viser 780 noe mørkere mellomtoner og 781 noe lysere mellomtoner; dette er dokumentert, ikke skjult med lokal histogrammatching. Ingen neon eller kontraststrekking til hvitt.

c-samlet-qa.png er sett ved sluttkontroll; kildens og HDs klipp/størrelsesforskjeller og gråvarianter er sammenlignet. Padding og gråkanallikhet er målt. Alle 40 beskyttede kilder er SHA-uendret. Råforsøk, komplette prompter, før-tone-motiver, tonebevis og reproduksjonsoppskrift er bevart.

Ingen runtime, kredittrekkefølge, faktisk palettstyring, import eller ny individuell brukergodkjenning er testet. Eksakt bildegeneratormodell er ikke eksponert av verktøyet.
