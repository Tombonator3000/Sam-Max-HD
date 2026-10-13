# Bestilling 17 A: produksjon og visuell QA

Rom070 begge deler og rom071 er levert med teknisk OK. Det betyr ikke at alle indre detaljer eller små glyffer er kildeidentiske. Særlig pizzaeskens etikett har fortsatt visuell restusikkerhet.

## Kilde og arbeidsmåte

a-kildeplan.md beskriver motiv, palett og lag før produksjon. Rom070s feilaktige flat-gray-note er eksplisitt korrigert i separat prompt: originalen har 26 fargede påkledningsdeler, ikke grå silhuetter. Rom071s PUSH ME-/pilnote gjelder separate objekter og er utelukket. Beskyttede promptfiler er ikke endret; ordrett tekst inngår i a-rom070-prompt.txt og a-rom071-prompt.txt.

Rom070 ble samlet fra begge originaler som 1920 × 800 referanse, kun til analyse/generering. Ingen av disse oppskalerte originalpikslene inngår i leveransene. Godkjent stil/rom007_del1av2.png ga malt kvalitet. Én fullgenerering ga alle 26 grupper; et andre innebygd imagegen-kall forsøkte å rette pizzalokkets glyffer. Bare rektangelet [1290,48,200,84] fra den nye rettingen ble satt inn i første nytegnede master. Ingen maske eller kontur fra originalen er brukt. Resten av masteren er byte-uendret.

Rom071 er nytegnet fra original med hovedark/sam.png og hovedark/max.png som identitets-/stilstøtte. Originalen styrer posisjon, brun/hvit palett og grunnfigurtilstand. Ingen standarddress, hatt, knapp eller pil er lagt til. Sam har det lille røde plagget, Max har hvit kropp og rosa øreinnside.

Verktøyet er innebygd ChatGPT-bildegenerator; eksakt modellnavn er ikke eksponert. To kall for rom070 inklusive etikettforsøk, ett for rom071. Råbilder, komplette prompter og første master er bevart.

## Presis plassering og teknikk

Valgt rom070-master er 1920 × 800. Del1 klippes [0,0,1536,800], del2 [384,0,1536,800], begge ved (0,112) på RGB128-lerret. Overlappen 1152 × 800 er byte-identisk, bekreftet i a-kildebevis.json. Master SHA256: e85626a3f155cc7b2230fea79a9ad5f77975b8107d3407a6248a783b7a2e7cbd.

Rom071s genererte motiv [128,112,1280,800] plasseres uten lokal omforming på nytt 1536 × 1024-lerret. All padding er eksakt RGB (128,128,128). Ingen warp, vektortrace eller originalsilhuettmaske. a-oppskrift.py.txt rekonstruerer resultatene fra råbilder og sammenligner byteverdier.

| Leveranse | Uendret checker | Global / blokk / kant |
| --- | --- | --- |
| rom070_del1av2 | OK | 0,07 / 0,20 / 0,96 |
| rom070_del2av2 | OK | 0,06 / 0,24 / 0,96 |
| rom071 | OK | 0,03 / 0,08 / 0,97 |

Alle 44 låste kilder er verifisert uendret. Slutt-SHA og kontrollfiler står i a-leveranser.json; rå-SHA og overlappbevis i a-kildebevis.json.

## Kontroll av de 26 delene

Alle 26 objektbokser fra registeret er sammenlignet i a-rom070-26-deler-qa.png. De er egne grupper som er til stede i riktig felt, ikke en påstand om at hvert ornament har identisk pikselantall. Boksene overlapper og inneholder av og til deler av naboen, slik kilderegisteret også gjør.

