# Fire returer fra ORDRE.md

15. oktober 2026, omtrent 21:18 norsk tid. Arbeidskopi gpt-arbeid ved 3284d7c369f688fcdc37c1740418e9b495692908. Ingen commit, push, grenbytte, PR eller fletting utført.

Fire jobber levert i ordrerekkefølgen: obj307_01, lag002_01, lag017_03_del1av2, lag017_03_del2av2. Fem nye bildeverktøyforsøk totalt. Innebygd image_gen, modellnavn ikke eksponert. Python er brukt til egen alfa, presis plassering og grå ramme etter Toms tillatelse.

Alle fire egenkontroller er OK. Den strengere objektkontrollen fra smhd.gpt.check_pieces og piece_problem er også kjørt med originalobjektenes masker fra work/extract. Alle elleve objekter i de tre lagjobbene består. Egenkontrollen alene fanget ikke de opprinnelige objektfeilene.

| Jobb | Globalt skift | Største blokkskift | Kantlikhet | Utfall |
| --- | --- | --- | --- | --- |
| obj307_01 | 0,16 | 0,13 | 0,960 | OK |
| lag002_01 | 0,04 | 0,09 | 0,960 | OK |
| lag017_03_del1av2 | 0,32 | 0,63 | 0,918 | OK |
| lag017_03_del2av2 | 0,06 | 0,57 | 0,944 | OK |

Skift er i originalpiksler. Målene gjelder ferdige resultat.png. SHA-256, beskyttede kildehash og objektmålinger ligger i [leveranser.json](leveranser.json). Eksakt RGB128-ramme er kontrollert på alle lerretene. Ingen figurark er levert, så rutekart og figurregistrering er ikke aktuelt.

## Kildegrunnlag og presiseringer

ORDRE.md, BESTILLING.md, AGENTS.md, ANALYSE.md, GJENNOMGANG.md, NATT-HANDOFF.md og tidligere lapp-rapport er lest. CLAUDE.md finnes ikke her. Remake-skillen og HD-REMASTER-METODE.md er lest fra lokal main 1c4ff977. Originalene og relevante godkjente stilbilder er sett før hvert nytt forsøk.

Obj307 viser bare kikkertinnfatningens toppstripe. Det generelle romnotatet beskriver også myntsliss og panorama, som ikke inngår i denne ressursen. Presisering og begrunnelse er bevart i separate promptfiler; beskyttet prompt.txt er urørt. Forsøk 1 fikk FEIL etter at midtfeltets fasett ble glattet bort. Forsøk 2 bevarer de asymmetriske fargefeltene og består.

Obj896_01 er den tente gule indikatorlampen bak kontrollpulten. Tidligere levering hadde svart kuppel med oransje kant. Ny lampe gir kantlikhet 0,680 mot originalobjektet og 0,233 mot bakgrunnen. Før var tallene 0,885 og 0,955, som forklarer returen om manglende objekt.

Flaggene i lag017_03 vises som animasjonslapper i referansen. Tidligere jobbkompositter viste komplett flaggduk. Helbildet besto, men objektmaskene fikk 0,062 for rødt og minus 0,078 for grønt. Nye lappformer er tegnet med bildeverktøyet fra originalreferansen, med åpne himmelgap og separate prikker. Egen alfa er deretter hentet fra nye motivfarger, uten originalkonturmaske. Kantlikheten er nå 0,990 for rødt, 0,962 for gult og 0,956 for grønt.

Eksisterende komplett grafikk i rapporter/lapper-eske-logo-20261015/ er bevart. Denne runden leverer jobbkompositter og oppretter ikke et nytt objektleveranser.json som overstyrer heltegningene. Claude må fortsatt kontrollere samsvar mellom jobbkompositt, separat heltegning, faktisk lappklipp og motorens tegnerekkefølge ved import. Formatene kan ikke brukes om hverandre uten kontroll.

Propellfeltet kommer fra det nye fullbildeforsøket for del 2. Tre synlige bladretninger beholdes. Den tidligere rektangulære sømmen gjennom andehodet er fjernet. Resten av romgrafikken og eksisterende kontrollpult er bevart. [Plasseringsoppskrift](plassering.py.txt).

## Visuell kontroll og begrensninger

[Kontaktarket](returmotiver-kontaktark.png) viser original, forrige og ny levering i samme skala. En sammenligningsside per jobb viser også original, ny levering og 50 prosent overlegg. Bildene er visuelt gjennomgått. Små avrundinger og høylys er HD-tolkninger. Ingen nye landemerker, skilt eller figurer er innført.

Ingen import til hd-mod eller ny spilltest er kjørt. Tilstandsbytter, timing, full animasjon og overgangen mellom kikkertpanelets deler er ikke verifisert i motoren. Teknisk OK er ikke Toms godkjenning. Sam091 er ikke tegnet om.

## Sandkasse og overlevering

git pull --ff-only ble forsøkt og stoppet på skrivebeskyttet FETCH_HEAD i repoets felles Git-metadata. Ingen omgåelse. Arbeidet bruker filene ved oppgitt HEAD. Brukerens nattskript må committe leveringene og rapportmappen.

Systemets python3 mangler numpy. Eksisterende repo-miljø har numpy 2.5.4 og Pillow 12.3.0. Kontrollene er kjørt med PATH=/home/tom/Sam-Max-HD/.venv/bin:$PATH python3 verktoy/sjekk_leveranse.py og riktig jobbfil. Ingen installasjon eller shellendring utenfor repoet er gjort.

Alle 16 beskyttede filer for disse jobbene er SHA-256-kontrollert mot HEAD. Samlet git diff-kontroll finner ingen endring av beskyttede jobb- eller hovedarkfiler. Bare fire resultat.png, fire notat.md og denne rapportmappen er endret.

OPPDRAG-GPT.md i prosjektbiblioteket kunne ikke hentes via nettverktøyet, og undersøkt lokal sti finnes ikke. Den eksplisitte nattordren i chatten gir arbeidsgrunnlaget. PR32 er gjennomgått statisk fra lokal referanse; se [kodegjennomgangen](PR32-kontroll.md). Ingen kode er kopiert eller endret.
