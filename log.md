# Logg

Alt som gjøres i prosjektet, med tidspunkt (norsk tid). Nyeste nederst.

## 2026-10-09 21:37
- Repo opprettet av Tom (bare README).

## 2026-10-10 12:57 til 13:25 (Claude)
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