| Kildeobjekt | Synlig identitet og kontroll |
| --- | --- |
| 685 | Grønt speiderantrekk, gul halsduk, beige ermer; ingen kropp fylt inn |
| 686 | Mørkt metallantrekk og to piggstøvler |
| 687 | Hvit brudekjole, puffskuldre, hansker og åpent halsfelt |
| 688 | Rødt/svart vampyrantrekk, hvit krage/hansker og liten mørk detalj til høyre |
| 689 | Rødt/gult tyrefekterantrekk, hvite strømper og svarte sko |
| 690 | Svart/hvitt pizzaantrekk med pizzaeske; glyffer har restusikkerhet |
| 691 | Blå/gul pysjamas med ansiktsmønster og to føtter |
| 692 | Mørkt dykkersett, blå detaljer, åpen maske og to svømmeføtter |
| 693 | Rødt flerbruksverktøy med utbrettede metallredskaper |
| 694 | Rød/gul gitar med blågrå hals; retning og plass bevart |
| 695 | Grå fugle-/kyllingrekvisitt med oransje nebb/føtter og løs fjær |
| 696 | Rød/hvit bukett med grønt løv; indre kronbladfordeling ikke sikkert tellbar |
| 697 | Mørk flaggermus med to vinger og røde detaljer |
| 698 | Langt lyst sverd, gult håndtak og diagonal retning |
| 699 | Rød kappe med gult øvre skaft og hull/rifter |
| 700 | Gult pizzastykke med røde felt og hengende ost |
| 701 | Brun teddybjørn med gul halsduk og rosa poter |
| 702 | Grønn/gul vekkerklokke og mørk opprullingsdel |
| 703 | Grønn speiderhatt og åpent ansiktsfelt |
| 704 | Svart punkhår med åpen ansiktsplass og liten gul detalj |
| 705 | Hvitt slør, folder og grålilla skygge |
| 706 | Løs tann-/munnrekvisitt med hvitt og rødt; ingen nytt ansikt |
| 707 | Liten svart beretform |
| 708 | Rød/gul lue med mørk brem |
| 709 | Oransje gresskarhode, grønn stilk og hvit tannrekke |
| 710 | Grå/farget tyggegummihode med rød 1¢-form og hvit munn |

Tomrom og kremfarget bakgrunn er bevart. Ingen nye Max-kropper er satt inn i klærne. Søm og klipp er kontrollert fra samme master.

## Restusikkerhet og leveransegrense

Første master skrev et tydelig LeChuck-lignende navn og PIZZA på esken. Originalforstørrelsen a-pizza-kilde-lesing.png viser små ujevne tegn; navn er ikke sikkert avklart. Andre imagegen-forsøk gjør tegnene mer ujevne, men øvre linje kan fortsatt leses som et navn. Dette er ikke fullt løst eller kildebevist. Valgt master har den smale rettingen; originalformen er ikke byttet inn eller brukt som maskering. Teknisk OK skal ikke brukes til å erklære denne teksttolkningen godkjent.

Små detaljer som blonder, kronblader, sømmer, prikker og gitarens stemmeskruer er mer artikulert i HD. Gruppeantall, hovedfarge og plass er kontrollert; ikke alle indre smådetaljer kan sertifiseres som eksakt samme antall fra den lave kilden. Rom071 har glatt skyggelegging og mer artikulert ansikt/tannlinje; kildepose og figuridentitet er kontrollert, ikke pikselidentisk strekføring.

[a-rom070-26-deler-qa.png](a-rom070-26-deler-qa.png) og [a-rom071-qa.png](a-rom071-qa.png) er visuelt undersøkt. Ingen motorimport, påkledningsfunksjon, interaksjon, runtime eller ny individuell brukergodkjenning er testet/påstått. Parent håndterer samlet batch, eventuell videre etikettavklaring, kø og Git.


Etikettens før/etter-visninger er bevart som a-etikett-for.png og a-etikett-etter.png. a-etikett-bytebevis.json dokumenterer fire rektangler som til sammen dekker ALT utenfor rettingen; alle er byte-identiske med første master. Registerets dominos-navn er kontekst, ikke bevis for et bestemt trykt merkenavn.
