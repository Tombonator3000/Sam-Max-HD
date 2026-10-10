# Sam & Max HD Remake: analyse av filer, omfang og veien videre

Skrevet 10. oktober 2026. Grunnlaget er spillfilene i grenen `spilldata`, indeksen `SAMNMAX.000` lest etter XOR, og kildekoden til ScummVM ved commit `c9091321` (`engine/SCUMMVM_COMMIT`). Oppbyggingen følger analysen i The Dig HD Remake. Det som ikke er målt ennå, står som "Ikke målt ennå", med hva som skal måles.

## Kort fortalt

- Spillfilene er den engelske CD-utgaven av *Sam & Max Hit the Road* (LucasArts 1993). MD5 for `SAMNMAX.000` stemmer med ScummVM sin oppføring for `samnmax`, CD, engelsk.
- Spillet er SCUMM v6. `SAMNMAX.000` og `SAMNMAX.001` er kryptert med XOR 0x69. Indeksen og blokkstrukturen i `SAMNMAX.001` er lest med `smhd info` (`pipeline/smhd/gamedata.py`).
- Dekompilering trengs ikke. ScummVM kjører spillet (`samnmax`), og skriptene kan leses med descumm. Arbeidet er HD-grafikken og å porte HD-patchen fra SCUMM v7 til v6.
- 85 rom (36 brede som ruller, ingen høye), 63 med z-plan, 2 med flere paletter, 43 med fargesykling. 959 objektbilder fordelt på 715 objekter. 348 kostymer. Hvor mange kostymeruter det er, er ikke målt (krever en COST-dekoder).
- Det er ingen SMUSH-filmer. Mellomsekvensene og minispillene tegnes av motoren, så de skal få HD gjennom de samme krokene som rom, objekter, figurer og tekst.
- Stilen er trofast HD: samme motiv og farger med mer detalj, og tegneserieuttrykket beholdes. En stilpilot (ett rom og ett figurark sett i motoren) skal godkjennes av Tom før noe bestilles.

## 1. Spillfilene

| Fil | Størrelse | Hva det er |
| --- | --- | --- |
| `SAMNMAX.000` | 9 080 byte | Indeksen: kataloger over rom, skript, lyder, kostymer, tegnsett og objekter. Kryptert med XOR 0x69 |
| `SAMNMAX.001` | 13 790 685 byte | Én LECF-blokk over hele filen. Etter v6-formatet ligger rom, skript, lyder, kostymer og tegnsett her. Musikken er MIDI (iMUSE) og ligger også her. Kryptert med XOR 0x69 |
| `MONSTER.SOU` | 183 195 967 byte | Talen. Starter med `SOU `. Ligger i grenen `spilldata` i to deler, `MONSTER.SOU.001` og `MONSTER.SOU.002` |
| `MT32_CONTROL.ROM`, `MT32_PCM.ROM` | 65 536 og 524 288 byte | Roland MT-32-ROM for musikkemulering i ScummVM. Ikke en del av spillet, og valgfrie |

Det er ingen filmfiler og ingen egne fontfiler.

**Hvor filene ligger:** originalen ligger på Google Drive (mappen `samnmax` i `Scummvm`). En kopi ligger i grenen `spilldata`, med SHA-256 for alle filene i `game/SHA256SUMS`. `tools/hent_spilldata.sh` henter grenen til `game/`, setter sammen `MONSTER.SOU` og sjekker summene. Testet fra en fersk klone 10. oktober.

**Utgave:** MD5 for `SAMNMAX.000` er `d917f311a448e3cc7239c31bddb00dd2`. I ScummVMs `engines/scumm/scumm-md5.h` er det `samnmax`, CD, 9080 byte, `EN_ANY`. Oppføringen står både i master (generert 27. september 2026) og ved `c9091321`. I `detection_tables.h` har `samnmax` flagget `GF_USE_KEY`, og for v6 gir `getEncByte` i `resource.cpp` nøkkelen 0x69. ScummVM dekrypterer altså filene selv.

**Indeksen etter XOR:** blokkene RNAM, MAXS, DROO, DSCR, DSOU, DCOS, DCHR, DOBJ og AARY. RNAM er tom, så rommene har ingen navn i indeksen.

## 2. Repoet

