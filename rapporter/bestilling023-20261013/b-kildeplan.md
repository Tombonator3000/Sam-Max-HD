# Kildeplan for bestilling 23

Kun analyse og rapporter. Alle 40 poster i kildehash.json er verifisert mot nåværende filer uten avvik; låsefilen er ikke skrevet om. Alle ti originalkomposisjoner, metadata, objektutsnitt, aktuelle prompter, ressursregisteret og begge leverte rom007-HD-ankre er lest. Ingen jobbfiler, bilder til produksjon, kode, Git eller globale logger er endret.

## Leveringskontrakt og koordinater

Dette er opake fullromslag, ikke spriteatlas. Alle ti har 1536 x 1024 canvas, motivfelt [0,112,1536,800] og grå RGB128-padding. Svart inne i rommet er faktisk rominnhold, blant annet tak, forgrunn og skygger. Det skal ikke gjøres transparent eller fylles med nye detaljer.

Første jobb, lag007_02_del2av2, har romregion [104,0,384,200]. Den må senere klippes ved x = 416 fra C sin låste lag02-master på 1952 x 800, og plasseres ved y = 112. Originalens overlapp med lag02 del 1 er bekreftet byte-identisk på 280 x 200 originalpiksler, altså 1120 x 800 HD. C sitt sluttmanifest finnes ikke på analysetidspunktet; masterhash, kandidatvalg og kontroll av del 2 må innhentes før klipp. Ingen nygenerering av denne jobben er nødvendig eller ønskelig.

Resten er lag007_03_del1av2 til lag007_11_del1av2, alle region [0,0,384,200]. De trenger ikke en ny panoramamaster per TV-bilde dersom det dokumenterte uendrede HD-rommet gjenbrukes. Ingen andre originaldeler behøves for TV-objektene, som ligger helt innen del 1.

| Objekt | Originalrekt i hele rommet | HD-rekt i aktuell del |
| --- | --- | --- |
| obj075_01, lag02 del 2 | [416,48,16,8] | [1248,304,64,32] |
| obj071_03 til 0B, lag03 til 11 | [144,88,24,24] | [576,464,96,96] |
| obj076_01, bare lag03 | [0,128,32,24] | [0,624,128,96] |

Objekt071 sine suffikser er HEKSADESIMALE tilstander. Lagnummeret er desimalt: lag10 inneholder obj071_0A, desimal 10; lag11 inneholder obj071_0B, desimal 11. Ikke let etter eller lag obj071_10/11 som erstatning. Nummerrekkefølgen beviser ikke alene runtime-timing.

## TV-motiv og palett

Registeret kaller071 «office-tv». Bildet er ikke statisk støy; denne har et annet registerobjekt078. Den hvite/grå skrå TV-kassen, de tre grå betjeningsformene til høyre og brun bordbakgrunn ligger i 24 x 24-komposittboksen. Skjermen viser grønn bakgrunn med en mindre rødbrun/oransje ansiktsform til venstre, blått felt under denne, og en større lys beige/oransje profil til høyre med svart øyepunkt, hvit/rød/brun munn-/snuteform. Navn på personer, dyr eller film er ikke bevist, og skal ikke tilføyes i prompten.

Alle ni TV-boksene har nøyaktig samme sett med 61 RGB-farger, inklusive kasse og bakgrunn. Fargefordelingen og pikselplasseringen endres. Viktige motivfarger er grønn (7,127,67), lys hud/beige (255,199,135), varm rosa (255,143,115), oransje (231,139,83), rødbrun (155,79,59), mørkerød (139,7,7), hvit (251,251,251) og svart (0,0,0). Fullstendige fargeantall finnes i b-palettbevis.json. Ikke moderniser dette til fotorealistiske ansikter, en ny TV-serie, logo, tekst eller en svart avslått skjerm.

