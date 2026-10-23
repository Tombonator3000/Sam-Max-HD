# WebP-omlegging og lagringsrydding, 23. oktober 2026

Motorstøtten er flettet via PR 36 og installert lokalt. Alle 4 872 fargebilder i modden er tapsfri WebP. 17 089 indeks- og maskebilder er beholdt byte for byte som PNG. Alle 3 723 native ruter er bevart. Figurproduksjonen er fortsatt 508 av 1 758 jobber med resultat.png.

- Kode: `4d9f1e46b85cd431e6e03571ecda319755ea8151`.
- CI-kode før fletting: `62479addbe8fcca10e92fe3f518aa5757f2e3b1a`.
- Native: `15835538ca4b4e70e95a0f227e7d41bea830400e`.
- PNG-forelder: `2ba07d9cb94c99053fd0e97b0dfab903f3b01aff`.
- Grafikkgrunnlag før formatbyttet: `fb494a4ecb01dfed56efb2e62ae4253e7fd0c740`.

Moddens samlede filstørrelse går fra 499 900 803 til 368 373 643 byte, inkludert ny migreringsrapport og sjekksummer. Full kontroll omfatter alle RGBA-byte i 530 782 192 piksler, også RGB under alfa 0, samt dimensjoner, VP8L-format, filhashene og PNG-indeksene. Ingen bilder er skalert, tegnet om eller kvantisert.

Felles utgivelse: [Linux og Windows, tapsfri WebP](https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/sam-max-hd-2026-10-23-webp). Utgivelsen er publisert, ikke utkast. Alle fire filer er hentet tilbake og kontrollert; taggen peker på kode-SHA-en over. Nettmotoren er også publisert på https://tombonator3000.github.io/Sam-Max-HD-Web/.

## Kontrollnivå

- Laget: WebP-representasjon og motorstøtte. Motivenes piksler er uendret.
- Egenkontrollert: full RGBA- og SHA-256-kontroll, med rutekart i `rutekart-webp.tsv` og komplett komprimert migreringsmanifest.
- Native mottatt: alle 21 968 publiserte filer hentet som faktisk GitHub-nedlasting og SHA-256-kontrollert. TAR ble ikke beholdt på disk.
- Visuelt sett: native motorbilder fra rom 7, 9 og 35 samt bildet fra den nedlastede Linux-pakken. Kontrollert oppsett med testaktør, ikke full naturlig gjennomspilling.
- Motorobservert: 18 identiske bildepar med hele PNG-/WebP-modden. Endelig CI og lokal prøve ga 63 identiske par ved likt originalt spillbilde. Den installerte motoren lastet ti WebP-bilder og hadde seks sene skjermkontroller uten avvik. Linux-pakken lastet 21 WebP-bilder i 160 bilder fra et lagret spill i rom 35. Windows har bestått faktisk oppstart i Actions.
- Nettleser: publisert motor, JavaScript og komplett kildearkiv er lastet ned og hashkontrollert. Motorloggen viser WebP-rommet lastet og bilde 200 nådd. Skjermbildet lot seg ikke hente gjennom nettleserverktøyet, så nettleseren er ikke merket visuelt sett.
- Publisert: begge pakker, deres sjekksummer og alt faktisk inkludert modinnhold er kontrollert. De fire filene i fellesutgivelsen er deretter lastet ned som strømmer og sammenlignet med de inspiserte pakkene.
- Tom-/Claude-godkjent: tidligere stilstatus er uendret. Formatkontrollen gir ingen ny stilgodkjenning.

Den første CI-prøven sammenlignet samme rendernummer og fikk fire avvik i rom 35. De opprinnelige flatbildene var ikke i den første artefakten, så årsaken kan ikke bekreftes entydig i ettertid. SCUMM bruker også forløpt tid til animasjon. Sluttprøven velger derfor bildepar utelukkende etter lik original RGBA-tilstand, deretter krever den at alle HD-piksler er identiske. Den velger aldri par etter likhet i HD-bildet. Endelig lokal prøve og CI hadde 63 par, ingen utelatte originaltilstander og ingen avvik. De opprinnelige kontrollene er beholdt for revisjon.

## Sletting og gjenoppretting

6 240 044 eksakte filer fra 293 gamle modkopier er fjernet etter SHA-256-kontroll mot beholdt PNG-grunnlag. 145 gamle arkivkopier er fjernet etter kontroll av alle medlemmer eller mot fast publisert utgivelse. Dette omfatter 141 arkiver i hovedryddingen og fire gamle pakkekopier med egen kvittering i `siste-gamle-pakkearkiver-fjernet.json`. 257 507 motorbildekopier er fjernet etter bytekontroll mot en beholdt identisk fil. 53 461 unike gamle motorbilder ble beholdt. Den gamle aktive PNG-modkopien ble fjernet etter kontroll av alle 21 967 filer mot Git-forelderen, verifisert ny nedlasting og vellykket kjøring av den installerte motoren.

`SLUTTSTATUS.json` oppgir faktisk ledig filsystemplass før og etter. Observert økning ved avslutning er 180.9 GB, fra 117.4 til 298.3 GB tilgjengelig. Logiske filstørrelser og frigjort fysisk plass er forskjellige på btrfs med delte utstrekninger. Originale jobbgrunnlag, råbilder og de tre stashene er bevart.

Gamle out-modmapper er nå ufullstendige historiske arbeidskopier. Bruk gjeldende hd-mod som utgangspunkt for nytt arbeid. De fjernede filene kan gjenopprettes slik:

1. Pakk ut `beholdt-png-grunnlag.json.gz`. Dets SHA-256 skal stemme med `baseline_sha256` i `slettede-duplikater-bitkart.json.gz`.
2. Sorter filstiene i grunnlagets `files`. Bitkartet bruker nullbasert indeks, laveste bit først. En satt bit betyr at filen under den oppgitte roten ble fjernet. Hent den opprinnelige PNG-filen fra Git-forelder `2ba07d9...`, og kontroller SHA-256 fra grunnlaget.
3. `slettede-motorbildekopier.jsonl.gz` viser hvilken identisk kopi som ble beholdt for hvert motorbilde. `beholdte-unike-bildehasher.json.gz` er oppslag for de unike bildene.
4. `arkivrydding-status.json` viser faste releaseadresser og medlemkontroll. `slettede-arkivmedlemmer.jsonl.gz` viser beholdt kilde for hvert medlem i de fjernede TAR-filene. Arkivmedlemmenes innhold er bevart; den gamle TAR-serialiseringen trenger ikke gjenskapes byteidentisk.
5. `webp-migration.json.gz` og `rutekart-webp.tsv` binder gammel fil og SHA-256 til ny fil, SHA-256 og identisk RGBA-hash. De historiske grafikkrapportenes PNG-SHA-er peker fortsatt på den bevarte Git-forelderen.

## Videre produksjon

Automatkjøringen er fortsatt ACTIVE med samme 20-minutters intervall og har fått regler for WebP og rydding. Gjenoppta den påbegynte figurproduksjonen etter siste fremdrift og retur. Originale jobbformater beholdes. Native fargebilder leses også fra .webp. Bruk én nødvendig kandidat per bunke, verifiser ny konvertering og publisering, og fjern verifiserte fullkopier og dobbeltlagrede nedlastinger etterpå. `docs/WEBP.md` beskriver formatbyttet. Den eldre `tools/mod_gren.sh send` force-pusher og skal ikke brukes til additiv publisering.