- `main` har dokumentasjon og verktøy, ingen spillfiler. `AGENTS.md`, `memory.md`, `todo.md`, `log.md` og `STATUS.md` er satt opp som i The Dig HD Remake.
- Kopiert fra The Dig HD Remake og under tilpasning: motorpatchen (`engine/patches/0001-dighd-hd-grafikk.patch`, uendret), pipelinen (`pipeline/smhd`, kommandoen `smhd`), verktøyene i `tools/`, `spill.sh`, nettsidekoden i `engine/pages`, Linux-pakken (`tools/pakke_linux.sh` og `.github/workflows/linux.yml`).
- Testet for Sam & Max 10. oktober: `tools/hent_spilldata.sh`, `engine/build.sh` (ScummVM med patchen bygget), spillet startet uten skjerm fra `game/` (se 8), `smhd info`, `tools/indeks_info.py` og Linux-pakken som AppDir (startet uten skjerm). Resten er ikke kjørt med Sam & Max.
- Ingen konseptbilder.

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer, uten felles historikk med `main` |
| `gpt-arbeid` | Arbeidsbordet med grafikerne. Tom startgren |
| `hd-mod` | Siste HD-mod, én commit som erstattes. Tom startgren |

## 3. Hva spillet består av

Tallene er lest 10. oktober med `smhd info` og `tools/indeks_info.py` (indeksen) og med `gamedata.read_rooms` (blokkene i `SAMNMAX.001`). Indeksen og datafilen stemmer: 85 rom i begge, og alle 348 COST-blokker har en kostyme-ID i DCOS.

| Del | Katalog | Plasser i indeksen | I bruk |
| --- | --- | --- | --- |
| Rom | DROO | 95 | 85 |
| Globale skript | DSCR | 122 | 121 |
| Lyder | DSOU | 95 | 94 |
| Kostymer | DCOS | 349 | 348 |
| Tegnsett | DCHR | 6 | 4 |
| Objekter | DOBJ | 1100 | Ikke talt |

**I `SAMNMAX.001`:** 85 LFLF med ett ROOM hver, 348 COST (kostymer), 120 SCRP (globale skript), 94 SOUN (lyder og musikk) og 4 CHAR (tegnsett). I rommene: 950 OBIM og 950 OBCD (objekter), 564 LSCR (lokale skript), og ENCD, EXCD, BOXD, BOXM, SCAL, CYCL, TRNS, PALS og RMIM i alle 85.

| Hva | Målt |
| --- | --- |
| Rommenes mål | 42 rom på 320 x 200, 36 brede som ruller (fra 416 til 1104 piksler; rom 31 er bredest), ingen høyere enn 200. 4 nesten tomme rom med bredde 0 eller 8 (rom 69, 80, 81 og 82). Til sammen 6,7 millioner piksler i 1x, 107 millioner i 4x |
| Z-plan | 63 av 85 rom har minst én forgrunnsmaske (ZP01 i IM00) |
| Paletter | Alle rom har PALS med WRAP og APAL. 2 rom har flere paletter (rom 7 og 51) |
| Fargesykling | 43 rom har sykling i CYCL |
| Objektbilder | 959 bilder (IMnn i OBIM) fordelt på 715 objekter. 235 objekter har ikke noe bilde. Plass og mål står i CDHD (v6) |
| Kostymer | 348 COST-blokker, alle med ID i DCOS (ID 1 til 348) |

Romlisten med mål, z-plan, paletter og objektbilder per rom ligger i `docs/rom-oversikt.csv`. Kolonnen `navn` er tom, fordi RNAM er tom; den fylles ved gjennomsyn.

### Ikke målt ennå

| Hva | Hva som skal måles |
| --- | --- |
| Z-plan | Hvor mange forgrunnsmasker hvert rom har (ZP02 og videre) |
| Fargesykling | Hvilke palettindekser som sykles, og hvor fort |
| Objektbilder | Hvilke som bare har BOMP-bilde (blast-objekter) |
| Kostymer og ruter | Antall ruter per kostyme, animasjoner og retninger, og største rute (krever en COST-dekoder) |
| Tegnsett | Hvilke tegnsett som brukes hvor (dialog, meny, bannere), med størrelse og antall farger |
| Lokale skript | Lokale skript og inn- og utgangsskript per rom (LSCR, ENCD, EXCD) |
| Mellomsekvenser og minispill | Hvilke rom og skript som står for dem |
| Figurer | Hvilke kostymer som er Sam, Max og de andre figurene |

## 4. Dekompilering: hva som faktisk trengs

Spillets exe-fil trenger ikke dekompileres. ScummVM har SCUMM v6-motoren (`ScummEngine_v6`), og spillet kjører der som `samnmax`.

Det som trengs, er to ting:

1. **Skriptene**, for å forstå når objekter skifter tilstand, når paletten byttes, og hvordan mellomsekvensene og minispillene er bygget. `descumm -6` fra scummvm-tools gir lesbar kode. Dette er oppslagsverk, ikke noe som skal endres. Ikke prøvd ennå.
2. **Grafikken**, som utgangspunkt for HD-versjonene: rom, objekter i hver tilstand og kostymeruter som indekserte PNG med palett, pluss JSON med metadata.

