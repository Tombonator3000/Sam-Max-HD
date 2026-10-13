# rom087 – HD-leveranse

Innebygd ChatGPT-bildegenerator brukt. Eksakt bildemodellnavn er ikke eksponert. 1 forsøk; valgt forsøk 1.

Pyramidetårn, lyst sylindrisk tårn, to røde store brotårn, røde kabler, rød/gul sporvogn, bukt og barskog er bevart i originalens tegnede geografi. Ingen foto eller ny bygeografi brukt. Små bygnings-/vindusstreker og granhøylys er renere og mer regelmessige enn originalens piksler; eksakt individuell vindusidentitet i de minste bakgrunnsfeltene er ikke bevist av kontrollen.

Originalreferanse og godkjent stil/rom007_del1av2.png ble brukt til første forsøk. Stilankeret styrer kun strek/penselnivå; innhold, farger og geometri kommer fra originalen. For obj839 forsøk 2 ble kun originalen brukt. Alle faktiske prompter og råforsøk er bevart i rapportmappen.

Plassering [x,y,b,h]: [128, 112, 1280, 800]. Kun presist rektangelklipp og helskalering av nygenerert motiv, der nødvendig; ingen originalmasker, geometriwarp eller vektorrekonstruksjon. Padding er bytekontrollert RGB 128 på 1536 x 1024. Se c-oppskrift.py.txt.

Resultat SHA-256: `1647f42f1867cdb69b4d3a7ac3a471b052f7de4e99cb40fa83ec05f6ec5ecb46`.

Uendret egenkontroll:
```
== rom087 (rom): jobber/rom087/resultat.png
OK    hele bildet (lerret): skift 0.02, blokker 0.11, kantlikhet 0.97
   Utfall: OK
```

Samlet original/HD-vurdering finnes i c-samlet-qa.png og c-kilde-qa.md. Teknisk OK er ikke ny individuell brukergodkjenning. Import, spillruntime og faktisk lagkomposisjon er ikke testet.
