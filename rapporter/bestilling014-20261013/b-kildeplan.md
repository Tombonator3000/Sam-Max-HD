# Kildeplan for Bestilling 14

Bare kildeanalyse, 13. oktober 2026. Ingen bilder er generert eller endret. Runtime og ny individuell brukergodkjenning er ikke utført.

## Kilder og kontroll

De ti neste jobbene er hentet fra `GRAFIKKLISTE.md`, Bestilling 14. For hver jobb er `original_1x.png`, `referanse.png`, `jobb.json` og `prompt.txt` lest; motivet er undersøkt visuelt i referansen. Rom061 del1 er også undersøkt for panoramakontekst. Objektidentifikatorene er kontrollert i `konsept/2026-10-12/objektbilder-959.csv`, og romnotene mot `origin/main:docs/gpt-romnotater.csv`.

Alle elleve referansefiler har SHA256 som stemmer med `sha256_referanse` i jobb.json. Ingen av de elleve aktuelle promptfilenes SHA256 stemmer med jobb.json sitt `sha256_prompt`. Dette er et forhåndseksisterende metadataavvik, observert før noen filskriving i denne oppgaven. [Root sin historikkontroll](root-promptmetadata-avvik.json) dokumenterer at alle elleve nåværende promptfiler er byte-identiske med grunncommit `c96f80b5`, hvor metadataavviket allerede finnes. Årsaken er ikke bevist, men avviket er ikke en lokal produksjonsendring. Root har låst de 40 + 4 faktiske kildefilene i bestillingens kildehash. Produksjon skal bruke de låste promptfilene og beholde deres ordrette innhold med separat kildepresisering. Ingen beskyttede filer skal repareres her.

## Canvas og klipp

Alle leveranser bruker 1536 × 1024, skala 4 og padding RGB (128,128,128). Felt nedenfor er `[x,y,bredde,høyde]` i leveransen, ikke objektets plassering i spillrommet.

| Jobb | Original | HD felt | Lag og tilstand |
| --- | --- | --- | --- |
| rom061_del2av2 | 384 × 200 | [0,112,1536,800] | Rom61, verdensregion [104,0,384,200] |
| rom062 | 320 × 200 | [128,112,1280,800] | Tjæregropens bakgrunn |
| rom066 | 320 × 200 | [128,112,1280,800] | Car Bomb sitt grunnbrett |
| obj598_01 | 320 × 104 | [128,304,1280,416] | Rom67, b-stars, tilstand01 |
| obj599_01 | 224 × 72 | [320,368,896,288] | Rom67, b-star-sign, tilstand01 |
| obj600_01 | 320 × 72 | [128,368,1280,288] | Rom67, credit-panel-7, tilstand01 |
| obj601_01 | 320 × 72 | [128,368,1280,288] | Rom67, credit-panel-8, tilstand01 |
| obj602_01 | 320 × 72 | [128,368,1280,288] | Rom67, credit-panel-9, tilstand01 |
| obj603_01 | 320 × 72 | [128,368,1280,288] | Rom67, credit-panel-10, tilstand01 |
| rom068 | 320 × 200 | [128,112,1280,800] | Highway Surfing sitt grunnlag |

Rom061 er 488 × 200 originalpiksler. Felles master skal være 1952 × 800. Del1 klippes fra x=0, del2 fra x=416, begge med bredde 1536. Overlapp er 1120 × 800. Originalenes 280 × 200 overlapp er sammenlignet byte for byte og er identisk. Del2 skal være eksakt klipp fra C sin låste master i Bestilling 13, med masterSHA kontrollert mot den endelige proveniensen. Ingen uavhengig generering av denne delen. Masteren er en produksjonsavhengighet, ikke allerede godkjent av denne planen.

Ingen andre panoramaer i disse ti jobbene krysser batchgrensen. Bestilling 15 begynner med obj604_01 og flere objekter i rom 68. Disse er separate spillag, ikke manglende deler av en panoramamaster for rom 068.

## Motiv og presiseringer

**Rom061 del2:** Gråsvart fjellhule, lys blå himmel og skyer, trekroner til høyre, trekantede fjellkanter og treplattform med ujevne planker, åpninger og rekkverk. Den brune skjermen og veggknappen fortsetter fra venstre del. Bevar opphenget med rødsvart form, ring og mørke kabelbuer. Ikke legg til hopper eller fullfør hullene i plattformen. Del1 viser heisdør, kontrollpanel og skjermens sammenheng; dette er grunnlaget for fullmasteren.

