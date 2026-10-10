# todo.md

Det som gjenstår, viktigst først. Kryss av når noe er gjort, og logg det i `log.md`.

## Neste

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
- [ ] Navn på rommene i romlisten ved gjennomsyn (RNAM er tom)
- [ ] Ruter per kostyme, animasjoner og retninger (krever COST-dekoder)
- [ ] Hvilke objekter som bare har BOMP-bilde (blast-objekter)
- [ ] Finn mellomsekvensene og minispillene som tegnes av motoren
- [ ] Hvilke kostymer som er Sam, Max og de andre (fyll `docs/figurer.csv`)

### Motor (`docs/HD-MOTOR.md`)

- [ ] Slå på DigHD for `GID_SAMNMAX` og test at ingenting brekker uten mod
- [ ] Rom og objekter først, test med en `nearest`-mod (0 avvik)
- [ ] Kroker for figurer i `ClassicCostumeRenderer`
- [ ] Tekst i `CharsetRendererClassic`
- [ ] Farger, fargesykling og blast-objekter; sjekk om blast-tekst brukes
- [ ] Pekeren (kroken finnes bare i `ScummEngine_v7::updateCursor`)
- [ ] Menyvalget HD Graphics i originalmenyen for v6 (raden står med v7-koordinater), og Ctrl+H

### Pipeline

- [ ] Velg vei for uttrekket: dump-modus i motorpatchen eller egne dekodere for SMAP og COST
- [ ] Uttrekk av rom, objekter og kostymeruter som indekserte PNG med JSON, i samme format som The Dig
- [ ] `smhd build-mod` med automatisk oppskalering
- [ ] `engine/test.sh` og `tools/romtest.sh` med Sam & Max
- [ ] Prompter og figurnavn i `gpt.py` og `figur.py` gjennomgått for Sam & Max (grovt tilpasset 10. oktober)

### Grafikk

- [ ] Stilpilot med Tom: ett rom og ett figurark sett i motoren, stilankere, godkjenning
- [ ] Aktiver bestillingen (`docs/BESTILLING-CHATGPT.md`) og grafikkrunder med `tools/gpt_runde.sh`

### Spillbart for Tom

- [x] `./spill.sh` fra repoet (starter originalspillet)
- [ ] Linux-pakken: kjør arbeidsflyten Linux-pakke for hånd og test AppImage-filen
- [ ] Nettsiden: lag repoet `Sam-Max-HD-Web` (Tom), bygg i Actions og test. Sjekk at siden takler en `hd-mod` uten mod
- [ ] Vurder `--enable-mt32emu` når musikken skal testes (MT-32-ROM-filene ligger i `spilldata`)

## Senere

- [ ] Vurder én felles kode-repo for alle LucasArts-HD-spillene (tanken fra 9. oktober), når Sam & Max og Zak trenger samme motor
- [ ] Slå på push-utløseren i `.github/workflows/linux.yml` når HD virker
