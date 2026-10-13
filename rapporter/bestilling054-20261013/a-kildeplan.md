# Max005 og Max235: kildeplan

Fire ark, 68 ruter. [a-kildehash.json](a-kildehash.json) låser de 16 beskyttede filene. Sam004/53 står frosset. C sine fig007-jobber og c-filer er ikke berørt. Ingen nye bilder eller resultater er skrevet i denne analysen.

| Jobb | Antall | Motiv og forhold til Max003 |
| --- | ---: | --- |
| fig005_01 | 28 | Tre separate kropper, tre hoder, to øyelokksruter, åtte gåposer mot høyre og tolv snakkehoder. Alle RGB-ruter er identiske med tilsvarende cel i fig003_01. |
| fig005_02 | 23 | Tolv snakkehoder forfra, tre bakhoder og åtte gåposer forfra. Alle har identisk RGB-kilde i fig003_02; bakhode423 er dessuten identisk med pilotens386. |
| fig005_03 | 9 | Åtte gåposer bakfra er identiske med fig003_03. Cel000 er en egen hel stående Max med lite munnuttrykk. |
| fig235_01 | 8 | Tre kropper, tre hoder, to øyelokksruter. Alle identiske med fig003_01. Rom47 gir ikke noen faktisk fargeforskjell i disse originalrutene. |

[a-kildebevis.json](a-kildebevis.json) angir hver rute, animasjon, retning, lag, atlasboks, synlig RGB-palett, originalmetadata og alle samsvarende003-cels. Alle 67 treff er faktisk identiske RGB-bilder inkludert cyan bakgrunn, ikke bare like silhuetter. Rutenes feste-, størrelse- og flyttemetadata er identiske med samme cel i003. Når423 matches mot386 er bare cel/kode forskjellig; sammecel423 finnes også i00302. Målmetadata skal uansett beholdes.

## Identitet og lag

Max er kremhvit med beige/grå skygger, lange rosa øreinnsider der de vender mot oss, svart øye/munn og rosa nese/tunge/potefelt der kilden viser det. Ingen klær eller utstyr er synlig i disse arkene. Kropper uten hode, hoder uten kropp og de to svært små øyelokksrutene er tilsiktede egne lag. De skal ikke fullføres. Gangposene viser bevisste øre-, hånd-, bein- og skyggeendringer, ikke nye figurer.

[Originalkontaktarket](a-original-kontaktark.png) og feltark [1](a-feltark-1.png), [2](a-feltark-2.png), [3](a-feltark-3.png), [4](a-feltark-4.png), [5](a-feltark-5.png), [6](a-feltark-6.png) er sett. [Rel-sammensettingen](a-rel-sammensetting.png) viser kildekropp/hode/øyelokk samlet etter rel-koordinater, i tre retninger samt235 og cel000. Dette er statisk kildeanalyse, ikke runtime.

## Den nye cel000 i00503

[Nærbildet](a-cel000-narbilde.png) viser en hel stående Max med to opprette, ulikt skrånende ører, små svarte øyne, rosa nese og liten mørk munn under nesen. Armene henger ned ved kroppen; føttene står på samme lave grunnlinje. Den grå/beige formen til høyre er den skyggelagte armen, beinet og foten, ikke påvist separat rekvisitt. Det finnes ingen synlig stang, pistol eller annen gjenstand som krever ny tolkning.

Cel000 er 31 × 53 kildepiksler, rel(-13,-52), lag0, retning0. Metadata bruker denne samme cel i a6 til a16. Det beviser ressurskoblingen, men ikke hva disse animasjonsnumrene betyr i spillet. Kildens rastervinkel prioriteres fremfor å speile til en generisk venstrevendt figur fordi teksten sier retning0.

En prøve med kropp129 og hvert tilgjengelige00501-hode på de originale festene gir ingen byte-identisk komposisjon. [a-cel000-komposisjonsprove.json](a-cel000-komposisjonsprove.json) dokumenterer avvikene. Cel000 skal derfor tegnes som egen kildepose, ikke konstrueres blindt fra et tilfeldig eksisterende hode. Ingen semantisk uklar rekvisitt er funnet; eventuell senere motivdrift skal likevel stoppes og undersøkes.

## Palett, alfa og proveniens

Kostymene003,005 og235 har identiske palettindekser: [3,234,235,236,237,238,239,240,241,9,10,11,12,13,14,15]. 003/005 henter rom1-palett0;235 henter rom47-palett0. Faktiske RGB-piksler er sammenlignet, og de67 like rutene har ingen lys-/fargeforskjell. Likhet er bevist for RGB-ark; ikke kall dette komplett opprinnelig native RGBA-bevis.

Kilden bruker cyan [0,200,200] og grå padding. Leveransen skal være ekte RGBA, 1536 × 1024, hele bakgrunnen og padding transparent. Motivfeltet er [64,32,1408,960], skala4. De diagnostiske kildealfamaskene i sammensettingsbildene brukes bare til analyse, aldri som maskering av ny grafikk.

## Produksjonsplan og avhengigheter

Gjenbruk eksakte nye003-cels for de67 beviselig like rutene, med egen målpakking og proveniens. B arbeider fortsatt med00302 og00303, så disse donorene må avvente rotens mottak. Pilotens avklarte00301 kan brukes når dens aktuelle godkjente fil/hash er kontrollert. Ikke ta et uferdig donorresultat som godkjent kilde.

Den ene nye cel000 kan produseres med innebygd imagegen, riktig original som pose/palett og godkjent Max-hovedark/pilot som stilanker. Ordrett jobbprompt og separat presisering av den ene ruten bevares. Deretter vanlig presis helskalering og plassering, ingen originalmaske eller warp. Uendret checker må kjøres på ferdige ark, og små øyelokk som hoppes over kontrolleres separat. Samlet hode/kropp/rel-kontroll, alle68 felt, alfakant og provenance må følge leveransen. Ingen motoravspilling eller ny individuell godkjenning er påstått.