Om uttrekket:

- The Dig brukte dekoderne i thedig-textures. De kan bare lese The Dig, så `smhd extract` er ikke portet.
- To veier, ikke bestemt: en dump-modus i motorpatchen (motoren dekoder alt allerede, også alle ruter via kostymetegneren), eller egne dekodere i pipelinen etter ScummVM-kildene (`gfx.cpp`, `costume.cpp`). Ingen av dem er laget.
- `pipeline/smhd/gamedata.py` leser nå både The Dig (v7) og Sam & Max (v6, etter XOR 0x69): romstørrelser, paletter, sykling, z-plan, objektenes plass og tilstander, og kostyme-ID for hver COST-blokk. Selve bildene (SMAP og COST) dekodes ikke ennå.
- Kostyme-ID er katalogens ID, ikke rekkefølgen i filen (lærdom fra The Dig).
- Tellingene fra uttrekket skal sjekkes mot spillfilene.

## 5. HD-bakgrunner

**Oppløsning:** 4x, altså 1280 x 800 for et rom på 320 x 200. Originalen vises på en 4:3-skjerm, så pikslene er litt høye. ScummVM strekker bildet når det vises. Maler vi i 4x og lar strekkingen skje til slutt, blir alle koordinater nøyaktig 4 ganger originalen.

**Fallgruver:**

1. **Objekter må passe på bakgrunnen.** Dører, lys og ting er egne objektbilder som tegnes oppå rommet. Males de hver for seg, får de andre detaljer. I The Dig ble små objekter derfor malt på plass i HD-rommet (lagjobber) og klippet ut.
2. **Palettbytte og toning.** Motoren i The Dig justerer HD-pikselen med forholdet mellom fargen spillet viser og originalfargen. Hvor mange rom i Sam & Max som bytter palett, er ikke målt.
3. **Fargesykling.** Motoren i The Dig viser syklede områder i HD gjennom et glatt fargekart. Hvilke rom i Sam & Max som sykler farger, er ikke målt.
4. **Z-planer** skaleres med nærmeste nabo, nøyaktig 4x, aldri med utjevning.
5. **Gangbokser og klikkområder endres ikke.** Spillogikken tror fortsatt at rommet er 320 x 200.

**Oppskalering:** `smhd build-mod` lager en mod med automatisk oppskalering (`nearest`, `lanczos`, `lanczos-sharp`, `realesrgan`), så alt finnes i HD fra første dag. Det krever uttrekket. Den ferdige grafikken males av ChatGPT/Codex etter stilpiloten.

## 6. HD-figurer

- Kostymene er klassiske (COST) og tegnes av `ClassicCostumeRenderer` i `costume.cpp`, ikke av AKOS som i The Dig. Antall ruter er ikke målt.
- Figurene som er kjent: Sam (hunden i dress og hatt) og Max (den hvite, kaninaktige figuren). Andre figurer er ikke kartlagt.
- **Stil:** glatt stil med ekte alfa fra starten. I The Dig avviste Tom figurer klippet med originalens omriss, fordi de fikk trappetrinn i 4x.
- **Animasjon:** rutene i én animasjon males på samme ark, så figuren ikke flimrer. Ankerpunkter og timing beholdes fra kostymet. HD-ruten erstatter bare pikslene.
- **Størrelse:** i The Dig tegnet grafikerne hodene omtrent 35 prosent større enn kroppene. Mottaket skalerer derfor hver gruppe ruter til originalens høyde og plasserer etter best overlapp (`myk.py`).
- **Farger:** spillet kan endre farger på figurer (skygger, mørke rom). Motoren justerer HD-figuren etter fargen spillet viser.

## 7. Mellomsekvenser og minispill

- Det er ingen SMUSH-filmer, og ingen filmrammer å skalere. Ifølge skillen tegnes mellomsekvensene og minispillene av motoren, altså med det samme som resten av spillet: rom, objekter, kostymer, tekst og blast-objekter. Ikke sjekket i spillet.
- Hvilke rom og skript som står for dem, er ikke kartlagt.
- En kommentar i ScummVM (`script_v6.cpp`, `o6_setBlastObjectWindow`) sier at Sam & Max bruker den opkoden bare i starten av minispillet på motorveien. Det tyder på at minispillet bruker blast-objekter. Ikke sjekket.

## 8. Motoren

