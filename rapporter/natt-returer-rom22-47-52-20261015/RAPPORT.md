# Fire returer fra ORDRE 15. oktober 2026 klokken 22:13

Fire leveranser er ferdige for Claudes kontroll. Alle fire består uendret egenkontroll, og alle 16 objekter består den strengere mottakskontrollen med check_pieces og piece_problem. Dette er lokal teknisk og visuell kontroll av bildene, ikke motorimport eller Toms godkjenning.

| Jobb | Skift | Blokker | Kantlikhet | Utfall |
| --- | --- | --- | --- | --- |
| lag022_02_del3av3 | 0,06 | 0,22 | 0,98 | OK |
| lag047_02 | 0,12 | 0,28 | 0,97 | OK |
| lag052_01_del2av2 | 0,02 | 0,10 | 0,97 | OK |
| lag052_02_del1av2 | 0,06 | 0,12 | 0,97 | OK |

Skift og blokker er i originalpiksler. Alle resultater er RGB PNG på 1536 x 1024 med eksakt #808080 utenfor bilde_i_lerret. Leveransebaner og SHA-256 står i [leveranser.json](leveranser.json). Samtlige 16 beskyttede filer er kontrollert mot [kildelåsen](beskyttede-kilder.json) og er uendret. Ingen figurark inngår, derfor er rutekart og figurfremdrift ikke relevant i denne runden.

## Grunnlag og motiv

Arbeidskopi: gpt-arbeid ved 1b571af9. ORDRE, AGENTS, BESTILLING, ANALYSE, GJENNOMGANG, GRAFIKKLISTE og feilrunde2s NATT-HANDOFF er lest. CLAUDE.md finnes ikke i denne mappen. Remake-skillens avsnitt om motiv og design er lest fra lokal origin/main. Originalene og de godkjente rombildene er sett. Referanse.png er geometri- og tilstandsfasit, bilde_to er stilgrunnlaget. De avviste leveringene brukes til å forstå returene og bevare andre gjennomarbeidede objekttilstander.

Lag022_02_del3av3 viser den åpne mørke døren, øksefiguren og Henrik VIII med løftet hånd. Nytegningen beholder hånden og ermet samlet. Obj228_02 har maskert kantlikhet 0,994 mot originalobjektet og -0,016 mot bakgrunnen. Dette løser den lokale returen på hånden. Den tidligere dokumenterte øksfeilen i motorens sammensetting er ikke erklært løst av denne leveransen.

Lag047_02 får nytt øvre øre-/øyeparti på det brune dyrehodet ved sceneskiltet. Hele første nytegning bestod egenkontroll, men mistet det lille øyet obj453_01 i mottakskontrollen. Derfor brukes bare feltet [768,208,160,64] fra nytegningen i forrige levering. Alle andre objekttilstander er beholdt. Obj442_01 har nå kantlikhet 0,945 mot objektet og 0,881 mot bakgrunnen. Alle åtte objekter består.

Lag052_01_del2av2 og lag052_02_del1av2 viser to munnfaser på den samme hvilende øglen. Det er små lag over et eksisterende dyr, ikke egne figurer. Tukanens åpne nebb og telefonboks-/dørtilstandene er også kontrollert. De første helbildene bestod teknikken, men innførte røde munnmerker. De er fjernet med nye bildeverktøykall. Tilstand 01 har mørkt gap uten oppdiktede indre merker. Tilstand 02 beholder den lille kjølige grålilla flaten som originalen viser foran i gapet. Ingen ny betydning er gitt til denne flaten. Sluttmålinger for obj486_01 er 0,775 mot objektet og 0,337 mot bakgrunnen. Obj486_02 har 0,815 mot objektet og 0,493 mot bakgrunnen.

## Nytegning og plassering

Ti nye image_gen-kall: ett for rom22, ett for rom47 og fire for hver lobbyjobb. Eksakt modellversjon er ikke eksponert. Første prompt per jobb begynner med prompt.txt ordrett, etterfulgt av returteksten og separate kildepresiseringer. Alle brukte prompter er bevart som jobbnavn-prompt*.txt. Råbilder og forkastede kandidater er bevart i denne mappen.

Lobbyenes andre forsøk kopierte hvilestillingen for mye og er forkastet. Tredje forsøk beholdt uønskede grå blokker. Fjerde forsøk retter munnfargene og beholder fasenes geometri. Bare feltene [550,748,60,48] og [934,748,60,48] fra de siste nytegningene er plassert i hovedforsøkene. Ingen originalkontur eller originalalfa brukes til å klippe leveransene.

[plassering.py](plassering.py) gjenskaper de fire resultatene. Python brukes til presis plassering av nytegnet grafikk og rensing av grå ramme etter Toms uttrykkelige tillatelse. Selve nytegningen er gjort med bildeverktøyet. [Kontaktark](leveranser-kontaktark.png), [dyrehode](lag047_02-hodekontroll.png) og [øglens munnfaser](ogle-faser-ferdig.png) er sett etter plassering.

Standard python3 mangler NumPy. Første bokstavelige egenkontroll stoppet derfor ved import. Alle sluttkontroller er kjørt med eksisterende /home/tom/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12 -B. Ingen pakker er installert. Egenkontrollen er uendret. Den strengere kontrollen bruker den eksisterende lokale pipeline-koden og originalobjektenes masker fra work/extract kun til måling. Resultatene står i [mottak-siste.json](mottak-siste.json).

## Overlevering

Claude bør kontrollere hånd/erme og øks i rom22 samlet i motoren, dyrehodets faseovergang i rom47, og øglens to munnfaser mot de senere fasene i rom52. Utsnittenes alfaklipp, underlag og tilstandsbytter må vurderes i den faktiske pakken. Skjerm, lyd og full animasjonsavspilling er ikke testet i denne økten.

[PR32-kontrollen](PR32-kontroll.md) dokumenterer konkrete statiske observasjoner. Ingen ny kodefeil er påvist innen undersøkt omfang. GitHub var utilgjengelig, så dagens PR-hode og CI er ikke bekreftet på nytt. Ingen kode er endret, duplisert eller flettet. Fig091_03 til 05 er urørt.

Git pull ble forsøkt ved start, men stoppet på skrivebeskyttet FETCH_HEAD utenfor arbeidskopien. Ingen commit eller push er forsøkt. Bare fire resultat.png, fire notat.md og filer under denne rapportmappen er endret eller opprettet. Nattskriptet kan ta dem med videre.
