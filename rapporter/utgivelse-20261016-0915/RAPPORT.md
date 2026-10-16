# Oppdatert Linux-pakke og nettmotor, 16. oktober 2026

Tom ba om oppdatert Linux-utgave på repoet og spurte om nettutgaven også hadde rettingen. PR32 ble flettet av Tom klokken 09:00, commit 74ab2af2. Begge utgavene er bygget fra denne commiten, med nattens pipelinekode fra PR33 med i main.

- [Linux-pakken](https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/linux) er publisert klokken 09:11, etter vellykket oppstartstest og Debian 12-test. Bygg 38864950569. AppImage er lastet ned på nytt, sjekksummen består, og BYGG.txt bekrefter kode 74ab2af og hd-mod a6c286bd. Pakken har 76 rom, 959 objektbilder, 113 native objektbilder og 1095 native figurruter. Den avviste munndelen costume249_257 er fortsatt utelatt som native, med indeksbilde til originalbasert visning.
- [Nettutgaven](https://tombonator3000.github.io/Sam-Max-HD-Web/) er bygget og publisert i kjøring 38865040675. Utsjekket kildecommit er kontrollert i byggeloggen, 19 nettsidetester består, og den faktisk publiserte WASM-filen er lastet ned. SHA-256 stemmer med build.json og er forskjellig fra motoren som lå ute før oppdateringen. Nettsiden henter grafikken fra hd-mod ved oppstart. Ingen faktisk spilling i nettleseren er utført i denne kontrollen.

## Spillprøver av den nedlastede Linux-pakken

Den uendrede motoren og modden fra AppImage er kjørt med kopier av de tidligere testlagringene. Brukerens innstillinger, lagringer og spillprosess er ikke endret. Alle tre scener avsluttet med kode 0. Alle målte bilder hadde 0 forskjell mellom skjermbufferen og full gjenoppbygging. Dette beviser ikke at alle malte motiver og animasjoner er riktige. Z-kantmålingene er fortsatt ikke null.

- [Inventaret](inventory.png): åpnet ved bilde 80 og lukket ved bilde 160, totalt 280 bilder. Native kort har rene kanter uten de tidligere rosa/grønne mattepikslene. Eskens myke kant er synlig.
- [Akvariet](akvarium.png): 240 bilder i rom 16. Max og Sam vises bak grønt glass uten det tidligere rosa/blå feltet.
- [Cafeteriarøret](cafeteria.png): 240 bilder i rom 30. Blått glass og Max inni røret vises uten rosa flate.

To første lokale kjøringer stoppet før spillet var lastet, med SDL_BlitSurface/NULL surface under GUI-oppstart med SDL dummy. Vindusmodus alene fjernet ikke feilen helt. Den fullførte kontrollen brukte vindusmodus, innebygd GUI-tema og én prosess om gangen. Dette er testinnstillinger, ikke endringer i pakken. CI testet vanlig pakkeoppstart og Debian 12 separat. De mislykkede lokale forsøkene er bevart i den lokale kontrollmappen.

Gjenværende arbeid: bakgrunns-/øksestillinger i rom 22, alle faktiske bevegelser til kranhodet og Chicken Dumpling, et vellykket opptak, bilens avreise og andre hele animasjonsforløp. Windows-pakken er ikke bygget i denne runden.

Konkrete sjekksummer og kildehenvisninger står i [utgivelse.json](utgivelse.json). [Kontrollresultater](kontroll.json), prøveskript og de tre spilloggene er bevart her. Ingen nytegning, bildepikselendring, rutekartendring eller ny import er utført.
