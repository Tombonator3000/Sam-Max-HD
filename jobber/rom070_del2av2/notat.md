# rom070_del2av2: HD-leveranse

Innebygd ChatGPT-bildegenerator, 2 kall inklusive eventuell smal etikettkorreksjon. Eksakt modellnavn er ikke eksponert. Kilder og feilaktige romnoter er dokumentert i a-kildeplan.md og a-kilde-qa.md under rapporter/bestilling017-20261013. Ordrette prompter med kildekorreksjon er bevart.

Resultat SHA256: e5ef3e368e6e3ca5bafe0e18dbe262ee0268e3b6b3ababaf73b85815071e8b0a. Egenkontroll med uendret verktoy/sjekk_leveranse.py: OK. Kontrollfil: rapporter/bestilling017-20261013/a-rom070_del2av2-kontroll.txt.

1536 x 1024 med eksakt RGB128-padding. Rom070 kommer fra én 1920 x 800-master med skift 384 og byte-identisk overlapp 1152; fullmaster-SHA står i a-leveranser.json. Ingen warp, originalmasker eller vektortrace. Vanlig helskalering/plassering og smalt rektangulært uttak fra NYGENERERT etikettkorreksjon er dokumentert i a-oppskrift.py.txt.

Alle 26 rom070-grupper og rom071-grunnfigurene er visuelt kontrollert. Pizzaeskens små glyffer er fortsatt ikke fullt kildeavklart, selv etter smal retting. Indre ornamenter er ikke sertifisert pikselidentiske. Teknisk OK er ikke visuell godkjenning. Ingen runtime, import eller påkledningsinteraksjon er testet.

Råforsøk, kildeutdrag, master, komplett prompt, oppskrift, QA og 44 uendrede kildehash er bevart i rapportmappen.
