# Sam & Max HD Remake: analyse av filer, omfang og veien videre

Skrevet 10. oktober 2026. Grunnlaget er spillfilene i grenen `spilldata`, indeksen `SAMNMAX.000` lest etter XOR, og kildekoden til ScummVM ved commit `c9091321` (`engine/SCUMMVM_COMMIT`). Oppbyggingen følger analysen i The Dig HD Remake. Det som ikke er målt ennå, står som "Ikke målt ennå", med hva som skal måles.

## Kort fortalt

- Spillfilene er den engelske CD-utgaven av *Sam & Max Hit the Road* (LucasArts 1993). MD5 for `SAMNMAX.000` stemmer med ScummVM sin oppføring for `samnmax`, CD, engelsk.
- Spillet er SCUMM v6. `SAMNMAX.000` og `SAMNMAX.001` er kryptert med XOR 0x69. Indeksen og blokkstrukturen i `SAMNMAX.001` er lest med `smhd info` (`pipeline/smhd/gamedata.py`).
- Dekompilering trengs ikke. ScummVM kjører spillet (`samnmax`), og skriptene kan leses med descumm. Arbeidet er HD-grafikken og å porte HD-patchen fra SCUMM v7 til v6.
- 85 rom (36 brede som ruller, ingen høye), 63 med z-plan, 2 med flere paletter, 43 med fargesykling. 959 objektbilder fordelt på 715 objekter (103 av dem er blast-objekter med BOMP). 348 kostymer med 16 052 ruter som animasjonene bruker. Alt er trukket ut med `smhd extract`, og alle 1181 skript er dekompilert med descumm.
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
| Kostymer og ruter | Største rute, og hvilke animasjoner skriptene faktisk bruker |
| Tegnsett | Hvilke tegnsett som brukes hvor (dialog, meny, bannere), med størrelse og antall farger |
| Lokale skript | Lokale skript og inn- og utgangsskript per rom (LSCR, ENCD, EXCD) |
| Mellomsekvenser og minispill | Hvilke skript som står for dem (rommene er kjent, se 11) |

## 4. Dekompilering

Spillets exe-fil trenger ikke dekompileres. ScummVM har SCUMM v6-motoren (`ScummEngine_v6`), og spillet kjører der som `samnmax`. Det som trengs, er skriptene og grafikken. Begge er tatt ut 10. oktober.

### Skriptene

`tools/bygg_descumm.sh` bygger descumm fra scummvm-tools (låst til commit `8665aa1d`, bare fem kildefiler, ingen biblioteker). `tools/dekompiler_skript.py` leser skriptblokkene og dekompilerer dem til `work/skript/` (åpne `OVERSIKT.md` først). Det tar et par sekunder.

| Sort | Skript | Uten feil | Feilet |
| --- | ---: | ---: | ---: |
| Globale skript (SCRP) | 120 | 120 | 0 |
| Lokale skript (LSCR) | 564 | 562 | 2 |
| Inngangsskript (ENCD) | 85 | 85 | 0 |
| Utgangsskript (EXCD) | 85 | 85 | 0 |
| Objektskript (VERB med kode) | 327 | 327 | 0 |
| Sum | 1181 | 1179 | 2 |

- De to som feilet (lokalt skript 210 i rom 66 og 206 i rom 78) stopper på opkoden 0xBD nesten til slutt. ScummVM kjører 0xBD som `o6_dummy` i v6; descumm kjenner den bare i HE-spill. Alt før står i filene.
- 623 av 950 objekter har tom verbtabell og ingen kode. Globalt skript 8 og 9 peker på samme blokk.
- Kontrollert: alle 3368 talereplikker (`sound(offset, 0xA)`) peker på en VCTL-blokk i MONSTER.SOU, alle kall til globale skript og 921 kall til lokale skript peker på skript som finnes, og i alle 78 `loadRoomWithEgo` ligger objektet i rommet.
- Første skript har versjonsteksten "Sam & Max Hit the Road, CD1.11, 3-24-94".

### Grafikken

