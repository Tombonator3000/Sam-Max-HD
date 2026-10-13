# Kilde-QA for Snuckey's og karnevalet

Fire deljobber er levert fra to sammenhengende fullscener. Originalrommene er 480x200 og 632x200. Originaldelene er slått sammen uten endring og brukt som redigeringsmål. Godkjent kontor er stilanker, ingen sceneinnhold er hentet derfra.

Verktøyet returnerte 1717x916 for rom011 og 1971x798 for rom015. Hele panoramabilder er normalisert til 1920x1024 og 2528x1024 med Lanczos. Bare global skala og marginal målavrunding er brukt, ingen lokal warp. Padding er satt til eksakt #808080. Endelige jobber er 1536x1024 med bildeområde [0,112,1536,800].

Rom011 har delskift384 og overlapp1152 piksler; rom015 har delskift992 og overlapp544 piksler. Begge overlapp er kontrollert med array_equal og er byte-identiske. Alle fire kontroller gir OK.

Karnevalets første D i ODDITIES ble feilaktig P i første forsøk. Avgrenset innebygd image_gen-edit rettet bokstaven. Bare det genererte bokstavutsnittet ble presist plassert i masteren, med myk rektangulær overgang. Dette er ikke originalpikselmaskering. Råbilde, førbilde, prompt, rettingsutsnitt, etterbilde og oppskrift er bevart.

Kildetekst: origin/main:docs/gpt-romnotater.csv ved 3df35f636f123584e4a8d454871fb9318f995d35. Fem krakker er synlige i Snuckey's når den delvis skjulte bakerste regnes med. Prompttilleggets fire var en tellefeil; original og resultat har fem. De beskyttede promptfilene er ikke rørt.

16 beskyttede kilder matcher kildehash.json. Ingen Git-mutasjoner, kodeendringer eller globale dokumentendringer er utført.

Små vareetiketter og plakatglyfer kan ikke uten videre kalles identisk tekst; de store dokumenterte skiltene er kontrollert, inklusive rettet ODDITIES. Motorintegrasjon, objektlag og ny visuell godkjenning fra Tom er ikke utført. Runtime=false og nybildegodkjenning=false er ført i manifestet.
