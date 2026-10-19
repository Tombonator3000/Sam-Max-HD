# Sam med gripearm i hyssingmuseet, 19. oktober 2026

Seks ark fig152_01 til fig152_06 er levert. 82 nye native ruter fra 46 eksakt ulike originalposer. 170 av 1758 figurjobber har resultat; 1588 mangler resultat, i tillegg til returer, stilgodkjenning og sluttkontroll. Dette er ingen sluttgodkjenning av hele spillet.

## Motiv og kilder

Sam bruker grønn pantograf/golfballhenter med Jesse James-hånden, rød fiskemagnet og grå/hvit humørring med kildebekreftet rød stripe. Originale hele kroppslag14 beholdes som hele kroppslag, mens separate magnet-/ringdeler blir egne ruter. De brune gripedelene bak magneten er beholdt. Lange kropp-/øre-/beinposer er original tegneseriebevegelse.

Alle seks originalark, godkjent hovedark/sam.png og fire originale motorsekvenser i rom28 ble sett før nytegning. Ressursbanken GJENNOMGANG.md og riktig kostyme152-rad i docs/figurer.csv er kontrollert. Gåten med hånd, golfballhenter, magnet og humørring støttes av [Derek Waites walkthrough, BALL OF TWINE (3)](https://www.justadventure.com/walkthrough/sam-max-hit-the-road-cheats/). Hintbok-PDF-er kunne ikke åpnes i nettverktøyet og er ikke brukt som visuelt sett bevis.

Prosjektbibliotekets figurark-fast-storrelse.md, scumm-v6-kostymer-skygge-og-soppelruter.md og publisert-mod-er-fasit.md er brukt for fast plassering, kildekontroll og bevaring. De er tilpasset Sam & Max v6; kontrollene nedenfor er kjørt her.

## Produksjon og rettinger

Innebygd image_gen. Eksakt modellnavn vises ikke. 11 faktiske kall i rekkefølgen A01, B01, C01, D01, E01, F01, G01, H01, E02, I01, F02. Alle ga bilde. Ni råbilder brukes i endelige prototyper; E01 og F01 er forkastede utkast. D01 brukes for fem poser, mens H01 erstatter 1960. I01 erstatter A-posen1923 og kildeidentisk alias1795. Hele call-ledgeren med prompt-, råbilde- og kilde-SHA er bildekall.json. Ingen avbrudd eller avslag i denne bunken.

H01 gjenoppretter en glemt hevet brun fot bak pantografen. E02 retter et overteksturert håndfeste. I01 retter for lang gripearm og for smal kropp. F02 beholder de små brune grepene rundt magneten og fjerner en oppdiktet grå tapp. F02 endrer bare ni nye native filer1937 til 1945; de øvrige 73 er byteidentiske med førversjonen. Animasjon7 er kjørt på nytt etter denne endringen.

Python er uttrykkelig godkjent av Tom for rensing og plassering. Generert alfa er brukt med myk kant; ingen hard original pikselmaske til klipping. Kildeidentiske RGBA-poser gir identiske native filer. Råbildene har sine faktiske størrelser registrert, blant annet H 1602 x 982 og I 1126 x 1397. Sluttleveransene er alle 1536 x 1024 med ekte alfa og riktig 4x plassering. De 24 beskyttede jobb-/referansefilene er uendret.

## Kontroller og praktiske grenser

- Egenkontroll: 75 OK, 7 SJEKK, 0 FEIL. Omrissmerknadene gjelder 1937, 1939, 1961, alias 1833, 1979, 1982 og 1983. Alle har 100% bredde/høyde og null original forskyvning. Merknadene er bevart, ikke kalt OK.
- Ordinært native mottak: 82 OK, 0 til gjennomsyn, 0 mangler, 0 tekniske feil, uendrede grenser.
- Alle 82 endelige ruter er sett i sju original/native/motor-brett. Alle fire hele motorbilder er sett. De to berørte brettene og hele animasjon 7-bildet er sett på nytt etter F02.
- Fire endelige animasjoner 1, 7, 8, 9 i den faktiske nedlastede Linux-kveldsmotoren. Alle 82 logget tegnet. 300 skjermbufferkontroller, 264 fra figurstart uten avvik. Fire kjente avvik 160 ved frame 36 før testfiguren er identiske med de fire grunnlagsprøvene i samme binær. Produksjonsbinær-SHA 76c736a695b54d802c4ff22c2c9d6426275f406d5771faac90a2555f64aa171b.
- motorlogger.zip bevarer 13 logger: fire opprinnelige grunnlagslogger, fire grunnlag i kveldsmotoren, fire endelige sekvenser og animasjon 7 før F02. Hashene står i motorlogger-manifest.json.
- Tvungne animasjoner, ikke naturlig gjennomspilling. Ingen separat Claude-kontroll eller ny Tom-godkjenning. Den eksisterende museumsvakten er fortsatt tidligere grafikk og inngår ikke i denne leveransen.

## Bevaring, publisering og pakker

Grunnlag er hd-mod bd65ce87f0f690ac19aa1c316f376a2e23810193 med 1654 native. Kandidaten har 1736 native og 19972 PNG-er. Alle 19890 tidligere PNG-er er byteidentiske; samtlige 19896 tidligere filer finnes fortsatt. Bare mod.json endres av tidligere filer før publisering. Tre stasher er bevart. Se bevaringskontroll.json og den senere mottak-publisert.json for kildecommit, faktisk publisert modd-SHA og verifisert tilbakehenting.

Den felles Linux-/Windows-nedlastingen sam-max-hd-2026-10-19-kveld inneholder 1654 native. Disse 82 nye er foreløpig ikke i pakken. Pakker oppdateres ved neste samlepunkt eller avslutning, etter ny nedlasting og filkontroll. Ny grafikk går ikke til main.

Neste uavhengige bunke er fig309_01 til 05, Sam og Max, 40 spillruter. Avklar kostyme 309 i spillkontekst og se begge godkjente hovedark før nytegning. Ikke bestill de avviste golf-E- eller VR-G-grunnlagene på nytt.
