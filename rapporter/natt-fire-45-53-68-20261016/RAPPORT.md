# Fire lagjobber i rom 45, 53 og 68

Dato: 16. oktober 2026. Levert: 4 ark med 30 objektrektangler i jobbmetadataene. Visuelt kontrollert av Codex: 4 ark og deres synlige objektutsnitt. Importert i denne økten: 0. Motoravspilling: ikke utført. Toms godkjenning: ikke innhentet.

De fire første jobbene i ORDRE.md datert 16. oktober klokken 01:43 er utført i oppgitt rekkefølge. Ingen av de fire hadde retur.md. PR32 er ikke kontrollert på nytt, Sam091 er ikke tegnet om, og ingen kode er endret.

| Jobb | Bildeforsøk | Skift | Blokkavvik | Kantlikhet | Egenkontroll |
| --- | --- | --- | --- | --- | --- |
| lag045_02 | 2 | 0,09 | 0,16 | 0,972 | OK |
| lag053_01_del1av2 | 1 | 0,11 | 0,11 | 0,966 | OK |
| lag053_02_del1av2 | 1 | 0,10 | 0,06 | 0,970 | OK |
| lag068_01 | 3 | 0,11 | 2,00 | 0,942 | SJEKK |

Alle sluttfiler er 1536 x 1024 med flat #808080 utenfor bildeområdet. Alle 16 beskyttede jobbfiler er kontrollert byte for byte mot HEAD og er uendret. [Leveransemanifestet](leveranser.json) har SHA256, stilreferanser, målinger og separat status for visuell kontroll og import. [Kildehashene](kildehash.json) og [råfilhashene](raafiler-sha256.json) dokumenterer grunnlaget.

## Motiv og stil

AGENTS.md, ORDRE.md, BESTILLING.md, ANALYSE.md, GJENNOMGANG.md og NATT-HANDOFF.md er lest. CLAUDE.md finnes ikke i denne arbeidskopien. Remake-skillen og HD-REMASTER-METODE.md er lest fra lokal main med git show. Originalene i 4x, jobbmetadata og de tre godkjente HD-rommene er undersøkt før tegning. Max-hovedarket er i tillegg kontrollert og lagt ved etter første Highway Surfing-forsøk.

Første bildeforsøk for hver jobb brukte prompt.txt ordrett. Senere rettinger ligger i egne tekstfiler her. Bilde én var alltid jobbens referanse, bilde to det godkjente HD-rommet. Innebygd image_gen er brukt til all nytegning. Eksakt modellnavn er ikke eksponert. Pillow er bare brukt til grå ramme, sammensetting av nytegnede forsøk og dokumenterende kontrollbilder. Ingen beskyttede jobbfiler, motorfiler eller pipelinefiler er endret.

Soverommet: Auberginen på sokkelen er en konkret gåtetilstand. Første forsøk utelot den og er forkastet. [LucasArts-hintboken](https://www.mocagh.org/lucasfilm/sammax-hintbook.pdf) bekrefter at Conroy-auberginen brukes for å få tupéen fra soverommet. Den blå boken og trappetilstanden følger originalen. Skiltet MA TRUK er bevart.

Festsalen: Blå musikere med instrumenter og mørke lilla festdeltakere følger originalen og godkjent rom. Første lag har tom vinflaskeposisjon, slik originalen krever. Andre lag inneholder egne arm- og kroppsdeler. Utsnittene er kontrollert samlet, men animasjonen er ikke avspilt.

Highway Surfing: Første forsøk manglet høyrekantrestene av Max og ga FEIL 7,22 i blokkmålingen. Andre forsøk ga SJEKK, men rosa øreinnsider var feil sett bakfra. Tredje forsøk rettet dette visuelt, men ga FEIL 3,75 i veifeltets blokk. Leveransen kombinerer øvre del fra forsøk tre med nedre del fra forsøk to. En lineær alfaskjøt ligger mellom y352 og y384 i tom himmel. Grå ramme er renset. Ingen motiver er flyttet eller skalert i sluttbildet. Forsøket beskrevet i plassering-vei.json er forkastet og brukes ikke.

Highway Surfing skal fortsatt behandles som SJEKK. Nedre midtblokk måler 2,00 originalpiksler. Veifeltet er visuelt sammenlignet med originalen, men måleresultatet er ikke avvist som falskt. obj651_01 og obj652_01 har samme rektangel og er for det meste utenfor romutsnittet. Leveransen dokumenterer bare deres synlige deler. Claude må kontrollere utklipp og faktisk tilstandsbruk før importen regnes som klar.

## Kontroll og overlevering

Hver jobb har et objektkontrollbilde med original, leveranse og godkjent HD-rom, et 50 prosent overlegg og egenkontrollens tekstutskrift. kontroll.py.txt kan kjøres med prosjektets eksisterende miljø:

```sh
PYTHONDONTWRITEBYTECODE=1 PATH=/home/tom/Sam-Max-HD/.venv/bin:$PATH python3 rapporter/natt-fire-45-53-68-20261016/kontroll.py.txt
```

Ingen pakker er installert. Systemets python3 mangler numpy, så det eksisterende prosjektmiljøet er brukt. Egenkontrollen er kjørt uendret. Tre leveranser er OK og én er SJEKK. Ingen sluttleveranse har FEIL.

Utgangspunkt: 4cd719f30b498b0e79b1d9f175a26ebfc1f3b102, gren gpt-arbeid. Git pull ble forsøkt, men FETCH_HEAD ligger i skrivebeskyttede Git-metadata utenfor sandkassen. Ingen commit, push, grenbytte, PR, fletting eller historikkendring er utført. Nattløpets skript må ta med de fire resultat.png, fire notat.md og denne rapportmappen. Ingen ny konkret kodeblokkering er påvist.
