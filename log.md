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

## 2026-10-10 17:36 til 18:45 (Claude)
- Tom: dekompiler Sam & Max og ta ut alle sprites. PR 1 var flettet (d4aa80c); ny arbeidsgren `uttrekk-v6` fra main.
- Skriptene (hjelpeagent): `tools/bygg_descumm.sh` henter scummvm-tools ved 8665aa1d og bygger bare descumm (fem kildefiler, ingen biblioteker). `tools/dekompiler_skript.py` dekrypterer filene og dekompilerer hver skriptblokk med `descumm -6` til `work/skript/` (globale, lokale, inngang, utgang og objektenes verbskript), med `OVERSIKT.md` og `objekter.tsv`. 1181 skript: 1179 uten feil, 2 lokale skript (rom 66 nr. 210 og rom 78 nr. 206) stopper på opkoden 0xBD, som ScummVM kjører som o6_dummy. Kontrollert at 3368 talereplikker peker på VCTL i MONSTER.SOU, at kall til globale og lokale skript treffer skript som finnes, og at objektene i 78 `loadRoomWithEgo` ligger i rommet. To bygg gir like filer.
- Grafikken: `pipeline/smhd/v6grafikk.py` med dekodere oversatt fra ScummVM ved c9091321: SMAP (`decompressBitmap`: rå, BasicV, BasicH, MajMin, med og uten gjennomsiktighet), BOMP (`bompDecodeLine`) og klassiske kostymer (`ClassicCostumeLoader`, `costumeDecodeData`, `drawLimb`, `byleRLEDecode`, med 0 som 256 i løpslengden og henvisningene i format 0x60 og 0x61). `pipeline/smhd/eksport_v6.py` skriver uttrekket i samme format som for The Dig. `smhd extract` bruker det for v6.
- `smhd extract` mot spillfilene: 83 rom (rom 81 og 82 har bredde 0), 959 objektbilder (856 SMAP, 103 BOMP), 16 052 kostymeruter fra 348 kostymer, 0 feil, omtrent halvannet minutt. 17 ruter har bredde eller høyde 0 og får ikke bilde; 175 animasjoner peker utenfor kostymet og står som advarsler i costumes.json (motoren leser dem bare om et skript ber om dem). Rutenummer = lag * 128 + kode.
- Sett på: alle rommene i et kontaktark, rom 2 med alle objektene lagt på plass etter CDHD, og den største ruten fra hvert av de 348 kostymene. Alt ser riktig ut; Sam er kostyme 2 og Max kostyme 3. Noen kostymer (127, 132, 153, 194, 211, 227, 280 og flere) blir magenta med paletten i rommet de ligger i; trolig skygger eller masker. Bare palettindeks 0 til 15 er lik i alle rom, så RGBA-fargene er fra kostymets eget rom. Ikke sammenlignet piksel for piksel med motoren.
- `smhd build-mod --name test-auto --method lanczos --kostymer 2,3`: 83 rom, 950 objektbilder, 175 kostymeruter. De 9 objektbildene i rom 81 og 82 tas ikke med, fordi build-mod hopper over rom uten bakgrunn.
- Tester: nye enhetstester for stripekodekene, SMAP og BOMP, og for kostymer i format 0x58 og 0x60 (syntetiske data), og en game-test for uttrekket. Den gamle testen som ventet at extract skulle stoppe, er fjernet. `pytest`: 33 bestått (31 uten spillfiler).
- `spill.sh --auto` og `tools/gpt_runde.sh` stopper ikke lenger på uttrekket. AGENTS, README, STATUS, todo, memory og docs (ANALYSE, HD-MOTOR, SPILLTEST, BESTILLING) oppdatert.
- Til Tom: `sam-max-sprites.zip` (rom, objekter og kostymeruter som PNG uten indeksbildene, med rooms.json og costumes.json), `sam-max-skript.zip` og to kontaktark. Laget fra `work/`, ikke lagt i repoet.

