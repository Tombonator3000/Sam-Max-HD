# todo.md

Det som gjenstår, viktigst først. Kryss av når noe er gjort, og logg det i `log.md`.

## Neste

- [x] Trappetrinn rundt bilen i rom 9: myk alfa for romobjekter og kanten lagt over HD-rommet i motoren (PR 29, 15. oktober)
- [ ] Tom fletter PR 28 og så PR 29; deretter nettsiden og Windows-pakken på nytt
- [ ] Samme patch i Dig-HD-Remake
- [ ] Se Sam og Max foran bilen i rom 9 og bilen som kjører bort

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
- [x] Car Bomb (rom 66): skipsmerkene glatte i HD (Toms ja 14. oktober; merket tegnes som glyf med xBR)
- [x] Noir-modusen (tast b): HD-bildet blir grått (14. oktober)
- [x] Utviklermodus: «Sam og Max HD - utvikler.bat» (hopp til rom eller last lagret spill, i vindu), `tools/romtest.py --lagret MAPPE`, testkroken `DIGHD_TEST_SCRIPT` (14. oktober)
- [ ] Tom lagrer i hvert nytt område under gjennomspillingen og sender lagrede spill; romtest `--lagret` på dem tester de 12 rommene som henger etter testhoppet
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
- [x] Test The Dig med den utvidede patchen (15. oktober): patchene slått sammen, felles patch i begge repoer (Dig-PR)
- [x] Piksler rundt HD-figurene (Toms skjermbilde 14. oktober): kantene på skalerte figurer merkes nå riktig, og ruter uten HD-bilde i kostymer med myke ruter glattes i motoren (15. oktober)
- [x] Kanten mot forgrunnen (z-masken) glattes med xBR (15. oktober)
- [x] Ressursbanken (`docs/GJENNOMGANG.md`) sendt til `gpt-arbeid` som GJENNOMGANG.md, med lenke i AGENTS.md der (15. oktober)
- [x] Små svarte felt i rom 8 og 28: forskjeller i ChatGPTs maling (mørkebrune partier i rekkverket malt nesten svart), ikke motoren. Til grafikkordren
- [ ] Grafikkordre: animasjonstilstander som bare er lapper (flaggene og propellen i rom 17, 19 objekter i alt) må tegnes som hele bilder og klippes etterpå; inventaresken (obj995) trenger egen alfa så kanten blir myk; obj049 (LucasArts-logoen) har magentaflekker fra ChatGPT; ikonene i rom 93 og 94 er Scale4x til ikonarkene er tegnet
- [x] Ny grafikk fra `gpt-arbeid` 15. oktober tatt inn: rettede rutekart (920 av 931 ruter), 111 ikoner med egen myk alfa (`smhd myke-ikoner`, PR 24), hd-mod publisert
- [ ] Tom fletter PR 24 (mottaket for myke ikoner), så nettsiden og pakkene bygges på nytt med den nye modden
- [x] Linux-pakken bygget på nytt med modden fra 15. oktober (release «linux», 15:57)
- [x] PR 26 flettet
- [x] Importpakken 15. oktober 16:17 tatt inn (`smhd importpakke`, PR 28), hd-mod og Linux-pakken oppdatert
- [ ] Tom fletter PR 28
- [ ] Se bassenget i rom 54 (objekt 833, 834, 836) i spillet; rom 54 henger etter testhoppet
- [ ] obj835 (bart eller åpen munn) venter på Toms avklaring
- [ ] Windows-pakken bygges på nytt med den nye modden
- [ ] Se inventaret i spillet med de nye ikonene (testhoppet åpner det ikke; krever lagret spill eller å spille dit)
- [ ] Tom ser på det nye Max-ikonet (obj1008_01) og de andre ikonene
- [ ] 11 figurruter til gjennomsyn (fig091_03 til 05, fig209_03, fig272_02): tegnet i annen størrelse enn gruppen, sendt tilbake i ordren
- [ ] Hakking på nettsiden (Tom 14. oktober). 15. oktober: SIMD i nettbygget (hele skjermen 20 til 30 ms i Chromium), bakgrunnshentingen venter ved grense fra GitHub (429 ga ventetid også for filene spillet trengte). Gjort: HD-pakken hentes i bakgrunnen, fargetoningen er raskere (15 til 11 ms per skjerm), `?adlib` for å sammenligne med MT-32. Tom tester igjen. Nettsiden henter nå HD-pakken i bakgrunnen. Hele skjermen tar 14 til 22 ms å bygge her; i nettleseren kan nedtoninger og rulling bli tunge. Mål med `DIGHD_BENCH` i nettleseren og se på å bygge bare det som er endret ved palettbytter

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
- [x] Linux-pakken: bygget fra main (407d763) og testet 15. oktober: AppImage lastet ned fra releasen, pakket ut og kjørt uten skjerm i rom 17 (HD-modden, Atkinson, MT-32)
- [x] Windows-pakken: arbeidsflyten Windows-pakke bygger ScummVM med HD-patchen i MSYS2, legger ved spillet og HD-modden og publiserer release "windows" (14. oktober)
- [ ] Tom tester Windows-pakken
- [x] Nettsiden: repoet `Sam-Max-HD-Web` med arbeidsflyt som bygger og publiserer (14. oktober). Siden henter spillet uten nøkkel
- [x] Nettsiden publisert på https://tombonator3000.github.io/Sam-Max-HD-Web/ (14. oktober); testet i Chromium uten skjerm
- [ ] Tom tester nettsiden på PC og mobil
- [ ] Windows-pakken starter ikke på Toms jobb-PC (startfila lukker seg); startfilene viser nå feilkode og logg (%APPDATA%\SamMaxHD\scummvm.log)
- [x] MT-32-musikk (14. oktober): motoren bygges med `--enable-mt32emu`, ROM-filene fra spilldata ligger i Linux- og Windows-pakken, og `engine/run.sh`, startfilene, AppImage og nettsiden velger `--music-driver=mt32`
- [x] `--enable-mt32emu` (14. oktober)

## Senere

- [ ] Vurder én felles kode-repo for alle LucasArts-HD-spillene (tanken fra 9. oktober), når Sam & Max og Zak trenger samme motor
- [ ] Slå på push-utløseren i `.github/workflows/linux.yml` når HD virker
