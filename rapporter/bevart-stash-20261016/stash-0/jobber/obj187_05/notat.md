# obj187_05, ny levering

Dato: 15. oktober 2026. Innebygd ChatGPT image_gen. Eksakt bildemodell er ikke eksponert. To nye bildeforsøk i denne økten, første forsøk valgt. Tidligere notat og resultat er bevart i `rapporter/natt-obj187_05-20261015/`.

## Kilde og motiv

Originalene `referanse.png` og `original_1x.png` er sett før tegning. Rom 18 er Wak-A-Rat, ifølge `GJENNOMGANG.md`. Objekt 187 tilstand 05 viser Sam som slår med en rød treklubbe over venstre del av brettet. Sam har orangebrun pels, grålilla jakke, lys mansjett og blåsvart slips i denne scenen. Ansikt og kropp er avskåret ved høyre kant. Køllen og hånden dekker de to venstre hullene. Tre hele hull er synlige. Ingen rotter er synlige. Behold bare den delen av bokstavene som finnes i utsnittet.

Godkjent `jobber/obj187_01/resultat.png` er sett og lagt ved som bilde to, slik ordren krever. `hovedark/sam.png` er sett og lagt ved som bilde tre for identitet. Farger, avkutting og slagfase følger originalen, ikke hovedarkets vanlige drakt. AGENTS.md, BESTILLING.md, ANALYSE.md og remake-skillen fra lokal main er lest. Ingen CLAUDE.md ble funnet i arbeidsmappen.

## Prompt og forsøk

Jobbens prompt er brukt ordrett som første del av begge forespørslene. Separat kildepresisering beskriver tilstand 05, de tre synlige hullene, originalpaletten og motivrektangelet. Det generelle romnotatet om fem hull og poengpanelet skal ikke føre til nye hull eller ny tekst i dette utsnittet. Presiseringen og begge faktiske prompter er bevart i rapportmappen. Ingen beskyttede jobbfiler er endret.

Forsøk 1: SJEKK, globalt skift 0,07, blokkavvik 1,42, kantlikhet 0,970.
Forsøk 2: FEIL, globalt skift 0,04, blokkavvik 6,90, kantlikhet 0,967. Forkastet.
Tidligere resultat: FEIL, globalt skift 0,15, blokkavvik 7,92, kantlikhet 0,973.

Sluttfilen bruker første forsøk. Kun lerretsinnpakking er utført med Pillow: det genererte motivrektangelet [352, 192, 832, 640] kopieres pikselidentisk til et 1536 x 1024 RGB-lerret med helt flat RGB(128,128,128) kant. Ingen skalering, forskyvning, warp, originalmaske eller lokal motivretusj. Råbildene ligger i rapportmappen.

## Kontroll og gjenstående usikkerhet

Uendret egenkontroll kjørt med repoets eksisterende Python-miljø i PATH:

`python3 verktoy/sjekk_leveranse.py jobber/obj187_05/resultat.png`

Resultat: SJEKK. Skift 0,07 originalpiksler, blokkavvik 1,42, kantlikhet 0,970. Ingen FEIL. Blokkavviket ligger i øvre venstre blå bakgrunnsområde. Dette er ikke kalt en bevist falsk positiv. Claude må vurdere SJEKK-statusen før mottak.

Visuelt kontrollert mot originalen og tilstand 01: vertikal rød kølle, grep, mansjett, ermets plassering, avskåret Sam og tre hele hull. Den glatte nytegningen tolker lokale konturer i treverk, fingre og jakkefolder. Identiske områder mellom tilstandene er ikke dokumentert byteidentiske. Ingen motoravspilling, skjermtest eller ny godkjenning fra Tom er utført. Artefakter ved kompositering av hammer og figur kan ikke erklæres løst av denne bildefilen alene.

SHA-256 resultat: `a32cc2e19b8223c57abd6b339d4fec20aaad249954e11bc8e9148260b783effb`.

Git pull ble forsøkt, men sandkassen blokkerte skriving til FETCH_HEAD utenfor arbeidsmappen. Grenen er gpt-arbeid. Ingen commit, push, PR, kodeendring eller installasjon er utført.
