# Bestilling 53 – Sam og Max

14. oktober 2026. Ti hele figurark med 137 ruter er mottatt: seks Sam004-ark (71 ruter) og fire Max003-ark (66 ruter). Uendret kontroll gir ni OK og én dokumentert SJEKK. De faktiske filenes hash og status står i `fremdrift.json`.

## Kildetro gjenbruk og nytegning

Alle 71 Sam004-ruter har identiske synlige RGB-kildebilder med de tilsvarende Sam002-rutene. Rot har kontrollert hvert kildetreff, metadata og hver ny RGBA-komponent uavhengig. De fire første arkene er hele byteidentiske donorfiler; de siste to er pakket fra eksisterende nye komponenter uten resampling. Cel 169/170 har rel_x -19 i kostyme 4 mot -18 i kostyme 2. Dette er beholdt som metadataforskjell, ikke skjult ved å flytte tegningen. Palettindeks 14 skiller seg, men de aktuelle kildebildene har identiske RGB-farger. De to små øyelokksrutene 512/513 er kontrollert særskilt som to brune komponenter hver. Alle seks feltark og rel-sammensettinger er sett av rot.

Max003-arkene følger det godkjente hovedarket og piloten. De bevarer egne talehoder, gangstillinger, separate hender, hodeløse kropper og bakhoder. Rot har sett alle ni feltark og 25 statiske rel-sammensettinger; de endrede feltene er sett på nytt etter siste retting. Tre talehoder fikk rosa nese og riktig munnvariant gjennom lokal nytegning av hele separate hoder. To andre cels fikk fjernet en ekstra rosa neseflekk med små rektangulære utsnitt fra en nygenerert snutekant. Rot har kontrollert at resten av arkene er byteidentiske før og etter disse rettingene. Det første inntrykket av manglende nese i cel 175 var feil: en liten rosa nese var allerede til stede og er bevart.

## Kontroller og gjenværende forbehold

40 beskyttede jobbkilder og sju Max-ankre er uendret. Alle ark er ekte RGBA 1536 × 1024. Rot har kjørt uendret checker på sluttfilene og kontrollert kildehash, donorfiler, råbilder, eksakte prompter og rettingenes avgrensning. De åtte Max-generatoranropene er registrert, også to ubrukte mellomforsøk. Innebygd ChatGPT imagegen ble brukt; eksakt bildemodellnavn er ikke eksponert.

`fig003_03` beholder SJEKK fordi checker hopper over halsskjøtene 551/552 og derfor teller 504 tilsiktede piksler som løse. Uavhengig måling viser nøyaktig 239 + 265 piksler i disse to 36 × 8-boksene og null øvrige avvikspiksler. Variantene har hver sin grå/kremhvite innertone. Rutene er ikke krympet eller fjernet for å endre kontrollutfallet.

`fig003_04` har 23 antialiaspiksler med alfa 1–126 like utenfor cel 179 sin eksakte synlig-boks etter neserettelsen. De ligger innenfor komponentens kontrollerte kantvindu, har ingen kjernepiksler med alfa ≥128 utenfor boksen og berører ikke nabocels eller padding. Alle øvrige Max-ark er helt transparente utenfor sine eksakte bokser. Sam-arkenes svake magenta-RGB-rester med alfa 1 er arvet byteidentisk fra de mottatte donorene. Ingen synlig bakgrunn eller grå padding er tegnet inn.

HD-streker og enkelte finger-/munnkurver er rundere enn originalens få piksler. Statiske rel-bilder viser lag og plassering, men beviser ikke animasjonstiming. Ingen motorimport, spilltest eller ny individuell brukergodkjenning er utført. Tidligere motivavklaringer er fortsatt åpne; denne leveransen lukker dem ikke.
