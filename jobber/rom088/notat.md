# rom088 – HD-leveranse

Innebygd ChatGPT-bildegenerator brukt. Eksakt bildemodellnavn er ikke eksponert. 1 forsøk; valgt forsøk 1.

Space Needle, asymmetriske totemvinger og stablede ansikter, store trær, hvite bygninger og klokke er bevart. Synlig ARKET begynner ved avklippet venstrekant uten ny M. PUBLIC er fortsatt delvis skjult av vingen; det er ikke laget et frittstående komplett skilt. Totemets små øyne/tenner og fjærstreker er glattet, og klokkeviserne følger samme generelle retning; de minste kildepikslene gir ikke bevis for hvert ornament eller presis klokketid.

Originalreferanse og godkjent stil/rom007_del1av2.png ble brukt til første forsøk. Stilankeret styrer kun strek/penselnivå; innhold, farger og geometri kommer fra originalen. For obj839 forsøk 2 ble kun originalen brukt. Alle faktiske prompter og råforsøk er bevart i rapportmappen.

Plassering [x,y,b,h]: [128, 112, 1280, 800]. Kun presist rektangelklipp og helskalering av nygenerert motiv, der nødvendig; ingen originalmasker, geometriwarp eller vektorrekonstruksjon. Padding er bytekontrollert RGB 128 på 1536 x 1024. Se c-oppskrift.py.txt.

Resultat SHA-256: `bd81b5dd27825bcfbe1b3073b7260a68c035a031f432d0f17c36e5dfc1a53e37`.

Uendret egenkontroll:
```
== rom088 (rom): jobber/rom088/resultat.png
OK    hele bildet (lerret): skift 0.08, blokker 0.17, kantlikhet 0.96
   Utfall: OK
```

Samlet original/HD-vurdering finnes i c-samlet-qa.png og c-kilde-qa.md. Teknisk OK er ikke ny individuell brukergodkjenning. Import, spillruntime og faktisk lagkomposisjon er ikke testet.
