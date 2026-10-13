# Kildeplan for bestilling 41 og lobbykontekst fra 42

Kun analyse. Ingen nye resultater er generert. Alle ti jobber i 41 og de første ni jobbene i 42 er sett som helscene og i egne objektfelt. Eksisterende HD-grunnrom er sammenlignet som kontekst. Runtime, import og ny individuell godkjenning er ikke utført.

## Låser og bevis

40 beskyttede filer for 41 er låst i [kildehash.json](kildehash.json). De ni 42-jobbene har 36 separate låser i [a-042-kontekst-kildehash.json](a-042-kontekst-kildehash.json). Fire grunnrom har ytterligere 16 låser i [a-grunnrom-kildehash.json](a-grunnrom-kildehash.json). HD-ankrenes faktiske SHA står i a-ankerhash.json og a-042-kontekst-ankerhash.json. Ingen jobbfiler er endret.

[Originalkontaktark](original-kontaktark.png), [42-kontekst](a-042-kontekst-kontaktark.png), [grunnrom original/HD](a-grunnrom-kontekst.png), a-objektfelt-1.png til 4 og a-042-kontekst-felt-1.png til 2 viser alle 37 metadatafelt. Registeroppslag, kildepalettantall, klipp og RGB-hasher står i a-feltbevis.json og a-042-kontekst-feltbevis.json. Analyseoppskriftene er bevart som a-analyse.py.txt, a-042-kontekstanalyse.py.txt og a-familieanalyse.py.txt.

Romnotatene fra origin/main:docs/gpt-romnotater.csv bekrefter at 49 med vilje er flate, skarpe polygoner; 50 skal bevare BUMPUSVILLE og puslespillets blokker/kabler; 52 skal bevare THE REPTILE QUEEN, tukan, øgle og steinhode. Registerets navn er kontekst, ikke alene identitetsbevis.

## 049: sverdfravær og rotert rødt hjerte

| Jobb | Felt i rommets kildepiksler | Faktisk innhold |
|---|---|---|
| lag049_01 | 458_01 [208,136,32,40] | Det gule sverdet er borte. Bevar grå stein og brun/mørk turkis bakgrunn. Ikke tegn et nytt sverd. |
| lag049_01 | 459_01 [136,120,24,24] | Rødt hjerte foran lilla hulevegg. Navnet vreality-key er ikke grunnlag for å gjøre det til en metallnøkkel. |
| lag049_02 | 459_02 samme rektangel | Egen rotasjon av det røde hjertet. Grunnrommets gule sverd er fortsatt synlig og skal beholdes. |

299 og 192 kildepiksler er endret mot hvert grunnrom. Null endringer utenfor de respektive feltunionene. Paletten er bevisst flat: grønt/turkis landskap, lilla fjell/himmel/hule, brunt gulv, grå stein, gult sverd og rødt hjerte. Eksisterende vektorlaget rom049 er kun levert bakgrunn/kontekst. Lag049 har ikke eget vektorunntak. Senere produksjon må bruke imagegen for de nye feltene og bevare flate farger uten påført tekstur.

## 050: hjernepanelets konkrete koblinger

BUMPUSVILLE står øverst på blå skjerm. Grunnrommet har limegrønne panelblokker, rosa hjerne, grå metallramme, grønt kveilunderlag og blå/grønne/gule/grå/oransje tilkoblinger. Røde felt er egne skjermtilstander, ikke nye bokstaver. Registernavnet S for noen felt er ikke tekst som skal males inn.

| Jobb | Egne metadataobjekter og synlig tilstand |
|---|---|
| lag050_01 | 461 og 464: røde skjermfelt til venstre og øverst til høyre. 466: blå løs plugg. 468: gul løs plugg nedover. 469: grå løs plugg. |
| lag050_02 | 462 og 465: egne små røde felt øverst/til høyre. 467: grønn løs plugg. 470: oransje løs plugg. 473: gul plugg koblet til hjernen. |
| lag050_03 | 463: bredt rødt felt med nedre midtparti. 471/472/474/475: blå, grønn, grå og oransje kabler koblet til sine egne hjernesokler. |

Endret mot grunnrom: 1237, 1004 og 2302 kildepiksler, alle innenfor hver lagunion. Kildeboksene og de overlappende kabelfeltene må ses samlet etter komposisjon. Ikke kombiner løse og innkoblede varianter fra feil lag, bytt kabelfarge eller gi dem nye sokler. Eksakte rektangler står i feltbeviset. Skjermtekst og hele hjernens form utenfor unionen kan bevares fra riktig HD-grunnrom.

## 052: panorama og samtidige tilstander

Begge komplette tilstandene 01 og 02 har kildeoverlapp som er byte-identisk i RGB. Master er 480 × 200 kildepiksler, altså 1920 × 800 HD. Klipp starter ved x=0 og x=384 HD, begge er 1536 × 800. Overlapp er 1152 HD-piksler. På leveransecanvas ligger motivet i [0,112,1536,800], med nøytral RGB128-padding over og under. Eksisterende HD-grunnrom har også identisk overlapp.