## 2026-10-10 18:48 til 19:31 (Claude)
- Tom: slå på HD-motoren. Ny gren `motor-v6` fra `uttrekk-v6` (PR 2 var ikke flettet).
- `DigHD::create` godtar `GID_SAMNMAX`. Testhoppet leser romstørrelsen fra RMHD i v6-formatet. Pekerkroken lagt i `ScummEngine::updateCursor` (v6), siden skjermen er RGB.
- Første kjøring (nearest-mod med rom og objekter, 3000 bilder fra start): 0 av omtrent 1 million HD-piksler skiller seg sterkt fra originalen, skjermen lik hele skjermen bygget på nytt, og "background without HD 0" i alle dumper. Uttrekket stemmer altså piksel for piksel med motoren.
- Kostymer: kroker i `ClassicCostumeRenderer` (`drawLimb` setter rutenummer lag * 128 + kode, `markAsDirty` husker rektangelet, `paintCelByleRLE` kaller `noteCel`), og `beginActor` i `base-costume.cpp` også for klassiske kostymer. Først fikk ingen figurpiksler HD: i v6 legger `drawStripToScreen` tekstlaget over bufferen i `_compositeBuf`, så `src` pekte ikke inn i bufferen der merkene står. `blitVirtScreen` får nå også `vsSrc` (området i bufferen) for merkene, og `src` for verdiene. Etterpå: Sam og Max i kontoret (rom 7) med HD-ruter, 0,26 til 0,29 prosent avvik i kantene av de skalerte figurene (skalatabellen mot jevn skalering, som i The Dig). Midlertidig logging brukt til feilsøkingen er fjernet.
- `DIGHD_TEST_COSTUME` leser animasjonene fra COST-hodet for klassiske kostymer. Med kostyme 2 (Sam) i rom 4: 57 animasjonsbytter, HD-ruter, 0 avvik.
- Blast-objekter: Sam & Max ber om bilde 0, og motoren bruker da bilde 1. Kroken fikk 0 og fant ingen HD. Nå får den bildet som faktisk tegnes. I motorveispillet (rom 68): 6907 av 6907 piksler med HD for objekt 604, og tilsvarende for de andre.
- `engine/test.sh` (nearest-mod med rom, objekter og kostyme 1 til 20): 0 avvik i alle dumper.
- `tools/romtest.sh --mod test-nearest --kamera ett --tidsgrense 45`: 85 rom, 62 ok med HD-bakgrunn, 0 krasj, 0 forskjøvne bilder, 0 kjøringer med skjermavvik. 12 rom hang etter testhoppet (skriptfeil fordi spillet ikke er i tilstanden rommet venter, for eksempel "state -1 is out of bounds" i rom 11, og ScummVM åpner feilsøkeren), 3 byttet til rom 0, 7 er mindre enn skjermen, rom 67 er svart. Kjørt i bakgrunnen; første forsøk ble avbrutt av tidsgrensen på 10 minutter i verktøyet.
- Ctrl+H bytter mellom HD og klassisk grafikk (testet med `DIGHD_TEST_KEYS=400:ctrl+h,500:ctrl+h`).
- Automatisk oppskalering (lanczos-sharp, kostyme 1 til 5) i kontoret: rom, objekter og Sam og Max fra modden. Figurene får harde kanter og ringer i oppskaleringen, som ventet; den ferdige grafikken skal males.
- Patchen laget på nytt (`git add -N` og `git diff`), og `git apply --check` mot c9091321 i en egen arbeidskopi bestått. The Dig er ikke testet med den utvidede patchen her.
- Ikke portet: teksten (`CharsetRendererClassic`) og menyraden HD Graphics for v6.
- Dokumentasjon oppdatert: HD-MOTOR (status, tester, listen over det som er portet), ANALYSE, SPILLTEST, PAGES, BESTILLING, gpt-kodeoppgaver, README, AGENTS, STATUS, memory, todo, og kommentarene i spill.sh, engine/run.sh, engine/test.sh, nettsidefilene, pakke_linux.sh og linux.yml.

