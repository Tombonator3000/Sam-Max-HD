# To nye helikopterfaser i fig178_02

Fase 2009/H082 og 2007/H085 er laget, egenkontrollert, native mottatt i lokal kandidat og observert i motoren. Begge native og hele motorbilder er visuelt sett. Publisering dokumenteres separat i mottak-publisert.json. Ingen ny Tom- eller Claude-godkjenning. Fire faktiske innebygde image_gen-kall H082..H085 gir tre nye råbilde-deler direkte brukt i to ferdige spritebilder.

Delarket er 1536 x 1024 med ekte alfa, nå 3/24 med tidligere 2008/H065 uendret. Delarket har SHA256 c10f760ab1f05357db633273a1963fb8a776decebd7259936d68d58fd81a0efe. Det ligger som fig178_02-delresultat.png med SHA-festet rutekart. Ingen hel jobb/resultat.png er levert. Hele figurjobber er fortsatt 508/1758, 1250 uten resultat, i tillegg til returer og sluttkontroll. Familien har 15/102 native i kandidaten, tidligere 13/102. Kandidaten har 3716 native, grunnlaget 3714.

| Fase | Sammensetning av egne tegnede deler | IoU | Dekning | Native SHA256 |
| --- | --- | --- | --- | --- |
| 2009/H082 | Ny H082-venstre + tidligere egen H080-høyre etter global blåkalibrering | 0,965 | 0,984 | fb4ea1934415953dd9785b7b487254db8998ecc53a55f32b02fbe76573dc35e2 |
| 2007/H085 | Ny H084-venstre + ny H085-høyre | 0,851 | 0,923 | f1a7be3c48613f3eb06ad9ee9b213b7b7a2fc9369919729481d276d3bc4ff2ff |

Originalene er sett hele i dokumentert spillkontekst med 0 RGB565-avvik og 0 opake indeks13. Det godkjente hovedarket til Sam og de faktiske originalene er sett før motivene. Dette er de synkende, delvis bortklipte helikopterfasene fra spillet. De skal beholde nettopp de synlige delene i hver fase. Testavspillingen plasserer dem kontrollert i rom 35. Den beviser riktig tegning og plassering i denne konstruerte situasjonen, ikke en naturlig full gjennomspilling av hendelsen.

Den nye arbeidsmåten tegner en hel uavhengig, atskilt gruppe om gangen i image_gen. Python kodedekoder egne farger, renser bare egen svak alfa under 8 og plasserer hele egne grupper i en tidligere egen tegning. Gruppestørrelser og posisjoner kommer fra egne tidligere bildegrenser. Kilden åpnes først etter sammensetningen for helplassering og kontroll. Ingen hard originalmaskeklipp, originalfragmenter, lokal påmaling eller flytting av enkeltrekk. Dette er en endring fra tidligere forsøk som redigerte hele motivet i ett kall. Det er ikke gjenbruk av originalens pikselmaske.

Ved nedskalering av de egne gruppene bevares kode-RGB kategorisk og egen alfa premultiplisert; kanters RGB hentes fra nærmeste egen kjerne. Alle egne kjernepiksler med alfa minst 128 er med før skalering. Kildepalett og originalen brukes til etterfølgende kontroll, ikke til lokal tegning. Hele H080-høyregruppen er bytebevart før siste helplassering i 2009. I 2007 kommer begge gruppers piksler fra de nye H084/H085-råbildene. H055 bidrar bare med egne lerretsmål og egne gruppegrenser, ingen gamle piksler i sluttgrafikken.

H083s høyregruppe hadde tre gale toppfelt og er et mellomresultat som er erstattet av H085. H084s tidlige helprototype med H083-høyre er en retur. H084s venstregruppe er derimot brukt i valgt H085. Disse to statusene skal ikke blandes. Tidligere H080 er fortsatt en retur som helsprite; bare dens gode egne høyregruppe brukes i den nye 2009-sammensetningen.

