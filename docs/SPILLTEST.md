# Spilltest

Slik skal Tom spille og teste HD-versjonen rett fra repoet, og hva han bør se etter. Oppsettet er kopiert fra The Dig HD Remake.

## Status

HD-motoren er på for Sam & Max (rom, objekter, blast-objekter og figurer), men det finnes ingen ferdig HD-grafikk ennå. `./spill.sh --auto` gir automatisk oppskalering å se på.

| Del | Status |
| --- | --- |
| Spillfilene til `game/` med `tools/hent_spilldata.sh` | Virker. Testet fra en fersk klone 10. oktober |
| HD-grafikk | Motoren bruker HD-bilder for rom, objekter, blast-objekter og figurer. Teksten er originalpiksler. Grenen `hd-mod` har ingen mod ennå |
| `./spill.sh` | Tilpasset. Testet her 10. oktober uten skjerm: hentet `hd-mod` (tom), bygget motoren og startet Sam & Max uten mod. Uten skjerm trengs `--programvare`, ellers finner OpenGL ingen grafikkmodus. Ikke testet med skjerm |
| `engine/run.sh` | Tilpasset (`engine/run.sh ingen` starter uten mod). Brukt av `spill.sh` i testen over |
| `engine/test.sh`, `tools/romtest.sh` | Tilpasset filnavn og spill-ID, men kan ikke brukes før DigHD er portet |
| `./spill.sh --auto` | Lager modden med automatisk oppskalering og starter med den. Ikke kjørt med skjerm |
| Nettsiden | Repoet `Tombonator3000/Sam-Max-HD-Web` finnes ikke. Se [PAGES.md](PAGES.md) |
| Linux-pakken | `tools/pakke_linux.sh` tilpasset. AppDir laget og startet uten skjerm her 10. oktober (uten HD-mod). AppImage og arbeidsflyten er ikke kjørt |
| ScummVM med patchen og Sam & Max | Bygget og testet uten skjerm 10. oktober med nearest-mod og romtest, se [HD-MOTOR.md](HD-MOTOR.md). Ikke testet med skjerm, mus og lyd |

Resten av dokumentet beskriver hvordan det skal virke når delene over er på plass.

## Første gang

Linux. Installer det motoren trenger:

```sh
sudo apt install build-essential git pkg-config libsdl2-dev libpng-dev zlib1g-dev     # Ubuntu/Debian
sudo dnf install gcc-c++ make git pkgconf SDL2-devel libpng-devel zlib-devel          # Fedora
```

Hent repoet og spillfilene:

```sh
git clone https://github.com/Tombonator3000/Sam-Max-HD.git
cd Sam-Max-HD
tools/hent_spilldata.sh
```

`tools/hent_spilldata.sh` henter grenen `spilldata` til `game/`, setter sammen talen (`MONSTER.SOU` ligger i to deler fordi GitHub ikke tar filer over 100 MB) og sjekker sjekksummene. Etterpå ligger `SAMNMAX.000`, `SAMNMAX.001`, `MONSTER.SOU` og de to MT-32-ROM-filene i `game/`.

Når `spill.sh` er tilpasset, skal `./spill.sh` gjøre alt: hente spillfilene og siste HD-mod (grenen `hd-mod`) første gang, bygge motoren og starte spillet. Senere skal den starte med en gang og bare hente ny HD-mod og bygge motoren på nytt når den er endret.

Musikk: musikken er MIDI (iMUSE) inne i `SAMNMAX.001`. `engine/build.sh` bygger motoren med `--disable-mt32emu`, så MT-32-ROM-filene brukes ikke nå. Om og hvordan musikken høres, er ikke testet.

## Valg

Fra The Dig. Valgene som styrer HD (`--rom`, `--klassisk`, `--gult`) virker først når patchen er portet.

| Kommando | Hva |
| --- | --- |
| `./spill.sh` | Vanlig start med HD-modden |
| `./spill.sh --rom N` | Hopper til rom N like etter starten, for å se på ett rom. Spillet er ikke i normal tilstand etter et hopp, så bruk det til å se, ikke til å spille videre |
| `./spill.sh --klassisk` | Starter med originalgrafikken |
| `./spill.sh --gult` | Farger gult der HD mangler |
| `./spill.sh --auto` | Fyller rom og objekter som ikke har HD fra ChatGPT, med automatisk oppskalering. Krever Python 3.12 og uttrekket |
| `./spill.sh --fort` | Starter uten å hente eller bygge noe |
| `./spill.sh --fullskjerm` | Fullskjerm |
| `./spill.sh --programvare` | Uten OpenGL. Bruk den hvis spillet ikke starter og terminalen sier "Could not load any graphics mode" |
| `./spill.sh --nettleser` | I nettleseren på http://localhost:8000, bare på denne maskinen |
| `git pull && ./spill.sh` | Siste versjon av koden og modden |

Andre valg sendes videre til ScummVM.

## Taster i spillet

