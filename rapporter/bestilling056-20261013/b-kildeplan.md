# Kildeplan, fig114_01 til fig114_05

Kun analyse. Ingen generering, jobbfiler, globale logger eller Git er endret. [Ruteregister](b-ruteregister.json) dokumenterer 52 ruter, paletter, original metadata, rel og identiske cels. [Kildelås](b-kildehash.json) låser 20 beskyttede jobbfiler; [kontekstlås](b-konteksthash.json) låser åtte tilleggskilder/ankre. Alle fem originalark og de ni detaljerte rutesidene er sett.

## Dokumentert motiv og kontekst

Sam i vanlig blågrå dress og fedora, hvit skjorte, mørk blå/svart stripet slips, brun pels, store brune nakne føtter. Hatten har ulike vinkler, hodet senkes og kroppen bøyes fremover mens hendene griper, slipper og rekker ned. Dette er ikke en gangsekvens, nytt kostyme, hansker, sko eller en golfkølle lagt i hånden. De synlige hendene er brune, slipsfliken flytter seg mellom rutene og må ikke fjernes som løs støy. Sam-hovedark og pilot gir identitet/strek, men originalens konkrete stillinger bestemmer hver cel.

Kostyme 114 er koblet til skuespiller 2 i rom 25 på seks steder i objekt 244 sitt verbscript: registeret `konsept/2026-10-12/skript-kostymekoblinger.tsv` viser linjene 25,43,70,92,123,148. `objektnavn-original.tsv` linje 199 navngir 244 som `golf-tee`, og linje 214 navngir 259 som `gator-ball-bucket`. Rom025 sin originale bakgrunn og jobbmetadata viser Gator Golf, utslagsplassen. Linje 277 viser også `w-o-fish-bucket` for objekt322 i rom35, men dette alene beviser ikke at alle grønne lag her er samme inventarressurs.

Lag 1 viser to klart ulike beholdere: grå metallignende bøtte med grønne former som i129/130 har tydelig fiskehode/øye, og blå bøtte med oransje kant og hvit/grå haug. Den første tolkningen som fisk støttes sterkt av nærbildene; den andre som golfballer støttes av rommet og det konkrete `gator-ball-bucket`-navnet. Rot har nå vurdert de originale objektnavnene, nærbildene og rom025 som tilstrekkelig grunnlag: grå/grønn variant er fiskebøtte, blå/oransje/hvit variant er golfballbøtte. Ingen ny brukeravklaring er nødvendig for disse motivdelene. Ingen grønne slanger, planter eller levende alligatorhoder skal oppfinnes ut fra små enkeltklynger. Ingen antatt telling av skjulte fisk eller kuler.

Fullscript `rom_025/obj_0244_verb.txt` er ikke bevart lokalt i det lesbare kildeutvalget. Gamle /tmp-spillkilder er utilgjengelige. Hovedcheckoutens docs/figurer.csv har bare header ved denne lesingen. Derfor påstår denne planen ikke å ha kjørt spillet eller verifisert eksakt scriptforløp. Rot har avklart fiskebøtte og golfballbøtte fra originalnavn og bildebevis. Det som fortsatt ikke bevises, er nøyaktig timing og årsaksrekkefølge for nedsetting, opptak eller bytte.

## Ark, lag og kombinasjoner

| Jobb | Antall | Innhold |
| --- | ---: | --- |
| fig114_01 | 12 | Cel0 stående, deretter1..6,8..12, alle Sam lag0. |
| fig114_02 | 17 | Sam13,14,16..20; ni grå/grønne bøttelag128..136; Sam15 til slutt. |
| fig114_03 | 8 | Bare blå/oransje/hvite bøttelag141..148. Ikke tegn Sam her. |
| fig114_04 | 12 | Sam30,31,22..28; tre grå/grønne bøttelag138..140. |
| fig114_05 | 3 | Bare blå/oransje/hvite bøttelag150..152. |

Alle er 352 × 240 kildeatlas på 1536 × 1024 canvas med motivfelt [64,32,1408,960]. Kildebakgrunnen er magenta [255,0,255], ikke motiv. Fremtidig resultat skal være ekte RGBA uten magenta/grå matte. En kildepiksel er fire HD-piksler. Eksakte synlige HD-bokser er i tabellen nedenfor. Store metadatarektangler på92 ×70 overlapper andre atlasruter fordi synlig innhold er pakket tett. De må ikke blindt klippes som enkeltcel. I analysen klippes bare synlig-boksen, legges tilbake på det opprinnelige tomme celcanvas med forskyvningen synlig minus rekt, og plasseres deretter med rel. Kildeavledet alfa brukes kun til disse diagnostiske originalarkene, aldri som produksjonsmaske.

