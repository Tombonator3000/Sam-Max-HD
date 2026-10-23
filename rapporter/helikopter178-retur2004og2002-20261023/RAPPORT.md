# Returene for helikopterfase 2004 og 2002

To nye hele sprites i fig178_02 er laget, egenkontrollert, native mottatt i lokal 3721-kandidat, visuelt sett og motorobservert. Valgt er 2004/H103 og 2002/H110. Publiseringskvitteringen følger i mottak-publisert.json. Tom og Claude har ikke gitt ny godkjenning. Åtte faktiske innebygde image_gen-kall H103..H110 er bevart med råbilder, eksakte prompter, verktøyargumenter og inputhash. Verktøyet oppgir ikke modellnavn. Ingen CLI/API-bildefallback er brukt.

Delarket er nå 8/24, fortsatt på 1536 x 1024 med ekte alfa. Alle seks tidligere delruter 2003 og 2005..2009, deres RGBA og nativehash er bevart. Ingen hel jobb/resultat.png leveres. Hele figurjobber er fortsatt 508/1758, 1250 uten resultat, pluss returer og sluttkontroll. Familien 178 har 20/102 native i 3721-kandidaten. Åtte bildekall er ikke åtte leverte figurjobber.

Begge riktige hele originaler er sett i spillkontekst med den faktisk nedlastede Linux-binæren 4e32ae90. Kildene er tidligere RGB565-bekreftet med null avvik og null opake indeks13. Godkjent Sam-hovedark er sett før hvert motiv. Motivet er de kildebestemte delene av helikopteranimasjonen. Avskjæringene og alle små fargefelt/åpninger beholdes. Gamle egne returer er bare redigeringsmål, aldri stilankere.

2004/H103 bruker ny H103-høyre og den tidligere egne H094-venstre, med et åtte råpikslers smalt skjøtebånd fra egen H093. Den manglende gjennomsiktige cellen 33,11 er nå gjenopprettet av image_gen. Den er et eget lite hull under og til venstre for det store vinduet. Forrige prototype hadde fylt hele cellen, og feilen var større enn en avrundet kant. En markert bildeforklaring gjorde det mulig å rette riktig hull. Alle eksisterende farger og den store åpningen er beholdt.

2002/H110 bruker ny H110-venstre og egen H109-høyre, med et åtte råpikslers skjøtebånd fra egen H076. Tre små åpninger i venstre skjøt og røde/brune felt i den utstrakte armen er rettet av image_gen. Mellomrettingene mistet enkelte hvite, lilla og grå felt; disse er gjenopprettet før mottak. H105, H107 og H109 er returer som hele prototyper. H109 bidrar bare den hele egne høyremodulen. H104, H106 og H108 er avviste venstremoduler og bidrar ingen sluttpiksler.

Begge kilder er én sammenhengende alfagruppe. Redigeringsmodulene er rektangulære deler av egne tegninger. Skjøten bestemmes fra egne alfakolonner, og hele nye moduler plasseres etter egne tidligere grenser. Originalen brukes til bildeguiding, samlet helplassering og kontroll. Ringer og inverse koordinater i rettingsguidene er bare referanser til image_gen. Ingen kildekoordinater brukes til delplassering eller ferdige piksler. Ingen originalmasker klipper ny grafikk, ingen kildefragmenter, lokal fargepåmaling eller flytting av enkeltrekk er brukt. Ringene finnes ikke i sluttgrafikken.

Global egen RGB-koderens og svak egen alfa under 8 er brukt. Egne alfa128-kjernepiksler bevares før plassering. ModulRGB skaleres kategorisk, og egen alfa premultiplisert. Ingen ekstra lokal fargekalibrering eller helflytt er anvendt. Begge ruter består alle alfa-, åpnings-, nativefarge- og rene kodefester innen uendret 3 HD, med null egne kodepiksler over 3 HD utenfor riktig kildeflate. Kildeløs replay gjenlager begge egne RGBA-PNG og native-PNG byteeksakt fra egne råbilder uten å åpne originaler. Tre nye råbilder og tre tidligere egne råbilder bidrar sluttpiksler; tre nye moduler og to gamle smale skjøter.

Original egenkontroll gir 8 OK og 16 tomme mål, forventet exit 2. Ingen produsert rute har FEIL. Automatisk mottak gir 2 OK og 0 SJEKK. Automatisk eksport er diagnostikk og importeres ikke. Bare de to SHA-festede egne nativefilene legges til 3719-grunnlaget. Alle 21963 tidligere filer og alle seks tidligere delruters RGBA er kontrollert før bygging.

To ferske kontrollerte motoravspillinger med den faktisk nedlastede Linux-binæren 4e32ae906ee610e1383b98143301b9aa17b01b726cd61efdf7ac441de36165bf sammenligner 3719 og 3721 i rom 35, aktør 29, kostyme 178, animasjon 1, posisjon 160,60 og zclip0. Begge har 160 kontroller/148 null og 120/120 null etter frame 40. Tolv kjente inngangsavvik er identiske i koordinater og begge RGB-verdier. Originalrektangler med 8 HD naboområde er identiske. Ingen uforklarte HD-endringer, og atomisk lagring består. Andre aktører og romskript kjører.

Begge native, hele delarket, gråbakgrunnstavlen, begge hele motorbilder, begge komplette før/etter-par og 24 sekvensfaser 1998..2021 er faktisk visuelt sett. 53 kildefaser er logget. Dette er ikke alle 102 familieruter eller naturlig full gjennomspilling. Ingen ny interaktiv Windows-/webtest. Ingen motor-/pipelinekodeendring; lokale hjelpefiler er arkivert som py.txt i grafikkrapporten.

Bibliotekskilder: losninger/grafikk/figurark-fast-storrelse.md og losninger/bygg/publisert-mod-er-fasit.md. Eksisterende helplassering og additiv publisering gjenbrukes med fersk fjern-SHA og full filhashkontroll. PASS gjelder opphavets tester; rutene er kontrollert lokalt. Alle 1472 beskyttede input og tre opprinnelige stasher skal bevares ved publisering.

Felles Linux/Windows helikopter-utgave har fortsatt 3713 og vil mangle åtte etter publisering. Ingen pakkedispatch ved dette 8/24-delarket. Begge faktiske pakker oppdateres ved neste komplette ark-/familiesamlepunkt eller avslutning med nedlasting, sjekksummer og faktisk grafikkinnhold kontrollert. Ingen nødvendig Tom-designavklaring er identifisert. Automatikken er ACTIVE og all grafikk er ikke ferdig.

Delark SHA256: 0ddbb14c35256c75d06db3d9911b2cd13f5d40dc96791794839603d84d64a6e6

costume178_2004 native SHA256 e2875cebc4c77b24193651b9bef173c193a0d0531ea7aab09f2caa30b00c5379, IoU/dekning 0.99/0.996, 6590 endrede synlige HD-piksler i motorrektangelet.

costume178_2002 native SHA256 4b74cc4c036afe46a295291bcc9aa4bffd4bce7edace7e1bd3cb0b6e28bf7639, IoU/dekning 0.953/0.974, 7399 endrede synlige HD-piksler i motorrektangelet.
