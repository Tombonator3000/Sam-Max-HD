# memory.md

Faste fakta og beslutninger. Oppdateres når noe endrer seg.

## Mål
- HD-versjon av *Sam & Max Hit the Road* (LucasArts 1993, SCUMM v6): HD-bakgrunner, HD-objekter, HD-figurer og HD-tekst, lagt oppå originalen slik som i The Dig HD.
- Tom vil ha det samme som for The Dig: spillet starter rett inn som originalen, HD eller originalgrafikk velges i spillets egen meny, det virker på mobil, og det finnes en komplett fil til nedlasting (Linux først).

## Spillfilene
- Original på Google Drive, mappen `samnmax` (id `1ZWXP2NLg9FzADXZ5G37HlkYGtoSKvHih`) i mappen `Scummvm` (id `1YpufOwLtohaVAPOdRxnIs4DHzO_0GcQ5`). Tom delte `Scummvm` med lenke 10. oktober 13:17 så filene kunne hentes.
- Utgave: engelsk CD-utgave. SAMNMAX.000 MD5 `d917f311a448e3cc7239c31bddb00dd2`, som i ScummVMs `scumm-md5.h` (master, generert 27. september 2026) står som samnmax, CD, 9080 byte, EN_ANY.
- Filer og størrelser: SAMNMAX.000 (9 080), SAMNMAX.001 (13 790 685), MONSTER.SOU (183 195 967, talen), MT32_CONTROL.ROM (65 536) og MT32_PCM.ROM (524 288). ROM-filene er Roland MT-32-ROM for musikkemulering i ScummVM, ikke en del av spillet, og er valgfrie.
- SHA-256 for alle filene står i `game/SHA256SUMS` i grenen `spilldata`.
- Kopi i grenen `spilldata` (uten felles historikk med `main`). MONSTER.SOU ligger i to deler på høyst 90 MiB (`MONSTER.SOU.001` og `.002`). `tools/hent_spilldata.sh` setter den sammen og sjekker summene.
- Repoet er offentlig etter Toms valg 10. oktober 2026 ("Offentlig, som The Dig").
- Spillfiler og alt laget fra dem (work/, mods/) skal aldri inn i main.

## Format (sjekket 10. oktober)
- SAMNMAX.000 og .001 er kryptert med XOR 0x69. Etter XOR: SAMNMAX.000 har blokkene RNAM (tom), MAXS, DROO, DSCR, DSOU, DCOS, DCHR, DOBJ og AARY. SAMNMAX.001 er én LECF-blokk over hele filen.
- Indeksen (plasser, i bruk): rom 95 (85), skript 122 (121), lyder 95 (94), kostymer 349 (348), tegnsett 6 (4), objekter 1100.
- I SAMNMAX.001 (målt med `gamedata.read_rooms`): 85 rom (42 på 320 x 200, 36 brede opptil 1104, 4 nesten tomme: 69, 80, 81, 82), 63 med z-plan, 2 med flere paletter (7 og 51), 43 med fargesykling, 959 objektbilder på 715 objekter, 348 COST med ID 1 til 348 i DCOS, 120 SCRP, 94 SOUN, 4 CHAR, 564 LSCR. Paletter i PALS/WRAP/APAL som i v7.
- MONSTER.SOU starter med `SOU `.

