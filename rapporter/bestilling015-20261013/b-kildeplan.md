# Kildeplan for Bestilling 15

Kildeanalyse 13. oktober 2026, uten produksjon. Bare denne rapporten er skrevet. Ingen bilder, beskyttede kilder, kode eller Git-tilstand er endret.

## Dokumenterte kilder

Bestilling 15 i `GRAFIKKLISTE.md` angir obj604_01 til obj613_01. Alle ti originalbilder er visuelt undersøkt samlet, og alle ti jobbmetadata og prompter er lest. Referansebildenes SHA256 stemmer med jobb.json. Promptfilenes SHA256 avviker fra det registrerte metadatafeltet for alle ti; faktisk innhold må låses og brukes, uten endring av beskyttede filer. Årsaken til avviket er ikke undersøkt for disse ti filene.

`konsept/2026-10-12/objektbilder-959.csv` identifiserer dem som BOMP-objekter i rom68 med navn `surf-street-11` til `surf-street-15` og `surf-street-21` til `surf-street-25`. Registeret har én oppføring, tilstand01, per objekt. De fem variantene innen hver gruppe er forskjellige objekt-ID-er, ikke fem registrerte tilstander av samme objekt. Dette skiller dokumentert uttrekk fra antatt animasjonsrekkefølge.

Kontekst er også lest fra rom068, `origin/main:docs/gpt-romnotater.csv`, `docs/rom-oversikt.csv` og `docs/ANALYSE.md`. Rom068 har grensesnitt og tomt svart nedre grunnfelt. Rom69 er lager for separate Highway Surfing-bilder, blant annet biler, skilt, start/mål og horisont. Den tilgjengelige analysen oppgir at styrende skript ikke er gjennomgått. Denne planen påstår derfor ikke en bestemt runtime-rekkefølge, kjørefysikk eller betydningen av hvert kurvenummer.

## Faktisk motiv

Alle ti bilder er banesegmenter. Hvert bilde inneholder en meget lav, grålilla veiflate med skrå sidekanter, nesten svarte områder utenfor veien og én gul markering som fortsetter ut av øvre eller nedre bildekant. Ingen av disse ti inneholder skilttekst, tall, poengfelt, biler, figurer, horisont eller andre spillgjenstander.

Obj604 til obj608 er en bredere gruppe med markeringen ved nedre kant. Obj609 til obj613 er en smalere og mørkere gruppe med markeringen ved øvre kant. Innen hver gruppe varierer både kantene og markeringens helning. Ikke speilvend ett bilde for å lage et annet: originalene har forskjellige små forskyvninger og sidefelt. De lave utsnittene skal ikke utvides til en hel vei eller et nytt perspektivbilde.

## Eksakt størrelse og plassering

Alle leveranser er 1536 × 1024 med skala4 og grå padding RGB (128,128,128). Originalenes nesten svarte motivfelt er RGB (7,7,0), ikke padding og ikke en autorisasjon til å legge inn transparens. Alle originaler er 24 piksler høye; HD-motivhøyden er 96.

| Jobb | Kildenavn | Original | HD-felt [x,y,b,h] | Objekt_i_rom [x,y,b,h] |
| --- | --- | --- | --- | --- |
| obj604_01 | surf-street-11 | 320 × 24 | [128,464,1280,96] | [0,168,320,24] |
| obj605_01 | surf-street-12 | 320 × 24 | [128,464,1280,96] | [0,152,320,24] |
| obj606_01 | surf-street-13 | 320 × 24 | [128,464,1280,96] | [0,136,320,24] |
| obj607_01 | surf-street-14 | 320 × 24 | [128,464,1280,96] | [312,168,320,24] |
| obj608_01 | surf-street-15 | 320 × 24 | [128,464,1280,96] | [312,168,320,24] |
| obj609_01 | surf-street-21 | 264 × 24 | [240,464,1056,96] | [32,144,264,24] |
| obj610_01 | surf-street-22 | 264 × 24 | [240,464,1056,96] | [32,144,264,24] |
| obj611_01 | surf-street-23 | 264 × 24 | [240,464,1056,96] | [32,144,264,24] |
| obj612_01 | surf-street-24 | 264 × 24 | [240,464,1056,96] | [32,144,264,24] |
| obj613_01 | surf-street-25 | 264 × 24 | [240,464,1056,96] | [32,144,264,24] |

