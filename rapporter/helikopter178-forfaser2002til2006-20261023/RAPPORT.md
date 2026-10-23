# Helikopterfase 2005 og 2006

To nye hele spritebilder i fig178_02 er laget, egenkontrollert, native mottatt i lokal kandidat, visuelt sett og motorobservert. Publiseringskvitteringen kommer i mottak-publisert.json. Ingen ny Tom-/Claude-godkjenning. Sju faktiske innebygde image_gen-kall H086..H092 gir to valgte spritebilder. Verktøyet oppgir ikke modellnavn. Ingen CLI/API-bildefallback er brukt.

Delarket er nå 5/24 på hele 1536 x 1024 med ekte alfa. Tidligere 2007/H085, 2008/H065 og 2009/H082 er bytebevart. Ingen hel jobb/resultat.png leveres. Hele figurjobber er fortsatt 508/1758, 1250 uten resultat, i tillegg til returer og sluttkontroll. Familien har 17/102 native i 3718-kandidaten, grunnlaget hadde 3716 og 15/102. Planlagte 2002..2004 ble ikke nytegnet i denne bunken.

Originalene er sett hele i dokumentert spillkontekst med den faktisk nedlastede 4e32ae90-Linux-binæren. Kildene har 0 RGB565-avvik og 0 opake indeks13. Riktig original og godkjent Sam-hovedark er sett før hvert motiv. Dette er de delvis bortklipte helikopterfasene; ingen komplett ny helikopter skal tegnes. Kildens avkuttede og synlige deler beholdes i sin fase.

Begge kilder er én sammenhengende alfagruppe. De nye redigeringsmodulene er rektangulære deler av vår egen tegning, ikke påstått atskilte kildegrupper. Skjøten velges fra medianen av tynneste egne alfakolonner innen 20..40 prosent av egen bredde. Hele nye moduler plasseres etter egne tidligere grenser. Et åtte råpikslers bredt bånd fra vår egen tidligere hals bevares i skjøten. Kildeutsnitt brukes bare som bildeguiding til image_gen og senere kontroll. Ingen kildekoordinater brukes til delplassering, ingen hard originalpikselmaske klipper ny tegning, og ingen originalfragmenter brukes.

2005/H090 bruker H088-venstre og H090-høyre, med egen skjøt og plasseringsmål fra H087. H088s navykode leses globalt som 71grå, fordi denne venstremodulen ikke har noen kildebekreftet opak svart. Egen alfa og geometri er uendret. H089s høyre er kun mellomresultat; H090 retter det ene feilaktige blå/navy-feltet. Alle andre felt og de små 239-oransje, oliven- og grønntonene er bevart i sluttkontrollen.

2006/H092 bruker H091-venstre og H092-høyre, med egen skjøt og plasseringsmål fra H086. En samlet flytting [1,1] HD, høyre og ned, retter noen randpiksler. Begge moduler og skjøten flyttes likt. Det faktiske nye alfaoverlappet er IoU 0,857 og dekning 0,931. Verdiene 0,957/0,987 før flyttingen er historikk. Det er ikke foretatt lokale form- eller fargeflyttinger.

Global egen kode-RGB-rens og svak egen alfa under 8 bevares. Egne kjernepiksler med alfa minst 128 beholdes før plassering; alfa er uendret ved fargerens. Kjerneerosjon 7 ble prøvd som global egen RGB-diagnostikk for H086/H087 og avvist. Den valgte kjernen er 3. Begge varianter er bevart. Nye modul-RGB skaleres kategorisk, egen alfa premultiplisert, og kant-RGB kommer fra egen kjerne. Ingen originalmasker brukes i dette arbeidet.

Begge valgte ruter består alle alfa-, åpnings-, nativefarge- og rene kodefester innen uendret 3 HD. Ingen egne kodepiksler ligger mer enn 3 HD utenfor riktig kildeflate. Kildeløs replay gjenlager både egne RGBA-PNG og native-PNG med eksakte SHA256 uten å åpne originalbilder. H086/H087/H089 er returer som hele prototyper. Fire nye moduldeler og to egne smale skjøter fra seks råbilder bidrar med piksler til sluttgrafikken. Det sjuende råbildet, H089, brukes bare som redigeringsreferanse.