## 2026-10-12 07:29 (Codex)
- Tom ba om å løse konfliktene i PR 2 (`uttrekk-v6`). Flettet `main` ved 5ef6f1f inn i arbeidsgrenen, uten å flette PR-en til main.
- PR 3 hadde allerede tatt med både uttrekkscommitten 3d74741 og motorarbeidet f2c0d55. Beholdt main-versjonene i alle ti konfliktfilene, slik at nyere HD-støtte og dokumentasjon ikke går tilbake. Før denne loggoppføringen og todo-punktet var hele resultatet identisk med main.
- Tester: 31 pipelinetester uten spillfiler bestått (Python 3.12, 2 game-tester valgt bort), 16 nodetester bestått, Pages-pakkeren kompilert med `py_compile`, og `bash -n` bestått for alle skallskriptene. Ingen spillfiler eller avledede filer spores i grenen. Ingen uløste konflikter.
- Motoren er ikke bygget eller startet på nytt; motorkoden er uendret fra main. Tidligere spilltester ovenfor er ikke kjørt på nytt.

## 2026-10-12 15:33 (Codex)
- Tom ba om regelen for kildetro motiv- og designanalyse i remake-skillen i Dig, Sam & Max og Zak. Oppdatert `docs/skills/scumm-hd-remake/SKILL.md` i Dig og lagt samme skill inn her i alle tre repoer.
- Regelen krever avklart originalkontekst, motiv, funksjon, palett, person/drakt og design før stilpilot eller nytegning. Hele animasjoner og sammensatte figurdeler kontrolleres visuelt i spillet i tillegg til teknisk mottak. Spillets egne stilvalg gjelder.
- Koblet regelen fra AGENTS, remastermetoden, bestillingen og malen for grafikkgrenen. Presisert at påviste feil i en prompt rettes i separat notat før generering når jobbfilene er beskyttet. Eksisterende godkjenninger gjelder fortsatt.
- Kontroll: skill-validatoren bestått for alle tre kopier, identiske skill-filer bekreftet med SHA-256, og lokale lenker og henvisninger til riktig repo kontrollert. `git diff --check` bestått. Ingen motor- eller pipelineendring; spillet er ikke startet på nytt og ingen ny grafikk er laget i denne oppgaven.

