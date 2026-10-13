# Kilde og egenkontroll, gruppe C

Rom 008 er gangen utenfor kontoret. Rom 009 er gaten utenfor kontoret. Metadata kobler hvert bilde til kilde, utsnitt, palettbilde og fast 4x-skala. Originaler i 1x og 4x samt godkjent stilanker er visuelt gjennomgått før generering. Føringer lest: AGENTS.md, BESTILLING.md, ANALYSE.md, source-faithful-production og imagegen, samt relevant del av origin/main:docs/skills/scumm-hd-remake/SKILL.md.

Ordrett prompt ble beholdt med tillegg som låser synlig kildeinnhold. Det generiske gangnotatet om skuddhull gir ikke anledning til å importere hull fra kontorreferansen. Fremre dør leses Flint / Paper. Den lille bakre dørteksten er ikke sikkert transkribert og er en uttrykkelig begrensning.

Gatekilden og origin/main:docs/gpt-romnotater.csv bekrefter NO WAY, VEHICLES WILL BE STOLEN, SOILED OFFICE SPACE AVAILABLE, Bosco's, GUNS LIQUOR BABY NEEDS, NEW, USED, COME ON IN og REALLY BAD FOOD. Radinndeling og plassering er sammenlignet visuelt; høyreskiltet er fortsatt avkuttet. Fem spisse vindusgitterstenger er beholdt. Blodflekk, bøyd parkometer, avfall, postkasse, dør/trapper, gjerde og bakgrunnsbygg er bevart. Nytegningen kan variere i små slitasjemerker; ingen garanti om identisk telling av utydelige kildemerker.

Alle tre leveranser fikk OK med uendret sjekk_leveranse.py. Eksakt lerret 1536 x 1024 og grå padding RGB 128 er kontrollert med array-sammenligning. Ingen skalering, warping eller originalmaskering ble brukt. Gatefullscene er 1920 x 800; de to overlappende utsnittene har byte-identisk felles 1152 x 800 område. Fullscene og utsnitt av skjøten er visuelt kontrollert. Produksjonsoppskrift og råforsøk er bevart.

Modellnavn er ikke eksponert. Import, maskesamspill, runtime og Toms godkjenning av disse nye bildene gjenstår. Tidligere stilgodkjenning er grunnlag for produksjon, ikke en påstått ny bildegodkjenning.

Lokal korreksjon av rom008: dekorative løkker på bakre dør erstattet av enkle mørke tegnklaser fra originalens uleselige kildeformer. Ingen navn/ord gjettet. Bare boks [886,373,911,434] endret, utenfor byte-identisk. Etterkontroll OK. Se rom008-doortekst-qa.png og c-leveranser.json for nytt SHA.
