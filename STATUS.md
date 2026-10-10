# Status

Oppdatert 10. oktober 2026.

## Kort

Repoet er satt opp og spillfilene ligger i grenen `spilldata`. Ingen motor, pipeline eller grafikk ennå.

## Det som virker

| Del | Hva | Hvordan det er testet |
| --- | --- | --- |
| Spillfiler | SAMNMAX.000, SAMNMAX.001, MONSTER.SOU (i to deler) og de to MT-32-ROM-filene i `spilldata`, hentes og sjekkes med `tools/hent_spilldata.sh` | Se `log.md` 10. oktober: grenen hentet fra en ny klone, MONSTER.SOU satt sammen, SHA-256 for alle fem filer stemmer |
| Utgave | Engelsk CD-utgave | MD5 av SAMNMAX.000 funnet i ScummVMs `scumm-md5.h` |
| Format | XOR 0x69, v6-blokker i indeksen, LECF i SAMNMAX.001 | Lest med et lite Python-skript |

## Ikke testet

- At ScummVM starter spillet fra `game/` (ingen ScummVM bygget her ennå).
- Tellingene fra indeksen er ikke kontrollert mot innholdet i LECF.
