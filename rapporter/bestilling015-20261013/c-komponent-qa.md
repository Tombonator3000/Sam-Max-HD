# Presis komponentretting, Bestilling 15

Kun nygenererte striper er segmentert etter gul farge, helskalert og plassert. Originalen er ikke brukt som konturmaske. Innebygd ChatGPT imagegen laget nytt veiunderlag; eksakt modellnavn er ikke eksponert. Underlaget er fargematchet mot omkringliggende genererte veipiksler med et affint fargeplan. Veikantene er byte-identiske.

QA-bildet viser original, tidligere kandidat og korrigert kandidat fra venstre. Lengdeavviket er rettet uten nye striper. Ingen runtime eller ny brukergodkjenning.

## obj609_01


## Komponentretting av gul stripe
Generert stripe er alfasegmentert fra tidligere valgt HD, helskalert fra [500, 0, 525, 45] til [500, 0, 524, 40] i lokale HD-koordinater. Nytt imagegen-underlag fjerner tidligere stripe. Ingen originalkonturmaske eller lokal geometriwarp. Endret lerretsboks [738, 464, 767, 511]; alle piksler utenfor boksen er byte-identiske. Veikanter og øvrig vei er uendret. Kontroll: SJEKK. SHA-256: 6113b6c363e13927ba5b95e51740937e2e9746e58b0f1251cbdad68fe63f8fdd. Se rapporter/bestilling015-20261013/c-609-kontroll-etter.txt. Runtime og ny brukergodkjenning er false.

Førkontroll:
```
== obj609_01 (objekt): /home/tombonator3000t/Dokumenter/ChatGPT/Sam&Max HD Remake/Sam-Max-HD/work/.gpt-gren/jobber/obj609_01/resultat.png
SJEKK hele bildet (lerret): skift 0.97, blokker 1.98, kantlikhet 0.94. forskjøvet +0.2, +1.0 originalpiksler; deler av bildet er flyttet eller zoomet (opptil 2.0 px)
   Utfall: SJEKK
```
Etterkontroll:
```
== obj609_01 (objekt): jobber/obj609_01/resultat.png
SJEKK hele bildet (lerret): skift 0.14, blokker 1.98, kantlikhet 0.95. deler av bildet er flyttet eller zoomet (opptil 2.0 px)
   Utfall: SJEKK
```

## obj612_01


## Komponentretting av gul stripe
Generert stripe er alfasegmentert fra tidligere valgt HD, helskalert fra [553, 0, 621, 45] til [560, 0, 620, 40] i lokale HD-koordinater. Nytt imagegen-underlag fjerner tidligere stripe. Ingen originalkonturmaske eller lokal geometriwarp. Endret lerretsboks [791, 464, 863, 511]; alle piksler utenfor boksen er byte-identiske. Veikanter og øvrig vei er uendret. Kontroll: OK. SHA-256: dab4a81759316a26e0cba3779216a4a418e44e3aa312cf6dc143bc01ae89e161. Se rapporter/bestilling015-20261013/c-612-kontroll-etter.txt. Runtime og ny brukergodkjenning er false.

Førkontroll:
```
== obj612_01 (objekt): jobber/obj612_01/resultat.png
SJEKK hele bildet (lerret): skift 1.48, blokker 1.49, kantlikhet 0.98. forskjøvet -1.0, +1.1 originalpiksler; deler av bildet er flyttet eller zoomet (opptil 1.5 px)
   Utfall: SJEKK
```
Etterkontroll:
```
== obj612_01 (objekt): jobber/obj612_01/resultat.png
OK    hele bildet (lerret): skift 0.15, blokker 0.15, kantlikhet 0.99
   Utfall: OK
```

## obj613_01


## Komponentretting av gul stripe
Generert stripe er alfasegmentert fra tidligere valgt HD, helskalert fra [407, 0, 473, 42] til [408, 0, 468, 40] i lokale HD-koordinater. Nytt imagegen-underlag fjerner tidligere stripe. Ingen originalkonturmaske eller lokal geometriwarp. Endret lerretsboks [645, 464, 714, 509]; alle piksler utenfor boksen er byte-identiske. Veikanter og øvrig vei er uendret. Kontroll: OK. SHA-256: 03f9afe5452a751186cefb9142fbc808a9c16d77c31c1a6252acbfaa0a51f54d. Se rapporter/bestilling015-20261013/c-613-kontroll-etter.txt. Runtime og ny brukergodkjenning er false.

Førkontroll:
```
== obj613_01 (objekt): jobber/obj613_01/resultat.png
SJEKK hele bildet (lerret): skift 1.34, blokker 1.31, kantlikhet 0.99. forskjøvet +1.0, +0.8 originalpiksler; deler av bildet er flyttet eller zoomet (opptil 1.3 px)
   Utfall: SJEKK
```
Etterkontroll:
```
== obj613_01 (objekt): jobber/obj613_01/resultat.png
OK    hele bildet (lerret): skift 0.25, blokker 0.30, kantlikhet 0.98
   Utfall: OK
```

Alle 40 beskyttede kildefiler har uendrede SHA-256. Gjenværende veikantavvik er de samme som root-kantmal.json: median venstre/høyre i HD-piksler 609: +1/+9; 612: -3/+1; 613: -1/+5. Ingen nye veikantavvik er innført. Gamle kandidater, raw og kontrollutdata er bevart.
