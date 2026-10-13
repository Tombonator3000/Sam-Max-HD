# Bestilling 19 B, kilde-QA

GRUNNLAG og C sin kildeplan er lest. Originalene 821/822/823 og tom hånd828 er sett før generering. Alle 40 beskyttede kilder stemmer fortsatt med kildehash.json. Kun eide resultater/notater og B-rapportfiler er endret.

| Jobb | Forsøk | Valgt | Uendret checker, global/blokk/kant | Utfall |
| --- | --- | --- | --- | --- |
| obj821_01 | 1 | 1 | 0,30 / 0,77 / 0,94 | OK |
| obj822_01 | 2 | 1 med lokal retting fra2 | 0,70 / 1,14 / 0,94 | SJEKK |
| obj823_01 | 4 | 2 med lokal retting fra3 | 0,07 / 0,15 / 0,96 | OK |

822 er ikke kalt teknisk OK eller klar for mottak. Blokkavvik 1,14 består. Ingen FEIL eller terskelendringer er skjult.

## Identitet og tilstand

Alle tre viser den samme tørre brune Jesse James-hånden, grønn golfballhenter og rød/oransje fiskemagnet med grønne finner, malt øye og to grå metallender. Ingen slange, levende fisk, monster eller Sam-hånd er innført. Fem fingre er delvis overlappet/tildekket i grepet; synlige neglspisser og fingerforløp er kontrollert mot kilden og C sine åpne håndvarianter. Ikke alle fingre skal gjøres fullt synlige i hver avkutting.

821 har to separate grønne leddsegmenter og ingen farget ring. 822 har to segmenter og ring med svart/grå bøyle og cyan/blå/grønn/lilla/rosa flate. 823 har ett separat segment, diagonalt avklipt brun håndleddsrest, separat avklipt hånd/magnetgruppe og stort svart mellomrom. Ingen manglende armforbindelse er tegnet inn. Ring og høyrekant følger denne avkuttingen.

## Rettelser og familieutveksling

823 første helforsøk fikk FEIL, blokk30,18, med endret segmentplassering og diagonal avkutting. Ny generering fra bare originalen ga OK. Første feilforsøk er bevart og er ikke anker for nytegningen.

C undersøkte B-familien og bekreftet hånd-/magnetidentitet, tom821/ring822 og konsistens med tomme håndvarianter. C påpekte også at 822 sitt nedre gule leddpunkt var for helt rundt. Lokal innebygd imagegen rettet den delvis skjulte formen. Innfelt rektangel [638,388,61,50], resten byte-identisk.

823 sitt lille gule leddpunkt ble tilsvarende undersøkt. Lokal retting fra forsøk3 er valgt i [482,306,60,60]. Forsøk4 ga en tydelig rektangulær fargeovergang og er forkastet selv om den tekniske kontrollen ikke alene fanget dette. Valgt lokalretting bevarer delvis skjult gul form og bedre kontinuitet med grønn mekanikk; en liten forskjell i grønn glans ved innfellingsgrensen er fortsatt et detaljforbehold. Resten av valgt helforsøk2 er byte-identisk.

B har også sett C sitt oppdaterte familieark: 828 sin diagonale håndavkutting og 830 sitt delvis skjulte leddpunkt er forbedret, og åpne femfingrede hender har samme rekvisittidentitet. Denne visuelle utvekslingen er ikke bruker- eller runtimegodkjenning.

## Tekniske grenser og stilforbehold

Alle leveranser er 1536 × 1024 med egne metadatafelt og eksakt RGB128-padding. Kun helskalering, klipp/plassering og avgrenset innfelling av nygenererte rektangler er brukt. Ingen originalkonturmasker, innlimte originalpiksler, lokal geometrisk warp eller vektortrace. Originale prompter er bevart ordrett som prefiks til faktisk brukte presiseringer. Eksakt bildemodell er ikke eksponert.

Nytegningene har tydeligere, blankere negler, metall og grønne kantlys enn originalen, og jevnere/litt kraftigere hudrynker. Ringflaten er glattere enn originalens fargedithering. Små finger-, finnekant- og metallfasetter er tolkning, ikke pikselidentitet. Svart tomrom er visuelt beholdt; ingen miljøbakgrunn eller tekst er lagt inn.

b-familie.png viser original til venstre og valgt HD til høyre. b-proveniens.json, b-lokalretting.json, råbilder, faktiske prompter og .py.txt-oppskrifter dokumenterer forløpet. Motorimport, transparensmaske, håndens skriptsekvens og timing er ikke testet. Runtime=false og ny_brukergodkjenning=false.
