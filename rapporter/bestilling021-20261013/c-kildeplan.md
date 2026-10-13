# Kildeplan for bestilling 21

13. oktober 2026. Kun kildelesing og rapporter; ingen bildegenerering, jobbfiler, Git-mutasjon eller globale logger. Ti jobber fra GRAFIKKLISTE.md er låst med 40 SHA-256-poster i kildehash.json. Originaler er sett samlet og enkeltvis i 4×, metadata og promptnoter gjennomgått, ressursregisteret konsept/2026-10-12/objektbilder-959.csv og relevante docs/gpt-romnotater.csv fra origin/main lest. source-faithful-production brukes som analysegrunnlag.

## Avgjørende kildekorreksjoner

- Rom091 er et fullt fargelagt kles-/rekvisittark, slik rom070 også er. Generisk silhuettnotis må ikke få generatoren til å erstatte klærne med grå flater.
- Obj850 er en annen faktisk tilstand: surferutstyret er erstattet av en flat lilla/grå silhuett, mens andre avklipte objekter og merket ved siden av fortsatt er fargede. Ikke gjeninnfør surfebrettet her.
- Rom090 viser ikke hele Sam og Max med pistoler: bare Sams avskårne hode med hatt og Max sine to avskårne ører i et blått scene-/hyllefelt. Ikke fullfør kropper, Max-hode, hender eller pistoler fra navnet.
- Lag002_01 er et opakt rombilde med seks objekter komponert på plass, ikke et rutenett med transparente sprites. Ekte alfa og figurarkets rutemaskeregler gjelder ikke denne typen.

## Rektangler og paletter

Alle leveringslerret er 1536 x 1024 med RGB (128,128,128) utenfor motivfeltet. Rektangler bruker [x,y,bredde,høyde]. c-metadata.json og c-paletter.json bevarer full metadata/palettgrunnlag.

| Jobb | Originalregion | HD-motivfelt | Farger |
| --- | --- | --- | --- |
| rom089 | [0,0,320,200] | [128,112,1280,800] | 139 |
| rom090 | [0,0,320,120] | [128,272,1280,480] | 41 |
| rom091 del 1 | [0,0,384,200] | [0,112,1536,800] | 148 |
| rom091 del 2 | [280,0,384,200] | [0,112,1536,800] | 151 |
| obj850_01 | [0,0,120,136] | [528,240,480,544] | 103 |
| rom092 | [0,0,320,200] | [128,112,1280,800] | 21 |
| obj901_01 | [0,0,128,128] | [512,256,512,512] | 8 |
| obj995_01 | [0,0,320,200] | [128,112,1280,800] | 5 |
| obj996_01 | [0,0,320,24] | [128,464,1280,96] | 32 |
| lag002_01 | [0,0,320,200] | [128,112,1280,800] | 122 |

## Rom089

Hyssingballen fra ny vinkel: enorm brun/beige kule med konkrete viklingsbånd, liten bygning/platform på toppen, trær foran og bak, liten rød takbygning ved foten og forgreinende grå gangsti. Høyre forgrunn har stor trestamme, trapper/rekkverk og skilt. TRAM og to MUSEUM-forekomster må bevares med kildeplassering og piler. Ett MUSEUM er mørkt på lyst felt og det nederste rødt på mørkt. Ingen ny lesbar tekst på det lille skiltet ved stien dersom kilden ikke støtter det. Paletten er dempet skoggrønn/brun med blå himmel, lyse skyer og sterke røde skiltaksenter. Ikke importer bil eller annet utsnitt fra rom027.

## Rom090

Blått panoramafelt, bare 320 x 120 originalpiksler. Tre hyller på hver side inneholder mørke blå flaske-/figurformer. Mørk buet topp med hengende rundinger, blå drapert front nederst og lyst blått tomrom i midten. Sams brune hode med blågrå hatt er avskåret rett under munnen; to beige/rosa Max-ører er separate uten ansikt. Originalen gir ikke tillatelse til å gjøre disse til komplette figurer eller våpen. Bevar samtlige hyllesilhuetter som synlige former; eksakt gjenstandsidentitet er ikke dokumentert fra hver mørke figur. Hovedark kan bare støtte identitet der kilden faktisk viser deler.

## Rom091 og obj850

Fulloriginal 664 x 200, begge deler finnes i samme bestilling. Master bør være 2656 x 800, med klipp x = 0 og x = 1120, hvert 1536 x 800. Overlapp 104 originalpiksler / 416 HD-piksler er kontrollert byteidentisk. Ingen ekstra originaldel fra bestilling 22 trengs. c-rom091-original-full.png er kildesammensetting.

