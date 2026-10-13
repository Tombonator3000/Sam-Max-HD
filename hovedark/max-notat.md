# Hovedark for Max

Rettet 2026-10-13 16:31 (norsk tid) av Codex. Visuelt godkjent av Tom 2026-10-13 som hovedreferanse for resten av stilpiloten.

## Verktøy og grunnlag

Tegningene kommer fra ChatGPTs innebygde bildegenerator. Eksakt modellnavn ble ikke eksponert. Tre genereringer. Valgt originalforsøk: 2. Ingen ny bildegenerering i den presise rettingen.

Tom valgte 13. oktober «Ja bruk presis skalering og plassering» og ba om å fortsette i denne chatten. Hver av de fem valgte tegningene er skalert og flyttet samlet med vanlig bildebehandling i Pillow. Lanczos med premultiplisert alfa bevarer myke kanter. Separat skalering langs x og y korrigerer sideforholdet mot originalboksen. Det er ikke tegnet på nytt, speilvendt eller maskert etter originalens pikselkontur.

Kildene er `hovedark/max/referanse.png`, `original_1x.png`, `prompt.txt` og `jobb.json`. Mål og plass beregnes fra `plassering` og `bokser` i `jobb.json`, ganger fire. Sam er hundedetektiven i blågrå dress og hatt. Max er den nakne kaninlignende figuren. Riktige hovedkostymer er 2 og 3, med nærbilder fra 27 og 28. Originalreferansene har prosjektets korrigerte normalpaletter. `ANALYSE.md` og Purcell-føringene er videreført. Beskyttede kilder er uendret.

## Kontroll

PNG, RGBA, 1536 x 1024, ekte alfa. 93.1 prosent av lerretet har alfa under 16. Fem separate visninger: forfra, høyre, bakfra, venstre og ansiktsnærbilde.

Egenkontroll: **OK** for alle fem visningene. Full kontrollutskrift ligger i `rapporter/hovedark-retting-20261013/egenkontroll.txt`. Kontrollen ble kjørt med appens medfølgende Python og prosjektets uendrede `verktoy/sjekk_leveranse.py`.

Utvidet måling kontrollerer også bredde og plassering. Alle boksene nedenfor er nøyaktig like ved alfa minst 128, i lerretspiksler `[x, y, bredde, høyde]`.

| Visning | Bestilt boks | Målt boks |
| --- | --- | --- |
| 1 | [264, 408, 136, 208] | [264, 408, 136, 208] |
| 2 | [432, 408, 144, 208] | [432, 408, 144, 208] |
| 3 | [608, 408, 124, 208] | [608, 408, 124, 208] |
| 4 | [764, 408, 144, 208] | [764, 408, 144, 208] |
| 5 | [940, 416, 328, 200] | [940, 416, 328, 200] |

Målinger, transformasjoner og kildehash ligger i `rapporter/hovedark-retting-20261013/presis-kontroll.json`. Kontaktarket `rapporter/hovedark-retting-20261013/sammenligning-max.png` viser original 4x, før og etter med samme utsnitt og skala. Visuell kontroll bekrefter at alle fem valgte tegninger er bevart, at fotlinjer og ytre bokser følger originalmålene, og at alfakantene er myke. Boksene beviser ikke samsvar for alle indre konturer eller ansiktsdetaljer.

Tom godkjente de to rettede hovedarkene 2026-10-13 med «Disse er bra, fortsett med resten». `visuelt_godkjent=true` gjelder hovedarket med ferdig SHA-256 nedenfor, levert i commit `2b22fe71`. Dette er en godkjent visuell hovedreferanse og autorisasjon til resten av stilpiloten. Full serieproduksjon venter på godkjenning av den samlede stilpiloten. Ingen motorimport, animasjonsavspilling eller publisert HD-mod er utført. Hovedarket er ikke en animasjonsleveranse. De øvrige pilotjobbene er ikke utført i denne rettingen.

## Sporbarhet

Før retting: `8e562e60240f6caa7c7d46749af17c01ab57cb5267d6bfd14f6cd1f216fdc2ab`. Kildetegningen finnes uendret i commit `09905c32` og som `rapporter/hovedark-retting-20261013/max-for-presis.png`.

Ferdig SHA-256: `8533bebbd672f6cdaeb03e0ad88548321c94e85b60796141d92f71a8ae1b95a4`.
