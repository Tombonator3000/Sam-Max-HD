# Alkoven: flere hoder og sugepiler

2026-10-20 02:48, Codex. Ti figurark, fig346_08 til 17. 22 nye runtime-ruter fra 17 ulike hele kildeutsnitt. Kandidat 2199 native, grunnlag 2177. 219 av 1758 figurjobber har resultat, 1539 mangler pluss returer og samlet spill-/stilkontroll.

## Kilder og produksjon

Lokalt skript 201 i rom 92 bruker aktør 6 ved 159,101, clip 0, skala 255. Originalark, to grunnlagsmotorforløp og godkjent Sam-master er sett. Varm brun/orange drakt, kremgul skjorte og grått/svart slips er tilsiktet lys. Lilla sugekopper/fjær og gule skaft, senere også tredje kopp på nesen. Avkuttede pilfragmenter fullføres ikke. 1956 er en brun, loddrett 1x19-avslutningsrute med to brune fargeband; den er ikke en pil eller kropp.

Fem innebygde image_gen-kall: sju nye hoder og tre separate sugepil-deler. Alle fem råbilder og faktiske prompter/forespørsler er bevart med SHA-er. Seks tidligere genererte prototyper dekker ni runtime-ruter med eksakt samme hele kilde-RGBA. De nye hodene gir ni runtime-ruter med aliasene; tre nye rekvisittdeler gir tre, og den enkle brune endestripen gir én. Stripen er beskåret/farget fra tidligere generert brunt materiale, ikke kalt en ny detaljtegning. Ingen CLI/API-fallback, avslag eller avbrutte bildekall.

Bibliotekskilder: prosjektbibliotek/losninger/grafikk/figurark-fast-storrelse.md og scumm-v6-kostymer-skygge-og-soppelruter.md. Eksisterende v6-mottak, eksakte kildebokser, SHA-fremdrift og rutekart er gjenbrukt og kontrollert i dette prosjektet. Ingen motor- eller pipelineendring.

## Lagmøtet ble rettet før publisering

Automatisk bufferkontroll var ren, men første helbildekontroll viste forskjell i nytegnet skjorte/jakke og den publiserte torsoen. En RGB-blanding og senere geometrisk kanttilpasning ga uønskede overganger og ble forkastet. De tidligere prøveforløpene er bevart i motorlogger.zip; de teller ikke som sluttresultat.

Sluttversjonen bruker sammenhengende genererte klær fra tidligere kontrollert costume346_1793-prototype som produksjonsmateriale under de sju nye hodene og sugepilene. Hoder, ansiktsdetaljer, piler og små kildebekreftede deler beholder egen generert alfa. Klærne er tilpasset 616 HD-piksler, og jakkematerialet fortsettes der det løftede øret avdekker skulderen. Ingen hard originalsilhuettmaske er brukt.

Automatisk native mottak: 22 OK. Sluttmottaket viser 18 etterfølgende produksjonstilpasninger. Ni runtime-aliaser bruker byteidentiske tidligere native ved eksakt samme kilde-RGBA. Ni nye runtime-hoder fra sju tegninger holdes ved kildens faste 4x-mål og 0,0, uten ekstra native-overlapp. Sluttomriss og dekning er målt igjen med de samme tersklene. Fire rekvisittruter er uendret fra mottaket. Se intern-lagkant-retting.json med før-/etter-SHA og bevart automatisk metadata. Tidligere publiserte filer er uendret.

## Kontroller

Egenkontroll: 21 målte ruter, 19 OK, to SJEKK, null FEIL. 1808 og 1810 har snitt/union 0,72, 100 % bredde/høyde og null forskyvning. Begge er manuelt sett og beholdt med merknad. 1x19-stripen er for smal for automatisk måling og er sett manuelt. Alle 22 har native mottak, uten originalutliggertillegg eller hel originalfallback. Ingen magenta med synlig alfa, ingen alfa utenfor resultatarkenes rutebokser. Like hele kildeutsnitt gir like native-SHA-er.

Alle 22 er sett i to original/native/motor-kontaktark og seks hele motorbilder. To endelige tvungne forløp, animasjon 1 og 7, ved kildeposisjon/aktør og med samme nedlastede e541253b-binær som grunnlaget. 160 skjermbufferkontroller, alle null, 142 fra figurstart. Ingen nye eller økte bufferavvik. Dette er ikke naturlig gjennomspilling.

40 beskyttede jobbfiler og tre opprinnelige stasher er uendret. Alle 20413 tidligere PNG-er er byteidentiske og alle 20419 gamle filstier bevart. Kandidaten har 20435 PNG-er og 20441 filer, 2199 native. Bare mod.json endres blant gamle kandidatfiler. Alle nye og gamle PNG-er skal bekreftes på nytt etter faktisk send/hent.

## Videre arbeid

Ingen ny Tom-godkjenning, separat Claude-kontroll eller interaktiv Windows-/webtest. Rommet har fortsatt originale Max-nærbilder og senere, ubehandlede deler. Kjent inventarkantavvik i rom 35 er ikke rettet her.

Siste felles Linux-/Windows-release sam-max-hd-2026-10-20-natt har fortsatt 2134 native. Etter denne leveransen er modden 65 ruter nyere. Pakkene oppdateres ved neste samlepunkt med faktiske nedlastinger og filkontroll.

Neste jobb er fig346_18. Fortsett kildebasert og søk eksakt gjenbruk før nye kall. Ikke gjenta denne bunken eller tidligere avviste 110_05/06 og 246_16 til 19. Automatisk fortsettelse er aktiv; gammel nattkontroll forblir pauset.

Faktisk publisering og tilbakehenting bekreftet: kilde 33ac0406607f5b8a9ee486d7620e3037f896e7ad, hd-mod ca6258e71ce130c228d45be233830945c1ceb16d. Alle20435 kandidat-PNG-er, alle20413 tidligere PNG-er og alle22 nye native-SHA-er stemmer.2199 native totalt.40 beskyttede kilder og tre stasher uendret. Se mottak-publisert.json. Fellespakken har fortsatt2134 og mangler65 til neste samlepunkt.
