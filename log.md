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

## 2026-10-14 07:05 (Claude)

- PR 11 flettet av Tom. Grenen satt til ny main.
- Todo «trolig»-kostymer og rulletekstpanelene: kostyme 103 er Trixie. Skript 120 setter kostymet mens fortelleren sier at hun leste godnatthistorier for Bruno. Rettet i `docs/figurer.csv` og i promptene til fig103_01 og fig103_02.
- Rulleteksten kjørt i motoren (rom 77). Panelene lånes fra rom 67 (objekt 600 til 603) og får HD. Tittel-kostymet (328) og fjellene (329) er originalpiksler til grafikeren har tegnet dem.
- To feil i HD-skriften funnet i rulleteksten og rettet: e, c og r ble store svarte former fordi kanten ble valgt som bokstav (`makeFaceGlyph` tegner nå slike glyfer fra fontbildet), og font 5 (pyntet, bare store bokstaver) ble små Exo 2-bokstaver. Font 5 er tatt ut av `skrift.py` og skaleres fra fontbildet.
- Testet: rulleteksten ser ut som originalen med glatte kanter, dialogen i introen bruker fortsatt HD-skriften (30 glyfer, ingen avvist), `engine/test.sh` 0 avvik, `pytest -m "not game"` 44 bestått, patchen passer mot ren ScummVM.

## 2026-10-14 07:55 (Claude)

- PR 12 flettet av Tom. Grenen satt til ny main, sjekk-inn avlyst.
- Todo «mellomsekvenser og minispill som tegnes av motoren»: kartlagt fra skriptene i `docs/MINISPILL.md`. Ingen SMUSH; det motoren tegner selv er `drawBox`, blast-objekter, skyggetabellen for figurer, lånte objekter, palettendringer, risting og noir-modus.
- Motor: figurpiksler tegnet gjennom skyggetabellen (skyggene under figurene, lyskjegler med skyggemodus 0x20) bygges nå fra HD-bakgrunnen og tones, som blast-skyggene. Testet i rom 16: lyskjeglen og lysstrålen er glatte, `DIGHD_VERIFY` 0 piksler ikke bygget på nytt. `engine/test.sh` 0 avvik, patchen passer mot ren ScummVM.
- Car Bomb-merkene (`drawBox` piksel for piksel) og noir-modusen står som åpne punkter i todo. Full romtest kjører.
- Full romtest med skyggekoden: 71 lastet, 60 ok med HD-bakgrunn, 0 krasj, 0 forskjøvet, 0 skjermavvik, svarte felt i 2 kjøringer. 12 hang: de 11 fra før og rom 79 (snøkulen). Rom 79 stopper på samme bilde (540 etter 120 s) også med skyggekoden slått av, og bruker lite CPU; det går tregt etter testhoppet og treffer tidsgrensen noen ganger. Ikke en følge av endringen.

## 2026-10-14 08:30 (Claude)

- Tom ba om en Windows-utgave som release, med HD-grafikken. Jeg foreslo først en pakke uten spillgrafikk (AGENTS-regelen); Tom sa at hele poenget er at HD-grafikken skal være med. AGENTS endret: releasene har spillet og HD-grafikken, Toms beslutning 14. oktober.
- Ny arbeidsflyt `.github/workflows/windows.yml`: bygger ScummVM med HD-patchen i MSYS2 (MINGW64) på Windows, henter spilldata og hd-mod, lager zip med `tools/pakke_windows.sh`, tester at spillet blir kjent igjen og at DigHD starter (SDL dummy, `DIGHD_QUIT_AT=600`), og publiserer release «windows» fra main. På andre grener blir zip-en en artefakt.
- Startfil `tools/windows/Sam og Max HD.bat`: fullskjerm, HD-mod, innstillinger og lagrede spill i %APPDATA%\SamMaxHD.
- HD-modden publisert på nytt med skriftrettingene (font 5 uten HD-skrift, skrå apostrof): hd-mod 5797a4b.
- Ikke testet her: ingen Windows eller MinGW i sandkassen. Første test er kjøringen i Actions.
- Windows-arbeidsflyten testet på grenen. Kjøring 1: bygg og pakke ok, testen fant ingen grafikkmodus (OpenGL uten skjerm). Kjøring 2: spillet startet med HD-modden, men stoppet på «IMuse initialization - Device not available» (ingen MIDI på maskinen). Kjøring 3 (38523014097) grønn med `--gfx-mode=surfacesdl` og `--music-driver=adlib` i testen. PR 14 mot main; releasen lages når den er flettet.

## 2026-10-14 09:15 (Claude)

- PR 14 flettet av Tom. Arbeidsflyten Windows-pakke kjørte fra main (38525134743, grønn) og publiserte release «Sam & Max HD for Windows»: SamMaxHD-Windows.zip (426 MB) med sjekksum.

## 2026-10-14 09:30 (Claude)

Tom: ja til Car Bomb på skriptnivå, implementer noir, lag en utviklermodus for å hoppe til områder.

- Car Bomb: `o6_drawBox` kjenner igjen den første boksen (14 x 9) i lokalt skript 207 i rom 66 og melder merket til DigHD (`noteBoxMarker`). Når skjermen bygges, leses merket ut av bufferen og tegnes som en glyf med xBR. Testet med den nye testkroken `DIGHD_TEST_SCRIPT` (fem merker i rom 66): glatte merker, 0 piksler ikke bygget på nytt.
- Noir: `updatePalette` gir DigHD fargepaletten og slår noir av og på (`setNoir`); DigHD gjør HD-bildet grått i `writeRect` og i dumpene, med samme snitt som ScummVM. Testet: introen hoppet over med Esc, tasten b i kontoret ved bilde 4400 og 5200 slår noir på og av, og bildet er grått.
- Utviklermodus: ingen romhopp i spillet selv (skript 64 har bare noir, versjon, minne og «dummy verb mode»). Laget «Sam og Max HD - utvikler.bat» i Windows-pakken (hopp til rom med romliste, last lagret spill, vindu), `tools/romtest.py --lagret MAPPE` (kjører hvert lagrede spill med `--save-slot`, rommet leses fra loggen) og `DIGHD_TEST_SCRIPT`. Testet romtest `--lagret` med et autolagret spill i kontoret: rom 7 ok med HD-bakgrunn, 0 avvik.
- `engine/test.sh` 0 avvik, patchen passer mot ren ScummVM. Dokumentert i SPILLTEST, HD-MOTOR og MINISPILL.

## 2026-10-14 10:00 (Claude)

Tom: Windows-pakken starter ikke (startfila lukker seg, kanskje jobb-PC), lag en nettløsning i Sam-Max-HD-Web, og er CD-musikken med?

- CD-musikken: Sam & Max CD har ingen CD-lydspor. ScummVM setter ikke `GF_AUDIOTRACKS` for spillet (`detection_tables.h`: MDT_ADLIB, MDT_MIDI, foretrekker General MIDI). Musikken er iMuse-MIDI inne i SAMNMAX.001 og er med i alle pakkene; den spilles med AdLib-emulering eller MIDI. MT-32-emulering med ROM-filene fra spilldata er satt opp som todo.
- Windows: startfilene kjører nå ScummVM direkte (ikke `start`), skriver loggen til %APPDATA%\SamMaxHD\scummvm.log og blir stående med feilkoden hvis spillet stopper. Utviklerstarten og romlisten er med i pakken (Windows-bygget på grenen var grønt).
- Nettsiden: koden i `engine/pages` henter nå fra det offentlige repoet uten nøkkel (fillister fra API-et, filer fra raw.githubusercontent.com) og ber om nøkkel bare når GitHub begrenser. Ny test; `node --test` 17 bestått.
- Sam-Max-HD-Web: arbeidsflyt som sjekker ut Sam-Max-HD, bygger med `engine/build-web.sh` og `engine/build-pages.py`, sjekker at ingen spillfiler er med, og publiserer på Pages fra main. Lokalt bygg stoppet: proxyen i sandkassen gir 403 på SDL3-arkivet fra GitHub.

