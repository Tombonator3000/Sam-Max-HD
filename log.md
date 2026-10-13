# Logg for konseptarbeidet

## 2026-10-12 20:02 (Codex)

- Tom ba om konseptbilder av hvert monster og analyse av navn, personer og objekter før HD-konvertering.
- Opprettet arbeidskopi av eksisterende gpt-arbeid under work/.gpt-gren etter fetch. Hovedarbeidskopien står fortsatt urørt på uttrekk-v6. Ingen produksjonsordre er aktivert.
- Leste prosjektreglene, gjeldende main-dokumentasjon og ferdighetene source-faithful-production, imagegen og prosjektets scumm-hd-remake. Dette er konseptforarbeid etter Toms nye bestilling, ikke serieproduksjon.
- Hentet grafikkfilene fra spilldata, kontrollert indeks-MD5 og gjort originaluttrekk. 348 kostymer, 16 052 bilder, 17 tomme ruter, 83 rom og 959 objektbilder. 0 dekoderfeil.
- Dekompilerte skriptene: 1179 uten feil, 2 kjente descumm-feil. Kopierte aktuelle skriptbevis og utvalgte 1x-originaler inn i konseptleveransen.
- Skilt Doug fra Trixie-kostymene i tilbakeblikket, servitøren med lilla turban fra kokken, Evelyn fra uidentifisert kostyme 254, og ekte Bigfoot fra Sam/Max-forkledningen. Uavklarte egennavn er beholdt som uavklarte.
- Laget 20 bilder med innebygget ChatGPT-bildegenerator, eksakt modellnavn ikke oppgitt. 4 første forsøk avvist på konkrete feil. 16 motivgrupper har nå konseptkandidat. 17 av de 33 foreløpig identifiserte motivgruppene mangler fortsatt konsept. Listen er ikke dokumentert komplett for alle skapninger i spillet.
- Rettet oppdiktet merke på Sams hatt, Max sin tannform, Lee-Harveys pikselkanter/feiltolkede bevegelsesstreker og ekstra hode i Bigfoot-drakten. Avviste forsøk ligger i avvist/, brukes ikke som referanse eller i galleriet.
- Viktig funn: ruter-listen i animasjonsmetadata dedupliserer rutekoder og mangler komplett timing/kontrollstrøm. Den er ikke tilstrekkelig for å godkjenne avspilling eller spritesheets. Motoravspilling eller komplett kommandostrøm må brukes før produksjon.
- Lagret galleri, figurnotater, prompter, SHA-256, 348-raders kostymetabell, 959-raders objektbildetabell og rutekart i konsept/2026-10-12/. SHA, antall og alle lokale gallerilenker er kontrollert.
- Full systemdisk stoppet først uthenting og metadata. Bare egne nye, regenererbare arbeidsfiler er flyttet til RAM under /tmp, uten å slette eksisterende brukerfiler. Utvalgte kilder og hele konseptleveransen er bevart i grenen. Bilder har harde lenker til generatororiginalene for å unngå dobbelt plassforbruk; ingen generatororiginal er fjernet.
- Diskplass-spørsmål er sendt til Tom. Ved siste kontroll var rundt 3,7 MB ledig. Resten av bildene krever mer plass.
- Ingen kodeendring i motor eller pipeline, ingen spillkjøring, ingen importert mod, ingen godkjenning fra Tom, ingen commit eller push. Leveransen er lokal og ikke ferdig for HD-produksjon.

## 2026-10-13 11:01 (Codex)

- Tom ba om analysen i Sam & Max, Zak og The Dig for senere grafikkarbeid. Lagt inn ANALYSE.md i gpt-arbeid og koblet fra AGENTS.md, uten å endre main eller beskyttede jobbfiler.
- Bevart DOTT-vedlegget, kildehash og datert guideavsnitt. Bigfoot-prøvene skal ha tynnere, mer variert strek; tilbakemeldingen er ikke spritesheet-godkjenning.
- Lagt inn Sam & Max-spesifikk Purcell-analyse og kildehenvisning. DOTT/Purcell skal ikke erstatte The Dig sine godkjente stilankere eller Zak sine personer/paletter.
- Full analyse fra Sam & Max 12. oktober er bevart som datert case med fungerende lenker til riktig spill. Tekniske tall overføres ikke mellom spill.
- Ingen ny bildegenerering eller spilltest i dokumentasjonsoppgaven. SHA-256, lokale dokumentlenker og git-diff kontrolleres før levering.
