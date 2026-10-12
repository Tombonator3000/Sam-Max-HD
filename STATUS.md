# Status

Oppdatert 10. oktober 2026.

## Kort

Repoet har samme oppsett som The Dig HD Remake, kopiert og tilpasset Sam & Max. Spillfilene ligger i `spilldata`, ScummVM med HD-patchen bygger og kjører spillet, all originalgrafikken er trukket ut, alle skriptene er dekompilert, og HD-motoren er på for Sam & Max: rom, objekter, blast-objekter og figurer får HD fra en mod. Teksten og menyraden HD Graphics er ikke portet. Ingen ferdig HD-grafikk ennå.

## Det som virker

| Del | Hva | Hvordan det er testet |
| --- | --- | --- |
| Spillfiler | SAMNMAX.000, SAMNMAX.001, MONSTER.SOU (i to deler) og de to MT-32-ROM-filene i `spilldata`, hentes og sjekkes med `tools/hent_spilldata.sh` | Fersk klone av main 86952bf og `tools/hent_spilldata.sh` 10. oktober: MONSTER.SOU satt sammen, SHA-256 for alle fem filer stemmer |
| Utgave | Engelsk CD-utgave | MD5 av SAMNMAX.000 funnet i ScummVMs `scumm-md5.h` |
| Motor | ScummVM c9091321 med `engine/patches/0001-dighd-hd-grafikk.patch` (The Dig sin, utvidet for v6) | `engine/build.sh` og `git apply --check` mot c9091321 her 10. oktober. Spillet kjører fra `game/` uten skjerm |
| HD i motoren | Rom, objekter, blast-objekter og kostymeruter (klassiske kostymer) får HD fra modden. Pekeren går gjennom DigHD. Ctrl+H bytter | `engine/test.sh`: 0 avvik og "background without HD 0" i alle dumper. Romtest i alle 85 rom med nearest-mod: 62 rom ok, 0 krasj, 0 forskjøvet, 0 skjermavvik; 12 hang etter testhoppet (skriptfeil uten riktig spilltilstand). Figurer i kontoret: 0,26 til 0,29 prosent avvik i kantene av skalerte figurer. Blast-objektene i rom 68 med HD. Ikke testet med skjerm |
| `./spill.sh` | Henter spillfiler og `hd-mod`, bygger motoren og starter spillet | Kjørt her uten skjerm: tom `hd-mod` hentet, motoren bygget, spillet startet uten mod med `--programvare` (OpenGL finner ingen grafikkmodus uten skjerm) |
| Pipeline | `smhd info` og `gamedata.py` leser v6 (XOR 0x69) og v7 | `smhd info` mot spillfilene: 85 rom, 63 med z-plan, 43 med sykling, 959 objektbilder, 348 kostymer. `pytest`: 31 tester uten spillfiler og 2 med, alle bestått |
| Nettsidekoden | `engine/pages` tilpasset Sam & Max (filfilter, MONSTER.SOU-deler, samnmax) | `node --test`: 16 bestått. Ikke bygget for nettleser |
| Linux-pakken | `tools/pakke_linux.sh` lager pakken uten HD-mod | AppDir laget her og startet uten skjerm: spillet kjente igjen utgaven og kjørte. AppImage og arbeidsflyten er ikke kjørt |
| Indeksverktøy | `tools/indeks_info.py game/SAMNMAX.000` | Kjørt mot spillfilene |
| Uttrekk | `smhd extract`: 83 rombakgrunner, 959 objektbilder (856 SMAP, 103 BOMP), 16 052 kostymeruter fra 348 kostymer, med rooms.json og costumes.json | Kjørt mot spillfilene 10. oktober, 0 feil. Alle rom og ett bilde fra hvert kostyme sett på i kontaktark; rom 2 med objektene på plass stemmer. Enhetstester for alle kodekene og en game-test med tellingene. Ikke sammenlignet piksel for piksel med motoren |
| Skript | `tools/bygg_descumm.sh` og `tools/dekompiler_skript.py`: 1181 skript til `work/skript` | 1179 uten feil, 2 stopper på opkoden 0xBD (ingen virkning i v6). Talereplikker, skriptnumre og romnumre kontrollert mot spillfilene |
| build-mod | Mod med automatisk oppskalering fra uttrekket | `smhd build-mod --method lanczos --kostymer 2,3`: 83 rom, 950 objektbilder, 175 kostymeruter. Objektbildene i rom 81 og 82 (ingen bakgrunn) tas ikke med |

## Ikke portet eller ikke testet

- Teksten (`CharsetRendererClassic`) og menyraden HD Graphics er ikke portet: teksten vises som originalpiksler, og HD velges med Ctrl+H. Se `docs/HD-MOTOR.md`.
- The Dig er ikke testet med den utvidede patchen her (filene er ikke i dette repoet).
- `tools/gpt_runde.sh` venter på stilpiloten.
- Kostymefargene i RGBA-bildene er fra rommet kostymet ligger i; i andre rom og med skuespillerpalett kan spillet vise andre farger. Noen skygge- eller maskekostymer blir magenta.
- Promptene i `gpt.py` og `figur.py` er grovt tilpasset Sam & Max, men ikke prøvd. Bestillingen er ikke aktiv før stilpiloten.
- Spillet er ikke spilt med skjerm og lyd her. Musikken går med AdLib uten MIDI-utgang; MT-32 er slått av i byggingen.
- Nettsiden: eget repo finnes ikke, ikke bygget eller prøvd.