Farget ark på ensfarget lys beige bakgrunn med lilla/grå slagskygger. Klærne er tomme: ingen nye hoder, hender eller kropper inni dem. Venstre del viser gul/grønn arbeids-/cowboybekledning med blå bukse og støvler; gul/svart hår-/parykkform; sag med grønt håndtak og røde merker; mørk dress med lilla magebånd; kokkehatt; oransje/grønn skjorte med svarte bukser og stor beltespenne; brunt mykt hodeplagg; hvitt skjegg; lite gult rundt objekt med kors; grønt todelt hodeplagg; rød/hvit bandana; svart flammebrett med lilla/gule shorts og blå svømmeføtter; femkantet hvitt merke med svart form; liten blå stang med hvit ende; grå hodeskalle-/dyremaske; rød/hvit stripet skjorte med hvite sko. Bevar de konkrete avkuttingene i delgrensen.

Høyre fortsetter samme klær og viser grønne solbriller, lilla/grå topphatt, hvitt/flekket forkleantrekk, gul medaljong, lite svart krusedull-/insektaktig element, brennende rød gjenstand med svart håndtak, brun frakk med støvler/blå bukser, lang svart stang, brun buet kles-/remform, hvit skjorte med mønstret midtbånd, grønt blodflekket medisinsk antrekk med stetoskop, grå frakk med åpen kasse/gul prislapp, hvit tube med røde bokstavformer, gul krok/stang med brun håndform og stor grå spade med rødt skaft. Disse beskrivelsene er visuelle; ikke fastslå uklar rekvisittfunksjon eller eksakte småord ved gjetning. Prislapp/tube har synlige glyfer som må kopieres, ikke erstattes med nye ord eller priser.

Obj850 har romposisjon [88,64,120,136], register sam-surfer-image. Det viser stor flat lilla/grå flammebrett-/shorts-/svømmeføttsilhuett på beige, men beholder det hvite femkantmerket og avklipte naborekvisitter. Silhuetten skal forbli uten innvendig brettdetalj, flammer eller shortsdekor. Skillet mellom rommet og denne tilstanden må dokumenteres ved produksjon. Runtime for valg/avkledning er ikke testet.

## Rom092 og obj901

Rom092 viser en stor oransje/brun pompadour-/hårform på en enkel tanfarget støtte og brun sokkel i varmt rødt lys. Mørk rød loddrett bakgrunnskant til høyre og brun høyresone. Ingen øyne, munn eller komplett levende person. Eksakt eierskap/navn på hårformen er ikke bevist her; bevar motivet uten å normalisere paletten til en figur fra hovedark.

Obj901, register alcove-stand, har romposisjon [120,32,128,128]. Dette er TOM tilstand: rød bakgrunn og mørk bakgrunnsskjøt, med bare toppen av brun sokkel nederst. Ikke behold hårform eller den høye støtten fra rom092. Åtte kildefarger, svært store flate felt; ikke tilføy tekstur som endrer mørke-/fargegrenser.

## Obj995 og obj996

Obj995, register dsf, er et brunt skjevt beholder-/inventarunderlag på svart. Fem farger: svart samt (67,35,11), (99,55,19), (123,83,39), (171,87,0). Ujevn ytterkant, brettede kanter og flere indre felt/linjer; svak sentral emblem-/bokstavstruktur og liten tekstlinje. Eksakt tekst er ikke sikkert transkribert. Bevar synlig retning, lav kontrast og glyfformer; ikke roter, speilvend, kontraststrekk eller skriv ny tydelig logo. Ressursnavn dsf fastslår ikke materialet eller runtimefunksjonen. Ingen inventargjenstander legges inn i de tomme feltene.

Obj996, register dashj, er et 320 x 24 utsnitt av UI-felt, ikke en komplett ikonmeny. Svart mellomrom, beige knappefelt med brun/oransje kant. Synlige delmotiver er blant annet magenta/rød diagonalform og spørsmålstegn, rød hånd, blå apparatform, blått/oransje kart-/skjermfelt og hvite/grønne papirer. Både øvre og nedre ikonrader er AVKLIPT ved utsnittskantene. Ikke fullfør ikoner eller skjulte etiketter, legg på rammer rundt hele stripen eller fyll svarte felter. Ikonenes eksakte funksjoner er ikke runtimeverifisert. Svart er kildeinnhold her, ikke automatisk transparent nøkkelfarge.

## Lag002_01: seks objektbilder på rommet

BESTILLING.md «Lagjobber (små objekter)» og jobbens prompt sier å male hele rommet inklusive objektene på eksakte posisjoner. `type=lag`, `lag=1`, `underlag=[]`; bilde to er `jobber/rom002/resultat.png`. Det er ikke et seksrutet kontaktark som skal reorganiseres. Ruteboksene er klippvinduer på det sammensatte rommet.

Rom002-ankeret er visuelt lest og samsvarer med SHA i rapporter/bestilling002-20261013/a-leveranser.json: `51a93c112da67447d8f7e0b623e7d31bf5a96eb8a4f6da9919e3b3291d3825a4`. Det er registrert teknisk OK; gammel manifestpost har tom_godkjent=false og runtime_verifisert=false. Gjeldende ordre autoriserer bruk som bilde to, men dette skal ikke omtales som dokumentert separat individuell godkjenning. Bevar samme blåfiolette steinvegger, apparater, oransje ledninger, grønne elektriske lys og gul lyspøl.

