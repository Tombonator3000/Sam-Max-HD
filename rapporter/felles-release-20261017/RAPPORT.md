# Felles Linux- og Windows-release, 17. oktober 2026

Tom ba om å hente og samle alt laget arbeid, legge Linux sammen med Windows og fortsette grafikken. Main og gpt-arbeid er hentet med fast-forward. Ingen åpne kode-PR-er. Ingen motorkode er endret i denne runden.

Begge pakkene er bygget fra main 6c181dec og hd-mod 5212c395. Linux 39020147979 og Windows 39020149118 er grønne. Linux har bestått oppstart og Debian 12; Windows har bestått oppstart med HD og MT-32. Begge nedlastinger har SHA-256 lik publiserte sjekksummer. Alle 19 531 runtime moddfiler i hver pakke er byteidentiske med publisert modd og hverandre. 1290 native figurruter, 76 rom og 959 objektbilder.

Første lokale manifestassert stoppet fordi repoets README.md manglet i pakken. Begge eksisterende pakkeskripter fjerner denne dokumentasjonsfilen med hensikt, tools/pakke_linux.sh:49 og tools/pakke_windows.sh:57. Kontrollskriptet utelater nå bare dette bestemte dokumentet og krever fortsatt identisk filsett og alle filhasher. Ingen grafikkfil er utelatt eller endret for å bestå kontrollen.

Den uendrede, nedlastede Linux-motoren er kjørt med pakkens spill og modd, minimal ini, gfx-mode=normal, builtin GUI, dummy lyd/skjerm og null musikk. Brukerens saves og innstillinger er ikke rørt; kopierte lagringer og egne HOME-/XDG-mapper brukes. Inventar 280 bilder, akvarium 240, cafeteriarør 240, Sam opp ned med blinking 160 og tale 160. Alle fem avslutter normalt, gir skjermbilder og har 99 skjermbufferkontroller uten avvik. Alle fem prøvebildene er sett. Rene inventarkort, grønt akvarium og blått rør uten rosa felt i disse prøvene; Sam blinker uten brune T-merker/svarte ender. Synlige grunnmotiv-/bakgrunnsrester og originalbaserte figurer står fortsatt i scenene. Z-kantmålingene er ikke null. Ikke naturlig full gjennomspilling eller interaktiv Windows-spilling.

Sam opp ned viser de samme rutenumrene som i lokal QA; costume204_286 er fortsatt ikke observert, men PNG-en er kontrollert. Nytegningen har ikke separat Claude-kontroll eller Toms nye stilgodkjenning. De dokumenterte omrissmerknadene, kunstig rom49-hopp og øvrige returer står åpne. 118 av 1758 figurjobber har resultat, 1640 mangler. Neste Sam-ark er fig307_01 til 05, deretter fig312_01 til 02. Natt-automatikken forblir pauset.

Fire filer ble først lastet opp i draft. Filstørrelser og GitHubs SHA-256-digest er kontrollert mot de lokale filene før publisering. Deretter publisert med Latest og kontrollert via releases/latest. De eldre releasene er bevart.

Publisert 2026-10-17 11:25 norsk tid: https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/sam-max-hd-2026-10-17

Se release-notater.md, moddfiler-kontroll.json, linux-kontroll.json, byggmetadata, sjekksummer, skjermbilder og motorlogger i denne mappen. Grafikkildene og mottakskvitteringene står i rapporter/fortsett-20261016-kveld og rapporter/opp-ned-20261016.

De fem motorloggene er bevart byteidentisk i motorlogger.zip; ingen logglinjer er renset for Git.
