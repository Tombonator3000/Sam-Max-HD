# Videre grafikkarbeid og Toms seks feilbilder

15. oktober 2026. Grafikkgrenen `gpt-arbeid`. Innebygd bildeverktøy, eksakt modellnavn ikke eksponert. Python er brukt til rensing og plassering med Toms tidligere uttrykkelige tillatelse. Ingen motorkode eller pipelinekode endret.

## Seks oppdaterte jobber

Alle seks består uendret `verktoy/sjekk_leveranse.py` med OK. [Leveranser og SHA-256](leveranser.json).

| Jobb | Retting |
| --- | --- |
| obj811_01 | Ny mellomstripe av kikkerten. Sort åpning, grått hus, rød/gul ring og avskårne hender beholdt. |
| lag037_01_del2av2 | Komplett fase 01 av den avskårne åtteballen. |
| lag037_02_del1av2 | Komplett fase 02 av fisken i speilet og åtteballen. |
| lag045_03 | Grå sengetrinn foran monstertruck-sengen i Bumpusville. |
| rom010 | Sams nedre tannrekke fullført etter Toms rettelse. |
| rom015_del1av2 | Rosa menneskelig kjerub og rød djevel i den fjerne tivolidekorasjonen. Det feilaktige griselignende ansiktet er erstattet. |

De fire nye komplette objektutsnittene ligger i `objects/` med [objektmanifest](objektleveranser.json). Som i forrige leveranse må komplette motiver bevares før mottakets eventuelle lappklipp. Rom- og objektjobbene ligger på ordinære `jobber/<jobb>/resultat.png`-stier. [Plassering/rensing av objektfasene](klargjor-objektfaser.py.txt) og [lokale rettelser](klargjor-lokale-rettelser.py.txt) dokumenterer behandlingen.

Ved plassering på jobblerretet er ytterkanten av de rektangulære utsnittene blandet over 8 HD-piksler, og 12 for kjeruben, for å unngå synlige fargeskjøter. De separate komplette RGBA-objektene er bevart uten denne kantblandingen. Ingen originalkonturmaske er brukt til å klippe de nye motivene.

Rom010 er bare endret innen [895,235,976,310] på HD-lerretet. Rom015 er bare endret innen [584,184,800,380]. Resten av hver native tegning er byteidentisk med førbildet i commit `6ffca8e8fba91c82efb43a0a26b17dfbd9ec3ab8`. Kjeruben ligger utenfor rom015-delenes overlapp; del 2 trenger ingen endring. [Sam før/etter](rom010-sammenligning.png), [kjerub før/etter](rom015_del1av2-sammenligning.png).

Kjerubens første retting ble for portrettaktig og fikk et nytt, smalt ansiktsforsøk. Valgt forsøk 2 har en enklere tegneserieutforming med svarte ovale øyne, små kinn og menneskelig nese. Originalens fjerne positur styrer plasseringen; den nærmere Tunnel of Love-visningen gir figuridentitet og stil. Frontbildet i rom21 viser allerede rosa kjeruber og rød djevel, og er ikke omskrevet.

Originalprompter og jobbmetadata er bevart. Store objektforsøk og lokale romrettelser bruker originalprompt med separat presisering. Lagrettingene bruker en separat komponentprompt på et kontrollert kontaktark, med de tilhørende HD-rommene som stilreferanser. Kildegeometri og beskyttede prompter er ikke endret. Alle faktiske prompter og råbilder ligger ved denne rapporten. 40 beskyttede filer er SHA-256-kontrollert uendret.

## To objektreturer er fortsatt ikke løst

Nytt hammerforsøk for obj187_05 har høy kantlikhet, men feiler blokkforskyvningen. Et forsøk med det kildeidentiske blå bakgrunnsområdet fra godtatt tilstand01 hjalp ikke. To nye toppstriper for obj307_01 feiler fortsatt blokkforskyvning i det flate midtfeltet. [Målinger](avviste-forsok-kontroll.json). Disse kandidatene er ikke levert som nye resultatfiler. Tidligere resultatfiler for begge jobber er beholdt byteidentisk. Det er ikke påstått at midtfeltets måling er bevist falsk positiv.

## Sam091: åtte størrelsesreturer skyldes ulike målegrunnlag

`myk.py` i undersøkt main `6269b68e` er byteidentisk med modulen brukt til kontrollen. `measure_mask` utelater en liten løs fotrest på 36 eller 37 originalpiksler som utligger. HD-målingen tar derimot med både hovedfigur og fotrest fra rutekartet. Det gir 23 til 30 prosent tilsynelatende høydeavvik.