Det er avgjørende å samle begge delers objektunion. Første del viser også endringer som bare står som metadata i andre del, og omvendt. Målingen finner 6112 endrede kildepiksler for tilstand 01 og 3135 for 02 i fullmaster. Null ligger utenfor unionen av begge delers metadataobjekter. Separate blinde feltutskiftninger per del vil derfor gi feil.

[Familiebevis](a-052-familiebevis.png) viser grunnrom til venstre og aktuell tilstand til høyre i hver rute. [Maskinlesbart familiebevis](a-familiebevis.json) inneholder panoramaresultater, full palett per familiefelt og nøyaktige mikroendringer når antallet er høyst 20. a-052-01-originalmaster.png, a-052-02-originalmaster.png og a-052-grunn-originalmaster.png er kun kildebevis, ikke HD-kandidater.

| Lag | Faktisk forskjell |
|---|---|
| 052_01 del1+2 | 483_01: tukanens lukkede nebb står mer vannrett enn grunnrommet. 480_01: egen lukket inngangsdør med metall/glass. 481_01: telefonboksens dør står skrått åpen. 486_01: egen øglesnute. Alle fire følger samme master. |
| 052_02 del1+2 | 483_02: åpent tukan-nebb. 486_02: egen snute. 480_02: inngangsdørene står åpne med kildeviste landskaps-/bilflater bak. Samtidige deler følger samme master. |
| 052_03 del1 | 486_03: egen snute, 63 kildepiksler mot grunn. 489_01: fuglens hode-/øyefelt, 107 endringer. Dette er ikke bare ett nytt øyepunkt; behold hele kildeformen i boksen. |
| 052_04 del1, kontekst42 | 486_04: snute, 68 endringer. 490_01: tukanen er borte, 624 endringer. Den vannrette sittepinnen og vegg/bakgrunn blir igjen. |
| 052_05 til 052_10 del2, kontekst42 | 486_05,06,07,08,09,0A: seks egne snutefelt med henholdsvis 65,63,76,95,93,77 endringer mot grunn. 0A er heksadesimal tilstand, ikke et antatt videre desimaltall. |
| 052_11 del2, kontekst42 | 487_01: lite fot-/tåfelt, 40 endringer mot grunn. |
| 052_12 del2, kontekst42 | 488_01: øyefelt, 12 endringer mot grunn. Alle 12 RGB-endringer er listet i familiebeviset. |

Tukanen er gul/svart med oransjerødt nebb, ikke en ny prinsesse selv om et registernavn nevner tiki-princess. Øglen er det store grønne reptilet som ligger på den mørke steinen i forgrunnen. Den grågrønne snuten, svarte munnstreker, lysegrønne striper og mørke naboflater må følge hver kildevariant. Ingen nye hoggtenner eller tunge er bevist i disse små feltene. Fargen på øye/fot må ikke normaliseres til ett felles symbol. Tilstandsrekkefølge, tale, pust og runtime-utløsere er ikke fastslått.

Senere produksjon bør bygge én sammenhengende ny feltfamilie mot korrekt eksisterende rom052-HD. Hele kropp, stein og rom utenfor faktisk union beholdes der det er mulig. For 01/02 komponeres unionen på master før klipp. 03 til 12 må ikke arve samtidige åpne inngangs-/telefonboksdører eller tukanvariant fra 01/02. 04s tomme fuglefelt må nytegnes som tomt underlag, ikke dekkes av en fargelapp. Ingen originalpikseloppskalering, originalkonturmaske eller lokal warp er tillatt.

## Avgrensninger og neste kontroll

Ingen avgjørende uklar motividentitet krever et nytt spørsmål etter denne kilde- og flervisningskontrollen. Små øglevarianter beskrives med den observerte formen, uten påstand om nøyaktig animasjonshandling. Det trykte plakatinnholdet og bakgrunnens innredning skal ikke nytolkes. Før produksjon må rot lese denne planen. Etter eventuell produksjonsordre kreves innebygd imagegen, bevarte råbilder og prompter, presis plassering, faktisk uendret sjekk_leveranse.py, målt perobjektkorrelasjon og samlet visuell kontroll av alle tilstander og panoramaoverlapper. Teknisk OK er ikke runtime eller individuell brukergodkjenning.


## Produksjonskorreksjon 2026-10-14

480_01 har forskjøvne skrå dørblad og synlig midtsone. Tidligere ord om lukket dør var for grovt. Lag049_01 er rekonstruert med presis vektor etter rotens avklaring av Toms eksisterende autorisasjon for samme VR-rom, dokumentert i a-lag049_01-metodevalg.json. Unntaket gjelder ikke andre rom. Se a-kilde-qa.md for faktisk valgt metode og begrensninger.