`smhd extract` tar ut all originalgrafikken til `work/extract` på omtrent halvannet minutt, i samme format som uttrekket for The Dig (`rooms.json`, `costumes.json`, `roomNNN.png`, `objNNN_SS.png`, `costumeCCC_NNN.png`, alle med `_idx.png`). Dekoderne står i `pipeline/smhd/v6grafikk.py` og er oversatt fra ScummVM ved `c9091321`:

- **Rom og objekter (SMAP):** `Gdi::decompressBitmap` med kodekene Sam & Max bruker: rå (1), BasicV (15 til 18, 34 til 38), BasicH (25 til 28, 48) og MajMin (104 til 108, 124 til 128). Gjennomsiktig farge fra TRNS (5 i 83 rom).
- **Blast-objekter (BOMP):** 103 objektbilder, `bompDecodeLine`, fargen 255 er gjennomsiktig.
- **Kostymer (COST):** `ClassicCostumeLoader` og `byleRLEDecode`. Format 0x58 (53 kostymer, 16 farger), 0x59 (39, 32 farger), 0x60 (79) og 0x61 (177). Formatene 0x60 og 0x61 kan peke på bildet til en annen rute. Ruter som animasjonene bruker, tas ut. Rutenummeret er lag * 128 + kode, så motoren kan regne det ut i `drawLimb`.

| Hva | Tatt ut |
| --- | --- |
| Rombakgrunner | 83 (rom 81 og 82 har bredde 0 og ingen bakgrunn) |
| Objektbilder | 959 (856 SMAP og 103 BOMP), 0 feil |
| Kostymeruter | 16 052 fra 348 kostymer. 17 ruter har bredde eller høyde 0 og får ikke noe bilde. 4789 ruter bruker samme bilde som en annen rute (`samme_bilde_som` i costumes.json) |

**Farger i kostymene:** kostymepaletten peker på indekser i rompaletten. Bare indeksene 0 til 15 er like i alle rom; Sam og Max bruker 234 til 255, som er like i 75 til 79 av 85 rom. RGBA-bildene har fargene fra rommet kostymet ligger i (palett 0), eller fra rommet i `docs/kostymefarger.csv` når kostymet vises et annet sted (se 11). Magentaen i noen kostymer er palettindeks 13, som `ClassicCostumeRenderer` tegner gjennom skyggetabellen (`base-costume.cpp`, `pcolor == 13`): det er skygger, ikke farger. Indeksbildene har de riktige indeksene uansett.

**Kontrollert:** alle rom og ett bilde fra hvert kostyme er sett på i kontaktark, og rom 2 med alle objektene lagt på plass etter CDHD stemmer med spillet. Sam (kostyme 2) og Max (kostyme 3) har riktige farger. Ikke sammenlignet piksel for piksel med motoren, fordi DigHD (som kan lagre skjermbilder) ikke er på for Sam & Max ennå. `smhd build-mod` lager en mod av uttrekket (testet med automatisk oppskalering: 83 rom, 950 objektbilder; de 9 objektbildene i rom 81 og 82 tas ikke med, fordi rommene ikke har bakgrunn).

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

- Kostymene er klassiske (COST) og tegnes av `ClassicCostumeRenderer` i `costume.cpp`, ikke av AKOS som i The Dig. 348 kostymer, 16 052 ruter (se 4). Animasjonene per kostyme, lag og retning står i `costumes.json` i samme form som for The Dig.
- Alle 348 kostymene har navn eller beskrivelse i `docs/figurer.csv` (13. oktober, se 11). Sam er kostyme 2, 4, 7 og flere; Max er 3, 5, 6 og flere.
- **Stil:** glatt stil med ekte alfa fra starten. I The Dig avviste Tom figurer klippet med originalens omriss, fordi de fikk trappetrinn i 4x.
- **Animasjon:** rutene i én animasjon males på samme ark, så figuren ikke flimrer. Ankerpunkter og timing beholdes fra kostymet. HD-ruten erstatter bare pikslene.
- **Størrelse:** i The Dig tegnet grafikerne hodene omtrent 35 prosent større enn kroppene. Mottaket skalerer derfor hver gruppe ruter til originalens høyde og plasserer etter best overlapp (`myk.py`).
- **Farger:** spillet kan endre farger på figurer (skygger, mørke rom). Motoren justerer HD-figuren etter fargen spillet viser.

