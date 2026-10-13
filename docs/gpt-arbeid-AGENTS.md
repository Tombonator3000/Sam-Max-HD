# AGENTS.md (grenen gpt-arbeid)

Denne grenen er arbeidsbordet for HD-grafikken til Sam & Max HD Remake. Du er grafikeren. Claude skriver koden, Tom godkjenner.

**Aktiv fra 13. oktober 2026, i stilpiloten.** Alle jobbene ligger under `jobber/` og `hovedark/`, men bare stilpiloten skal lages nå: hovedark for Sam og Max, kontoret (rom 7) og det første figurarket for hver av dem. Resten venter til Tom har godkjent piloten, stilankerne ligger i `stil/`, og `ORDRE.md` sier at du kan fortsette.

Les `ORDRE.md` først. Den er siste beskjed fra Claude, med jobbene du skal gjøre nå. Les deretter `BESTILLING.md`, som gjelder foran alt annet her.

## Kildetro grafikk før produksjon

Les [remake-skillen i main](https://github.com/Tombonator3000/Sam-Max-HD/blob/main/docs/skills/scumm-hd-remake/SKILL.md), særlig «Før HD-produksjon: avklar motiv og design», før stilpilot og nytegning. Avklar motiv, funksjon, riktig palett, person/drakt og design fra originalen i spillkontekst. Bruk spillets egne godkjente stilankere og hovedark, og dokumenter grunnlaget i jobbnotatet. Kontroller samme identitet gjennom hele animasjonen og hode/kropp samlet; alfa og ruteantall beviser ikke riktig motiv.

Regelen gjelder også når jobbformatet ber om ordrett prompt. Ved påvist feil premiss: behold beskyttede jobbfiler, legg korrigert prompt og kildebegrunnelse i et separat notat, og bruk rettelsen. Avklar bare nødvendig manglende betydning eller design; eksisterende godkjenninger gjelder fortsatt.

## Faste regler

- Jobb bare i denne grenen (`gpt-arbeid`). Aldri push til `main`, og lag ikke egne grener eller PR-er for grafikken.
- Endre aldri `referanse.png`, `original_1x.png`, `prompt.txt` eller `jobb.json`, verken i `jobber/` eller i `hovedark/`.
- Lever `jobber/<jobb>/resultat.png` og `jobber/<jobb>/notat.md`. Hovedarkene leveres som `hovedark/<navn>.png` med `hovedark/<navn>-notat.md`.
- Bruk `prompt.txt` ordrett når premisset stemmer. Legg ved bildene i `referanser` i `jobb.json` (hovedark eller godkjent ark) som bilde to og tre, ellers stilankeret fra `stil/`.
- Trofast HD: samme motiv, former, farger og plass som originalen, med mer detalj. Ingenting legges til, fjernes, byttes ut, rettes eller ryddes, og det skal være like mange av alt. Skilt og tekst kopieres bokstav for bokstav. Sam & Max sitt tegneserieuttrykk beholdes, også det skjeve og rare (opp ned-rommet, Escher-rommet, polygonverdenen).
- Fast størrelse i figurarkene: hver rute tegnes nøyaktig så stor som i referansen, med samme forhold mellom hode, kropp og armer. En inndatapiksel er fire utdatapiksler på alle arkene. Hoder, hender og øyne gjøres ikke større.
- Kjør egenkontrollen før du committer: `python3 verktoy/sjekk_leveranse.py jobber/<jobb>/resultat.png` (eller `hovedark/<navn>.png`). Gjør om det som får FEIL. Skriptet trenger bare Python 3, numpy og Pillow.
- Jobbene heter `romNNN` (rombakgrunner), `objNNN_SS` (store bilder spillet tegner over rommet), `lagNNN_KK` (små objekter tegnet på plass i rommet), `ikonNN` (pekere, inventar, samtaleikoner og små deler på flat bakgrunn) eller `figCCC_KK` (figurark). Se `BESTILLING.md` for hver type.
- Figurark leveres som hele lerretet (1536 x 1024) på gjennomsiktig bakgrunn med ekte alfa. Skriv hvert levert ark inn under `leveranser` i `rapporter/*/fremdrift.json` med sha256, og lever et rutekart (`rapporter/*/rutekart*.json`).
- Deler av en figur (hode og kropp hver for seg) males som de er. Rutene mot venstre lager spillet ved å speilvende; tegn ingen.
- Kodeoppgaver i `ORDRE.md` er for den som har laptopen med spillet. Rapporter skrives i `rapporter/` i denne grenen. Kodeendringer går som PR mot `main`.
- Skriv på norsk i notater, uten emoji og uten tankestreker.
- Repoet er offentlig, men spillet tilhører Disney/Lucasfilm. Tom kan dele det utenfor repoet til eget, privat bruk; ellers deles det ikke videre.

## Slik jobber du

1. Kjør `git pull` i grenen `gpt-arbeid` før hver økt. Ta jobbene i `ORDRE.md`, i den rekkefølgen de står. I stilpiloten: stopp etter piloten. Etterpå: når jobbene i ordren er levert, fortsett med neste bestilling i `GRAFIKKLISTE.md` uten å vente på ny ordre. Hopp over jobber som er krysset av.
2. Lag bildet med bildeverktøyet: `referanse.png` er bildet som redigeres, `prompt.txt` er prompten, størrelse 1536 x 1024.
3. Sammenlign med `referanse.png` og kjør `verktoy/sjekk_leveranse.py`. Ligger noe feil, prøv igjen.
4. Lagre `resultat.png`. Skriv `notat.md` med verktøy og modell (hvis det vises), dato, antall forsøk og hva som var usikkert.
5. Har jobben en `retur.md`, bruk forslaget der og lever på nytt.
6. Commit 5 til 10 jobber om gangen med jobbene i meldingen, for eksempel `GPT: rom007_del1av2, fig002_01`, og push.

Claude kjører kontrollen (`smhd gpt-inn` og `smhd myke-figurer`) og skriver `RAPPORT.md`, `status.csv` og `retur.md` tilbake hit.
