# Sam & Max HD på GitHub Pages

Planen er den samme som for The Dig: en nettside som går rett inn i spillet, på PC og mobil, med bare den kompilerte ScummVM-motoren, HD-patchen, brukergrensesnittet, ScummVM sine temaer og tilhørende kildekode. Spillfiler og HD-bilder skal aldri inn i nettsidepakken.

## Status

| Del | Status |
| --- | --- |
| Nettsiderepoet `Tombonator3000/Sam-Max-HD-Web` | Finnes ikke ennå |
| Nettsidekoden i `engine/pages` | Tilpasset Sam & Max. Ikke bygget og ikke testet i nettleser |
| Motoren for nettleseren (`engine/build-web.sh`, `engine/build-pages.py`) | Ikke bygget for Sam & Max |
| HD-grafikk | Ingen. HD-patchen er ikke portet til SCUMM v6, så motoren viser bare originalgrafikken, og det finnes ingen HD-mod i `hd-mod` |

Alt under beskriver hvordan siden skal virke, etter The Dig sin nettside. Ingenting av det er prøvd med Sam & Max.

`./spill.sh --nettleser` er en egen løsning som kjører nettleserversjonen på localhost fra filene på maskinen (se [SPILLTEST.md](SPILLTEST.md)).

## Spille

Siden går rett inn i spillet, som originalen. Det er ingen knapper eller menyer rundt spillet. Grafikkvalget skal ligge i spillets egen meny.

Første gang ber siden om en lesenøkkel til repoet `Tombonator3000/Sam-Max-HD`, der spillet (grenen `spilldata`) og HD-pakken (grenen `hd-mod`) ligger. Nøkkelen lages på https://github.com/settings/personal-access-tokens/new:

- Repository access: Only select repositories, Sam-Max-HD
- Permissions: Contents, Read-only
- Utløpsdato etter eget valg

Nøkkelen lagres bare i nettleseren (IndexedDB). Alle Pages-sider under tombonator3000.github.io deler opprinnelse og dermed nettleserlagring, så nøkkelen skal bare ha lesetilgang til dette ene repoet.

Filene hentes fra GitHub med nøkkelen når spillet trenger dem, og lagres i nettleseren etter git-blob-ID. Ved hver start hentes fillisten for de to grenene på nytt, så ny HD-grafikk i `hd-mod` kommer med av seg selv, og bare filene som er endret, hentes. Ingen spillfil eller HD-fil ligger på nettsiden eller sendes dit. Forespørslene går bare til api.github.com for repoet.

Spillfilene:

| Fil | Størrelse | Merknad |
| --- | --- | --- |
| `SAMNMAX.000` | 9 080 byte | Indeksen |
| `SAMNMAX.001` | 13 790 685 byte | Spillet, med musikken (MIDI) |
| `MONSTER.SOU` | 183 195 967 byte | Talen. Ligger i `spilldata` i to deler (`MONSTER.SOU.001` og `.002`), og siden setter dem sammen i nettleseren |
| `MT32_CONTROL.ROM`, `MT32_PCM.ROM` | 65 536 og 524 288 byte | Valgfrie. `engine/build.sh` og `engine/build-web.sh` bygger nå motoren med `--disable-mt32emu`, så de brukes ikke |

Ikke målt: hvor mye som lastes ned før spillet kan vise noe, hvor mye minne siden bruker med talen, og om musikken spilles i nettleseren.

Fra The Dig sin nettside, ventet å virke likt (ikke testet):

- **Fullskjerm:** nettlesere tillater fullskjerm bare etter et klikk eller en tast, så spillet går i fullskjerm ved det første klikket eller tastetrykket.
- **Tegning:** med WebGL. Uten WebGL brukes ScummVMs programvaretegning (`--gfx-mode=surfacesdl`), og `?programvare` velger den med vilje.
- **Grafikk:** F5 åpner spillets meny, der raden HD Graphics skal velge HD eller originalgrafikk. Ctrl+H bytter også. Begge krever at patchen er portet.
- **Mobil og nettbrett** (`engine/pages/touch.mjs`): trykk er klikk, dra flytter pekeren, hold fingeren i ro et halvt sekund for høyreklikk, to fingre åpner spillets meny (F5), tre fingre gir Esc. Første trykk gir fullskjerm.
- **Nett:** mistes kontakten med GitHub mens spillet trenger en fil, venter spillet, og siden prøver igjen til filen er kommet. Bare en nøkkel GitHub avviser, stopper.
- **Valg i adressen:** `?ny-nokkel` (be om ny nøkkel), `?programvare`, `?uten-lyd`, `?rom=N`, `?klassisk`, `?gult` og testkrokene fra motoren (`DIGHD_*`, se [HD-MOTOR.md](HD-MOTOR.md)). `?rom`, `?klassisk`, `?gult` og testkrokene virker ikke før patchen er portet.
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
