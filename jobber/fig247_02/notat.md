# fig247_02

Dato: 2026-10-16T06:18:39.351524+02:00

Verktøy: innebygd image_gen.imagegen. Modellnavnet vises ikke. Python, Pillow, numpy og scipy er brukt til tillatt rensing, alfa og presis plassering. Ingen pipelinekode er endret.

Kostyme 247 i rom48. Sam holder Max vannrett mens VR-kablene endrer form. Returen gjelder bare de grønne båndene over den svarte hjelmkuppelen. Originalen og fig247_01/03 til 05 viser grønnstripet kuppel. Ett nytt bildeforsøk for båndene. Bare de nytegnede grønne båndene er tatt inn med Pillow og numpy. Alle andre RGB-piksler er uendret utenfor båndområdene. 3558 RGB-piksler er endret, og hele alfakanalen er bitidentisk med førbildet. Grep, Max, Sam, visir, kabelstillinger, rutestørrelser og plassering er bevart. Egenkontrollen har fortsatt den allerede eksisterende omrissmerknaden på costume247_1926, snitt/union 0,75. Tre ruter OK, én SJEKK, ingen FEIL. Claude må vurdere denne merknaden separat fra den rettede fargereturen.

Original_1x.png, referanse.png og relevante godkjente hovedark er sett før nytegning. hovedark/sam.png styrer Sam-identitet og strek. For kostyme247 er hovedark/max.png bilde tre. Originalen styrer motiv, drakt, lokal palett, positurer og tilstander. Sam har VR-hjelm i kostyme247; den generiske prompten beskriver fedora og begge figurer også når de ikke er synlige. Rettet prompt og kildebegrunnelse er bevart separat i rapporten. Beskyttede jobbfiler er uendret.

Nytegningens egen alfa er renset. Svak løs bakgrunnssmitte er fjernet, myke kanter beholdt og farge langs svært svake kanter renset. Returarket er ikke skalert eller flyttet; bare båndenes RGB er skiftet. Originalmasken brukes bare til kontroll og målbokser, aldri til å klippe produksjonstegningen. Hele lerretet er 1536 x 1024 med ekte alfa. Rutekartet følger faktisk alfa over 128 og inkluderer frakoblede deler.

Egenkontroll: SJEKK. Systemets python3 mangler numpy. Samme kontrollskript er derfor kjørt med den eksisterende /home/tom/Sam-Max-HD/.venv/bin/python3 uten installasjon. Kontrollutskrift: rapporter/natt-fire-20261016-0610/fig247_02-egenkontroll.txt.

Statisk visuell egenkontroll er utført mot original og stilreferanser. Dette er levering til Claudes mottakskontroll. Import, motoravspilling, animasjonstiming og Toms godkjenning er ikke utført. Eventuelle forskjeller i geometri og strek innenfor originalboksene må vurderes ved mottaket.

Rapport, råforsøk, korrigerte prompter, plassering og rutekart: rapporter/natt-fire-20261016-0610/.

SHA-256: 7ea6eef6a69901027b009cce020cc54d3184e89d7110ae45f700e8f8f5b9409b
