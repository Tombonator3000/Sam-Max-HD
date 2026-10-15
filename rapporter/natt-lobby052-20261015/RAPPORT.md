# Fire returer fra lobbyen i rom 52

15. oktober 2026, avsluttet omtrent klokken 23:47 norsk tid. Jobbene er tatt i rekkefølgen i ORDRE.md, oppdatert klokken 23:30.

Fire resultat.png og fire notat.md er klare for Claude. Alle fire består egenkontrollen og den maskerte objektkontrollen med smhd.gpt.check_pieces og piece_problem. Levert: 4. Visuelt kontrollert som stillbilder: 4. Importert i denne økten: 0. Motoravspilling: 0. Toms godkjenning: ingen ny.

| Jobb | Objekt | Kantlikhet mot objekt | Mot bakgrunn | Utfall |
| --- | --- | --- | --- | --- |
| lag052_07_del2av2 | obj486_07 | 0,877 | 0,658 | OK |
| lag052_08_del2av2 | obj486_08 | 0,884 | 0,643 | OK |
| lag052_09_del2av2 | obj486_09 | 0,888 | 0,676 | OK |
| lag052_10_del2av2 | obj486_0A | 0,877 | 0,674 | OK |

Egenkontrollen måler 0,05 originalpiksler i skift, 0,41 i blokker og omtrent 0,96 i kantlikhet for alle fire. Resultatene er RGB på 1536 x 1024, med eksakt #808080 i rammen. Alle 16 beskyttede jobbfiler er kontrollert mot beskyttede-kilder.json og er uendret.

## Grunnlag

ORDRE.md, BESTILLING.md, AGENTS.md, ANALYSE.md, relevante deler av GJENNOMGANG.md, NATT-HANDOFF.md og prosjektbibliotekets OPPDRAG-GPT.md er lest. CLAUDE.md finnes ikke i dette arbeidstreet. Remake-skillen er lest fra den lokale docs/skills/scumm-hd-remake/SKILL.md. Imagegen-skillen er brukt.

Originalene viser den samme hvilende grønne øglen med små endringer rundt øyelokk og munn. Øvre øyespalte er synlig i tilstand 07 og lukket i de senere fasene. Den kjølige grålilla formen endrer plass og utstrekning i 07, 08 og 09 og er borte i 0A. Motivet er ikke gjort om til en ny figur, og den lille formens anatomiske betydning er ikke gjettet. Farger og konturer tas fra originalene. Rommets stil og identitet tas fra jobber/rom052_del2av2/resultat.png. docs/gpt-romnotater.csv rad for rom 52 bekrefter øglen som del av rommet.

Full referanse og godkjent rombilde er sett før tegning for hver jobb. Originalobjektene i work/extract/objects og rooms.json gir ressurs-ID, ti tilstander og rektangelet [232,152,24,24] i rommet. På jobblerretet er dette [544,720,96,96]. Originalene og ferdige faser kan sammenlignes i [kontaktarket](faser-ferdig.png).

## Nytegning og plassering

Seks nye image_gen-kall: ett helbilde per jobb og ett ekstra detaljforsøk for hver av tilstandene 07 og 08. Eksakt modellversjon er ikke eksponert. Første kall per jobb bruker prompt.txt ordrett, med returteksten og en separat presisering etterpå. Detaljprompter og råbilder er bevart her.

De første helbildene for 07 og 08 bestod helbildemålingen, men den maskerte objektkontrollen fant at fasen fortsatt manglet. De brukes derfor ikke som ferdige objekter. Det første detaljforsøket for 07 flyttet andre hodedeler for mye ved innsetting som stort felt. Bare den nytegnede grålilla formen brukes fra detaljbildet.

[plassering.py](plassering.py) gjenskaper leveransene. Det nytegnede hodets felles munn og kjeve tas fra helbildet for 0A. Originalene viser samme nedre former i alle fire. Øyespalten for 07 tas fra helbildet for 09. De nytegnede grålilla detaljene for 07 og 08 renses til egen alfa og settes i originalens mål. Den korte formen for 09 bruker samme nytegnede detalj som 08, tilpasset originalens 8 x 8 HD-piksler. Ingen originalkontur brukes som klippemaske.

Bare det nytegnede objektfeltet settes inn i det godkjente HD-rommet, med en smal myk overgang langs det rektangulære feltets kant. Rommet utenfor objektfeltet er kontrollert som identisk med stilreferansen. Den grå rammen er renset. Python brukes bare til alfa, rensing, presis plassering og måltilpasning etter Toms uttrykkelige tillatelse. All nytegning er fra bildeverktøyet.

Kontaktarket er visuelt kontrollert etter siste plassering. Fire ulike faser, øyelokk, grålilla former, munn, kjeve, snute, farger og overgang til resten av hodet er vurdert mot originalene. De røde munnmerkene fra tidlige råforsøk er fjernet ved å bruke den rene nytegnede munnen fra 0A.

## Kontroll og overlevering

Standard python3 mangler NumPy og stoppet først ved import. Sluttkontrollene bruker prosjektets eksisterende .venv via PATH og uendret verktoy/sjekk_leveranse.py. Ingen pakker er installert. Egenkontrollene står i jobbnavn-egenkontroll.txt. Den maskerte kontrollen står i [mottak-siste.json](mottak-siste.json). Filbaner, sjekksummer og antall egne forsøk står i [leveranser.json](leveranser.json).

Claude bør kontrollere originalens faktiske alfaklipp og avspilling av alle ti ansiktsfaser, særlig overgangen fra 07 til 08, 09 og 0A. Visuell stillbildekontroll og teknisk kantlikhet er ikke motoravspilling eller Toms godkjenning. Ingen figurark inngår, så figurfremdrift og rutekart er ikke relevant.

Git pull ble forsøkt, men sandkassen blokkerte skriving til FETCH_HEAD utenfor arbeidstreet. Arbeidet er utført på gpt-arbeid. Ingen commit eller push er forsøkt. Ingen kode, PR32, main eller fig091_03 til 05 er endret. Bare de fire resultatene, tilhørende notater og denne rapportmappen er endret eller opprettet. Nattskriptet kan committe dem videre.
