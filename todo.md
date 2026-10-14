# todo.md

Det som gjenstår, viktigst først. Kryss av når noe er gjort, og logg det i `log.md`.

## Neste

- [x] Innført kildetro motiv- og designanalyse før HD-produksjon i `docs/skills/scumm-hd-remake/SKILL.md`, med henvisninger fra arbeidsinstruksene (12. oktober 2026)

- [x] Løs konfliktene i PR 2 mot main uten å miste motorarbeidet fra PR 3 (12. oktober, Codex)

### Oppsett (10. oktober)

- [x] Repoet satt opp med AGENTS, README, memory, todo, log, STATUS, .gitignore og CI-sjekk mot spillfiler
- [x] Spillfilene hentet fra Drive og lagt i grenen `spilldata` med sjekksummer, MONSTER.SOU i deler på 90 MB
- [x] Utgaven bekreftet med MD5: engelsk CD-utgave
- [x] Samme oppsett som Dig-HD-Remake: `engine/`, `pipeline/` (`smhd`), `tools/`, `docs/`, `spill.sh`, arbeidsflyter, grenene `hd-mod` og `gpt-arbeid`
- [x] ScummVM ved c9091321 med patchen bygget, og Sam & Max startet uten skjerm (uten HD)
- [ ] Tom skrur av lenkedelingen på Drive-mappen `Scummvm` (den trengs ikke lenger)
- [ ] Tom starter `./spill.sh` på laptopen og ser at spillet starter med bilde og lyd

### Analyse (`docs/ANALYSE.md`)

- [x] Tell rom, størrelser, z-plan, paletter, fargesykling, objektbilder og kostymer (`smhd info`)
- [x] Romliste som CSV (`docs/rom-oversikt.csv`, uten navn)
- [x] Navn på rommene i romlisten (13. oktober, alle 85)
- [x] Ruter per kostyme, animasjoner og retninger (`costumes.json`, 16 052 ruter)
- [x] Hvilke objekter som har BOMP-bilde (103 blast-objektbilder, `kind` i rooms.json)
- [x] Dekompiler alle skriptene med descumm (`tools/dekompiler_skript.py`, 1179 av 1181)
- [x] Finn hvilke rom og palett hvert kostyme vises i fra skriptene (`tools/kostymer.py`, `docs/kostymefarger.csv`, 13. oktober)
- [x] Se de kostymene som står med «trolig» i `docs/figurer.csv` i spillet, og rulletekstpanelene i rom 67 og 77 (14. oktober): kostyme 103 er Trixie (skript 120), panelene (objekt 600 til 603 lånt fra rom 67) får HD i rom 77. Rulleteksten avslørte to feil i HD-skriften, rettet
- [x] Finn mellomsekvensene og minispillene som tegnes av motoren (14. oktober, `docs/MINISPILL.md`). Figurskygger og lyskjegler (skyggetabellen) får nå HD
- [ ] Car Bomb (rom 66): skipsmerkene tegnes med `drawBox` piksel for piksel og blir blokkete. HD krever at motoren kjenner igjen mønsteret (skriptnivå, trenger Toms ja)
- [ ] Noir-modusen (tast b): test med et lagret spill, og la HD bli grå i stedet for å tones per fargekanal
- [x] Hvilke kostymer som er Sam, Max og de andre (`docs/figurer.csv`, 13. oktober)

### Motor (`docs/HD-MOTOR.md`)

- [x] Slå på DigHD for `GID_SAMNMAX` (10. oktober)
- [x] Rom og objekter, testet med `nearest`-mod (0 avvik, `engine/test.sh`) og romtest i alle rom
- [x] Kroker for figurer i `ClassicCostumeRenderer` (testet i kontoret og med `DIGHD_TEST_COSTUME=2`)
- [x] Merkene per piksel i v6, der teksten legges over i `_compositeBuf` (`blitVirtScreen` med `vsSrc`)
- [x] Blast-objekter (bildet som faktisk tegnes; testet i rom 68)
- [x] Pekeren (`ScummEngine::updateCursor`), ikke sett på skjerm
- [x] Ctrl+H bytter HD og klassisk
- [x] Tekst i `CharsetRendererClassic` (HD-glyfer som i The Dig), med eget lag for tekstlaget i v6 (14. oktober)
- [x] Menyvalget HD Graphics i originalmenyen for v6 (14. oktober, testet med F5 og klikk)
- [x] Sjekk om blast-tekst brukes i Sam & Max: nei, bare blast-objekter (14. oktober)
- [ ] Romtest: finn en måte å komme inn i de 12 rommene som henger etter testhoppet (lagret spill eller objekttilstander). Sjekket 14. oktober: rom 11 stopper på «state -1 is out of bounds» og rom 50 på «readArray: invalid array 261», fordi variablene ikke er satt uten vanlig spill. Krever lagrede spill fra en ekte gjennomspilling
- [ ] Test The Dig med den utvidede patchen (i Dig-repoet) før patchen kopieres dit

