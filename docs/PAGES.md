# Sam & Max HD på GitHub Pages

Planen er den samme som for The Dig: en nettside som går rett inn i spillet, på PC og mobil, med bare den kompilerte ScummVM-motoren, HD-patchen, brukergrensesnittet, ScummVM sine temaer og tilhørende kildekode. Spillfiler og HD-bilder skal aldri inn i nettsidepakken.

## Status

| Del | Status |
| --- | --- |
| Nettsiderepoet `Tombonator3000/Sam-Max-HD-Web` | Publisert 14. oktober. Testet i Chromium uten skjerm (Playwright, SwiftShader): siden startet uten nøkkel, hentet spillet og HD-modden fra repoet, og viste kontoret med HD (`?DIGHD_TEST_ROOM=7`). Ikke testet på mobil eller med lyd. Arbeidsflyten `.github/workflows/pages.yml` der bygger motoren fra dette repoet og publiserer på https://tombonator3000.github.io/Sam-Max-HD-Web/ |
| Nettsidekoden i `engine/pages` | Tilpasset Sam & Max. Ikke bygget og ikke testet i nettleser |
| Motoren for nettleseren (`engine/build-web.sh`, `engine/build-pages.py`) | Bygges i Actions i web-repoet. I Claude sin sandkasse stopper proxyen nedlastingen av SDL3 fra GitHub-arkivet |
| HD-grafikk | Motoren har HD for rom, objekter og figurer i Sam & Max, men det finnes ingen HD-mod i `hd-mod` ennå |

Alt under beskriver hvordan siden skal virke, etter The Dig sin nettside. Ingenting av det er prøvd med Sam & Max.

`./spill.sh --nettleser` er en egen løsning som kjører nettleserversjonen på localhost fra filene på maskinen (se [SPILLTEST.md](SPILLTEST.md)).

## Lystest (testrom for dynamisk lys)

`lystest/index.html` er et testrom for det valgfrie dynamiske lyset (normalkart og lysmaske, ingen kastede skygger). Arbeidsflyten `.github/workflows/pages.yml` publiserer mappen på https://tombonator3000.github.io/Sam-Max-HD/ når `lystest/` endres i `main`, eller når den startes for hånd.

- Testrommet og testfiguren er egen testgrafikk tegnet i koden. `lystest/` i repoet har bare HTML; arbeidsflyten stopper hvis noe annet havner der.
- Siden starter i kontoret. Publiseringen henter rom 7 (begge delene) og hovedarkene til Sam og Max fra `gpt-arbeid` inn i Pages-pakken (`spill/`), og kjører på nytt hver sjette time så HD-bilder fra piloten kommer med. Det er en offentlig side med grafikk Disney/Lucasfilm eier, etter Toms beslutning 13. oktober 2026 (AGENTS). Åpnet lokalt henter siden grafikken fra `gpt-arbeid` i stedet. Når piloten har levert `resultat.png` for rom 7, brukes HD-bildet; ellers originalen forstørret 4x. Taklampene i kontoret er lyskilder. Figurene tegnes over alt (ingen z-maske), og vinduene står ikke i lysmasken.
- Egne bilder (for eksempel et HD-rom fra stilpiloten, normalkart og lysmaske) kan lastes inn i nettleseren. De leses lokalt og sendes ingen steder.
- Lyset: bordlampe, musepeker og et lys på figuren, hver med farge, styrke, rekkevidde og høyde. Valg for omgivelseslys, relieff, trinnvis lys (ett skyggetrinn og høylys), sammenligning med originalen og visning av normalkart, lysmaske og bare lyset. `L` slår lyset av og på.
- Første gang: Settings > Pages > Source må stå på GitHub Actions.
- Testet 13. oktober 2026 i Chromium uten skjerm (SwiftShader): ingen feil i konsollen, lyset av og på, figuren som går, normalkart, sammenligning, eget bilde med normalkart og mobilbredde 375 px uten sideveis rulling. Ikke prøvd i Firefox, Safari eller på telefon.

## Spille

Siden går rett inn i spillet, som originalen. Det er ingen knapper eller menyer rundt spillet. Grafikkvalget skal ligge i spillets egen meny.

Sam-Max-HD er offentlig, så siden henter spillet (grenen `spilldata`) og HD-pakken (grenen `hd-mod`) uten nøkkel: fillistene fra api.github.com og filene fra raw.githubusercontent.com (14. oktober). Uten nøkkel tillater GitHub 60 API-forespørsler i timen per adresse; siden bruker to per start. Blir grensen nådd, ber siden om en lesenøkkel, som lages på https://github.com/settings/personal-access-tokens/new:

- Repository access: Only select repositories, Sam-Max-HD
- Permissions: Contents, Read-only
- Utløpsdato etter eget valg

Nøkkelen lagres bare i nettleseren (IndexedDB). Alle Pages-sider under tombonator3000.github.io deler opprinnelse og dermed nettleserlagring, så nøkkelen skal bare ha lesetilgang til dette ene repoet.

Filene hentes fra GitHub med nøkkelen når spillet trenger dem, og lagres i nettleseren etter git-blob-ID. Ved hver start hentes fillisten for de to grenene på nytt, så ny HD-grafikk i `hd-mod` kommer med av seg selv, og bare filene som er endret, hentes. Fem sekunder etter at spillet har startet, hentes resten av HD-pakken i bakgrunnen (to filer om gangen, figurrutene først, så objekter og rom), så spillet ikke stopper for å vente på GitHub første gang det trenger en figurrute eller et rom. Det var det som ga hakkingen innimellom (15. oktober). `?uten-forhenting` slår det av. Bakgrunnshentingen prøver hver fil én gang; svarer GitHub med en grense (429), venter den et minutt, så filene spillet trenger kommer først. Indeksbildene for ruter uten HD-bilde (rundt 15 000 små filer) står sist i køen. Ingen spillfil eller HD-fil ligger på nettsiden eller sendes dit. Forespørslene går bare til api.github.com for repoet.

