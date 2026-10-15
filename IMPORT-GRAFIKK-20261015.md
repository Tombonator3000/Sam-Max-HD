# Samlet grafikkleveranse for import, 15. oktober 2026

Nyere enn ZIP-pakken nedenfor: [seks nye rettede jobbresultater, fire komplette objektutsnitt og Toms feilbilder](rapporter/videre-grafikk-20261015/RAPPORT.md). Hent disse fra de ordinære jobb-/manifeststiene i repoet ved neste mottak. ZIP-pakken nedenfor er et tidligere datert øyeblikksbilde og inneholder ikke denne delrunden.

Alle kildeleveranser, råforsøk, prompter og kontroller er versjonert på `gpt-arbeid`. [Samlet importpakke](rapporter/import-grafikk-20261015/importpakke.zip) inneholder 155 separate RGBA-bilder, 12 tilhørende indeksfiler og 5 verbhjulaliaser. [Manifest](rapporter/import-grafikk-20261015/manifest.json) kobler hvert pakkebilde til original sti i repoet, objekt-ID, SHA-256 og behandlingsmåte. Arkivets SHA-256 ligger [her](rapporter/import-grafikk-20261015/importpakke.sha256).

Dette er inngangsdata til mottak og modbygg. Pakken er ikke en ferdig mod som kan kopieres direkte til spillet. Det er ikke gjort ny motorimport, webpublisering eller spilltest i dette pakkesteget.

## Bruk ved import

1. Hent `gpt-arbeid` og pakk ut `importpakke.zip` til et eget mottaksområde.
2. `ikoner/objects/`: 111 ikoner med egen alfa, inkludert siste rettede Max-ikon `obj1008_01`. Bruk den eksisterende myke ikonimporten som bevarer egen alfa, slik Claude beskriver i ORDRE 15. oktober 14:30. `verbhjul/` inneholder fem aliaser; koblingen til originalverb og objekt-ID følger `handlingsmanifest.json` i pakken. Aliasene er ikke fem ekstra spillobjekter.
3. `hele-motiver/objects/`: 30 komplette native objektmotiver. Disse må være tilgjengelige før modbyggets lappklipp. Vanlig lagmottak kan gjeninnføre lappalfa for tidlig. Bruk de komplette bildene fra manifestet før `_patch_from_full_painting`, fremfor å basere dette steget bare på de utklipte lagjobbene.
4. `egen-alfa/objects/`: inventareske `obj995_01` og LucasArts-logo `obj049_01`. Bevar den leverte alfaen og de rensede kantene ved mottak. Inventareskens stempel skal fortsatt være utvasket; «THX1138» er en tentativ lesning fra Tom.
5. `basseng-rom054/objects/`: 12 komplette tilstander av objektene 833, 834 og 836. De lagres i ressursrom 83, men tegnes i rom 54. Bruk de vedlagte `_idx.png`-filene med rom54-paletten ved fargelås/import. Indekspiksler og transparens er bevart. Bruk deretter originalens tilstandsmasker til lappklipp. Ikke fargelås disse bildene med lagerrom83-paletten.
6. Kontroller importen i motoren: tilstandsbytter, plassering, palett, alfa, peker/inventar og hele animasjonsforløp. Teknisk egenkontroll er ikke Toms visuelle godkjenning.

## Holdes utenfor import

`obj835_01` til `obj835_04` avventer Toms avklaring av svartfeltet under nesen som bart kontra åpen munn. Råforsøk og originalreferanser ligger i [rettingsrapporten](rapporter/lapper-eske-logo-20261015/RAPPORT.md), men rutene finnes ikke i importpakken. Behold eksisterende grafikk for disse til avklaringen er gjort. Avviste råforsøk er heller ikke importfiler.

## Kilder og kontroll

- [Ikonmanifest](rapporter/ikoner-ui-20261015/ikonmanifest.json), [ikonrapport](rapporter/ikoner-ui-20261015/RAPPORT.md) og [Max-rettelse](rapporter/max-ikon-retting-20261015/RAPPORT.md).
- [44 objektleveranser](rapporter/lapper-eske-logo-20261015/leveranser.json), [teknisk kontroll](rapporter/lapper-eske-logo-20261015/teknisk-kontroll.json) og [rettingsrapport](rapporter/lapper-eske-logo-20261015/RAPPORT.md). 36 lapp-tilstander består kontrollert utklipp; 3 lapp-tilstander i 835 avventer avklaring.
- 22 oppdaterte jobbresultater ligger på ordinære `jobber/<jobb>/resultat.png`-stier med notater. Egenkontroll: 20 OK og 2 SJEKK, ingen FEIL. Ikon01 og grønt flagg obj182_04 beholder SJEKK-status.
- [73 figurark med rettede rutekart](rapporter/fortsettelse-20261015/RAPPORT.md) er også allerede i repoet. Dette var en kartrettelse av eksisterende grafikk, og arkene er ikke duplisert i denne objektpakken.

Pakken er satt sammen uten nytegning eller endring av bildeinnholdet. SHA-256 i alle kildemanifester og alle arkivfiler er kontrollert. Bildearbeidets prompter og bruk av innebygd bildeverktøy er dokumentert i kilderapportene.
