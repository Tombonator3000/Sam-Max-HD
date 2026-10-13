# rom008

Dato: 2026-10-13. Verktøy: innebygd ChatGPT image_gen. Eksakt bildemodell vises ikke i verktøyet og påstås ikke. To genereringsforsøk, inkludert lokal dørtekstkorreksjon. Astra håndterte produksjonsoppgaven.

Gangen utenfor kontoret: to høyredører, trapp og balustrader, to lyse buevinduer, olivengrønn vegg og løper med rød kant. Fremre dør har Flint / Paper. Bakre dørtekst er for liten for sikker transkripsjon; formene er behandlet som kildeformer.

Kilde: jobb.json, referanse.png og original_1x.png i denne jobben, samt romnotater fra origin/main. Samtlige lokale inputbilder er visuelt sett. Godkjent stilanker: stil/rom007_del1av2.png, kun strek og penselnivå. Ordrett originalprompt og nødvendig kildepresisering er bevart i rapporter/bestilling002-20261013/rom008-prompt-brukt.txt. Beskyttede jobbfiler er ikke endret.

Grå padding er satt eksakt til RGB 128 uten endring av bilderektangelet.

Egenkontroll med uendret verktoy/sjekk_leveranse.py: OK. Logg: rapporter/bestilling002-20261013/rom008-egenkontroll.txt. Visuelt sammenlignet med original i 1x og 4x, samt fullscene og skjøt for gatebildene. Store landemerker, romtopologi, palettfamilier og lesbar skilttekst er beholdt. Små tegnete slitasjemerker og bakre gangdørtekst er ikke bevist identiske på detaljnivå. Teknisk OK er ikke Toms nye bildegodkjenning.

SHA-256 resultat: 37c6e4ee90282d035890d80047931f305946de049447a12e4a1a65e6062b514b
SHA-256 råforsøk: 7802efee199ae7b956e1d8dd5e21db2aeea746660c80f055080219b56a1e7579
Råforsøk: rapporter/bestilling002-20261013/rom008-raa-1.png

Runtime, maskesamspill, import og visning i motor: UVERIFISERT. Disse kontrollene tilhører mottaket hos Claude. Ingen kode, pipeline, Git eller andres leveranser er endret.

Korreksjon 2026-10-13: Første forsøk hadde dekorative løkker som ikke finnes i kilden. Innebygd image_gen laget en smal rettelse til enkle mørke, uleselige tegnklaser. Ingen ord er gjettet. Bare rektangelet [886,373,911,434] ble lagt inn fra råforsøk 2. Array-kontroll bekrefter at alt utenfor boksen er byte-identisk med forrige leveranse. Original, før og etter er vist i rapportens rom008-doortekst-qa.png. Ny egenkontroll: OK, skift 0.03, blokk 0.30, kantlikhet 0.97. Eksakt bokstavidentitet er fortsatt uavklart og påstås ikke.
