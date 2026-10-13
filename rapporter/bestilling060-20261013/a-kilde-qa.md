# Bestilling 60 A: ferdig figurleveranse

fig209_01 til fig209_05 er levert som ekte RGBA 1536 × 1024. Familien har 36 ruter og 22 forskjellige kildekomposisjoner. Alle fem faktiske jobbfiler gir OK fra uendret sjekk_leveranse.py. [Manifest](a-leveranser.json) har faktiske SHA, kontrollfiler og ruteantall. Ingen runtime, ny individuell brukergodkjenning eller Git-handling er utført av denne agenten.

## Kilde, identitet og tilstand

[Kildeplanen](a-kildeplan.md) og [kildebeviset](a-kildebevis.json) dokumenterer Sam og Max i glassapparatet fra rom040. Opp ned-retningen, Sam-dressen, den varme Max-paletten og blå/lilla glassoverlegg er bevarte motivdeler. Magenta og grå atlaspadding er transparent, mens glassfargene fortsatt er malt inn som motiv. Rom040s original og inngangsskript underbygger romkonteksten. Eksakt handling og timing er ikke runtime-testet.

En konkret feil ble oppdaget ved nærlesing: 1936 til 1942 er Max bakfra. Føttene er øverst, rund hale sitter på den lille kroppen, det store lyse feltet er bakhodet, og de nedhengende formene er ører. Første nye gruppe gav uriktig ansikt. Den ble avvist. Andre gruppeforsøk korrigerte de fem første posene, men 1942 fikk fortsatt ansikt. Denne kompositten ble nytegnet separat fra originalen med synlige såler, hale og bakhode. Ingen av de avviste forsøkene var referanse for nygenerering. 1943 og senere har kildens synlige ansikt.

De 12 kildeidentiske gruppene deler samme nye komponent. Hele ark02 er kildeidentiske motbilder fra ark01 i omvendt rekkefølge. De øvrige duplikatene er dokumentert i [familiebeviset](a-familiebevis.json) og [koblingen](a-unik-kobling.json). Egne rel-verdier og synlig/rekt behandles separat. Alle 20 beskyttede jobbkilder er uendret.

## Fremstilling og etterbehandling

Syv innebygde imagegen-kall er brukt. Eksakt modellnavn er ikke eksponert. [Kallhistorikken](a-bildekall.json) har alle råbilder, faktisk sendt prompt, SHA, valgte deler og avvisning. Forsok=7 i manifestet er familiens totale antall kall. Originalpromptene er bevart ordrett og kildepresiseringene separat; faktiske tekststrenger finnes også i a-sendte-promptstrenger.json og a-sendte-rettingsprompter.json. Kall 6 leverer fem valgte figurcels og punktet; den sjette cellen erstattes av kall 7.

[Plasseringsoppskriften](a-plasser.py.txt) skalerer hele nye kompositter til kildebestemte mål. Alfarensing bruker bare NY generert alfa: kjerne alfa minst 128, rand alfa minst 40 innen to piksler fra kjernen, MaxFilter(5). Andre piksler nulles. Premultiplisert RGBA og Lanczos brukes ved helskalering. Ingen originalsilhuettmasker, koordinatstyrte kildefargekart, lokal warp eller vektortracing er brukt. Målinger og råutklipp finnes i [plasseringsbeviset](a-plasseringsbevis.json).

Cel1941 er et eksplisitt unntak fra samlet boksstrekking. Ny hovedkompositt skaleres til 276 × 448 HD-piksler og forskyves 36 HD-piksler fra venstre synligkant. Det nye isolerte lyseblå punktet tas fra generatorens egen separate flekk, råboks [592,772,642,820], og helskaleres til 4 × 4 ved HD(388,776). Det tilsvarer kildeatlas (81,186). Ingen originalpiksler eller originalkontur er brukt til dette. [Kildekomponentene](a-kildekomponenter.json) viser målebeviset. Nedre grå utstikkere inngår i de nye komposittene.

## Kontroll og konkrete begrensninger

Alle fem a-slutt-feltqa-ark, alle fem a-rel-slutt-ark og [samlet helark](a-slutt-helark.png) er gjennomgått. Kildebildene vises med nearest-forstørring, rel-arkene med samme kildefeste og forskyvning som ny art. Opp ned-orientering, egne hender/føtter, Max bakfra/forfra, små tilstandsendringer og glassoverlegg er sammenliknet. 1952 og 1954 har samme kildeegne delvise glassdekning, 1953 egen bredere dekning, 1955 tilbake til åpnere felt.

Den nye streken er glattere og mer avrundet. Apparatets små nedre utstikkere er mer modellerte, og refleksfelt og detaljkonturer varierer noe mellom de nye komposittene. Dette er ikke påstått byteidentisk fast apparatkontur eller pikselkopi av originalen. Hovedmotiv, relativ plassering og kildeegne tilstander er kontrollert, men animasjon i spillet og faktisk motorimport gjenstår hos mottaker.

Endelige kontrollfiler er a-fig209_01-kontroll.txt til a-fig209_05-kontroll.txt. [Rutekartet](a-rutekart-hd.json) kobler alle 36 cels med native metadata til faktisk HD-boks. Klonekontroller var forarbeid; de endelige loggene gjelder jobbmappene. Root gjør separat mottak og Git-levering.
