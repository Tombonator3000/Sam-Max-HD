# obj187_05, ny levering i nattløpet

Dato: 15. oktober 2026. Verktøy: innebygd image_gen.imagegen. Eksakt bildemodell er ikke eksponert. Seks nye bildeforsøk i denne økten. Tidligere resultat og notat er bevart i rapporter/natt-obj187_05-20261015/.

## Motiv og kildegrunnlag

Objekt 187, tilstand 05, rom 18 Wak-A-Rat. Sam slår mot fremre venstre hull med en rød treklubbe. Hånd og klubbe skjuler to hull, og tre åpne hull er synlige. Sam beholder orangebrun pels, grålilla frakk, lys mansjett og blåsvart slips. Avskåret ansikt, arm, grep og klubbestilling følger original 05. Ingen rotter eller treffeffekter er tilført.

Original 05 i 1x og 4x, originaltilstandene 01, 03 og 06 og originalrom 18 er visuelt gjennomgått. Godkjent jobber/obj187_01/resultat.png ble brukt som bilde to for materialer og kontinuitet. Godkjent hovedark/sam.png ble brukt som identitetsreferanse. Stil/rom007_del1av2.png og stilmanifestet er også sett. ANALYSE.md, GJENNOMGANG.md, BESTILLING.md, ORDRE.md, AGENTS.md, nattoverleveringen og remake-skillen fra lokal main er lest. Ingen CLAUDE.md finnes i denne mappen.

Den generelle rompromptens fem hull og HIT 20 WIN skal ikke føre til utfylling av dette utsnittet. To hull er skjult i denne tilstanden, og poengpanelet ligger utenfor objektbildet. Delvis WAK-A-tekst beholdes avskåret. Ordrett prompt står først i de relevante genereringspromptene, fulgt av denne dokumenterte kildepresiseringen og returens rettingsforslag. Beskyttede jobbfiler er uendret.

## Resultat og kontroll

Resultat.png er sjette rågenerering, kopiert direkte uten bildebehandling. Formatet er direkte objektbilde, RGB, 1430 x 1100, med nøyaktig sideforhold 208:160. Dette formatet er tillatt i ORDRE.md. Verktøyet ga ikke de forespurte 1664 x 1280 pikslene. Ingen grå lerretskant følger det direkte bildet.

Forsøk 1 og 2 fikk FEIL på blokkavvik. Forsøk 3 og 4 besto geometrikontrollen, men beholdt struktur i grå padding. Forsøk 3 hadde også en ekstra skygge rundt klubben, fjernet i forsøk 4. De to siste forsøkene bruker direkte objektformat. Forsøk 6 har bedre kildeplassering og kantlikhet enn forsøk 5 og er valgt.

Sluttkontroll med uendret verktoy/sjekk_leveranse.py: SJEKK, skift 0,07 originalpiksler, blokkavvik 1,31, kantlikhet 0,94. Ingen FEIL. Prosjektets eksisterende virtuelle miljø ble lagt først i PATH og kommandoen python3 verktoy/sjekk_leveranse.py jobber/obj187_05/resultat.png ble kjørt. Systemets python3 mangler NumPy. Ingenting er installert.

Visuelt kontrollert: Sam-identitet, rød treklubbe, grep, tre synlige hull, avskåret tekst og ansikt, og fravær av ekstra klubbeskygge. Kildegeometrien er fortsatt fasit. Blokkdiagnosen viser avvik opptil 1,31 i området med venstre del av klubben og brettet, og omtrent 1,08 i to øvre blokker. Dette krever Claudes vurdering. SJEKK skal ikke omtales som OK. Det er ikke gitt noe målefritak. Hele animasjonen, faktisk tilstandsrekkefølge og sammensetting i motoren er ikke testet. Tom har ikke godkjent leveransen.

SHA-256 resultat: f48b2d49875c752719f5f64ea8b9768a8bb15cea19aa5ad4eecdc47a0bb2777c

Alle seks råforsøk, faktiske promper, sluttkontroll, blokkdiagnose, kildegrunnlag og sjekksummer ligger i rapporter/natt-obj187_05-20261015/.

Git pull ble forsøkt på gpt-arbeid, men stoppet fordi FETCH_HEAD i det delte Git-området er skrivebeskyttet i sandkassen. Grenen er ikke byttet. Ingen kode, motor, PR, commit eller push er utført. Nattløpets skript håndterer commit. Sam091-arkene er ikke endret.
