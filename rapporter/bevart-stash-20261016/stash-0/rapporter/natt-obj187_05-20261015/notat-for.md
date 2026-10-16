# obj187_05

Dato: 2026-10-13. Astra-produksjon med innebygd ChatGPT image_gen. Eksakt bildemodell ikke eksponert. Forsøk: 2.

Sam slår mot fremre venstre hull med rød treklubbe. Hånd og klubbe dekker begge venstre hull; tre hele hull synlige.

Originalreferanse1x/4x og jobb.json bestemmer innhold, kildepalett, avkutting og geometri. Hovedark for Sam/Max og rom018-HD er visuelt lest som identitets-/stilgrunnlag, uten å overstyre variantuttrykket. Rød treklubbe, orangebrun Sam, grålilla frakk, lys mansjett og blåsvart slips videreføres. Ingen rotter eller nye fingre. Ordrett jobbprompt med kildepresiseringer er bevart i rapportmappen.

Eksakt rektangel [352, 192, 832, 640] på1536x1024RGB128lerret. Sluttbildet bruker direkte utsnitt fra siste generering, ingen geometriwarp eller originalmaskering. Alle tilstander vist samlet i c-tilstander-qa.png. Egenkontroll: FEIL. Se individuell logg; eventuelt FFT-blokkavvik føres separat i kilde-QA og er ikke kalt bestått.

SHA-256: d72e66283a831d668aa49a7eb73a75ea8466dda02d4fdcada083f0ea9122fc9f
Råforsøk: rapporter/bestilling005-20261013/obj187_05-raa-2.png
SHA-256 råforsøk: 80cb29902af127024982f32829c9429188d27b62bfa15f315e651f9b0a283ab3

Runtime/import/maskesamspill: UVERIFISERT. Ny brukergodkjenning: false. Beskyttede kilder, kode og Git uendret.
# Avgrenset retting av obj187_05

Dato: 2026-10-13. To rettingskandidater etter C sine to genereringer. Kandidat 1 gjenbrukte nytegnet bakgrunn fra obj187_03. Originalområdet [0,0,69,70] er byte-identisk i 03, 05 og 06. Området [0,0,69,80] er ikke likt, fordi køllen når inn i de nederste ti originalradene. Kildebevis med SHA ligger i a-retting187-kildebevis.json.

Kandidat 1 kopierte canvasrektangel [352,192,628,472] direkte fra 03. Kontrollen ga FEIL med blokk 7.94. Synlig gradientsøm gjorde kandidaten uegnet.

Kandidat 2 bruker én smal redigering med innebygd ChatGPT image_gen. Eksakt modell ikke eksponert. Ordrett jobbprompt pluss presisering ligger i a-retting187-prompt02.txt. Bare samme blå bakgrunnsrektangel og venstre mørke kant ble hentet fra råresultatet. En rektangulær fargeovergang på 32 HD-piksler innenfor høyre/nedre kant fjerner skjøten; ingen originalpikselmaske, silhuettmaske, geometriwarp eller ditheroppskalering. Alt utenfor rektangelet, inkludert kølle, hånd og brett, er byte-identisk med førbildet. Presis oppskrift og råfil er bevart.

Visuell kontroll: Sam griper rød treklubbe over fremre venstre hull; tre hull synlige. Ingen observasjon av den rapporterte forskyvningen på omtrent åtte originalpiksler i kølle/hånd/brett. Den svake blå gradienten og originalens dither gjør FFT-instabilitet plausibel, men dette er en hypotese, ikke et bevist fritak. Mørk venstrekant er fortsatt en glattet tolkning av originalens trinnkant. Ingen runtime- eller motorinspeksjon utført.

Uendret verktoy/sjekk_leveranse.py: fortsatt FEIL, globalt skift 0.15, blokk 7.92, kantlikhet 0.97. Leveransen er derfor IKKE teknisk godkjent. Kandidat 2 ligger som resultat.png med SHA-256 79d504780a59e4050b2611d98f7f59f16f4f07274cf73b368a453781e9650571. Førbildet er bevart med SHA d72e66283a831d668aa49a7eb73a75ea8466dda02d4fdcada083f0ea9122fc9f. Canvas 1536x1024, padding nøyaktig RGB128. Beskyttede kilder, kontrollskript, Git og C-manifest er uendret.



## Ett nytt helhetsforsøk, forkastet

Etter separat beskjed fra rot ble ett nytt helhetsforsøk laget fra beskyttet referanse, godkjent hovedark/sam.png og stil/rom007_del1av2.png. Ingen avvist kandidat ble brukt som anker. Ordrett prompt med kildepresisering er a-retting187-prompt03.txt; råfil, presis rektangelplassering og kandidat er bevart med samme prefiks. Innebygd image_gen; eksakt modell ikke eksponert. Samlet antall genereringer for denne jobben er fire: to opprinnelige hos C, én smal retting og dette helhetsforsøket.

Det synlige motivrektangelet [287,143,1249,870] ble skalert samlet til832x640 og plassert [352,192] på1536x1024 RGB128. Ingen lokal forskyvning eller konturmaskering. Kandidat03 fikk FEIL: globalt skift1.70, blokk12.13, kantlikhet0.90. Visuelt endret den nese-/øyekontur, jakkeslag og skygger; køllens overkant ble glattere og den blå flaten fortsatt annerledes. Den er ikke minst like kildetro eller teknisk bedre, og ble derfor forkastet.

Resultat.png er tilbakeført byte-identisk til kandidat02: SHA79d504780a59e4050b2611d98f7f59f16f4f07274cf73b368a453781e9650571. Gjenstående tekniskproblem er FEIL med skift0.15/blokk7.92/kant0.97. Ingen flere genereringer eller pipelineendringer utført.