## 7. Mellomsekvenser og minispill

- Det er ingen SMUSH-filmer, og ingen filmrammer å skalere. Ifølge skillen tegnes mellomsekvensene og minispillene av motoren, altså med det samme som resten av spillet: rom, objekter, kostymer, tekst og blast-objekter. Ikke sjekket i spillet.
- Hvilke rom og skript som står for dem, er ikke kartlagt.
- En kommentar i ScummVM (`script_v6.cpp`, `o6_setBlastObjectWindow`) sier at Sam & Max bruker den opkoden bare i starten av minispillet på motorveien. Det tyder på at minispillet bruker blast-objekter. Ikke sjekket.

## 8. Motoren

Patchen er The Dig sin, utvidet for Sam & Max 10. oktober: rom, objekter, blast-objekter og kostymer får HD; teksten og menyraden er ikke portet. Detaljer og tester i [HD-MOTOR.md](HD-MOTOR.md).

**Bygget og startet 10. oktober:** `engine/build.sh` bygde ScummVM ved `c9091321` med patchen her (Ubuntu 24.04, SDL 2.30). Spillet ble startet fra `game/` uten skjerm (`SDL_VIDEODRIVER=dummy`) og kjørte i 25 sekunder til det ble stoppet: ScummVM kjente igjen `samnmax`, CD, SCUMM 6 og MD5-en, leste alle katalogene i indeksen, skriptene la objekt 35 fra rom 1 i inventaret, og iMUSE startet musikken (AdLib, fordi MIDI-utgangen ikke finnes her). Ingen feil. Bildet er ikke sett, fordi det ikke er skjerm og DigHD (som har bildedump) ikke er på for Sam & Max.

**Stedene i ScummVM som gjelder Sam & Max** (sjekket i kildekoden ved `c9091321`):

| Fil | Funksjon | Kroker fra The Dig |
| --- | --- | --- |
| `engines/scumm/gfx.cpp` | `drawStripToScreen`, `markRectAsDirty`, overgangseffekter | Finnes. Felles for alle SCUMM-versjoner |
| `engines/scumm/object.cpp` | `drawObject`, `ScummEngine_v6::drawBlastObject`, `removeBlastObjects` | Finnes. Blast-objektene er v6-kode |
| `engines/scumm/palette.cpp` | `updatePalette`, `initCycl`, `cyclePalette`, `setCurrentPalette` | Paletten går til DigHD fra `updatePalette` |
| `engines/scumm/costume.cpp` | `ClassicCostumeRenderer::drawLimb`, `paintCelByleRLE` | Lagt til 10. oktober |
| `engines/scumm/charset.cpp` | `CharsetRendererClassic` | Mangler. Kroken finnes bare i `CharsetRendererV7::drawCharV7` |
| `engines/scumm/cursor.cpp` | `ScummEngine::updateCursor` | Lagt til 10. oktober |
| `engines/scumm/gfx_gui.cpp` | `ScummEngine_v6::setUpMainMenuControls`, `updateMainMenuControls` | Raden HD Graphics finnes, men bare for `GID_DIG` |

**Filnavn i mod-mappen:** som i The Dig (`rooms/roomNNN.png`, `objects/objNNN_SS.png`, `costumes/costumeCCC_NNN.png`, med `_idx.png` ved siden av). Uttrekk, oppskalering og motor bruker de samme navnene.

## 9. Stilen

Planen er trofast HD: samme motiv, samme former på samme sted og samme farger, bare skarpere og med mer detalj. Sam & Max sitt tegneserieuttrykk beholdes.

