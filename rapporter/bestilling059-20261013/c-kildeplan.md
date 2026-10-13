# Bestilling 59 C: fig066_01..03

Kun kildeanalyse og produksjonsplan. Alle tre originalark er sett, med egne sekvensark og faktisk rel-sammensetting i denne mappen. Ingen ny grafikk eller resultatfil er laget for 066. De 12 beskyttede kildene er verifisert uendret mot roots tidligere lås i bestilling056, og registrert i `c-kildehash.json`.

## Identitet og rekvisitt

Max er oppreist, uten klær, i sin kremhvite originalpalett, med rosa øreinnsider/nese og brune skygger. Ressursen hører til Snuckey's, rom 11/12. Kostymeregisteret har rom11/palett0, mens skriptkoblingene knytter kostyme 66 til actor 3 i globale scrp067 linje172, rom011 lokal200 linje10 og lokal203 linje6, samt rom012 lokal202/203 linje5. Dette er en annen scene og orientering enn 205.

Rekvisitten er rasp med tilknyttet toalettnøkkel, kildeavklart av root fra LucasArts-hintboken, ikke brukerbekreftet. Se `rapporter/bestilling056-20261013/root-max066-kildeplan.md`: gjenstandstabellen på trykt side 33 og forklaringen på side 39. Kildelenke: https://www.mocagh.org/lucasfilm/sammax-hintbook.pdf. Denne analysen bygger på roots dokumenterte tekstutdrag, ikke en påstand om egen gjennomlesning av hele PDF-en.

Originalen bestemmer det lange grå raspfeltet, den mørke delen, den tynne blå forbindelsen og det røde hengende nøkkelfeltet. Ingen gjenstand må bli pistol, gevær, mikrofon eller annen lang rekvisitt. Ikke legg til gullnøkkel, ny ring, merkelapp, kjedeledd eller tenner som ikke støttes av formene. Rød del skifter vinkel og blir delvis skjult i forskjellige retninger; den skal ikke tvinges fullt synlig i alle ruter.

## Ark, lag og bevegelser

| Ark | Ruter | Faktisk innhold |
|---|---:|---|
| fig066_01 | 14 | Tre hele stående Max-posisjoner med rasp/nøkkel, to egne små øyelag, åtte høyregangruter, én hodeløs talekropp med rekvisitt |
| fig066_02 | 21 | Tretten separate talehoder mot høyre, åtte gangruter forfra med rekvisitt |
| fig066_03 | 11 | Åtte gangruter bakfra med rekvisitt, tre egne a6-posisjoner |

A6 viser cel133 med løftet rasp/nøkkel, cel134 med utstrakt tom hånd og cel135 stående uten rekvisitt. Sekvensen er visuelt forenlig med slipp/overlevering, men ingen konkret mottaker eller ny handling skal tegnes inn. Bare de faktiske tre posene leveres. Det skal verken ligge en ny gjenstand på bakken i 134 eller fortsatt henge nøkkel i 135.

De tre gangsekvensene har åtte ruter hver. Hender, ben, føtter og raspens helning flyttes med kilden, ikke bare samme figur med armen justert. Front-/bakrutene viser forkortet rasp og ulik overlapping med hånden. Fotputenes rosa merker er synlige bare i de konkrete løftede føttene. Bakfra er hodet blankt uten øyne og munn.

## Eksakt gjenbruk og egne ruter

Uavhengig måling bekrefter roots 13 donorhoder. Synlig original-RGB og form er eksakt like etter at atlasbakgrunnene er normalisert kun for analysen. Det er ikke produksjonsmasker. Alle 46 målmotivene er innbyrdes ulike.

| 066 cel | 003 cel |
|---:|---:|
| 260 | 390 |
| 262 | 392 |
| 259 | 389 |
| 264 | 395 |
| 266 | 397 |
| 263 | 394 |
| 257 | 385 |
| 270 | 402 |
| 271 | 403 |
| 268 | 400 |
| 269 | 401 |
| 267 | 399 |
| 261 | 391 |

