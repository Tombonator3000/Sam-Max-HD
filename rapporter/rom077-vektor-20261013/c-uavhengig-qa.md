# Uavhengig kilde- og geometrikontroll av rom077

Kontrollert 13. oktober 2026 av C. Kun denne rapporten er skrevet; bilder, oppskrift, jobber og kilder er ikke endret. Grunnlag er de to originaldelene, sammensatt original, native SVG, geometri, rastermaster, faktiske delklipp og oppdatert `samlet-panel-qa.png`. Ingen runtime er kjørt, og rapporten er ikke ny brukergodkjenning.

## Konklusjon og konkrete forbehold

Native vektor bevarer det svært mørke veipanelet, de store svarte tomrommene, røde randlinjene og kildens separate markeringer. Jeg finner ikke nye figurer, navn, biler, gradienter eller ekstra fasetter. To konkrete presiseringer må følge leveransen:

- Kilden har **fire**, ikke tre, små sidemarkeringer. Alle fire er bevart i vektoren. Tidligere omtale av tre er en tellefeil, ikke grunn til å fjerne en markering.
- PNG-rasteriseringen har én ekstra svak rød rad utenfor panelets nedre grense: HD y = 532, x = 1280..2559, RGB (52,0,0). Panelet skal slutte eksklusivt på y = 532. Native SVG slutter korrekt på kilde y = 133; dette er et rasteravvik, sannsynligvis fra inkluderende polygonendepunkt før nedskalering. Anbefalt å rette i rasteriseringen før endelig låsing, uten å endre native geometrien.

Uendret egenkontroll er OK for del 1 (0,03 / 0,04 / 1,00) og SJEKK for del 2 (0,03 / 1,20 / 1,00). SJEKK er ikke oppgradert. Den geometriske utjevningen er synlig og dokumentert nedenfor; tallene alene brukes ikke som motivgodkjenning.

## Motiv og kildekomponenter

Originalens seks farger er svart, grå 23, 39, 55 og 71 samt rød (207,0,0). SVG bruker nøyaktig disse seks flate fyllfargene. Rasterets kantutjevning gir mellomtoner på grenser, ikke en ny gradientflate. Det mørke panelet opptar kilde [320,67,640,133]; resten av fullverdenen er svart. Den ekstra rasterraden nevnt over er eneste målte utvidelse av dette avgrensede feltet.

Fem lyse midtkomponenter er beholdt inklusive det lille apex-punktet. Originalens separate komponentbokser, eksklusive høyre/nedre koordinater, er [480,78,481,79], [480,80,481,83], [479,85,482,93], [478,98,483,109] og [476,121,485,132]. Ingen komponent er lagt til eller slått sammen. Den tredje har fortsatt en uregelmessig utstikkende fot; en rastertrapp på høyre side er gjort til kort skråkant innen ordinær toleranse.

Fire grå sidemarkeringer er dokumentert direkte med 4-nabokomponenttelling i originalen: [456,84,457,85] (1 piksel), [512,84,513,85] (1 piksel), [433,91,438,92] (5 piksler) og [539,100,542,102] (6 piksler). De to nederste er asymmetriske i både høyde og størrelse. Vektoren bevarer plassering og størrelse, og normaliserer dem ikke til symmetriske veimerker.

## Geometri og faktisk filstruktur

SVG er native geometri med seks path-elementer og 24 lukkede regionløkker, evenodd-fyll og viewBox 0 0 640 200. Ingen image-elementer, bitmapdata, href eller gradient finnes. De delte grensene gjenbruker samme forenklede kjede på begge sider. 34 kjeder er kontrollert; alle kildeendepunkter er bevart.

Uavhengig av oppskriftens oppgitte toleranse er avstanden fra hvert opprinnelig kjedepunkt til nærmeste nye linjesegment beregnet. Største målte avstand er 1,5268567 kildepiksler. Bare kjede 9 og 17 overskrider 0,8, med henholdsvis 1,2682088 og 1,5268567. Dette er de to avtalte veisidene. De går fra (371,132) til (478,78) og fra (482,78) til (589,132), med uendrede endepunkter. Originalens trappekanter er synlig erstattet med rette diagonaler; dette er ikke pikselidentisk geometri, men den særskilt autoriserte utjevningen. De øvrige kjedene ligger innen 0,8 kildepiksel.

