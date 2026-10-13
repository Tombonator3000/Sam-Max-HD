# Bestilling 57, Sam 272: kilde og sluttkontroll

De seks arkene fig272_01 til fig272_06 er ferdige og frosset for mottak. Leveransen omfatter 79 ruter, bygget fra 45 ulike kildeutsnitt og 45 nye figurkomponenter. Kildeidentiske ruter gjenbruker samme nye komponent med hver rutes egne mål og relative feste. Alle seks faktiske jobber har OK fra uendret sjekk_leveranse.py. Dette er teknisk kontroll og visuell kildevurdering, ikke runtime eller ny individuell brukergodkjenning.

## Motivgrunnlag

Alle originalark, synlige ruter, rektangler, paletter og relative fester er undersøkt før produksjon. Se [kildeplan](a-kildeplan.md), [kildebevis](a-kildebevis.json), [familiebevis](a-familiebevis.json) og [komponentbevis](a-kildekomponenter.json). Ingen av disse 45 ulike utsnittene var eksakte Sam002-donorer.

Sam beholder brun pels, blågrå dress og hatt, hvit skjorte, skrått slips og bare brune poter. Originalens håndstillinger og avkutting prioriteres foran stilarkets posering.

* 01 og 02 viser puten med kremfarget stoff og grønne mønstre, deretter egne tomme håndstillinger. Scriptet knytter objekt 428 og animasjon 6 til hårvann og pute.
* 03 viser dinosaurens elfenbensfargede tann med én spiss og butt rot. Scriptet knytter objekt 571 til animasjon 7 og dinosaurtannen. Avviste forsøk med blå hette, knott eller en ekstra spiss er bevart, men ikke brukt som anker.
* 04 viser den Muir-formede kalebassen med lilla kropp og grønn stilk, delvis skjult av hånden. Scriptets objekt 548 og animasjon 8 knyttes til totem 3. LucasArts-hintbokens trykte side 35 skiller «Muir-shaped gourd» fra «Bumpus-shaped eggplant». Dermed er tidligere generell Conroy-tolkning korrigert. [Hintbok](https://www.mocagh.org/lucasfilm/sammax-hintbook.pdf). Sammenlikningen av ikon1037/1042 er støtte, ikke et bevist runtime-kart mellom ikon-ID og objekt-ID.
* 05 og 06 viser håndholdt vortex med orange/gul overdel, blå bunn og svart propp, egne oppløsningstilstander og tomme hender. Scriptet knytter objekt 272 til animasjon 9. Den øvre tomme hånden er brun, uten det nye gullredskapet fra et avvist forsøk.

Scriptgrunnlaget er konsept/2026-10-12/kildebevis/rom_054/obj_0515_verb.txt. Det er statisk primærkildeanalyse; animasjonstiming og faktisk spillkjøring er ikke testet.

## Nytegning og faktisk historikk

Innebygd imagegen ble brukt i 14 kall. Ni valgte gruppebilder dekker 45 unike figurer. Eksakt modellversjon eksponeres ikke av verktøyet. Originalpromptene er bevart ordrett, med separat kildepresisering og godkjent hovedark/sam.png som stilanker. [Bildekall](a-bildekall.json) viser alle råfiler, valgte og avviste forsøk, faktiske promptfiler og SHA. Feltet forsok=14 i manifestet gjelder hele familiens samlede kall, ikke 14 kall per ark.

En feil i klargjøringsløkken brukte siste gruppenavn i flere tidlige presiseringer. Dette er rettet og dokumentert i [promptrettingen](a-promptretting.md). De faktisk sendte tekstene ligger i a-kall01-faktisk-prompt.txt til a-kall14-faktisk-prompt.txt og [samlet historikk](a-sendte-promptstrenger.json). Senere rettede tekstfiler er ikke presentert som historiske kall. Tidlige puteutgaver som visuelt fulgte riktig kilde er beholdt; feil tann- og vortexutgaver er erstattet. Avviste kandidater ble ikke brukt som genereringsankre.

## Plassering og alfa

[Plasseringsoppskriften](a-plasser.py.txt) skalerer og plasserer hele nye komponenter. Kildekonturmasker, lokal warp og vektortracing er ikke brukt. Utklipp og alfaopprydding beregnes bare fra det nygenererte bildet. Kjernen er alfa minst 128. Rand med alfa minst 40 beholdes innenfor to piksler fra denne kjernen, med MaxFilter(5); øvrige piksler nulles. Premultiplisert RGBA og Lanczos brukes ved helskalering. Før- og etterdata finnes i [plasseringsbeviset](a-plasseringsbevis.json).

1993 og 1994 bruker største sammenhengende komponent fra ny alfa før opprydding, slik at nye, feilplasserte partikler ikke arves. Deres kildebestemte separate fargepunkter legges inn fra egne nye punktkomponenter. Dette er ikke en maske fra originalens silhuett.

1941 har en hovedfigur på 38 × 70 kildepiksler og et eget beige punkt ved lokal posisjon (122,20), kildeatlas (322,24). Hovedfiguren blir 152 × 280 HD-piksler; punktet er en separat ny 4 × 4-komponent ved HD (1352,128). Hovedfiguren er ikke strukket over den samlede 123-pikslers kildebredden.

1993 har tre egne punkter ved kildeatlas (214,196), (217,200) og (222,200), henholdsvis gull, blått og grått. 1994 har gull og blått ved (273,196) og (276,200). Alle seks forekomster er separat plassert fra nye fargekomponenter, med kildeplasseringen bevart. Rågenerering og kobling ligger i komponent- og plasseringsbeviset.

Leveransene er ekte RGBA med transparent atlasbakgrunn, også der referansen bruker magenta eller grått. Originalens relative fester er beholdt; lik bilderegion overstyrer ikke rel-metadata.

## Sluttkontroll og begrensninger

[Manifest](a-leveranser.json), [HD-rutekart](a-rutekart-hd.json) og a-fig272_01-kontroll.txt til a-fig272_06-kontroll.txt dokumenterer 17 + 7 + 13 + 20 + 19 + 3 = 79 kontrollerte ruter. De 24 beskyttede kildefilene er uendret mot [kildelåsen](a-kildehash.json).

Alle ti a-slutt-feltqa-ark og alle ti a-rel-slutt-ark er visuelt gjennomgått. Originalen vises forstørret med nærmeste nabo i feltkontrollen; relativvisningen bruker originalens feste og synlige forskyvning. [Samlet helark](a-slutt-helark.png) viser de seks ferdige atlasene. Pute, tannrot, synlige hånd- og rekvisittvarianter samt punktplassering er kontrollert samlet. Konturene er rundere og tydeligere enn pikseloriginalen, og mønstre og ansiktsmodellering har penselstilens tolkning. Leveransen påstås ikke piksel- eller bokstavidentisk med originalen.

Root har også meldt uavhengig kontroll av 79 ruter, byteidentisk rekonstruksjon fra de nye komponentene, seks punktforekomster, alle 14 prompt- og råhashpar og seks ferske checkere. Ingen spillimport, runtime, timingtest eller ny individuell brukerbedømmelse er utført av denne agenten.
