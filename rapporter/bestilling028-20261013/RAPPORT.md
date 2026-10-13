# Bestilling 28: tre panoramatilstander og minispilluttrykk

Ti grafikkjobber er klare for mottak, alle teknisk OK. Root har kontrollert 25 faktiske metadatafelt, uten hoppede felt, og sett original/HD, minispillenes helscener og alle tre panoramamastere. De 40 beskyttede kildene og åtte ekstra kontekstfilene er uendret. Dette er grafikklevering; import, runtime og ny individuell bildegodkjenning er ikke utført.

## Karnevalets tre tilstander

Hver av 017_02, 017_03 og 017_04 har egen 2528 × 800-master. Delene klippes ved x = 0 og 992 og har 544 × 800 byteidentisk overlapp. Root har verifisert at begge delbilder kommer fra riktig felles master. Fullscene bruker unionen av begge delers objekter, så synlighet i overlapp bevares selv når metadata tildeler objektet bare én del.

02 har tom kjegleplass med gul stjernekrans, åpen tom WIN-luke, liten lås på lukket Trixiedør, brede vimpler og egen propellstilling. En rest av grunnrommets HD-kjeglespiss lå over originalens metadatafelt. Det nye tomme underlaget er derfor satt inn 16 HD-piksler høyere. Det gir 3808 endrede piksler utenfor bare metadataunionen; null utenfor dokumentert komposisjonsfelt. Dette er kontrollert og oppgitt, ikke feilaktig rapportert som null utenfor metadata.

03/04 beholder egne fragmenterte røde/gule/grønne vimpler, små adskilte punkter/fliker og forskjellige propell-/spakstillinger. Root avviste fire første vimpelfelt fordi konturene fortsatt var store pikseltrappetrinn. Ett nytt lokalt imagegen-kall rettet rød/gul 03 og rød/grønn 04, med jevne konturer og de separate formene bevart. Ingen hel duk er fylt inn. Null piksler er endret utenfor de fire feltene i denne rettingen. Grønn 03 og gul 04 er beholdt; gul 04 har fortsatt noen kantete småpartier rundt kildens åpne løkke.

04-propellens manglende lange høyreblad ble rettet før mottak. Fire synlige armretninger er nå bevart, med nesten vannrett høyreblad. Bladet er noe lengre/tynnere og blankere enn den sparsomme kilden. Lås, luker og vimpler er også mer modellert. Ingen nytt avgjørende motivbytte er funnet i den siste helscene-/feltkontrollen. C sine råforsøk, førmastere, oppskrifter og konkrete forbehold er bevart.

## Sam- og Max-feltene

018_01 gjenbruker allerede kildeidentiske Sam-øyne/tunge fra riktig HD-grunnrom. Nytt 196-felt viser to adskilte avskårne øyefragmenter uten tredje mørk form eller fullført Max-hode. 018_02 har egen lavere tunge, endret blikk og lite rødt nesefelt. 018_03 har lukkede øyne og egen tungeform. Overlappende øye-/tungefelter kommer fra samme nytegnede ansiktsutsnitt per tilstand.

Fem svarte hull er tomme, og HIT 20 WIN-panelets svarte tellefelt er tomt. 019_01 har Max med kildeegne bøyde ører og avskårne poter; Sam har armen nede og rommet har ikke 018-poengpanelet. Den senere utstrakte Sam-armen fra 019_03 er ikke arvet inn her. C har utført uavhengig visuell kontroll av disse fire jobbene, med låste aktuelle hasher, og root har sett både felt og helscener.

En blå rektangelskjøt mellom 196-fragmentene er fjernet med fargeseparasjon av bare nygenererte piksler mot nytegnet blått grunnrom. Kriterium og pikselantall står i a-blaafeltbevis.json. Ingen originalsilhuett eller originalfargekart er brukt som maske. Alle fire resultater er byteidentiske med sitt korrekte HD-grunnrom utenfor metadataunionen. Tunger, neser og Max-former er rundere/blankere enn originalen, dokumentert som tegningsforbehold.

## Leveransebevis

A brukte seks innebygde imagegen-kall; C brukte ti inklusive tre propellforsøk og siste vimpelretting. Eksakt bildemodell er ikke eksponert. Ordrette jobbprompter, separate kildepresiseringer, råbilder, sammensetting, SHA og visuell QA er bevart. Vanlig helskalering, rektangulær plassering/fjæring og dokumentert ny-til-ny tonejustering er brukt; ingen vektorunntak, originalpiksler som erstatningskunst eller lokal geometriwarp.

Aktuell status er i fremdrift.json og sluttkontroll.json. root-objektkontroll.json viser alle 25 felt, og root-bakgrunnskontroll.json viser de faktiske bakgrunnsunntakene. Samlet kontaktark følger. Ti offentlige PNG-hasher fra forrige bestilling 27 er bekreftet mot den eksakte push-commiten i bestilling027-pushkontroll.json.