Motoren er den samme uansett stil. Før noe bestilles i mengde, lages en stilpilot, sett i motoren, med stilankere. Tom godkjenner. Piloten er valgt 13. oktober: hovedark for Sam og Max, kontoret (rom 7, to deler) og det første figurarket for Sam (kostyme 2) og Max (kostyme 3).

## 10. Første steg

1. Spillfilene til `game/` med `tools/hent_spilldata.sh`. Gjort og testet 10. oktober.
2. Bygg ScummVM ved `c9091321` med patchen (`engine/build.sh`), og start spillet uendret fra `game/` uten skjerm. Gjort 10. oktober (se 8).
3. Mål rom, objekter og kostymer, og lag romlisten. Gjort 10. oktober for det indeksen og blokkene sier; det under Ikke målt ennå gjenstår.
4. Uttrekket med egne dekodere (`smhd extract`). Gjort 10. oktober (se 4).
5. Port DigHD til v6 etter [HD-MOTOR.md](HD-MOTOR.md): slå den på for `GID_SAMNMAX`, ta rom og objekter først, og test med en `nearest`-mod (0 avvik mot originalen). Deretter figurer, tekst, farger og sykling, blast-objekter, menyen og pekeren.
6. `smhd build-mod` med automatisk oppskalering.
7. Stilpilot med Tom.
8. Spillbart for Tom: `./spill.sh`, nettsiden (eget repo) og Linux-pakken.

## 11. Klargjøring av grafikken (13. oktober 2026)

Tom ba om at all grafikken klargjøres så ChatGPT kan male den i HD: samme størrelse i alle figurarkene, ingen oppdiktede eller endrede objekter, og trofast mot originalen. Det som ble funnet og avgjort før jobbene ble laget:

**Romnavn.** RNAM er tom. Alle 85 rom har fått navn i `docs/rom-oversikt.csv`, fra gjennomsyn av rommene og de interne objektnavnene i skriptene (for eksempel `office-dart-board`, `carny-kushman-sign`, `escher-mirror`).

**Rom uten egen bakgrunn.** Ni rom er lagerrom for bilder spillet tegner andre steder: rom 1 (LucasArts-logoen), 67 og 77 (rulletekst), 69 (Highway Surfing: politibilene, veiskiltene med vitser, start- og mållinje, horisont), 78 (landskapsbitene i kikkerten), 80 og 82 (slangene i hyssingnøstet), 81 (ringen under forstørrelsesglasset), 93 (pekerne for handlingene) og 94 (inventaresken, samtaleikonene og inventaret). De store bildene der blir objektjobber, de små havner på ikonark.

**Ikonarkene.** Rutenettet fra The Dig (én rute på størrelse med det største ikonet) ga 82 nesten tomme ark for Sam & Max. Nå pakkes ikonene tett i rader, rom for rom, med tilstandene til et ikon etter hverandre og en flat bakgrunnsfarge som ikke finnes i ikonene: 9 ark med 163 bilder.

**Paletter.** `tools/kostymer.py` leser skriptene og finner rommene der hvert kostyme settes på en skuespiller eller lastes (345 av 348 har fast nummer i skriptene), og velger paletten flertallet av de rommene har. Åtte kostymer får en annen palett enn hjemrommet sitt (`docs/kostymefarger.csv`, tatt i bruk av `smhd extract`):

| Kostyme | Ligger i | Vises med | Hvorfor |
| --- | --- | --- | --- |
| 2, 4, 7 (Sam) | rom 1 | rom 7 | Indeks 250 er oransje i rom 1, men krem (255, 247, 199) i 75 av 85 rom |
| 104, 106, 107, 108 | rom 23 | rom 76 | Settes bare i rom 76; 5 til 22 farger er ulike |
| 334 (tre) | rom 86 | rom 88 | Settes 7 ganger i rom 88; 10 farger er ulike |

Motoren toner HD-pikselen etter paletten i indeksbildet (`basePal` i patchen), så riktig palett i uttrekket gir riktige farger også når spillet viser andre.