## 2026-10-13 08:03 til 09:20 (Claude)
- Tom: klargjør all grafikken så ChatGPT kan male den i HD. Samme størrelse i alle figurarkene, ingen oppdiktede eller endrede objekter, trofast remake. Se hvordan det ble gjort i Dig, og sjekk skillene. Lest AGENTS, memory, todo, log, remake-skillen og spill-gjenbruk, og `gpt-arbeid`, `myk.py`, bestillingen og hovedarkene i Dig-repoet.
- Romnavn for alle 85 rom i `docs/rom-oversikt.csv` (fra gjennomsyn og objektnavnene i skriptene). Engelske romnotater med skilttekst bokstav for bokstav i `docs/gpt-romnotater.csv` (rom med skilt, opp ned-rommet 40, Escher-rommet 37, polygonverdenen 49, silhuettene i 70 og 91 med flere).
- `tools/kostymer.py` (ny): leser skriptene, finner rommene hvert kostyme brukes i, velger palett og skriver `docs/figurer.csv` for alle 348 kostymer med navn, beskrivelse på engelsk og hovedark. Navnene er tatt fra replikkene (Kushman-brødrene, Shuv-Oohl, Doug, Trixie, Bruno, Conroy, håndlangeren). `docs/kostymefarger.csv`: åtte kostymer får annen palett, og `smhd extract` bruker den. Uttrekket kjørt på nytt.
- Skygger og søppel: palettindeks 13 er skygge i klassiske kostymer og tas bort fra arkene; fem kostymer som bare er skygge, får ingen ark. Seks ruter i kostyme 62, 133, 331 og 346 er søppel fra animasjoner utenfor kostymet og holdes ute (`figur.MAX_CEL`).
- Hovedark som i Dig (Full Throttle-måten): Sam og Max, satt sammen av start- og ståanimasjonen med nærbildet (kostyme 27 og 28). Figurjobbene for Sam og Max får hovedarket som bilde to, senere ark av samme kostyme får første ark som bilde tre.
- Fast størrelse: figurprompten gir målet på hver rute i 4x og sier at hoder, hender og øyne ikke gjøres større. `tools/sjekk_leveranse.py` (ny, bare numpy og Pillow) sjekker størrelse, plass og omriss per rute, og forskyvning og kanter for rom, objekter, lag og ikoner. `tools/gpt_gren.sh` kopierer den til `verktoy/` i `gpt-arbeid`. `myk.py` hentet fra Dig (versjon 3) og utvidet til versjon 4: merker grupper der tegnet størrelse spriker mer enn 12 prosent.
- Ikonarkene pakkes i rader rom for rom med flat bakgrunn som ikke finnes i ikonene: 9 ark i stedet for 82. Romprompten skrevet om for Sam & Max (ingenting legges til, fjernes eller ryddes, skilt kopieres, det skjeve beholdes).
- `smhd gpt-ordre` skriver bare stilpiloten (hovedark Sam og Max, rom007 i to deler, fig002_01, fig003_01) så lenge `stil/` er tom. Romnavnene står i ordren.
- Jobbene laget i `work/gpt` (`smhd gpt-pakke --figurer alle`): 2 hovedark, 115 romjobber for 76 rom, 86 objektjobber, 296 lagjobber (701 bilder), 9 ikonark (163 bilder), 1758 figurark (15 661 ruter fra 343 kostymer), omtrent 127 MB. Stikkprøver sett på.
- Sett i motoren uten skjerm (testhopp og dump): rom 92 viser Sam og Max i de samme fargene som uttrekket, rom 77 rulleteksten og tittelen. Rulletekstpanelene i 67 og 77 kom ikke på skjermen.
- Dokumentasjon: `docs/BESTILLING-CHATGPT.md` og `docs/gpt-arbeid-AGENTS.md` skrevet om (aktiv i stilpiloten, egenkontroll, fast størrelse), ANALYSE avsnitt 11, STATUS, README, memory og todo. CSV-filene i `docs/` skrives nå med LF.
- Tester: `pytest` 43 bestått (40 uten spillfiler og 3 med), nye tester for skyggepiksler, hovedark, ikonark, myke figurer, størrelsesspredning, egenkontrollen og pilotordren. `bash -n` på skallskriptene og `git diff --check` bestått. Egenkontrollen prøvd på syntetiske leveranser (riktig OK, rute 15 prosent for stor FEIL, rom 3 px forskjøvet FEIL).
- Ordren og grafikklisten fikk UTC-tid merket som norsk tid; `gpt.norsk_tid` bruker nå Europe/Oslo, også i committen fra `tools/gpt_gren.sh`. Jobbene er committet lokalt i `work/.gpt-gren` (gpt-arbeid), ikke pushet.
- Ikke gjort: ingen bilder laget, ingenting pushet til `gpt-arbeid` (venter på Toms ja), promptene ikke prøvd i ChatGPT, `myk.py` og egenkontrollen ikke prøvd på ekte leveranser. Figurene med «trolig» i figurlisten er ikke sett i spillet.

## 2026-10-13 09:34 (Claude)
- Tom sa ja til å pushe jobbene og til PR mot main. `gpt-arbeid` pushet (c96f80b): alle jobbene, hovedarkene, `verktoy/sjekk_leveranse.py` og ordren med bare stilpiloten.
- PR 4 mot main fra `ccr-f99918a6-v2s5v1` for koden og dokumentasjonen. Tom fletter når CI er grønn.

