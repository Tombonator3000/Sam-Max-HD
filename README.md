# Sam & Max HD Remake

HD-versjon av *Sam & Max Hit the Road* (LucasArts 1993, SCUMM v6). Planen er den samme som for [The Dig HD Remake](https://github.com/Tombonator3000/Dig-HD-Remake): spillet kjører uendret i ScummVM, og en patch legger HD-grafikk nøyaktig oppå originalen i 4x oppløsning. Det som ikke har en HD-versjon ennå, vises som originalen skalert opp, så spillet kan spilles hele veien mens grafikken lages.

Arbeidsdeling: Claude skriver koden, ChatGPT/Codex lager HD-grafikken, Tom godkjenner.

Repoet er offentlig etter Toms valg. Spillfilene og alt som lages fra dem ligger i egne grener og skal aldri inn i `main`.

## Status

| Del | Status |
| --- | --- |
| Repo | Satt opp som The Dig: AGENTS, logg, minne, todo, status, grener |
| Spillfiler | CD-utgaven (SAMNMAX.000, SAMNMAX.001, MONSTER.SOU med tale). Se `memory.md` for utgave og sjekksummer |
| Uttrekk | Ikke startet |
| HD-motor | Ikke startet. The Dig-patchen er for SCUMM v7 og må tilpasses v6 |
| HD-grafikk | Ikke startet |

Detaljer: [STATUS.md](STATUS.md). Hva som gjenstår: [todo.md](todo.md).

## Hente spillfilene

```sh
git clone https://github.com/Tombonator3000/Sam-Max-HD.git && cd Sam-Max-HD
tools/hent_spilldata.sh
```

Skriptet henter grenen `spilldata` til `game/`, setter sammen talen (`MONSTER.SOU` ligger i deler på 90 MB fordi GitHub ikke tar filer over 100 MB) og sjekker sjekksummene.

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer |
| `gpt-arbeid` | Arbeidsbordet med grafikerne (kommer) |
| `hd-mod` | Siste HD-pakke (kommer) |
