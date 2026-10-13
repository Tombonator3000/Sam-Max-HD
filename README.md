# Sam & Max HD Remake

HD-versjon av *Sam & Max Hit the Road* (LucasArts 1993, SCUMM v6). Planen er den samme som for [The Dig HD Remake](https://github.com/Tombonator3000/Dig-HD-Remake): spillet kjører uendret i ScummVM, og en patch legger HD-grafikk nøyaktig oppå originalen i 4x oppløsning. Det som ikke har en HD-versjon ennå, vises som originalen skalert opp, så spillet kan spilles hele veien mens grafikken lages.

Arbeidsdeling: Claude skriver koden, ChatGPT/Codex lager HD-grafikken, Tom godkjenner.

Repoet er offentlig etter Toms valg. Spillfilene og alt som lages fra dem ligger i egne grener og skal aldri inn i `main`.

## Status

| Del | Status |
| --- | --- |
| Repo | Samme oppsett som The Dig HD Remake: `engine/`, `pipeline/` (`smhd`), `tools/`, `docs/`, `spill.sh`, arbeidsflyter og grenene `spilldata`, `hd-mod` og `gpt-arbeid`. Kopiert og tilpasset Sam & Max |
| Spillfiler | Engelsk CD-utgave (SAMNMAX.000, SAMNMAX.001, MONSTER.SOU med tale) i `spilldata` |
| Analyse | 85 rom med navn (36 brede), 63 med z-plan, 43 med fargesykling, 959 objektbilder, 348 kostymer. Se [docs/ANALYSE.md](docs/ANALYSE.md) og [docs/rom-oversikt.csv](docs/rom-oversikt.csv) |
| HD-motor | På for Sam & Max: rom, objekter, blast-objekter og figurer får HD fra modden. Testet med nearest-mod (0 avvik) og romtest i alle rom. Teksten og menyraden HD Graphics er ikke portet; Ctrl+H bytter ([docs/HD-MOTOR.md](docs/HD-MOTOR.md)) |
| Uttrekk | `smhd extract` tar ut alt: 83 rombakgrunner, 959 objektbilder og 16 052 kostymeruter fra 348 kostymer, som PNG med metadata. Egne dekodere oversatt fra ScummVM |
| Skript | Alle 1181 skript dekompilert med descumm (`tools/dekompiler_skript.py`), 1179 uten feil |
| HD-grafikk | Alle jobbene til ChatGPT er klargjort: hovedark for Sam og Max, rom, objekter, ikoner og 1758 figurark med fast størrelse og egenkontroll ([docs/BESTILLING-CHATGPT.md](docs/BESTILLING-CHATGPT.md)). Stilpiloten først, ingen bilder laget ennå |
| Spille | `./spill.sh` starter originalspillet. Linux-pakken er tilpasset, ikke bygget i Actions ennå. Nettsiden trenger eget repo |

Detaljer: [STATUS.md](STATUS.md). Hva som gjenstår: [todo.md](todo.md).

## Spille

```sh
sudo apt install build-essential git pkg-config libsdl2-dev libpng-dev zlib1g-dev   # én gang (Ubuntu/Debian)
git clone https://github.com/Tombonator3000/Sam-Max-HD.git && cd Sam-Max-HD
./spill.sh
```

`spill.sh` henter spillfilene og siste HD-mod, bygger motoren første gang og starter spillet. Talen (`MONSTER.SOU`) ligger i deler på 90 MB i `spilldata` fordi GitHub ikke tar filer over 100 MB, og settes sammen av `tools/hent_spilldata.sh`. Til det finnes en HD-mod, starter spillet med originalgrafikken; `./spill.sh --auto` gir automatisk oppskalering. Ctrl+H bytter mellom HD og original. Alle valg og hva du skal se etter: [docs/SPILLTEST.md](docs/SPILLTEST.md).

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer |
| `gpt-arbeid` | Arbeidsbordet med grafikerne: alle jobbene, bare stilpiloten er bestilt |
| `hd-mod` | Siste HD-pakke, én commit som erstattes. Tom til den første modden finnes |
