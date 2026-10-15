# Fire returjobber etter ORDRE 15. oktober 2026 klokken 21:44

Fire nye leveranser er klare til Claudes kontroll. Alle fire består egenkontrollen. Den strengere objektkontrollen smhd.gpt.check_pieces og piece_problem er kjørt med originalobjektenes alfamasker fra /home/tom/Sam-Max-HD/work/extract. Alle ti objekter i de tre lagjobbene består. Dette er lokal leveransekontroll, ingen ny motorimport eller godkjenning fra Tom.

## Resultat

| Jobb | Utfall | Skift | Blokker | Kantlikhet |
| --- | --- | --- | --- | --- |
| obj307_01 | OK | 0.37 | 0.36 | 0.956 |
| lag002_01 | OK | 0.02 | 0.09 | 0.969 |
| lag017_04_del1av2 | OK | 0.33 | 0.66 | 0.919 |
| lag017_04_del2av2 | OK | 0.07 | 0.57 | 0.943 |

Mål er i originalpiksler. Alle PNG-er er 1536 x 1024 RGB med eksakt grå ramme. SHA-256 og leveransebaner står i [leveranser.json](leveranser.json). Kontrollen av de 16 beskyttede kildene står i [beskyttede-kilder.json](beskyttede-kilder.json). Ingen figurark inngår, derfor er rutekart og figurfremdrift ikke relevante i denne runden.

## Kilde og motiv

Grunnlag: arbeidsgren gpt-arbeid ved 92392b21d588fac18f36585cc1a0c8bdfe50a950. Ordren, bestillingen, AGENTS.md, ANALYSE.md, ressursbanken, feilrunde 2s NATT-HANDOFF.md og scumm-hd-remake/SKILL.md fra lokal main er lest. CLAUDE.md finnes ikke i denne arbeidsmappen. Original_1x.png, referanse.png og relevante godkjente rom er sett før generering. Godkjent kontoranker er også sett. Avviste bilder brukes som feilgrunnlag og for å bevare uttrykkelig godkjente deler, ikke som nye stilankere.

Obj307_01 er toppstripen i kikkertens grålilla ramme. To skruer og fasetter er bevart. Andre forsøk ble tegnet med topp og nedre obj304_01 synlig samtidig. Bare toppstripen ble tatt ut, det godkjente nedre objektet er uendret. Etterarbeidet begrenser RGB-rensing til åtte HD-rader på felles flater. [Samlet skjøt](obj307-skjot-ferdig.png) er visuelt kontrollert.

Lag002_01 viser to ringpar rundt energikulene, med svakere ytre ring utenfor den indre. Lampen og resten av den tidligere leveransen er uendret utenfor de to objektrektanglene. Maskert kantlikhet er 0,935 for obj897_01 og 0,956 for obj900_01. Lampen beholder 0,680 mot objektet og 0,233 mot bakgrunnen.

Lag017_04_del1av2 og del2av2 viser tilstand 04 for røde, gule og grønne vimpler og andens propell. Første romforsøk bestod egenkontrollen, men hadde omtolkede rifter og fragmenter. Forstørrede originalutsnitt ble derfor brukt til ny lokal tegning. Nytegnede vimpler er renset til egen alfa og redusert til nøyaktig 4x. Originalens pikseltrapper brukes ikke som klippemaske. Rød vimpel har to løse røde biter. Grønn vimpel har to remser og seks løse biter. En liten oppstikker ble flyttet én HD-piksel for å beholde kontakt med remsen. Propellens nesten vannrette høyreblad og korte venstreblad er bevart. Samme røde og gule nytegning brukes i delenes overlapp.

Maskert kantlikhet fra mottakskontrollen: obj180_04 0,996, obj181_04 0,949, obj182_04 0,937 og obj183_04 0,814. Ingen av dem ligner mer på tom bakgrunn enn på originalobjektet. [Full kontroll](mottak-etter.json).

## Verktøy og etterarbeid

Innebygd image_gen, eksakt modellnavn ikke eksponert. Ni nye kall: to til kikkert, ett til laboratoriet, to hele Midway-bilder og fire lokale Midway-utsnitt. Prompt.txt er brukt ordrett i hvert første romforsøk, med separate presiseringer fra retur og kildekontroll. Lokale detaljforsøk bruker egne bevarte prompter. Beskyttede promptfiler er uendret.

Python brukes etter Toms uttrykkelige tillatelse til presis plassering og rensing. [plasser_utsnitt.py](plasser_utsnitt.py) gjenskaper Midway-leveransene. [rens_skjot.py](rens_skjot.py) gjenskaper kikkertstripen. Laboratoriet bruker nytegnede rektangler [544,272,224,192] og [160,304,160,128] fra råforsøket satt inn i forrige levering. Dette skal ikke forveksles med nytegning i Python.

Standard /usr/bin/python3 mangler NumPy. Egenkontroll og mottakskontroll er derfor kjørt med eksisterende /home/tom/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12 -B. Ingen pakker er installert. Ingen endring utenfor repoet er gjort av etterarbeidet.

## For Claude

Kontroller særlig kikkertskjøten i spillstørrelse, at de ytre energiringene gir en egen synlig tilstand, og overgangene til og fra vimpel- og propelltilstand 04. Mottakets alfaklipp og fargelås må kontrolleres i den faktiske pakken. Full animasjonsavspilling, skjerm og lyd er ikke testet her.

Git pull ble forsøkt først, men stoppet med read-only file system for /home/tom/Sam-Max-HD/.git/worktrees/-gpt-gren/FETCH_HEAD. Ingen commit eller push er forsøkt. Nattskriptet kan ta med resultat.png, notat.md og denne rapportmappen.

Ingen kodeøkt i denne runden. Forrige avgrensede statiske kontroll av PR32 står i [PR32-kontroll.md](../natt-fire-returer-20261015/PR32-kontroll.md). Den er lest, men dagens PR-hode eller CI er ikke hentet på nytt. PR32 er ikke flettet eller duplisert. Fig091_03 til 05 er ikke endret.