Kostymemetadata: format0x59,32 palettindekser, rom25/palett0; fire mulige retninger, men de faktiske handlingsrutene her er retning1. Ingen venstreruter skal legges til. Alle move_x/move_y er0. De fleste celcanvas er92 ×70 med rel(-18,-70), men8 har49 ×65/rel(-14,-65),18/30 har60 ×65/rel(-13,-65),31 har73 ×56/rel(-13,-56). Bøtte128/141 har11 ×14/rel(14,-31),136 har28 ×22/rel(46,-23),147 har22 ×22/rel(50,-23). Disse unntakene er viktige for kontakt med hånden/gulvet.

Animasjon7 bruker grå/grønn bøtte og Samforløpet;8 bruker blå/oransje bøtte og inkluderer Sam15. Animasjon9/10 har nedbøying/opptakslignende forløp med hver bøttefamilie.11/12 gjenbruker begge familier i motsatt rekkefølge, og de skal ikke få nye tilfeldige cels. De fullstendige listene er bevart i ruteregisteret. Listene har ulik lengde mellom lagene og er ikke timingbevis. [Sammensetting1](b-sammensetting-1.png) og [2](b-sammensetting-2.png) viser16 bevisste statiske rel-kombinasjoner for hånd/bøtte/gulv; de er diagnostiske, ikke påstått eksakte samtidige filmruter.

## Palett, likhet og risiko

Alle faktiske RGB-farger og antall percel er registrert. Bevar blågrå dress, mørkt slips og brune hender/føtter uavhengig av hovedarkets glattere streker. Bøttefamiliene har bevisst ulike materialfarger; de skal ikke tones til samme nøytrale rekvisitt. De hvite/grå buene som skifter over bøttekanten er håndtak/tilstandsflater og må følge kilden. Store magenta hull i138/139 og150/151 er tilsiktet transparent plass for den overlappende Sam-hånden, ikke en ødelagt bøtte eller et manglende motiv som skal fylles ut.

Bare cel15 og25 er byte-identiske etter korrekt rekonstruksjon av hele originale celcanvas. De kan dele samme nytegnede komponent hvis alle koordinater verifiseres. Ingen andre av52 er identiske i dette beviset. Nesten like13/14/15/16 og22/23/24/25/26 har egne slips-/arm-/fotendringer.129/130 har forskjellig fiskehodeplass,131/132/133 egne håndtaksformer. De to palettfamiliene er ikke sammebitmap med en fargetoneendring.

Avklart produksjonsgrunnlag: trygg arbeidsform én eier for alle52, med separat Samfamilie og to egne bøttefamilier. Generer gjerne komponentgrupper etter sammenheng, men behold hver celmapping og riktig ark. Ingen ny hånd på lag1, ingen bøtte bakt inn i lag0, ingen maskering fra original eller lokal warp. Kontroller sluttark, alle cels, registernavn, kontaktpunkter og rel-sammensetting før mottak. Teknisk checker alene beviser ikke riktig innhold, timing eller runtime.

## Eksakte ruter

HD-boksen er x,y,bredde,høyde. Rute-ID er intern cel-ID, ikke animasjonsnummer.