## 2026-10-13 09:35 (Claude)
- PR 4 (grafikkjobbene) squash-flettet til main som e0baba9 mens CI på siste commit fortsatt kjørte; nettleser og pipeline var grønne på commiten før (ef9c441), og siste commit endret bare logg, todo, STATUS og README. Arbeidsgrenen startet på nytt fra main.

## 2026-10-13 09:50 (Claude)
- Tom spurte om dynamisk lys med normalkart og luminansmaske (bilde av Pixel Art Lighter). Svar: det passer i HD-motoren som et siste steg per piksel, men strider mot trofast remake om det står på, og normalkartene er en ekstra produksjon. Tom: valgfritt for spilleren, ingen kastede skygger, vent til stilpiloten er godkjent. Lagt i todo og memory.
- Sjekket Zak-repoet (FM-Towns, v3): skyggeregelen herfra gjelder ikke der, fordi ScummVM bare setter skyggetabellen for v5 og nyere. Notert i memory her og i Zak.

## 2026-10-13 10:32 (Claude)
- Tom viste Bernard, Laverne og Hoagie fra Day of the Tentacle, original og remaster side om side, og ba om at metoden legges i guiden for hvordan originalgrafikk gjøres om til HD.
- Nytt punkt «Fra piksel til HD-strek, slik DOTT Remastered gjorde det» under Figurstilen i `docs/skills/scumm-hd-remake/SKILL.md`, og en henvisning under forbildene: samme positur, silhuett og proporsjoner, hver pikselklynge tegnet som det den forestiller, samme farge per flate, ren mørk kontur, flate farger med ett skyggetrinn, ingen nye detaljer, hodet ikke større. Med forslag til engelsk prompttekst. Skillen er lik i Dig, Sam & Max og Zak (SHA-256 kontrollert).
- Kort avsnitt i `docs/HD-REMASTER-METODE.md`. Bildet er ikke lagt i repoet (grafikken tilhører Disney/Lucasfilm).
- Sam & Max: samme regel i figurdelen av `docs/BESTILLING-CHATGPT.md`. Kopien i `gpt-arbeid` og figurpromptene i `figur.py` er ikke endret.
- 10:41 Codex (PR 6) påpekte at figurpromptene fortsatt ba om «smooth shading». Rettet `PROMPT_FIGURE` og `PROMPT_MASTER` i `figur.py`: overtegning som i DOTT, ren mørk kontur, flate farger med ett skyggetrinn og noen få høylys, ingen gradienter, tekstur eller dithering. Romprompten er uendret, fordi bakgrunnene i Sam & Max er malt. Presisert i skillen (alle tre kopier) at malte bakgrunner beholder malt lys og fargeoverganger. `pytest` 43 bestått. Jobbene laget på nytt og committet lokalt i `gpt-arbeid` (bare figur- og hovedarkpromptene, tidsstempler, ordren og bestillingen er endret), ikke pushet.
- 10:46 Codex påpekte at DOTT-punktet i skillen tvang tegneseriestil på alle spill og påsto at Double Fine tegnet over originalen. Rettet: punktene om form (samme figur, pikselklynger blir det de forestiller, farge per flate, ingenting nytt) gjelder alle spill; ren strek og flate farger gjelder bare tegneseriespill (DOTT, Sam & Max, Zak), og The Dig beholder sin malte stil. Overskriften sier nå «sett i DOTT Remastered», ikke «slik de gjorde det». Skillen er lik i alle tre repoer.

