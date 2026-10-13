# Max006: kildeanalyse og produksjonsplan

Kun analyse. To ark, 32 ruter. Åtte beskyttede filer er låst i [a-kildehash.json](a-kildehash.json). Fig236_01 og øvrige55-filer, samt frosset54, er ikke endret. Ingen bildekall er utført.

## Fordeling og identitet

Fig006_01 har15 ruter: åtte grunnlag og sju nye a17-poser fra siden. Fig006_02 har17 nye a17-poser: sju forfra og ti bakfra. Alle viser Max, kremhvit pels med beige/grå skygger, rosa øreinnsider/nese/potefelt der kilden viser dem, mørke øyne og egne munnuttrykk. Ingen separat rekvisitt er påvist. «a17» beholdes som teknisk ressursnavn uten ubekreftet funksjonsnavn.

De åtte grunnrutene129/128/130,385/384/386,513/512 har identiske RGB-kildepiksler, dimensjoner og celmetadata med fig003_01. De er henholdsvis tre kroppslag, tre hodelag og to små øyelokkslag. [a-kildebevis.json](a-kildebevis.json) dokumenterer hvert treff. De24 a17-rutene har ingen identisk rute i de fem003-arkene som ble sammenlignet. Bare de åtte pilotrutene er dermed dokumenterte gjenbrukskandidater.

Kostymepalettene003 og006 er identiske: [3,234,235,236,237,238,239,240,241,9,10,11,12,13,14,15], rom1/palett0. Synlige RGB-farger er registrert separat per rute. Ulike skygger og rosa felt i hver pose skal bevares, ikke utjevnes til én generisk fargefordeling.

## Avgjørende atlasregel

`rekt` er den opprinnelige hele celens rektangel, også når store deler av cellen er transparente. For a17 kan rekt begynne utenfor arket og overlappe andre atlasmotiver. `synlig` er den korrekte avgrensningen av den enkelte synlige tegningen på arket. Eksempel267: rekt[-3,53,43,87], men synlig[4,96,40,140]. Eksempel259: rekt[-2,-24,45,87], men synlig[4,20,43,63].

Blind klipping av rekt fra atlaset tar med naboer og utenforliggende svarte piksler. Dette skjedde i første diagnostiske utkast og ble rettet før rapporten ble levert. Alle gjeldende feltark og målinger bruker synlig. Det er ingen svart tilleggsfigur, ingen ekstra hoder eller øyelokk inne i a17-cellene.

For statisk verdensplassering brukes:

`world_xy = origin + original_rel + (synlig_xy - rekt_xy)`

For produksjonsatlas brukes synlig-boksen ×4 pluss canvasoffset[64,32]. Ikke tegn den tomme delen av originalrektangelet, ikke sentrer alle figurene rundt en ny grunnlinje, og ikke flytt eksisterende kildefester. Original rel_x/rel_y for sidene er(-22,-86), for forfra(-23,-86), for bakfra(-27,-80). Synlig-offsetene gjør at figurene bevisst flytter seg i høyden rundt samme feste.

## Konkrete a17-poser

| Retning | Cel og synlig posering |
| --- | --- |
| Side,7 | 267 lavt bøyd med arm bak;268 langstrakt med hengende føtter og knekte ører;269 og270 foroverbøyde med ulike bein/hender;271 svært lange rette ører og lave hender;272 flat/lav kropp med utstrakte lemmer og bakoverbøyde ører;273 lav med bøyde knær, hånd fram og senkede øyelokk. |
| Forfra,7 | 259 lavt bøyd;260 langstrakt med ulik ørebøy;261 spredte bøyde bein;262 brede framvendte fotsåler;263 oppstrakte armer, lange ører og store synlige såler;264 svært lav og bred med knekte ører;265 lav med sidearmer og senkede øyelokk. |
| Bakfra,10 | 275 til277 egne stående/lave kroppshøyder og armstillinger;278 lange hengende føtter og hengende ører;279 opptrukne bøyde bein og nesten horisontale ører;280 kompakt kropp med opprette ører;281 langstrakte ører og bøyde bein;282 høye ører og oppstrakte armer;283 sammenfoldede/knekte øreformer over lav kropp;284 hengende ører over lav ståstilling. |

Denne tabellen beskriver synlig form, ikke handlingens årsak eller avspillingshastighet. Rosa felt i føttene er synlige potefelt, ikke sko eller nytt utstyr. Bakfra skal ingen ansikter legges til. Bevar kildens asymmetri og avkutting.

## Komposisjonsbevis

[Originalkontaktark](a-original-kontaktark.png), [grunnlag og rel-sammensetting](a-rel-grunnkomposisjon.png), samt alle32 nærfelt: [1](a-feltark-1.png), [2](a-feltark-2.png), [3](a-feltark-3.png), [4](a-feltark-4.png). Alle felt er sett etter korrigert synlig-klipping.

[A17 side med felles origin](a-a17-rel-retning1.png), [a17 forfra](a-a17-rel-retning2.png), [a17 bakfra](a-a17-rel-retning3.png). Røde akser er analysemerking og skal ikke med i leveransen. Originalens cyan brukes bare diagnostisk til å vise kildedeler på grå flate, ikke som produksjonsmaske.

## Produksjon etter rotens lesing

1. Kontroller mottatt pilot00301-hash og gjenbruk bare de åtte dokumenterte nye RGBA-celene. Behold små øyelokksforskjeller og kontroller dem eksplisitt hvis checker hopper over dem.
2. Nytegn24 a17-poser med innebygd imagegen, delt i de tre konkrete retningsgruppene7/7/10, med ordrett jobbprompt og separat kildepresisering. Originalens synlige utsnitt og rel-bevis prioriteres; godkjent hovedark/pilot styrer identitet og tegnestil. Ingen nye funksjonsantakelser eller rekvisitter.
3. Plasser hele NYE komponenter presist etter synlig-mål, uten originalkonturmasker eller lokal warp. Bevar rekt/synlig/rel-forskjellen i komponentkartet.
4. Lever ekte RGBA1536×1024, transparent cyan/grå kildebakgrunn og padding. Kjør uendret checker på begge hele ark, og kontroller alle32 felt samt verdensplassering, små lag og familie samlet.

Ingen motoravspilling eller ny individuell godkjenning er utført. Oppskrift og konteksthash: [a-analyse.py.txt](a-analyse.py.txt), [a-konteksthash.json](a-konteksthash.json). Alle beskyttede kilder beholdes uendret.
