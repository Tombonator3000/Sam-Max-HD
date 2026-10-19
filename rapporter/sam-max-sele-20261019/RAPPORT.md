# Sam og Max i strikksele, 19. oktober 2026

Fem ark fig309_01 til05 er levert med 40 nye native ruter fra 35 eksakt ulike originalposer. 175 av 1758 figurjobber har resultat. 1583 mangler resultat, i tillegg til returer, stilgodkjenning og sluttkontroll.

## Motiv og kildegrunnlag

Kostyme309, rom61, strikkhoppgrotten. Sam og Max kommer opp fra strikkhopp. Sam holder Max mens han snur seg og setter ham ned. Rød sele, gul/purpur strikkbriller, blågrå dress/fedora og grønn/gul strikk med grå krok følger originalen. Første åtte spillruter viser bare strikken. De to neste viser delvise Sam-poser. Disse er ikke fullført med ekstra figurer. De isolerte små strikkdelene og kildebekreftede ørebevegelsesstrekene er beholdt.

Alle fem hele kilder, Sam- og Max-hovedark og to originale motorforløp er sett før nytegning. Ressursbanken GJENNOMGANG.md rom61 og riktig kostyme309-rad i docs/figurer.csv er kontrollert. Ingen uavklart motivfortolkning gjenstår for denne bunken. Alle 170 tidligere resultatjobber ble søkt etter eksakt kilde-RGBA, ingen treff. 20 beskyttede kildefiler er uendret.

Prosjektbibliotekets figurark-fast-storrelse.md, scumm-v6-kostymer-skygge-og-soppelruter.md og publisert-mod-er-fasit.md er brukt for fast plassering, riktige v6-deler og kontroll av tilbakehentet modd. Kontrollene er kjørt i dette prosjektet.

## Faktisk produksjon

Innebygd image_gen, eksakt modellnavn ikke vist. Sju faktiske kall i rekkefølgen A01, B01, C01, D01, E01, F01, A02. Alle ga bilde. Seks brukes i sluttresultatene; A01 er bevart som utkast. Faktiske prompter, råbilder, råbildenes genererte filsti og SHA-er er bevart i bildekall.json og unik-X-kvitteringNN.json. Alle råbilder er1536x1024 RGBA, alle resultatark er1536x1024 RGBA med ekte alfa.

A02 retter oppdiktede ledd i tre bøyde strikker.1926/1927 hadde fortsatt feil kurve og er plassert langs originalens glattede strikksenter. Bare generert RGBA flyttes; originalens alfasilhuett brukes aldri til klipping. Førversjoner og egenkontroll-FEIL er bevart i for-kurveplassering. Begge rettede ruter har nå egenkontroll OK. Oppdiktede løse bunnbiter fra A02 er utelatt der originalen har sammenhengende strikk.

Kildekomponentenes rektangler styrer plassering av genererte deler. Hver kildekomponent har generert innhold; manglende små strikkdeler gjenbruker A02 sin genererte korte strikk. Den lille blå jakkedelen i1928 bruker generert blått jakkestoff fra samme råbilde. Den femte ørebevegelsesstreken i1952 deler generert strek i samme kildefarge. Dette er ført per del med kildeboks, generert råboks og SHA i prototype-kvitteringer.json. Ingen hard original pikselmaske. Python-rensing og plassering er uttrykkelig godkjent av Tom.

## Kontroll og begrensninger

- Egenkontroll: 32 OK, 8 SJEKK, 0 FEIL. Merknader om omriss står på1921,1922,1923,1930,1931,1946,1953 og1954. Alle har100% bredde/høyde og null original forskyvning. Ikke relabelt som OK.
- Ordinært native mottak: 40 OK, 0 til gjennomsyn, 0 mangler, 0 tekniske feil. Uendrede mottaksgrenser.
- Alle40 er visuelt sett mot original/native/motorutsnitt i fire kontrollbrett. Begge hele motorbilder er sett. Både Sam- og Max-identitet, retninger, seletøy, briller, krok, løse strikkdeler og ørebevegelse er kontrollert.
- Begge animasjoner1 og7 er kjørt i nedlastet uendret Linux-kveldsmotor. Alle40 er registrert tegnet.150 skjermbufferkontroller,132 fra figurstart uten avvik. To kjente avvik160 ved frame36 før testfiguren er identiske med de to grunnlagsprøvene. Produksjonsbinær-SHA76c736a695b54d802c4ff22c2c9d6426275f406d5771faac90a2555f64aa171b. Isolerte HOME/XDG og saves per prosess, ingen lokal retningskrok.
- Fire rålogger og SHA-manifest er bevart i motorlogger.zip og motorlogger-manifest.json. Ingen naturlig gjennomspilling, interaktiv Windows-test, ny Tom-godkjenning eller separat Claude-kontroll. Den eksisterende damen i rom61 er ikke nytegnet i denne bunken.

## Bevaring og publisering

Grunnlag: hd-mod69d5f1ff15fd1b9c7b388a74041b65ccf83d8ec1 med1736 native. Kandidaten har1776 native og20012 PNG-er. Alle19972 tidligere PNG-er er byteidentiske, alle19978 tidligere filer finnes fortsatt. Bare mod.json endres før publisering. Tre stasher er bevart. Se bevaringskontroll.json og den senere mottak-publisert.json for faktisk kildecommit, publisert modd-SHA og kontrollert tilbakehenting.

Den eksisterende felles Linux-/Windows-releasen sam-max-hd-2026-10-19-kveld har1654 native. Den mangler nå82 gripearmruter og disse40 strikkrutene,122 i alt. Neste samlepakke må lastes ned og sammenlignes før den kalles oppdatert. Ingen ny grafikk går til main.

Neste uavhengige serie er fig215_01 til04, Sam ved Frog Rock i rom41,48 spillruter. Betydningen av de gule delene ved føttene skal kontrolleres mot originalmotor og spillkontekst før nytegning. Fig300_01 til04, Sam med langt tau i rom58,27 ruter, kan tas i samme praktiske bunke etter egen kildekontroll. Avviste golf-E- og VR-G-grunnlag bestilles ikke på nytt.

Publisering bekreftet: kildecommit 9b6da3b8a40694663f857c43ad8250030ac0a428, hd-mod 6513908aa6d47dd73abd58f6f101ff9641c25d6b. Alle 20 012 kandidat-PNG-er stemmer etter tilbakehenting; alle 19 972 tidligere PNG-er er byteidentiske. Alle 40 nye native-SHA-er er verifisert. Native totalt1776. Se mottak-publisert.json.
