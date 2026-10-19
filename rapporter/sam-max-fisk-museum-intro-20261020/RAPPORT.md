# Max med fisk, museumssekvens og Sam i introen

2026-10-20 01:13, Codex. Fem nye ark: fig193_01/02, fig298_01/02 og fig009_01. 61 native-ruter fra 55 eksakt ulike hele kildeutsnitt og 81 kildekomponenter. Kandidaten har 2134 native mot publisert grunnlag 2073. 199 av 1758 figurjobber har resultat; 1559 mangler resultat, i tillegg til returer og samlet spill-/stilkontroll. Faktisk publisering og hentet tilbake kontroll dokumenteres i mottak-publisert.json.

## Motiv og originalgrunnlag

193: Max plukker opp og kaster en liten grønn fisk mot akvariet ved World of Fish, rom 35. Originalt lokalt skript 213 bruker aktør 3, kostyme 193 ved 305,168. Fiskens grep, flyvende kropp/hode/hale og små restfragmenter er beholdt gjennom animasjon 1 og 7. Ingen pistol, plante eller ekstra hel fisk.

298: Sam viser John Muir-portrettet og mottar John Muir-grønnsaken ved Celebrity Vegetable Museum, rom 57. Lokalt 201 og globalt 114 bruker aktør 5 med kostyme 298 ved 299,128, mens museumsdamen i aktør 4/kostyme 297 skjules under fellesanimasjonen. Originaldialogen identifiserer John Muir. Portrettet er svart/hvitt med svart bred hatt, hvitt skjegg og gullramme. Damen er avklart mot kostyme 297: orangebrunt krøllet hår, tan/beige stråhatt med små hvite blomster/grønne blader og gul bluse. Lilla/grønt er grønnsaken som leveres, ikke damens klær eller en bukett. Bare hode/hals/krage/hånd der originalen viser disse fragmentene, ingen fullført kropp.

009: Sam i introens laboratorium, rom 2, globalt 65, etter «Hello?», ved 164,170. Hendene går mot og inn i lommene. Animasjon 7 er et delvis kroppslag uten hode/hatt, beholdt slik. Ingen normalisering til en hel figur.

Originalark, åtte originale motorforløp, Sam-/Max-master og damens sammensatte originalanker er sett før nytegning. Primære skript og SHA-proveniens er bevart. De tvungne motorprøvene viser ruter og lag i riktig rom; de er ikke naturlig gjennomspilling. Museumsprøven ved kildeposisjon fikk kameraklipp, derfor suppleres den med synlig diagnose i samme rom ved 170,165. Dette er ikke fremstilt som en naturlig kamerasekvens.

Bibliotekskilder brukt: figurark-fast-storrelse.md og scumm-v6-kostymer-skygge-og-soppelruter.md under prosjektbibliotek/losninger/grafikk, samt publisert-mod-er-fasit.md under losninger/bygg. Eksisterende v6-mottak, SHA-fremdrift og rutekart brukes med uendrede terskler.

## Produksjon

Elleve innebygde image_gen-kall, faktiske prompter/forespørsler og råbilder bevart. Ti råbilder brukes helt/delvis. F ga hatten en ekstra krone; K erstatter alle seks F-poser og følger originalens flate hattekant. F er beholdt som forkastet utkast. Ingen CLI-/API-fallback, avslag eller avbrutte bildekall i denne bunken.

Python renser generert kantalfa og plasserer hele genererte deler i originale delbokser. Originalens pikselmaske brukes ikke til å klippe nye silhuetter. Kildebekreftede separate fiskedeler, hvite blomsterpunkter og en håndstrek beholdes. Små ettpikselpunkter bruker generert mykt småmateriale med kildefarge. Seks magentafargeavrundinger med alfa 1 til 3 i 298_1935 er renset med alfa uendret. Alle 61 native kommer kun fra arkene, ingen originalutliggertillegg og ingen hel originalfallback. Identiske hele kildeutsnitt gir byteidentiske native PNG-er.

## Kontroller

Egenkontroll: 61 målte, 57 OK, fire SJEKK, null FEIL. SJEKK gjelder Max 193_1921, 1922, 1925 og 1931: snitt/union 0,72 til 0,75, 100 % bredde/høyde og null forskyvning. Alle fire er manuelt sett og står fortsatt som merknader. Ingen terskel er endret.

Native mottak: 61 OK, null til gjennomsyn, null mangler, null tekniske feil. Alle 61 er sett i seks kilde/native/motor-kontaktark og seks hele motorbilder. Alle er registrert tegnet i åtte tvungne motorforløp: 50 ved kildeposisjon og 11 flere i museets synlige diagnose. Den faktiske Linux-binæren e541253b fra nattpakken er brukt, med samme rom, posisjon, kamera, skala og animasjon mot uendret grunnlag 6512f670 først.

640 skjermbufferkontroller, 568 fra figurstart. Ingen nye eller økte avvik. Rom 57 og 2 er null. Rom 35 har fortsatt de tidligere inventarkantpikslene: 61 ved frame 36 og 27 ved 40 til 56 i begge forløp, null fra 60. De er lokalisert og dokumentert i tidligere sam-boey-og-slutt-rapport; denne grafikkleveransen retter ikke den motorfeilen.

Alle 20 beskyttede jobbfiler og tre opprinnelige stasher er bevart. Alle 20309 tidligere PNG-er byteidentiske, alle 20315 tidligere filstier bevart. Bare mod.json endres blant gamle kandidatfiler. Alle 20370 kandidat-PNG-er og 61 nye native-SHA-er skal også bekreftes etter faktisk hent.

## Gjenstår

Ny Tom-godkjenning, separat Claude-kontroll, naturlig gjennomspilling og ny interaktiv Windows-/webtest er ikke utført. Dette er egenkontroll og motorobservasjon, ikke endelig stilgodkjenning.

Felles Linux-/Windows-release sam-max-hd-2026-10-19-natt har 1960 native. Moddkandidaten har 174 flere. Pakkene oppdateres ved samlepunkt med faktisk nedlasting, sjekksummer og innholdskontroll før de kalles 2134.

Neste kildearbeid: fig039_01, fig113_01, fig295_01 og fig346_01 til 07. Følg bestilling 12 og avklar rekvisitter, palett og lag i originalmotoren før nye kall. Automatisk fortsettelse består, den gamle nattkontrollen forblir pauset.

Publisering og tilbakehenting bekreftet: kilde c0e364bfe2c249dcc692116c3cd03a923335eeda, hd-mod bdd4aec8b14581a0e090d976262818cda9246175. Alle 20370 kandidat-PNG-er og alle 20309 tidligere PNG-er bekreftet. 61 nye native-SHA-er stemmer, 2134 native totalt. 20 beskyttede kilder og tre stasher uendret. Se mottak-publisert.json. Pakken har fortsatt 1960 til samlepunktkontrollen.
