# Hele animasjonsmotiver, inventareske og LucasArts-logo

15. oktober 2026. Grafikkgrenen `gpt-arbeid`. Innebygd bildeverktøy, eksakt modellnavn ikke eksponert. Python til rensing, normalisering og plassering er uttrykkelig godkjent av Tom. Ingen kodeendringer.

## Levert

- 44 komplette RGBA-bilder i [leveranser.json](leveranser.json), med mål og SHA-256. 32 ligger i `objects/`, 12 bassengbilder med korrekt palett ligger i `runtime-rom054/objects/`.
- 22 jobbresultater oppdatert. Egenkontroll: 20 OK, 2 SJEKK, ingen FEIL. Se [jobblisten](endrede-jobber.json) og kontrolltekstene ved siden av denne rapporten.
- 36 av 39 lapp-tilstander har komplett native HD-tegning som eksisterende `_patch_from_full_painting` godtar. Tre lapp-tilstander i objekt 835 avventer motivavklaring. Ingen av objekt 835s fire kandidatbilder er levert til import.
- Inventaresken har egen alfa og renset ytterkant. Stempelet er utvasket. Toms opplysning: sannsynligvis THX1138 med utydelig tekst under. Dette er en tentativ lesning, ikke en kildeverifisert transkripsjon. Eksisterende native stempelutforming beholdes slitt.
- LucasArts-logoens eksisterende native motiv og bokstaver er beholdt. Magentanøkkelen er renset, også inne i åpningene. Hele ikon01 bruker grønn nøkkelbakgrunn. Separat RGBA-logo levert.
- Tidligere manglende `lag056_04` er komplettert med åpen fryser, tom isplukkholder og Conroy Bumpus/Lee Harvey frosset i forkledningen. Den tekniske kontrollen er OK.

## Motivgrunnlag og rettelser

Originale SCUMM-ressurser, romutsnitt, dekompilerte skript og relevante eksisterende HD-rom er undersøkt. Fullstendige kildemotiver ligger i `kilder/`; plassering, tilstander og jobbkoblinger i [objektfamilier.json](objektfamilier.json). Skriptene for kildekontaktark er bevart som `.py.txt`. Beskyttede jobbmetadata og referanser er ikke omskrevet.

154 er mannen med kranhode; 155 er den sammenkrøkte mannen i grønt kar. 180 til 182 er flagg. 183 er propellen på andeattraksjonen, med alle synlige blader i hver kildefase. Første propellforsøk utelot faste deler og er forkastet; forsøk 2 følger komplett hovedtilstand pluss lapp. 222 er den maskerte bøddelen med øks og den lille figuren ved blokken, ikke en musiker. 301 er små elektriske gnister. 350 er fisken som passerer speilet, og 352 den avskårne åtteballen. 439 er frosketrofé, 444 det smale kattetroféansiktet. 530 er isplukkholderen, også tom tilstand. 897 er laboratoriets kule og energiring. 318 er en svært liten grå rest; eksisterende native HD-utsnitt er gjenbrukt komplett, uten oppdiktet ny figur.

### Rom 83 er lager for bassengscenens grafikk

Den eldre beskrivelsen av disse bildene som bilder i skyer var et feil premiss. Globale skript [108](scrp_108.txt) og [109](scrp_109.txt) bruker objektene 833 til 836 i rom 54. Lagerrom 83s palett får skog og pels til å se ut som skyer/hvite figurer. `sluttscene-rom54-original.png`, `obj833-referanse-rom54.png` til `obj836-referanse-rom54.png` bruker rom 54s palett og viser den faktiske bassengscenen.