## 2026-10-14 10:10 (Claude)

- PR 15 (Sam-Max-HD) og PR 1 (Sam-Max-HD-Web) flettet av Tom. Arbeidsflyten i web-repoet bygde motoren fra main og publiserte siden på https://tombonator3000.github.io/Sam-Max-HD-Web/.
- Testet siden i Chromium uten skjerm (Playwright med SwiftShader) med `?DIGHD_TEST_ROOM=7`: ingen nøkkel trengtes, spillfilene og HD-modden ble hentet fra repoet, talen lastet ned med fremdriftslinje, DigHD startet (1280 x 800) og kontoret vises med HD-bakgrunn, HD-figurer og inventaret. Ikke testet: lyd, mobil, en hel spilløkt.
## 2026-10-14 10:35 (Claude)

Tom: legg inn MT-32.

- `engine/build.sh` og `engine/build-web.sh` bygger med `--enable-mt32emu`. `engine/build.sh` lagrer valgene i `.dighd-valg` og konfigurerer på nytt når de endres, så `./spill.sh` får MT-32 uten `RECONFIGURE=1`.
- `engine/run.sh` (og dermed `./spill.sh`) velger `--music-driver=mt32` når ROM-filene ligger i `game/`. Linux-pakken og Windows-pakken tar med MT32_CONTROL.ROM og MT32_PCM.ROM, AppRun og startfilene velger MT-32, og nettsiden velger MT-32 når ROM-filene er med i spilldata. Windows-testen i Actions bruker nå MT-32 i stedet for AdLib.
- Testet her: motoren bygget med `USE_MT32EMU`, spillet startet med `--music-driver=mt32` uten lydkort, ROM-ene ble funnet («Falling back to MT32»: MT-32-ROM-ene, ikke CM-32L), 1500 bilder, avsluttet normalt. Lyden er ikke hørt.

## 2026-10-14 11:05 (Claude)

Tom (skjermbilder av kontoret i HD og klassisk): 1 piksler rundt HD-figurene, 2 hakker innimellom, 3 MT-32 på nettsiden, 4 (kuttet av).

- Punkt 1, årsak: figurene er skalert i rommet (Sam tegnes 36 x 44, originalruten er 40 x 52). ScummVM hopper over bestemte rader og kolonner etter en skalatabell og kan tegne én piksel utenfor rektangelet. `markCel` regnet med jevn skalering, så kantpikslene ble ikke merket som figurens og sto igjen som originalpiksler. Rettet med `nearCode` (kodene rundt punktet), én piksel ekstra rundt skalerte ruter, fargesjekk og at en piksel en annen rute eier, ikke tas. `softCelColour` gjør det samme for skyggesjekken under myke ruter.
- Punkt 1, del to: Sams hender er en egen rute (kostyme 4, rute 256) som er holdt tilbake (ChatGPT tegnet én hånd, ruten har to). Ruter uten HD-bilde i kostymer med myke ruter får nå bare indeksbildet i modden, og motoren glatter dem (`smoothCel`: xBR på omrisset, Scale4x på fargene). `build-mod` tar med indeksbildene (ny test, 47 bestått); lagt inn 48 indeksbilder i mods/gpt.
- Testet i rom 7: Max helt ren, Sam ren bortsett fra kanten mot stolen (z-masken i 4 x 4-blokker, kjent begrensning, lagt i todo). `DIGHD_VERIFY`: 0 piksler ikke bygget på nytt i 15 kontroller. `engine/test.sh` 0 avvik. Patchen passer mot ren ScummVM.
- Punkt 2: på PC laster motoren raskt (rom 7 på 77 ms, ruter rundt 1 ms). På nettsiden ble hver fil hentet fra GitHub første gang spillet trengte den, og spillet ventet imens. Nettsiden henter nå hele HD-pakken i bakgrunnen fem sekunder etter start, figurrutene først (`prefetch`), og samme fil hentes bare én gang selv om spillet og bakgrunnshentingen ber om den samtidig. Ny test, `node --test` 18 bestått. Hele skjermen tar 14 til 22 ms å bygge her; nedtoninger kan bli tunge i nettleseren (todo).
- Punkt 3 var gjort (nettsiden bygget med MT-32 08:30 UTC). Punkt 4 må Tom si hva var.

## 2026-10-14 11:40 (Claude)

- Full romtest med den nye motoren og modden (`--kamera ett`): 71 lastet, 60 ok med HD-bakgrunn, 0 krasj, 0 forskjøvet, 0 skjermavvik. De samme 12 rommene henger etter testhoppet som før.
- Modden med de 48 nye indeksbildene er publisert i `hd-mod` (`tools/mod_gren.sh send`, 238 MB).

## 2026-10-14 12:05 (Claude)

Tom: nettsiden hakket, PR 17 flettet, punkt 4 var ikke skrevet ennå.

- Kjørte arbeidsflyten i Sam-Max-HD-Web fra main; siden er ute med bakgrunnshentingen. Testet i Chromium uten skjerm (SwiftShader): ingen lange stopp over 50 ms på 30 sekunder i kontoret med MT-32.
- Profilerte byggingen av hele skjermen med callgrind: fargetoningen (`tinted`) tok 55 prosent, med tre divisjoner per HD-piksel. Faktorene regnes nå én gang per originalpiksel (`tintFactors`, `applyTint`). Hele skjermen i kontoret gikk fra rundt 15 til rundt 11 ms. `engine/test.sh` 0 avvik, `DIGHD_VERIFY` 0 i 15 kontroller, patchen passer.
- Nettsiden: `?adlib` velger AdLib i stedet for MT-32, så Tom kan sammenligne om MT-32-emuleringen er det som hakker.

## 2026-10-14 13:10 (Claude)

Tom (fem skjermbilder fra nettsiden): piksler bak Max, rester rundt objekter, piksler når figurene går bak ting, piksler rundt inventaret, artefakter ved sceneskifte.

- Sceneskifte: tekst med svart skygge som slettes med svart, beholdt skyggepikslene som HD-bokstaver (prikkete tekst). Rettet i `textAt`. Ved nedtoning ble svarte originalpiksler stående lyse i HD; nå følger de fargene rundt. Introen: logoen tones nå helt til svart (før 0,3 prosent lyse piksler). `DIGHD_VERIFY` 0 i 150 kontroller etter at `writeRect` bygger én piksel ekstra.
- Det oransje pikselbildet ved Max var musepekeren: den glattes nå (xBR og Scale4x).
- Figurer uten HD-tegning (flagg, folk, Sams hender) glattes i motoren: modden har nå indeksbildet for alle 15 085 ruter uten HD-bilde (26 MB).
- Flaggene og propellen i rom 17 er objekter med tilstander som bare er lapper. Motoren husker hver tilstand og bruker den forrige under lappen; `build-mod` skalerer lapper på plass over den hele tilstanden i stedet for å bruke ChatGPTs frittstående lapp (39 bilder byttet). Propellen har fortsatt svake spøkelseslinjer fra ChatGPTs bredere blader; trenger hele tegnede bilder (todo).
- Forgrunnen: z-masken glattes med xBR, så kanten mot stolen i kontoret er myk.
- Inventaret: ikonene (rom 93) og inventartingene (rom 94) var ikke i modden fordi rommene er smalere enn skjermen. `build-mod` tar dem alltid med, skalert med Scale4x (ny metode for pikselgrafikk). Esken (obj995) er ChatGPTs tegning med den prikkete teksten fra originalen; kanten blir trappete fordi tegningen ikke har egen alfa (todo til grafikkordren).
- Pipeline-tester 49 bestått, `engine/test.sh` 0 avvik, patchen passer. Hele skjermen 13 til 16 ms (litt mer enn før naboregelen).

