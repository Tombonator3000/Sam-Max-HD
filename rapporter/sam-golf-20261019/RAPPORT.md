# Sam med golfkølle, 19. oktober 2026

Fem komplette figurark er levert: fig110_01 til 04 og fig110_07. De gir 64 nye native ruter fra 25 ulike originalposer. Fig110_05 og 06 er ikke levert, se gjenstar.json. Kandidaten har 1654 native ruter og 19 890 PNG-er. Publisert gren og kildecommit kvitteres separat i mottak-publisert.json etter push og tilbakehenting. Felles nedlastingspakke har foreløpig 1546, 108 færre enn kandidaten.

## Grunnlag og tegning

Kostyme 110, format 0x61, rom 25, Gator Golf utslagsplassen. Spillets figurer.csv, GJENNOMGANG.md, alle sju originalark, begge hele originalkontaktark og Sam-hovedarket er brukt. Handlingens originaltilstander er sett i motoren før tegning. Sam bruker tynn sølvfarget golfputter. Han kaster slipset bak nakken før svingen; senere hvit skjortefront og blått stoff bak nakken følger kilden. Det godkjente hovedarkets vanlige slipstilling skal ikke overstyre handlingen.

Eksakt RGBA-gjenbruk mot 159 tidligere resultatjobber ga ingen treff. Eksakt like kilder i denne bunken er samlet i ruteplan-unik.json. Alle 41 ulike kilder og deres 92 mål er bevart i planen; bare de 25 ulike kildene til de fem komplette arkene er levert. Aliaser har identiske native-hasher. Ulike originalposer er ikke slått sammen.

Syv faktiske innebygde image_gen-kall: fem råbilder, ett avbrutt C01 uten funnet resultat og ett E-avslag. Fire råbilder, A/B/C02/G, brukes i leveransene. D er bare utkast. C02 bruker eksakt samme prompt som det avbrutte C01. F er klargjort, ikke bestilt. Eksakt modellnavn vises ikke. Faktiske prompter, input-SHA-er, råbilder og utfall står i bildekall.json. Ingen CLI/API-fallback.

Toms tillatelse til Python-rensing og plassering er brukt. Generert alfa beholdes og renses for dis, med myke kanter og rektangulær tilpasning til 4x-mål. Ingen hard original pikselmaske. Kildens hvite bevegelsesstreker i 1976 bevares, også syv små kildebekreftede utliggerpiksler i native mottak. Utilsiktede hvite riper inne i den genererte buksen i 1975 er renset uten alfaendring. Råfil og førbilder er bevart. Originalene 1942 og 1949 er like utenfor hoderektangelet [17,0,41,23]. HD-kroppen deles derfor, mens hvert hode beholder sin kildevinkel med myk overgang. Det hindrer at en kropp som er uendret i kilden hopper mellom hvilefasene. Se prototype-kvitteringer.json, C-bukserens.json og plasser-unike.py.txt.

## Kontroll

Egenkontroll: 64 OK, null SJEKK/FEIL. Native mottak v6: 64 OK, null til gjennomsyn eller manglende, uendrede grenser. Alle resultat-SHA-er og rutekart er kontrollert. 28 beskyttede kildefiler er byteidentiske. Alle 19 826 tidligere publiserte PNG-er og alle 19 832 tidligere filstier er beholdt. Bare mod.json endres i kandidaten. Tre eksisterende stasher er bevart.

Den faktiske nedlastede Linux-produksjonsmotoren fra 19. oktober, SHA c7b4e73c882ea999a55bb11b01f2fe3cabb17dcedc87859fae2255a876d821be, spiller fire animasjoner (1,7,8,9) i rom 25. Ingen lokal retningskrok eller motorendring. Grunnlaget ved 160/180 ga ingen avvik. Siste kandidat kjøres ved 80/180 for fri sikt fra de andre figurene: 260 kontroller, 224 fra figurstart, alle null. Alle 64 nye ruter er logget tegnet. Alle er visuelt sett mot original, native og faktiske motorutsnitt i seks kontaktark. Hele scener for start, baksving og retur er sett. Logg ved frame f vises i dump f+4. Før- og etterlogger for kroppssamordningen er bevart sammen med grunnlaget i motorlogger.zip, tolv logger med SHA-manifest.

Dette er egne tekniske og visuelle kontroller. Ingen naturlig gjennomspilling, interaktiv Windows-test, ny nettlesertest, ny Tom-godkjenning eller separat Claude-kontroll. De andre figurene i golfrommet er fortsatt originaler. Teknisk mottak og rutetelling er ikke en slik godkjenning.

## Åpent og videre

Bildeverktøyets outputkontroll avviste E med moderation_blocked, kategori other, request-ID 7bb75223-5f5b-465b-87e4-da8c8877a5e2. Samme avviste grunnlag bestilles ikke på nytt og erstattes ikke med andre poser. Fig110_05/06 står derfor åpne, 28 ruter. D-utkastets 1983 har også feil hoderetning og skal rettes før bruk; det er ikke native mottatt eller publisert. F er ikke kalt. Feilen og alt arbeid er bevart. Neste uavhengige bunke er fig152_01 til 06.

Direkte telling: 164 av 1758 figurjobber har resultat, 1594 mangler, i tillegg til returer og utestede helheter. Arbeidet er ikke ferdig. Oppdater felles Linux-/Windows-nedlasting ved dette samlepunktet med kontroll av nedlasting, sjekksummer og faktisk moddinnhold.

Bibliotekskilder: figurark-fast-storrelse og scumm-v6-kostymer-skygge-og-soppelruter for mål, skygger og lag; publisert-mod-er-fasit for additiv bevaring. PASS i opphavet er kontrollert på denne bunken med faktiske kilde-, kandidat- og motorresultater. Ingen produksjonskode endret.

## Publisering bekreftet

Kildecommit 5ed07eca694b7ce3c92d989c36f8951321d2cff9, hd-mod bd65ce87f0f690ac19aa1c316f376a2e23810193. Hentet tilbake og kontrollert: alle 64 nye SHA-er, alle 19 890 kandidat-PNG-er og alle 19 826 tidligere PNG-er stemmer. Alle gamle filstier bevart. Bare mod.json og generert SHA256SUMS endres. 1654 native bekreftet. Felles pakke har fortsatt 1546 til nytt bygg er kontrollert.

Senere samme kveld er felles Linux-/Windows-pakke med 1654 native publisert og kontrollert: ../felles-release-20261019-kveld/RAPPORT.md. Begge faktiske nedlastinger har alle 64 golfruter, alle nye SHA-er og hele moddinnholdet bekreftet.
