# Fortsett med Astra i samme chat

Dette er et historisk overleveringspunkt før pilotens samlede commit. Samlet RAPPORT.md og Git-historikken viser senere levering. Den nye brukerautorisasjonen nedenfor gjelder fortsatt.

## Brukerens siste ordre

Tom: «veldig bra! godkjenner dette! sett inn i repo , fortsett med resten av HD konvertering». Deretter: «Continue with astra instead».

Dette er godkjenning av stilpiloten og autorisasjon til videre HD-grafikkproduksjon i samme prosjekt. Den nyere menneskelige ordren går foran stoppunktet i den eldre ORDRE.md. Ikke spør på nytt om samme arbeid eller per batch. Bruk innebygd ChatGPT-bildegenerator, ikke eksterne kredittjenester. Tom har allerede valgt og godkjent vanlig presis bildebehandling for skalering og plassering. Eksakt bildemodell er ikke eksponert og skal ikke påstås.

## Arbeidskopi og Git

- Canonical graphics: `/home/tombonator3000t/Dokumenter/ChatGPT/Sam&Max HD Remake/Sam-Max-HD/work/.gpt-gren`.
- Repo: `https://github.com/Tombonator3000/Sam-Max-HD.git`, gren `gpt-arbeid`.
- Siste push er `2b22fe7181faf35b4d975ec2c5897d6769e80dc4`, de presist rettede hovedarkene. Tom har godkjent begge.
- Fire nye pilotjobber og dokumentasjon er ferdige lokalt, men IKKE committet/pushet ennå. Fullfør denne leveringen først.
- Den ytre arbeidskopien er på `uttrekk-v6` og skal bevares. Aldri push grafikk til main. Ingen ny gren eller PR for grafikken.
- Eldre utrackede rawbilder i rapporter/hovedark-20261013, hovedark-retting-20261013/sam-generatorforsok-* og hele rapporter/stilpilot-20261013 er tidligere arbeid. Bevar dem og ikke ta dem blindt med i en ny commit.

## De fire ferdige pilotjobbene

| Jobb | Resultat SHA-256 |
| --- | --- |
| rom007_del1av2 | 00a82be6b79380c8f5ff1da07a3a43d39eead22aa81d111773514be40f1e3a82 |
| rom007_del2av2 | e1d9c0685e40e35f11a316bcc3b0a06463fba798b306a18d00c3d6e2d9aa26d9 |
| fig002_01 | 45b434f4b7f44b5e27ffa0b8ed5f05b819dde86b388913c2a26736d7744fda7d |
| fig003_01 | 20f125fce533fe320a2a1715221c912a6128b218832de03586f6360db506551d |

Hver jobb har `jobber/<jobb>/resultat.png` og `notat.md`. Rapportene ligger i denne mappen. `sluttkontroll.json` og `fremdrift.json` viser alle fire. Alle fire får OK i uendret egenkontroll. Alle 37 figur-rutebokser er eksakte ved alfa >=128; ingen ekstra figurkjerner utenfor rutene. Alle 18 låste kilde-/hovedarkfiler er uendret. Romoverlappen på 1120 x 800 er byte-identisk fordi begge leveransene er skåret fra samme konsistente 1952 x 800 fullscene. Topp/bunn er nøyaktig #808080.

Room raw: del1 forsøk01 er avvist på feil dørtekst/skrivebordsriss. Valgt del1 er forsøk02, del2 forsøk01. Fullscene og skjøt er sett visuelt av root og romagent, ingen vesentlige sikre semantiske feil. Bakvendt dørskilt, LO/VE-skilt, rot og skjeve former er bevart.

Sam raw hadde ett manglende øyelokkpar og for store/flyttede deler. Korreksjonen brukte nye genererte øyelokkformer, ikke oppskalert originalfallback. Pupillene er presist festet til originalplassene så blink faktisk lukker øynene. Lokal hudgradient fjernet plastereffekten. Root så kontaktark før siste fargeforbedring; se de oppdaterte `sam-blink-overlay.png` og `sam-blink-naerbilde.png` før levering. `sam-kropp-hode-kontaktark.png` viser riktig sammensatte hode/kropp/hender.