## Oppsettet (10. oktober)
- Tom ville ha repoet satt opp på samme måte som Dig-HD-Remake, med skillen `scumm-hd-remake`, og valgte "hele oppsettet, tilpasset": samme mapper og filer, tilpasset der det går, og det som ikke er portet til v6, merket.
- Kopiert fra Dig-HD-Remake (main 36cd09f): `engine/` (patch, byggeskript, nettsidekode), `pipeline/` (omdøpt fra `dighd` til `smhd`), `tools/`, `docs/`, `spill.sh`, `.github/workflows/test.yml` og `linux.yml`. The Dig-spesifikke data (konseptbilder, romnotater, figurliste, avvisninger, kostymefarger, grafikkpiloten) er ikke tatt med; CSV-filene har bare overskrifter, unntatt `docs/rom-oversikt.csv`, som er fylt fra Sam & Max-filene.
- Miljøvariablene `DIGHD_*`, klassen DigHD, `dighd.cpp/.h`, patchnavnet og mod-formatet beholdes, fordi patchen er den samme.
- `gamedata.py` leser både v6 (Sam & Max, XOR 0x69) og v7 (The Dig). `smhd info` virker.
- Uttrekket (10. oktober): egne dekodere oversatt fra ScummVM i `pipeline/smhd/v6grafikk.py` (SMAP-kodekene 1, 15 til 18, 25 til 28, 34 til 38, 48, 104 til 108, 124 til 128; BOMP; klassiske COST i format 0x58, 0x59, 0x60, 0x61) og `eksport_v6.py`. `smhd extract` gir 83 rom, 959 objektbilder og 16 052 kostymeruter fra 348 kostymer på omtrent halvannet minutt.
- Rutenummer i Sam & Max-kostymer = lag * 128 + kode (filnavn costumeCCC_NNN). Bare ruter som animasjonene bruker, tas ut. Kostyme 2 er Sam og 3 er Max (begge i rom 1).
- Kostymefarger: COST-paletten peker på indekser i rompaletten; bare 0 til 15 er like i alle rom (Sam og Max bruker 234 til 255). RGBA-bildene bruker paletten i rommet kostymet ligger i.
- Skriptene: `tools/bygg_descumm.sh` (scummvm-tools 8665aa1d) og `tools/dekompiler_skript.py` dekompilerer 1181 skript til work/skript (1179 uten feil; to stopper på 0xBD, som er o6_dummy i ScummVM).
- `hd-mod` har første HD-mod fra 14. oktober (e85f760). `gpt-arbeid` har jobbene og ordren for neste runde.
- `tools/gpt_gren.sh send` kopierer `docs/gpt-arbeid-AGENTS.md` over AGENTS.md i `gpt-arbeid`. Det Codex legger til der, må også inn i kilden i main, ellers forsvinner det.
- `myk.py` velger leveransen med sha256 lik filen når en jobb har flere oppføringer i `fremdrift.json`; rapportmappene sorteres på navn, ikke tid.
- Linux-arbeidsflyten kjører bare for hånd eller om natten når `hd-mod` endres; push-utløseren er av til HD virker.
- Nettsiderepoet (planlagt `Tombonator3000/Sam-Max-HD-Web`) finnes ikke.

## Teknisk plan (fra The Dig, ikke testet for Sam & Max)
- Referanse: github.com/Tombonator3000/Dig-HD-Remake og skillen `scumm-hd-remake`. The Dig-patchen er for SCUMM v7 og kan ikke kopieres rett.
- DigHD er på for Sam & Max fra 10. oktober (`DigHD::create` godtar `GID_SAMNMAX`). Endringer i patchen for v6: kroker i `ClassicCostumeRenderer` (`drawLimb` setter rutenummer lag * 128 + kode, `markAsDirty` husker rektangelet, `paintCelByleRLE` kaller `noteCel`), `beginActor` også for klassiske kostymer, pekerkroken i `ScummEngine::updateCursor`, testhoppet leser RMHD i v6-format, `DIGHD_TEST_COSTUME` leser COST-hodet, blast-objekter får bildet som faktisk tegnes (Sam & Max ber om 0, motoren bruker 1).
- Viktig v6-forskjell: `drawStripToScreen` legger tekstlaget over bufferen i `_compositeBuf` før blit. `blitVirtScreen` får derfor også `vsSrc` (området i bufferen) for merkene per piksel; uten det fikk ingen figurer HD.
- Ikke portet: tekst (`CharsetRendererClassic`) og menyraden HD Graphics for v6. Ctrl+H virker.
- Sam & Max er v6: kostymene tegnes av `ClassicCostumeRenderer` (`costume.cpp`), ikke AKOS. Teksten av `CharsetRendererClassic`. Ingen SMUSH-filmer, mellomsekvensene tegnes av motoren. Blast-objekter finnes i v6. Blast-tekst er tom i `ScummEngine_v6` ved c9091321 (skillen sier den finnes; må sjekkes i spillet).
- Funnet i ScummVM-kilden 10. oktober: pekerkroken i patchen ligger bare i `ScummEngine_v7::updateCursor`, og menyraden HD Graphics står med v7-koordinater i `setUpMainMenuControls`. Begge må lages for v6.
- `engine/build.sh` bygger med `--disable-mt32emu`, så MT-32-ROM-filene brukes ikke. Uten MIDI-utgang spiller iMUSE musikken med AdLib.
- Nettsiden: `engine/pages` er tilpasset (filfilter, MONSTER.SOU-deler, samnmax), 16 nodetester består, men den er ikke bygget eller prøvd i nettleser. Lerretet venter på loggen `DigHD: screen`, som ikke kommer før DigHD er på.
- ScummVM-ID `samnmax`. Låst til commit c9091321 (`engine/SCUMMVM_COMMIT`), samme som The Dig.
- For uttrekket: enten en dump-modus i motorpatchen eller egne dekodere etter ScummVM-kildene. Ikke bestemt.