833 viser Sam og tre ulike sasquatcher; 834 én kjeglehodet sasquatch; 835 den rødpelsede figuren i blått ved høyre kant; 836 den mørke flokken ved flettveggen til venstre. Vi bevarer synlige former, ikke gjettede personnavn. Spillgjennomgangene gir støtte for basseng-/sluttkonteksten: [Sam & Max](https://samandmax.co.uk/games/hit-road/), [walkthrough](https://www.arrpeegeez.com/2023/08/sam-max-hit-road-walkthrough-guide.html). Selve palettvalget og ressursbruken er dokumentert av spillets egne skript.

For 836 er forsøk 1 forkastet: det krympet flokken og la til sklie og rominventar. Forsøk 2 bruker bare originalutsnittet og et beskåret stilbilde av flettveggen, og beholder hele flokken i alle fire ruter.

For 835 er svartfeltet under nesen fortsatt usikkert som bart kontra åpen munn. Et smalt rettingsforsøk ga ingen pålitelig løsning. Tom er spurt; begge råforsøk er bevart som kandidater, uten produksjonsstatus. Den tidligere forespørselen om identiteten til «skybildene» bygger på den nå korrigerte lagerromspaletten og er ikke lenger grunnlaget for arbeidet.

## Mottak: komplette tegninger må bevares før lappklipp

Vanlig lagmottak i `gpt.py::_finish_pieces` gjeninnfører originalens lappalfa. Dette kan miste komplett dekning før modbyggets `_patch_from_full_painting` rekker å klippe. Bruk de komplette RGBA-filene fra denne rapporten som objektgrunnlag før modbyggets lappklipp. [Teknisk kontroll](teknisk-kontroll.json) bekrefter dimensjoner, dekning og faktisk godkjent lappklipp for de 36 leverte lapp-tilstandene.

Bassengbildene leveres separat, uten å males over rom83-malen med feil palett/bakgrunn. Hvert bilde i `runtime-rom054/objects/` har en tilsvarende `_idx.png` med rom54-paletten. Indeksdata og transparens er identiske med originalen; bare paletten er endret. Mottaket må bruke disse tilhørende indeksfilene ved fargelås og videre import. Å bruke lagerromspaletten på de nye tegningene ville gjeninnføre feil farger. Dette er dokumentert overlevering, ikke en pipelineendring eller utført runtimeimport.

## Alfa og visuell kontroll

Ingen synlige nøkkelmagentapiksler er funnet i de 44 separate leveransene. Esken er kontrollert på sort, hvitt, grønt og rødt; [alfakontroll](alfa-kontroll.png) viser resultatet. Bildeverktøyets malte sjakkbakgrunn og frakoblede grå flekker ved eskens høyrekant er fjernet etter nytegning. Originalsilhuetter er ikke brukt som produksjonsmasker.

Originale synlige bokser styrer mål og plassering, med alfa fra den nye tegningen. Skalering bruker premultiplisert alfa. Original og HD er visuelt sammenlignet på fire kontaktsider: [1](visuell-kontroll-01.jpg), [2](visuell-kontroll-02.jpg), [3](visuell-kontroll-03.jpg), [4](visuell-kontroll-04.jpg). Dette er egen visuell kontroll, ikke Toms godkjenning.

SJEKK: ikon01 har globalt blokkskift 1,28 originalpiksler. Den tidligere leveransen hadde 1,42. lag017_04_del2av2 har kantlikhet 0,60 for grønt flagg obj182_04. Begge beholdes som SJEKK og er ikke omtalt som fullgodkjent.

9056 beskyttede filer er SHA-256-kontrollert uendret. [Kontrollskript](kontroller.py.txt), [normalisering](klargjor.py.txt), prompter `*-prompt*.txt`, råforsøk `*-raa*.png` og [manifest](leveranser.json) bevarer arbeidsgrunnlaget. Baseline for tidligere jobber er commit `1f5e0ebf3e37497e730a2375f714f113594cba26`. Eskens native førbilde er også bevart i `for/obj995_01.png` fordi det ble brukt som redigeringsreferanse.

## Publisering og gjenstående

Nyeste Claude-oppdatering `dc5fcba9` er hentet uten konflikt. Den opplyser at de tidligere 111 RGBA-ikonene nå er importert i hd-mod og at pekeren er sett i spillet; inventaret er ikke sett ennå. hd-mod var `e3b7a785` ved kontrollen, med moddato 15. oktober 14:22. Denne rettingspakken er grafikkleveranse på gpt-arbeid og er ikke importert i hd-mod eller spilltestet av denne økten.

Gjenstår: avklare og ferdigstille objekt 835, importere komplette lapptegninger og runtime54-paletter, teste tilstandsbytter og alfakanter i motoren, samt Toms visuelle godkjenning. Animasjonenes timing og overganger er ikke testet ved spillavspilling.
