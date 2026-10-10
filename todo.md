# todo.md

Det som gjenstår, viktigst først. Kryss av når noe er gjort, og logg det i `log.md`.

## Neste

### Oppsett (10. oktober)

- [x] Repoet satt opp som The Dig: AGENTS, README, memory, todo, log, STATUS, .gitignore, CI-sjekk mot spillfiler
- [x] Spillfilene hentet fra Drive og lagt i grenen `spilldata` med sjekksummer, MONSTER.SOU i deler på 90 MB
- [x] Utgaven bekreftet med MD5: engelsk CD-utgave
- [ ] Tom skrur av lenkedelingen på Drive-mappen `Scummvm` (den trengs ikke lenger)

### Analyse (`docs/ANALYSE.md`)

- [ ] Lås en ScummVM-commit (`engine/SCUMMVM_COMMIT`) og bygg ScummVM her
- [ ] Kjør spillet uendret fra `game/` uten skjerm og bekreft at det starter
- [ ] Tell rom, objektbilder per tilstand, kostymer og ruter, tegnsett, z-plan, paletter og fargesykling
- [ ] Romliste som CSV (`docs/rom-oversikt.csv`)
- [ ] Finn mellomsekvensene og minispillene som tegnes av motoren

### Motor

- [ ] Port DigHD fra The Dig og slå den på for `GID_SAMNMAX`
- [ ] Rom og objekter først, test med en `nearest`-mod (0 avvik)
- [ ] Kroker for figurer i `ClassicCostumeRenderer`
- [ ] Tekst i `CharsetRendererClassic`
- [ ] Farger, fargesykling, blast-objekter og blast-tekst
- [ ] Menyvalget HD Graphics i originalmenyen for v6, og Ctrl+H

### Pipeline

- [ ] Uttrekk av rom, objekter og kostymeruter som indekserte PNG med JSON (dump-modus i motoren eller egne dekodere)
- [ ] `build-mod` med automatisk oppskalering
- [ ] Jobbene til grafikerne

### Grafikk

- [ ] Stilpilot med Tom: ett rom og ett figurark sett i motoren, stilankere, godkjenning
- [ ] Grafikkrunder med `gpt-arbeid` og `hd-mod`

### Spillbart for Tom

- [ ] `./spill.sh` fra repoet
- [ ] Nettsiden
- [ ] Linux-pakken

## Senere

- [ ] Vurder én felles kode-repo for alle LucasArts-HD-spillene (tanken fra 9. oktober), når Sam & Max og Zak trenger samme motor