**Skygger.** Palettindeks 13 (255, 87, 255) tegnes gjennom skyggetabellen. Skyggepikslene er tatt bort fra figurarkene, og fem kostymer som bare er skygge (127, 132, 153, 211 og 280), får ingen ark. Kostyme 95 og 194 har en hvit og en svart form i tillegg og får ark for den.

**Feil i dataene.** Seks ruter i kostyme 62, 133, 331 og 346 er 4163 til 6189 piksler brede eller 4924 til 5257 høye. De kommer fra animasjoner som peker utenfor kostymet (advarslene i `costumes.json`), og dekoderen leser tilfeldige data som ruter. Ruter større enn 640 x 400 tas ikke med på arkene (`figur.MAX_CEL`); ekte ruter er høyst 320 x 200.

**Lag og speilvending.** I klassiske kostymer er kroppen oftest lag 1 (i The Dig lag 0), og munn og hode er egne lag. En animasjon endrer bare lagene den har; de andre beholder ruten fra startanimasjonen. Mot venstre tegner `ClassicCostumeRenderer` rutene mot høyre speilvendt når kostymet ikke har eget speilflagg (`_drawActorToRight` i `costume.cpp`). Promptene sier derfor at arkene ikke har ruter mot venstre, og hovedarkene settes sammen av start- og ståanimasjonen.

**Hvem er hvem.** Navnene er hentet fra replikkene i skriptene og koblet til kostymet skuespilleren har i samme skript: Shep og Burl Kushman (78, «Hi. I'm Shep Kushman, and this is my brother Burl.»), Shuv-Oohl (201 og 202), Doug the Mole Man (102), Trixie (80, 229, 240, 241; «Goodbye, everyone!»), Bruno (228, 237 til 239, 242), Conroy Bumpus (68, 125, 130, 231 til 234, 244) og Conroys håndlanger (69, 129, 245, 293). Det som er tolket og ikke bekreftet, står med «trolig» i `docs/figurer.csv` (for eksempel kvinnen med lang ringhals i rom 23). Hver rad har en engelsk beskrivelse (`prompt_en`) som går inn i prompten, og kolonnen `hovedark` sier hvilke kostymer som får hovedarket til Sam eller Max som bilde to.

**Sett i motoren.** Rom 67, 77, 83 og 92 ble kjørt uten skjerm med testhoppet og bildedump (13. oktober). Alkoven (rom 92) viser Sam i brun dress og Max i ferskenfarge i varmt rødt lys, slik uttrekket har dem; derfor får kostyme 341 til 347 ikke hovedarket som bilde to. Rom 77 viser rulleteksten i rødt på en mørk vei og tittelen (kostyme 328). Rulletekstpanelene i rom 67 og 77 kom ikke på skjermen i løpet av de 900 bildene; fargene deres er ikke sett i spillet.

**Jobbene** (`smhd gpt-pakke --figurer alle`): 2 hovedark, 115 romjobber for 76 rom, 86 objektjobber, 296 lagjobber med 701 objektbilder, 9 ikonark med 163 bilder og 1758 figurark med 15 661 ruter fra 343 kostymer. Ni objektbilder er helt gjennomsiktige og får ingen jobb. Promptene, ordren og egenkontrollen står i [BESTILLING-CHATGPT.md](BESTILLING-CHATGPT.md).

**Minispill og mellomsekvenser** (rommene, fra gjennomsynet): Wak-A-Rat (18, 19), Gator Golf (25), Car Bomb (66), Highway Surfing (68, 69), påkledning (70, 71, 91), den virtuelle verdenen (49, 50), kikkerten (31, 78) og introen (1 til 6). Hvilke skript som styrer dem, er ikke gått gjennom.

## Kilder

- ScummVM, SCUMM-motoren: https://github.com/scummvm/scummvm/tree/master/engines/scumm
- ScummVM deteksjonstabell: https://github.com/scummvm/scummvm/blob/master/engines/scumm/scumm-md5.h
- scummvm-tools (descumm): https://github.com/scummvm/scummvm-tools
- The Dig HD Remake, referansen: https://github.com/Tombonator3000/Dig-HD-Remake