### Pipeline

- [x] Uttrekket med egne dekodere for SMAP, BOMP og COST (`pipeline/smhd/v6grafikk.py`, `eksport_v6.py`)
- [x] Uttrekk av rom, objekter og kostymeruter som indekserte PNG med JSON, i samme format som The Dig
- [x] `smhd build-mod` med automatisk oppskalering (testet)
- [x] Sammenlign uttrekket med motoren: alle bakgrunnspiksler finner HD-bildet sitt med nearest-mod ("background without HD 0")
- [x] `build-mod` tar med objektbildene i rom uten bakgrunn (rom 81 og 82, 9 bilder), skalert alene (14. oktober)
- [x] `engine/test.sh` og `tools/romtest.sh` med Sam & Max
- [x] Prompter og figurnavn i `gpt.py` og `figur.py` skrevet for Sam & Max (13. oktober)

### Grafikk

- [x] Alle grafikkjobbene laget med hovedark, fast størrelse i figurarkene og egenkontroll (`tools/sjekk_leveranse.py`), 13. oktober
- [x] Jobbene lagt i `gpt-arbeid` (13. oktober, c96f80b)
- [x] PR 4 (grafikkjobbene) flettet til main (13. oktober, e0baba9)
- [x] Stilpilot: hovedark Sam og Max, rom 7 og fig002_01 og fig003_01 levert, kontrollert, sett i motoren og godkjent av Tom; stilankere i `stil/` (godkjent 13. oktober)
- [x] Aktiver bestillingen og første grafikkrunde: gpt-inn, myke figurer, build-mod, romtest, `hd-mod` e85f760 og ny ordre i `gpt-arbeid` (14. oktober)
- [ ] Neste grafikkrunder med `tools/gpt_runde.sh`: avvisningene først, så resten av GRAFIKKLISTE (ikoner 46 av 163, lag 534 av 701, objekter 83 av 86)
- [x] Se på de 15 figurrutene som myke-figurer merket til gjennomsyn (14. oktober): 12 med feil omriss (blant annet Max uten esken) holdes nå utenfor modden og står øverst i ordren; 3 med bare størrelsesavvik er med
- [x] Finn hvor de små svarte feltene i romtesten kommer fra (14. oktober): spredte piksler fra mørke streker grafikeren har tegnet en piksel ved siden av. Romtesten teller nå bare sammenhengende felt; 2 kjøringer igjen (benken i rom 28, en strek i rom 85), begge tegnefeil, ikke motorfeil
- [x] `tools/gpt_gren.sh send` stopper når AGENTS.md i `gpt-arbeid` har linjer som ikke står i `docs/gpt-arbeid-AGENTS.md` (14. oktober)
- [x] Testrom for dynamisk lys på GitHub Pages (`lystest/`, 13. oktober). Tom slår på Pages med GitHub Actions som kilde
- [ ] Dynamisk lys med normalkart og luminansmaske, etter godkjent stilpilot (Tom 13. oktober): valgfritt for spilleren (av som standard, eget valg i menyen), ingen kastede skygger. Prøv først i ett rom (kontoret med lampen) med normalkart regnet ut fra HD-bildene og lyset av og på med en tast. Lyset legges inn før fargeforholdet fra paletten, så nedtoning og blink fortsatt virker. Rommene har lyset malt inn, så det må vurderes i spillet om det løfter eller bare endrer

### Spillbart for Tom

- [x] `./spill.sh` fra repoet (starter originalspillet)
- [ ] Linux-pakken: kjør arbeidsflyten Linux-pakke for hånd og test AppImage-filen
- [x] Windows-pakken: arbeidsflyten Windows-pakke bygger ScummVM med HD-patchen i MSYS2, legger ved spillet og HD-modden og publiserer release "windows" (14. oktober)
- [ ] Tom tester Windows-pakken
- [ ] Nettsiden: lag repoet `Sam-Max-HD-Web` (Tom), bygg i Actions og test. Sjekk at siden takler en `hd-mod` uten mod
- [ ] Vurder `--enable-mt32emu` når musikken skal testes (MT-32-ROM-filene ligger i `spilldata`)

## Senere

- [ ] Vurder én felles kode-repo for alle LucasArts-HD-spillene (tanken fra 9. oktober), når Sam & Max og Zak trenger samme motor
- [ ] Slå på push-utløseren i `.github/workflows/linux.yml` når HD virker
