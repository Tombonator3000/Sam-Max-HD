# Sam004: gjenbruk og sluttkontroll

Seks RGBA-resultater er klare for rotens mottak. Alle seks får OK fra uendret sjekk_leveranse.py. Alle 71 nye cels er RGBA-byteidentiske med donorens rektangulære celutsnitt inkludert åtte pikslers alfamargin. Ingen resampling, originalkonturmaske eller ny generering er brukt. Donorene er uendret. Kopiering ble autorisert etter mottak av commit 03e56d0cbbb7815cfeb743fe006d3d0b8c730aec.

[a-leveranser.json](a-leveranser.json) inneholder resultatfilene og SHA. [a-celkart.json](a-celkart.json) inneholder donorhash, utsnittshash, alle 71 alfa-bokser og egne festepunkter. [a-gjenbruk-utfort.json](a-gjenbruk-utfort.json) dokumenterer faktisk kjøring. De 24 låste kildene er kontrollert uendret.

Alle seks helscener og seks feltark er sett. Kildeegne kroppsfragmenter, hender, snakkehoder, gåstillinger og tre retninger er beholdt. Ingen manglende kroppsdeler er fullført. Bildene arver donorens godkjente mottak og tegnede modellering, med glattere og rundere detaljer enn pikselkilden. Dette er ikke en ny individuell brukergodkjenning eller runtime-test.

## Øyelokk som checker hopper over

Cel 513 har 7 synlige kildepiksler; cel 512 har 6. Checker hopper over dem fordi antallet er under 20. Begge er eksplisitt sett i [øyelokk- og rel-arket](a-oyelokk-rel-qa.png). De har to separate brune smådeler, uten utfylling mellom dem eller nye ansiktsdeler. Nye alfa >=128-arealer er henholdsvis 112 og 111 HD-piksler. De er ikke innbyrdes kopiert: hver er byteidentisk med sin egen nye pilotcel. Dette er visuell og numerisk kontroll av de små ressursene, ikke verifisert øyelokksavspilling i motoren.

## Festepunkter og palett

Cel 169 og 170 har fortsatt målmetadata rel_x=-19, mens donorens opprinnelige kostyme hadde -18. Bildegjenbruk endrer ikke disse festene. Ingen kompenserende rasterforskyvning er innført. Feltarket viser begge kildestillingene, nytegningene og metadataforskjellen. Riktig anvendelse av festene i motoren er ikke runtime-testet.

Kostymepalettens indeks 14 er fortsatt 14 for Sam004 mot 255 for Sam002. De 71 RGB-kildecels er identiske til tross for denne metadataforskjellen. Ingen palettmetadata er endret.

## Alfa og små donorrestfarger

Ytre canvaspadding har alfa 0. Atlasets tomme rom er transparent, ikke RGB-magenta bakgrunn. De seks allerede dokumenterte magenta-RGB-pikslene med alfa 1 er bevart i ark 02/03/04, fordelt 2/1/3. I tillegg har pilotark 01 én slik piksel med alfa 1. Totalt er det syv slike nesten transparente kantpiksler i de seks arkene, ingen med alfa over 1. De vises ikke som en synlig bakgrunn i kontrollarkene. Donorene er ikke redigert for dette.

## Kontrollark og proveniens

[Alle seks helscener](a-helscene-qa.png), [felt 1](a-feltqa-1.png), [felt 2](a-feltqa-2.png), [felt 3](a-feltqa-3.png), [felt 4](a-feltqa-4.png), [felt 5](a-feltqa-5.png), [felt 6](a-feltqa-6.png). Kontrollarkenes grå visningsbakgrunn er ikke del av RGBA-leveransene.

Oppskrift: [a-forbered-gjenbruk.py.txt](a-forbered-gjenbruk.py.txt), [a-sluttfor.py.txt](a-sluttfor.py.txt). Opprinnelig nytegning, råfiler og prompter spores via donorens manifest i bestilling052 og pilotens eksisterende proveniens. Ingen nye imagegen-kall er utført her. Eksakt underliggende bildeversjon er ikke eksponert. Ingen Git-, globale status- eller produktkodeendringer er gjort.
