# Bestilling 31 C – kilde- og motivkontroll

Sju jobber er levert i c-leveranser.json: lag026_01, 04, 05, 06, 07, 08 og 09. lag026_02/03 er fortsatt holdt for brukerens svar om figuridentitet og kremfragment. De to første råforsøkene er bevart som uavklarte/avviste, ikke brukt som identitetsankre. Ingen resultat eller notat er skrevet for disse to.

## Kilde og mening

Originalkompositter, metadata, root-kildeplan, feltbevis og sammenlikninger mot både originalt og levert HD-grunnrom er lest visuelt. Brukerens avklaring styrer 269: søl/vannplask fra Dunk the Beast. 272 viser et mørkt avklippet interiør, ingen synlig kule og ikke et komplett skap. 276 er sete borte, med stolpen og blå/hvit detalj igjen. Ingen ny fortelling eller runtimefunksjon er antatt.

269-nærbildet har rosa RGB 151/107/115 ved lokale originalkoordinater (15,11), (14,12), (17,12), (36,12), (19,13), (17,14), (21,14). Det er sju piksler, men diagonalparet danner én skrå markering: seks grupper. Første teksttelling var for upresis og er ikke brukt som endelig kildebevis. De feilaktige promptene beholdes for proveniens. Valgt nytegning har tre løse hvite dråper under plasket og seks rosa grupper, inklusive den skrå. Konturene er spisse, men den hvite bunnformen er rundere og rosa merker mindre/mykere enn originalrasteret. Dette er eksplisitte tegningsforbehold, ikke påstått pikselidentitet.

## Rettelser og familiekontroll

272 sitt første forsøk fullførte en innrammet gjenstand med for mye gul rand. Et nytt source-only-bilde beholder nå svart avskjæring, brun/oliven struktur og kildens lille gule høyrekant. Det er plassert uten kantfjæring fordi originalfeltet selv er hardt avskåret.

275_04/05/06 er tre egne vinkler i ett nytt tilstandsark. Første 04-forsøk kopierte grunnrommets vanlige vinkel og er forkastet. Original- og HD-feltene i c-objektqa-2/3 viser de ulike venstrepanelene. 275_01 har sin egen smalere geometri. Hengsel 270_01 og åpen luke 270_02 bevarer egne avskårne tekstflater og mørke innvendige detaljer. Blink 274 har sin egen ringtilstand.

276 første forsøk fjernet feilaktig stolpen; senere helforsøk omtolket den gule delen til en naglet presenning. Begge er forkastet. Valgt lokal kandidat har stolpen og intet sete; den lille blå/hvite formen ble nytegnet i et eget mikro-kall og bare [120,64,24,20] av det nygenererte objektfeltet er innfelt. En 4 px rektangulær overgang demper den lokale blå skjøten. Stolpen er noe skråere enn kilden, og detaljen er mer modellert. Ingen annen gjenstand er fullført rundt den.

269 sitt detaljforsøk beholdt tre dråper, men for mange rosa merker. To senere brede forsøk la til en fjerde nedre dråpe og brukes ikke. Nytt mikro-kall ga riktig markstruktur. Alfa er beregnet utelukkende fra de rosa fargene i NYGENERERTE bilder, ikke fra originalkonturer. Hvitt nygenerert underlag fjerner de gamle nye merkene; den nye markgruppen plasseres samlet i [48,40,108,24]. Ingen originalmaskering, tracing eller geometrisk warp. Alle mellomfiler, alfaer og oppskrift er bevart.

## Kontroller og avgrensning

Alle sju faktiske resultatfiler består uendret verktoy/sjekk_leveranse.py med OK. De ti egne objektfeltene er i tillegg kontrollert separat med kantkorrelasjon og faktiske nærbilder. Korrelasjon er støttebevis, ikke identitetsbevis. Den laveste er 276 med omtrent 0,907; 269 har omtrent 0,942 og 272 omtrent 0,996. Faktiske verdier står i c-objektkontroll.json. Hele kompositter er kontrollert samlet i c-helsceneqa.png.

Alle sju er RGB 1536 × 1024 med motiv [128,112,1280,800] og eksakt RGB 128 utenfor. Utenfor hver jobbs egen metadataunion er resultatet byte-identisk med levert rom026-HD. Alle 40 egne bestillingskilder og åtte låste kontekstkilder er uendret. Dette står i c-kildehashkontroll.json og c-komposisjonsbevis.json.

Innebygd ChatGPT imagegen er brukt; eksakt modellnavn er ikke eksponert. Originalprompt er bevart ordrett før separat kildepresisering. Alle 15 faktiske kall er ført i c-proveniens.json med rå- og prompt-SHA. Felles atlas/kall telles per berørt jobb i manifestet, men er ikke separate duplikatkall. Råforsøkene og oppskrifter er bevart. Import, runtime, animasjonstiming og ny individuell brukergodkjenning er ikke utført. Root gjør samlet mottak.
