# AGENTS.md

Instrukser for alle KI-agenter som jobber i dette repoet (Claude, Codex, ChatGPT).

## Før du starter

1. Les `memory.md` (faste fakta og beslutninger).
2. Les `todo.md`, særlig `## Neste`.
3. Les de siste oppføringene i `log.md`.
4. Les `STATUS.md` hvis du skal endre noe som er testet eller rapportert der.
5. Les `docs/HD-REMASTER-METODE.md` og `docs/HD-MOTOR.md` ved arbeid med motor, pipeline eller grafikk. Referansen er The Dig HD Remake (github.com/Tombonator3000/Dig-HD-Remake), som dette repoet er kopiert fra og tilpasset.

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
- Repoet er offentlig etter Toms valg (10. oktober 2026). *Sam & Max Hit the Road* tilhører Disney/Lucasfilm. Ingenting fra spillet deles utenfor repoet.
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
engine/build.sh                  # ScummVM med patchen til engine/scummvm
./spill.sh                       # henter det som mangler, bygger og starter spillet
```

`smhd extract` er ikke portet til SCUMM v6 ennå (The Dig brukte dekoderne i thedig-textures). DigHD i patchen er bare slått på for The Dig. Til begge er portet, kjører Sam & Max som originalen, og `engine/test.sh`, `tools/romtest.sh`, `tools/gpt_runde.sh` og `./spill.sh --auto` kan ikke brukes.

## Kommandoer

```sh
cd pipeline && pytest            # etter endringer i pipelinen (game-testene hoppes over uten game/)
pytest -m "not game"             # det CI kjører
node --test engine/pages/tests/*.test.mjs   # nettsidekoden
engine/run.sh ingen              # spillet uten mod
python3 tools/indeks_info.py game/SAMNMAX.000
```

## Arbeid med motoren

- Patchen ligger i `engine/patches/` og er foreløpig den samme som i The Dig. Gjør endringer i `engine/scummvm`, og lag patchen på nytt med
  `git -C engine/scummvm add -N engines/scumm/dighd.cpp engines/scumm/dighd.h && git -C engine/scummvm diff > engine/patches/0001-dighd-hd-grafikk.patch`.
- ScummVM-versjonen er låst i `engine/SCUMMVM_COMMIT`. Bytt den bare sammen med en test av patchen.
- Hva som må portes for v6: `docs/HD-MOTOR.md`.

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer, uten felles historikk med `main` |
| `gpt-arbeid` | Arbeidsbordet med ChatGPT/Codex. Ingen jobber før stilpiloten er godkjent |
| `hd-mod` | Siste ferdige HD-mod, én commit som erstattes. Tom til den første modden finnes |