## 2026-10-13 11:01 (Claude)
- Tom sa ja til å pushe de oppdaterte jobbene. `gpt-arbeid` pushet (1a82e24): figur- og hovedarkpromptene med DOTT-metoden (overtegning, ren strek, flate farger med ett skyggetrinn) og `BESTILLING.md` med samme regel. Rom, objekter og bilder er uendret. PR 6 (Sam & Max), PR 7 (Zak) og PR 47 (Dig) med guiden er flettet.
- 12:28 Tom ba om et testrom for dynamisk lys som kan kjøres fra GitHub Pages. Laget `lystest/index.html` (én fil, WebGL2): eget testrom og egen figur tegnet i koden i flat tegneseriestil, med høydekart og lysmaske tegnet med de samme formene. Normalene regnes per piksel fra høydekartet. Tre lyskilder (bordlampe, musepeker, lys på figuren) med farge, styrke, rekkevidde og høyde; omgivelseslys, relieff, trinnvis lys, sammenligning med originalen og visning av normalkart, lysmaske og bare lyset. Figuren går dit man klikker og får lys fra den siden lampen står. Egne bilder (rom, normalkart, lysmaske) kan lastes inn lokalt. Ingen kastede skygger, som Tom bestemte. Ingen spillgrafikk på siden.
- Arbeidsflyt `.github/workflows/pages.yml` publiserer `lystest/` når den endres i main, og stopper hvis annet enn HTML havner der. Tom må sette Settings > Pages > Source til GitHub Actions.
- Testet i Chromium uten skjerm (SwiftShader, Playwright): ingen feil i konsollen, lys av og på, figuren som går forbi lampen, normalkartet, sammenligningen, eget rom med normalkart og 375 px bredde uten sideveis rulling (filvelgerne var for brede først; rettet). Første standardverdier gjorde bildet mørkere enn originalen og trinnvis lys ga harde ringer; omgivelseslys 0,85, svakere lamper og trinnvis lys av som standard. Ikke prøvd i Firefox, Safari, på telefon eller i selve spillmotoren.
- 12:33 Tom ba om testrommet med grafikken fra Sam & Max. Spillgrafikk kan ikke ligge på Pages (offentlig side, AGENTS). Knappen «Hent kontoret» henter i stedet rom 7 (to deler satt sammen, 1952 x 800) og Sam og Max (ruten mot høyre i hovedarkene, fargenøkkelen gjennomsiktig, høyde fra omrisset) fra `gpt-arbeid` via raw.githubusercontent.com når man trykker. HD-bildet fra piloten brukes når `resultat.png` finnes. Max følger etter Sam. Taklampe 1 og 2 i kontoret er lyskildene. Testet i Chromium uten skjerm: grafikken hentes (to forventede 404 for resultat.png), figurene går, lyset og sammenligningen virker, ingen andre feil. Figurene har ingen z-maske og tegnes foran stolen i forgrunnen.
- 12:34 Codex (PR 7): lysets rekkevidde ble skalert etter bredden, så brede rom fikk for stort lys (kontoret 1,5 ganger). Skaleres nå etter høyden. Nettlesertestene kjørt på nytt uten feil.
- 12:38 PR 7 flettet. Arbeidsflyten lystest-pages kjørte uten feil, og https://tombonator3000.github.io/Sam-Max-HD/ svarer med testsiden (sjekket med curl, ikke åpnet i nettleser fra Pages).