264 og 270 skal bruke B sine godkjente korrigerte nye 395/402-komponenter i bestilling058, eventuelt den dokumentert oppdaterte donorfilen etter roots arkivering. Ikke den gamle røde munnvarianten. Ingen av disse donorene skal vendes; 066 er oppreist. Nåværende filhash og komponentuttrekk må låses ved produksjonsstart.

De 33 øvrige rutene består av tre stående, to smålag, 24 gangruter, én talekropp og tre a6-posisjoner. Ingen av disse er eksakte 003-donorer i målingen. Smålagene har synlig størrelse 13 × 2 og 14 × 2 kildepiksler og må ikke bare erstattes av de liknende donorene fra andre kostymer.

## Rel og pakking

`c-rutekart066.json` inneholder råmetadata, synlig boks, faktisk synlig rel-boks, palettmålinger og eksakte donorlenker for alle ruter. Format0x59 med 32 palettindekser, speil=false, fire retninger. Jobbarkene leverer de tre viste retningene; ikke tegn ekstra venstreruter.

Hodeløs talekropp 164 har synlig rel [-11,-21,30,0]. Stående132 har [-18,-52,30,0], stående130 [-17,-53,17,2] og stående128 [-19,-52,20,0]. Den synlige y=2 i frontstillingen er kildeegent og skal ikke presses opp til null. Smålag384 har [-5,-31,8,-29], smålag512 [-8,-32,6,-30]. A6-bokser:133 [-17,-49,38,0],134 [-17,-49,33,0],135 [-18,-52,18,0].

Talehodene bruker ulike rårektangler og enkelte egne én-piksel-rel-avvik mot 003. Bruk målboks og målrel, ikke donorens opprinnelse. `c-rel-tale.png` viser alle 13 hoder på kropp164. Fraskilte hoder skal ikke få hals/kropp malt inn. Ekte RGBA-leveranse blir1536 × 1024, med målrekt [64+4x,32+4y,64+4x2,32+4y2] fra synlig kildeboks. Magenta er bare bakgrunn; ingen originale produksjonsmasker.

## Palett

Faktiske synlige farger er svart; grå71/151/191; blå(35,99,191); mørkerød(139,7,7), rød(191,51,63); brun(179,147,119); rødbrun(199,79,43); beige(207,195,179)/(215,179,143); rosa(223,115,107); lys(251,251,251) og krem(255,243,227). Magenta er utelatt. Ikke gjør alle skygger svarte eller den røde nøkkelen rosa hud. Hovedark/max.png og mottatte Max003 gir identitet/strek; de bestemmer ikke rekvisittens form.

## Anbefalt produksjonsrekkefølge

1. Pakk de 13 dokumenterte nye donorhodene med kilde-/RGBA-kvittering og riktige målrel. Bevar korrigert 395/402.
2. Nytegn tre stående posisjoner sammen med talekropp164 som første rekvisitt-/håndanker, og kontroller mot source i alle tre retninger før resten.
3. Lag åtte gangruter per retning i egne håndterbare genereringsgrupper. Kildens håndkontakt, raspvinkel, blå forbindelsesform og røde nøkkelsving må sammenliknes rutefor-rute.
4. Lag tre a6-posisjoner med egne kilder og de to smålagene. Kontroller smålagene oppå de nye hodene; en teknisk OK-rute er ikke bevis på at øynene faktisk dekkes.
5. Samlet kontroll av alle 46 ruter, de 24 gangposene, 13 talesammensettinger og tre a6-faser. Kjør uendret checker, bevar faktisk SJEKK hvis det oppstår, og dokumenter egen visuell vurdering av smålagene.

Ingen nødvendig identitetsuklarhet gjenstår etter hintbokavklaringen. Nøyaktig scenehendelse, timing, mottaker ved a6, motor-speiling og runtime/import er fortsatt uverifisert. Ingen generering er startet før denne planen er ferdig.
