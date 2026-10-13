# Bestilling 15 B, kilde-QA

Obj607,608 og610 har OK. Obj609 har SJEKK etter andre forsøk: skift 0.97, blokk 1.98, kantlikhet 0.94. Første609/610 var FEIL og ble omtegnet. SJEKK er ikke godkjent automatisk og må inngå i roots mottaksvurdering.

Alle 40 låste kilder er kontrollert uendret. Kildeplanen og Highway Surfing-registeret er brukt. Råbilder og ordrette prompter med separat lagpresisering er bevart. Ingen vektortrace eller masker fra originalen.

Familie-QA:607 har gulstripe som heller venstre nedover,608 høyre nedover; begge er bredere og lysere enn609/610.609 har nesten rett stripe fra toppen,610 skrå stripe mot venstre nedover. Veikantene har de ulike hellingene. Ingen nye HUD-felt, tekst, biler, veistriper eller objekter. Både nesten svarte sidefelt og tomme veirader er bevart.

Forbehold:609 har fortsatt litt lengre stripe og lokale kantavvik, i samsvar med SJEKK. Genererte flater har svak malerisk tonevariasjon, også i mørke sidefelt; ingen ny asfaltkorntekstur eller fysisk detalj er tilsiktet. Den presise RGB (7,7,0)-flatheten er ikke garantert av genereringen. Lave felt er særlig følsomme for få pikslers avvik.

B-familiearket viser original over HD for hver jobb. Motortegning, segmentrekkefølge, dynamisk palett og sømløshet mot øvrige veisegmenter er ikke runtime-testet. Runtime og individuell ny brukergodkjenning er false.


Avgrenset lokalforsøk 3: imagegen ble bedt om å korte inn stripen med originalen som kilde. Et fast rektangel [730,464,45,52] ble satt inn i en diagnostisk kandidat; alt utenfor ble verifisert byte-identisk. Uendret checker ga fortsatt SJEKK, blokk 1.98. Gulområdet endte fortsatt på y507 mot originalens y503 (inklusive), og flyttet seg ett HD-piksel til høyre. Lengdeavviket ble dermed ikke rettet. Forsøk 2 beholdes som beste leveranse, SHA uendret. Forsøk 3 og kontroll er bevart, men ikke brukt. Ingen warp eller originalkonturmaske.
