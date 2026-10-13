# rom015_del2av2

Dato: 13. oktober 2026. Innebygd image_gen; eksakt bildemodell er ikke eksponert. Ett fullsceneforsøk og én avgrenset innebygd bilde-edit. Første D i ODDITIES var feilaktig P. Rettet generert bokstavutsnitt er plassert presist i fullscenen; begge deler er deretter skåret på nytt. Råforsøk2, rettingsprompt og oppskrift er bevart. Rettet skilt er inspisert i rom015-skiltkontroll-rettet.png.

## Kilde og motiv

Karnevalinngangen. Kiosk, klovneformet søppelbøtte, skjeve telt, karikert inngangshode, sideplakater, karusellarm, grønt telt, gjerde og vegetasjon. KUSHMAN BROS SHOWS, CLOSED, HALL of ODDITIES, WEIRD og CREEPY er kontrollert. Delvis skjult høyreskilt er ikke fullført.

Kildegrunnlag: beskyttet jobbmetadata og originalreferanser, samt origin/main:docs/gpt-romnotater.csv ved 3df35f636f123584e4a8d454871fb9318f995d35. Begge deler er sett før produksjon. Godkjent stil/rom007_del1av2.png er kun stilanker. Begge originale prompt.txt er bevart ordrett i rom015-prompt.txt med presisering for én fullscene.

## Plassering og kontroll

Felles fullscene sikrer byte-identisk overlapp på 544 piksler. Resultatet er 1536 x 1024, scene [0,112,1536,800] og eksakt #808080 padding. Hele generert panorama er normalisert med Lanczos til kildeformat, uten lokal geometriwarp. Delene er klippet fra samme master etter jobbens region.

Uendret verktoy/sjekk_leveranse.py: OK. Kontrollutdata er bevart som rom015_del2av2-kontroll.txt. Alle 16 beskyttede kildefiler for disse fire jobbene er kontrollert mot kildehash.json uten avvik.

Referanse SHA-256: 9cf361d28b35797a817de5c97c56093bbc07245cadc2454a28199ba3b1bf49f2
Resultat SHA-256: 5b027a50d43522adcbf50cddb100602f3b62bc614022014592e0ed574c66366c
Master SHA-256: 28d1aa8a7271750ed684821268a3ab6758cc2e2d675a135bae11ab11416119c1

Visuell egenkontroll omfatter fullscene, hovedformer, skilt og overlapp. Små emballasjefigurer, varenes detaljer og plakatenes små tegn er tolkninger av lave pikselmengder; de er ikke bekreftet bokstav-/detaljidentiske. Nytegningen har jevnere og noe sterkere skygger enn kilden.

Runtime: ikke utført. Nybildegodkjenning fra Tom: ikke gitt. Dette er arbeidsasset med teknisk og visuell egenkontroll, ikke dokumentert ferdig motorintegrasjon.
