# AGENTS.md

Instrukser for alle KI-agenter som jobber i dette repoet (Claude, Codex, ChatGPT).

## Før du starter

1. Les `memory.md` (faste fakta og beslutninger).
2. Les `todo.md`, særlig `## Neste`.
3. Les de siste oppføringene i `log.md`.
4. Les `STATUS.md` hvis du skal endre noe som er testet eller rapportert der.
5. Referansen er The Dig HD Remake (github.com/Tombonator3000/Dig-HD-Remake). Les `AGENTS.md`, `docs/HD-MOTOR.md` og `docs/HD-REMASTER-METODE.md` der før du lager motor, pipeline eller grafikkjobber her.

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
- ChatGPT/Codex: HD-grafikken. Jobber bare i grenen `gpt-arbeid` når den finnes.
- Tom: godkjenner stil og resultater.

## Oppsett

```sh
tools/hent_spilldata.sh          # spillfilene til game/, setter sammen MONSTER.SOU og sjekker sjekksummene
```

Motor, pipeline og spill.sh kommer etter hvert, etter mønster fra The Dig.

## Grener

| Gren | Innhold |
| --- | --- |
| `main` | Kode og dokumentasjon |
| `spilldata` | Spillfilene med sjekksummer, uten felles historikk med `main` |
| `gpt-arbeid` | Arbeidsbordet med ChatGPT/Codex (lages når grafikkarbeidet starter) |
| `hd-mod` | Siste ferdige HD-mod, én commit som erstattes (lages når modden finnes) |
