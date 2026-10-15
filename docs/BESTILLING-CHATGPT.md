# Bestilling til ChatGPT: trofast HD-grafikk for Sam & Max

Til: ChatGPT (bildegenerering, helst som Codex i dette repoet)
Fra: Tom, med Claude som står for koden
Dato: 10. oktober 2026, oppdatert 13. oktober 2026

**Aktiv fra 13. oktober 2026, i stilpiloten.** Alle jobbene er laget og ligger i grenen `gpt-arbeid`. Arbeidet starter med stilpiloten: hovedark for Sam og Max, kontoret (rom 7) og det første figurarket for hver av dem. Resten venter til Tom har godkjent piloten og stilankerne ligger i `stil/`. `ORDRE.md` i grenen sier hva som gjelder nå.

## Kildetro grafikk før produksjon

Les [remake-skillen i main](https://github.com/Tombonator3000/Sam-Max-HD/blob/main/docs/skills/scumm-hd-remake/SKILL.md), særlig «Før HD-produksjon: avklar motiv og design», før stilpilot og nytegning. Avklar motiv, funksjon, riktig palett, person/drakt og design fra originalen i spillkontekst. Bruk spillets egne godkjente stilankere og dokumenter grunnlaget i eksisterende analyse og jobbnotat. Kontroller samme identitet gjennom hele animasjonen og hode/kropp samlet i spillet; alfa og ruteantall beviser ikke riktig motiv.

Regelen gjelder også når jobbformatet ber om ordrett prompt. Ved påvist feil premiss: behold beskyttede jobbfiler, legg korrigert prompt og kildebegrunnelse i et separat notat, og bruk rettelsen. Avklar bare nødvendig manglende betydning eller design; eksisterende godkjenninger gjelder fortsatt. Fortsett uavhengig arbeid som allerede er autorisert.

Det som er avklart for Sam & Max før jobbene ble laget, står i `docs/ANALYSE.md` (avsnittet om klargjøringen), `docs/figurer.csv` (hvem og hva hvert kostyme er), `docs/gpt-romnotater.csv` (skilt, tekst og rariteter per rom) og `docs/kostymefarger.csv` (paletten kostymene vises med).

## 1. Hva vi bestiller

Vi lager en HD-versjon av LucasArts' *Sam & Max Hit the Road* (1993). Spillet kjører i ScummVM med en patch som legger HD-bilder nøyaktig oppå originalgrafikken, piksel for piksel. Vi trenger at du maler grafikken på nytt i 4x oppløsning (1280 x 800 for et rom på 320 x 200), **trofast mot originalen**: samme motiv, samme former på samme sted, samme farger og samme tegneserieuttrykk. Bare skarpere og med mer detalj.

Jobbene (laget med `smhd gpt-pakke --figurer alle` 13. oktober 2026):

| Hva | Jobber | Bilder i dem |
| --- | --- | --- |
| Hovedark (Sam og Max) | 2 | Referanse til alle figurarkene for dem |
| Rombakgrunner (`romNNN`) | 115 | 76 rom; de brede er delt i deler med overlapp |
| Store objektbilder (`objNNN_SS`) | 86 | Nærbilder, kart, store deler og bilder i rom uten bakgrunn |
| Lagjobber (`lagNNN_KK`) | 296 | 701 små objektbilder tegnet på plass i rommet |
| Ikonark (`ikonNN`) | 9 | 163 pekere, inventar- og samtaleikoner og små deler |
| Figurark (`figCCC_KK`) | 1758 | 15 661 kostymeruter fra 343 kostymer |

Hver jobb er ett bilde på 1536 x 1024 piksler. Ni objektbilder er helt gjennomsiktige og får ingen jobb. Fem kostymer er rene skyggeformer og får ingen figurark (se 4).

## 2. Hvem gjør hva

| Hvem | Ansvar |
| --- | --- |
| **ChatGPT** | Lager HD-bildene etter jobbene. Kjører egenkontrollen før levering. Gir råd om stil og sier fra når en jobb er uklar eller umulig. Skriver et kort notat per jobb. |
| **Claude** | All kode: lager jobbene, tar imot bildene, sjekker plassering, størrelse og farger, syr sammen deler, lager mod-mappen, tester i motoren og skriver rapport. |
| **Tom** | Godkjenner stilen og hovedarkene, flytter filer mellom dere hvis ChatGPT ikke jobber i repoet, og har siste ord. |

ChatGPT skal ikke endre kode, jobbfiler eller noe i grenen `main`.

## 3. Hva trofast betyr her

Motoren bruker HD-bildet bare der den vet at originalen viser uendret bakgrunn. Den sammenligner piksel for piksel. Figurer går foran og bak ting etter masker i originalens oppløsning, og klikkområder og gangflater ligger der de lå. Derfor:

1. **Ingenting flyttes.** Kanter, horisont, dører, møbler, skilt og lys skal ligge på nøyaktig samme sted. Ikke zoom, beskjær, roter, speil eller komponer om.
2. **Ingenting legges til, fjernes eller byttes ut.** Ingen nye gjenstander, figurer, tekst, skilt, symboler, mønstre, planter, rot eller detaljer. Like mange av alt: vinduer, stolper, bøker, flasker, stjerner, tenner og fingre.
3. **Ingenting rettes eller ryddes.** Det skjeve, rotete og rare er en del av spillet: kontoret skal være rotete, gavebutikken er opp ned, Escher-rommet har umulig perspektiv, VR-verdenen er flate polygoner. Skrå og buede linjer forblir skrå og buede. Flater som er tomme, er ofte tomme fordi spillet tegner objekter eller figurer der.
4. **Skilt, tekst og symboler kopieres bokstav for bokstav.** Samme ord, stavemåte, bokstavform, størrelse og plass. Mange er vitser eller gåteledetråder. Romnotatene siterer teksten der den kan leses sikkert; der en bokstav ikke kan leses, beholdes formen i stedet for å gjette et ord.
5. **Samme farger, lys og stemning.** Samme lysretning, skygger og kontrast. Ikke varmere, kaldere, mørkere eller lysere. Noen scener har egne farger med vilje (alkoven i rom 92 viser Sam i brun dress i varmt lys, rulletekstpanelene er psykedeliske eller grå); de beholdes.
6. **Samme stil.** Sam & Max sitt tegneserieuttrykk fra LucasArts i 1993: kraftige mørke omriss, mettede farger, malte skygger og overdrevet perspektiv. Ikke fotorealisme, ikke moderne 3D, ikke filmkorn, ikke vignett.
7. **Det som blir bedre:** jevne overganger i stedet for dithering og fargebånd, rene kanter og streker, og mer detalj der originalen antyder den.

Farger som animeres med fargesykling, viser motoren i HD gjennom et glatt fargekart (se [HD-MOTOR.md](HD-MOTOR.md)). Mal dem like nøye som resten. 43 av rommene har fargesykling.

## 4. Jobbene

Hver jobb ligger i `jobber/<jobb>/`:

| Fil | Innhold |
| --- | --- |
| `referanse.png` | Originalen forstørret 4x med harde pikselkanter, på en grå kant (#808080). 1536 x 1024. Dette er bildet du redigerer. |
| `original_1x.png` | Det samme utsnittet i originalstørrelse, til sammenligning. |
| `prompt.txt` | Teksten til bildeverktøyet, på engelsk. Brukes ordrett. Den kan ha et notat for rom med spesielle hensyn. |
| `jobb.json` | Metadata (rom, utsnitt, rektangler, bilde to, sjekksummer). Skal ikke endres. |
| `resultat.png` | **Det du leverer.** PNG, enten hele lerretet (1536 x 1024 med grå kant) eller bare bildet i samme sideforhold som utsnittet (16:10 for vanlige rom, minst 1280 x 800). Figurark leveres alltid som hele lerretet med ekte alfa. |
| `notat.md` | **Det du skriver:** verktøy og modell hvis det vises, dato, antall forsøk, og hva som var usikkert. |
| `retur.md` | Kommer fra Claude hvis jobben ble avvist eller må sjekkes, med grunn og forslag til ny prompt. |

Den grå kanten er bare fyll, slik at bildet får sideforholdet 3:2. Hold den grå. Rom som er bredere enn ett lerret, er delt i deler med overlapp (for eksempel `rom007_del1av2`). Delene sys sammen av Claude, så kantene skal være naturlige, uten ramme eller toning.

Oversikt over alle jobber: `JOBBER.md`. Status: `status.csv` (ny, godkjent, sjekk, avvist). Rekkefølgen: `GRAFIKKLISTE.md`. Kolonnen `type` sier om jobben er et rom (`rom`), et stort objektbilde (`objekt`), et lag (`lag`), et ikonark (`ikon`) eller et figurark (`figur`).

### Objektjobber

Noen ganger tegner spillet et stort bilde over bakgrunnen, for eksempel et nærbilde, et kart eller en del av et minispill. Slike store objektbilder er egne jobber. Grensen er minst 16 000 piksler i alt, eller minst 200 piksler bredt, eller minst 150 piksler høyt.

- Jobbene heter `objNNN_SS`: objekt-ID og tilstand som i filnavnet.
- `referanse.png` viser objektbildet lagt over rommet der spillet tegner det, på samme lerret og med samme grå kant som rommene. Der objektet er gjennomsiktig, synes rommet bak. Utenfor rommet er det svart. Noen rom er nesten tomme lagerrom for bilder spillet viser andre steder (rom 1, 67, 69, 78, 80, 81, 82, 93 og 94); der er bakgrunnen svart.
- Mal hele bildet som en bakgrunn. Bare objektets egne piksler brukes i spillet, de gjennomsiktige delene klippes ut igjen etterpå.
- Leveres som rommene. Leverer du bare bildet, skal det ha objektets sideforhold (`bilde_i_lerret` i `jobb.json`).

### Lagjobber (små objekter)

De andre objektbildene er små: dører, brytere, lys og ting. De males på plass i rommet, så de får samme stil og lys som HD-rommet, og klippes ut etterpå.

- Jobbene heter `lagNNN_KK`: rom NNN, lag KK. Brede rom har samme deler som romjobbene, for eksempel hører `lag007_01_del2av2` til `rom007_del2av2`. Deler uten objekter er ikke med.
- `referanse.png` er rommet med lagets objekter tegnet der spillet tegner dem. Lag 01 har første tilstand av hvert objekt, lag 02 neste og så videre. Objekter som ville ligget oppå hverandre, står i hvert sitt lag.
- Bilde to er det godkjente HD-bildet for samme del (`bilde_to` i `jobb.json`).
- Mal hele bildet trofast, også rommet rundt. Objektene klippes ut etter posisjon, så de må ligge nøyaktig der de er, med samme størrelse, omriss og farger. Ingen objekter skal mangle, flyte inn i rommet eller tegnes om.

### Ikonark

Pekerne (rom 93), inventaret og samtaleikonene (rom 94) og små deler som spillet tegner over skjermen (skilt og biler i Highway Surfing, landskapsbitene i kikkerten, ringen under forstørrelsesglasset og lignende) ligger tett i rader på ikonark, på en flat bakgrunnsfarge som ikke finnes i ikonene.

- Jobbene heter `ikonNN`. Tilstandene til et ikon (for eksempel vanlig og uthevet) står ved siden av hverandre. Et nytt rom begynner på ny rad.
- Mal hvert bilde trofast i ruten sin, med samme størrelse, omriss og bokstaver. Hold bakgrunnen flat, uten rammer, rutenett, skygger eller glød.
- Leveres som rommene, med stilankeret som bilde to.
- I tillegg kan hvert ikon leveres som eget RGBA-bilde med myk alfa, i 4x av originalen (lik marg på begge sider er lov), oppført i `rapporter/*/ikonmanifest.json` med `bilde`, `fil` og `sha256`. `smhd myke-ikoner` tar dem inn som `objNNN_SS_hd.png` når ikonarket er godtatt, og motoren bruker dem i inventaret og pekeren med den myke kanten. Uten egen fil brukes ikonet klippet ut av arket, med originalens kant.

### Figurark

Figurene er kostymer: animasjonsruter som spillet tegner etter hverandre. Rutene som hører sammen, står på figurark, så figuren blir lik i alle rutene.

- Jobbene heter `figCCC_KK`: kostyme CCC, ark KK.
- `referanse.png` er rutene i 4x på en flat bakgrunnsfarge som ikke finnes i kostymet, med 32 HD-piksler mellom rutene og samme grå kant som de andre jobbene. Ruter i samme animasjon og retning står etter hverandre på samme rad, i den rekkefølgen spillet viser dem. Prompten sier hva som står på arket og hvem det er (fra `docs/figurer.csv`).
- Kroppen og hodet er ofte egne deler i kostymet (i Sam & Max er kroppen lag 1, munn og hode lag 2 til 4). Delene males som de er, uten å gjøre dem hele.
- Ruter mot venstre finnes ikke på arkene når kostymet ikke har egne: spillet speilvender rutene mot høyre. Ikke tegn noen.
- Skyggepiksler (palettindeks 13, som spillet tegner gjennom skyggetabellen) er tatt bort fra arkene; motoren tegner skyggen selv. Fem kostymer (127, 132, 153, 211 og 280) er bare skygge og har ingen ark.
- Seks ruter i fire kostymer er feil i dataene (animasjoner som peker utenfor kostymet, og som dekoderen leser som ruter på opptil 6189 piksler). De er ikke med.
- Mal alle rutene som den samme figuren: samme ansikt, klær, farger og lys. Bare posen skal være forskjellig, nøyaktig som i originalen.
- Glatt stil med ekte alfa: arkene leveres på gjennomsiktig bakgrunn, med myke kanter, ikke klippet med originalens omriss (Tom avviste trappetrinnene i The Dig).
- Tegn figuren over originalen, så den ser ut som figurene i Day of the Tentacle Remastered ved siden av originalene: samme positur, silhuett og proporsjoner, hver pikselklynge tegnet som det den forestiller (briller, slips, sko), samme farge per flate, ren mørk kontur, flate farger med ett skyggetrinn og noen få høylys. Ingen nye detaljer, ingen tekstur og ingen dithering. Hodet blir ikke større.
- Bilde to: hovedarket for kostymer med Sam eller Max (kolonnen `hovedark` i `docs/figurer.csv`; for kostymer med begge er hovedarket til Max bilde tre). For de andre kostymene er bilde to stilankeret for ark 01 og det godkjente ark 01 for de andre arkene. Det står i `bilde_to` og `referanser` i `jobb.json`.
- Unntak: nærbildene i alkoven (kostyme 341 til 347) har varme farger med vilje og får ikke hovedarket som bilde to. Fargene tas fra referansen.
- Leverte ark føres under `leveranser` i `rapporter/*/fremdrift.json` med `jobb`, `resultat` (stien til PNG-en) og `sha256`. Hvert ark skal ha et rutekart (`rapporter/*/rutekart*.json`) som kobler hver rute (`bilde`) til boksen rundt delen av tegningen med alfa over 128, `[x, y, bredde, høyde]`.

### Hovedark

Før figurarkene for Sam og Max lages ett hovedark per person, slik Full Throttle hadde ett hovedark per figur som alle tegnerne fulgte. Referansen ligger i `hovedark/sam/` og `hovedark/max/`: originalfiguren forfra, fra høyre, bakfra og fra venstre, satt sammen av lagene slik spillet tegner dem, og et nærbilde av ansiktet. Leveransen er `hovedark/sam.png` og `hovedark/max.png` på gjennomsiktig bakgrunn, uten tekst, med notat i `hovedark/<navn>-notat.md`. Tom godkjenner hovedarkene før de brukes.

## 5. Fast størrelse i alle figurark

Dette er den viktigste regelen for figurene. En figur som er tegnet litt større i én rute enn i den neste, vokser og krymper i spillet. I The Dig så Tom astronautene skifte størrelse når de snakket, og hodene ble tegnet omtrent 35 prosent større enn kroppene.

- Hver rute tegnes nøyaktig så stor som den er i referansen: samme høyde, samme bredde og samme forhold mellom hode, kropp, armer, ben og gjenstander. En piksel i referansens originalstørrelse er fire piksler i resultatet, på alle arkene til samme figur.
- Prompten sier hvor store rutene på arket er, og `jobb.json` har boksen rundt hver rute (`synlig` under `ruter`, i originalpiksler).
- Hoder, hender og øyne gjøres ikke større. Ingen rute fylles ut eller strekkes for å se bedre ut.

Egenkontroll før levering, i grenen `gpt-arbeid`:

```sh
python3 verktoy/sjekk_leveranse.py jobber/fig002_01/resultat.png
```

Skriptet måler hver rute: bredde og høyde på det som er tegnet mot originalen ganger 4, hvor langt midten er flyttet, og hvor godt omrisset dekker originalen. Grensene: OK innen 6 prosent i størrelse og 1,5 originalpiksler i plassering, SJEKK opptil 12 prosent og 3 piksler, FEIL over det. Det sier også fra når rutene i samme animasjon er tegnet ulikt store (mer enn 5 prosent forskjell). Gjør om rutene som får FEIL. Skriptet sjekker også rom, objekter, lag, ikonark og hovedark med de samme grensene som mottaket.

Mottaket hos Claude (`smhd myke-figurer`) skalerer hver gruppe av ruter til originalens høyde og tilpasser hver rute høyst 12 prosent, men det kan ikke rette proporsjoner inne i en rute. Det merker ruter som er tegnet mer enn 12 prosent større eller mindre enn resten av gruppen, med status sjekk.

## 6. Rekkefølge

1. **Stilpilot (nå):** hovedark for Sam og Max, kontoret (`rom007_del1av2` og `rom007_del2av2`), og `fig002_01` (Sam) og `fig003_01` (Max) med hovedarkene som bilde to. Stopp etter piloten.
2. **Godkjenning:** Tom ser på piloten i motoren. De godkjente bildene legges i `stil/` som stilankere, og Claude skriver ny ordre.
3. **Løpende ordre:** Claude skriver `ORDRE.md` etter hver kontroll. Avviste rom- og objektjobber står først. Nye jobber står etter romnummer, med romjobbene før objektjobbene i samme rom. Så lagjobbene (først de der bilde to er godkjent), så ikonarkene, og til slutt figurarkene: Sam og Max først, så de andre kostymene med dem, så de navngitte figurene (Conroy Bumpus, Trixie, Bruno, Doug, Shuv-Oohl, Kushman-brødrene), så resten.
4. **Retur:** jobber med `retur.md` står først i ordren og gjøres på nytt med teksten der.

Det er ingen filmer i Sam & Max. Mellomsekvensene og minispillene tegnes av motoren og bruker rom, objekter og figurer fra spillfilene, så de dekkes av de samme jobbtypene.

## 7. Arbeidsflyt

### A. ChatGPT som Codex i repoet (anbefalt)

1. Åpne repoet `Tombonator3000/Sam-Max-HD` og bytt til grenen `gpt-arbeid`. Den har sin egen `AGENTS.md` og en kopi av denne bestillingen.
2. Les `ORDRE.md` og ta jobbene der. Lag ikke egne grener eller PR-er for grafikken.
3. For hver jobb: bruk bildeverktøyet med `referanse.png` som bildet som skal redigeres, bildene i `referanser` (eller stilankeret) som bilde to og tre, og `prompt.txt` ordrett som prompt. Be om 1536 x 1024. Lagre som `resultat.png` og skriv `notat.md`.
4. Kjør `python3 verktoy/sjekk_leveranse.py jobber/<jobb>/resultat.png` og se på resultatet ved siden av referansen. Ligger noe feil, prøv igjen.
5. Commit i grenen `gpt-arbeid` med jobbene i meldingen, for eksempel `GPT: rom007_del1av2, fig002_01`, og push. Aldri til `main`.

Claude henter grenen, kjører kontrollen og skriver `RAPPORT.md` og `retur.md` tilbake.

### B. Vanlig ChatGPT-chat (manuelt)

1. Lag et ChatGPT-prosjekt «Sam & Max HD» og lim inn teksten i punkt 11 som instruksjoner.
2. For hver jobb: last opp `referanse.png` (og bilde to), lim inn `prompt.txt`.
3. Last ned bildet og lagre det som `work/gpt/innboks/<jobb>.png`, for eksempel `rom007_del1av2.png`.
4. Kjør `smhd gpt-inn`. Bildene flyttes inn i riktig jobb og sjekkes.

## 8. Slik sjekkes leveransene

`smhd gpt-inn` gjør dette med hvert bilde:

| Sjekk | Hva den måler | Godkjent | Sjekk | Avvist |
| --- | --- | --- | --- | --- |
| Størrelse | Sideforhold 3:2 (lerret) eller samme som utsnittet (direkte) | ett av dem | | annet |
| Forskyvning | Hele bildet mot originalen, i originalpiksler | 0,75 eller mindre | 1,5 eller mindre | mer |
| Blokker | Forskyvning i deler av bildet (avslører zoom og flyttede ting) | 1,0 eller mindre | 2,0 eller mindre | mer |
| Kantlikhet | Om formene er de samme (0 til 1) | 0,55 eller mer | 0,40 eller mer | mindre |

Prøvd i The Dig med kunstige svar: et bilde forskjøvet 3 piksler ble avvist, 3 prosent zoom ble avvist, 1 prosent zoom havnet på sjekk, feil sideforhold ble avvist, og et omtegnet bilde som lå riktig, ble godkjent. Egenkontrollen her er prøvd med kunstige leveranser for Sam & Max (13. oktober): et rom forskjøvet 3 piksler gir FEIL, en riktig leveranse gir OK, og en figurrute tegnet 15 prosent for stor gir FEIL. Ikke prøvd med ekte ChatGPT-bilder for Sam & Max.

Etter sjekken **låses fargene til originalen**: de grove fargeflatene hentes fra originalen og detaljene fra ditt bilde. Et lite fargestikk gjør derfor ikke noe, men feil plassering gjør det.

Lagjobber og ikonark kontrolleres i tillegg objekt for objekt, bare på objektets synlige piksler:

| Sjekk per objekt | Avvist når |
| --- | --- |
| Mangler | Resultatet ligner mer på rommet uten objektet enn på objektet (kantlikhet mot bakgrunnen er over kantlikheten mot objektet pluss 0,05). Måles når objektet skiller seg fra bakgrunnen. |
| Tegnet om | Kantlikheten i objektet er under 0,50, for objekter med tydelige kanter. |

Ett feil objekt avviser hele jobben. Senere tilstander av et objekt gjøres like den første der originalene er like.

Figurark i glatt stil tas inn med `smhd myke-figurer` (`pipeline/smhd/myk.py`, versjon 4): rutekartet kobler delene av tegningen til rutene, hver gruppe skaleres til originalens høyde, hver rute tilpasses høyst 12 prosent, og ruter som er tegnet ulikt store, får status sjekk (se 5). Ruter der omrisset er svært ulikt originalen (dekker under 80 prosent, eller snitt delt på union under 0,6), får også status sjekk, med kontaktark i `forhandsvisning/myk_<jobb>.png`.

Ferdige rom havner i `work/gpt-ferdig/rooms/`, objektbilder i `work/gpt-ferdig/objects/` og figurruter i `work/gpt-ferdig/costumes/`. `smhd build-mod --egne work/gpt-ferdig` lager mod-modden. Teknisk status godkjent er ikke Toms visuelle godkjenning (se [HD-REMASTER-METODE.md](HD-REMASTER-METODE.md)).

## 9. Sporing

Hver leveranse skal kunne spores. Claude skriver `work/gpt-ferdig/provenance.json` med sjekksum for referanse, prompt og resultat, målingene og innstillingene for fargelåsen, og `myke.json` for figurarkene. Ditt `notat.md` utfyller med verktøy, modell, dato, antall forsøk og eventuelle endringer i prompten.

## 10. Erfaringer fra Jones, Moonstone og The Dig

**Jones in the Fast Lane** fikk HD-grafikk fra ChatGPT sitt innebygde bildeverktøy (via Codex): én presis prompt per bilde med lister over hva som skal bevares og hva som ikke skal gjøres virket. Verktøyet skrev feil tekst på et skilt og kuttet hår fordi figurene var plassert litt annerledes; begge ble rettet med en smal korrigeringsprompt. Stilen ble skiftet to ganger, derfor stilpilot og stilankere først. Bildeverktøyet tok høyst fem referansebilder om gangen og ga ikke alltid nøyaktig størrelse.

**Moonstone** fikk motoren for HD-grafikk, men ikke ferdig grafikk: HD-bildene navngis likt som utpakkede filer i 4x, liste over all grafikk med mål, bryter mellom HD og original, og automatisk kontroll av plasseringen.

**The Dig HD Remake** (skillen `scumm-hd-remake`): ChatGPT bommet på tekst og plassering, og stilen gled over tid. En dårligere ny leveranse skal ikke erstatte en godtatt. Den grå lerretskanten blødde inn i ytterradene. Codex laget egne jobber utenfor jobblisten. Figurene skiftet størrelse mellom rutene, og tre kvinner i romdrakt ble tegnet like fordi kostymene manglet navn. Derfor har Sam & Max navn og beskrivelse per kostyme, hovedark og egenkontroll av størrelsen fra starten.

## 11. Tekst til ChatGPT-prosjektet

Lim inn dette som instruksjoner i et ChatGPT-prosjekt (arbeidsflyt B), eller la Codex lese denne filen (arbeidsflyt A):

```text
Du er grafiker i et prosjekt som lager en trofast HD-versjon av Sam & Max Hit the Road (LucasArts, 1993).
Claude skriver all kode. Du lager bildene. Tom godkjenner.

For hver jobb får du referanse.png (originalen forstørret 4x med harde piksler på grå kant, 1536 x 1024)
og prompt.txt. Bruk prompt.txt ordrett og referanse.png som bildet som redigeres. Lever ett bilde på
1536 x 1024 med samme oppsett. Jobber som heter objNNN_SS, er store bilder spillet viser over rommet.
Behandle dem som bakgrunner. Jobber som heter lagNNN_KK, er rommet med små objekter tegnet på plass.
Mal alt trofast; objektene klippes ut etter posisjon, så de må ligge nøyaktig der de er. Bruk det
godkjente HD-bildet i bilde_to som bilde to. Jobber som heter ikonNN, er små bilder på flat bakgrunn.
Jobber som heter figCCC_KK, er figurark: animasjonsruter av samme figur. Mal alle rutene som samme figur
(samme ansikt, klær, farger og lys), i glatt stil med myke kanter på gjennomsiktig bakgrunn med ekte alfa.

Regler: ingenting flyttes, zoomes eller beskjæres. Ingenting legges til, fjernes eller byttes ut, og det
skal være like mange av alt. Ingenting rettes eller ryddes, heller ikke det som ser rart ut. Skilt, tekst
og symboler kopieres bokstav for bokstav. Samme farger, lys og stemning. Samme tegneserieuttrykk som
originalen, med kraftige omriss og mettede farger. Ikke fotorealisme, ikke moderne 3D. Den grå kanten
skal være grå. Bedre detalj, jevne overganger og rene kanter er målet.

Figurer: hver rute tegnes nøyaktig så stor som i referansen (en inndatapiksel er fire utdatapiksler),
med samme forhold mellom hode, kropp og armer. Hoder og hender gjøres ikke større. Deler av en figur
(hode og kropp hver for seg) males som de er. Rutene mot venstre lager spillet ved å speilvende.

Hvis et stilanker eller hovedark er vedlagt som bilde to, følg detaljnivået og designet i det, men ta
alle former, størrelser, posisjoner og farger fra referansen.

Kjør python3 verktoy/sjekk_leveranse.py på resultatet før du leverer, og gjør om det som får FEIL.
Si fra hvis noe ikke lar seg gjøre trofast. Skriv et kort notat: verktøy, dato, antall forsøk, hva som var usikkert.
```

## 12. Opphav

*Sam & Max Hit the Road* eies av Disney/Lucasfilm. Repoet er offentlig etter Toms valg, men jobbene, referansene og resultatene ligger bare i grenen `gpt-arbeid` og i `work/`. De legges ikke i `main`. Tom kan dele dem utenfor repoet til eget, privat bruk.

## 13. Videre arbeidsmetode

Se [HD-REMASTER-METODE.md](HD-REMASTER-METODE.md) for kontroll av figuridentitet, rutekart, hele animasjoner, objekttilstander og visuell godkjenning. Teknisk mottaksstatus er ikke i seg selv Toms visuelle godkjenning.
