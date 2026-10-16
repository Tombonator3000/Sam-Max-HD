# Status 15. oktober 2026

Siste feilrunde: Sams frontvendte hånd er rettet i fig002_01 og fig004_01, og 110 separate RGBA-ikoner har fått grønn kantmatte renset uten endring av alfa eller størrelse. Lokal motorretting er bygget og testet: inventarkortene er rene, og rosa/blå maskefeil i akvarium og cafeteriarør er borte i prøvene. Grafikken er klar for mottak, kode går via egen PR; denne delrunden er ikke publisert som ny spillpakke. Øks-/bakgrunnsrester, kranhode/dumpling, faktisk opptak og bilens avreise gjenstår. [Rapport og overlevering](rapporter/feilrunde2-20261015/RAPPORT.md).

Oppdatert status for grafikkgrenen: stilpiloten er godkjent, første HD-mod er laget, og siste ORDRE gjelder videre arbeid. Avsnittene nedenfor er historiske og beskriver de tidligere konsept- og pilotrundene.

15. oktober er rutekartformatet rettet for alle 73 leverte figurark, 931 ruter. Mottaket kunne tidligere lese kart for bare 2 ark. Alle 12 returrutene øverst i ORDRE har to tegnede komponenter; radgjettingen utelot én av dem. Begge er nå koblet, uten endring av PNG-ene.

Kontroll: alle 73 kart leses av mottakets eksisterende kartleser, alle alfakjerner har én eier, 365 kilde-/resultatfiler er uendret. Egenkontroll: 69 OK, 4 SJEKK, ingen FEIL. Ny motorimport, hd-mod og spilltest er ikke utført. Se [rapporten](rapporter/fortsettelse-20261015/RAPPORT.md).

Mangler resultatfil: 1685 figurark og 28 lagjobber. Alle 9 ikonark, 115 romjobber og 86 store objektjobber har nå resultatfiler, men enkelte er fortsatt avvist eller trenger retting etter ORDRE. Filtilstedeværelse betyr ikke godkjenning.

Verb/inventar, 15. oktober: ikon07, ikon08 og ikon09 er levert og består egenkontroll. 21 handlingspekere og 90 inventar-/samtalebilder er eksportert separat med ekte alfa, med fem navngitte verbhjulikoner og manifest. Alle 117 felt i de tre arkene er visuelt gjennomgått. Ingen ny motorimport eller spilltest. Se [ikonrapporten](rapporter/ikoner-ui-20261015/RAPPORT.md).

## Historisk status 12. oktober 2026

Delvis konseptleveranse i [galleriet](konsept/2026-10-12/index.html), med [analyse](konsept/2026-10-12/ANALYSE.md).

16 av 33 foreløpige motivgrupper har konseptkandidat. Fire første forsøk er avvist og erstattet. 17 konsepter gjenstår. Diskplassblokkeringen fra 12. oktober er opphevet (rundt 37 GB ledig kontrollert 13. oktober). Listen er ikke bevist komplett for alle skapninger.

348 kostymer og 959 objektbilder er indeksert. Mange motiver og egennavn krever fortsatt semantisk kontroll. Kostyme er ikke det samme som person. Konseptene er ikke spritesheets, ikke godkjent av Tom og ikke kontrollert i motoren.

Ingen HD-konvertering, motorendring eller pipelineendring er gjort. Ingen commit eller push. Alt arbeid her er lokalt i gpt-arbeid. SHA-256, tabellantall og lokale gallerilenker er kontrollert; galleri i nettleser og spillavspilling er ikke testet.

## Stilrettelse 13. oktober

Se [ANALYSE.md](ANALYSE.md): tynnere Bigfoot-strek og Steve Purcell-referansene fra Tom. Dette dokumentasjonssteget lager ingen nye HD-ruter. Kandidatene er fortsatt ikke produksjonsgodkjent.

## Hovedark 2026-10-13 15:47

To hovedark er levert som pilotkandidater: hovedark/sam.png og hovedark/max.png, med notater, prompter, SHA-256 og kontroll i rapporter/hovedark-20261013/. Begge er PNG 1536 x 1024 med ekte alfa og fem visninger. Egenkontroll SJEKK, ingen FEIL i valgte kandidater. Sam er 5 til 7 prosent for høy i ståvisningene; Max 10 til 12 prosent for lav. Bredde og plassering er også dokumentert som avvik. Ikke godkjente stilankere eller ferdige produksjonsark. Ingen motorimport eller spilltest.

Max-ikonet obj1008_01 er rettet etter Toms avvisning 15. oktober. Ny tegning fra originalen, godkjent hovedark og Purcell-referanse, med små svarte øyne og tannglis. Ikon08 består egenkontroll; de øvrige 110 RGBA-ikonene er uendret. Toms godkjenning og spilltest gjenstår. Se [rettingsrapport](rapporter/max-ikon-retting-20261015/RAPPORT.md).

## Retting av lapper, eske og logo 15. oktober

44 separate RGBA-bilder levert, 22 jobbresultater oppdatert. Egenkontroll: 20 OK, 2 SJEKK, ingen FEIL. 36 av 39 lapp-tilstander har komplette tegninger kontrollert mot eksisterende lappklipp. Objekt 835s fire kandidatbilder holdes utenfor produksjon mens bart/munn avklares med Tom. Rom83-ressursene bruker rom54-paletten i bassengscenen og leveres separat med passende indeksfiler. Ingen runtimeimport av denne pakken. Se [rapport](rapporter/lapper-eske-logo-20261015/RAPPORT.md).

Ny status fra Claude dc5fcba9: de tidligere 111 ikonene er tatt inn i hd-mod; pekeren er sett i spillet. Dette erstatter den tidligere opplysningen om at disse ikonene ikke var publisert.

## Videre grafikk og Toms feilbilder, 15. oktober

Seks jobber er oppdatert og består egenkontroll med OK: obj811_01, lag037_01_del2av2, lag037_02_del1av2, lag045_03, rom010 og rom015_del1av2. Kjerub-/djevelmotivet og Sams nedre tannrekke er rettet etter Tom. Fire komplette RGBA-objektutsnitt er levert separat. Nye forsøk på obj187_05 og obj307_01 består ikke kontrollen; tidligere resultater er beholdt.

Sam091s åtte høydereturer skyldes ulike målebokser for original/HD når en løs fotrest filtreres bort fra originalen. Arkene er uendret; bevis er levert for mottaksvurdering. Toms rester etter opptak, hammerkanter og skadde chatrammer er dokumentert som åpne runtimeproblemer. Se [rapport](rapporter/videre-grafikk-20261015/RAPPORT.md). Ingen import av denne delrunden i hd-mod eller ny spilltest. Main har i mellomtiden fått myke romobjektkanter i 9e1b7b29 (#29); effekt på Toms feilbilder må bekreftes i spillet.


## HD-produksjon 2026-10-16T12:57:09+02:00

Fem nye ark med32 ruter og én munndelretting levert til kontroll i gpt-arbeid. fig249_02 og fig249_04 har egenkontroll OK; fig249_05 til fig249_08 SJEKK. Ingen ny import eller motoravspilling. Se rapporter/produksjon-20261016/RAPPORT.md.
