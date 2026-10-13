# 068-familien, samlet kilde- og kandidatkontroll

Tolv tilstander og 45 metadatafelt er tegnet og kontrollert. Fire har OK: lag068_02, 03, 08 og 11. Lag068_04 har SJEKK, blokkforskyvning 1,75. Disse fem er klare for rotens visuelle mottak. De sju andre er uttrykkelig holdt tilbake med teknisk FEIL, ikke ferdige leveranser. Manifestene ligger under bestilling045, 046 og 047 med kun egne jobber.

15 innebygde imagegen-kall er bevart, med ordrett jobbprompt og separat kildepresisering. Eksakt modellnavn er ikke eksponert. Alle 52 kildefiler er SHA-verifisert uendret. Det leverte rom068-HD er uendret, og resultatene beholder bakgrunnspiksler utenfor egne metadatarektangler. Ingen Git, motorendring, lokal warp, kildekonturmaske eller vektorrekonstruksjon er brukt.

## Faktisk motiv og rettinger

Alle tolv originalhelscener, nærfeltene, metadata og riktig HD-grunnrom er gjennomgått. 01 til 05 har fire separate veifragmenter, hvorav to i samme fjerne overlappende kildefelt. 06 til 10 har tre fragmenter. Det finnes bare én gul strek i hver tilstand. Retning, høyde og skjevhet er forskjellige mellom tilstandene; svart mellomrom er tilsiktet. Ingen sammenhengende ny veibane er tegnet. Ingen biler eller tall er lagt inn.

01 har Max bakfra med armene ut, rundt halefelt, lange ører og avskårne komponenter helt til høyre. 651/652 er samme synlige kildeunion, ikke to figurer. Det synlige høyrefeltet er bare åtte kildekolonner. 02 har eget mindre avskåret felt. Øvrige veitilstander har ingen Max. 01 beholder de to lave stolpeføttene med forskjellige lyssider.

11 har tre egne stolper. Første forsøk ga feil lik sidebelysning; andre forsøk retter venstre stolpe til mørk venstreside og lys høyreside. Midtre og høyre stolpe har lys venstreside. 12 har bare én middels stolpe med motsatt lysretning. Kildeplanens x208 for 12 er en tekstfeil: faktisk metadata er [192,72,24,80], og synlig originalbbox er [198,72,15,74]. Metadata ble brukt i sammensettingen. Et nytt 12-forsøk ga feltkorrelasjon 0,982, men beholdt teknisk FFT-FEIL.

Det andre 01-forsøket retter veienes overflatemodellering; bare veifeltene brukes derfra. Andre figurer/stolper kommer fra første forsøk. Formene er litt glattere og noen flater lysere enn originalens dither. Ny gul strek i en fjern01-silhuett ble oppdaget i nærkontroll og fjernet gjennom fargeforenkling og fylling av et innelukket hull i den NYE genererte komponenten. Originalen har ensfarget RGB19,19,19 her. Ingen originalkontur ble brukt som maske.

## Sammensetting og fargebehandling

`a-sammensetting.py.txt` er den faktiske, bevarte oppskriften. Generatorbildet helskaleres til 1536 ×1024. Nye veiflater trekkes ut gjennom blå/lilla fargekomponent eller gul stripe. Fjerne svarte komponenter trekkes ut fra det genererte bildet og får kildens ensfargede mørke tone. Begge overlappende metadatafelt bruker samme genererte bilde; ingen duplisering. Stolper trekkes ut fra NYE grå/lilla farger og mørke sky-sider. Den genererte horisontstripen rundt stolpene er fjernet uten å fjerne selve den mørke stolpesiden. Bakgrunnen er det eksisterende HD-rommet. Grå padding er eksakt RGB 128.

For 02/04 er en enkelt kildepalettbasert tonevariant valgt fordi overflaten er nærmere originalens mørke farger og geometrien består. Den genererte blå/lilla flatens blåkanal mellom 1.-99.percentil er lineært avbildet til den samme semantiske kildeflatens 1.-99.percentil; R/G settes 12 under B, som de dominerende kildefargene. Det er ingen koordinatbasert originalfargekopiering. Kriteriet er B>R+5 og B>G+5. Ingen posisjon eller kontur ble flyttet. Førbilder og øvrige ikke valgte toneprøver er bevart. Toneprøvene er ikke en alternativ kontrollterskel. Andre tilstander har sine opprinnelige valgte nye overflater.

## Kontroll og begrensninger

Uendret checker er faktisk kjørt på alle tolv resultatfiler. Alle 45 felt er målt eksplisitt; laveste kantkorrelasjon er omtrent 0,760 i de avskårne høyrefragmentene. Helscene-FEIL kan derfor ikke skjules som felt-OK. Samlet visuell kontroll finnes i a-fullsceneqa-1.png til 3.png og a-objektqa-1.png til 8.png. Ingen åpenbar fullføring av figurer eller endret antall veier er sett etter rettingene.

Min første hypotese om at den helt tomme venstre blokken i11/12 forklarte FEIL var feil. Den blokken har source-standardavvik under 0,001 og hoppes over av checker. Dette er tilbakevist i a-problemblokker.json; a-blokkdiagnose.json markerer nå om hver blokk faktisk teller. Uendret rom068 har OK (skift 0,07, blokk 0,06, kant 0,98). Ingen global bakgrunnsjustering er gjort.

De tellende problemblokkene inneholder en liten veikant eller stolpekant. a-problemblokker.png og.json viser original/grunnrom/lag, unike kilde-RGB og nytt min/maks. Grunnrommet har svak nesten-svart struktur, men det er ikke bevist at denne alene forklarer FFT-avviket. 01/05s problem ligger over den brede veiflaten. 06/07/09 har et lite veifragment i venstre blokk, 10 i høyre. 12 har en svært smal stolpefotstripe i høyre blokk. Disse sju holdes derfor tilbake, uten påstand om ferdig teknisk levering.

Runtime/import er ikke testet. Ingen ny individuell brukergodkjenning påstås. Rot eier mottak og publisering.