| Jobb | Cel | Animasjon/lag | HD-boks | rel | Synlige kildepiksler |
| --- | ---: | --- | --- | --- | ---: |
| fig114_01 | 0 | 3/0 | 80,48,160,280 | -18,-70 | 1815 |
| fig114_01 | 1 | 7/0 | 80,360,152,280 | -18,-70 | 1788 |
| fig114_01 | 2 | 7/0 | 264,368,144,272 | -18,-70 | 1711 |
| fig114_01 | 3 | 7/0 | 440,372,160,268 | -18,-70 | 1781 |
| fig114_01 | 4 | 7/0 | 632,380,188,260 | -18,-70 | 1899 |
| fig114_01 | 5 | 7/0 | 852,384,188,256 | -18,-70 | 1847 |
| fig114_01 | 6 | 7/0 | 1072,384,188,256 | -18,-70 | 1842 |
| fig114_01 | 8 | 7/0 | 80,680,196,260 | -14,-65 | 1876 |
| fig114_01 | 9 | 7/0 | 308,672,160,268 | -18,-70 | 1613 |
| fig114_01 | 10 | 7/0 | 500,680,232,260 | -18,-70 | 1873 |
| fig114_01 | 11 | 7/0 | 764,716,284,224 | -18,-70 | 1938 |
| fig114_01 | 12 | 7/0 | 1080,732,316,208 | -18,-70 | 2151 |
| fig114_02 | 13 | 7/0 | 80,68,320,204 | -18,-70 | 2180 |
| fig114_02 | 14 | 7/0 | 432,68,320,204 | -18,-70 | 2204 |
| fig114_02 | 16 | 7/0 | 784,64,332,208 | -18,-70 | 2232 |
| fig114_02 | 17 | 7/0 | 1148,48,296,224 | -18,-70 | 2010 |
| fig114_02 | 18 | 7/0 | 80,324,240,260 | -13,-65 | 1886 |
| fig114_02 | 19 | 7/0 | 352,304,140,280 | -18,-70 | 1689 |
| fig114_02 | 20 | 7/0 | 524,304,152,280 | -18,-70 | 1761 |
| fig114_02 | 128 | 7/1 | 80,652,44,56 | 14,-31 | 121 |
| fig114_02 | 129 | 7/1 | 156,620,92,88 | -18,-70 | 355 |
| fig114_02 | 130 | 7/1 | 280,620,104,88 | -18,-70 | 400 |
| fig114_02 | 131 | 7/1 | 416,616,104,92 | -18,-70 | 407 |
| fig114_02 | 132 | 7/1 | 552,616,104,92 | -18,-70 | 407 |
| fig114_02 | 133 | 7/1 | 688,616,104,92 | -18,-70 | 407 |
| fig114_02 | 134 | 7/1 | 824,620,104,88 | -18,-70 | 417 |
| fig114_02 | 135 | 7/1 | 960,624,112,84 | -18,-70 | 424 |
| fig114_02 | 136 | 7/1 | 1104,620,112,88 | 46,-23 | 426 |
| fig114_02 | 15 | 8/0 | 80,740,320,204 | -18,-70 | 2205 |
| fig114_03 | 141 | 8/1 | 80,84,44,56 | 14,-31 | 121 |
| fig114_03 | 142 | 8/1 | 156,52,88,88 | -18,-70 | 352 |
| fig114_03 | 143 | 8/1 | 276,52,88,88 | -18,-70 | 384 |
| fig114_03 | 144 | 8/1 | 396,48,88,92 | -18,-70 | 378 |
| fig114_03 | 145 | 8/1 | 516,48,88,92 | -18,-70 | 378 |
| fig114_03 | 146 | 8/1 | 636,48,88,92 | -18,-70 | 378 |
| fig114_03 | 147 | 8/1 | 756,52,88,88 | 50,-23 | 389 |
| fig114_03 | 148 | 8/1 | 876,56,96,84 | -18,-70 | 396 |
| fig114_04 | 30 | 9/0 | 80,48,240,260 | -13,-65 | 1884 |
| fig114_04 | 31 | 9/0 | 352,84,292,224 | -13,-56 | 1963 |
| fig114_04 | 22 | 9/0 | 676,100,340,208 | -18,-70 | 2277 |
| fig114_04 | 23 | 9/0 | 1048,104,340,204 | -18,-70 | 2309 |
| fig114_04 | 24 | 9/0 | 80,360,332,204 | -18,-70 | 2268 |
| fig114_04 | 25 | 9/0 | 444,360,320,204 | -18,-70 | 2205 |
| fig114_04 | 26 | 9/0 | 796,356,316,208 | -18,-70 | 2201 |
| fig114_04 | 27 | 9/0 | 1144,340,284,224 | -18,-70 | 1975 |
| fig114_04 | 28 | 9/0 | 80,596,232,260 | -18,-70 | 1875 |
| fig114_04 | 138 | 9/1 | 80,888,112,84 | -18,-70 | 274 |
| fig114_04 | 139 | 9/1 | 224,888,112,84 | -18,-70 | 250 |
| fig114_04 | 140 | 9/1 | 368,888,104,84 | -18,-70 | 349 |
| fig114_05 | 150 | 10/1 | 80,52,96,80 | -18,-70 | 246 |
| fig114_05 | 151 | 10/1 | 208,52,96,80 | -18,-70 | 225 |
| fig114_05 | 152 | 10/1 | 336,48,88,84 | -18,-70 | 323 |

Runtime=false. Ingen ny individuell brukergodkjenning eller HD-produksjon er påstått.
