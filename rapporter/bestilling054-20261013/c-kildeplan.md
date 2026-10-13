# Bestilling 54 C – Sam kostyme 7, fig007_01–06

Analyse 14. oktober 2026. Bare kilde- og rapportarbeid; ingen generering, gjenbrukskomposisjon eller jobbendring. Sam 002 i bestilling 52 står frosset for rotmottak.

## Bevis og identitet

24 beskyttede jobb-/prompt-/original-/referansefiler er låst i `c-kildehash.json`. `c-original-kontaktark.png` viser seks ark; `c-sekvens-*.png` viser hver animasjon/retning/laggruppe. `c-rutekart-kilde.json` har alle 109 ruter, eksakte pakkerektangler, synlighetsbokser, relative posisjoner, bevegelsesfelt og egne RGB-sammenlikninger mot Sam 002. `c-rel-sammensetting.png` viser ti statiske originalkomposisjoner. `c-analyse.py.txt` bevarer måleoppskriften. Ekstra kildelås dekker originalmetadata, roots kandidatregister og Sam-hovedarket.

Dette er Sam, ikke en ny figur bestemt av kostyme-ID. Jobbnavn/anker er Sam/hovedark/sam.png, figurens brune pels, blågrå dress/fedora og stripede slips stemmer, og `skript-kostymekoblinger.tsv` knytter kostyme 7 til skuespiller 2 gjennom en rekke skript. Brune bare poter og de samme proporsjonene gjelder. Jeg har sett alle seks originale ark.

Begge kostymer bruker rom 1, palett 0, format 0x58 og 16 palettindekser. Indekslistene er forskjellige: kostyme 7 har 235, mens kostyme 2 har 255. Det er derfor **ikke** bevist at hele kostymenes palettoppsett er likt. De konkrete dublettene nedenfor er like i ferdig dekodet RGB, inklusive transparente magentafelt innen synlig boks, og trenger ingen antatt indekskonvertering.

## Oversikt

| Ark | Antall | RGB-like 002-ruter | Faktisk innhold |
|---|---:|---:|---|
| fig007_01 | 23 | 23 | Tre hodeløse hvilende kropper, todelt håndlag, tre hvilende hoder, to øyelokkpar og 14 høyrevendte talehoder. |
| fig007_02 | 25 | 25 | 13 frontvendte talehoder, to bakhoder, fem todelte håndlag, fem a07-helfigurer med hender ved bryst/slips. De siste fem har samme ventepunkt som 002. |
| fig007_03 | 21 | 0 | Smal hodeløs/armløs kropp 179, seks faser av fjernt arm-/håndlag 8 og seks av nærmere arm-/håndlag 9; deretter fire nye varianter på hvert av lagene. Ikke 20 nye hele figurer. |
| fig007_04 | 15 | 0 | Hodeløse kroppsvarianter på lag 0. Hånden beveges opp og inn ved dressens side/lommeområde; kroppen forskyves/svikter ulikt. Ti a17-ruter og fem a18-ruter. Ingen separat sikker rekvisitt. |
| fig007_05 | 9 | 0 | Fire helfigurer a19 der hatten står løs over hodet og ørene løftes, fire a20-helfigurer med endrede ører/hatt/uttrykk; siste rute er hodeløs/armløs kropp 178 til senere lagsammensetting. Den løse hatten er del av samme cel, ikke en rute som kan slettes eller presses ned på hodet. |
| fig007_06 | 16 | 2 | Tre torso-/skulderlag 10, ni smale arm-/håndlag 11, ett separat hode på lag 12 og øyelokk på lag 13, samt to egne erme-/håndlag 6. De tynne blågrå flikene er arm-/dresslag i sammensetting, ikke rekvisitter eller ekstra ben. |

Totalt 109 ruter, hvor 50 er synlig RGB-identiske med 002. Fem av de 50 er ventende a07. Dermed finnes 45 kildebeviste gjenbrukskandidater uten dette gestusventepunktet, og 59 ruter uten eksakt 002-treff. Gjenbruk av nye 002-bilder venter på roots mottak.

## Gjenbruk, lag og den viktige pakkefellen