## Arbeidsform
- Roller: Claude koden, ChatGPT/Codex grafikken, Tom godkjenner.
- Claude får ikke flette sine egne PR-er herfra (sikkerhetskontrollen, 10. oktober). Tom fletter når CI er grønn.
- Stilpilot med ett rom og ett figurark før noe bestilles i mengde. Ta glatt figurstil med ekte alfa fra starten (lærdom fra The Dig).
- Stilpiloten (valgt 13. oktober): hovedark for Sam og Max, kontoret (rom 7, to deler) og første figurark for kostyme 2 og 3. Så lenge `stil/` er tom, skriver `smhd gpt-ordre` bare piloten i ORDRE.md.

## Kildetro grafikk og design (12. oktober 2026)
- Tom ba om samme regel i remake-skillen i Dig, Sam & Max og Zak: avklar motiv, funksjon, palett, figuridentitet og design fra riktig originalkontekst før grafisk HD-arbeid, også stilpilot.
- Skillen ligger i `docs/skills/scumm-hd-remake/SKILL.md`. Den er koblet fra AGENTS, remastermetoden, bestillingen og malen for grafikkgrenen. Spillets egne stilvalg gjelder; Dig sine figurer og materialer er ikke designfasit for de andre spillene.
- Rett påviste feil i produksjonsgrunnlaget før generering. Beskyttede jobbfiler beholdes; korrigert prompt og kildebegrunnelse leveres i et separat notat.
- Visuell kontroll av mening, identitet og hele animasjoner i spillet kommer i tillegg til teknisk mottak. Innført regel er ikke bevis for at alle ressursene er analysert eller spilltestet.

## Grafikkjobbene (13. oktober 2026)
- Tom: klargjør all grafikken til ChatGPT, samme størrelse i alle figurark, ingen oppdiktede eller endrede objekter, trofast HD. Fremgangsmåten er hentet fra Dig (`gpt-arbeid` der, hovedark som Full Throttle, `myk.py` versjon 3).
- `smhd gpt-pakke --figurer alle` gir 2 hovedark, 115 romjobber (76 rom), 86 objektjobber, 296 lagjobber (701 bilder), 9 ikonark (163 bilder) og 1758 figurark (15 661 ruter, 343 kostymer). Ligger i `work/gpt`, ikke i noen gren ennå.
- Fast størrelse: prompten gir målet på hver rute i 4x, og `tools/sjekk_leveranse.py` (bare numpy og Pillow) kopieres til `verktoy/` i `gpt-arbeid` så grafikeren kan sjekke før commit. `myk.py` versjon 4 merker grupper der tegnet størrelse spriker mer enn 12 prosent.
- Hovedark: `figur.MASTERS` (Sam kostyme 2 og nærbilde 27, Max kostyme 3 og nærbilde 28). Figurjobber for kostymer med `hovedark` i `docs/figurer.csv` får hovedarket som bilde to; senere ark av samme kostyme får første ark som bilde tre.
- Klassiske kostymer: palettindeks 13 er skygge (tegnes gjennom skyggetabellen) og tas bort fra arkene. Gjelder v5 og nyere: ScummVM setter `_shadowTable` bare da, så i Zak (v3) er 13 en vanlig farge. Kostyme 127, 132, 153, 211 og 280 er bare skygge og får ingen ark. Kroppen er oftest lag 1. Mot venstre speilvender motoren rutene mot høyre (ingen egne ruter).
- Seks ruter i kostyme 62, 133, 331 og 346 er søppel fra animasjonskoder utenfor kostymet (opptil 6189 px). `figur.MAX_CEL` = 640 x 400 holder dem ute.
- Paletter: `docs/kostymefarger.csv` (2, 4, 7 til rom 7; 104, 106, 107, 108 til rom 76; 334 til rom 88). Fra `tools/kostymer.py`, som leser skriptene.
- Romnavn i `docs/rom-oversikt.csv` (alle 85), engelske romnotater med skilttekst i `docs/gpt-romnotater.csv`, figurliste med navn og engelsk beskrivelse i `docs/figurer.csv`.
- CSV-filene i `docs/` skrives med LF (`lineterminator="\n"`), ellers klager `git diff --check`.
- Dynamisk lys (normalkart og luminansmaske) er planlagt etter stilpiloten: valgfritt for spilleren, ingen kastede skygger (Tom 13. oktober). Samme plan i Zak.
- Deling (13. oktober 2026): Tom tillater at grafikk og annet fra spillet deles utenfor repoet til hans eget private bruk (egne enheter, private steder). Offentlige sider og pakker har fortsatt ingen spillgrafikk. Spillfilene og det som lages fra dem holdes fortsatt utenfor `main`.
- Unntak (13. oktober 2026, Toms bevisste beslutning): lystesten på GitHub Pages har kontoret (rom 7) og hovedarkene til Sam og Max. Offentlig side; filene hentes fra `gpt-arbeid` inn i Pages-pakken av `pages.yml` og sjekkes ikke inn i `main`.
