# Sam & Max HD Remake

HD-versjon av *Sam & Max Hit the Road* (LucasArts 1993, SCUMM v6). Planen er den samme som for [The Dig HD Remake](https://github.com/Tombonator3000/Dig-HD-Remake): spillet kjører uendret i ScummVM, og en patch legger HD-grafikk nøyaktig oppå originalen i 4x oppløsning. Det som ikke har en HD-versjon ennå, vises som originalen skalert opp, så spillet kan spilles hele veien mens grafikken lages.

Arbeidsdeling: Claude skriver koden, ChatGPT/Codex lager HD-grafikken, Tom godkjenner.

Repoet er offentlig etter Toms valg. Spillfilene og alt som lages fra dem ligger i egne grener og skal aldri inn i `main`.

## Status

| Del | Status |
| --- | --- |
| Repo | Samme oppsett som The Dig HD Remake: `engine/`, `pipeline/` (`smhd`), `tools/`, `docs/`, `spill.sh`, arbeidsflyter og grenene `spilldata`, `hd-mod` og `gpt-arbeid`. Kopiert og tilpasset Sam & Max |
| Spillfiler | Engelsk CD-utgave (SAMNMAX.000, SAMNMAX.001, MONSTER.SOU med tale) i `spilldata` |
| Analyse | 85 rom (36 brede), 63 med z-plan, 43 med fargesykling, 959 objektbilder, 348 kostymer. Se [docs/ANALYSE.md](docs/ANALYSE.md) og [docs/rom-oversikt.csv](docs/rom-oversikt.csv) |
| HD-motor | ScummVM med The Dig-patchen bygger og kjører Sam & Max, men uten HD: DigHD er ikke portet til SCUMM v6 ennå ([docs/HD-MOTOR.md](docs/HD-MOTOR.md)) |
| Uttrekk | Ikke portet (`smhd extract` stopper med en melding) |
| HD-grafikk | Ikke startet. Stilpilot med Tom først |
| Spille | `./spill.sh` starter originalspillet. Linux-pakken er tilpasset, ikke bygget i Actions ennå. Nettsiden trenger eget repo |

Detaljer: [STATUS.md](STATUS.md). Hva som gjenstår: [todo.md](todo.md).

## Spille

```sh
sudo apt install build-essential git pkg-config libsdl2-dev libpng-dev zlib1g-dev   # én gang (Ubuntu/Debian)
git clone https://github.com/Tombonator3000/Sam-Max-HD.git && cd Sam-Max-HD
./spill.sh
```

`spill.sh` henter spillfilene og siste HD-mod, bygger motoren første gang og starter spillet. Talen (`MONSTER.SOU`) ligger i deler på 90 MB i `spilldata` fordi GitHub ikke tar filer over 100 MB, og settes sammen av `tools/hent_spilldata.sh`. Til HD-delen er portet, starter spillet som originalen. Alle valg og hva du skal se etter: [docs/SPILLTEST.md](docs/SPILLTEST.md).

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer |
| `gpt-arbeid` | Arbeidsbordet med grafikerne. Ingen jobber før stilpiloten |
| `hd-mod` | Siste HD-pakke, én commit som erstattes. Tom til den første modden finnes |
