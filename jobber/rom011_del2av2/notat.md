# rom011_del2av2

Dato: 13. oktober 2026. Innebygd image_gen; eksakt bildemodell er ikke eksponert. Ett fullsceneforsøk, ingen lokal retting.

## Kilde og motiv

Snuckey's inne. Oransje disk og fem røde/oransje krakker, hyller med varer, vindusruter, donut-glassfelt, karusellstativ, klær og hengende varer. Hovedskiltet fountain er kontrollert. Prompttillegget sa ved en tellefeil fire krakker; originalen og levert bilde viser fem, inkludert den delvis skjulte bakerst. Kilden og det leverte bildet går foran den feilaktige teksttellingen.

Kildegrunnlag: beskyttet jobbmetadata og originalreferanser, samt origin/main:docs/gpt-romnotater.csv ved 3df35f636f123584e4a8d454871fb9318f995d35. Begge deler er sett før produksjon. Godkjent stil/rom007_del1av2.png er kun stilanker. Begge originale prompt.txt er bevart ordrett i rom011-prompt.txt med presisering for én fullscene.

## Plassering og kontroll

Felles fullscene sikrer byte-identisk overlapp på 1152 piksler. Resultatet er 1536 x 1024, scene [0,112,1536,800] og eksakt #808080 padding. Hele generert panorama er normalisert med Lanczos til kildeformat, uten lokal geometriwarp. Delene er klippet fra samme master etter jobbens region.

Uendret verktoy/sjekk_leveranse.py: OK. Kontrollutdata er bevart som rom011_del2av2-kontroll.txt. Alle 16 beskyttede kildefiler for disse fire jobbene er kontrollert mot kildehash.json uten avvik.

Referanse SHA-256: 7198a86fa8e0ad0c1aa33219d9c1813b0269171c429a897eadcfecfaed9a3030
Resultat SHA-256: bbf0b63bebf79ca811594e36bc785a81f734bf4249ab9501ddff18f7229462b0
Master SHA-256: d243d99de69619dd5a43dbd3775a757b0c431fb681333e4adcf46debb96085f0

Visuell egenkontroll omfatter fullscene, hovedformer, skilt og overlapp. Små emballasjefigurer, varenes detaljer og plakatenes små tegn er tolkninger av lave pikselmengder; de er ikke bekreftet bokstav-/detaljidentiske. Nytegningen har jevnere og noe sterkere skygger enn kilden.

Runtime: ikke utført. Nybildegodkjenning fra Tom: ikke gitt. Dette er arbeidsasset med teknisk og visuell egenkontroll, ikke dokumentert ferdig motorintegrasjon.
