# Kilde-QA, bestilling 13 A

Original1x, referanse4x, jobbmetadata og ordrette prompter er sett for alle fire objekter. Begge rom059-delene er sett før generering. GRUNNLAG og root-kildeplan er lest. Godkjent kontorpilot gir strek/pensel, ikke motiv.

Obj566_01 er dinosaur-wooly-mammoth i originalregisteret. Sammenligningen med rom059 viser den samme attraksjonsmodellen med mindre pels og avdekkede grå mekaniske side-/benformer. Pelskanter, grå bånd og naglemerker beholdes; ingen levende såret mammut, ny serviceluke eller oppfunnet mekanikk. Den avklipte venstre delen fullføres ikke.

[LucasArts-hintboken](https://www.mocagh.org/lucasfilm/sammax-hintbook.pdf) ble undersøkt gjennom søkeutdrag fordi direkte PDF-åpning feilet med størrelsesgrense 17 926 463 byte. Utdraget om håruttak sier «Use Max with the mammoth.» Root-kildeplan oppgir trykte sider 26 og 48; egen søkevisning viste ikke sidetallet for dette utdraget. Hintbokens tabell på trykt side 33 viser 91 yds. of twine og bruken «Use with dinosaur mouth and Max at Mt.Rushmore to pull tooth». Primærkilden støtter identiteten håruttak/hyssing, men bekrefter ikke runtime-kobling til disse ressurs-ID-ene.

Obj570_01/02/03 heter dinosaur-string og viser gul hyssing, ikke ledning eller bungee. 01 har feste oppe ved tann, 02 har løs øvre ende under kjeven, 03 har kortere synlig strand med lavere øvre ende og annen vannrett bunnstrek. Gul samling på bakken, dinosaurens kildeavklipte tenner/arm, høyttaler, mur, trapp, gress og himmel skal være konsistente. Ressursnumrene tolkes ikke som bevist avspillingsrekkefølge.

Pikselforskjeller mot 01 er målt: 02 har 283 endrede originalpiksler i boks [33,7,47,144], 03 har 285 i [26,7,47,144]. Dette gjør det mulig å bevare nytegnet felles bakgrunn utenfor dokumentert forskjellsområde. Ingen originalsilhuettmaske brukes. Se a-tilstandsforskjeller.json.

Alle bilder leveres på 1536 x 1024 med jobbens motivrektangel og eksakt padding RGB 128. Uendret egenkontroll er separat fra visuell egenvurdering og brukergodkjenning. Ingen import, timing, masker, dynamisk palett eller runtime er prøvd.

## Sluttkontroll

Samme attraksjonsmammut som i rom059, med pels fjernet og grå mekanisk side, bånd og benformer synlige. Ingen ny serviceluke, hud eller person. SJEKK 0.32/1.06/0.90: lite lokalt avvik, opptil 1.1 originalpiksler. Ikke merket OK.

Gul hyssing festet ved dinosaurens tann og kildeformet samling på bakken. Andre fullforsøk valgt: OK 0.02/0.03/0.96. Første var SJEKK 0.41/1.82/0.84 og er bevart, ikke brukt som anker.

Gul hyssing med løs øvre ende under kjeven. Samme nye bakgrunn som 01, bare [800,216,864,770] satt inn fra egen generering. OK 0.02/0.03/0.96.

Kortere gul hyssing med lavere løs øvre ende og annet nedre forløp. Samme nye bakgrunn som 01, bare [776,216,864,770] satt inn fra egen generering. OK 0.02/0.03/0.96.

Alle 44 låste kilder er SHA-verifisert uendret. Alle fire har eksakt RGB 128-padding. Se a-kildebevis.json, a-kontinuitetsbevis.json, a-leveranser.json og a-samlet-qa.png. Små maleriske detaljer i mekanikk og tenner er visuell tolkning, ikke runtime-bevist modellinformasjon. Ordrette prompters formulering om godkjent tilstand 01 er eksplisitt korrigert: det er nytt produksjonsgrunnlag for kontinuitet, ikke individuell brukergodkjenning. Tilstand 02/03 er byteidentiske med ny 01 utenfor oppgitte rektangler. Ingen originalpikselmaske brukes. Eksakt modellnavn er ikke eksponert.