| Jobb / tilstand | Synlig motivforskjell | Endring fra foregående i denne bestillingen |
| --- | --- | --- |
| lag03 / 03 | Høyre lyse profil med utstrakt hvit munnlinje; mørkt felt under munnen. Venstre mindre ansikt står ved siden av. | Egen startvariant; 20 TV-piksler forskjellig fra04. |
| lag04 / 04 | Munnen er mer kompakt, med hvite nedre felt og mørkerød innside; venstre ansikts lille mørke detalj endres. | 20 TV-piksler. I tillegg seks piksler i telefonsvarerfeltet skifter tilbake til grunnrommets mørkere indikator. |
| lag05 / 05 | Den store lyse profilen strekker seg mer vannrett mot venstre, med lang hvit overkant og mørkerød innvendig flekk. | 77 TV-piksler, romboks [150,90,12,13]. |
| lag06 / 06 | Samme hovedprofil som05, endret hvitt/beige/rødbrunt felt under venstre side av snute/munn. | 10 piksler i [150,98,5,3]. |
| lag07 / 07 | Samme lange profil; mørkt felt nær venstre ansikt og nedre munnlinje endres. | 11 piksler i [150,93,5,6]. |
| lag08 / 08 | Samme profil; mer sammenhengende lyst felt til venstre og mindre mørk/rød markering ved munnen. | 11 piksler i [150,93,5,6]. |
| lag09 / 09 | Tilbake til04-liknende kompakt munnform. | 81 piksler fra08. Mot04 er KUN én piksel forskjellig, se nedenfor. |
| lag10 / 0A | Den lyse profilen blir kortere/smalere til høyre, munnfeltet mer loddrett; svart øyepunkt fortsatt synlig. | 62 piksler i [149,91,13,14]. |
| lag11 / 0B | Samme hovedstilling som0A; øyefeltet blir brun strek/felt, og venstre figur får endret mørk munndetalj. | 7 piksler i [149,94,12,9]. |

Dette er beskrivelser av små synlige former, ikke en bekreftet handling eller filmidentitet. Kontaktarket b-tv-objektkontaktark.png viser hver variant forstørret uten interpolasjon. Eksakte RGB-overganger og koordinater fra foregående tilstand ligger i b-differansebevis.json.

Den ene forskjellen04 til09 ligger på romkoordinat (150,100), TV-lokal (6,12): svart (0,0,0) blir rosa (255,143,115). På HD-canvas svarer dette til [600,512,4,4]. Disse tilstandene må ikke dedupliseres bare fordi motivene ser nesten like ut. Koordinaten er analysebevis, ikke en tillatelse til å lime inn den oppskalerte originalpikslen.

## Telefonsvarer og øyetilstand

Obj076 heter «office-answering-machine». Lag03 viser fortsatt den røde telefonhånddelen over apparatet; dette er ikke lag02 sin telefon uten rødt rør. Endringen mot grunnrommet er bare seks piksler ved rom x10..12, y133..134 i den lille grønne indikatoren. Feltet blir lysere grønt med (51,107,35) og (115,183,55), fra mørk oliven/grønt. På HD svarer hele endringsboksen til [40,644,12,8]. Selve apparatkassen, tastene, telefonen, bordet og mørke felt skal ikke tegnes om for å markere dette.

Obj075_01 i lag02 del 2 viser skalle-/øyefeltet på hyllen. Mot grunnrommets tilsvarende felt endres tre piksler: lokal (0,0) til blåhvit (187,207,227), og lokale (6,3)/(12,4) til grønn (115,183,55). Originalen støtter altså små grønne øyefelt, ikke ny figur eller større hode. Dette skal allerede håndteres i C sin master fra22. b-ovrige-objektkontaktark.png og b-mikroendringer.json dokumenterer begge småtilstandene.

## Bevis for bakgrunnsgjenbruk