| Objekt / tilstand | Originalboks | Boks på HD-lerret | Faktisk kildeinnhold |
| --- | --- | --- | --- |
| obj052_01 | [176,104,64,16] | [832,528,256,64] | Register car-windshield: lav blå/mørk glass-/bilrutedel med oransje lyspunkter til venstre. Ikke tegn en hel bil. |
| obj053_01 | [104,152,40,32] | [544,720,160,128] | lab-rock-1: lys grå/blå nedrast murstein på gulvet. |
| obj055_01 | [160,168,48,32] | [768,784,192,128] | lab-rock-3: mørk blå stein foran/ved løs pære og skalle. Bevar pærens overlapp. |
| obj896_01 | [248,168,16,8] | [1120,784,64,32] | lab-light-2: bitte liten gul/oransje lys-/knappvariant ved panelet, ikke stor ny lampe. |
| obj897_01 | [104,40,56,48] | [544,272,224,192] | lab-light-3: egen tagget limegrønn lyskrans rundt blåhvit apparatkule. |
| obj900_01 | [8,48,40,32] | [160,304,160,128] | lab-light-4: grønngul kule med lilla elektrisk krans under venstre apparat. |

c-lag002-rutebevis.png viser hver originalboks mot rom002 uten laget. c-lag002-rutekart.json har bokser og antall ulike kildepiksler mot grunnrommet: 900, 419, 436, 23, 99 og 75 i rekkefølgen over. Særlig små lysvarianter kan lett forsvinne dersom HD-ankeret kopieres blindt. Ingen kildeobjekter overlapper hverandres rektangler i dette laget. Obj052s svevende rutedel er tilsiktet separat komponent, ikke grunn til å finne opp underliggende bil.

Neste bestilling inneholder lag002_02..05. Lag002_02 metadata har bil obj051_01, annen stein obj054_01, lys obj992_01 og obj897_02. De skal ikke importeres inn i lag 01. Lagnummer er en pakkegruppering av tilstander/ikke-overlappende objekter; dette er ikke bevis på kronologisk animasjon eller en samlet runtimehendelse. De senere lagene trengs ikke som ekstra originaldel til en master i bestilling 21.

### Alfa, nøkkelfarge og checker

Ingen transparent bakgrunn, nøkkelfarge eller alfarutekart er angitt for lag002 i jobb.json eller prompt. Lever vanlig opakt RGB-PNG med hele rommet og grå padding. BESTILLINGs ekte-alfa-/rutekartkrav gjelder figurark, ikke lagtypen. Svart/lilla/grønt i laboratoriet er motivfarger og må ikke chroma-keyes bort. Originalmasker skal ikke brukes til å skjære nytegningen.

Uendret `verktoy/sjekk_leveranse.py` ruter lagtypen til `check_picture`, som konverterer resultatet til RGB. Hele bildet kontrolleres for forskyvning, blokkforskyvning og kantlikhet. OK-grenser er 0,75 / 1,0 / minst 0,55; SJEKK-grenser 1,5 / 2,0 / minst 0,40. Deretter undersøkes hver oppført objektboks med kantkorrelasjon: OK minst 0,60, SJEKK fra 0,50, FEIL under 0,50. Bokser under 4 piksler i bredde/høyde eller originalkantstandardavvik under 1,0 hoppes over. De seks aktuelle boksene er alle store nok; ikke anta at en stille checkerutskrift beviser separat motividentitet. Ingen alfatest utføres for lag. Bruk full canvas for entydig plassering selv om generelt bildeformat også tillater passende utsnitt.

Leveringsbevis bør omfatte resultat/notat, faktisk prompt og råforsøk, SHA, plasseringsoppskrift, uendret checker, samlet romsammenligning og egne nærbilder av alle seks boksene. Rapportens rutekart er analysebevis, ikke et pålagt alfarutekart. Importørens senere klipp/maskering og spillruntime er ikke utført eller verifisert her.

## Anbefalt arbeidsdeling og åpne forhold

A: rom089, rom090, rom092 og obj901. B: hele rom091-paret samt obj850, slik én fullmaster og den særskilte silhuettilstanden vurderes samlet. C: obj995, obj996 og lag002_01; lagtypen får egen seksobjektskontroll. Dette er forslag, ikke produksjonsstart.

Største feilrisikoer er at klesarket gjøres grått, at obj850 får surferutstyret tilbake, at rom090 fullføres til hele figurer, at obj901 får hår/støtte, at UI-stripen fullføres, at svak tekst i obj995 gjettes, og at små lys-/steinlag i labben uteblir fordi grunnrommet ligner. Usikker småtekst og funksjon bør bevares som kildeform fremfor ny tolkning. Ingen nye kilder fra bestilling 22 er nødvendige for fullstendig rompanorama i denne gruppen. Ingen runtime, timing, import eller brukergodkjenning er verifisert av denne analysen.
