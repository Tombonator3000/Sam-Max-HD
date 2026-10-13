# Bestilling 29 A, kilde og egenkontroll

Fem leveranser er produsert: lag019_02, lag019_03 og lag020_01/02/03. Root-kildeplanen, alle fem originalkompositter, metadata, riktig levert rom019/020-HD og nærbilder er lest. Kildeplanens to Max-poser, egne underlag og tre skap/kistetilstander er beholdt. Det finnes ikke GRUNNLAG.md her ved produksjonsstart; roots uttrykkelige bestilling og root-kildeplan.md er arbeidsgrunnlaget.

## Motiv og tilstand

019_02 har egne bredt bøyde ører, kremfarget pels, rosa øreinnside, små svarte øyne, oransjerød nese, hvit sikksakk-tannrekke og poter ved venstre brettkant. Venstre øre/pote forblir avklipt. Sam har armen nede. 019_03 har rettere ører og det kildeegne større underlaget med utstrakt lilla dressarm, brun hånd, rød redskapsende og avskåret lys form over hånden. Den loddrette avkuttingen ved x512 er faktisk i originalkompositten og er bevisst beholdt. Redskapets funksjon/timing er ikke bevist. Begge har fem tomme svarte hull og intet poengpanel.

019_03 er satt sammen fra ett sammenhengende nytegnet felt [128,240,896,544], tilsvarende obj199-underlagets romrektangel [0,32,224,136]. Dermed følger de 3676 endrede kildepikslene utenfor Max-boksen med. Ingen blind gjenbruk av tom armstilling. Øvrig rom-HD er byte-identisk utenfor dokumentert felt.

020_01 viser åpen rosa venstre skapdør, mørk rød åpning, høyre dør/håndtak og lukket blå kiste. 020_03 bruker samme nytegnede skap med sitt eget kortfelt; alt utenfor [1080,456,68,52] er byte-identisk mellom de to. Fullsceneutkastet utelot et grått punkt på den tomme døren og forenklet kortets brunlige stripe. To lokale imagegen-kall rettet dette. Punktet er nytt generert grått motiv, skalert og klippet til fire HD-piksler ved [1112,468]; ikke kopierte originalpiksler. Kortet bevarer seks synlige kolonner i to hvite rader, blå skillelinje, brunlig venstre stripe og abstrakte grønne/mørke og rosa/røde toppmerker. Ingen dato, måned, bokstaver eller funksjon er oppfunnet. De firkantede toppformene er meningsbærende kildeglyfer, ikke en bekreftet tekst.

020_02 har eget løftet blått lokk og gul femtagget stjerne, med lukket skap. Ingen nye kistegjenstander. Kiste- og romperspektivet er kontrollert i fullscene og nærbilde. Stjernens nye malte lys har mer volum enn originalens flate gule felt; samme tagger, plass og retning er beholdt.

## Produksjon og kontroll

Sju faktiske kall til innebygd imagegen. Eksakt modellnavn er ikke eksponert. Alle råforsøk, ordrette låste jobbprompter og separate presiseringer er bevart. a-forbered.py.txt, a-kortanalyse.py.txt, a-kortprompt.py.txt, a-sammensetting.py.txt og a-kontroll.py.txt er faktisk kjørt. Førvarianten av sammensettingen er også bevart. Bare nye genererte bilder er skalert/klippet; rektangulær fire HD-pikslers kantovergang går mot nytegnet grunnrom. Ingen originalkonturmasker, originaloppskalering som leveranse, vektor eller lokal geometriwarp.

Uendret sjekk_leveranse.py gir OK for alle fem. Alle fem metadatafelt har eksplisitt kantkorrelasjon 0.943 til 0.980 og er ikke hoppet over. 40 beskyttede jobbkilder og 16 låste kontekstfiler er uendret. RGB, 1536 x 1024, motivfelt og eksakt RGB128-padding er kontrollert. SHA/proveniens, inputhash, kontrollfiler og faktisk oppskrifts-SHA finnes i a-leveranser.json. Skapfamiliens bytebevis finnes i a-familiebevis.json.

Visuell kontroll: a-samlet-kontaktark.png, a-objektqa.png og a-underlag-kantqa.png. Bildene er vurdert som kildebevarende kandidater til roots mottak, ikke individuelt brukergodkjente. Ingen import, motorlagdeling, runtime eller animasjonstiming er testet. Root eier mottak og Git.
