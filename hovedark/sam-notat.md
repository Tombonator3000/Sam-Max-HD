# Hovedark for Sam

Rettet 2026-10-13 16:31 (norsk tid) av Codex. Visuelt godkjent av Tom 2026-10-13 som hovedreferanse for resten av stilpiloten.

## Verktøy og grunnlag

Tegningene kommer fra ChatGPTs innebygde bildegenerator. Eksakt modellnavn ble ikke eksponert. Fem opprinnelige genereringer og ett senere avvist generatorforsøk, seks totalt. Valgt originalforsøk: 4. Ingen ny bildegenerering i den presise rettingen.

Tom valgte 13. oktober «Ja bruk presis skalering og plassering» og ba om å fortsette i denne chatten. Hver av de fem valgte tegningene er skalert og flyttet samlet med vanlig bildebehandling i Pillow. Lanczos med premultiplisert alfa bevarer myke kanter. Separat skalering langs x og y korrigerer sideforholdet mot originalboksen. Det er ikke tegnet på nytt, speilvendt eller maskert etter originalens pikselkontur.

Kildene er `hovedark/sam/referanse.png`, `original_1x.png`, `prompt.txt` og `jobb.json`. Mål og plass beregnes fra `plassering` og `bokser` i `jobb.json`, ganger fire. Sam er hundedetektiven i blågrå dress og hatt. Max er den nakne kaninlignende figuren. Riktige hovedkostymer er 2 og 3, med nærbilder fra 27 og 28. Originalreferansene har prosjektets korrigerte normalpaletter. `ANALYSE.md` og Purcell-føringene er videreført. Beskyttede kilder er uendret.

## Kontroll

PNG, RGBA, 1536 x 1024, ekte alfa. 89.8 prosent av lerretet har alfa under 16. Fem separate visninger: forfra, høyre, bakfra, venstre og ansiktsnærbilde.

Egenkontroll: **OK** for alle fem visningene. Full kontrollutskrift ligger i `rapporter/hovedark-retting-20261013/egenkontroll.txt`. Kontrollen ble kjørt med appens medfølgende Python og prosjektets uendrede `verktoy/sjekk_leveranse.py`.

Utvidet måling kontrollerer også bredde og plassering. Alle boksene nedenfor er nøyaktig like ved alfa minst 128, i lerretspiksler `[x, y, bredde, høyde]`.

| Visning | Bestilt boks | Målt boks |
| --- | --- | --- |
| 1 | [224, 372, 192, 280] | [224, 372, 192, 280] |
| 2 | [448, 372, 160, 280] | [448, 372, 160, 280] |
| 3 | [640, 372, 180, 280] | [640, 372, 180, 280] |
| 4 | [852, 372, 160, 280] | [852, 372, 160, 280] |
| 5 | [1044, 444, 268, 208] | [1044, 444, 268, 208] |

Målinger, transformasjoner og kildehash ligger i `rapporter/hovedark-retting-20261013/presis-kontroll.json`. Kontaktarket `rapporter/hovedark-retting-20261013/sammenligning-sam.png` viser original 4x, før og etter med samme utsnitt og skala. Visuell kontroll bekrefter at alle fem valgte tegninger er bevart, at fotlinjer og ytre bokser følger originalmålene, og at alfakantene er myke. Boksene beviser ikke samsvar for alle indre konturer eller ansiktsdetaljer.

Tom godkjente de to rettede hovedarkene 2026-10-13 med «Disse er bra, fortsett med resten». `visuelt_godkjent=true` gjelder hovedarket med ferdig SHA-256 nedenfor, levert i commit `2b22fe71`. Dette er en godkjent visuell hovedreferanse og autorisasjon til resten av stilpiloten. Full serieproduksjon venter på godkjenning av den samlede stilpiloten. Ingen motorimport, animasjonsavspilling eller publisert HD-mod er utført. Hovedarket er ikke en animasjonsleveranse. De øvrige pilotjobbene er ikke utført i denne rettingen.

## Sporbarhet

Før retting: `a00c29a5ad3e1bab9be9dcb22ee866cd37b8cf04f379a9ca0f19a644919d1980`. Kildetegningen finnes uendret i commit `09905c32` og som `rapporter/hovedark-retting-20261013/sam-for-presis.png`.

Ferdig SHA-256: `3318856a0d8aee78be150b4cd223398a65c189e0c5e5929db22b5023ad9a2c7f`.
