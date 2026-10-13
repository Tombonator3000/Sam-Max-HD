# Status

Oppdatert 13. oktober 2026.

## Kort

Repoet har samme oppsett som The Dig HD Remake, kopiert og tilpasset Sam & Max. Spillfilene ligger i `spilldata`, ScummVM med HD-patchen bygger og kjører spillet, all originalgrafikken er trukket ut, alle skriptene er dekompilert, og HD-motoren er på for Sam & Max: rom, objekter, blast-objekter og figurer får HD fra en mod. Teksten og menyraden HD Graphics er ikke portet. All grafikken er klargjort som jobber til ChatGPT (13. oktober), og stilpiloten venter på grafikeren og Tom. Ingen ferdig HD-grafikk ennå.

## Det som virker

| Del | Hva | Hvordan det er testet |
| --- | --- | --- |
| Spillfiler | SAMNMAX.000, SAMNMAX.001, MONSTER.SOU (i to deler) og de to MT-32-ROM-filene i `spilldata`, hentes og sjekkes med `tools/hent_spilldata.sh` | Fersk klone av main 86952bf og `tools/hent_spilldata.sh` 10. oktober: MONSTER.SOU satt sammen, SHA-256 for alle fem filer stemmer |
| Utgave | Engelsk CD-utgave | MD5 av SAMNMAX.000 funnet i ScummVMs `scumm-md5.h` |
| Motor | ScummVM c9091321 med `engine/patches/0001-dighd-hd-grafikk.patch` (The Dig sin, utvidet for v6) | `engine/build.sh` og `git apply --check` mot c9091321 her 10. oktober. Spillet kjører fra `game/` uten skjerm |
| HD i motoren | Rom, objekter, blast-objekter og kostymeruter (klassiske kostymer) får HD fra modden. Pekeren går gjennom DigHD. Ctrl+H bytter | `engine/test.sh`: 0 avvik og "background without HD 0" i alle dumper. Romtest i alle 85 rom med nearest-mod: 62 rom ok, 0 krasj, 0 forskjøvet, 0 skjermavvik; 12 hang etter testhoppet (skriptfeil uten riktig spilltilstand). Figurer i kontoret: 0,26 til 0,29 prosent avvik i kantene av skalerte figurer. Blast-objektene i rom 68 med HD. Ikke testet med skjerm |
| `./spill.sh` | Henter spillfiler og `hd-mod`, bygger motoren og starter spillet | Kjørt her uten skjerm: tom `hd-mod` hentet, motoren bygget, spillet startet uten mod med `--programvare` (OpenGL finner ingen grafikkmodus uten skjerm) |
| Pipeline | `smhd info` og `gamedata.py` leser v6 (XOR 0x69) og v7 | `smhd info` mot spillfilene: 85 rom, 63 med z-plan, 43 med sykling, 959 objektbilder, 348 kostymer. `pytest` 13. oktober: 40 tester uten spillfiler og 3 med, alle bestått |
| Nettsidekoden | `engine/pages` tilpasset Sam & Max (filfilter, MONSTER.SOU-deler, samnmax) | `node --test`: 16 bestått. Ikke bygget for nettleser |
| Linux-pakken | `tools/pakke_linux.sh` lager pakken uten HD-mod | AppDir laget her og startet uten skjerm: spillet kjente igjen utgaven og kjørte. AppImage og arbeidsflyten er ikke kjørt |
| Indeksverktøy | `tools/indeks_info.py game/SAMNMAX.000` | Kjørt mot spillfilene |
| Uttrekk | `smhd extract`: 83 rombakgrunner, 959 objektbilder (856 SMAP, 103 BOMP), 16 052 kostymeruter fra 348 kostymer, med rooms.json og costumes.json | Kjørt mot spillfilene 10. oktober, 0 feil. Alle rom og ett bilde fra hvert kostyme sett på i kontaktark; rom 2 med objektene på plass stemmer. Enhetstester for alle kodekene og en game-test med tellingene. Ikke sammenlignet piksel for piksel med motoren |
| Skript | `tools/bygg_descumm.sh` og `tools/dekompiler_skript.py`: 1181 skript til `work/skript` | 1179 uten feil, 2 stopper på opkoden 0xBD (ingen virkning i v6). Talereplikker, skriptnumre og romnumre kontrollert mot spillfilene |
| Grafikkjobber | `smhd gpt-pakke --figurer alle`: 2 hovedark (Sam, Max), 115 romjobber for 76 rom, 86 objektjobber, 296 lagjobber (701 bilder), 9 ikonark (163 bilder) og 1758 figurark (15 661 ruter fra 343 kostymer). `smhd gpt-ordre` skriver ORDRE.md med bare stilpiloten til stilankerne finnes | Laget mot spillfilene 13. oktober i `work/gpt`. Stikkprøver av referanser og prompter sett på. Ikke sendt til grafikeren, ingen bilder laget ennå |
| Egenkontroll | `tools/sjekk_leveranse.py` sjekker en leveranse før grafikeren committer: forskyvning og kanter for rom, objekter, lag og ikoner; størrelse, plass og omriss per rute for figurark; høyder for hovedark | Testet med syntetiske leveranser (riktig gir OK, rute 15 prosent for stor gir FEIL, rom forskjøvet 3 px gir FEIL) og i `pytest`. Ikke prøvd på ekte ChatGPT-bilder |
| Myke figurer | `myk.py` versjon 4 (versjon 3 fra Dig): skalerer og plasserer hver rute etter originalen og merker grupper der tegnet størrelse spriker mer enn 12 prosent | Enhetstester med syntetiske ark. Ikke kjørt på ekte leveranser |
| Kostymepaletter | `tools/kostymer.py` finner rommene hvert kostyme brukes i fra skriptene; `docs/kostymefarger.csv` gir 8 kostymer riktig palett i uttrekket. Skyggepiksler (indeks 13) tas bort fra figurarkene | `smhd extract` kjørt på nytt; game-test sjekker paletten for Sam. Rom 92 sett i motoren med samme farger som uttrekket |
| build-mod | Mod med automatisk oppskalering fra uttrekket | `smhd build-mod --method lanczos --kostymer 2,3`: 83 rom, 950 objektbilder, 175 kostymeruter. Objektbildene i rom 81 og 82 (ingen bakgrunn) tas ikke med |

