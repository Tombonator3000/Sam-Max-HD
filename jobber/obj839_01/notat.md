# obj839_01 – HD-leveranse

Innebygd ChatGPT-bildegenerator brukt. Eksakt bildemodellnavn er ikke eksponert. 2 forsøk; valgt forsøk 2.

Egen tett skogstilstand, med flere mørke grantrær i himmelfeltene. Ikke produsert som klipp av rom086. Skilt og tak har samme identitet, men separate originalstyrte avkuttinger. Nedre kant stopper i tak-/skiltområdet uten bro eller plen. Forsøk 1 avvist: FEIL 2,27 / 3,43 / 0,58 og feil proporsjoner/plassering. Forsøk 2 er nytegnet fra originalreferansen alene og valgt. Ingen forskyvning eller lokal warp for å jage kontrollmål.

Originalreferanse og godkjent stil/rom007_del1av2.png ble brukt til første forsøk. Stilankeret styrer kun strek/penselnivå; innhold, farger og geometri kommer fra originalen. For obj839 forsøk 2 ble kun originalen brukt. Alle faktiske prompter og råforsøk er bevart i rapportmappen.

Plassering [x,y,b,h]: [160, 304, 1216, 416]. Kun presist rektangelklipp og helskalering av nygenerert motiv, der nødvendig; ingen originalmasker, geometriwarp eller vektorrekonstruksjon. Padding er bytekontrollert RGB 128 på 1536 x 1024. Se c-oppskrift.py.txt.

Resultat SHA-256: `61c7ed8ac7eca5d585517aca6a897523d284dcf9417dcd3f1affc68310310f32`.

Uendret egenkontroll:
```
== obj839_01 (objekt): jobber/obj839_01/resultat.png
OK    hele bildet (lerret): skift 0.03, blokker 0.10, kantlikhet 0.96
   Utfall: OK
```

Samlet original/HD-vurdering finnes i c-samlet-qa.png og c-kilde-qa.md. Teknisk OK er ikke ny individuell brukergodkjenning. Import, spillruntime og faktisk lagkomposisjon er ikke testet.
