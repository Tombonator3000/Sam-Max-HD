# Aktive returer

H126 / 1999: finere kurver, men mange fargefelt skifter størrelse og små felt mangler. Ingen import.
H127 / 1998: to alfafester og mange fargefelt avviker. Ingen import.
H128 / 1999: presis geometri (IoU 0,988), men stilretur for pikseltrapper. Etter global kodekalibrering gjenstår et for tett hull, runnerens lysegrønne felt og ekstra gult/teal.
H129 / 1999: ren tegning har IoU 0,997 og åpner hullet, men har andre feltfeil. Sammensetning med H128 har fortsatt ett mørkegrønt festeavvik og små ekstra kodefelt. Heleflyttdiagnosen gir ingen godkjent løsning og er ikke anvendt. Ren kontroll er kontroll-for-sammensetning.json.
H130 / 1999: isolert egen redigeringsmodul for runnerenden. Sammenstilling med H128-RGB og hel H129-alfa har alle positive alfa-/åpnings-/farge-/kodefester innen uendret 3 HD, men ekstra rene kodepiksler består fortsatt. 30 ekstra svarte kodepiksler og 1..2 i enkelte andre felt. Egen modul har en mørk støy-/omrisskant som ikke skal inn i sluttbildet. Ingen import eller stilgodkjenning.

Ingen port er svekket, ingen originalmaske er brukt til klipp, ingen originalfragmenter er lagt inn, ingen kildestyrt lokal trekkflytting er brukt. Egne hele redigeringsvinduer og globale RGB-kalibreringer er dokumentert. Alle fem faktiske råbilder og prompter er beholdt. Sammenstillingene teller ikke som nye bildekall eller leveranser.
