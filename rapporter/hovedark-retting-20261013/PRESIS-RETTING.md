# Presis retting av hovedarkene

Tom ba 13. oktober 2026 om å fortsette rettingen i denne chatten og valgte «Ja bruk presis skalering og plassering». Dette godkjenner vanlig bildebehandling av de allerede leverte Sam- og Max-kandidatene.

## Grunnlag og avgrensning

Kildene er de beskyttede `hovedark/sam/`- og `hovedark/max/`-filene. Geometrien beregnes fra `plassering` og `bokser` i hver `jobb.json`, ganger fire. `retteplan.json` bevarer planen fra forrige chat. Kildetegningene er leveransen fra commit `09905c32`, med SHA-256 låst i planen. De bevares også som `sam-for-presis.png` og `max-for-presis.png` i denne rapportmappen.

Sam er hundedetektiven, hovedkostyme 2, med brun pels, lang snute, blågrå dress og hatt, hvit skjorte, stripet mørkeblått slips og bare føtter. Max er den nakne kaninlignende figuren, hovedkostyme 3, med kremhvit pels, lange ører, store føtter og bredt glis. Begge ark viser forfra, høyre, bakfra, venstre og et ansiktsnærbilde fra kostyme 27 og 28. Originalreferansene bruker prosjektets korrigerte normalpaletter. Nærbildenes scenebakgrunn er ikke del av de transparente kandidatene.

Dette er en geometrisk retting av de valgte tegningene. Ansikt, drakt, strek og uttrykk tegnes ikke på nytt. Hver visning skaleres samlet, slik at hode, kropp og hender følger samme transformasjon. Ulik skalering langs x og y retter kandidatenes avvikende sideforhold. Det gjøres ingen maskering etter originalens pikselomriss, speiling eller rotasjon.

## Metode og kontroll

Hver tegning isoleres med transparent marg rundt sin målte alfakjerne. Skalering bruker Pillow med Lanczos og premultiplisert alfa, slik at myke kanter beholdes og usynlig bakgrunnsfarge ikke blør inn. Den skalerte alfakjernen måles på nytt ved alfa minst 128 og plasseres i originalens boks. Eventuell justering for avrunding dokumenteres i `presis-kontroll.json`.

Resultatene kontrolleres med prosjektets uendrede `verktoy/sjekk_leveranse.py`, separat måling av alle ti bokser, sammenligning med originalene på kontaktark og kontroll av at beskyttede kilder ikke er endret. Kontrollfiler og ferdige hashverdier legges i denne mappen.

Teknisk OK og kontroll av plassering er ikke Toms godkjenning av designet. Motorimport, animasjonsavspilling og HD-mod er ikke del av denne rettingen. Hovedarkene leveres fortsatt som pilotkandidater.

## Resultat 2026-10-13 16:31

Alle ti bokser stemmer nøyaktig med originalen ved alfa minst 128. Prosjektets egenkontroll gir OK for begge arkene. Kontrollutskriften er `egenkontroll.txt`. Myke kanter er bevart, og alle beskyttede kildefiler har samme SHA-256 før og etter.

Original, før og etter er visuelt sammenlignet i `sammenligning-sam.png` og `sammenligning-max.png`. Samlet forhåndsvisning er `sam-og-max-rettet.png`. Geometrien er rettet; forskjeller i indre silhuett, ansiktsuttrykk og strek mot originalen er fortsatt del av pilotkandidaten som Tom vurderer.

Den eksakte bildebehandlingsoppskriften er bevart som `bildebehandling-oppskrift.py.txt`. Det er en sporbar kopi av engangskjøringen, ikke en endring av spillets kode eller pipeline.
