# Bestilling til ChatGPT: trofast HD-grafikk for Sam & Max

Til: ChatGPT (bildegenerering, helst som Codex i dette repoet)
Fra: Tom, med Claude som står for koden
Dato: 10. oktober 2026

**Ikke aktiv.** Bestillingen gjelder ikke før stilpiloten (ett rom og ett figurark sett i motoren) er godkjent av Tom. Ikke lag grafikk etter den før det. Status nå:

- Det finnes ingen jobber. Uttrekket (`smhd extract`) er ikke portet til Sam & Max, og HD-motoren er ikke portet til SCUMM v6.
- Jobbformatet, kontrollene og mottaket er kopiert fra The Dig HD Remake og er ikke prøvd med Sam & Max.
- Promptene som `smhd gpt-pakke` skriver, er fortsatt The Dig sine og må skrives om før de første jobbene lages.

## Kildetro grafikk før produksjon

Les [remake-skillen i main](https://github.com/Tombonator3000/Sam-Max-HD/blob/main/docs/skills/scumm-hd-remake/SKILL.md), særlig «Før HD-produksjon: avklar motiv og design», før stilpilot og nytegning. Avklar motiv, funksjon, riktig palett, person/drakt og design fra originalen i spillkontekst. Bruk spillets egne godkjente stilankere og dokumenter grunnlaget i eksisterende analyse og jobbnotat. Kontroller samme identitet gjennom hele animasjonen og hode/kropp samlet i spillet; alfa og ruteantall beviser ikke riktig motiv.

Regelen gjelder også når jobbformatet ber om ordrett prompt. Ved påvist feil premiss: behold beskyttede jobbfiler, legg korrigert prompt og kildebegrunnelse i et separat notat, og bruk rettelsen. Avklar bare nødvendig manglende betydning eller design; eksisterende godkjenninger gjelder fortsatt. Fortsett uavhengig arbeid som allerede er autorisert.

## 1. Hva vi bestiller

Vi lager en HD-versjon av LucasArts' *Sam & Max Hit the Road* (1993). Spillet kjører i ScummVM med en patch som legger HD-bilder nøyaktig oppå originalgrafikken, piksel for piksel. Vi trenger at du maler grafikken på nytt i 4x oppløsning (1280 x 800 for et rom på 320 x 200), **trofast mot originalen**: samme motiv, samme former på samme sted, samme farger og samme tegneserieuttrykk. Bare skarpere og med mer detalj.

Det som skal males: rombakgrunner, store objektbilder, små objekter (dører, ting) i lagjobber, ikoner og figurark. Hvor mange av hver, er ikke talt ennå. Hver jobb er ett bilde på 1536 x 1024 piksler.

## 2. Hvem gjør hva

| Hvem | Ansvar |
| --- | --- |
| **ChatGPT** | Lager HD-bildene etter jobbene. Gir råd om stil og sier fra når en jobb er uklar eller umulig. Skriver et kort notat per jobb. |
| **Claude** | All kode: lager jobbene, tar imot bildene, sjekker plassering og farger, syr sammen deler, lager mod-mappen, tester i motoren og skriver rapport. |
| **Tom** | Godkjenner stilen, flytter filer mellom dere hvis ChatGPT ikke jobber i repoet, og har siste ord. |

ChatGPT skal ikke endre kode, jobbfiler eller noe i grenen `main`.

## 3. Hva trofast betyr her

Motoren bruker HD-bildet bare der den vet at originalen viser uendret bakgrunn. Den sammenligner piksel for piksel. Figurer går foran og bak ting etter masker i originalens oppløsning, og klikkområder og gangflater ligger der de lå. Derfor:

1. **Ingenting flyttes.** Kanter, horisont, dører, møbler, skilt og lys skal ligge på nøyaktig samme sted. Ikke zoom, beskjær, roter, speil eller komponer om.
2. **Ingenting legges til eller fjernes.** Ingen nye gjenstander, figurer, tekst, symboler eller detaljer som endrer hva man ser.
3. **Skilt, tekst og symboler kopieres nøyaktig.** Noen av dem er gåteledetråder eller vitser.
4. **Samme farger, lys og stemning.** Samme lysretning, skygger og kontrast. Ikke varmere, kaldere, mørkere eller lysere.
5. **Samme stil.** Sam & Max sitt tegneserieuttrykk fra LucasArts i 1993, med samme streker, former og farger som originalen. Ikke fotorealisme, ikke moderne 3D, ikke filmkorn, ikke vignett.
6. **Det som blir bedre:** jevne overganger i stedet for dithering og fargebånd, rene kanter og streker, og mer detalj der originalen antyder den.

Farger som animeres med fargesykling, viser motoren i HD gjennom et glatt fargekart (se [HD-MOTOR.md](HD-MOTOR.md)). Mal dem like nøye som resten. Hvilke rom i Sam & Max som sykler farger, er ikke målt.

## 4. Jobbene

Hver jobb ligger i `jobber/<jobb>/`:

| Fil | Innhold |
| --- | --- |
| `referanse.png` | Originalen forstørret 4x med harde pikselkanter, på en grå kant (#808080). 1536 x 1024. Dette er bildet du redigerer. |
| `original_1x.png` | Det samme utsnittet i originalstørrelse, til sammenligning. |
| `prompt.txt` | Teksten til bildeverktøyet, på engelsk. Brukes ordrett. Den kan ha et notat for rom med spesielle hensyn. |
| `jobb.json` | Metadata (rom, utsnitt, sjekksummer). Skal ikke endres. |
| `resultat.png` | **Det du leverer.** PNG, enten hele lerretet (1536 x 1024 med grå kant) eller bare bildet i samme sideforhold som utsnittet (16:10 for vanlige rom, minst 1280 x 800). |
| `notat.md` | **Det du skriver:** verktøy og modell hvis det vises, dato, antall forsøk, og hva som var usikkert. |
| `retur.md` | Kommer fra Claude hvis jobben ble avvist eller må sjekkes, med grunn og forslag til ny prompt. |

Den grå kanten er bare fyll, slik at bildet får sideforholdet 3:2. Hold den grå. Rom som er bredere eller høyere enn ett lerret, er delt i deler med overlapp (for eksempel `romNNN_del1av3`). Delene sys sammen av Claude, så kantene skal være naturlige, uten ramme eller toning.

Oversikt over alle jobber: `JOBBER.md`. Status: `status.csv` (ny, godkjent, sjekk, avvist). Kolonnen `type` sier om jobben er et rom (`rom`), et stort objektbilde (`objekt`), et lag (`lag`), et ikonark (`ikon`) eller et figurark (`figur`).

### Objektjobber

Noen ganger tegner spillet et stort bilde over bakgrunnen, for eksempel et nærbilde eller et kart. Slike store objektbilder er egne jobber. Grensen i pipelinen er minst 16 000 piksler i alt, eller minst 200 piksler bredt, eller minst 150 piksler høyt.

- Jobbene heter `objNNN_SS`: objekt-ID og tilstand som i filnavnet.
- `referanse.png` viser objektbildet lagt over rommet der spillet tegner det, på samme lerret og med samme grå kant som rommene. Der objektet er gjennomsiktig, synes rommet bak. Utenfor rommet er det svart.
- Mal hele bildet som en bakgrunn. Bare objektets egne piksler brukes i spillet, de gjennomsiktige delene klippes ut igjen etterpå.
- `prompt.txt` har en ekstra linje om at bildet er et stort bilde spillet viser over rommet.
- Leveres som rommene. Leverer du bare bildet, skal det ha objektets sideforhold (`bilde_i_lerret` i `jobb.json`).

### Lagjobber (små objekter)

De andre objektbildene er små: dører, brytere, lys og ting. De males på plass i rommet, så de får samme stil og lys som HD-rommet, og klippes ut etterpå.

- Jobbene heter `lagNNN_KK`: rom NNN, lag KK. Brede og høye rom har samme deler som romjobbene, for eksempel hører `lagNNN_01_del2av3` til `romNNN_del2av3`. Deler uten objekter er ikke med.
- `referanse.png` er rommet med lagets objekter tegnet der spillet tegner dem. Lag 01 har første tilstand av hvert objekt, lag 02 neste og så videre. Objekter som ville ligget oppå hverandre, står i hvert sitt lag.
- Ligger objektene på et stort objektbilde, er det store bildet med i referansen.
- Bilde to er det godkjente HD-bildet for samme del: `jobber/romNNN/resultat.png` eller `jobber/romNNN_delXavY/resultat.png`, eller objektjobben for det store bildet objektene ligger på. Det står i `bilde_to` i `jobb.json` og i ordren. Bruk det i stedet for stilankeret.
- Mal hele bildet trofast, også rommet rundt. Objektene klippes ut etter posisjon, så de må ligge nøyaktig der de er, med samme størrelse, omriss og farger. Ingen objekter skal mangle eller flyte inn i rommet.
- `jobb.json` lister objektene som klippes ut av akkurat denne jobben (`objekter`, med rektangel i originalpiksler).
- Leveres som rommene.

### Ikonark

Ikoner som ikke tegnes på plass i et rom (for eksempel tingene i inventaret), ligger i et rutenett på ikonark, på en flat bakgrunnsfarge. Hvilke bilder dette gjelder i Sam & Max, er ikke kartlagt.

- Jobbene heter `ikonNN`. Tilstandene til et ikon (for eksempel vanlig og uthevet) står ved siden av hverandre.
- Mal hvert ikon trofast i ruten sin. Hold bakgrunnen flat, uten rammer eller rutenett.
- Leveres som rommene, med stilankeret som bilde to.

### Figurark

Figurene er kostymer: animasjonsruter som spillet tegner etter hverandre. Males hver rute for seg, blir det for mange jobber, og figuren flimrer fordi hver rute blir litt ulik. Derfor står rutene som hører sammen, på figurark.

- Jobbene heter `figCCC_KK`: kostyme CCC, ark KK.
- `referanse.png` er rutene i 4x på en flat bakgrunnsfarge som ikke finnes i kostymet, med 32 HD-piksler mellom rutene og samme grå kant som de andre jobbene. Ruter i samme animasjon og retning står etter hverandre på samme rad, i den rekkefølgen spillet viser dem. Prompten sier hva som står på arket.
- Er figuren delt i deler i kostymet (for eksempel hode og kropp hver for seg), males delene som de er, uten å gjøre dem hele.
- Mal alle rutene som den samme figuren: samme ansikt, klær, farger og lys. Sam er hunden i dress og hatt, Max den hvite, kaninaktige figuren. Bare posen skal være forskjellig, nøyaktig som i originalen.
- Bilde to er stilankeret for ark 01. For de andre arkene er bilde to det godkjente ark 01 for samme kostyme (`bilde_to` i `jobb.json`). Lag dem etter at ark 01 er godkjent.
- Ruter som ikke får plass på et ark i 4x, skaleres ikke ned. De blir egne jobber, og er de bredere eller høyere enn lerretet, deles de som rommene.
- Leveres som rommene.

#### Glatt stil med ekte alfa

Figurene lages i glatt, detaljert stil med myke kanter fra starten. I The Dig avviste Tom figurer klippet med originalens omriss, fordi de fikk trappetrinn i 4x.

- Arkene tegnes på gjennomsiktig bakgrunn med ekte alfa, ikke på flat farge. Figurene kan være tegnet i litt annen størrelse og litt andre steder enn i referansen. De klippes ikke med originalens omriss.
- Leverte ark føres under `leveranser` i `rapporter/*/fremdrift.json` med `jobb`, `resultat` (stien til PNG-en) og `sha256`. Stemmer ikke sha256 med filen, tas arket ikke inn.
- Hvert ark skal ha et rutekart (`rapporter/*/rutekart*.json`). Det kobler hver rute (`bilde`) til boksen rundt delen av tegningen med alfa over 128, `[x, y, bredde, høyde]`, under `ny_diagnostisk_rekt_alfa128`, `drawn_bbox_alpha128`, `native_analyseboks_alfa128` eller `rect`. Uten rutekart kobles rutene etter rad og rekkefølge, og da må antall rader og deler per rad stemme med referansen.
- Claude tar arkene inn med `smhd myke-figurer`. Hver gruppe av ruter (samme animasjon og lag, samme rad på arket) skaleres til originalens høyde, og hver rute tilpasses originalens omriss i bredde og høyde for seg, høyst 12 prosent fra gruppens faktor. I The Dig ble hodene tegnet omtrent 35 prosent større enn kroppene, så hoder og kropper skaleres hver for seg.
- Ruter der omrisset er svært ulikt originalen (dekker under 80 prosent av originalens piksler, eller snitt delt på union under 0,6), får status sjekk i `myke.json` og kontaktark `forhandsvisning/myk_<jobb>.png`.

Kostymene skal stå i `docs/figurer.csv` i grenen `main`, med navn, antall ruter og antall ark, sortert etter hvor mye de vises. Filen har bare overskriftene nå. Hvilke kostymer som er Sam og Max, er ikke kartlagt.

## 5. Rekkefølge

1. **Stilpilot:** ett rom og ett figurark, sett i motoren. Tom godkjenner. Rommet og figuren er ikke valgt.
2. **Stilankere:** de godkjente pilotbildene legges i `stil/` i grenen `gpt-arbeid`. Legg ved det ankeret som passer best, som bilde nummer to i hver jobb (prompten forklarer hvordan). Det holder stilen lik fra rom til rom.
3. **Løpende ordre:** Claude skriver `ORDRE.md` i grenen etter hver kontroll, med de neste jobbene. Ta dem i den rekkefølgen. Avviste rom- og objektjobber står først. Nye jobber står etter romnummer, med romjobbene før objektjobbene i samme rom. Lagjobbene kommer etter rom- og objektjobbene, og først de der bilde to er godkjent. Så ikonarkene, og til slutt figurarkene utenfor piloten når de er bestilt.
4. **Retur:** jobber med `retur.md` står først i ordren og gjøres på nytt med teksten der.

Det er ingen filmer i Sam & Max. Mellomsekvensene og minispillene tegnes av motoren, så de bruker rom, objekter og figurer fra spillfilene og dekkes av de samme jobbtypene. Hvilke rom det gjelder, er ikke kartlagt.

## 6. Arbeidsflyt

### A. ChatGPT som Codex i repoet (anbefalt)

1. Åpne repoet `Tombonator3000/Sam-Max-HD` og bytt til grenen `gpt-arbeid`. Den har sin egen `AGENTS.md` og en kopi av denne bestillingen.
2. Les `ORDRE.md` og ta jobbene der. Lag ikke egne grener eller PR-er for grafikken.
3. For hver jobb: bruk bildeverktøyet med `referanse.png` som bildet som skal redigeres, et stilanker som bilde to (for lagjobber det godkjente HD-bildet i `bilde_to`), og `prompt.txt` ordrett som prompt. Be om 1536 x 1024. Lagre som `resultat.png` og skriv `notat.md`.
4. Se på resultatet ved siden av referansen før du leverer. Ligger noe feil, prøv igjen.
5. Commit i grenen `gpt-arbeid` med jobbene i meldingen, for eksempel `GPT: romNNN, objNNN_SS`, og push. Aldri til `main`.

Claude henter grenen, kjører kontrollen og skriver `RAPPORT.md` og `retur.md` tilbake.

### B. Vanlig ChatGPT-chat (manuelt)

1. Lag et ChatGPT-prosjekt «Sam & Max HD» og lim inn teksten i punkt 10 som instruksjoner.
2. For hver jobb: last opp `referanse.png` (og stilankeret), lim inn `prompt.txt`.
3. Last ned bildet og lagre det som `work/gpt/innboks/<jobb>.png`, for eksempel `romNNN.png`.
4. Kjør `smhd gpt-inn`. Bildene flyttes inn i riktig jobb og sjekkes.

## 7. Slik sjekkes leveransene

`smhd gpt-inn` gjør dette med hvert bilde:

| Sjekk | Hva den måler | Godkjent | Sjekk | Avvist |
| --- | --- | --- | --- | --- |
| Størrelse | Sideforhold 3:2 (lerret) eller samme som utsnittet (direkte) | ett av dem | | annet |
| Forskyvning | Hele bildet mot originalen, i originalpiksler | 0,75 eller mindre | 1,5 eller mindre | mer |
| Blokker | Forskyvning i deler av bildet (avslører zoom og flyttede ting) | 1,0 eller mindre | 2,0 eller mindre | mer |
| Kantlikhet | Om formene er de samme (0 til 1) | 0,55 eller mer | 0,40 eller mer | mindre |

Prøvd i The Dig med kunstige svar: et bilde forskjøvet 3 piksler ble avvist, 3 prosent zoom ble avvist, 1 prosent zoom havnet på sjekk, feil sideforhold ble avvist, og et omtegnet bilde som lå riktig, ble godkjent. Ikke prøvd med Sam & Max.

Etter sjekken **låses fargene til originalen**: de grove fargeflatene hentes fra originalen og detaljene fra ditt bilde. Et lite fargestikk gjør derfor ikke noe, men feil plassering gjør det. Grensene justeres når vi har sett ekte resultater.

Objektjobber kontrolleres på samme måte mot sitt eget `original_1x.png` (objektbildet over rommet i 1x).

Lagjobber og ikonark kontrolleres som helhet på samme måte, og i tillegg hvert objekt for seg, bare på objektets synlige piksler:

| Sjekk per objekt | Avvist når |
| --- | --- |
| Mangler | Resultatet ligner mer på rommet uten objektet enn på objektet (kantlikhet mot bakgrunnen er over kantlikheten mot objektet pluss 0,05). Måles når objektet skiller seg fra bakgrunnen (kantlikhet under 0,90 mellom dem). |
| Tegnet om | Kantlikheten i objektet er under 0,50, for objekter med tydelige kanter. |

Ett feil objekt avviser hele jobben.

Figurark kontrolleres som helhet på samme måte (plassering), og i tillegg hver rute for seg og flimmer mellom rutene:

| Sjekk per figurark | Avvist når |
| --- | --- |
| Mangler | Under halvparten av rutens piksler er malt som figur |
| Omriss | Overlappen mellom det som er malt som figur og originalens omriss (snitt delt på union, i 4x) er under 0,80 |
| Tegnet om | Kantlikheten inne i omrisset er under 0,50, for ruter med tydelige kanter |
| Flimmer | To nabo-ruter i samme animasjon og retning skiller seg mye mer fra hverandre i HD enn i originalen. Rutene legges over hverandre der originalene passer best, og forskjellen måles i 1x etter fargelåsen, der begge har figur, jevnet ut over 3 x 3 piksler. Avvist når HD skiller seg mer enn 30 (0 til 255) mer enn originalen noe sted |

Ark i glatt stil med ekte alfa går gjennom `smhd myke-figurer` i tillegg (punkt 4).

Etter fargelåsen klippes hvert objekt ut av delen det står i (sydd sammen hvis det står i flere) på rektangelet sitt, i 4x med gjennomsiktigheten fra originalen. Figurruter klippes ut på samme måte til `costumes/costumeCCC_NNN.png`. Myke kanter i arket blander inn bakgrunnsfargen langs omrisset. Der en HD-piksel innenfor omrisset (høyst 2 originalpiksler fra kanten) er dratt mer enn 12 prosent av veien fra originalfargen mot bakgrunnsfargen, fylles den innenfra, ellers får figuren en glorie i bakgrunnsfargen. Et objekt er ferdig når alle delene det står i, er godtatt (godkjent, eller sjekk som for rommene; med `--bare-godkjente` bare godkjent). Senere tilstander av et objekt gjøres like den første der originalene er like.

Ferdige rom havner i `work/gpt-ferdig/rooms/`, ferdige objektbilder i `work/gpt-ferdig/objects/` og ferdige figurruter i `work/gpt-ferdig/costumes/`. `smhd build-mod --egne work/gpt-ferdig` lager mod-mappen motoren bruker, og bruker de godkjente bildene i stedet for automatisk oppskalering. Ruter uten HD-bilde vises som originalen, med mindre kostymet er valgt med `--kostymer`; da skaleres resten automatisk. Et rom regnes som ferdig når romjobbene er godkjent, uavhengig av objektene.

## 8. Sporing

Hver leveranse skal kunne spores. Claude skriver `work/gpt-ferdig/provenance.json` med sjekksum for referanse, prompt og resultat, målingene og innstillingene for fargelåsen. Objektbilder fra lag og ikonark får hver sin oppføring med laget eller arket de kom fra og rektangelet i det. Figurruter får én oppføring per rute med arket, rektangelet, animasjonen og målingene for ruten og nabo-rutene. Ditt `notat.md` utfyller med verktøy, modell, dato, antall forsøk og eventuelle endringer i prompten.

## 9. Erfaringer fra Jones, Moonstone og The Dig

**Jones in the Fast Lane** fikk HD-grafikk fra ChatGPT sitt innebygde bildeverktøy (via Codex):

- Det som virket: én presis prompt per bilde med lister over hva som skal bevares og hva som ikke skal gjøres, referansebildet som bildet som redigeres, og atlas for flere animasjonsrammer i ett bilde.
- Det som gikk galt og måtte rettes: verktøyet skrev feil tekst på et skilt, og hår ble kuttet fordi figurene var plassert litt annerledes. Begge ble rettet med en ny, smal korrigeringsprompt.
- Stilen ble skiftet to ganger. Derfor starter vi med pilot og stilankere før resten.
- Sporingen (prompt, referanse og sjekksum for hvert bilde) og automatisk kontroll av størrelser og plassering gjorde det mulig å holde orden.
- Bildeverktøyet tok høyst fem referansebilder om gangen og ga ikke alltid nøyaktig størrelse. Derfor tåler `gpt-inn` andre størrelser med samme sideforhold.

**Moonstone** fikk motoren for HD-grafikk, men ikke ferdig grafikk:

- HD-bildene navngis likt som utpakkede filer, i 4x størrelse.
- Liste over all grafikk med mål og HD-navn (her `docs/rom-oversikt.csv` og `JOBBER.md`).
- Bryter mellom HD og original, og gult felt der HD mangler.
- Plasseringen sjekkes automatisk. Her gjør `gpt-inn` det før bildet slipper inn, og `engine/test.sh` i motoren etterpå.
- HD-bildene må tones med paletten når spillet fader. Motoren fra The Dig gjør det.

**The Dig HD Remake** (fra skillen `scumm-hd-remake`):

- ChatGPT bommet på tekst og plassering, og stilen gled over tid. Den automatiske kontrollen og stilankerne fanget det meste.
- En dårligere ny leveranse skal ikke erstatte en godtatt. Mottaket tar vare på den beste per jobb.
- Den grå lerretskanten blødde inn i ytterradene på noen bilder. Hold kanten grå og bildet innenfor.
- Små objekter ble malt på plass i rommet (lagjobber) og klippet ut. Ikoner ble malt i ikonark.
- Codex laget egne jobber utenfor jobblisten. Mottaket leser derfor leveransene i `rapporter/*/fremdrift.json` og rutekartene, ikke bare `status.csv`.

## 10. Tekst til ChatGPT-prosjektet

Lim inn dette som instruksjoner i et ChatGPT-prosjekt (arbeidsflyt B), eller la Codex lese denne filen (arbeidsflyt A):

```text
Du er grafiker i et prosjekt som lager en trofast HD-versjon av Sam & Max Hit the Road (LucasArts, 1993).
Claude skriver all kode. Du lager bildene. Tom godkjenner.

For hver jobb får du referanse.png (originalen forstørret 4x med harde piksler på grå kant, 1536 x 1024)
og prompt.txt. Bruk prompt.txt ordrett og referanse.png som bildet som redigeres. Lever ett bilde på
1536 x 1024 med samme oppsett. Jobber som heter objNNN_SS, er store bilder spillet viser over rommet.
Behandle dem som bakgrunner. Jobber som heter lagNNN_KK, er rommet med små objekter tegnet på plass.
Mal alt trofast; objektene klippes ut etter posisjon, så de må ligge nøyaktig der de er. Bruk det
godkjente HD-bildet i bilde_to som bilde to. Jobber som heter ikonNN, er ikoner på flat bakgrunn.
Jobber som heter figCCC_KK, er figurark: animasjonsruter av samme figur. Mal alle rutene som samme figur
(samme ansikt, klær, farger og lys), med samme pose og plass som originalen, i glatt stil med myke kanter
på gjennomsiktig bakgrunn med ekte alfa. Deler av en figur (for eksempel hode og kropp hver for seg)
males som de er.

Regler: ingenting flyttes, zoomes eller beskjæres. Ingenting legges til eller fjernes. Skilt, tekst og
symboler kopieres nøyaktig. Samme farger, lys og stemning. Samme tegneserieuttrykk som originalen, med
samme streker, former og farger. Ikke fotorealisme, ikke moderne 3D. Den grå kanten skal være grå.
Bedre detalj, jevne overganger og rene kanter er målet.

Hvis et stilanker er vedlagt som bilde to, følg detaljnivået og strekene i det, men ta alt
innhold fra referansen.

Se på resultatet ved siden av referansen før du leverer. Si fra hvis noe ikke lar seg gjøre trofast.
Skriv et kort notat: verktøy, dato, antall forsøk, hva som var usikkert.
```

## 11. Opphav

*Sam & Max Hit the Road* eies av Disney/Lucasfilm. Repoet er offentlig etter Toms valg, men jobbene, referansene og resultatene ligger bare i grenen `gpt-arbeid` og i `work/`. De skal ikke deles utenfor repoet eller legges i `main`.

## 12. Videre arbeidsmetode

Se [HD-REMASTER-METODE.md](HD-REMASTER-METODE.md) for kontroll av figuridentitet, rutekart, hele animasjoner, objekttilstander og visuell godkjenning. Teknisk mottaksstatus er ikke i seg selv Toms visuelle godkjenning. Kontrollnivåene i metoden er forslag inntil verktøy og rapporter støtter dem.
