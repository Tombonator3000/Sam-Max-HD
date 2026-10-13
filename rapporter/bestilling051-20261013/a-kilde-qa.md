# Leveranse-QA for ikon01 til ikon06

Seks ark med 46 faktiske metadatafelt er produsert. Ikon01 og ikon02 har SJEKK, ikon03 til ikon06 har OK. Ingen FEIL gjenstår i disse seks kandidatene. 51/a-leveranser.json har fem resultater, 52/a-leveranser.json har ikon06. Ti innebygde genereringer er bevart med eksakte prompter, referansehash og råhash i a-ikon-proveniens.json. Eksakt modellnavn er ikke eksponert.

Kildeanalyse, alle felter og avklaringer finnes i a-kildeplan-ikoner.md og a-ikon-motivregister.md. 36 av 36 beskyttede ikonfiler er kontrollert uendret. Ikon07 til ikon09 er ikke produsert. Figurark og andres leveranser er ikke berørt.

## Kontrollert motiv og sammensetting

Logoidentitet, de tre forskjellige bakfra-vinklene av politibilen, dinosaurens kildeavskårne snute/kjeve og alle seks store grønne skilt er sett mot original. Dinosaurens to første forsøk hadde nytt øye og tenner og ble ikke valgt for feltet. Isolert tredje forsøk har de brede grå/teal formene uten nye ansiktsdeler. Den lille blågrå bakgrunnsflekken øverst til venstre er svakere enn i originalen; detaljlikhet er ikke pikselidentitet.

Skilt02s første forsøk hadde nye tykke rammer, andre forsøk hadde rundere og større bokstaver. Tredje forsøk har originalnære kantede glyfer og bare kildens tynne toppkant. All stor lesbar tekst er kontrollert, inkludert Placeholder Name Joke. De bittesmå skjoldglyfene er stiliserte og ikke bekreftet bokstavidentiske. 677, 679 og 681 er helt magenta i resultatene. Ingenting er tegnet inn i de tomme rutene.

Landskapsarkene har hvert enkelt kildeutsnitt, ingen konstruert felles panorama eller generisk kopiert skogstripe. Stubbe, regnsky, røde/grønne argyletrær, dekkhaug med flamme/røyk og hvite lysgrupper over elven er bevart. Trær, skyer og lysgrupper er sammenlignet som former/plasseringer. Penseldetaljer, høylys og overganger er nye, og noen flater er mer mettede og modellerte enn den ditherede kilden. Ingen runtime-rekkefølge er påstått.

Etter rotens gjennomgang ble en konkret hvit bunnstripe i 680 rettet til kildens lysegrønne tone. Bare de NYE pikslene i [304,275,76,5] ble fargebehandlet; pil, toppstripe og resten er byteidentiske. Førbilde og formel er i a-680-bunnstripe-bevis.json og a-680-bunnstripe-for-etter.png. 380 piksler ble endret. Egenkontroll er fortsatt OK.

Presis plassering bruker bare hele rektangulære komponentbokser, ikke originalkonturer. Ny bakgrunnsmagenta gjenkjennes med R>200, B>200, G<80 og settes til RGB255,0,255. Tegningene skaleres og plasseres etter de målte kildeboksene med ordinær Lanczos-skalering. Ingen originalpikseloppskalering, silhuettmasker, vektortegning eller lokal geometriwarp. Padding er eksakt RGB128 og leveransene opake RGB1536 × 1024. Oppskrift og faktisk perkomponentboks ligger i a-ikon-sammensetting.py.txt og a-ikon-forelopig-kontroll.json.

## Teknisk resultat

| Jobb | Status | Globalt skift | Blokkskift | Kantlikhet |
|---|---|---:|---:|---:|
| ikon01 | SJEKK | 0.15 | 1.42 | 0.965 |
| ikon02 | SJEKK | 0.35 | 1.65 | 0.954 |
| ikon03 | OK | 0.02 | 0.15 | 0.989 |
| ikon04 | OK | 0.06 | 0.11 | 0.971 |
| ikon05 | OK | 0.01 | 0.06 | 0.982 |
| ikon06 | OK | 0.11 | 0.17 | 0.964 |

Alle 46 felter er registrert og målt. Uendret checker kan hoppe over tomme/nesten kantløse felt; tomtilstandene er derfor også direkte pikselkontrollert. Fullscene- og nærbildeark a-ikonNN-helsideqa.png og a-ikonNN-feltqa-N.png viser de faktiske siste kandidatene. Kontroll er teknisk egenkontroll og visuell vurdering, ikke individuell brukergodkjenning, motorimport eller runtime. To SJEKK skal beholdes som SJEKK i mottaket.
