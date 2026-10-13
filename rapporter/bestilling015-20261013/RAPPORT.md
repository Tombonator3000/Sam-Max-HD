# Samlet rapport for bestilling 15

Ti lave Highway Surfing-veisegmenter er levert: **9 OK og 1 SJEKK**, obj605_01. Root har sett alle ti originaler og HD samlet. Alle 40 beskyttede kildefiler er uendret, lerret/padding/resultat-SHA kontrollert i sluttkontroll.json. Skilt, HUD, biler og ekstra veimarkører er ikke lagt til.

604 til 608 har stripe ved nedre kant, 609 til 613 stripe ved øvre kant. Alle beholder hver sin sidevinkel, svartaktige sidefelt og gulstripe. Originalens grådithering er tolket som en svak ny gradient. Sidefelt med RGB nær (7,7,0) er motiv, ikke transparens. 605 har små lokale side-/stripevinkelavvik og egenkontroll SJEKK, blokk 1.13; dette er ikke kalt OK. De øvrige er teknisk OK, ikke påstått piksel- eller geometrisk identiske med originalen.

Root målte veikantene uavhengig i root-kantmal.json. Avvikene kunne ikke korrigeres med én samlet forskyvning. C alfasegmenterte derfor de nye genererte gulstripene i 609/612/613, laget rent underlag med innebygd imagegen og helskalerte stripene til målte rektangler. Ingen originalpiksler eller originalkonturmasker inngår. Resten av veiene var byte-identisk etter dette trinnet. 612/613 ble OK; tidligere kandidater og kontroller er bevart.

609 krevde deretter vanlig helskalering av selve nytegnede veikomponenten, fra [10,0,1024,96] til [8,0,1016,96] lokalt. Ny gulstripe ble beholdt fast i [500,0,524,40]. Originalen bidrar bare med rektangulære mål og kontrollpunkter, ingen lokalt geometriwarp, trace eller konturmaske. 40 kantmålinger forbedret middel absolutt HD-avvik fra 5.2 til 1.775 og maksimum fra 12 til 5. Små lokale avvik består. Uendret checker gir nå OK 0.14 / 0.52 / 0.98. Root har sett før/etter og samlet familie; root-609-overstyring.json er gjeldende, B/C-manifestene er bevart historikk.

Bestilling 14 sine ti leverte PNG er SHA-verifisert fra eksakt GitHub-commit, se bestilling014-pushkontroll.json. Ordrette prompter med egne kildepresiseringer, råforsøk, oppskrifter, familieark og notater er bevart. Eksakt bildemodellnavn er ikke eksponert. Ingen motorimport, masker/nøkkelfarge, originaltiming, faktisk Highway Surfing-visning eller ny individuell brukergodkjenning er verifisert.