## 2026-10-13 12:39 (Claude)
- Tom: tillat at det deles utenfor repoet, til hans eget private bruk. Regelen i AGENTS er endret: grafikk og annet fra spillet kan deles utenfor repoet til Toms private bruk (for eksempel testsider på GitHub Pages og filer til egne enheter). Spillfilene og alt laget fra dem holdes fortsatt utenfor `main` og kodegrenene.
- Samme endring i `docs/gpt-arbeid-AGENTS.md`, `docs/BESTILLING-CHATGPT.md` og AGENTS i `gpt-arbeid`.
- 12:45 Presisert etter Codex (Dig PR 48): privat deling gjelder egne enheter og private steder. Offentlige sider og pakker (GitHub Pages, releaser) har fortsatt ingen spillgrafikk, så README, Linux-pakken, SPILLTEST og PAGES stemmer som de er.
- 13:25 Tom ba om tillatelsesregler for lystesten. Lagt inn `.claude/settings.json` med `Edit(lystest/**)` og `Edit(.github/workflows/pages.yml)`. Ingen endring i lystest eller arbeidsflyten ennå: AGENTS sier at offentlige sider ikke har spillgrafikk, så Tom må velge mellom offentlig Pages (endre AGENTS), en privat lokal versjon eller å beholde knappen.
- 13:33 Tom bestemte at lystesten skal være offentlig på Pages med kontoret og hovedarkene. AGENTS har fått et uttrykkelig unntak. `pages.yml` henter rom 7 og hovedarkene fra `gpt-arbeid` inn i pakken (`lystest/spill/`), og kjører hver sjette time for nye HD-bilder. Siden starter i kontoret og faller tilbake til raw.githubusercontent.com når den åpnes lokalt. Testet med en lokal kopi av pakken servert over http i Chromium uten skjerm: kontoret lastes fra pakken, bare oppslagene etter resultat.png går ut (404 til piloten er levert), ingen andre feil.
- 13:36 Codex (PR 9): en treg kontorinnlasting kunne overstyre testrommet eller et eget rom valgt i mellomtiden. Lagt inn et lastenummer (`lasteNr`) som øker ved hvert scenevalg; utdaterte innlastinger setter ikke scenen. Testet: vanlig innlasting gir kontoret, og med 2,5 s forsinkelse på grafikken og testrommet valgt underveis blir testrommet stående.
- 13:41 PR 9 flettet. Pages er publisert: https://tombonator3000.github.io/Sam-Max-HD/ svarer med «Sam & Max lystest», og spill/hovedark/sam/jobb.json ligger i pakken (sjekket med curl). Dig PR 48 er også flettet.
- 02:44 Tom ba om å flette og pulle gpt-arbeid. Fletting til main er ikke mulig (ingen felles historikk) og ikke tillatt (AGENTS). Hentet gpt-arbeid (bcd0a01, bestilling 60; stilpiloten godkjent av Tom 13. oktober, ankere i stil/) med `tools/gpt_gren.sh hent`: 1100 filer. `smhd gpt-inn` (13,5 min): godkjent 419, sjekk 31, avvist 26, levert 72 (figurark, venter på myke-figurer), ny 1716. Rom 76 av 76, objekter 83 av 86, lagbilder 534 av 701, ikoner 46 av 163, figurruter 0 av 15661 (ikke tatt inn ennå). Ikke bygget mod, ikke sendt rapport eller ordre tilbake.
- 03:06 Figurmottaket (`myk.deliveries`) valgte oppføringen fra den rapportmappen som sorteres sist etter navn. Rettet fig003_01 i bestilling 58 tapte dermed mot den eldre pilotoppføringen («sha256 stemmer ikke»). Velger nå oppføringen som stemmer med filen. Ny test, `pytest -m "not game"` 41 bestått. `smhd myke-figurer` på nytt: 73 ark, 916 ruter ok, 15 til gjennomsyn. `smhd build-mod --name gpt --method lanczos-sharp --rooms <76 rom> --egne work/gpt-ferdig`: 76 rom, 841 objektbilder, 931 kostymeruter (238 MB). Romtest med modden startet.

## 2026-10-14 03:17 (Claude)

- Første grafikkrunde ferdig. Modden lagt i `hd-mod` (e85f760, 238 MB): 76 rom, 841 objektbilder, 931 figurruter.
- Romtest med modden: 71 av 85 rom lastet, 61 ok med HD-bakgrunn, 0 krasj, 0 forskjøvet, 0 skjermavvik. 11 hang etter testhoppet, det samme som før HD. Små svarte felt (17 til 78 px) i 24 kjøringer. Disse er ikke forklart ennå.
- Rapport, retur.md, status, ORDRE, GRAFIKKLISTE og BESTILLING lagt i `gpt-arbeid` (07f3e04). Ordren ber om avvisningene først og så resten av listen.
- `gpt_gren.sh send` tok bort Codex sin linje om ANALYSE.md i AGENTS.md i `gpt-arbeid`. Rettet der (e5433e0) og i `docs/gpt-arbeid-AGENTS.md`.
- STATUS, README, todo og memory oppdatert for runden.