Lag04 til11 er BYTE-IDENTISKE med grunnrom007 del 1 utenfor TV-rekt [144,88,24,24]. Hver har199 forskjellige piksler mot grunnrommet, alle inne i skjermens romboks [146,90,16,16]. Lag03 har de samme199 TV-pikslene pluss de seks indikatorpikslene. Utenfor TV- og076-rektene er alle ni originaler identiske. Derfor er også alle svarte romflater og samtlige øvrige bakgrunns-/objektfelt identiske utenfor disse rektanglene. Forskjellige totaltellinger av svarte piksler skyldes de små motivendringene, ikke nye svarte romåpninger.

IKKE bruk lag02-masteren direkte som bakgrunn for03 til11. Lag03 mot lag02 del1 har1000 endrede piksler, hvor960 ligger utenfor TV/076. Telefonfeltet og vindusfeltet har egne tilstander i lag02. Målt i de aktuelle metadatafeltene:312 endrede piksler i telefonrekt [0,112,40,24],669 i vindu [240,48,24,56],21 i076-boksen og19 i TV-boksen. Telefon- og076-boksene overlapper; disse tallene kan derfor ikke summeres som disjunkte områder. Lag03 og senere følger grunnrommets røde telefonrør og vanlige vindu, ikke lag02 sin variant.

De leverte HD-ankrene er sett og hashført i b-differansebevis.json. Del1 SHA er 00a82be6b79380c8f5ff1da07a3a43d39eead22aa81d111773514be40f1e3a82. Del2 SHA er e1d9c0685e40e35f11a316bcc3b0a06463fba798b306a18d00c3d6e2d9aa26d9. At de er leverte/stilankre er ikke påstand om ny individuell godkjenning.

## Trygg produksjonsform og arbeidsdeling

Forslag: C eier eksakt klipp av lag02 del2 fra egen sluttmaster. Én agent bør eie hele TV-familien03 til0B for å unngå ni ulike figuridentiteter eller fluktuerende TV-kasser. En annen kan uavhengig QA-kontrollere mikroendringene og obj076. Dersom produksjonen deles, grupper03/04/09 sammen,05/06/07/08 sammen og0A/0B sammen, med avtalt felles nytegnet TV-kasse og bakgrunn.

Gjenbruk riktig rom007 del1-HD utenfor dokumenterte rektangler. Generer de små TV-motivene med originalutsnittet og riktig levert HD-rom som kontekst. Nygenererte komponenter kan helskaleres/plasseres i TV-boksen, med samme kasse og ramme gjennom familien. For mikrovariantene kan et lokalt innebygd imagegen-edit bevare resten av en god nytegnet variant byte-identisk. Ingen kopiering av originalpiksler, fargemasker fra originalen, silhuettmaskering, warp eller numerisk korrelasjonsjakt. Endringen må være synlig som riktig nye motivform/fargeområde, ikke bare ulik filhash. En tilfeldig variasjon er heller ikke dokumentasjon på originaltilstanden.

Kontroller original og HD samlet, hvert TV-utsnitt, indikatorfelt og svarte romflater. Kjør den uendrede checkerens helbilde- og perobjektkontroll; merk at nesten likt rom kan skjule feil TV-innhold numerisk. Dokumenter småforskjellene visuelt og med posisjon/fargeanalyse. Ingen generering, import, runtime, originaltiming eller ny individuell brukergodkjenning er utført i denne analysen.

## Reproduserbare analysefiler

b-analyse.py.txt bygger kontaktark, fullpaletter og RGB-differanser. b-differansebevis.json inneholder kildekontroll, differansebokser, nullavvik utenfor rektangler og ankerhash. b-mikroendringer.json inneholder de eksakte småtilstandene og registerutdrag. b-rgb-differanser-mot-lag04.png viser absolutt RGB-differanse i kildeoppløsning; dette er et diagnostisk bilde, ikke en produksjonsmaske. Ingen originalavledet maske er brukt til bildekomposisjon.