| Tast | Hva |
| --- | --- |
| Ctrl+H | Bytter mellom HD og originalgrafikken (når patchen er portet) |
| Ctrl+Shift+H | Gult felt der HD mangler, av og på (når patchen er portet) |
| Alt+S | Skjermbilde (lagres i mappen ScummVM skriver ut i terminalen) |
| F5 | Spillets meny (lagre, laste, avslutte). Raden HD Graphics kommer når patchen er portet |
| Ctrl+F5 | ScummVM-menyen |

## Hva du bør se etter

Når det finnes HD-grafikk:

1. Rom med HD-bakgrunn: bytt med Ctrl+H og se at alt står på samme sted.
2. Sam og Max går bak ting i forgrunnen der de skal, og kanter og dører ligger der de lå.
3. Objekter som bytter bilde (dører som åpnes, ting som tas), bytter riktig.
4. Replikker og menyer: teksten er glatt og står der den står i originalen. Ingen tekst blir stående igjen.
5. Menyen (F5) og bannere over en figur: ingen figur skal skinne gjennom boksen.
6. Mellomsekvenser og minispill: de tegnes av motoren, ikke som filmer, og skal vises riktig med HD.
7. Gå mellom rom med og uten HD, og se at spillet ikke krasjer eller blinker.
8. Ctrl+Shift+H: det gule skal vise nøyaktig det som mangler HD. Tekst og pekeren skal ikke bli gul.

Hvilke rom som er best å se på, står i `STATUS.md` når de første HD-rommene finnes.

## Utviklermodus: hopp til et område

- Windows: start «Sam og Max HD - utvikler.bat» i pakken. Velg 1 for å hoppe til et rom (romlisten står i `rom-liste.txt`), 2 for å laste et lagret spill, 3 for vanlig start i vindu.
- Linux og repoet: `./spill.sh --rom 22` hopper til rom 22. `./spill.sh --save-slot=3` laster lagret spill 3 (valget går rett til ScummVM).
- Hoppet setter ikke spillet i vanlig tilstand: figurer kan mangle, og noen rom henger fordi skriptene mangler variabler. Et lagret spill fra en ekte gjennomspilling er riktig tilstand.
- Lagre i hvert nytt område mens du spiller (F5, Save), med romnavnet i beskrivelsen. Lagrede spill ligger i `%APPDATA%\SamMaxHD\saves` (Windows). Send mappen til Claude, så kjører romtesten alle områdene fra dem: `tools/romtest.py --lagret MAPPE`.
- ScummVM sin konsoll (Ctrl+Alt+D) har kommandoer som `room N`, men den hopper på samme måte som testhoppet.

## Uten skjerm: alle rom

Krever at patchen er portet, og at `tools/romtest.py` starter Sam & Max. Ikke kjørt med Sam & Max.

```sh
tools/romtest.sh                     # alle rom med mods/gpt
tools/romtest.sh --rom 1,2,3         # noen rom (--rom 10-20 for et område)
tools/romtest.sh --mod test-nearest  # en annen mod
tools/romtest.sh --kamera ett        # bare der spillet selv setter kameraet
tools/romtest.sh --objekter          # i tillegg alle tilstandene til alle objektene i hvert rom
tools/romtest.sh --bare-rapport      # rapport og ark på nytt fra kjøringene som finnes
```

Skriptet kjører motoren uten skjerm (SDL dummy) én gang per rom og hopper til rommet med `DIGHD_TEST_ROOM`. I rom som er bredere eller høyere enn skjermen, kjører det i tillegg med kameraet satt (`DIGHD_TEST_CAMX` og `DIGHD_TEST_CAMY`), så hele rommet blir vist. Skjermen lagres i HD og med originalpikslene. Motoren er `$SCUMMVM_SRC/scummvm` eller `engine/scummvm/scummvm` (`--motor` for en annen).

For hver kjøring samles: om rommet ble lastet, om motoren krasjet eller hang, om HD-bakgrunnen ble lastet og brukt, andelen piksler fra HD-bakgrunn, HD-objekt, HD-figur og originalen, og avviket fra originalen (`DIGHD_VERIFY`). Bildene sammenlignes også i skriptet: forskyvning, svarte felt der originalen ikke er svart, og de største avvikene, med nærbilder. Sømmene mellom HD-objekter og HD-rommet måles også.

Resultatet ligger i `work/romtest`: `RAPPORT.md`, `romtest.csv`, `somer.csv`, kontaktark `ark_NN.png` med HD og originalen side om side, en mappe per kjøring med logg og bilder, og `naerbilder/`. Notater fra gjennomsynet kan skrives i `work/romtest/FUNN.md` og kommer med i rapporten neste gang.

Hoppet setter ikke spillet i vanlig tilstand. Figurer og objekter kan mangle eller stå et annet sted enn i vanlig spill, og noen rom starter en mellomsekvens eller bytter rom selv. Testen fanger krasj, rom som ikke lastes, rom der HD-bakgrunnen ikke brukes og tydelige feil i bildet, ikke feil som bare viser seg i vanlig spill.

### Objekttilstander

