# Kontoret, del 1 av 2

Levert 2026-10-13 av Codex som stilpilotkandidat. Tom har godkjent hovedarkene, men har ennå ikke vurdert dette rombildet. Ingen motorimport eller spilltest er utført.

## Kilde og motiv

Sam og Max sitt kontor, rom 7, med bevisst rot og skjev geometri. Jobbens `referanse.png`, `original_1x.png`, `jobb.json` og `prompt.txt` er bevart uendret. Utsnittet dekker originalens x=0 til 383 og y=0 til 199. Kontoret er totalt 488 x 200 originalpiksler.

Dørens innvendige, bakvendte bokstaver er beholdt. Lampene, vinduene, TV og antenne, telefon/svarer, dartskive med fire røde piler, bilderammer, hull, skrivebord, stol, papirer, mat og skrivemaskin er sammenlignet med originalen. Små originale streker skal ikke leses som ny tekst eller fullføres til nye objekter.

## Verktøy og forsøk

Bildet er nytegnet med ChatGPTs innebygde bildegenerator. Eksakt modellnavn er ikke eksponert av verktøyet. Det ble gjort 2 genereringsforsøk for denne delen. Forsøk 2 er valgt og bevart som `rapporter/stilpilot-fortsettelse-20261013/rom007_del1av2-forsok-02.png`. Prompter og det første forsøket ligger i samme rapportmappe.

Pillow er brukt til vanlig bildebehandling etter genereringen. Det valgte bildet og del 2 er satt sammen til én fullscene på 1952 x 800 uten skalering eller geometrisk transformasjon. En 128 piksler bred smoothstep-overgang ligger ved fullscenens x=912 til 1039, midt i overlappen. Begge sluttbilder er deretter skåret fra samme fullscene. Ingen semantisk retusj eller originalmaske er brukt.

Leveransen er RGB PNG, 1536 x 1024. Bildet ligger ved x=0, y=112 og har størrelse 1536 x 800. Øvre og nedre gråbånd er nøyaktig #808080 og 112 piksler høye. Overlappen med del 2 er byte-identisk: del 1 x=416 til 1535 og del 2 x=0 til 1119, begge y=112 til 911.

## Kontroll og status

Uendret `verktoy/sjekk_leveranse.py` er kjørt med prosjektets tilgjengelige Python-runtime. Utfall: **OK**, skift 0,04 originalpiksler, største blokkskift 0,08 og kantlikhet 0,98. Dette er teknisk egenkontroll, ikke visuell godkjenning.

Original, råbilder, fullscene og skjøt er gjennomgått visuelt. Ingen vesentlige, sikkert påviste semantiske feil ble funnet. HD-piloten har glattere og lysere malte flater enn originalen; stil og små tolkninger gjenstår for Toms vurdering.

SHA-256 for `resultat.png`: `00a82be6b79380c8f5ff1da07a3a43d39eead22aa81d111773514be40f1e3a82`.

Mål, kildehash, råfiler, fremgangsmåte og leveransehash er dokumentert i `rapporter/stilpilot-fortsettelse-20261013/rom-sammenstilling.json`. Reproduserbar Pillow-kode ligger i `rom-sammenstilling.txt`, og kontrollutskrift i `rom-egenkontroll.txt`. Se også `kontor-for-etter.png`, `kontor-helrom-kontaktark.png` og `kontor-skjot-kontaktark.png` i rapportmappen.