## Ikke portet eller ikke testet

- Teksten (`CharsetRendererClassic`) og menyraden HD Graphics er ikke portet: teksten vises som originalpiksler, og HD velges med Ctrl+H. Se `docs/HD-MOTOR.md`.
- The Dig er ikke testet med den utvidede patchen her (filene er ikke i dette repoet).
- `tools/gpt_runde.sh` er ikke kjørt på ekte leveranser. Jobbene ligger klare lokalt; de er ikke lagt i `gpt-arbeid` før Tom sier ja.
- Kostymefargene: åtte kostymer har fått paletten fra rommene de brukes i. Resten bruker hjemrommet, som stemmer for de fleste, men er ikke sjekket kostyme for kostyme i spillet. Rulletekstpanelene i rom 67 og 77 er ikke sett i motoren.
- Promptene i `gpt.py` og `figur.py` er skrevet om for Sam & Max, men ikke prøvd i ChatGPT. Bestillingen er aktiv bare for stilpiloten.
- Figuridentiteten: navnene i `docs/figurer.csv` kommer fra replikkene i skriptene. De som står med «trolig», er tolket og ikke sett i spillet.
- Spillet er ikke spilt med skjerm og lyd her. Musikken går med AdLib uten MIDI-utgang; MT-32 er slått av i byggingen.
- Nettsiden: eget repo finnes ikke, ikke bygget eller prøvd.