Parvise tester av segmenter finner ingen nye strenge indre kryssinger, heller ikke selvkryssinger. Dette er en test for faktiske kryssende segmenter, ikke et generelt matematisk bevis om alle kollineære kontakter. Visuell sammenligning viser sammenhengende veifelt, beholdt horisontprofil og ingen nye omkryssinger eller hull. Horisontens korte nivåtrinn er delvis gjort til skråkanter innen ordinær toleranse; ingen ekstra fjell eller detaljer er introdusert.

## Kilder, delklipp og padding

`original-full.png` er byteidentisk med del 1 i x = 0..383 og del 2 i x = 256..639. Alle åtte beskyttede filer stemmer med `kildehash.json`.

Begge kandidatene er faktiske klipp fra samme 2560 x 800 master: del 1 bruker x = 0..1535, del 2 x = 1024..2559. Begge er plassert ved y = 112 på 1536 x 1024 lerret. Motivpikslene er byteidentiske med masterklippene, og dermed er hele 512 x 800 overlapp byteidentisk. Øvre og nedre padding er RGB (128,128,128). Dette er kontroll av kandidatfilene i rapportmappen, ikke påstand om runtime-integrasjon.

## Kontrollert versjon

- SVG SHA-256: `1ea45412b81c53f7b3025dc89114da93e9337154f9d25891ed91c7cc7e4bbe64`
- PNG SHA-256: `0ddf7dac73895ae19eb058f0fdc9b4c05935770c33e71943c8c9d821d9bc098b`
- geometri.json SHA-256: `02b7dfef62f0569703ad68134d77789243d01a1da866283bb32825b1cbc165a2`
- Original-full SHA-256: `a88ec2ceebbe35e7deab0e6b32149d3f9528ae57da96557ab649ac1dbd900c9c`
- Oppdatert panel-QA SHA-256: `5a916356eb4a7fa5d7fd62e92bd59e25307324ff70b442240db35a7380385c3b`

Førversjonen er bevart separat. Rapporten gjelder hashene over; en senere rasterretting må kontrolleres særskilt. Det er ikke funnet et motivbytte som krever nytegning av native SVG. Endelig mottak avgjøres av root med det konkrete rasteravviket og teknisk SJEKK synlig.

## Etterkontroll etter rasterretting

Root har byttet rasterisering til samplesentre og halvåpne intervaller. Ny master er visuelt kontrollert og målt. Ikke-svart bbox er [1280, 268, 2560, 532]. Rad y = 532 er nå helt svart; den tidligere ekstra røde raden er borte. Native SVG-geometri er uendret.
- rom077-master.svg SHA-256: `1ea45412b81c53f7b3025dc89114da93e9337154f9d25891ed91c7cc7e4bbe64`
- rom077-master.png SHA-256: `451a010626cb29ebdb2f16b3d62553faff068a6304fcbeb8c2db2342117f3693`
- rekonstruer.py.txt SHA-256: `d8b4eb78a20ff84a3680670914e005ebbb5d1b42b377883c9774dff3d862919d`
- Del 1: klipp og padding bytekontrollert; SHA-256 `541408d6cefef9af0024ff741f5ba144df6b51acbddb017297ba2c1b6de44fcd`.
- Del 2: klipp og padding bytekontrollert; SHA-256 `9f4be089c7e95743b7dbe0d5aa97d87c480705fea3aad1d755e8a23f2ecbc96b`.
Alle åtte kildehash er fortsatt uendret. Oppdaterte uendrede checkerfiler:
```
== rom077_del1av2 (rom): rapporter/rom077-vektor-20261013/kontroll-del1/resultat.png
OK    hele bildet (lerret): skift 0.00, blokker 0.00, kantlikhet 1.00
   Utfall: OK
```
```
== rom077_del2av2 (rom): rapporter/rom077-vektor-20261013/kontroll-del2/resultat.png
OK    hele bildet (lerret): skift 0.05, blokker 0.99, kantlikhet 1.00
   Utfall: OK
```
Det konkrete rasteravviket er rettet. Tidligere teknisk SJEKK beskriver førversjonen; begge nye checkerutfall er OK. Motivvurderingen over gjelder fortsatt, inklusive fire sidemarkeringer og dokumentert utjevning. Runtime og ny brukergodkjenning er fortsatt ikke verifisert.