For H085 løser én samlet flytting [0,-1] HD tre randpiksler i ren kodeflatekontroll. Begge egne grupper flyttes likt. Forrige native og kontroll før flyttingen er bevart. Det nye faktiske alfaoverlappet er IoU 0,851 og dekning 0,923, ikke de gamle verdiene 0,945/0,976 før endelig måling. Alle tekniske porter, kildebekreftede smådeler, åpninger, nativefarger og rene kodefester består uendret grense på 3 HD. Ingen egne rene kodepiksler ligger mer enn 3 HD utenfor tilsvarende kildeflate.

Kildeløs replay gjenlager begge egne RGBA-PNG og begge native-PNG med eksakt SHA256 uten å åpne originalbilder eller bruke kildekoordinater for delplassering. Beviset og råbildefestene ligger i kildelos-replay.json og kall/*/. Faktiske prompter og image_gen-argumenter ligger ved hvert av de fire råbildene. Ingen CLI/API-bildefallback er brukt.

Original egenkontroll gir tre riktige ruter og 21 tomme mål, forventet exit 2. Ingen produsert rute har FEIL. Automatisk mottak av de to nye rutene gir 2 OK og 0 SJEKK. Den automatiske eksporten brukes som diagnostikk; bare de to særskilt SHA-festede egne nativefilene er tatt inn. Alle tidligere modfiler er kontrollert før kandidatbygging. Tidligere 2008-piksler og nativehash er uendret.

To ferske kontrollerte motoravspillinger med den faktisk nedlastede Linux-binæren 4e32ae906ee610e1383b98143301b9aa17b01b726cd61efdf7ac441de36165bf sammenligner 3714 og 3716 ved rom 35, aktør 29, kostyme 178, animasjon 1, posisjon 160,60 og zclip0. Begge gir 160 kontroller, 148 null og 120/120 null etter frame 40. Tolv kjente inngangsavvik er eksakt identiske i koordinater og begge RGB-verdier. Originalrektangler med 8 HD naboområde er identiske. Ingen uforklarte HD-endringer. Atomisk lagring består. 4102 og 5182 HD-piksler endres i henholdsvis 2009 og 2007 sitt aktørrektangel.

Begge hele motorbilder, begge komplette før/etter-par, begge native, hele delarket, gråbakgrunnstavlen og alle 24 utvalgte sekvensfaser 1998..2021 er faktisk visuelt sett. 53 kildefaser er logget. Dette er ikke alle 102 familieruter eller naturlig full gjennomspilling. Ny interaktiv Windows-test og ny webtest er ikke utført. Motor og pipeline er uendret; lokale hjelpefiler arkiveres bare som py.txt i grafikkrapporten.

Bibliotekskildene er losninger/grafikk/figurark-fast-storrelse.md og losninger/bygg/publisert-mod-er-fasit.md. Eksisterende smhd.myk-helplassering og additiv publisering gjenbrukes med fersk fjern-SHA og full filhashkontroll. PASS i kildenes opphavsprosjekt er ikke tatt som lokal godkjenning.

Felles Linux/Windows helikopter-utgave har fortsatt 3713 native og vil mangle tre etter denne publiseringen. Begge pakker oppdateres ved neste komplette ark-/familiesamlepunkt eller avslutning med faktisk nedlasting, sjekksummer og innholdskontroll. Dette delarket er ikke et nytt pakkesamlepunkt. Ingen gammel nattprosess startes. Automatikken er ACTIVE og all grafikk er ikke ferdig.

Publisert hd-mod 42d9d9c1044f493a8f972126329bf1832814ca5b har 3716 native. Grafikkilde er gpt-arbeid 56f31cea06ee81430d4c957a2a014aea7be31cae. Alle 21960 publiserte filhash er hentet tilbake og kontrollert. Alle 21958 tidligere stier og 21952 tidligere PNG er bevart. 1472 beskyttede input og tre opprinnelige stasher er uendret. Lokal mods/gpt er atomisk mottatt fra det verifiserte arkivet; 3714-grunnlaget er bevart under out. Bare to nye SHA-festede native er lagt til, og tidligere 2008 er bytebevart. Alle 47 eksisterende releaser og fire fellesvedlegg er bevart. Ingen aktive pakkebygg eller nativefrys ved publiseringen.
