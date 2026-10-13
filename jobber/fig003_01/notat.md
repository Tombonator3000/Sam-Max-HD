# Max: figurark fig003_01

Levert lokalt 2026-10-13T17:29:18+02:00. 28 ruter, PNG RGBA, 1536 x 1024, ekte alfa. Originalen er jobbens uendrede referanse/original_1x/jobb.json/prompt.txt. Godkjent hovedark/max.png styrer identiteten. Ett genereringsforsøk med innebygd ChatGPT-bildegenerator, eksakt modellnavn ikke eksponert. Råbilde og faktisk prompt finnes i rapporter/stilpilot-fortsettelse-20261013/fig003_01-forsok-01.*.

Presis bildebehandling med Pillow etter Toms godkjente metode har tilpasset hver rute samlet til originalens synlig-boks i 4x, med myk alfa. Ingen originalpikselmaske brukes til å forme figuren. En feil ring på frontkroppens mage er erstattet med den riktige lille markeringen fra godkjent frontmaster, med lokal myk sammensetting. Genererte pupiller er skalert/flyttet til originalens øyefester, og de nye øyelokkflekkene har lokal hudgradient og svak fold. Bakgrunnsglød er fjernet ved hjelp av tegningenes egne figurkjerner og kantpiksler.

Uendret prosjektkontroll: OK (26/26 store nok ruter). Utvidet sluttkontroll: alle 28 rutebokser er eksakte, også de to små øyelokkrutene som prosjektkontrollen hopper over. Begge øyelokkrutene beholder to atskilte flekker. Blinkdiagnosen viser full dekning av de fire relevante mørke øyefestene. Se rutekart-max.json, max-presis-kontroll.json, max-blink-kontroll.json og max-egenkontroll.txt i rapportmappen.

Stående kropp+hode, frontkorreksjon, blink, gange og talehoder er satt sammen til diagnostiske kontaktark i rapportmappen. max-gange-diagnose.gif er en visuell poseoversikt med valgt tempo, ikke original timing eller motoravspilling. Root har ved samlet levering sett de ferdige stå-, blink- og gangkontaktarkene. Sluttkontrollen av alle 28 rutebokser og den uendrede egenkontrollen er bestått.

Tom har godkjent stilpiloten og autorisert resten av HD-konverteringen. Ingen motorimport, originaltimingkontroll eller spilltest er utført i denne grafikkleveransen. status.csv og ORDRE.md er ikke endret.

SHA-256: 20f125fce533fe320a2a1715221c912a6128b218832de03586f6360db506551d.

## Kildetro munnretting 2026-10-14

De kildeidentiske munnfeltene 395, 402 er rettet med nye, lokalt genererte svart/hvite munnfelter fra bestilling 058. Originalen har ikke rødt i disse feltene. Bare RGB inne i de dokumenterte munnrektanglene er erstattet; all alfa og alle øvrige atlaspiksler er uendret. Førversjonen er bevart i `rapporter/bestilling058-20261013/root-fig003_01-for-munn.png`. Bevis: `rapporter/bestilling058-20261013/root-maxmunn-rettingbevis.json`.

Ny SHA-256: `c3e080fc505c743a436e64c5a2e2bd1e7a9ccac0829011b8c6a82dc5dd4af70e`. Egenkontroll: OK. Ingen ny individuell brukergodkjenning, import eller runtime-test.