Etter hoppet står hvert objekt i tilstanden skriptene ga det, så HD-bildene for de andre tilstandene blir ikke prøvd i den vanlige kjøringen. Med `--objekter` kjøres hvert rom som har objekter, én gang til med `DIGHD_TEST_OBJSTATE=alle`. Motoren setter hvert objekt i hver tilstand slik skriptene gjør det og lagrer skjermen. Rapporten har status, HD-andel og nærbilde per objekt og tilstand (`objekter.csv`).

Et objekt som et annet objekt dekker, kan testes for seg med en liste, der det som dekker får tilstand 0. Når motoren er tilpasset, blir kommandoen slik (R er rommet, A og B er objektnumre):

```sh
mkdir -p /tmp/dump
DIGHD_MOD="$PWD/mods/gpt" DIGHD_TEST_ROOM=R DIGHD_TEST_OBJSTATE=A:0,B:2 \
  DIGHD_DUMP_DIR=/tmp/dump DIGHD_DUMP_FLAT=1 DIGHD_QUIT_AT=400 \
  engine/scummvm/scummvm --path="$PWD/game" --debuglevel=1 samnmax 2>&1 | grep "DigHD: test"
```

## I nettleseren, på denne maskinen

```sh
./spill.sh --nettleser
```

Skriptet skal hente spillfilene og siste HD-mod, bygge ScummVM med HD-patchen for nettleseren (WebAssembly med Emscripten) og starte en webserver på maskinen. Åpne adressen det skriver ut, vanligvis http://localhost:8000. Ctrl+C i terminalen stopper serveren. `engine/run-web.sh` og `engine/web/` er kopiert fra The Dig. Ikke testet med Sam & Max.

**Bare lokalt.** Spillet og HD-grafikken tilhører Disney/Lucasfilm. Denne løsningen skal bare kjøres på egen maskin:

- webserveren (`engine/web/server.py`) lytter bare på 127.0.0.1 og svarer bare på forespørsler til localhost,
- siden (`engine/web/index.html`) nekter å starte hvis den er åpnet fra en annen adresse enn localhost,
- alt som serveres, ligger i `work/nettleser`, og byggefilene i `engine/emsdk` og `engine/scummvm-web`. Alle tre er ignorert av git.

Krav: git, make, python3, pkg-config, xz og zip, og en nyere Chrome, Edge eller Firefox.

```sh
sudo apt install git make python3 pkg-config xz-utils zip     # Ubuntu/Debian
sudo dnf install git make python3 pkgconf xz zip              # Fedora
```

Første gang installeres Emscripten 4.0.10 i `engine/emsdk` (omtrent 350 MB), og ScummVM hentes til `engine/scummvm-web`. Motoren bygges på nytt når patchen, ScummVM-versjonen eller `engine/build-web.sh` er endret.

| Kommando | Adresse | Hva |
| --- | --- | --- |
| `./spill.sh --nettleser` | http://localhost:8000/ | Vanlig start med HD-modden |
| `./spill.sh --nettleser --rom N` | http://localhost:8000/?rom=N | Hopper til rom N |
| `./spill.sh --nettleser --klassisk` | http://localhost:8000/?klassisk=1 | Starter med originalgrafikken |
| `./spill.sh --nettleser --gult` | http://localhost:8000/?gult=1 | Gult felt der HD mangler |
| `./spill.sh --nettleser --auto` | http://localhost:8000/?mod=auto | Med automatisk oppskalering for resten |
| `./spill.sh --nettleser --fort` | | Starter uten å hente eller bygge noe |
| `./spill.sh --nettleser --port 8001` | http://localhost:8001/ | En annen port, hvis 8000 er i bruk |

Tastene er de samme som ellers. Siden stopper nettleserens egne snarveier for F1 til F10 og for Ctrl og Alt med en bokstav, så F5 åpner spillmenyen i stedet for å laste siden på nytt. F11 gir fullskjerm.

Lagring: lagrede spill og innstillingene ligger i nettleseren (IndexedDB for localhost og porten), ikke i repoet.

## Fra GitHub Pages

Planen er en nettside som går rett inn i spillet, på PC og mobil, og henter spillet og HD-grafikken fra grenene `spilldata` og `hd-mod` med en lesenøkkel. Nettsiderepoet `Tombonator3000/Sam-Max-HD-Web` finnes ikke ennå. Se [PAGES.md](PAGES.md).

## Linux: én fil med alt

Planen er som for The Dig: én AppImage med ScummVM med HD-patchen, spillet, talen og HD-grafikken, under Releases i dette repoet. Spillet skal starte rett, i fullskjerm, og F5 skal åpne menyen med HD Graphics.

`tools/pakke_linux.sh` og `.github/workflows/linux.yml` er tilpasset Sam & Max. AppDir-mappen er laget og startet uten skjerm her (originalspillet, uten HD-mod). Selve AppImage-filen lages bare i arbeidsflyten Linux-pakke, som ikke er kjørt ennå. Den startes for hånd eller kjører om natten når `hd-mod` er endret.

## Si fra

Skriv hva du så, i hvilket rom og omtrent hvor, og legg ved skjermbilde (Alt+S) hvis du kan. Gi det til Claude i chatten, eller legg det i `rapporter/` i grenen `gpt-arbeid`.
