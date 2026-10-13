# Uavhengig C-kontroll – bestilling 24

Alle ti siste resultatfiler er lest mot originalkontaktark, egne metadatafelt og levert rom007-del1-HD. Filhashene stemmer med a-leveranser.json; c-uavhengig-hashkontroll.json låser kandidatene som denne kontrollen gjelder. C har bare skrevet egne kontrollfiler, ingen jobbilder eller A-filer.

## Avgjørende åpent funn: rektangulær veggtone

067_01 i lag007_14 og 067_03 i lag007_20 har en synlig lysere/gråere rektangulær flate på veggen, med rette topp- og sidekanter fra innfellingen [544,392,144,72]. Dette sees i faktisk sistefil, ikke bare et gammelt kontaktark. Se c-antenne-static-narkontroll.png rad 1 og 3. Lag14 SHA `0bc4f8519886fc516fc9cbcb674f7d5d91ea213d4d91a093c4be32acd035f20c`; lag20 SHA `eec414429b928629aeb9b977228932c2aa8482018ecb146a6f5ef8f2df57f164`. Lag17 har vesentlig svakere overgang og ikke samme tydelige lyse panel i denne visningen.

067_03 mangler korrekt antenne og stamme, men fargelappen er et separat visuelt avvik selv om checker er OK. Funn meldt straks til root og A. A har bekreftet at kontaktarket viser siste kandidat. Root har bedt A rette sine egne 024-filer; C gjør ny etterkontroll når rettingen er klar. Disse to kandidatene er derfor ikke visuelt sluttklarert her.

Original067_03 er ikke identisk med originalgrunnrommet i feltet: 67 piksler endres i rombbox [136,64,167,87]. Levert HD-grunnrom har en stiplet antenne på samme vegg, så direkte tilbakekopiering av grunnfeltet vil gi feil tilstand. c-06703-grunnforskjell.json dokumenterer dette. En retting må bevare tom vegg uten å blande inn gamle antennerester. Ingen originalmaske eller lokal warp er nødvendig eller tillatt for denne oppgaven.

## Motiv-/tilstandskontroll

071_0C: venstre oransje/brune form har en bredere mørk nedre munn, blått nederst; høyre lyse profil har brun øyestrek. 071_0D: venstre svarte munn er mindre/kortere og det blå nedre feltet endres; høyre brune øyemarkering går over til svarte punkter/lys hud. Disse faktiske endringene kan sees i c-tv12-mikro.png og c-tv15-mikro.png. Figurformene er noe mindre på skjermen, mer avrundede og har mer glans/antialiasing enn originalen. Ingen navn eller filmidentitet er bevist. Det er konkrete tegningsforbehold, ikke en ny identitetsbestemmelse.

071_0D/0E/0F har identiske kildekompositter ifølge kildemålingen, og leveransene har samme SHA. Separate ressurs-ID-er/notater er bevart. Dette er korrekt kildebevist bildegjenbruk, ikke bevis om runtime-timing.

078_01 og078_02 har ulike grå/grønne oppstykkede, vertikale stripefordelinger. Det er ingen tilfeldig monokrom TV-snø eller ny tekst. 078_03, lag19, har de særskilte fersken/oransje øvre og sentrale stripene, grå brudd, grønt til sidene, rødt/brunt nederst og små blå rester nederst til venstre. De brede fargeområdene og signalbruddene stemmer visuelt; nye striper er jevnere, smalere og mer farget av skjermglans enn kildepikslene. Nærbildet ligger nederst i c-antenne-static-narkontroll.png. Jeg finner ikke et konkret motivbytte som alene tilsier avvisning, men 0,602296-kantkorrelasjonen er marginal og skal beholdes som presist forbehold; helbilde-OK er ikke begrunnelse for å utelate dette. Ingen ekstra teknisk margin eller runtime-verifikasjon hevdes.

067_01 og067_02 har to faktisk forskjellige løkkehellinger og kort stamme, ikke to dupliserte antenner eller stiplet erstatning. 067_03 har ingen antenne. Alle tre beholder grå/reflekterende tom TV-skjerm; farget071/078-motiv er ikke feilaktig kopiert inn under antennevariantene. Det åpne skjøtefunnet over gjelder bakgrunnstonen, ikke disse tilstandene.

## Bakgrunn, skjøter og teknikk

Separat bytekontroll viser null endringer utenfor egen metadatarekt i alle ti leveranser. Dermed følger telefon med rødt rør, standardvindu, dør, dartfelt og øvrig rom riktig grunnanker. TV-feltene viser ingen tydelig hard rektangulær bord-/kasseskjøt i de gjennomgåtte fullscenene etter A sin kantblanding. Antennefeltet har derimot fortsatt det konkret beskrevne panelavviket, som ikke skjules av gode korrelasjonstall.

Perobjektmålinger i A sin uendrede kontroll er faktisk utført for alle ti. Alle rapporterte utfall er OK, med svakest 078_03 0,602296, 071_0D/E/F 0,623236 og071_0C 0,642214. Ingen felter hoppes over. C har kontrollert manifesthashene og bakgrunnsgjenbruket separat; kontrollscriptet er ikke endret. Kandidatene er ikke importert eller testet i runtime av C, og ny individuell brukergodkjenning er ikke innhentet.

Status: motivfamiliene er vurdert med forbeholdene over. Lag14/20 avventer retting/etterkontroll av synlig fargelapp. Øvrige kandidater har ingen ny avgjørende tilstandsfeil funnet i denne gjennomgangen. Root avgjør samlet mottak.

## Etterkontroll etter A sin fargesammenpassing

A har rettet de tre antennefeltene med et jevnt additivt RGB-korreksjonsfelt beregnet mellom NYGENERERT utklipp og NYTEGNET HD-grunn. Ingen originalpiksler eller innhold fra den gamle antennen er kopiert inn. Metode, førfiler og mål er bevart i a-fargesammenpassing.py.txt/bevis.json.

Jeg har sett før/etter-nærbildene og siste fullscene for lag20. De lyse rektanglene i lag14/20 er nå visuelt borte; veggtonen fortsetter uten den tidligere rette panelgrensen. Antenne01/02 beholder forskjellige løkkeformer;06703 er fortsatt helt uten antenne/stamme. Det er ingen tilbakeblandet stiplet rest. Grå/tom TV-skjerm er bevart. Separat bytekontroll bekrefter at alt utenfor [544,392,144,72] er identisk med grunnrommet i alle tre; etterhash stemmer med A sitt bevis.

Nye SHA:
- lag007_14_del1av2: `2bf41036fc4c647d733ad6e75617e77d125da6f4bfbb30c3188b8c7f91b876cf`
- lag007_17_del1av2: `aad518e6c7ffe371bad884602fe12c105ffc1737ab15596204165f4c19070d54`
- lag007_20_del1av2: `dad0744657fc2f1258fa25d1a3770e9474c9fabb0d33a0c2e733377fd8b8f116`

Det konkrete skjøtefunnet er rettet. Tidligere avventende status for lag14/20 over er historikk og erstattes av denne etterkontrollen. Ingen avgjørende ny feil funnet; øvrige TV-/07803-forbehold beholdes uendret. Runtime/import og individuell brukergodkjenning er fortsatt uverifisert.