Alle 50 treff har samme synlige størrelse og samme synlige verdensopprinnelse som 002. De første 48 har også samme lag og retning. I 007_06 er cel 1536 identisk med 002 cel 385 (hode), men flyttet fra lag 3 til lag 12; cel 1664 er identisk med 002 cel 513 (øyelokk), men flyttet fra lag 4 til lag 13. Rel-koordinatene er uendret: hode (-13,-70), lokk (1,-58). Metadata for a29/a30 bruker disse som hode-/øyelokk-lag, så lagnummerendringen er ikke ny identitet. Gjenbruk av selve HD-komponenten er begrunnet; behold det nye kostymets lagnummer og pakking.

**007 cel 128 kan ikke behandles med blindt helrektangelklipp.** Dets metadata har 70 × 70-rektangel [42,-14,70,70], rel(-32,-70), mens synlig område er [52,5,100,56], altså 48 × 51. Det synlige motivet er helt likt 002 cel 128 med rel(-22,-51). Kompensering med synlig offset gir nettopp (-22,-51). Pakkerektangelet går over arkets topp og omfatter tomt område/naboer; bruk eksisterende nytegnet **komponent** og den dokumenterte synlige målposisjonen, ikke et rått stort rektangel fra resultatarket. Ingen originalkonturmaske trengs eller tillates av dette funnet.

HD-plassering er som før: 1536 × 1024 RGBA; synlig [sx0,sy0,sx1,sy1] blir [64+4sx0,32+4sy0,64+4sx1,32+4sy1]. Magenta/grå kildepadding er transparent i levering. De 50 treffene er målt uavhengig av roots grovere kandidatregister, som bare er et søkegrunnlag.

## Rel-kontekst og bevegelse

Kropp 179 har rel(-13,-52), 35 × 52, uten de armene som lag 8/9 skal levere. Kropp 178 har samme størrelse/rel, men en egen kontur; de må ikke byttes eller fylles ut med pilotens komplette armer. Lag 8 og 9 overlapper kroppen etter egne rel-koordinater. Statiske eksempler i c-rel-sammensetting viser dette.

Lag 11 sine første to celler er bare 7 × 28 ved rel(12,-44). Senere faser flytter arm/hånd mot ansiktet. Med kropp 178, skulderlag 1285/1287 og hode 1536 ser hånden ut til å ligge ved snute/hake, ikke holde en ny gjenstand. Dette er visuell rel-kontroll, ikke navngitt handling eller fullstendig bekreftet tidskobling.

A17/a18 har move_x fra 0 til -4 i ulike cels; disse skal ikke nullstilles i en hypotetisk runtime-sammenstilling. A26/a27 gjenbruker deler av disse kroppscellene i andre rekkefølger. A13/a14/a21–25 gjenbruker armcellene i flere kombinasjoner. Originalens metadata lister dedupliserte ressurser, ikke venting og gjentakelser. Kontaktark eller lik RGB alene beviser derfor ikke en avspilling.

## Avklaringer til rot før nytegning

1. A07 i 007_02 er nøyaktig den samme femruters gesten som venter i 002. Ikke spør på nytt eller generer en annen tolkning.
2. A13/a14 viser åpne/lukkede hender og armbevegelser uten en synlig separat rekvisitt. A17/a18 viser hånden ved/inn i dressens side. A19/a20 viser hatten løftet og ørene i ulike stillinger. A29/a30 viser en hånd ved snute/hake. Disse formene kan beskrives direkte, men jeg har ikke kildebevist funksjonsnavn som «forklarer», «leter i lomma», «overrasket» eller «tenker». Rot bør se sekvensene og sammensettingen og avgjøre om en meningsavklaring kreves før de 59 nye rutene tegnes. Ingen slik rekvisitt eller årsak skal oppfinnes.
3. Ved nytegning av hattsekvensen må luftgapet mellom hatt og hode beholdes. Ved nye arm-/skulderlag må klippede skjortebiter, mansjetter og tomrom beholdes. De må ikke normaliseres til komplette armer eller torsoruter.

Anbefaling: hold familien hos samme eier. Etter rotmottak av 002, klargjør først de 45 avklarte dublettene med dokumentert donor-SHA/celboks; bevar de fem a07-ventecellene. Generer de 59 nye cellene i grupper etter lag og kontroller over de riktige hodeløse kroppene. Alle 109 ruter trenger separat rutekart/komponentkontroll, også små øyelokk som hjelpecheckeren kan hoppe over. Runtime, import og ny brukergodkjenning er uverifisert. Ingen produksjonsendring er gjort i denne analysen.