## 2026-10-14 13:40 (Claude)

Tom (bilder fra nettsiden, før PR 18 er flettet): artefakter i HD-grafikken og flagget i rom 17, artefakter rundt logoen i introen, ønske om automatisk fjerning av slike feil, mer lettlest tekst, svarte kanter rundt Sam og Max foran svanen, piksler bak kjerubene. Og: legg inn gjennomgangen fra Just Adventure som ressursbank.

- Introen: de små logoene er skalerte blast-objekter tegnet med fargetabell. Motoren godtar nå HD-bildet når fargen er en tonet utgave av koden, og slår opp riktig piksel i skalerte objekter. HD-andel 32 til 99,8 prosent.
- Automatisk rensing: `build-mod` fyller magentaflekker i malte bilder fra fargene rundt; kjørt på modden: 9 085 piksler i 231 bilder (obj049 og karnevalsobjektene 661 til 807 mest). Rom 84 (Max's Wax, ekte magenta) er urørt. Ny test, 50 bestått.
- Teksten: HD-skriften byttet fra Exo 2 til Atkinson Hyperlegible (fet, laget for lesbarhet, OFL). Sett i introen.
- Svarte kanter foran svanen og pikslene bak kjerubene: svanen er en figur uten HD-tegning, og bak Sam ble bakgrunnen bygget uten svanen. Med PR 18 glattes figurer uten tegning og legges som egne myke figurer, så Sams kant faller på svanen. Kjerubene er animasjonslapper som flaggene.
- Ressursbank: `docs/GJENNOMGANG.md`, egen oppsummering sted for sted med romnumre, hvem som er der og tingene som hører til; kilden lenket og kreditert. Henvist fra AGENTS.md og `docs/gpt-arbeid-AGENTS.md`.
- Romtest med motoren fra PR 18: 71 lastet, 60 ok, 0 krasj, 0 skjermavvik, samme 12 hang. Små svarte felt i rom 8 og 28 (todo). `engine/test.sh` 0 avvik, patchen passer.

## 2026-10-14 14:30 (Claude)

Tom: spillet krasjer på nettsiden når Sam plukker opp pengene i musehullet.

- PR 18 er flettet (uten den siste committen med logo, skrift og magenta). Nettsiden ble bygget fra main kl. 11:26.
- Gjenskapt i Chromium uten skjerm med testkrokene i adressen (`?DIGHD_TEST_ROOM=7&DIGHD_TEST_SCRIPT=700:206:0`; skript 206 er opplukkingen, fra `work/skript/rom_007/lokal_206.txt`). Med `?adlib` kom den egentlige feilen: «Common::Array: failure to allocate». Motorens minne vokste med rundt 3,5 MB per fil den hentet, til 2 GB etter to minutter.
- Årsak: ScummVMs filsystem for nettleseren (`backends/fs/emscripten/http-fs.cpp`) hentet og tolket mappelisten (`index.json`) på nytt for hver fil som ble åpnet, og frigjorde aldri teksten, den tolkede JSON-en eller nodene. Mappen med figurruter fikk 15 000 nye filer i forrige runde (indeksbildene som motoren glatter), så hver lekkasje ble stor. Rettet: én delt liste per mappe (`listing()`), teksten og JSON-en frigjøres. Ligger nå i patchen. Kompilert med em++ (bare syntaks; nettbygget skjer i Actions).
- Testkroken `DIGHD_TEST_CLICKS` tar høyreklikk (`r` til slutt), og loggen viser objektet under klikket.
- Testet nettbygget fra grenen (arbeidsflyten i Sam-Max-HD-Web startet fra grenen sin, som bygger uten å publisere; artefakten lastet ned og servert lokalt) i Chromium med skript 206: minnet holdt seg på 276 MB gjennom 618 filhentinger og 7 minutter, ingen krasj. Den publiserte siden (før rettelsen) nådde 2 GB og krasjet etter 2 minutter. Tom fikk samme feil på gaten utenfor kontoret («failure to allocate»).
- Grenen er lagt oppå main etter at PR 18 ble slått sammen til én commit (PR 19).
- PR 19 flettet av Tom. Nettsiden bygget fra main og publisert; testet den publiserte siden i Chromium med skript 206 og MT-32: 278 MB gjennom 620 filhentinger, ingen krasj.

## 2026-10-14 15:30 (Claude)

Tom: ja til punkt 1 til 4 (pakkene på nytt, svarte felt, hakking, ressursbanken til ChatGPT).

- Arbeidsflytene Windows-pakke og Linux-pakke startet fra main (med PR 18 og 19).
- `tools/gpt_gren.sh` tar med `docs/GJENNOMGANG.md` som GJENNOMGANG.md; hentet (0 nye filer fra ChatGPT) og sendt til `gpt-arbeid`.
- De små svarte feltene i rom 8 og 28 er ChatGPTs maling (mørkebrunt nesten svart i rekkverket), ikke motoren.
- Hakking: `DIGHD_BENCH` virker nå uten skjermdumper (hvert 400. bilde), så den kan måles på nettsiden. Nettbygget kompileres med WebAssembly SIMD (`-msimd128`), så kompilatoren kan vektorisere bildebyggingen. Måles i nettleseren før og etter.
- Målt i Chromium (nettbygget fra grenen, med SIMD): hele skjermen 20 til 30 ms per bygg i kontoret (native 13 ms).
- Funnet under målingen: GitHub svarte 429 (for mange forespørsler) på bakgrunnshentingen, som prøvde å hente over 30 000 filer. Med uendelige nye forsøk ventet også spillets egne filer, og siden viste ventetid. Bakgrunnshentingen prøver nå hver fil én gang, venter et minutt ved grense og legger filen sist i køen (høyst tre forsøk); spillet henter selv en fil bakgrunnen ga opp. Indeksbildene for ruter uten HD-bilde står sist. Ny test, `node --test` 19 bestått.
- Windows-pakken er bygget på nytt fra main og lagt i releasen «windows». Linux-pakken bygges.
- Linux-pakken hang 50 minutter på testen i Debian 12 (spillet avsluttet ikke på TERM fra `timeout 30` i containeren). Kjøringen er avbrutt. Testen bruker nå `timeout -k 10 30` (godtar 124 og 137), og steget har `timeout-minutes: 10`. Releaseteksten sier ikke lenger at HD mangler. Arbeidsflyten må kjøres igjen fra main etter fletting.

## 2026-10-15 00:30 (Claude)

Tom: flettet PR 20, neste todo, så punkt 2 (The Dig) og 3 (grafikkordre).

- Nettsiden bygget fra main og publisert (med SIMD og ny bakgrunnshenting). Linux-pakken bygget fra main: testen i Debian gikk gjennom med rettelsen, releasen «linux» oppdatert. AppImage lastet ned, pakket ut og kjørt her i rom 17: HD-modden, Atkinson og MT-32 lastes, bildet er i HD.
- Ny ordre til ChatGPT (`smhd gpt-ordre` med beskjeder) sendt til `gpt-arbeid`: lapp-tilstandene tegnes som hele bilder (19 objekter listet), aldri magenta, obj049 på nytt, alfa og tydelig tekst på inventaresken obj995, ikke mørkere enn originalen (rom 8), bruk ressursbanken. Sams hender (fig004_01) står fortsatt øverst.
- `build-mod`: en lapp-tilstand som ChatGPT leverer som helt bilde (dekker minst 80 prosent av den hele tilstanden) klippes med lappens maske; en lapp tegnet alene skaleres som før. Ny test, 51 bestått.

## 2026-10-15 01:23 (Claude)
- Oppgave 2 fra todo: testet The Dig med Sam & Max-patchen. Spilldata og HD-modden (hd-mod) hentet i Dig-repoet. Nearest-testen kunne ikke lages der, dekoderne (thedig-textures) lot seg ikke hente fra denne maskinen, så testen ble kjørt med den ekte modden og et lite erstatningsuttrekk (romstørrelser og indeksbilder fra modden).
- Funn: Sam & Max-patchen alene ga kantete originalpiksler i kanten av skalerte astronauter i The Dig. Digs patch hadde fått presise figurmerker for AKOS (Codex, Dig PR 49 og 51) etter at Sam & Max ble kopiert ut 10. oktober. Kopiering ville tatt bort Digs rettinger.
- Slått sammen tre-veis fra Dig main 36cd09f: 10 konflikter (blast, markCel, z-kant, palettmasker og skyggetabell, objektoppslag). Digs kostyme- og objektnumre (119, 298 til 300, bølgene, pekerobjekt 650 og 688) gjelder nå bare The Dig. Objektoppslaget: Digs krav om at tilstanden fortsatt gjelder, sammen med Sam & Max sine lapp-tilstander (newest[]).
- Testet: Sam & Max `engine/test.sh` 0 avvik. Romtest Sam & Max: samme som før (rom 1 viste «hoppet ikke» fordi testkroken fra Dig ikke hopper når spillet alt står i rommet; `tools/romtest.py` godtar nå det). The Dig: intro 3000 bilder, skjermen lik full ombygging i alle 12 kontroller, kantene rene; romtest i 106 rom likt med Digs egen patch og den felles (105 lastet, 0 krasj, 0 heng). pytest 51 bestått.
- PR 21 åpnet for build-mod-klippingen og ordren fra forrige runde.

## 2026-10-15 05:11 (Claude)
- Tom (i Dig-økta): fiks den felles motorpatchen i Dig og Sam & Max, med rettingen fra kontrollen. Dig PR 53 er flettet; den felles patchen med lista over det som vises uten HD og rettingen (bakgrunn under myke figurer telles ikke) er Dig PR 54.
- `engine/patches/0001-dighd-hd-grafikk.patch` her er nå byte for byte lik den i Dig PR 54. Lista er beskrevet kort i `docs/HD-MOTOR.md` og `docs/SPILLTEST.md`. Tatt med fra grenen ccr-f99918a6-v2s5v1 er bare patchen; testfila `dighd-uten-hd.txt` som ble lagt i roten der, er ikke tatt med.
- Testet: spillfilene hentet, `smhd extract` (83 rom, 959 objektbilder, 16 052 ruter), `engine/test.sh` med motoren bygget fra patchen: skjermen lik full ombygging i 12 av 12 kontroller. Fem dumper i rom 3 (bilde 1500 til 2500) har 0,4 til 0,8 prosent HD-piksler som avviker kraftig fra originalen; det samme kom med patchen i main før endringen (0,38 til 0,48 prosent), så det er ikke nytt. Ikke undersøkt videre.

## 2026-10-15 05:55 (Claude)
- Den felles patchen har fått tre tillegg for Zak McKracken (FM-Towns), der HD-laget nå virker: `GID_ZAK` i `DigHD::create`, `objNNN_01` uansett tilstand i v3, testhoppet mot spillflaten. Byte for byte lik Dig PR 55.
- Testet: `engine/test.sh` med motoren bygget fra patchen, 12 av 12 kontroller lik full ombygging; avvikene mot originalen i rom 3 som før.

## 2026-10-15 14:34 (Claude)

Tom: ta inn ny grafikk til spillet.

- Ny grafikk i `gpt-arbeid` fra i dag: rettede rutekart for 73 figurark (931 ruter), tre ikonark med 111 ikoner til verbene og inventaret som egne RGBA-filer med myk alfa, og et nytt Max-ikon (obj1008_01) etter Toms avvisning.
- Oppsett på ny maskin: spilldata, pipelinen (uten `uttrekk`, thedig-textures lot seg ikke hente; `gpt_runde.sh` faller nå tilbake til det), `smhd extract`, motoren bygget fra patchen.
- `smhd gpt-inn`: alle 163 ikoner fra ikonarkene godtatt. `smhd myke-figurer`: 920 ruter ok, 11 til gjennomsyn (tegnet i annen størrelse enn gruppen, se todo).
- Nytt steg `smhd myke-ikoner` (`pipeline/smhd/ikoner.py`): ikonene fra `ikonmanifest.json` blir `objNNN_SS_hd.png` med egen alfa når arket er godtatt og sjekksum og størrelse stemmer. `build-mod` tar dem med. Motoren bruker `_hd.png` for blast-objekter og pekeren fra før. Ny test, pytest 49 bestått. PR 24.
- Ikonene sett på et kontaktark: motivene stemmer med originalene, de fire tomme kortene og det rosa feltet (obj887) er slik i originalen.
- Modden bygget (76 rom, 958 objektbilder, 923 figurruter, 304 MB) og publisert i `hd-mod`.
- Testet uten skjerm i rom 7: pekeren er det myke ikonet obj889 uten rosa rand (det utklipte hadde rosa rand). Inventaret åpnet seg ikke med testklikk eller tast etter testhoppet, så de nye inventarikonene er ikke sett i spillet.
- Ny ordre til ChatGPT med beskjed om ikonene og de 11 rutene, sendt til `gpt-arbeid`. Toms presisering i AGENTS.md der (se originalen og stilreferansene, spør ved uklart motiv) er tatt inn i `docs/gpt-arbeid-AGENTS.md`.

## 2026-10-15 15:45 (Claude)
- Ny 0001 fra Zak McKracken HD (5782de2): `compose()` i `dighd.cpp` kopierer HD-pikslene rett når fargen er uendret, uten tak og med 32-bits skjerm i samme format som HD-bildet (alfa 255 som før). Ellers den gamle veien; 16-bits skjerm er uendret.
- Målt i Zak (OpenGL under Xvfb, nearest-mod): 4,7 til 5,9 ms ned til 1,6 til 2,7 ms for hele skjermen. `engine/test.sh` 0 avvik med 16 og 32 bit, og bilder byte for byte like med gammel motor. Ikke testet med dette spillet.
- Bare `engine/patches/0001-dighd-hd-grafikk.patch` endret, byte for byte lik den i Zak, Sam & Max, The Dig og Dig-HD-Web.

## 2026-10-15 15:58 (Claude)

Tom: lag oppdatert Linux-pakke.

- Arbeidsflyten Linux-pakke startet fra main (PR 24 trengs ikke, pakken tar modden fra `hd-mod`). Pakken ble bygget og testet uten skjerm, men Debian 12-testen fikk `toomanyrequests` fra public.ecr.aws, også ved ny kjøring, så releasen ble ikke publisert.
- Rettet: testen henter Debian-bildet fra første speil som svarer (public.ecr.aws, mirror.gcr.io, docker.io). Grenen `linux-debian-speil`, PR 26. Arbeidsflyten kjørt fra grenen: mirror.gcr.io brukt, ingen manglende biblioteker, spillet startet, releasen «linux» publisert (hd-mod e3b7a78, modden fra 15. oktober 14:22).
- Testet: AppImage lastet ned fra releasen, sjekksummen stemmer, 111 myke ikoner med i modden, startet uten skjerm i rom 7 med HD-rom, HD-objekter, myke figurer og Atkinson-skriften. Ikke testet med skjerm og lyd.

## 2026-10-15 16:17 (Claude)

Tom: push ny grafikk til nettutgaven også.

- Nettsiden (Sam-Max-HD-Web) henter HD-modden i nettleseren rett fra grenen `hd-mod` (fillisten uten mellomlager, filene etter sjekksum), så den nye modden fra 14:22 er med uten ny bygging. Motoren på siden ble sist bygget fra main 16:00 (kjøring 38747604195), med samme patch.
- Sjekket: fillisten i `hd-mod` har 111 myke ikoner, raw.githubusercontent.com gir samme obj1008_01_hd.png som modden (sjekksum lik), siden svarer 200. Ikke sett i en nettleser denne gangen.

## 2026-10-15 16:52 (Claude)

Tom: pakk ny Linux-pakke med den nye grafikken.

- Ny grafikk i `gpt-arbeid` siden forrige mod: hele animasjonsmotiver og alfa (15:17, 22 jobbresultater) og en samlet importpakke (16:17, `rapporter/import-grafikk-20261015/manifest.json`): 30 hele motiver for lapp-tilstander, 12 tilstander av objekt 833, 834 og 836 med indeksbilder i rom 54-paletten, egen alfa for inventaresken obj995_01 og logoen obj049_01, og ikonene. obj835 avventer Toms avklaring og er ikke med.
- Runden: `gpt-inn` (ferdige objektbilder fra lag 534 av 701, ikoner 163 av 163), `myke-figurer` (920 ruter ok, 11 til gjennomsyn som før), `myke-ikoner` (111).
- Nytt steg `smhd importpakke` (`pipeline/smhd/importpakke.py`) tar inn pakken etter behandlingen i manifestet: 56 tatt inn, 0 hoppet over. `build-mod` bruker et eget indeksbilde fra `--egne` foran uttrekkets. Ny test, pytest 50 bestått. PR 28.
- Modden bygget (76 rom, 958 objektbilder, 923 figurruter, 113 myke objektbilder) og publisert i `hd-mod` (b5f33fd).
- Testet uten skjerm: rom 17 viser flaggene og teltene i HD uten lapp-blokker. Rom 54 henger etter testhoppet (kjent), så bassenget er ikke sett i spillet.
- Linux-pakken bygget fra main med den nye modden og publisert i releasen «linux» (bygget 14:48 UTC, Debian-testen gikk gjennom). Lastet ned: sjekksummen stemmer, ikonene, obj995 og indeksbildene for rom 54 er med, startet i rom 17 med HD.

## 2026-10-15 17:42 (Claude)

Tom: fiks bilkantene i rom 9 (rapporten i `gpt-arbeid`, `rapporter/rom009-bilkanter-20261015/RAPPORT.md`).

- Bekreftet årsaken: romobjekter bygges per originalpiksel, og alfaen i objektbildet ble ikke brukt, så kanten på bilen (obj089_01) fulgte originalens maske i trinn på 4 x 4 HD-piksler.
- `build-mod` gir malte objekter i rom med HD-bakgrunn myk alfa (`soft_alpha`). Motoren legger kanten over HD-rommet (`drawSoftObjectEdges`, aktiv bare for objektbilder med myk alfa). PR 29, bygger på PR 28.
- Testet: pytest 51 bestått. `engine/test.sh` 12 av 12 kontroller lik full ombygging, avvikene i rom 3 som før. Rom 9 uten skjerm med kameraet på bilen: tak, frontrute, støtfanger og halefinne glatte; lik full ombygging i alle kontroller, også etter Ctrl+H. Ikke sett: Sam og Max foran bilen, bilen som kjører bort.
- Modden bygget på nytt med myk alfa og publisert i `hd-mod` (9512fd8). Motoren i main bruker ikke alfaen for romobjekter, så den gir samme bilde som før til PR 29 er flettet.
- Linux-pakken bygget fra grenen `myke-objektkanter` og publisert i releasen «linux» (15:38 UTC) så Tom kan teste. Lastet ned, sjekksummen stemmer, startet i rom 9.
- Patchen er felles med Dig-HD-Remake; Dig-repoet har ikke fått endringen ennå.

## 2026-10-15 17:55 (Claude)

Tom: løs konfliktene i PR 29.

- PR 28 ble slått sammen til én commit i main, så PR 29 hadde den gamle importpakke-committen under seg og fikk konflikt i `pipeline/tests/test_pipeline.py`. Rettelsen for romobjektene er lagt oppå main på nytt, uten innholdsendring. pytest 51 bestått lokalt, CI grønn, PR 29 kan flettes.

## 2026-10-15 18:08 (Claude)

Tom: PR 29 flettet.

- Bygget fra main (9e1b7b2) med hd-mod 9512fd8: Linux-pakken (release «linux», 16:03 UTC), Windows-pakken (release «windows», 16:06 UTC) og nettsiden (Sam-Max-HD-Web, kjøring 38765138956). Alle tre arbeidsflytene grønne, siden svarer 200.
- Alle tre har nå de nye grafikkleveransene fra i dag og de myke kantene på romobjektene. Pakkene og siden er ikke spilt med skjerm etter denne byggingen.

## 2026-10-15 18:56 (Claude)

Tom: hent det nye fra hd-mod og gpt-arbeid inn i Sam & Max-repoet, og gi Dig HD Remake samme motorpatch.

- `hd-mod` og `gpt-arbeid` flettes ikke inn i main (spillgrafikk). Det nye i `gpt-arbeid` (18:06): seks rettede jobber (rom010 Sams tenner, rom015_del1av2 kjerub og djevel, lag037_01_del2av2, lag037_02_del1av2, lag045_03, obj811_01) og fire hele objektutsnitt med eget manifest (`rapporter/videre-grafikk-20261015/objektleveranser.json`).
- Runden: `gpt-inn` godkjente alle seks. `smhd importpakke` leser nå også `objektleveranser.json` (PR 30): 60 tatt inn, 0 hoppet over. Ny test, pytest 52 bestått.
- Modden bygget (76 rom, 959 objektbilder, 923 figurruter) og publisert i `hd-mod` (dd43c31). Rom 10 og rom 15 sett uten skjerm: tennene og kjeruben med djevelen er der. Ny ordre med status sendt til `gpt-arbeid`.
- Linux-pakken (16:52 UTC) og Windows-pakken (16:54 UTC) bygget fra main med den nye modden. Nettsiden henter modden selv.
- Dig-HD-Remake: samme motorpatch (myke kanter på romobjekter) i PR 57 der, byte for byte lik. Ingen av de 640 objektbildene i Digs `hd-mod` har myk alfa, så The Dig ser ut som før. Ikke kjørt med The Dig.
- Åpent fra grafikerens rapport: rester etter opplukking i kontoret, kantene rundt Sam og hammeren i Wak-A-Rat, chatrammene i spillet, og at mottaket måler Sam091 uten fotresten (8 ruter feilaktig til gjennomsyn).
## 2026-10-15 19:02 (Claude)

Tom: få Claude og ChatGPT til å samarbeide automatisk på Linux-maskinen og jobbe til i morgen, med grafikk og kode.

- Natteskiftet ligger i prosjektbiblioteket (`samarbeid/`, grenen claude/sleepy-hawking-492gnq) siden det skal brukes i flere repoer. Rollene er de samme som i AGENTS.md: Codex tegner jobbene i ORDRE.md i `gpt-arbeid`, Claude kjører `tools/gpt_runde.sh` og ser på bildene; Claude koder fra todo.md på grenen `samarbeid/natt-<dato>`, Codex kontrollerer.
- Codex kjører i sin egen sandkasse og kan ikke committe; skriptet committer bare `resultat.png`, `notat.md`, hovedark og `rapporter/` i `gpt-arbeid`. Det bruker samme arbeidstre som `tools/gpt_gren.sh` (`work/.gpt-gren`).
- Ikke kjørt her ennå. Testet bare med falske agenter i Claude-økta.
## 2026-10-15 20:05 (Claude)

Natt: kontroll av ny leveranse fra Codex (commit edec20f7 i `work/.gpt-gren`).

- Oppgaven nevnte fig091_04, men edec20f7 leverer en ny utgave av fig091_03 (bare rute 1955 tegnet om). fig091_04 er fra bestilling 59 (41bcb1b5). Begge er sett på.
- `tools/gpt_runde.sh`: henting, `gpt-inn`, `myke-figurer`, `myke-ikoner`, `importpakke` og byggingen av modden (76 rom, 959 objektbilder, 923 figurruter) gikk. Push til `hd-mod` feilet på innlogging mot GitHub, så runden stoppet før ordren. Kjørte `smhd gpt-ordre` og `tools/gpt_gren.sh send` med `SEND_UTEN_PUSH=1`: ordren er committet lokalt i `work/.gpt-gren` (dcd9962d, cb4ecc3e), ikke pushet. Klonen har ingen git-identitet; satt Claude som forfatter med miljøvariabler for den ene commiten, ingen konfigurasjon endret.
- Kontroll mot referanse.png, sett med øynene og målt: fig091_04 seks ruter, boksen rundt det synlige er lik originalen i 4x for alle, snitt delt på union 0,95, 0,96 og 0,85 (rute 1958 til 1961; forskjellen er konturtykkelse og den lille fotresten). Ingen ruter flyttet, lagt til eller fjernet, samme rekkefølge, lokket med gul stjerne og den løse fotresten er med. fig091_03 rute 1955: samme boks, snitt delt på union 0,93, positur, lokk og fotrest som originalen. Ingen tekst på arkene.
- Ingen avvisning: ingenting å legge i `docs/gpt-avvisninger.csv`.
- Figurmottaket holder likevel rute 1955 og 1957 til 1961 ute (status sjekk, tegnet 1,28 mot 4x), og ordren ber Codex tegne dem på nytt. Det er den kjente målefeilen (Sam091 uten fotresten, todo). La inn beskjed i ORDRE.md om ikke å tegne dem på nytt. Mottaket er ikke rettet i natt.
- Spørsmål til Tom: push fra denne maskinen krever ny innlogging mot GitHub. Ikke testet i spillet.

## 2026-10-15 20:19 (Claude)

Natt: kontroll av obj187_05 (oppgaven pekte på commit cb4ecc3e i `work/.gpt-gren`).

- cb4ecc3e er Claudes egen ordre-commit fra 20:05, ikke en ny leveranse. `origin/gpt-arbeid` står fortsatt på 55061f0d. `jobber/obj187_05/resultat.png` ble sist endret 13. oktober (61b58eaf), så det finnes ingen ny utgave av obj187_05.
- `tools/gpt_runde.sh`: henting, `gpt-inn`, `myke-figurer`, `myke-ikoner`, `importpakke` og byggingen av modden (76 rom, 959 objektbilder, 923 figurruter) gikk. Push til `hd-mod` feilet igjen på innlogging mot GitHub, så runden stoppet før ordren. Ordren er ikke skrevet på nytt: ingenting nytt er kommet inn, og beskjeden fra 20:05 i ORDRE.md skal stå.
- RAPPORT.md: obj187_05 avvist av mottaket (deler flyttet eller zoomet, opptil 7,9 px, kantlikhet 0,97).
- Sett med øynene mot originalen og referanse.png i forhåndsvisningen: avvisningen stemmer. Klubbehodet og hånden ligger lenger til venstre og høyere enn i referansen, hullene har mørke flekker rundt kanten, og fargen i bakgrunnen er jevnet ut. Ingenting lagt til eller fjernet, teksten på brettet er bare et utsnitt og ser lik ut.
- Ingen ny rad i `docs/gpt-avvisninger.csv`: mottaket avviste allerede, og `retur.md` med forslag ligger i jobben fra før.
- Fortsatt åpent spørsmål til Tom: push fra denne maskinen krever ny innlogging mot GitHub. Lokale commits i `work/.gpt-gren` (edec20f7, dcd9962d, cb4ecc3e) er ikke pushet. Ikke testet i spillet.

## 2026-10-15 20:25 (Claude)

Natt: kodeoppgave fra todo, mottaket for myke figurer måler Sam091 uten fotresten.

- Årsak: `measure_mask` tar den løse fotresten (36 eller 37 originalpiksler) ut som utligger, men tegningen ble målt med fotresten fra rutekartet. Høyden ble da 23 til 30 prosent for stor, plasseringen ble gjort mot originalen uten fotrest, og fotresten ble i tillegg lagt inn fra originalen.
- Rettet i `pipeline/smhd/myk.py`, versjon 6 (alle ark tas inn på nytt): ny `drawn_outliers`. Har originalen utliggere, tegningen mer enn én del, og ligger forholdet mellom høyde og bredde i tegningen nærmere originalen med utliggerne enn uten, måles og plasseres ruten med utliggerne på begge sider, og de legges ikke inn fra originalen.
- Ny test `test_soft_cel_drawn_outlier`. Sjekket at den feiler uten rettelsen. pytest i `pipeline`: 55 bestått.
- Kjørt på alle leverte ark i `work/.gpt-gren` til en midlertidig mappe i /tmp (ikke `work/gpt-ferdig`, ikke modden): 931 ruter ok og 0 til gjennomsyn, mot 920 og 11 før. De eneste som endret status er de 11 kjente: fig091_03 til 05 (fotresten, snitt delt på union nå 0,90 til 0,96) og fig209_03 og fig272_02 (én løs originalpiksel langt til siden som grafikeren har tegnet, så bredden ble målt 1,13 og 3,24 mot 4x; nå 1,0). Forhåndsvisningene for fig091_04 og fig272_02 sett med øynene: fotresten og pikselen ligger på originalens plass innenfor omrisset.
- Ikke gjort: modden er ikke bygget på nytt og ORDRE.md er ikke endret. Endringen ligger på natt-grenen og må gjennom PR mot main før `tools/gpt_runde.sh` tar inn rutene. Ikke testet i spillet.

## 2026-10-15 21:10 (Claude)

Natt: kontroll av ny leveranse fra Codex, obj187_05 (commit 01a36834 i `work/.gpt-gren`).

- `tools/gpt_runde.sh` gikk helt gjennom denne gangen: henting, mottak, myke figurer (73 ark, 931 ruter ok, 0 til gjennomsyn, nå med myk.py versjon 6), bygging av modden (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md sendt til `gpt-arbeid`. Innloggingen mot GitHub virker igjen.
- RAPPORT.md: obj187_05 står på sjekk (deler flyttet eller zoomet opptil 1,3 px), mot avvist med 7,9 px i forrige utgave. Codex sin egenkontroll: skift 0,07 originalpiksler, kantlikhet 0,94. Resultatet er 1430 x 1100, som er 208:160.
- Sett med øynene mot originalen og i forhåndsvisningen, og som et halvt gjennomsiktig lag over originalen i 4x: klubbehodet, hånden, armen, slipset, snuten og de tre hullene ligger der de ligger i originalen, uten doble konturer. Ingenting lagt til eller fjernet, ingen rotter eller treffeffekter. Den avskårne teksten på brettet («AK-A» til høyre og bokstavresten til venstre) er lik originalen. Det mørke rundt hullene og den utjevnede bakgrunnen fra forrige utgave er borte.
- Godkjent i kontrollen, ingen rad i `docs/gpt-avvisninger.csv`. Stilen er ikke godkjent av Tom. Ikke testet i spillet, og hele animasjonen med de andre tilstandene er ikke sett i motoren.

## 2026-10-15 21:37 (Claude)

Natt: kontroll av lag002_01, lag017_03_del1av2, lag017_03_del2av2 og obj307_01 fra Codex (commit 3f64f318 i `work/.gpt-gren`).

- `tools/gpt_runde.sh` gikk helt gjennom: henting, mottak, myke figurer, modden bygget (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md til `gpt-arbeid`. Mottaket godkjente alle fire.
- Sett med øynene: utsnitt per objekt fra referanse.png og resultat.png side om side, og originalobjektet mot rommet i 1x for å se hva tilstanden legger til.
- lag017_03_del1av2: godkjent. Rødt og gult flagg har samme brutte former, prikker og himmelhull som originalen. Kontrollpulten med de to røde spakene (obj184_02) har samme plass og antall knapper.
- lag017_03_del2av2: godkjent. Det grønne flagget har samme bruddstykker og prikker. Propellen på anda har tre blader i samme retninger og samme nav.
- lag002_01: avvist i `docs/gpt-avvisninger.csv`. Lampen obj896_01 er nå tent gul som i originalen. Men obj897_01 og obj900_01 har i originalen to ringer hver: den indre som også står i rommet, og en tynnere ytre ring som er selve tilstanden. Leveransen har bare én takket ring rundt hver kule, så tilstanden mister den ytre ringen. Notatet sier at to ringer er bevart; det stemmer ikke med bildet. Feilen sto også i forrige leveranse.
- obj307_01: avvist. Toppen av kikkerten er riktig (to skruer, fasetter, åpningen), men satt sammen med godkjent obj304_01 under gir den en tydelig søm ved rad 40: himmelen er lysere (ca. 120,180,252 mot 103,166,250) og rammens kant og skygge møter ikke. I originalen er farge og ramme sammenhengende. Mottaket måler bare mot originalen og ser ikke dette.
- Runden kjørt på nytt: begge står som avvist i status.csv, øverst i ORDRE.md med retur.md, og er sendt til `gpt-arbeid` (92392b21). Modden er bygget og publisert i `hd-mod` på nytt.
- Ikke testet i spillet. Stilen er ikke godkjent av Tom.

## 2026-10-15 22:20 (Claude)

Natt: kontroll av lag002_01, lag017_04_del1av2, lag017_04_del2av2 og obj307_01 fra Codex (commit ad9e48c7 i `work/.gpt-gren`).

- `tools/gpt_runde.sh` gikk helt gjennom: henting, mottak, myke figurer, modden bygget (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md til `gpt-arbeid` (1b571af9). Mottaket godkjente alle fire.
- Sett med øynene: utsnitt per objekt fra referanse.png og resultat.png side om side med originalobjektet i 4x.
- lag002_01: godkjent. obj897_01 og obj900_01 har nå to ringer hver som i originalen: en sterk indre ring og en svakere ytre ring (gulgrønn rundt den lyse kulen, lilla rundt den grønne). Lampen obj896_01 er fortsatt tent gul. Returen fra 21:37 er rettet.
- lag017_04_del1av2: godkjent. Den røde vimpelen obj180_04 har den lange remsen, de to oppstikkerne og den løse biten til venstre på samme plass som originalen.
- lag017_04_del2av2: godkjent. Gul vimpel med åpen løkke til høyre, grønne rester med samme antall løse biter, propellen med fire blader i samme stilling og nesten vannrett høyreblad.
- obj307_01: godkjent. Satt sammen med godkjent obj304_01 under: ingen synlig søm, himmelen er 109,164,248 på begge sider av skjøten, og snittforskjellen over skjøten er 3,1 mot 2,3 mellom to naborader i obj304_01. Rammen og skyggen møter. Toppen har to skruer, fasettene og den svarte åpningen som originalen. Returen fra 21:37 er rettet.
- Ingen rad i `docs/gpt-avvisninger.csv`. Ikke testet i spillet, og tilstandsbyttene er ikke sett i motoren. Stilen er ikke godkjent av Tom.

## 2026-10-15 22:20 (Claude)

Natt: kodeoppgave, kontroll av PR 32 (Codex, `codex/hd-masker-inventory`, native inventarkort og glassmasker).

- ScummVM `c9091321` hentet til /tmp, patchen fra main og fra PR 32 lagt på hver sin kopi (begge gikk rent). Hele kodeforskjellen lest (316 linjer i fire filer), med koden rundt. Patchen i natt-grenen er lik main.
- Fem funn i `docs/KONTROLL-PR32.md`. Viktigst: blast og romobjekt deler bildebufferen, og lastes `_hd.png` først som blast, mister romobjektet den myke alfaen (`softEdge` regnes ikke ut med marg på). Treffer trolig ikke dagens innhold: alle 113 `_hd.png` i `mods/gpt` er uten marg, og inventarikonene er SMAP-objekter i rom 93 og 94. (Rettet 23:00: feil, 13 inventarikoner i rom 93 er BOMP, se oppføringen 23:00.) Ellers: fargetoningen for myke romobjekter er nå ett snitt per bilde, de myke kantene fra PR 29 (bilen i rom 9) tones nå med rommets farge, og patchen er ikke lenger lik den i Dig.
- Ingen funn som stopper flettingen av det som treffer dagens innhold. Ikke flettet, ikke rettet, ingen kommentar lagt på PR-en.
- Ikke bygget og ikke kjørt: maskinen har ingen C++-kompilator, og ingenting er installert. `engine/test.sh` er ikke kjørt med PR 32.
- Testene i natt-grenen: pytest i `pipeline` 56 bestått, nettlesertestene 19 bestått.

## 2026-10-15 22:35 (Claude)

Natt: retting etter Codex sin kontroll av PR 32-kontrollen.

- Funn 4 i `docs/KONTROLL-PR32.md` rettet. Codex har rett: PR 32 skriver selv i `docs/HD-MOTOR.md` linje 7 at tillegget ennå ikke er samkjørt med The Dig. Funnet etterlyser ikke lenger dokumentasjon; det sier bare at samkjøringen med Dig avgjøres etter flettingen.
- Arbeidskopiene i `/tmp/smhd-pr32` (2,4 GB: ScummVM to ganger og patchene) er slettet. Enig i at de brøt nattregelen om ingen endringer utenfor repoet. Ingenting annet ble lagt utenfor repoet. Linjen under «Hvordan» i kontrollen sier nå at mappen er slettet. Neste gang en patch skal sjekkes mot ScummVM, bruker jeg en mappe under `work/`, som ikke sjekkes inn.
- Lot være: resten av kontrollen, som Codex ikke hadde innvendinger mot.
- Testene: pytest i `pipeline` 56 bestått, nettlesertestene 19 bestått, `git diff --check` uten feil.

## 2026-10-15 23:00 (Claude)

Natt: retting etter Codex sin andre kontroll av PR 32-kontrollen.

- Codex har rett. `work/extract/rooms.json` viser 13 BOMP-objekter blant inventarikonene i rom 93: obj874 til obj878, obj883 til obj886 og obj889 til obj892. Alle 13 har `_hd.png` i `mods/gpt/objects`. Sjekket med et kort Python-oppslag i `rooms.json` og filene. Rom 94 har bare SMAP.
- Rettet i `docs/KONTROLL-PR32.md`: linjen under «Hvordan», funn 1 og konklusjonen. Funn 1 er vurdert på nytt: forskyvningen treffer ikke (ingen marg), men den tapte myke alfaen kan treffe de 13 ikonene hvis samme objekt og tilstand tegnes både som blast og som romobjekt i samme rom. Det er ikke vist. Konklusjonen sier nå at funn 1 bør rettes, eller inventaret i rom 93 ses i spillet, før fletting.
- Begrunnelsen i oppføringen 22:20 er markert som feil med henvisning hit; resten av den oppføringen står.
- Lot være: å sjekke om ikonene faktisk går gjennom `blastSlot`. ScummVM-kilden ble slettet fra /tmp, og ny henting utenfor `work/` er ikke ønsket i natt; spillet kan heller ikke kjøres her. Spørsmål til neste kodeøkt eller Tom: tegnes BOMP-ikonene i rom 93 med `drawBlastObject`, som romobjekt, eller begge?
- Testene: pytest i `pipeline` 56 bestått, nettlesertestene 19 bestått, `git diff --check` uten feil. Motortesten er ikke kjørt (ingen C++-kompilator).

## 2026-10-15 22:53 (Claude)

Natt: kontroll av lag022_02_del3av3, lag047_02, lag052_01_del2av2 og lag052_02_del1av2 fra Codex (commit e107128e i `work/.gpt-gren`).

- `tools/gpt_runde.sh` gikk helt gjennom: henting, mottak, myke figurer, modden bygget (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md til `gpt-arbeid` (8389ad1e). Mottaket godkjente alle fire.
- Sett med øynene: hele referanse.png over resultat.png, utsnitt per objekt med 8 px marg (referanse i nearest, resultat side om side), og originalobjektene i `work/extract/objects` i 12x mot objektbildene i `mods/gpt/objects`.
- lag022_02_del3av3: godkjent. obj219_02 er den åpne mørke døren i buen, obj222_02 er øksefiguren med lutten og mannen med bøtta i samme stilling, obj228_02 er Henrik VIII med løftet åpen hånd. Ermet henger ikke igjen fra hvilestillingen.
- lag047_02: godkjent. Alle åtte objekter på plass: kameraet ved høyre kant (obj436), nebbdyret (obj437), frosken med åpen munn (obj438), bjørnehodet ved skiltet (obj442), katten (obj444_02 med lukket munn og rød nese som originalen), kamelens øye (obj447), figuren til venstre (obj451) og tukanens lille øye (obj453_01, som manglet i første forsøk). Skiltet staves BUMPUSVILLE SINGS som originalen.
- lag052_01_del2av2: godkjent. Vinduet med finnen til bilen utenfor (obj480), hyllen (obj481) og øglens munnfase obj486_01 uten oppdiktede røde merker.
- lag052_02_del1av2: godkjent. Tukanen med åpent nebb (obj483_02) og øglens neste fase obj486_02 med én liten grålilla flate i gapet som originalen. Plakaten staves THE REPTILE QUEEN og COLOR. Tukanens øye er rundt i HD mens originalen har en smal strek; det er likt det godkjente rombildet og obj483_01, så det er ikke avvist her. Spørsmål til Tom ved stilgodkjenningen: skal tukanen ha det smale øyet fra originalen?
- Ingen rad i `docs/gpt-avvisninger.csv`. Ikke testet i spillet, og faseovergangene for øglen og tukanen er ikke sett i motoren. Stilen er ikke godkjent av Tom.

## 2026-10-15 23:33 (Claude)

Natt: kontroll av lag052_03_del1av2, lag052_04_del1av2, lag052_05_del2av2 og lag052_06_del2av2 fra Codex (commit 68058936 i `work/.gpt-gren`, sikret etter 503-feil hos Codex). Ikke tegnet på nytt.

- `tools/gpt_runde.sh` gikk helt gjennom: henting, mottak, myke figurer, modden bygget (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md til `gpt-arbeid` (82805f06). Mottaket godkjente alle fire.
- Sett med øynene: øglens munnfaser obj486_01 til 06 side om side (original i nearest over HD-objektbildet, og tett romutsnitt referanse over resultat), og utsnitt med 8 px marg for obj489_01 og obj490_01. Kort Python-måling av hvilke originalpiksler hver fase endrer, og av avviket i HD nede til venstre mellom fasene.
- obj486_03 til 06: godkjent. Endringen ligger der originalen endrer seg: 03 en liten grålilla flate i gapet, 04 en større trekant, 05 en lang lys flate langs kjeven, 06 overkjeven løftet med lys flekk øverst til høyre. Foten og haken nede til venstre er lik i alle originalfasene; i HD er avviket mellom fasene der like lite som mellom de godkjente 01 og 02 (snitt 4 til 9 av 255 i RGB), så overgangene skal ikke hoppe synlig. Ikke sett i motoren.
- obj489_01: godkjent. Tukanens lukkede øye med den olivengrønne folden ved nebbet, samme plass som originalen.
- obj490_01: godkjent. Tom sittepinne uten tukan, tauene og stangen på samme plass som originalen. Merknad: stangen har noen små mørke merker på midten der originalen har en mørkere midtdel; de ser litt ut som tegn på nært hold, men er ikke tekst og leses som skygge i spillstørrelse. Tas med ved Toms stilgodkjenning.
- Ingen rad i `docs/gpt-avvisninger.csv`. Ikke testet i spillet, og faseovergangene er ikke sett i motoren. Stilen er ikke godkjent av Tom. STOPP-filen er ikke rørt.

## 2026-10-15 23:57 (Claude)

Natt: kontroll av lag052_07_del2av2, lag052_08_del2av2, lag052_09_del2av2 og lag052_10_del2av2 fra Codex (commit 3bdf5ce6 i `work/.gpt-gren`).

- `tools/gpt_runde.sh` gikk helt gjennom: henting, mottak, myke figurer, modden bygget (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md til `gpt-arbeid` (6803a651). Mottaket godkjente alle fire.
- Alle fire er obj486 i rom 52 (rute 232,152, 24x24), fasene 07, 08, 09 og 0A. Obj486 er øglens øye med dråpen under, ikke munnen som jeg skrev i de to forrige oppføringene; rutene der gjelder samme objekt, så kontrollen står.
- Sett med øynene: originalobjektene 06 til 0A i 10x nearest over HD-objektbildene i `mods/gpt/objects`, og romutsnitt av referanse.png over resultat.png for fase 06 til 0A. Kort Python-måling: alle piksler som endrer seg fra den godkjente fase 06 ligger innenfor objektruten (x 545 til 638, y 721 til 814 i lerretet), ingenting annet i rommet er rørt.
- obj486_07: godkjent. Øyelokket halvt ned, den grålilla dråpen under øyet som originalen.
- obj486_08: godkjent. Øyet lukket med den lange dråpen.
- obj486_09: godkjent. Øyet lukket, mindre dråpe som originalen.
- obj486_0A: godkjent. Øyet lukket, ingen dråpe, som originalen.
- Ingen rad i `docs/gpt-avvisninger.csv`. Ikke testet i spillet, og faseovergangene er ikke sett i motoren. Stilen er ikke godkjent av Tom.

## 2026-10-16 00:20 (Claude)

Natt: kontroll av lag052_11_del2av2, lag056_06, lag061_01_del1av2 og lag068_08 fra Codex (commit c0b5f112 i `work/.gpt-gren`).

- `tools/gpt_runde.sh` gikk helt gjennom: henting, mottak, myke figurer, modden bygget (76 rom, 959 objektbilder, 931 figurruter), push til `hd-mod` og ny ORDRE.md til `gpt-arbeid` (e004175e). Mottaket godkjente alle fire.
- Sett med øynene: hele referanse.png over resultat.png, og per objekt romoriginalen og tilstanden i nearest over godkjent romanker og resultat.png. Kort Python-måling: i alle fire jobbene ligger alle endrede HD-piksler (mot godkjent romanker) innenfor objektrutene, ingenting annet i rommet er rørt.
- lag052_11_del2av2 (obj487_01, rom 52): godkjent. Klørne på øglens fot er flyttet som i originalen: øvre grå klo vannrett mot høyre og nedre klo lenger ned. Notatet fra Codex kaller motivet munn og underkjeve; det er foten, men tegningen følger originalen.
- lag056_06 (rom 56): godkjent. obj539_01 er fryseren med åpen dør, mørk åpning med istapper og skrutrekkeren i vinduet som originalen. obj537_01 er bare en liten skyggeendring på rørbøyen i originalen, og HD-endringen er like liten og på samme sted.
- lag061_01_del1av2 (rom 61): godkjent. obj582_01 er brettenden med den knekte enden til høyre som originalen. obj585_01 er den grønne og gule strikken i løkke fra ringen, med festet til høyre for ringen og den lille grå krokbiten nede til venstre. obj581_01 er lik rommet også i originalen og er uendret.
- lag068_08 (rom 68): godkjent. De tre vegsegmentene med ett gult skråstrek på det nærmeste. I resultat.png er asfalten lysere enn originalen, men etter fargelåsen har objektbildene i `mods/gpt/objects` samme median som originalen (obj621_01 28,28,36 mot 27,27,35; obj631_01 26,25,28 mot 23,23,27). Den gule streken er litt lengre og bredere enn originalen; ikke avvist.
- Ingen rad i `docs/gpt-avvisninger.csv`. Ikke testet i spillet, og tilstandene er ikke sett i motoren. Stilen er ikke godkjent av Tom.
