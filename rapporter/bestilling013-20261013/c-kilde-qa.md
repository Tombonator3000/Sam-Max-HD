# Bestilling 13 C – kilde-QA

Begge panoramaer, alle fire referanser og nærbildet av tjæredyrene er undersøkt før generering. Kildens brune hode med hvite tenner og separate fot-/kloform er dyreformer; eksakt art er uavklart. Ingen badende barn er innført. Tre købarn har ulike hår/klær, og kilden viser også en delvis skjult figur ved sklietoppen. Skiltene TARPIT SLIDE, BUNGEE og YOU / MUST / BE / THIS / TALL er bevart.

Rom061 er tom, med heisfelt, skiftelskjerm, skjev plattform og hengende sele. Ingen personer eller ny tekst. Originalens hovedformer, skyprofil og trær er visuelt sammenlignet med den ferdige masteren. Begge utsnitt OK; framtidig del 2 ligger kun i rapportens kontrollmappe med kopier av beskyttede referansefiler, ikke i jobbmappen.

Rom060 forsøk 1 hadde FEIL med 2.7 pikslers blokkforskyvning. Forsøk 2 er omtegnet: del 1 OK, del 2 SJEKK (skift 0.53, blokk 1.06, kantlikhet 0.91). Verst blokk i del 2: x 256, y 100, 128 × 100 originalpiksler. Dette gjelder faktisk tegnet struktur; intet er flyttet lokalt for å jage FFT. Samlet QA må behandle SJEKK som avvik, ikke OK.

Master060 1760 × 800, delskift 224, overlapp 1312 × 800. Master061 1952 × 800, delskift 416, overlapp 1120 × 800. Begge overlapper målt byte-identiske. Én helgenerering per master, derfor ingen sammensatt skjøt. Rå060 1860 × 845 og rå061 1959 × 803 er helskalert til kontraktstørrelsene; ingen lokal warp/maskering. Alle 44 kildehash er kontrollert uendret. Runtime, dynamisk palett og ny individuell brukergodkjenning er uverifisert.
