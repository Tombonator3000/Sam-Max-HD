# Kontoret, del 2 av 2

Levert 2026-10-13 av Codex som stilpilotkandidat. Tom har godkjent hovedarkene, men har ennå ikke vurdert dette rombildet. Ingen motorimport eller spilltest er utført.

## Kilde og motiv

Sam og Max sitt kontor, rom 7, med bevisst rot og skjev geometri. Jobbens `referanse.png`, `original_1x.png`, `jobb.json` og `prompt.txt` er bevart uendret. Utsnittet dekker originalens x=104 til 487 og y=0 til 199. Kontoret er totalt 488 x 200 originalpiksler.

Delens vinduer, lamper, TV, dartskive, skrivebord, stol, mat og skrivemaskin er sammenlignet med del 1 og originalen. Høyresidens rifle med bajonett, figur med røde klær, hodeskalle, bein og svart rekvisitt på hyllen, rød rosett, lilla rund gjenstand og mørkt skoddefelt er bevart. Skiltet nederst i det smale åpne skapet viser **LOVE**, fordelt på LO og VE. Små rekvisitter er vurdert etter originalens former, uten å hevde sikrere identitet enn kilden gir.

## Verktøy og forsøk

Bildet er nytegnet med ChatGPTs innebygde bildegenerator. Eksakt modellnavn er ikke eksponert av verktøyet. Det ble gjort 1 genereringsforsøk for denne delen. Råbildet er bevart som `rapporter/stilpilot-fortsettelse-20261013/rom007_del2av2-forsok-01.png`, med brukt prompt i samme rapportmappe. Del 1 ble brukt som ekstra referanse for felles innhold og stil; del 2 sin original styrer høyresidens innhold og geometri.

Pillow er brukt til vanlig bildebehandling etter genereringen. Det valgte bildet og del 1 er satt sammen til én fullscene på 1952 x 800 uten skalering eller geometrisk transformasjon. En 128 piksler bred smoothstep-overgang ligger ved fullscenens x=912 til 1039, midt i overlappen. Begge sluttbilder er deretter skåret fra samme fullscene. Ingen semantisk retusj eller originalmaske er brukt.

Leveransen er RGB PNG, 1536 x 1024. Bildet ligger ved x=0, y=112 og har størrelse 1536 x 800. Øvre og nedre gråbånd er nøyaktig #808080 og 112 piksler høye. Overlappen med del 1 er byte-identisk: del 1 x=416 til 1535 og del 2 x=0 til 1119, begge y=112 til 911.

## Kontroll og status

Uendret `verktoy/sjekk_leveranse.py` er kjørt med prosjektets tilgjengelige Python-runtime. Utfall: **OK**, skift 0,08 originalpiksler, største blokkskift 0,09 og kantlikhet 0,98. Dette er teknisk egenkontroll, ikke visuell godkjenning.

Original, råbilder, fullscene og skjøt er gjennomgått visuelt. Ingen vesentlige, sikkert påviste semantiske feil ble funnet. HD-piloten har glattere og lysere malte flater enn originalen; stil og små tolkninger gjenstår for Toms vurdering.

SHA-256 for `resultat.png`: `e1d9c0685e40e35f11a316bcc3b0a06463fba798b306a18d00c3d6e2d9aa26d9`.

Mål, kildehash, råfiler, fremgangsmåte og leveransehash er dokumentert i `rapporter/stilpilot-fortsettelse-20261013/rom-sammenstilling.json`. Reproduserbar Pillow-kode ligger i `rom-sammenstilling.txt`, og kontrollutskrift i `rom-egenkontroll.txt`. Se også `kontor-for-etter.png`, `kontor-helrom-kontaktark.png` og `kontor-skjot-kontaktark.png` i rapportmappen.