Max har 28 eksakte bokser. En feil magerring i front er erstattet med riktig detalj fra godkjent frontmaster. Pupiller og øyelokk er rettet tilsvarende Sam. Se `max-staaende-sammensatt.png`, `max-blink-kontroll.png`, `max-front-foer-etter.png`, `max-gange-kontaktark.png`, `max-tale-sammensatt.png` og `max-gange-diagnose.gif`. Max-agenten meldte alt teknisk og visuelt kontrollert, men forbindelsen brøt før sluttsvar/notat. Root har opprettet notat fra verifiserte resultater. Root må fortsatt se de siste Max-kontaktarkene før samlet levering.

## Kontroller og kildefunn

- Python med numpy/Pillow: `/home/tombonator3000t/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.
- Verifikasjonsoppskrift: `verifiser-pilot.py.txt`, original kjørekopi `/tmp/sammax-verifiser-pilot-20261013.py`.
- Sam har 9 ruter, men standardkontroll måler bare 7. Max har 28, standardkontroll måler 26. Øyelokkrutene er så små at skriptet hopper over dem; de er kontrollert separat.
- Lag4 512/513 er blink/øyelokk, ikke munn. Bevar to atskilte flekker. Kropp/hode/hender må ses samlet på originalens rel_x/rel_y.
- Max gang148–155 er helfigurer med hode. Ikke legg ståhodet oppå. `synlig` gir riktig geometri; `rekt` kan inkludere fjernet skyggetomrom.
- Ruteformatet i `rutekart-sam.json` og `rutekart-max.json` er bekreftet mot origin/main myk v4 (3df35f63).
- Deduplisert metadata beviser ikke originaltiming. GIF og kontaktark er tydelig merkede diagnoser, ikke motoravspilling.
- Ingen motorimport, spilltest eller ny HD-mod er utført. Ikke kall disse trinnene bestått.

## Fullfør straks, deretter fortsett serien

1. Se de siste Sam/Max-kontaktarkene. Rett eventuelle vesentlige faktiske feil, uten å starte ny stilutforskning.
2. Lag samlet RAPPORT.md/forhåndsvisning, oppdater GRAFIKKLISTE.md med de fire leveransene, rydd gammel slutttekst som sier at hovedarkene venter på godkjenning, oppdater relevant todo og logg. Ikke endre Claude-eide status.csv eller beskyttede jobb/sourcefiler. TOMS-GODKJENNING.json registrerer brukerens nye autorisasjon.
3. Commit og push kun denne øktens jobbresultater/notater, nye rapportmappe og relevante godkjennings-/statusdokumenter til gpt-arbeid. Kontroller GitHub-bytes/SHA og at beskyttede kilder er uendret. Rapporter kort til Tom, men ikke avslutt hele oppdraget ved dette delsteget.
4. Fortsett resterende 2260 jobber etter rekkefølgen i GRAFIKKLISTE.md, med brukerens godkjente hovedark og pilotrom som stilgrunnlag. Undersøk eksisterende format for stilankere før du legger dem inn; ikke gjett og ikke endre beskyttede jobbfiler. Bruk egne notater/supplerende prompter hvis et gammelt premiss er feil.
5. Generer avgrensede batcher med ett innebygd bildekall per asset, inspiser motiv/tilstander, kontroller alle ruter, korriger reelle feil, noter prompt/kilde/hash/rutekart og push i prosjektets passende batcher. Batchgrenser er ingen ny godkjenning. Bruk subagenter til uavhengig analyse/QA når det hjelper, men én eier per fil.

Les gjeldende AGENTS.md, BESTILLING.md, ANALYSE.md og relevante skills. Bevar roller og arbeidskopier, ikke skriv motor-/pipelinekode uten et faktisk kodeoppdrag. Grafikkproduksjonen skal fortsette på den autoriserte retningen; den er ikke ferdig bare fordi stilpiloten er levert.
