# AGENTS.md

Instrukser for alle KI-agenter som jobber i dette repoet (Claude, Codex, ChatGPT).

## Før du starter

1. Les `memory.md` (faste fakta og beslutninger).
2. Les `todo.md`, særlig `## Neste`.
3. Les de siste oppføringene i `log.md`.
4. Les `STATUS.md` hvis du skal endre noe som er testet eller rapportert der.
5. Les `docs/HD-REMASTER-METODE.md` og `docs/HD-MOTOR.md` ved arbeid med motor, pipeline eller grafikk. Referansen er The Dig HD Remake (github.com/Tombonator3000/Dig-HD-Remake), som dette repoet er kopiert fra og tilpasset.
6. Før grafisk HD-arbeid, også stilpilot: les [remake-skillen](docs/skills/scumm-hd-remake/SKILL.md), særlig «Før HD-produksjon: avklar motiv og design». Avklar originalens betydning, funksjon, palett, figuridentitet og design før nytegning. Teknisk mottak alene er ikke visuell godkjenning.
7. Ressursbank: `docs/GJENNOMGANG.md` sier sted for sted hva som skjer, hvem som er der og hvilke ting som hører til hvilket rom (romnumre). Bruk den før et rom eller en figur tegnes eller testes.

## Mens du jobber

- Logg alt du gjør nederst i `log.md` med dato og klokkeslett i norsk tid, og hvem du er: `## 2026-10-10 13:20 (Claude)`, så punkter.
- Kryss av og legg til punkter i `todo.md` underveis.
- Oppdater `memory.md` når en beslutning eller et fast faktum endrer seg.
- Oppdater `STATUS.md` når noe nytt virker, er testet eller har fått en kjent begrensning.

## Stil

- Dokumentasjon og logg på norsk. Kode og kommentarer kan være på norsk eller engelsk, som filen rundt.
- Ingen emoji og ingen tankestreker. Skriv vanlig og direkte, uten fyllord og salgsspråk.
- Si hva som er testet og hvordan. Det som ikke er testet, står som ikke testet.

## Regler

- Spillfiler (`SAMNMAX.*`, `*.SM0`, `*.SM1`, `MONSTER.SOU`, `*.ROM`) og alt som lages fra dem (`work/`, `mods/`, HD-bilder) skal aldri inn i `main` eller kodegrener. De ligger i egne grener (se under).
- Repoet er offentlig etter Toms valg (10. oktober 2026). *Sam & Max Hit the Road* tilhører Disney/Lucasfilm. Tom har bestemt (13. oktober 2026) at grafikk og annet fra spillet kan deles utenfor repoet til hans eget, private bruk: som filer til egne maskiner og telefoner, eller på private steder bare han har tilgang til. Releasene (Linux- og Windows-pakken) har spillet og HD-grafikken med: Tom har bestemt (14. oktober 2026) at hele poenget med pakkene er å teste HD-utgaven, så HD-grafikken skal være med. Releasene er offentlige, og spillet og grafikken tilhører Disney/Lucasfilm. Andre offentlige sider har ellers ingen spillgrafikk. Unntak (Toms bevisste beslutning 13. oktober 2026): lystesten på GitHub Pages (https://tombonator3000.github.io/Sam-Max-HD/) har kontoret (rom 7) og hovedarkene til Sam og Max. Det er en offentlig side, og grafikken tilhører Disney/Lucasfilm. Publiseringen henter filene fra `gpt-arbeid` inn i Pages-pakken; de sjekkes ikke inn i `main`. Spillfilene og alt som lages fra dem holdes fortsatt utenfor `main` og kodegrenene.
- Kjør testene før du committer endringer i pipelinen eller motoren.
- Kodeendringer går via PR mot `main` og flettes når CI er grønn. Logg, status, todo og minne kan committes rett i `main`.

## Roller

- Claude: all kode (pipeline, motor, test, verktøy for grafikkjobbene) og kontrollen av grafikken.
- ChatGPT/Codex: HD-grafikken, etter `docs/BESTILLING-CHATGPT.md` når den er aktiv. Jobber bare i grenen `gpt-arbeid`.
- Tom: godkjenner stil og resultater.

## Oppsett

```sh
tools/hent_spilldata.sh          # spillfilene til game/, setter sammen MONSTER.SOU og sjekker sjekksummene
python3 -m venv .venv && . .venv/bin/activate
pip install -e "pipeline[dev]"   # smhd
smhd info                        # sjekker spillfilene og viser nøkkeltall
smhd extract                     # all originalgrafikk til work/extract (rom, objekter, kostymeruter)
engine/build.sh                  # ScummVM med patchen til engine/scummvm
./spill.sh                       # henter det som mangler, bygger og starter spillet
tools/bygg_descumm.sh && .venv/bin/python tools/dekompiler_skript.py   # alle skript som tekst i work/skript
```

`smhd extract` bruker egne dekodere for SCUMM v6 (`pipeline/smhd/v6grafikk.py`, oversatt fra ScummVM). Rutenummeret i kostymene er lag * 128 + kode. DigHD i patchen er på for The Dig og Sam & Max; i Sam & Max får rom, objekter, blast-objekter, figurer og teksten HD, og menyraden HD Graphics står i originalmenyen (`docs/HD-MOTOR.md`). Kjør `engine/test.sh` (0 avvik med nearest-mod) og gjerne `tools/romtest.sh --mod test-nearest --kamera ett` etter endringer i patchen.

## Kommandoer

```sh
cd pipeline && pytest            # etter endringer i pipelinen (game-testene hoppes over uten game/)
pytest -m "not game"             # det CI kjører
node --test engine/pages/tests/*.test.mjs   # nettsidekoden
engine/run.sh ingen              # spillet uten mod
python3 tools/indeks_info.py game/SAMNMAX.000
```

## Arbeid med motoren

- Fargebilder i den publiserte modden er tapsfri WebP fra 23. oktober 2026. Les `docs/WEBP.md` før motor-, mod- eller pakkeendringer. Originale grafikkjobber og råbilder beholder formatet sitt. Indeks- og maskebilder beholdes som PNG.
- Bruk gjeldende `hd-mod` som grunnlag. Gamle `out/`-modkopier er ryddet for verifiserte duplikater og kan være ufullstendige. Ikke bruk `tools/mod_gren.sh send`, som force-pusher; bevar tidligere publiserte filer i Git-historikken og verifiser ny faktisk nedlasting.

- Patchen ligger i `engine/patches/`. Gjør endringer i `engine/scummvm`, og lag patchen på nytt med
  `git -C engine/scummvm add -N engines/scumm/dighd.cpp engines/scumm/dighd.h && git -C engine/scummvm diff > engine/patches/0001-dighd-hd-grafikk.patch`.
- ScummVM-versjonen er låst i `engine/SCUMMVM_COMMIT`. Bytt den bare sammen med en test av patchen.
- Hva som må portes for v6: `docs/HD-MOTOR.md`.

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer, uten felles historikk med `main` |
| `gpt-arbeid` | Arbeidsbordet med ChatGPT/Codex. Ingen jobber før stilpiloten er godkjent |
| `hd-mod` | Gjeldende ferdige HD-mod. Publiser additivt med tidligere mod som Git-forelder og kontroller fjern-SHA før push |
