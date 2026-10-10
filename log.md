# Logg

Alt som gjøres i prosjektet, med tidspunkt (norsk tid). Nyeste nederst.

## 2026-10-09 21:37
- Repo opprettet av Tom (bare README).

## 2026-10-10 12:57 til 13:22 (Claude)
- Tom: sett opp repoet på samme måte som The Dig HD Remake, klargjør filene fra Google Drive og legg dem inn.
- Sjekket etter AGENTS.md. Fantes ikke. Leste AGENTS, memory, todo, STATUS, siste del av log og `tools/hent_spilldata.sh` i Dig-HD-Remake, og skillen `scumm-hd-remake`.
- Spurte Tom om synlighet: offentlig, som The Dig.
- Drive-mappen `samnmax` var bare delt med Tom. Fikk tilgang til `~/Games` og `~/Nedlastinger` på tom-travelmate, men filene lå ikke der. Tom delte så mappen `Scummvm` (der `samnmax` ligger) med lenke.
- Lastet ned alle fem filene fra `samnmax` med curl. Størrelsene stemmer med Drive: SAMNMAX.000 9 080, SAMNMAX.001 13 790 685, MONSTER.SOU 183 195 967, MT32_CONTROL.ROM 65 536, MT32_PCM.ROM 524 288.
- Utgave: MD5 av SAMNMAX.000 er `d917f311a448e3cc7239c31bddb00dd2`, som i ScummVMs `scumm-md5.h` (master, generert 27. september 2026) er samnmax, CD, EN_ANY. Engelsk CD-utgave.
- Format: SAMNMAX.000 og .001 gir gyldige blokker etter XOR 0x69 (RNAM, MAXS, DROO, DSCR, DSOU, DCOS, DCHR, DOBJ, AARY; .001 er én LECF). Indeksen har 95 romplasser (85 i bruk), 122 skript (121), 95 lyder (94), 349 kostymer (348), 6 tegnsett (4) og 1100 objekter. Ikke kontrollert mot LECF.
- Grenen `spilldata` (uten felles historikk med main): README, `game/` med SAMNMAX.000, SAMNMAX.001, de to MT-32-ROM-filene og `SHA256SUMS` for alle fem hele filer (a65333e), så MONSTER.SOU delt med `split -b 90M` i `MONSTER.SOU.001` (94 371 840) og `.002` (88 824 127), én del per push (04c068b, 55a26b7). Sjekket før push at delene satt sammen gir samme SHA-256 som originalen.
- Main: AGENTS.md, README, memory.md, todo.md, log.md, STATUS.md, .gitignore mot spillfilene, `tools/hent_spilldata.sh` (setter sammen MONSTER.SOU og sjekker summene) og en CI-sjekk som stopper spillfiler i main og kodegrener.
- Ikke gjort: ScummVM er ikke bygget, og spillet er ikke startet. Ingen motor, pipeline eller grafikk ennå.

## 2026-10-10 13:23 (Claude)
- Kontroll: fersk `git clone` av main (86952bf), så `tools/hent_spilldata.sh`. Grenen hentet, MONSTER.SOU satt sammen (183 195 967 byte), SHA-256 for alle fem filer stemmer. `git status` er tom etterpå, så `game/` holdes utenfor.
- CI (test) på main 86952bf: bestått.
- Tom kan skru av lenkedelingen på Drive-mappen `Scummvm` nå.

