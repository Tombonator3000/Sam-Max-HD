# Kilde-QA, bestilling 14 A

Original1x og referanse4x, metadata, ordrette prompter, GRUNNLAG og b-kildeplan er lest før tegning. Faktiske promptbytes er låst og beholdt. Det historiske metadataavviket omtalt av root er ikke reparert eller tolket som lokal endring.

Obj598_01 er b-stars: små flerfargede lysklaser på svart. Obj599_01 er b-star-sign: nærlesing viser GO TO BUMPUSVILLE som punktglyfer. Ingen ny sammenhengende font eller gjettet fritekst er lagt til. Dette er originalnærlesing, ikke runtime-kobling.

## Komponentmetode og begrunnelse

8-nabosammenheng i originalens ikke-svarte piksler gir 88 kildegrupper i 598 og 144 i 599. Gruppeantall betyr sammenhengende kildeklaser, ikke nødvendigvis antall blink eller individuelle lyspærer. Kildens delvis berørende prikker kan tilhøre samme gruppe.

Første fullgenerering ga teknisk OK. 598 hadde 88 nye lyskomponenter; 599 hadde 160 ved lysgrense48, med 11 kildegrupper delt i 2 til 4 nye punkter og ingen manglende kildematcher. Komponentenærlesing fant imidlertid tap av interne farger, hvor flerfargede klaser ble monokrome. Fullbildene er derfor bevart som forkastede fargekandidater, ikke brukt i sluttbildene.

Andre forsøk bruker kildeatlas med 88 respektive 144 store referanseruter. Disse rutene inneholder forstørret kilde bare som referanse. Innebygd imagegen nytegnet hver rute i glatte flerfargede lysformer. Sluttbildene bruker UTELUKKENDE pikselinnhold fra de nye genererte atlasene, svart bakgrunn og grå padding. Ingen originaloppskalering er levert.

For hver kildegruppe finnes en fast kobling til samme nummererte nye rute. Ny komponent klippes rektangulært etter sin egen lysutstrekning, samlet skaleres til kildens boks ganger fire og plasseres på eksakt kildekoordinat. Lysgrense32 brukes bare til å finne generatorens klippeboks med to pikslers margin, ikke som pikselmaske. Ingen originalsilhuettmaskering, recoloring fra originalpiksler eller lokal warp. Oppskriften leser boksmetadata og genererte atlas, ikke originalbildene.

598 har ingen overlappende gruppebokser. 599 har tre par overlappende kildebokser: 99/103, 125/132 og 132/138. Nytegnet svart skal ikke overskrive lys i en annen gruppe; derfor kombineres overlapp med maksimum per fargekanal. Dette er vanlig komposisjon av NYE komponenter, ingen originalmaske. Alle 88/144 grupper finnes i sluttbildet, med én generert rute per kildegruppe og ingen manglende ruter. Antall interne glødlober kan fortsatt variere innen en gruppe og påstås ikke å være originalens blinkantall.

## Kontroll og begrensninger

Slutt-punktkobling.json viser kilde-ID, kildeboks, ny rute, ny klippeboks, målrektangel og hash av den nye skalerte komponenten. Slutt-komponent-qa.png viser original/ny parvis for ALLE grupper. Begge genererte atlas og begge sluttbilder er sett visuelt. Intern flerfarget struktur er klart bedre bevart enn i første forsøk. Lysfordeling, glød og avrundede underformer er nytegnet, ikke numerisk identiske med 1993-paletten.

Uendret egenkontroll gir 598 OK 0.02/0.06/0.98 og 599 OK 0.02/0.05/0.95. Alle 44 låste kilder er verifisert uendret. Canvas 1536 x 1024 RGB og padding nøyaktig128. Se a-leveranser.json, a-kildebevis.json, a-samlet-qa.png og a-oppskrift.py.txt. Eksakt bildemodell er ikke eksponert. Runtime, import, dynamisk palett og timing er ikke prøvd; ny individuell brukergodkjenning=false.