## 2026-10-14 03:23 (Claude)

- PR 10 flettet av Tom (myk.py velger riktig leveranse, status og dokumentasjon for første grafikkrunde). CI grønn, Codex hadde brukt opp kvoten og gjorde ingen gjennomgang. Sjekk-inn slettet.

## 2026-10-14 03:55 (Claude)

Tom: GPT har nådd bruksgrensen, fiks alt som kan fikses i mellomtiden.

- Romtest: de svarte feltene var spredte piksler fra mørke streker grafikeren har tegnet en piksel ved siden av originalens. `tools/romtest.py` teller nå bare sammenhengende felt (minst 16 px): 2 kjøringer igjen av 24 (benken i rom 28 og en strek i rom 85), begge tegnefeil. Romnavnene i rapporten kommer fra `docs/rom-oversikt.csv`.
- `build-mod` tar med objektbildene i rom uten bakgrunn (rom 81 og 82, 9 bilder), skalert alene. Ny test, og kjørt på de ekte bildene.
- `tools/gpt_gren.sh send` stopper når AGENTS.md i `gpt-arbeid` har linjer som ikke står i `docs/gpt-arbeid-AGENTS.md`, så Codex sine tillegg ikke forsvinner. `AGENTS_OVERSKRIV=1` for å fjerne dem med vilje.
- De 15 figurrutene til gjennomsyn: 12 hadde feil tegning (Max uten esken i fig091_05, for store hender i fig002_05, små deler i fig004_01, fig007_01 og fig236_01). `myk.py` versjon 5 skriver slike ruter (omriss for ulikt originalen) til `sjekk/costumes/` i stedet for `costumes/`, så de ikke kommer i modden. 3 ruter med bare størrelsesavvik er med som før.
- `smhd gpt-ordre` leser `myke.json`: ordren sa 0 ferdige figurruter, nå 919 av 15 661, og rutene som er holdt ute står øverst i ordren. `gpt_gren.sh send` tar med `forhandsvisning/myk_<ark>.png` for de arkene.
- Myke figurer tatt inn på nytt (73 ark), modden bygget på nytt (76 rom, 841 objektbilder, 919 figurruter), kort romtest i rom 2, 7, 9 og 28 uten feil, og lagt i `hd-mod` (24f561d). Ny ordre i `gpt-arbeid` (c2f66c7).
- Motor: menyraden HD Graphics for v6. Raden står under Text Speed, og rammen er 14 piksler høyere nedover. Testet med F5 og klikk i introen: klikket gir klassisk grafikk.
- Motor: HD-tekst for Sam & Max. `CharsetRendererClassic` melder glyfene, og DigHD har et eget lag for tekstlaget i v6 (`_textV6`, skjermkoordinater). Introen med undertekster og originalmenyen har HD-tekst, og `DIGHD_VERIFY` gir 0 piksler som ikke er bygget på nytt. `engine/test.sh` 0 avvik. Patchen passer mot ren ScummVM.
- Blast-tekst: skriptene bruker ingen, bare blast-objekter.
- Rommene som henger etter testhoppet stopper på skriptfeil fordi variablene ikke er satt (rom 11 «state -1 is out of bounds», rom 50 «readArray: invalid array 261»). Krever lagrede spill.
- HD-skriften: apostrofen tegnes skrå (U+2019) som i spillets font. Kommer med i neste mod.
- Romtest i alle 85 rom med den nye motoren: 71 lastet, 61 ok, 0 krasj, 0 forskjøvet, 0 skjermavvik, svarte felt i 2 kjøringer, 11 hang som før.
- Merk: klikktesten lagret `dighd_classic=true` i `~/.config/scummvm/scummvm.ini` her; satt tilbake til false før de andre testene.
