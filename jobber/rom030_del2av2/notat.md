# rom030_del2av2

Dato: 13. oktober 2026. Ett innebygd image_gen-forsøk for hele rommet. Eksakt modellversjon er ikke eksponert.

## Kilde og motiv

Den roterende restauranten, rom030,416x200 originalpiksler. Kildegrunnlag er begge beskyttede jobbmetadata/originalreferanser og origin/main:docs/gpt-romnotater.csv. SEAFOOD og FRESH FISH er kontrollert bokstavvis. Fisketegningen på skiltet, fiskedekorasjonen ved venstre bås, fiskegarn, lamper, båser/bord og flasker, sentral blå glassylinder med gullkant og den gule tannede gulvkanten er beholdt. Ingen gjester er lagt til i bakgrunnen.

Begge originalpromptene er bevart ordrett med tillegg om fullscene og kildeinnhold. Godkjent kontor er kun stilstøtte. Originalrommet styrer former, plassering og lokal palett.

## Leveranse og kontroll

Råformat1599x984 normalisert globalt med Lanczos til1664x1024. Scene [0,112,1664,800]; resten er #808080. Del1/2 er skåret ved x0/x128. Ferdige jobber1536x1024 har1408 piksler byte-identisk overlapp. Ingen lokal warp, originalpiksler eller konturmasker brukt.

Uendret sjekk_leveranse.py: OK. Åtte beskyttede kilder matcher kildehash.json. Råfil, master, brukte prompter og oppskrift er bevart.

Referanse SHA-256: d81dc3035924eb6fd6d3c2d1e2d905225b060e6c5d7da214811a23cbade4105e
Resultat SHA-256: a1781fd0c5829dbea3d15b9fc9744f5b6af5980f31fc3c0ed99d8d6573af24a5
Master SHA-256: 1898271b6a6b0a676d920941d019726cdfc39a19c79d079341941aff45776e31

Visuell egenkontroll omfatter skilt, plassering av sentralsylinder, båsoppsett, nett/lamper og gulvkant. Små råvareformer i disken, garnknuter og beslag er fortolkninger, ikke bevist detaljidentiske. Fargeflater har jevnere skygger og vindusflaten svak gradient sammenlignet med originalens flate blå.

Runtime=false. Nybildegodkjenning=false. Animert romutsikt, objekt-/kostymelag og faktisk motorvisning gjenstår.
