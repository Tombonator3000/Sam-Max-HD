# Bestilling 24: ti lagkompositter

Alle ti lag er produsert og får OK i uendret sjekk_leveranse.py. [Manifestet](a-leveranser.json) har resultathash, hvert genereringsforsøk, prompt, råbilde, referanser og perobjektmåling. [Samlet kontaktark](a-samlet-kontaktark.png) og [original/HD-basis/resultat i kontekst](a-kontekstqa.png) er visuelt kontrollert. Ingen import, runtime eller ny individuell bildegodkjenning er utført.

## Kilde og identitet

Produksjonen følger a-kildeplan.md og roots direkte produksjonsordre. De 40 beskyttede filene er uendret, dokumentert i a-kildehashkontroll.json. Ingen vektormetode er brukt. Vektorunntakene for andre navngitte jobber er ikke overført til TV eller antenner.

De ti konkrete ressursene er 071_0C, 078_01, 067_01, 071_0D, 078_02, 067_02, 071_0E, 078_03, 067_03 og 071_0F. Dette er tre objektfamilier, ikke ti desimaltrinn av samme TV-bilde. Ressursnavnene office-tv, office-tv-static og antenna avklarer komponenttypen, men beviser ikke navn på TV-figurer, film, replikk eller runtime-rekkefølge.

071_0C har grønnt felt, venstre oransje/brune motiv med blått nederst og høyre lys krem/rød/brun/hvit form med brun øyestrek. 0D bruker den andre konkrete øye-/nedre motivtilstanden med svart høyre øyefelt. De små formene er holdt enkle og delvis geometriske; ingen ny kjent figuridentitet eller tekst er lagt til. Nytegningen er ikke påstått pikselidentisk med de syv endrede kildepikslene.

071_0D, 0E og 0F er identiske i de dekodede kildekomposittene. Samme nye kontrollerte bilde fra lag15 er derfor brukt i lag18 og lag21. Sluttfilene har identisk SHA-256. Ressurs-ID-ene og egne jobbnotater er beholdt. Dette er kildebevist gjenbruk, ikke en antakelse om avspillingsrekkefølge.

078_01 og 02 har ulike grønne/grå, oppstykkede stripefordelinger. 078_03 har også fersken-, brun-, rød- og blåfargede motivrester. Alle er nygenerert fra egen referanse; ingen tilfeldig ny støymatte erstatter dem. Glans og antialiasing gir lokale forskjeller fra originalens flate pikselfelt. 078_03 ligger nær checkerens OK-grense og bør vurderes i nærbildet ved mottak.

067_01 og 02 har hver sin sammenhengende tynne antenneløkke med ulik øvre helling og kort stamme. 067_03 har ingen antenne eller stamme. TV-skjermen er grå og tom i alle tre antennelag. Det første 067_02-forsøket ble feilaktig stiplet av HD-ankeret og ble forkastet. Ingen slike stiplede komponenter er valgt.

## Kontrollresultater

| Ressurs | Objektkantkorrelasjon | Utfall |
|---|---:|---|
| 071_0C | 0.642214 | OK |
| 078_01 | 0.850231 | OK |
| 067_01 | 0.924687 | OK |
| 071_0D | 0.623236 | OK |
| 078_02 | 0.734327 | OK |
| 067_02 | 0.939961 | OK |
| 071_0E | 0.623236 | OK |
| 078_03 | 0.602296 | OK |
| 067_03 | 0.942121 | OK |
| 071_0F | 0.623236 | OK |

Ingen objektfelt ble hoppet over. Helbildene har globalt skift omtrent 0.04 til 0.05, blokk 0.08 og kantlikhet 0.97 til 0.98. [Perobjektkontroll](a-perobjektkontroll.json) inneholder full presisjon, original kantstandardavvik og rektangler. Helbildets gode tall brukes ikke som erstatning for objektkontroll eller visuell kontroll. Første 078_03-sammensetting var SJEKK; loggen er bevart som kontroll01. Den endelige filen er faktisk kontrollert på nytt etter skjøtbehandlingen.

## Sammensetting og forsøk

Tolv innebygde imagegen-kall er bevart. Eksakt bildemodell er ikke eksponert. Åtte første komponentforsøk, ett ekstra antenne02-forsøk og tre fullromsforsøk gir tolv. Lag18 og21 bruker eksisterende nytt lag15-bilde uten eget genereringskall. Alle prompts begynner med den ordrette jobbprompten og har kildepresisering som eget etterfølgende avsnitt.