For alle åtte returnerte ruter er hele HD-boksens høyde nøyaktig 4x hele originalboksens høyde. Eksempel costume091_1955: originalen er 69 piksler høy med fotrest, men måles som 53 uten; HD er 276 piksler høy med fotrest. 276/(53x4) = 1,302, mens 276/(69x4) = 1,000.

[JSON-bevis](sam091-maalegrunnlag.json), [visuell kontroll](sam091-maalegrunnlag.png), [kontrollskript](sam091-maalegrunnlag.py.txt) og [uendrede arkhash](sam091-urorte-ark.json). Den røde boksen i originalen viser importerens mål uten fotresten. Arkene er ikke krympet for å kompensere for denne asymmetrien. Dette opphever ikke automatisk mottakets status; målegrunnlaget må vurderes ved neste import. Det er ikke en påstand om at alle interne tegnekonturer er perfekte.

## Toms fem nye feilpunkter

Originale skjermbilder er bevart som `tom-feilbilde-1.png` til `tom-feilbilde-6.png`, med [sjekksummer](tom-feilbilder.json).

1. Rester etter at et objekt plukkes opp, vist i kontoret. Ikke rettet eller runtimeisolert her. Test opptak og tilstandsendring i rom7, og sjekk at det gamle HD-motivets fulle område bygges på nytt. Skill motorrester fra detaljer som er malt inn i HD-bakgrunnen. Originalskriptet for objekt65 beskriver tunfisksmørbrødet, og objekt66 er Max sin kakerlakkfarm. Skjermbildet alene fastslår ikke hvilken hendelse som etterlot hver rest.
2. Sams nedre tenner på USA-kartet. Rettet i rom010 og kontrollert visuelt og teknisk. Ny import og Toms vurdering gjenstår.
3. Rosa kjerub og djevel bak på tivoliet. Kildene identifiserer rom15s fjerne dekorasjon og rom21s nærmere Tunnel of Love-visning. Det griselignende ansiktet i rom15 er rettet til en rosa menneskelig kjerub. Rom21 er identitets-/stilreferanse. Den hvite svanen i Toms bilde er et separat motiv; den er ikke tegnet i denne delrunden.
4. Artefakter rundt Sam og trehammeren i Wak-A-Rat. Ikke rettet i motoren her. Skjermbildet viser trappete grenser mellom separate objekt-/figurflater. Se også den [bekreftede bilmaskediagnosen](../rom009-bilkanter-20261015/RAPPORT.md). Kontroller alle hammerfaser og overgangen mellom hovedbildet, Sams animerte ansikts-/munndeler og maskene. En ny bildefil alene er ikke bevis på løst kompositering.
5. Rene inventar-/chatrammer. [Syv RGBA-ikoner](ui-native-kontroll.png) er kontrollert direkte mot `hd-mod` e3b7a785 og nyeste undersøkte 9512fd81. Hashene er identiske. De har myk alfa, ingen synlig nøkkelmagenta og ingen synlige piksler med eksakt grønn nøkkelfarge. [Målinger](ui-publiseringskontroll.json). Den rosa trappekanten i skjermbildet er ikke til stede i disse leverte rammefilene. Om årsaken er et eldre kjørende nettleserbygg, originalrammen under HD-laget eller annen kompositering, er ikke isolert. Kontroller derfor faktisk lastet mod/motor og valgt/ikke-valgt chatkort i samme scene. Den store inventareskens nye alfa ligger allerede i forrige importpakke, men den rettingen er ikke bekreftet importert eller vist i spillet.

Ved sluttsjekk var main oppdatert til `9e1b7b29b1b00c595a118eadbeafe2f393e8e2b1` med motor-/pipelineendringen «Myke kanter på romobjekter: bilen i rom 9 uten trappetrinn» (#29). Koden har nå `soft_alpha`, `softEdge` og `drawSoftObjectEdges`, og endrer derfor den tidligere diagnosens forutsetning om hard romobjektmaske. Dette er en kodeendring levert av motorarbeidet, ikke av denne grafikkrunden. Den kan hjelpe romobjektkantene, men viser ikke alene at opptaksrestene, Wak-A-Rat-kompositeringen eller chatkortene er løst i Toms kjørende webbygg. Nyeste undersøkte hd-mod er `9512fd813d96ab6bae31ec042188fa5d767df7ae`; de syv native UI-filene er fortsatt identiske med den rene leveransen. [Kontrollgrunnlag](ny-motorstatus.json).

Punkt 1, 4 og spillvisningen i punkt 5 er fortsatt åpne for bekreftelse i spillet. Rapporten er konkret feilgrunnlag, ikke en ferdig motorrettelse. Dette arbeidet har bare endret de seks grafikkjobbene listet øverst. Denne grafikkrunden har ikke utført import til hd-mod, webpublisering, motoravspilling eller individuell godkjenning fra Tom.
