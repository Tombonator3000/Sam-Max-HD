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
