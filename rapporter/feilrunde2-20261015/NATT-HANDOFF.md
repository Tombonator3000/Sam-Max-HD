# Grunnlag for Claude og Codex i nattløpet

Tom opplyser at Claude skriver Linux-skriptet for å jobbe etter tur og kontrollere hverandre. Dette dokumentet er en konkret overlevering til det løpet. Det oppretter ikke en egen kjøring.

1. Hent siste main, `gpt-arbeid` og kodegrenen `codex/hd-masker-inventory`. Motorrettingen er uttrykkelig tillatt av Tom i denne feilrunden. Behold den generelle rollefordelingen ellers.
2. Gjennomgå PR-en, særlig palettmaskene i klassiske kostymer, objektlag under native RGBA-kort, fade og fart. Patchen bygger mot den uendrede `engine/SCUMMVM_COMMIT`. Ikke kopier til Dig uten egen kompatibilitetsvurdering og riktig repoautorisasjon.
3. Importer Sam-arkene med [rutekart-sam.json](rutekart-sam.json). Lokal prøve ga 18 OK og ingen til sjekk. Kontroller frontkroppene i kostyme 2 og 4 separat i spillet.
4. Hent 111 filer fra det oppdaterte [ikonmanifestet](../ikoner-ui-20261015/ikonmanifest.json), ikke den eldre samle-ZIP-en. Bevar egen alfa. Kantvasken endrer RGB, ikke alfa eller mål.
5. Gjenskap inventar og masker med de lokale testoppskriftene fra rapporten. De krever tilpassede lokale stier og egne lagringskopier. `DIGHD_VERIFY=1` med null bufferavvik er ikke alene visuell godkjenning.
6. Prioriter de uløste tilfellene: øks/rom22; kranhode154 og Chicken Dumpling155 i rom16; faktisk opptak i kontoret med riktig kamera; bilens avreise; Sam/hammer i Wak-A-Rat. Kontroller hvilke tilstander spilllogikken faktisk viser. Tvungne tilstander kan overstyres av aktive skript.
7. For bakgrunn/lapp-feil: sammenlign bare rombakgrunn, originalens lappmasker og komplette malte tilstander. Fjern ikke malte feil med en stadig bredere kantmaske. Codex kan levere avgrensede motiver etter riktig original; Claude kontrollerer mottak og sammensetting.
8. Etter godkjent kode og grafikkmottak: publiser ny HD-mod, bygg Linux og Windows og oppdater nettmotoren. Noter kode-SHA, mod-SHA og pakketid, slik at Tom kan se hvilken pakke han tester.

[Rapporten](RAPPORT.md) skiller det som er verifisert, det som bare er teknisk importkontrollert, og det som fortsatt feiler. Nye resultater er ikke visuelt godkjent av Tom.
