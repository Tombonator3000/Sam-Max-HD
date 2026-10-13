# Ordre fra Claude

Oppdatert 2026-10-13 10:45 (norsk tid)

Les denne filen før du starter. Den erstatter tidligere ordre. Les også `AGENTS.md` og `BESTILLING.md` i denne grenen.

## Status

- Jobber: 2264. ny 2264
- Ferdige rom: 0 av 76
- Ferdige objekter: 0 av 86
- Lagjobber: 0 av 296 godkjent. Ferdige objektbilder fra lag: 0 av 701
- Ikonark: 0 av 9 godkjent. Ferdige bilder fra ikonark: 0 av 163
- Figurark: 0 av 1758 godkjent. Ferdige figurruter: 0 av 15661
- Hovedark: 0 av 2 levert

## Stilpiloten (gjør dette nå)

Før noe annet males, lager vi en stilpilot som Tom godkjenner: hovedark for Sam og Max, kontoret (rom 7) og det første figurarket for hver av dem. Ta dem i denne rekkefølgen:

1. Hovedark for Sam: lag `hovedark/sam.png` etter `hovedark/sam/referanse.png` og `hovedark/sam/prompt.txt`, og skriv `hovedark/sam-notat.md`.
2. Hovedark for Max: lag `hovedark/max.png` etter `hovedark/max/referanse.png` og `hovedark/max/prompt.txt`, og skriv `hovedark/max-notat.md`.
3. `rom007_del1av2` (rom 7, Kontoret, del 1/2). (pilot)
4. `rom007_del2av2` (rom 7, Kontoret, del 2/2). (pilot)
5. `fig002_01` (figurark 1 for Sam (kostyme 2), 9 ruter: stående mot høyre, mot oss, bort (3 ruter); stående (lag 2, tegnes over kroppen) mot høyre (1 rute); start (lag 3, tegnes over kroppen) mot høyre, mot oss, bort (3 ruter); start (lag 4, tegnes over kroppen) mot høyre, mot oss (2 ruter), del 1/1). (pilot) Legg ved `hovedark/sam.png` som bilde to (ikke stilankeret). Lag denne etter at `hovedark/sam.png` er levert.
6. `fig003_01` (figurark 1 for Max (kostyme 3), 28 ruter: stående mot høyre, mot oss, bort (3 ruter); start (lag 3, tegnes over kroppen) mot høyre, mot oss, bort (3 ruter); start (lag 4, tegnes over kroppen) mot høyre, mot oss (2 ruter); gange mot høyre (8 ruter); snakking (lag 3, tegnes over kroppen) mot høyre (12 ruter), del 1/1). (pilot) Legg ved `hovedark/max.png` som bilde to (ikke stilankeret). Lag denne etter at `hovedark/max.png` er levert.

**Stopp etter piloten.** Ikke start på jobbene i `GRAFIKKLISTE.md` under «Etter godkjent stilpilot» før Tom har godkjent piloten og Claude har lagt stilankerne i `stil/` og skrevet en ny ordre. Kjør `verktoy/sjekk_leveranse.py` på hver leveranse før du committer.

## Stilankere

Ingen ennå. De godkjente pilotbildene blir stilankerne.

## Leveringsformat

- Rom, objekter, lag og ikonark: `resultat.png` på 1536 x 1024 med samme grå kant som `referanse.png`, eller bare bildet i samme sideforhold som utsnittet (16:10 for vanlige rom, minst 1280 x 800). Objekt-jobbene (`objNNN_SS`) er store bilder spillet tegner over rommet; leverer du bare bildet, skal det ha objektets sideforhold (`bilde_i_lerret` i `jobb.json`).
- Lagjobbene (`lagNNN_KK`) er rommet med spillets små objekter tegnet på plass. Objektene klippes ut etter posisjonen, så de må ligge nøyaktig der de er, med samme størrelse og omriss. Bilde to er det godkjente HD-bildet i `bilde_to`.
- Ikonarkene (`ikonNN`) er pekere, inventar, samtaleikoner og små deler på en flat bakgrunnsfarge. Hvert bilde klippes ut etter posisjonen. Hold bakgrunnen flat.
- Figurarkene (`figCCC_KK`) leveres som hele lerretet, 1536 x 1024, på gjennomsiktig bakgrunn med ekte alfa. Hver rute skal ha nøyaktig samme størrelse og plass som i referansen (en inndatapiksel er fire utdatapiksler). Før leveransen inn under `leveranser` i `rapporter/<din rapport>/fremdrift.json` med sha256, og lever et rutekart (`rapporter/<din rapport>/rutekart*.json`).
- Hovedarkene (`hovedark/<navn>.png`) leveres på gjennomsiktig bakgrunn, uten tekst.

Kjør `python3 verktoy/sjekk_leveranse.py <resultat>` før du committer, og gjør om det som får FEIL. Skriv `notat.md` i jobbmappen. Commit 5 til 10 jobber om gangen i grenen `gpt-arbeid` og push.

## Kodeoppgaver

Ingen kodeoppgaver nå. HD-motoren virker for Sam & Max, men det finnes ingen HD-mod ennå. `./spill.sh --auto` starter med automatisk oppskalering. Oppgavene under er for senere, når Claude har skrevet i `ORDRE.md` at de gjelder. De er for Codex eller ChatGPT med tilgang til laptopen og repoet. Ta én om gangen, og skriv i `rapporter/` i denne grenen hva du gjorde og fant.

1. **Test HD-modden på laptopen med skjerm og tastatur.** `git checkout main && git pull && ./spill.sh` henter, bygger og starter alt. Rommene som skal sjekkes, står i `ORDRE.md`. Følg `docs/SPILLTEST.md`. Sjekk:
   - at Sam og Max går bak ting i forgrunnen der de skal,
   - at objekter bytter bilde riktig,
   - at Ctrl+H bytter mellom HD og klassisk, og at Ctrl+Shift+H viser gult felt der HD mangler,
   - at F5 åpner spillets meny med raden HD Graphics, og at valget huskes,
   - at teksten (replikker og menyer) er glatt og står der den skal,
   - at mellomsekvenser og minispill vises riktig,
   - at ingenting krasjer når du går mellom rom med og uten HD.
   Ta skjermbilder i `rapporter/laptop-test/` og skriv `rapporter/laptop-test.md`: hva du testet, hva som var feil, med rom og omtrentlig sted. Ikke rett i motoren selv. Beskriv feilen, så retter Claude den.
2. **Mål fart og lyd.** Kjør ett rom i ett minutt med og uten modden. Noter bilder per sekund hvis ScummVM viser det, og om musikk eller tale hakker. Skriv det i `rapporter/laptop-test.md`.

Kodeendringer går som PR mot `main`, aldri rett i `main`. Skjermbilder og andre filer fra spillet skal bare ligge i denne grenen.

## Neste sjekk

Claude henter grenen, kontrollerer leveransene, oppdaterer `status.csv`, `RAPPORT.md` og `retur.md`, og skriver ny ordre her.
