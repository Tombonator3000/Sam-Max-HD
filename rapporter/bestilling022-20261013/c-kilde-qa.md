# Bestilling 22 C – kilde- og tilstandskontroll

Tre leveranser: lag007_01 del 1 og 2, lag007_02 del 1. Fremtidig lag007_02 del 2 ligger bare i rapportens kontrollmappe. To separate fullmastere er låst i c-masterlas.json. Hver er 1952 × 800; klipp x 0 og 416 har byteidentisk 1120 × 800 overlapp. Alle leveranser er RGB 1536 × 1024 med motiv y 112..912 og eksakt padding 128. 44 låste kildefiler er kontrollert uendret i c-kildehashkontroll.json.

## Kilde og kontrakt

Originaler, metadata, fullkomposisjoner og godkjente rom007-HD-deler er lest visuelt. Dette er RGB-romkompositter; assign_parts bestemmer metadatafordeling, ikke hvilke kildeobjekter som faktisk vises i overlapp. Originaldelene har identisk overlapp. Det nye HD-romankeret ble satt sammen uten søm, men nygenererte lagbakgrunner er ikke byteidentiske med ankeret eller med hverandre.

Lag 01: åpen svart dør med nedre rekkverk; liten grå knapp over LOVE; gulvrester uten sandwich; TV-tilstand 071_01; dukke som ser mot bildehøyre; dartskive uten piler; papirer på skrivebordet; delvis åpnet venstre vindu. Lag 02: telefonbase uten rødt håndsett; TV-tilstand 071_02; større uhindret blå vindusåpning; to grønne glimt i skallens øyehuler. Lag 02 beholder lukket dør, piler, sandwich, lilla kule og skrivebord uten den hvite papirbunken. Ingen tilstand er utledet bare fra generiske navn.

## De små tilstandsendringene

Se c-smatilstander-kilde-hd-anker.png: samme eksakte utsnitt vises fra originalrom, begge kildelag, godkjent HD-rom og begge nye HD-lag. c-smatilstander-kildedelta.json oppgir endrede originalkoordinater. Dette er visuell tilstandsverifikasjon i tillegg til korrelasjon, ikke en slutning fra høy rektangelkorrelasjon.

- Dukke 074_01: fire kildepiksler flytter mørke/lyse par ved x 412/413 og 417/418, y 41. Begge pupiller ser mot bildehøyre i HD-lag 01. Lag 02 og romankeret beholder motsatt blikk. Første generering beholdt feil blikk og er derfor lokalt korrigert. Øynene er rundere/åpnere enn lavoppløsningskilden, i tråd med det eksisterende HD-ankeret; ingen påstand om identisk ansiktsgeometri.
- TV 071_01 → 071_02: tre kildepiksler endres; det røde merket ved den venstre figurens nedre ansikt blir hudfarget, og to piksler blir blå. I valgt HD 02 er det lille røde munnmerket fjernet og blå hake-/kragekant utvidet. HD 01 beholder merket. Den sammenhengende mørke horisontale formen i venstre ansikt beholdes. De to figurformenes navn og handling kan ikke fastslås fra dette utsnittet. TV-formene er renere og enkelte mørke former større enn kilden; de er ikke en pikselidentisk rekonstruksjon.
- Skalle 075_01: tre kildepiksler gir to grønne markeringer i øyehulene. Begge er synlige i HD-lag 02, mens HD-lag 01 og romankeret har svarte øyehuler. De nye punktene har litt lysende kant og større tonebredde enn originalens flate grønne piksler. Dette er et konkret kvalitetsforbehold, ikke en ny figuridentitet.

## Arbeidsform og proveniens

Innebygd ChatGPT imagegen. Eksakt modellversjon er ikke eksponert. Originalpromptene er gjengitt ordrett før separat kilde-/fullmasterpresisering. Referanser var de sete originalene og godkjent HD-romanker. Hver fullscene er helskalert til 1952 × 800. Lokale nygenererte korreksjoner er deretter innfelt: lag 01 øyefelt [1642,155,40,20], samt TV [576,352,96,96] i begge lag. Kantblanding er rektangulær 2/3 piksler, ikke en originalkonturmaske. Alt utenfor disse feltene er målt byteidentisk med helskalert første rågenerering.

Lag 01 hadde fem imagegen-kall: fullscene, øyefelt og tre TV-forsøk. TV-forsøk 1 hadde separate øyne og ble forkastet; forsøk 2 hadde feil sideforhold/innramming og ble forkastet; forsøk 3 er valgt. Lag 02 hadde to kall: fullscene og TV-variant av valgt TV 01. Alle råfiler og fullstendige promptfiler med SHA er listet i c-leveranser.json. c-oppskrift.py.txt beskriver deterministisk skalering, innfelling og klipp. c-dokumenter.py.txt verifiserer hash, padding, overlapp og uendrede områder. De tidlige *-tv-source.png er feilbeskårne hjelpeutkast og er ikke brukt som kilde for TV-genereringen; *-tv-source-correct.png er riktig kildebevis.

## Kontroll og grenser

Uendret checker gir OK: lag 01 del 1 0,07 / 0,17 / 0,97; del 2 0,05 / 0,15 / 0,97. Lag 02 del 1 0,09 / 0,20 / 0,96; fremtidig del 2 0,07 / 0,24 / 0,97. Verdiene er globalt skift / blokkavvik / kantlikhet, ikke kvalitetskarakterer.

Alle 12 metadataobjekter er målt separat, ingen er hoppet over. c-objekt-kontroll.json inneholder eksakte bokser og korrelasjoner; c-objekt-qa-1/2/3.png viser hvert original-/HD-utsnitt. Laveste korrelasjon er TV 071_02 0,858, deretter vindu 080_02 0,866 og TV 071_01 0,871. Visuell kontroll bekrefter åpent vindu og begge TV-tilstander, men normalisering av små figurer og renere kanter er dokumenterte restavvik. Gulvrester, papirer og skallepunkter er mer tydelig modellerte enn kildepikslene. c-samlet-qa.png viser begge fulle kilder og HD-mastere; ingen feil tilstand er byttet mellom lagene.

Masterne er klare for roots mottaksvurdering med disse forbeholdene. Runtime, faktisk import/sammensetting i motoren og ny individuell brukergodkjenning er ikke utført. Fremtidig del 2 er kontrollert og masterlåst, men ikke levert i jobbmappen.