Levert jobber/rom007_del1av2/resultat.png er felles NYTEGNET basis. Originalanalysen beviser at de ti kildene er identiske med grunnrommet utenfor sitt respektive metadatafelt. De endelige resultatene er målt byte-identiske med denne HD-basisfilen utenfor eget felt. Telefon med rødt rør, standardvinduer, dør, dartprosjektiler, papirer og øvrig romrot kan derfor ikke ha blitt byttet til feil lag02-/lag03-tilstand av disse endringene.

TV-komponentene ble generert som lokale utsnitt, helskalert med Lanczos til 96 x 96 og plassert ved [576,464]. En seks HD-pikslers lineær overgang på alle fire rektangelkanter blander bare NYGENERERT komponent med NYTEGNET HD-basis. Masken beregnes utelukkende fra avstand til det rektangulære feltets kanter, ikke kildefarger eller originalsilhuett. Den fjerner synlige harde skjøter i TV-kassen og bordflaten. Kjernefeltet er uendret; ingen geometri flyttes. a-skjoter.py.txt og a-skjotbevis.json bevarer metode og førverdier.

Antenneforsøkene som bare fikk lokal utsnittskontekst ga synlig veggfargeforskjell. Rektangulær kantovergang kunne dessuten la et lite fragment av den gamle antennen stå igjen. Disse sammensettingene er forkastet og bevart som mellomforsøk. Endelig løsning er fullromsgenerering med kildekompositt og HD-basis som referanser. Bare et rektangulært utsnitt [544,392,144,72] innenfor metadatafeltet [544,368,160,96] tas fra den nye genereringen. Dette inneholder hele den gamle og nye antennen, men lar eksisterende bilderammekant og kulehull til høyre komme direkte fra HD-basis. Ingen kantovergang brukes på de endelige antennefeltene. Oppskriften er a-antenner-fullkontekst.py.txt. Det er ikke en konturmaske og ikke lokal warp.

Alle ti leveres opakt RGB 1536 x 1024 med motiv [0,112,1536,800] og eksakt RGB128-padding. Originaler eller originalpikselmasker er aldri brukt som synlig erstatningskunst. Ingen skjult alfa, vektortrace eller ny kode i motor/pipeline er innført.

## Begrensninger og mottak

Det nye TV-motivet er fortsatt lite, med antialiasing og enkelte malte høylys. Kildeformene er bevart som mål og synlig familie, men det er ikke bevist at hver enkelt mikropikselendring gir identisk dekodet farge etter HD-rendering. Svakest margin er 078_03 med 0.602296 mot OK-grensen 0.60; tall og nærbilde skal følge mottaket. Ikke kall dette runtime-bevis eller ny brukeraksept.

Kildeplan, råforsøk, alle faktiske prompter, forkastede førbilder, oppskrifter, eksakte kildehash og sluttresultathash er bevart i denne mappen. Root eier videre samlet QA, kø, Git og levering.

## Retting etter uavhengig kontroll av antenneskjøter

C og root fant en synlig lys rektangelgrense i særlig 067_01 og 067_03, selv om checker ga OK. Dette var en faktisk komposisjonsfeil. De tre antennefeltene er nå fargesammenpasset med grunnrommet uten å flytte eller blande inn gammel antenne. Ny fullromsgenerering beholdes som motivgrunnlag.

Oppskriften `a-fargesammenpassing.py.txt` beregner RGB-differansen mellom NYTEGNET felt og NYTEGNET grunnrom langs rektangelets kant. En fast median over 21 HD-piksler fjerner isolerte mørke innslag fra fargeestimatet. Dette er bare et estimat av veggfarge, ingen originalkonturmaske. En harmonisk additiv RGB-korreksjon interpoleres deretter over feltet med fire naboer. Ingen geometri, kildepiksler, vektor eller innhold fra gammel antenne blandes inn. Fargefeltet er lagret som NPY med min/maks/gjennomsnitt, konvergens og SHA i `a-fargesammenpassing-bevis.json`. Førbildene og tidligere manifest er bevart.

Nærkontroll før/etter finnes i `a-fargesammenpassing-naerkontroll.png`; nytt fullsceneark og kontekstark er oppdatert. Begge løkkene og stammen beholder sin form, mens 067_03 fortsatt er uten løkke og stamme. Veggens rektangulære tonehopp er fjernet ved egen visuell kontroll. Uendret checker gir fortsatt tre OK; objektkorrelasjonene er nå 0,946990, 0,957081 og 0,956508. Dette er teknisk kontroll, ikke runtime eller ny brukergodkjenning. C gjør separat visuell etterkontroll.
