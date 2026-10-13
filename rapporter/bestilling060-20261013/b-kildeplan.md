# Kildeplan for fig196_01 til fig196_04

Kun analyse, ingen nye produksjonsbilder. B eier disse fire arkene; A sine 209-ark berøres ikke. Alle 52 ruter er gjennomgått på åtte originaldetaljsider, sammen med b-kontekst.png og de to komplette rel-sekvensarkene. De 16 beskyttede jobbfilene er låst og kontrollert uendret i b-kildehash.json. Kontekst og konkret ny donor er låst separat i b-konteksthash.json.

## Identitet og handling

Sam med blågrå dress og hatt, hvit skjorte, mørkeblått/svart slips, brun pels og bare føtter. Han løfter og strekker frem en arm mot høyre, går tilbake, fører hånden opp mot snuten, peker frem og senker hånden igjen. Hendene er tomme der de er synlige. Ingen rekvisitt kan leses i disse rutene og ingen skal legges til.

Det originale skriptregisteret oppgir rom_037/lokal_217.txt, actor 2, linje 23 og 43 som kostymekoblinger. Originalrommet er Escher-rommet med skjeve trapper, speil, piano og andre separate romobjekter. Disse objektene er ikke en del av figurarkene. Fullscriptets timing, dialog og presise handlingsutløser er ikke lest og bekreftes ikke her. Kilden støtter gestus, men ikke et mer spesifikt funksjonsnavn.

Cel 1924 viser en liten brun håndrest ved høyre grense. Cel 1925 og 1926-gruppen slutter ved den blå ermekanten, uten hånd. Denne avkuttingen er kildeegen og skal beholdes. Ikke tegn hånd, håndflate, rekvisitt eller bakgrunn utenfor grensen. Det samme gjelder den riktige åpne formen i ermet; ikke legg til en svart mansjettåpning som antyder amputasjon. I den andre sekvensen ligger en finger nær snuten i 1946-gruppen, armen peker skrått frem i 1953 til 1956, og hånden holdes nær haka i 1957-gruppen.

## Ark og geometri

| Ark | Ruter | Animasjon og motiv |
|---|---|---|
| 01 |1920 til 1934, 15 ruter| Animasjon 1: nøytral Sam, armløft og kildeavklippet utstrakt arm. |
| 02 |1935 til 1949, 15 ruter| Avslutter animasjon 1; animasjon 7 begynner ved 1942 og løfter hånden mot snuten. |
| 03 |1950 til 1970, 21 ruter| Fortsettelse av animasjon 7, hånd ved snute, fremoverpeking og senking. |
| 04 |1971, 1 rute| Tilbake til den nøytrale kildeidentiske stillingen 1920. |

Alle ruter ligger på lag 15 og retning 1 i jobbarkene. Ikke legg til venstrevendte ruter eller separate hoder. Kildecanvas er 352 × 240. Mål er 1536 × 1024, skala 4, offset 64,32 og motivfelt 1408 × 960. Eksakte synlig-bokser, nativebredde og rel finnes i b-felttabell.md og b-ruteregister.json. Synlig-bokser har endekoordinater. Alle move-delta er 0,0. Rel_x varierer fra−23 til−13 og rel_y mellom−70 og−68. Disse små variasjonene skal beholdes, ikke sentreres bort.

Paletten er rom 037, format 0x60, 16 farger, transparent indeks 255. Magenta i originalarkene er padding. RGB-palett og antall er lagret per rute. Kildealpha er brukt bare til analyse og visning; produksjonsalpha må komme fra ny art.

## Beviste gjentakelser og donor

52 ruter gir 20 unike originale RGBA-bilder. Følgende grupper er byte-identiske, inkludert dimensjonene:

* 1920 og 1971.
* 1926 til 1939, 14 ruter.
* 1942 og 1970.
* 1946 til 1952, 7 ruter.
* 1954 og 1955.
* 1957 til 1967, 11 ruter.

Alle øvrige motiver er egne varianter, også 1925 mot 1926, 1923 mot 1940 og 1921 mot 1941. Likhet i grov positur er ikke bevis for gjenbruk. b-familiebevis.json oppgir samtlige 20 grupper med originalhash i ruteregisteret.

1920 og 1971 matcher originalens synlige RGBA i fig114_01 cel 0 nøyaktig. Rel er−18,−70 i begge, altså delta 0,0. Kilde 114 har nativebredde 92 mot 40 i kostyme 196, men de ekstra 52 kolonnene gir ikke noe synlig motiv. Synlig donor er 160 × 280 HD og er vist i b-donor114-cel0-kontekst.png. Donorarkets SHA er f94a4774d7305d15f40b1d9079cb908be284318918c527a818878ffa36d9febb. Bruk eksakt utsnitt med jobbens synlig-koordinater, uten ny oppskalering eller kroppstillegg. Donorfila står urørt. Ingen 003/005-donor brukes.

## Foreslått produksjon etter rotgjennomgang

To ruter kan bruke den beviste 114-komponenten. De resterende 50 rutene trenger 19 unike nye motiver, der kildeidentiske gjentakelser kopieres fra samme nytegning. Sam-hovedark og den verifiserte 114-stillingen gir stil/identitet; hver 196-original bestemmer kropp, håndstilling, avkutting og palett. Ordrette prompter suppleres med kildepresisering om tomme hender og avklippet arm. Kontroller særlig 1924/1925/1926 som egne overgangsformer og de to ulike håndfeltene nær snuten. Bevar råforsøk, rutemapping, ekte RGBA og rel-kontaktark; kjør uendret checker på alle fire faktiske leveranser.

Ingen vesentlig uavklart rekvisitt krever et brukerspørsmål nå. Runtime og fullscriptbasert årsaksforklaring forblir ubekreftet. Ingen 196-generering er gjort i denne analyseleveransen.
