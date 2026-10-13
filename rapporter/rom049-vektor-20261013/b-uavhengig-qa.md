# Uavhengig QA av rom049

**Resultat:** Ingen avgjørende semantisk feil eller påvist topologisk brudd funnet i den undersøkte kandidaten. Rekonstruksjonen er i samsvar med den særskilt autoriserte vektormetoden. Det gjenstår et synlig forbehold om delvis bevarte trappetrinn, og ingen runtime er kontrollert. Root kjører ordinær teknisk leveransekontroll separat.

Undersøkt kandidat: `rom049-kandidat.png`, SHA256 `1b243b1d5fdd5c8ca1b29c6229b205e28b008585933d74323dc4c105378b45b1`. Kilde: `jobber/rom049/original_1x.png`, SHA256 `ddef15cafec6636d76725dbfb1dee08d4ae2459eaeb99d8eef6462357ea16d3a`. Algoritmen i `rekonstruer.py.txt`, `geometri.json`, SVG og begge rasterbilder er undersøkt. [Detaljkontrollen](b-detaljkontroll.png) viser original til venstre og kandidat til høyre; diagnostiske utsnitt er forstørret med nearest neighbor og har ingen rolle som produksjonsfiler.

## Motiv og utseende

Den rosa himmelen, grønne forgrunnen, blågrønne fjell, lilla slott, mørke hule, brun bakke og guloransje sverd i gråblå stein har beholdt plassering og funksjon. Hulens svarte indre er fortsatt tomt. Ingen nye personer, vegetasjon, skilt eller landskapselementer er innført. Den tilsiktede enkle VR-geometrien er beholdt.

Slottets tårn, øvre mørke vindusrekke, mindre enkeltvinduer, store mørke åpning og forbindelsen til fjellryggen er gjenkjennelig bevart. Vindusformene får glattere skrå kanter, uten at jeg ser et vindu som er fjernet eller lagt til. Sverdets lyse blad, oransje kontur, parerstang, håndtak og knopp er fortsatt tydelige og har samme helning. Hulens inngang og lilla innramming har bevart hovedformene.

**Synlig begrensning:** Enkelte kanter har fortsatt trappetrinn, særlig sverdets diagonaler og deler av fjellene og hulerammen. Andre kanter er nå lange, rene polygonlinjer. Resultatet er derfor ikke jevnt utglattet på alle detaljer. Dette følger av at mange korte grenser og knutepunkter beholdes. Det er et kvalitetsforbehold, ikke i seg selv et nytt motiv eller en påvist topologifeil.

## Algoritme og uavhengig diagnose

Algoritmen tar ut felles fargegrenser fra originalen, deler dem ved knutepunkter, forenkler hver kjede én gang med RDP og gjenbruker samme kjede i begge naboflater. Knutepunktene flyttes ikke. Maksimal RDP-avstand er 0,8 originalpiksel. Små isolerte løkker har en kontroll mot kollaps eller snudd areal. Kilde og vektor har begge 532 regionløkker.

Jeg utførte en separat read-only krysskontroll av de 1256 kjedene, totalt 3709 rette segmenter, med fortegnstest for orientering og romlig indeksering. Den fant **0 egentlige segmentkryss**. Testen regner ikke delte endepunkter som feil og er ikke et fullstendig matematisk bevis mot alle tangeringer, kollineære overlapp eller endret flatenabotopologi. Sammen med gjenbruk av fellesgrenser og det visuelle gjennomsynet gir den ingen indikasjon på ny sprekk eller kryssende grense.

SVG inneholder fargelag med polygonbaner og evenodd-fylling. Det finnes ikke innebygd bitmap, gradient eller ny separat tekstur. De 41 opprinnelige fargene brukes som fyllfarger. Rasteren rendres fra polygonene med supersampling og BOX-nedfiltrering; ekstra rasterfarger langs kantene er dekningsblanding, ikke nye gradientflater. Ingen nye regionløkker opprettes, men forenklingen endrer kantenes lokale areal og form. Det ville være misvisende å kalle resultatet pikselidentisk med originalen.

Som enkel diagnose av dette avviket var 2354 av 64000 originalpikslers sampled midtpunkter forskjellige i 4x-rasteren. Målingen er ikke en kvalitetsgrense og skiller ikke antialiasblanding fra en flyttet grense; den bekrefter bare at rekonstruksjonen faktisk endrer rastergeometri lokalt. Ingen terskler eller produksjonsfiler er endret i QA.

## Mottaksgrense

Kandidaten kan etter denne uavhengige gjennomgangen gå videre til roots tekniske kontroll og samlede vurdering, med trappekantforbeholdet oppgitt. Runtime, import, spillinteraksjon og ny individuell bildegodkjenning er ikke verifisert. Jeg har bare skrevet denne rapporten og det diagnostiske detaljbildet.