## 2026-10-10 13:26 til 15:15 (Claude)
- Tom: oppsettet var ikke som i Dig-repoet; sett det opp på samme måte, med remake-skillen (skrevet "temakveld skill", tolket som `scumm-hd-remake`, den eneste remake-skillen). Valgte "hele oppsettet, tilpasset": samme mapper og filer, tilpasset der det går, ScummVM bygget og spillet startet, og det som ikke er portet til v6, tydelig merket.
- Arbeidsgren `oppsett-som-dig`. Kopiert fra Dig-HD-Remake (main 36cd09f): `engine/` (SCUMMVM_COMMIT c9091321, patchen uendret, build/run/test, nettsidekoden i `pages/` og `web/`), `pipeline/` (pakken omdøpt fra `dighd` til `smhd`), `tools/` (gpt_gren, gpt_runde, mod_gren, pakke_linux, romtest, check_hd_art, `la0_info.py` som `indeks_info.py`), `docs/`, `spill.sh`, `.github/workflows/linux.yml`. Ikke tatt med: konseptbilder, romnotater, figurliste, avvisninger, kostymefarger og grafikkpiloten fra The Dig. CSV-filene har bare overskrifter.
- To hjelpeagenter: én tilpasset nettsidekoden (filfilter for SAMNMAX.000/.001, MONSTER.SOU-deler og ROM-filene, samnmax, Sam-Max-HD; rettet en regex som ville ha slått sammen SAMNMAX.000 og .001 som deler av én fil; 16 nodetester bestått), én skrev om dokumentene i docs/ for Sam & Max (ANALYSE, HD-MOTOR kortet ned til det som gjelder, HD-REMASTER-METODE, BESTILLING og gpt-arbeid-AGENTS merket som ikke aktive, PAGES, SPILLTEST).
- ScummVM: `engine/build.sh` bygde c9091321 med patchen (libsdl2-dev og libpng-dev installert her). Sam & Max startet fra `game/` uten skjerm og kjørte i 25 sekunder: `samnmax`, CD, SCUMM 6, riktig MD5, alle kataloger lest, objekt 35 lagt i inventaret fra rom 1, iMUSE i gang med AdLib. Ingen feil. DigHD er av, fordi `DigHD::create` krever `GID_DIG`.
- Pipeline: `gamedata.py` leser nå v6 med XOR 0x69 i tillegg til v7 (MAXS uten tekster, RMHD uten versjon, objektenes plass fra CDHD, COST-blokker). `smhd info` viser Sam & Max-tallene. `smhd extract` stopper med en melding for v6, og `smhd san` er fjernet (ingen SMUSH). Promptene i `gpt.py` og `figur.py` er grovt skrevet om til Sam & Max, `FIG_PILOT` er tom og The Dig sine inventarobjekter er tatt ut. Testene: The Dig sine spillfiltester er byttet med Sam & Max-tall, ny syntetisk v6-test med XOR, testene bruker et kunstig pilotkostyme. `pytest` med spillfilene: 30 bestått.
- Målt i SAMNMAX.001: 85 rom (42 på 320 x 200, 36 brede opptil 1104 i rom 31, 4 nesten tomme), 63 med z-plan, 2 med flere paletter (7 og 51), 43 med fargesykling, 959 objektbilder på 715 objekter, 348 COST med ID i DCOS, 120 SCRP, 94 SOUN, 4 CHAR, 564 LSCR. Romlisten i `docs/rom-oversikt.csv`. ANALYSE.md oppdatert.
- `tools/indeks_info.py` leser SAMNMAX.000 (XOR, v6-MAXS, plasser og i bruk). `engine/run.sh` (valget `ingen` starter uten mod), `engine/test.sh` (stopper til uttrekket finnes), `tools/romtest.py`, `tools/gpt_runde.sh` og `tools/mod_gren.sh` tilpasset filnavn og spill-ID.
- `spill.sh` tilpasset: starter uten mod når `hd-mod` ikke har noen, `--auto` stopper med melding. Kjørt her uten skjerm: hentet `hd-mod`, bygget motoren og startet spillet med `--programvare`. Uten skjerm og uten `--programvare` stopper OpenGL med "Could not load any graphics mode".
- Linux: `tools/pakke_linux.sh` lager pakken uten HD-mod (SamMaxHD-x86_64.AppImage, data i `sam-max-hd`). AppDir laget her og startet uten skjerm. `linux.yml` tilpasset; testen sjekker at spillet starter og fortsatt kjører etter 60 sekunder. Push-utløseren er tatt bort til HD virker. Arbeidsflyten er ikke kjørt.
- `test.yml`: nettsidetestene, pipelinetestene, sjekken mot spillfiler og `bash -n` på hvert skript.
- Grenene `hd-mod` (README og SHA256SUMS, ingen mod, 396177a) og `gpt-arbeid` (AGENTS, BESTILLING, ORDRE uten jobber, stil/, 0e359b2) laget og pushet.
- Funnet i ScummVM-kilden: pekerkroken i patchen er bare i `ScummEngine_v7::updateCursor`, menyraden HD Graphics står med v7-koordinater, blast-tekst er tom i `ScummEngine_v6`, og `--disable-mt32emu` gjør at ROM-filene ikke brukes. Skrevet i HD-MOTOR, memory og todo.
- AGENTS, README, memory, todo og STATUS oppdatert.
- PR 1 (`oppsett-som-dig`), CI (test) grønn på push og PR. Jeg får ikke flette min egen PR herfra (stoppet av sikkerhetskontrollen, som i Dig-repoet). Tom fletter.