**Rom062:** Oval svart tjæregrop med mørkeblå flate bånd, lysgrå ring, nagler, bølger og fjellvegg. Venstre brune dyreform har lyst snuteparti, store lyse tenner, åpen rødsvart munn og bøyd forlem. Til høyre stikker en brun, stripet lang form opp med grå, hul ende. Bevar den hule enden og den ubehagelige situasjonen. Bildet alene fastslår ikke sikkert hva høyre fragment er; ikke gjør det om til en vanlig hale, støvel eller levende badegjest ut fra gjetting. Ingen tekst.

**Rom066:** Kopier `CAR BOMB` med samme skrå oppstilling over gul eksplosjonsform og rød pil. Max er allerede synlig bak brettet med lange ører, svart øye og stort smil, og skal ikke fjernes som et antatt separat figurlag. Oppreist brett har visuelt 10 × 10 celler; det nederste brettet er en tilsvarende kraftig forkortet rutenettflate. Alle linjer og skjæringspunkter må følge originalen, uten normalisering av perspektivet. Bevar røde rammer, lilla veiflater, sluk, fortauskanter, hydrantene, blå beholder, liten stolpe, bombekasse og bombene til venstre, samt de to rakettformene nederst til høyre. Ingen nye biler eller spillmarkører i rutene. Rutenettets geometriske samsvar må kontrolleres særskilt ved produksjon.

**Obj598:** `b-stars` er spredte små flerfargede lyspunkter på svart, ikke et panel med navnetekst. Bevar punktgruppenes antall, plassering og farger. Ikke erstatt med realistisk nattehimmel eller store fyrverkerieksplosjoner.

**Obj599:** `b-star-sign` er et skilt bygget av adskilte flerfargede lyspunkter på svart. Høyre del har bokstavlignende former, blant annet en lesbar avslutning som ligner `VILLE`; full tekst er ikke sikkert avlest her. Dette er ikke grunnlag for å skrive et gjettet stedsnavn med sammenhengende typografi. Følg originalens punkter, buer og glyfer.

**Obj600:** Illustrasjonspanel med Max til venstre og Sam til høyre, lange utstrakte hender mot midten og en liten lys ansiktsform bak Sam. Bevar figuridentitet og den aktuelle gesten. Sterkt rødt, brunt, lilla og grønt er kildens panelpalett; hovedarkene styrer tegneseriestrek og identitet, ikke en omfarging til vanlige klær.

**Obj601:** Stor pistolform mot venstre, Sam mot høyre, sterkt grønn, rød, oransje og lilla palett. Pistolens side har stor lys tekst og en mindre linje som starter med `CALL`. Små tegn og resten av teksten må følges som kildeglyfer; ingen komplett telefonfrase er verifisert her. Bevar løpets runde åpning, avtrekkerform, håndgrep og figurens plassering.

**Obj602:** Sam og Max i en overfylt, stilisert mekanisk scene med doble runde mørke åpninger midt i bildet, røykbue, hjulformer og utstikkende deler. Max sine lange ører og Sam sin hatt og snute er identitetsankere. Ingen generell biltegning skal erstatte den uvanlige komposisjonen. Svart stripe nederst tilhører motivet.

**Obj603:** Sam og Max tett sammen med store forgrunnshender og en diagonal mønstret rem eller gjenstand. Bevar de overlappende figurdelene og den grønne ovale bakgrunnen. Den diagonale detaljen er ikke avklart som lesbar tekst eller en bestemt ny rekvisitt; kopier formen uten å skrive inn ord. Svart toppstripe og beskjæringen av figurene beholdes.

**Rom068:** Oransjegul himmelflate, to grønne felt øverst og en stor nesten svart nedre flate. Teksten er `Time` uten synlig kolon og `Score:` med kolon. Tidsfeltets mørke indre er tomt; ingen tall legges til. Romnoten «keep ... the road exactly» er for generell her: originalen har ingen tegnet vei, kjørefelt, biler eller landskap i det svarte området. Disse må ikke konstrueres. Spillobjekter kommer på egne lag i senere bestillinger.

## Grenser for produksjon

Rulletekstnoten er relevant for den spesielle paletten, men betyr ikke at alle seks objekter er tekstpaneler. Romnavn og generiske noter overstyrer ikke faktisk innhold. Uleselige tegn skal forbli kildetro former. Sam og Max kontrolleres mot godkjente hovedark, mens originalenes uttrykk, kroppsstilling, palett og beskjæring beholdes. Etter produksjon kreves både uendret teknisk kontroll og visuell kontroll av lag, tekst og sammensetning. Denne kildeplanen dokumenterer ikke runtime eller en ny bildegodkjenning.
