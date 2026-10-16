# Fire grafikkjobber 16. oktober 2026

Grafiker: Codex. Gren gpt-arbeid. Ingen commit, push, grenbytte, PR, fletting eller kodeendring. Nattkjøringen håndterer commit.

Git pull ble forsøkt før produksjon, men Git-metadata ligger utenfor sandkassens skrivbare område. Feilen var read-only på FETCH_HEAD. Arbeidet bruker allerede tilgjengelig ordre, oppdatert 06:06 norsk tid. Arbeidstreet var rent ved start.

Lest: ORDRE.md, AGENTS.md, BESTILLING.md, ANALYSE.md, GJENNOMGANG.md, NATT-HANDOFF.md og rapporter/lapper-eske-logo-20261015/RAPPORT.md. CLAUDE.md finnes ikke her. Remake-skillen er lest fra lokal main med git show main:docs/skills/scumm-hd-remake/SKILL.md, særlig motivavklaringen. Imagegen-skillen er lest fra den installerte systemskillen. Ingen ekstra agenter er brukt.

## Rekkefølge og utsatte jobber

Fig247_02 er rettet først etter retur.md. Deretter ble lag083_01 til 04 hoppet over, og neste avklarte jobber i ordren ble fig247_10, fig247_11 og fig116_01.

Lag083_01 til 04 krever godkjent rom083 i ordren. Rom083 står fortsatt som sjekk i status.csv. Det viktigste hinderet er dessuten det kjente feilpremisset: rom83 lagrer grafikk som brukes med rom54-palett i bassengscenen. Referanser/prompt for skybildene er derfor ikke riktig produksjonsgrunnlag. Den eksisterende bassengrapporten leverer allerede separate komplette motiver for objekt833, 834 og 836; objekt835 har fortsatt uavklart bart kontra åpen munn. Ingen ny gjetning eller duplisering er gjort. Claude bør fjerne disse fire jobbene fra køen eller gi en korrigert, kildeavklart bestilling basert på runtime54-grunnlaget når Tom har avklart objekt835.

## Leveranse og kontroll

Fire ark, 22 ruter, statisk visuell egenkontroll på alle fire. Tre ark OK. Fig247_02 SJEKK på den samme eldre omrissmerknaden for siste rute. Ingen FEIL. Se fremdrift.json, rutekart og separate egenkontrollfiler.

Fig247_02: bare de grønne båndenes RGB er endret. Hele alfaen er bitidentisk med det avviste førbildet. To grønne bånd per hjelm, svart mellom båndene og eksisterende grønt visir. Sam, Max, grep og fire kabelfaser er bevart. Sammenlignet med originalen og hjelmfargene på fig247_01, fig247_03, fig247_04 og fig247_05. Originalens grønne bånd er fasit; tidligere HD-ark alene gir ikke fargegodkjenning.

Fig247_10 og 11: promptenes generiske omtale av begge figurer og fedora er korrigert separat. Sam løfter og slipper VR-hjelmen, og fedoraen avdekkes under den. Max er ikke synlig i disse rutene. Fig247_10 fikk ett ekstra bildeforsøk for det pressede ansiktsuttrykket i tredje rute. Alle øvrige hode-/hjelmtilstander, grep, synlige hatter og kabelkurver er sammenlignet statisk. Ingen påstand om avspilling, tempo eller godkjente overganger.

Fig116_01: originalens alligatorer og Sam er avklart med docs/figurer.csv i lokal main og rom25-konteksten. De grønne alligatordelene er ikke gress. Luftbåren midtrute mangler riktig nok alligator. Originalens små isolerte pikselrester er beholdt på sine koordinater med fargeprøver fra nytegningen, uten å dikte opp en identitet. De frakoblede større alligatordelene har egne plasseringsbokser.

Bildeverktøyet lager også svak alfahaze utenfor tegningene. Denne er fjernet ved å isolere nytegningens egne alfakomponenter, med myke kanter. Originalen er ikke brukt som produksjonsmaske. Python er brukt innenfor Toms uttrykkelige tillatelse til rensing og presis plassering. Returrettingen endrer ingen eksisterende alfapiksler.

Systemets python3 mangler numpy. Eksisterende prosjektvenv med numpy, Pillow og scipy er brukt uten installasjon. Det samme verktoy/sjekk_leveranse.py er kjørt. Alle 16 beskyttede filer for de fire jobbene er SHA-kontrollert uendret.

Levert: 4. Statisk visuelt kontrollert: 4. Importert i denne økten: 0. Motoravspilt: 0. Godkjent av Tom: 0. Ingen pipelinekode eller motorretting er gjort. PR32-kontrollen er ikke gjentatt.
