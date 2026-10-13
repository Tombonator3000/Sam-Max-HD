# Bestilling 58 C: Max opp ned, kostyme 205

Kun kildeanalyse. Ingen bilder er generert, ingen resultatfiler endret. 12 beskyttede jobbfiler er SHA-256-låst i `c-kildehash.json`. Hele familien er 57 ruter på tre ark, med 56 ulike synlige RGB-motiver. Alle tre originalark og rom040 er sett visuelt. Analyseoppskriftene er bevart som `.py.txt` og lager bare rapportbevis.

## Dokumentert kontekst og identitet

Dette er Max alene, opp ned, i den opp-ned-vendte gavebutikken rom040. Kremhvit kropp, lange ører med rosa innside, rosa nese, svarte øyne og egne tann-/munntilstander. Ingen klær, hatt, glassbeholder eller rekvisitt skal legges til. Den separate 207-familien viser Mini Vortex-beholderen; den er ikke del av 205-rutene.

`konsept/2026-10-12/skript-kostymekoblinger.tsv` knytter kostyme 205 til actor 3 i rom040/lokal200 linje5, lokal202 linje34, lokal203 linje136 og lokal208 linje7. Kostymeregisteret beskriver denne statiske Max-koblingen med forbehold. Den faktiske figuridentiteten bekreftes her visuelt og gjennom eksakte originaldubletter til Max003. De fulle lokale skriptene er ikke tilgjengelige i mappens kildebevis; analysen påstår ikke runtime-bevist sekvenstiming.

## Ark og sekvenser

| Jobb | Ruter | Faktisk innhold |
|---|---:|---|
| fig205_01 | 28 | Tre opp-ned kroppsdeler, tre separate hoder, to små ansiktslag, åtte høyregangruter, tolv separate høyre talehoder |
| fig205_02 | 21 | Tolv talehoder forfra, tre bakhoder, seks gangruter forfra |
| fig205_03 | 8 | Åtte gangruter bakfra |

`c-sekvens-*.png` viser hver metadata-gruppe i kilderekkefølge. Merk at faktisk a4/r1 også bruker cel 257 mellom 266 og 274. Jobbarket lister257 bare én gang under stående; animasjonsmetadata gjentar den i talesekvensen. Nytegningen må derfor fungere i begge sammenhenger.

## Rel, lag og levering

Full originalmetadata ligger i `c-rutekart205.json`, inklusive hver synlig boks, relativ posisjon, råcelmål og målrektangel. Format 0x58, 16 palettindekser, rom 40 / palett 0, speil=false, alle move_x/move_y=0. Retning 0 deler kildecels med retning 1; ikke tegn ekstra venstreruter ut fra standardpromptens generiske speilforklaring.

Stående sammensetting er [129,257,385] høyre, [128,256,384] forfra og [130,258] bakfra. `c-rel-sammensetting.png` viser den faktiske rel-plasseringen. Kroppens synlige y er 1..23, hodet 23..53 og de små lagene 30..32. Smålagene er de få lyse ansiktsmarkeringene som dekker øyestedene i sammensettingen, ikke nye lemmer eller hele hoder. Nøyaktig spillfunksjon/timing er ikke runtime-bekreftet.

Mange råcelrektangler er50×62 eller52×64 selv om bare et lite hode er synlig. De skal ikke fylles. Leveranse er 1536×1024 RGBA, ekte ny alfa, med synlig kildeboks [x,y,x2,y2] på [64+4x,32+4y,64+4x2,32+4y2]. Cyan er analysebakgrunn, ikke pels. Kildealfa brukt til rapportens sammensetting er kun analyse og skal aldri brukes som produksjonsmaske.

## Palett og originaltrohet

Synlige kildefarger: (255,243,227) krem, (251,251,251) lyst, (215,179,143)/(207,195,179)/(179,147,119) kontur/skygger, (223,115,107) rosa, (199,79,43) rødbrun og (0,0,0). Bakgrunn(0,200,200) er ekskludert fra motivmålingen. Godkjent `hovedark/max.png` bestemmer strek/identitet; kilden bestemmer opp-ned-orientering, skyggeplassering og uttrykk. Ingen automatisk ny lysretning bare fordi Max er snudd.

## Gjenbruk og nødvendige egne varianter

49 av 57 synlige kildeutsnitt matcher Max003 eksakt i RGB og dimensjoner: 47 ved vertikal vending, to små ansiktslag uten vending. Dette er ikke 180-graders rotasjon: venstre/høyre må beholdes. `c-dublettkandidater.json` gir alle kildetreff; `c-donorrelbevis.json` knytter foretrukket003-donor til faktisk205-rel og målpakking. Dette er kildebevis, ikke ferdig godkjenning av en bestemt HD-donorfil. Før produksjon må mottatt donor, celuttrekk og SHA velges og kontrolleres.

De åtte uten eksakt donor er 257,258,274,289,290,288,291,295. Av disse er 258 og 295 eksakt identiske innbyrdes, altså sju egne motiver. 257 avviker bare én RGB-piksel fra vertikalt vendt003/385 ; 274 avviker åtte fra003/402. Disse må ikke blindt kalles dubletter. Nærbildene `c-naerdonor-1.png` og `c-naerdonor-3.png` dokumenterer forskjellen. Øvrige nærmeste samme-størrelse-treff er ikke meningsfulle gjenbruksbevis ; 288 har ikke engang slikt dimensjonstreff. Hode-/øreform og munnstilling skal styres av egne originaler.

## Anbefalt produksjonsdeling og kontroll

1. Frys valgt mottatt Max003-donor med SHA og trekk de 49 kildebeviste komponentene. Vend bare 47 vertikalt og pakk alle etter205, uten originale produksjonsmasker.
2. Nytegn de sju egne motivene i en samlet hodefamilie; gjenbruk den ene nye258-komponenten eksakt til 295. Små257/274-avvik kan gjøres med lokalt innebygd imagegen på valgt ny donor, med øvrig komponent bevart.
3. Kontroller alle 57 faktiske ruter og alle tre gangsekvenser, talehoder på riktige kroppsdeler og to smålag i sammensetting. Kjør uendret checker på tre hele ark. Tynne smålag krever egen visuell kontroll selv om checker hopper over dem.

Motividentiteten fremstår avklart; ingen ny ukjent rekvisitt eller gest er sett. Runtime, faktisk motor-speiling, animasjonstiming og HD-import er uverifisert. Denne planen autoriserer ikke generering på egen hånd; root skal først sammenlikne planen med familien.