Spillfilene:

| Fil | Størrelse | Merknad |
| --- | --- | --- |
| `SAMNMAX.000` | 9 080 byte | Indeksen |
| `SAMNMAX.001` | 13 790 685 byte | Spillet, med musikken (MIDI) |
| `MONSTER.SOU` | 183 195 967 byte | Talen. Ligger i `spilldata` i to deler (`MONSTER.SOU.001` og `.002`), og siden setter dem sammen i nettleseren |
| `MT32_CONTROL.ROM`, `MT32_PCM.ROM` | 65 536 og 524 288 byte | Musikken: motoren bygges med `--enable-mt32emu` (14. oktober), og siden starter med `--music-driver=mt32` når ROM-filene er med |

Ikke målt: hvor mye som lastes ned før spillet kan vise noe, hvor mye minne siden bruker med talen, og om musikken spilles i nettleseren.

Fra The Dig sin nettside, ventet å virke likt (ikke testet):

- **Fullskjerm:** nettlesere tillater fullskjerm bare etter et klikk eller en tast, så spillet går i fullskjerm ved det første klikket eller tastetrykket.
- **Tegning:** med WebGL. Uten WebGL brukes ScummVMs programvaretegning (`--gfx-mode=surfacesdl`), og `?programvare` velger den med vilje.
- **Grafikk:** F5 åpner spillets meny, der raden HD Graphics skal velge HD eller originalgrafikk. Ctrl+H bytter også. Begge krever at patchen er portet.
- **Mobil og nettbrett** (`engine/pages/touch.mjs`): trykk er klikk, dra flytter pekeren, hold fingeren i ro et halvt sekund for høyreklikk, to fingre åpner spillets meny (F5), tre fingre gir Esc. Første trykk gir fullskjerm.
- **Nett:** mistes kontakten med GitHub mens spillet trenger en fil, venter spillet, og siden prøver igjen til filen er kommet. Bare en nøkkel GitHub avviser, stopper.
- **Valg i adressen:** `?ny-nokkel` (be om ny nøkkel), `?programvare`, `?uten-lyd`, `?uten-forhenting`, `?adlib` (AdLib i stedet for MT-32), `?rom=N`, `?klassisk`, `?gult` og testkrokene fra motoren (`DIGHD_*`, se [HD-MOTOR.md](HD-MOTOR.md)). `?rom`, `?klassisk`, `?gult` og testkrokene virker ikke før patchen er portet.
- **Uten nøkkel:** spillet kan kjøre fra mapper på maskinen (lenken under nøkkelfeltet): spillmappen med `SAMNMAX.000`, `SAMNMAX.001` og `MONSTER.SOU`, og HD-mappen (`mod.json`, `rooms`, vanligvis `mods/gpt`). Filene kopieres til nettleseren.
- **Lagring:** lagrede spill og scummvm.ini ligger i nettleserens lagring (IDBFS) og blir der selv om spillfilene slettes. Nettlesere kan slette lokal lagring ved lite ledig plass, og privatmodus kan gjøre lagringen midlertidig.

## Bygge fra kildekode

Krever git, make, Python 3, pkg-config, tar, xz og zip. Fra prosjektroten:

```sh
JOBS=2 engine/build-web.sh
python3 engine/build-pages.py
```

ScummVM er låst til `engine/SCUMMVM_COMMIT`. Emscripten 4.0.10 med Node, Clang og SDL3, libpng og zlib hentes til `engine/emsdk`. Byggeskriptet bruker ScummVM sin konfigurasjon, bare SCUMM-motoren er med, og prosjektets HD-patch legges på. Ingen av stegene henter spillet eller HD-pakken.

Nettsiden havner i `out/pages`. `source.tar.gz` inneholder den patchede ScummVM-kilden, HD-patchen, nettleserkoden og byggeoppskriften. Motoren og HD-patchen er GPL-3.0-or-later. ScummVM sin COPYRIGHT og lisensfilene skal følge nettsiden.

Ikke kjørt for Sam & Max.

## Publisere

Publiser bare innholdet i `out/pages`, i det egne repoet `Tombonator3000/Sam-Max-HD-Web`, som bare skal ha motoren (GPL). Repoet finnes ikke ennå.

En arbeidsflyt med `actions/upload-pages-artifact` og `actions/deploy-pages` kan publisere pakken. Nettsiden bruker relative adresser til motoren, så prosjektprefikset på GitHub Pages virker. Filpakkeren bruker en navneliste for ScummVM-temaene og kopierer aldri `data/games` fra distribusjonen. Kontroller `build.json` og filene før publisering.

## Verifisering

```sh
node --test engine/pages/tests/*.test.mjs
python3 -m http.server 8000 --bind 127.0.0.1 --directory out
```

Åpne http://127.0.0.1:8000/pages/ for å teste prosjektprefikset. Kontroller mappevalg, omlasting og lagring med spillfilene fra `game/`, og HD og HD-bryteren når patchen er portet. Spillfiler og HD-bilder skal ikke være tilgjengelige som HTTP-ressurser. En full gjennomspilling og mobiltest må rapporteres for seg.

Ingen av disse er kjørt for Sam & Max.