Patchen er den samme som i The Dig, og den er ikke aktiv for Sam & Max ennå: `DigHD::create` slår seg bare på for `GID_DIG`. Hva som må portes, står i [HD-MOTOR.md](HD-MOTOR.md).

**Bygget og startet 10. oktober:** `engine/build.sh` bygde ScummVM ved `c9091321` med patchen her (Ubuntu 24.04, SDL 2.30). Spillet ble startet fra `game/` uten skjerm (`SDL_VIDEODRIVER=dummy`) og kjørte i 25 sekunder til det ble stoppet: ScummVM kjente igjen `samnmax`, CD, SCUMM 6 og MD5-en, leste alle katalogene i indeksen, skriptene la objekt 35 fra rom 1 i inventaret, og iMUSE startet musikken (AdLib, fordi MIDI-utgangen ikke finnes her). Ingen feil. Bildet er ikke sett, fordi det ikke er skjerm og DigHD (som har bildedump) ikke er på for Sam & Max.

**Stedene i ScummVM som gjelder Sam & Max** (sjekket i kildekoden ved `c9091321`):

| Fil | Funksjon | Kroker fra The Dig |
| --- | --- | --- |
| `engines/scumm/gfx.cpp` | `drawStripToScreen`, `markRectAsDirty`, overgangseffekter | Finnes. Felles for alle SCUMM-versjoner |
| `engines/scumm/object.cpp` | `drawObject`, `ScummEngine_v6::drawBlastObject`, `removeBlastObjects` | Finnes. Blast-objektene er v6-kode |
| `engines/scumm/palette.cpp` | `updatePalette`, `initCycl`, `cyclePalette`, `setCurrentPalette` | Paletten går til DigHD fra `updatePalette` |
| `engines/scumm/costume.cpp` | `ClassicCostumeRenderer::drawLimb`, `paintCelByleRLE` | Mangler. Krokene finnes bare i `akos.cpp` |
| `engines/scumm/charset.cpp` | `CharsetRendererClassic` | Mangler. Kroken finnes bare i `CharsetRendererV7::drawCharV7` |
| `engines/scumm/cursor.cpp` | `ScummEngine::updateCursor` | Mangler. Kroken finnes bare i `ScummEngine_v7::updateCursor` |
| `engines/scumm/gfx_gui.cpp` | `ScummEngine_v6::setUpMainMenuControls`, `updateMainMenuControls` | Raden HD Graphics finnes, men bare for `GID_DIG` |

**Filnavn i mod-mappen:** som i The Dig (`rooms/roomNNN.png`, `objects/objNNN_SS.png`, `costumes/costumeCCC_NNN.png`, med `_idx.png` ved siden av). Uttrekk, oppskalering og motor bruker de samme navnene.

## 9. Stilen

Planen er trofast HD: samme motiv, samme former på samme sted og samme farger, bare skarpere og med mer detalj. Sam & Max sitt tegneserieuttrykk beholdes.

Motoren er den samme uansett stil. Før noe bestilles i mengde, lages en stilpilot: ett rom og ett figurark, sett i motoren, med stilankere. Tom godkjenner. Rommet og figuren til piloten er ikke valgt.

## 10. Første steg

1. Spillfilene til `game/` med `tools/hent_spilldata.sh`. Gjort og testet 10. oktober.
2. Bygg ScummVM ved `c9091321` med patchen (`engine/build.sh`), og start spillet uendret fra `game/` uten skjerm. Gjort 10. oktober (se 8).
3. Mål rom, objekter og kostymer, og lag romlisten. Gjort 10. oktober for det indeksen og blokkene sier; det under Ikke målt ennå gjenstår.
4. Velg vei for uttrekket: dump-modus i motoren eller egne dekodere.
5. Port DigHD til v6 etter [HD-MOTOR.md](HD-MOTOR.md): slå den på for `GID_SAMNMAX`, ta rom og objekter først, og test med en `nearest`-mod (0 avvik mot originalen). Deretter figurer, tekst, farger og sykling, blast-objekter, menyen og pekeren.
6. `smhd build-mod` med automatisk oppskalering.
7. Stilpilot med Tom.
8. Spillbart for Tom: `./spill.sh`, nettsiden (eget repo) og Linux-pakken.

## Kilder

- ScummVM, SCUMM-motoren: https://github.com/scummvm/scummvm/tree/master/engines/scumm
- ScummVM deteksjonstabell: https://github.com/scummvm/scummvm/blob/master/engines/scumm/scumm-md5.h
- scummvm-tools (descumm): https://github.com/scummvm/scummvm-tools
- The Dig HD Remake, referansen: https://github.com/Tombonator3000/Dig-HD-Remake
