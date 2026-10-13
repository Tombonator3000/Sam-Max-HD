# Avgrenset retting av obj187_05

Dato: 2026-10-13. To rettingskandidater etter C sine to genereringer. Kandidat 1 gjenbrukte nytegnet bakgrunn fra obj187_03. Originalområdet [0,0,69,70] er byte-identisk i 03, 05 og 06. Området [0,0,69,80] er ikke likt, fordi køllen når inn i de nederste ti originalradene. Kildebevis med SHA ligger i a-retting187-kildebevis.json.

Kandidat 1 kopierte canvasrektangel [352,192,628,472] direkte fra 03. Kontrollen ga FEIL med blokk 7.94. Synlig gradientsøm gjorde kandidaten uegnet.

Kandidat 2 bruker én smal redigering med innebygd ChatGPT image_gen. Eksakt modell ikke eksponert. Ordrett jobbprompt pluss presisering ligger i a-retting187-prompt02.txt. Bare samme blå bakgrunnsrektangel og venstre mørke kant ble hentet fra råresultatet. En rektangulær fargeovergang på 32 HD-piksler innenfor høyre/nedre kant fjerner skjøten; ingen originalpikselmaske, silhuettmaske, geometriwarp eller ditheroppskalering. Alt utenfor rektangelet, inkludert kølle, hånd og brett, er byte-identisk med førbildet. Presis oppskrift og råfil er bevart.

Visuell kontroll: Sam griper rød treklubbe over fremre venstre hull; tre hull synlige. Ingen observasjon av den rapporterte forskyvningen på omtrent åtte originalpiksler i kølle/hånd/brett. Den svake blå gradienten og originalens dither gjør FFT-instabilitet plausibel, men dette er en hypotese, ikke et bevist fritak. Mørk venstrekant er fortsatt en glattet tolkning av originalens trinnkant. Ingen runtime- eller motorinspeksjon utført.

Uendret verktoy/sjekk_leveranse.py: fortsatt FEIL, globalt skift 0.15, blokk 7.92, kantlikhet 0.97. Leveransen er derfor IKKE teknisk godkjent. Kandidat 2 ligger som resultat.png med SHA-256 79d504780a59e4050b2611d98f7f59f16f4f07274cf73b368a453781e9650571. Førbildet er bevart med SHA d72e66283a831d668aa49a7eb73a75ea8466dda02d4fdcada083f0ea9122fc9f. Canvas 1536x1024, padding nøyaktig RGB128. Beskyttede kilder, kontrollskript, Git og C-manifest er uendret.