Original egenkontroll gir 5 OK og 19 tomme mål, forventet exit 2. Ingen produsert rute har FEIL. Automatisk mottak av de to nye rutene gir 2 OK og 0 SJEKK. Den automatiske eksporten er bare diagnostikk. Bare de to egne særskilt SHA-festede nativefilene tas inn. Alle tidligere modfiler og alle tre gamle delruters RGBA er kontrollert før bygging.

To ferske kontrollerte motoravspillinger med faktisk nedlastet Linux-binær 4e32ae906ee610e1383b98143301b9aa17b01b726cd61efdf7ac441de36165bf sammenligner 3716 og 3718 i rom 35, aktør 29, kostyme 178, animasjon 1, posisjon 160,60 og zclip0. Begge gir 160 kontroller, 148 null og 120/120 null etter frame 40. Tolv kjente inngangsavvik er eksakt like i koordinater og begge RGB-verdier. Originalrektangler med 8 HD naboområde er identiske. Ingen uforklarte HD-endringer. Atomisk lagring består. 6269 og 5908 HD-piksler endres i henholdsvis 2005 og 2006 sitt aktørrektangel.

Begge hele motorbilder, begge komplette før/etter-par, begge native, hele delarket, gråbakgrunnstavlen og alle 24 utvalgte sekvensfaser 1998..2021 er faktisk visuelt sett. 53 kildefaser er logget. Dette er ikke alle 102 familieruter eller naturlig full gjennomspilling. Ny interaktiv Windows-test og ny webtest er ikke utført. Ingen motor-/pipelinekode er endret; lokale hjelpefiler er bare arkivert som py.txt i grafikkrapporten.

Bibliotekskildene er losninger/grafikk/figurark-fast-storrelse.md og losninger/bygg/publisert-mod-er-fasit.md. Eksisterende helplassering og additiv publisering gjenbrukes med fersk fjern-SHA og full filhashkontroll. PASS gjelder opphavets tester; de to nye rutene er kontrollert lokalt.

Felles Linux/Windows helikopter-utgave har fortsatt 3713 native og vil mangle fem etter denne publiseringen. Begge faktiske pakker oppdateres ved neste komplette ark-/familiesamlepunkt eller avslutning med nedlasting, sjekksummer og faktisk inkludert grafikk kontrollert. Ingen gammel nattprosess startes. Automatikken er ACTIVE og all grafikk er ikke ferdig.

Delark SHA256: 648b414179d682351eff8fa0208caf65b71a074c8d7b50e61f0daeeed2a6b109

Native costumes/costume178_2005_hd.png SHA256 f31b5d3ab40b8fe3e6b46ede6afc1b0e009528fab62c79c3787a5042c93c562b; IoU 0.964, dekning 0.977.

Native costumes/costume178_2006_hd.png SHA256 0b0f2365df832184b1e9de038cfbb2a92f5efb78cd56397638276b39058c9c9e; IoU 0.857, dekning 0.931.

Publisert hd-mod c2ef7ebebedd515ae3a60a5e2591ab7ff34c10a5 har 3718 native. Grafikkilde er gpt-arbeid ae6c8fe9340db326f28a8d900779b27908364115. Alle 21962 publiserte filhash er hentet tilbake og kontrollert. Alle 21960 tidligere stier og 21954 tidligere PNG er bevart. 1472 beskyttede input og tre opprinnelige stasher er uendret. Lokal mods/gpt er atomisk mottatt fra verifisert arkiv, og 3716-grunnlaget er bevart under out. Bare to nye native er lagt til. Alle 47 eksisterende releaser og fire fellesvedlegg er bevart. Ingen aktive pakkebygg eller nativefrys ved publiseringen.
