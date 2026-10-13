# Rom049, presis vektorrekonstruksjon

Tom valgte uttrykkelig «Bruk presis vektorrekonstruksjon for VR-rommet» 13. oktober 2026. Fem bildeforsøk hadde ekstra fasetter og gradienter og ble visuelt avvist. Ny leveranse bruker kildebaserte SVG-flater, ikke et nytt bildeforsøk eller oppskalert originalbitmap.

Python 3, numpy og Pillow henter originalens 41 farger og sammenhengende fargegrenser. Felles grenser forenkles én gang og gjenbrukes på begge naboflater. Knutepunktene står på kildekoordinater, største tillatte kjedeforenkling er 0,8 originalpiksel. Alle 532 rasterregionløkker består; dette er et topologimål, ikke et anslag over antall designfasetter. SVG har ingen innbakt raster, gradient eller tekstur. PNG rendres fra de samme vektorbanene med antialiasdekning langs kanter. Ingen generert tegning er maskert med originalsilhuetten.

Uendret egenkontroll: OK, skift 0,01, blokk 0,07 og kantlikhet 1,00. Root og uavhengig Astra-QA har sett original/HD. Hule, sverd, slottvinduer og kildepalett er bevart. Separat diagnose fant ingen egentlige segmentkryss, uten å være et fullstendig topologisk bevis.

Enkelte trappetrinn består ved små, tette knutepunkter, særlig sverdet og noen fjell-/hulekanter. Resultatet er ikke jevnt utglattet eller pikselidentisk overalt. Dette forbeholdet er bevart. Fire beskyttede jobbfiler er SHA-uendret. Råforsøk og tidligere avviste kandidat finnes i historikken og rapportene.

Detaljer, master, oppskrift, brukerens metodevalg og uavhengig QA: rapporter/rom049-vektor-20261013/. Totalt fem bildeforsøk og én vektorrekonstruksjon. Eksakt bildemodell for avviste forsøk var ikke eksponert; denne leveransen er vektorrendret. Individuell bildegodkjenning, originalmasker, dynamisk palett, motorimport og faktisk spillvisning er ikke verifisert.
