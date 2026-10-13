# Produksjons-QA, gruppe B, bestilling 23

Ni TV-lag er produsert fra tilstand 03 til 0B, med desimal lag 03 til 11. Jobbene er opake fullromskomposisjoner på 1536 x 1024. Riktig levert rom007 del1 er byte-identisk utenfor TV-felt [576,464,96,96] og, bare for lag03, indikatorfelt [36,642,18,10]. Lag02 sin andre telefon-/vindutilstand er ikke brukt som bakgrunn. Alle 40 beskyttede kilder er uendret.

## Produksjonsforløp

Tre felles atlasforsøk er bevart. Første zoomet ut TV-kassen og la til ansiktstolkning; det ble forkastet. Andre hadde bedre utsnitt, men større runde ansiktstrekk og tre runde betjeningsfelt. Tredje er valgt etter uavhengig tidlig QA fra C: enklere fargeformer og rektangulært nederste betjeningsfelt ligger nærmere kilden. Ingen forkastet kandidat ble brukt som kildeanker for neste atlas; forsøk 2 og 3 var kildebaserte.

Alle ni deler en nytegnet TV-kasse fra tilstand 04 i tredje atlas. Skjerminnholdet er klippet innen åpningen til denne NYGENERERTE kassen, med polygonpunkter dokumentert i b-komposisjonsbevis.json. Klippet er utledet fra den nye tegningen, ikke fra originalens kontur, fargekart eller alfamasker. Ingen geometriwarp er brukt. Midlertidig atlas og alle ruter spores til hver kilde/tilstand; slutten er fullromslag.

Et lokalt firefelts imagegen-forsøk rettet 05 sin manglende nedre lyse utstikker, 08 sitt for hvite nedre felt, 09 sitt svarte punkt og 0B sitt øye-/munnfelt. Bare dokumenterte rektangler på den nye tegningen er komponert inn. Lag 09 er bygget på 04, og lag 0B på 0A, slik at resten er byte-identisk fremfor tilfeldig variert. Indikator 03 er et femte separat genereringskall, lokalt på grunnrommets eksisterende apparat. Totalt fem imagegen-kall, ikke fem per jobb. Eksakt bildemodell er ikke eksponert.

## Tilstands- og motivkontroll

Grønn TV-bakgrunn, mindre oransje/rødbrun venstre form med blått felt og større lys beige høyre profil er beholdt som unavngitte tegneserieformer. Ingen film, navn eller ny tekst er lagt inn.03 har langt hvitt munnfelt og mørkt nedre hull. 04 har kompakt åpen munnform. 05 til 08 har lengre vannrett profil, med egne nedre munn-/fargefelt. 09 bruker samme tegning som 04, men det svarte nedre punktet i venstre ansikt er fjernet til varmt rosa/oransje felt.0A og 0B beholder den kortere profilen, med svart øye versus brun øyestrek og lengre versus kortere venstre munnmarkering.

04/09 har 110 endrede HD-piksler i lokalboks [22,43,10,11], relativt til 96 x 96-TV-feltet. Kildens én-pikselendring er dermed tolket som en liten nytegnet markering, ikke kopiert til fire ganger fire originalfargede piksler. Alt utenfor den nye lokale boksen er byte-identisk.0A/0B skiller seg bare i to nye rektangler [53,20,16,15] og [24,46,11,16]. Se b-komposisjonsbevis.json for faktisk antall endrede piksler. Dette beviser avgrensning, ikke eksakt originalkontur.

Lag 03 har lysere grønn indikator med nye genererte toner. De øvrige åtte bruker grunnrommets mørkere indikator byte-identisk. Telefonrøret er fortsatt rødt og vinduene følger grunnrommet i alle ni.

## Teknikk og begrensninger

Alle ni uendrede helbildekontroller gir OK, med skift 0,05 til 0,06, blokk 0,08 og kantlikhet 0,97. Alle ti oppførte objektbokser er faktisk undersøkt; ingen ble hoppet over for lav varians. TV-korrelasjonene ligger 0,729 til 0,849 og indikatorboksen 0,983. Se b-objektkontroll.json. Bakgrunnsbevis, padding og kildehash er kontrollert separat.

Nytegningen gjør de små formene mer sammenhengende og tydeligere ansiktsliknende enn 24-pikselkilden. Kassen og skjermens glasstone er nytolket og mer detaljert. Munn-/øyefeltene er ikke punktsertifisert og det er ikke hevdet at hver eneste originalpiksel har en tilsvarende identisk HD-kontur. De grønne negative feltene og variantfamiliene er kontrollert samlet; forskjellig SHA alene regnes ikke som korrekt animasjon.

b-tv-familie.png viser alle original/HD-utsnitt sammen. b-076-familie.png viser kilde 03, grunn-HD og 03-HD. Råbilder, sendte prompter, atlasrutesporing, komponenter, førkandidater og oppskrifter er bevart. Import, faktisk motorvisning, timing og ny individuell brukergodkjenning er ikke utført. C sin uavhengige sluttsjekk i c-uavhengig-tv-qa.md er ferdig og bekrefter de avgjørende tilstandsforskjellene, alle manifesthash og bytebevart bakgrunn. Ingen avgjørende tilstandsforveksling gjenstår i den gjennomgangen. Form- og lysforbeholdene består.

C fant ved sluttsjekk en svart rest fra 0A rett under øyeklippet i 0B. Samme allerede nygenererte mikrokomponent inneholdt riktig nytt område; klippet ble utvidet med [53,31,16,4] uten ny generering. Resten er byte-identisk. Kontroll er kjørt på nytt med OK, og C har bekreftet at den svarte øyeresten er borte.