`region` er lokalt [0,0,bredde,24]. Objekt_i_rom er uttrekkets metadata, ikke leveranseplassering. De merkelige x=312-verdiene for obj607 og obj608 skal ikke «rettes» eller brukes til å flytte motivet uten dokumentert motorkontekst. Leveransen følger feltet i tabellen.

## Variantsærtrekk og målepunkter

Tabellen under viser kildens lokale x-intervaller, med inklusive endepunkter. Veikantene er målt ved å skille den grålilla flaten fra den nesten svarte bakgrunnen med blåkanal >20. Dette er kun en read-only beskrivelse av originalene, ikke en maske eller en produksjonsmetode. Gulmarkeringens første og siste synlige rad er angitt for å bevare knekk, bredde og plassering.

| Objekt | Vei øverste rad | Vei nederste rad | Gul markering, første rad | Gul markering, siste rad |
| --- | --- | --- | --- | --- |
| 604 | 33..287 | 0..319 | y15:155..163 | y23:155..163 |
| 605 | 44..298 | 0..319 | y15:160..167 | y23:155..163 |
| 606 | 21..275 | 0..319 | y15:152..160 | y23:156..164 |
| 607 | 56..309 | 0..319 | y15:164..172 | y23:156..164 |
| 608 | 10..264 | 0..319 | y15:148..156 | y23:156..164 |
| 609 | 35..221 | 2..253 | y0:125..129 | y9:125..130 |
| 610 | 51..236 | 6..257 | y0:141..145 | y9:136..141 |
| 611 | 27..213 | 6..257 | y0:118..122 | y9:122..127 |
| 612 | 58..244 | 2..253 | y0:149..154 | y9:140..145 |
| 613 | 12..197 | 2..253 | y0:102..107 | y9:111..116 |

Obj604 sin stripe er rett. Obj605 og obj607 heller mot venstre fra topp til bunn, den siste sterkere. Obj606 og obj608 heller motsatt. Obj609 er nesten rett, men bredden øker ett originalpiksel til høyre. Obj610 og obj612 heller mot venstre, obj611 og obj613 mot høyre. Bevar disse forskjellene og de bevisst tomme radene før eller etter stripen.

## Korrigering av generisk romnote

Promptens romnote om to øvre bokser, biler, skilt, tall og `Score:` gjelder spillrommets samlede kontekst. Den er misvisende dersom den brukes som motivbestilling her. Separat kildepresisering må si at ingen bokser, tekst, biler eller skilt finnes i dette objektet og at ingenting slikt skal legges til. Her finnes heller ingen uleselige glyfer som trenger teksttolkning.

Veifargen bruker få grålilla nyanser og dithering, med gul markering og mørke sidefelt. Glattere HD-overganger må beholde samme lyse/mørke retning og variantforskjeller. Ikke legg til asfaltkorn, sprekker, kantstriper, flere gule streker, glød eller refleksjoner. Ikke normaliser skjevhetene eller sentrer stripene på nytt.

## Sammenheng og gjenstående kontroll

Registeret fortsetter med `surf-street-31` til `surf-street-75` og enda fjernere segmenter, med avtagende bredder. Dette underbygger at de ti er deler av en perspektivoppbygd veifamilie. Ingen panoramaoverlapp er deklarert, og ingen felles verdensmaster skal antas. Bestilling16 begynner med obj649 og obj650, ikke de mellomliggende småsegmentene; deres eksakte leveranserute må sjekkes mot eksisterende ikonark og hovedliste før en senere samlet runtime-påstand.

Før produksjon må faktiske kildebytes låses. Etter produksjon kreves kontroll av alle ti sammen, spesielt sidekantvinkler, gulstriper, mørke felt og den eksakte plasseringen på canvas. Uendret teknisk checker er nødvendig, men erstatter ikke kontroll av lagkomposisjon i Highway Surfing. Faktisk motortegning, palettbruk, segmentrekkefølge og koblingen mellom veivariant og spilltilstand er fortsatt uverifisert. Ingen ny individuell brukergodkjenning eller runtime er utført.
