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
| HD-motor | På for Sam & Max: rom, objekter, blast-objekter og figurer får HD fra modden. Testet med nearest-mod (0 avvik) og romtest i alle rom. Teksten har HD, og HD Graphics står i originalmenyen (F5); Ctrl+H bytter ([docs/HD-MOTOR.md](docs/HD-MOTOR.md)) |
| Uttrekk | `smhd extract` tar ut alt: 83 rombakgrunner, 959 objektbilder og 16 052 kostymeruter fra 348 kostymer, som PNG med metadata. Egne dekodere oversatt fra ScummVM |
| Skript | Alle 1181 skript dekompilert med descumm (`tools/dekompiler_skript.py`), 1179 uten feil |
| HD-grafikk | Under produksjon. Publisert mod bruker tapsfri WebP med ekte alfa; palettindekser og masker er PNG. Originalgrafikken brukes der HD mangler. Se [STATUS.md](STATUS.md) |
| Spille | Last ned ferdig Linux- eller Windows-pakke nedenfor. Begge inneholder spillet, tale, motor og dagens HD-mod |

Detaljer: [STATUS.md](STATUS.md). Hva som gjenstår: [todo.md](todo.md).

## Spille

Last ned den [felles kontrollerte utgaven](https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/sam-max-hd-2026-10-24-helikopter-forfaser). Du trenger ingen Git-klon eller grafikkarbeidsmappe.

| Plattform | Nedlasting | Plass etter utpakking | Start |
| --- | --- | --- | --- |
| [Linux AppImage](https://github.com/Tombonator3000/Sam-Max-HD/releases/download/sam-max-hd-2026-10-24-helikopter-forfaser/SamMaxHD-x86_64.AppImage) | 392 MB | Kjøres som én fil | Gjør filen kjørbar og start den |
| [Windows ZIP](https://github.com/Tombonator3000/Sam-Max-HD/releases/download/sam-max-hd-2026-10-24-helikopter-forfaser/SamMaxHD-Windows.zip) | 545 MB | 659 MB | Pakk ut og start «Sam og Max HD.bat» |

Størrelsene gjelder utgaven 24. oktober 2026, målt i desimale MB. Spillet, tale, motor og dagens HD-grafikk er inkludert. Grafikken lages fortsatt; dette er ikke en påstand om at all HD-grafikk er ferdig. Ctrl+H bytter HD og original; F5 åpner spillmenyen. Se [spilltest](docs/SPILLTEST.md) og [plassbruk og størrelsesgrenser](docs/PLASSBRUK.md).

## Bygge selv

Dette er utvikleroppsettet. Hent bare kodegrenen ved første kloning:

```sh
sudo apt install build-essential git pkg-config libsdl2-dev libpng-dev libwebp-dev zlib1g-dev
git clone --depth 1 --single-branch --branch main https://github.com/Tombonator3000/Sam-Max-HD.git
cd Sam-Max-HD
./spill.sh
```

`spill.sh` henter spillet og gjeldende HD-mod og bygger motoren første gang. Grafikerens råbilder, jobbmapper og historiske testkopier skal ikke hentes for å spille. Talen settes sammen fra grenen `spilldata`; `gpt-arbeid` er bare for grafikkproduksjon.

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer |
| `gpt-arbeid` | Grafikerens råbilder, jobbgrunnlag og kontrollrapporter. Inngår ikke i spillerpakken |
| `hd-mod` | Gjeldende HD-mod med bevarte Git-foreldre. Publiseres uten force-push |
