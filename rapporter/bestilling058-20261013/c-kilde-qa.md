# Sluttkontroll av 205-familien

Alle 57 ruter er levert i fig205_01..03. Uendret checker gir OK på alle tre ark, med 26 + 21 + 8 kontrollerte ruter. De to små ansiktslagene faller utenfor checkerens vanlige rutetelling og er derfor kontrollert separat i faktisk rel-sammensetting.

`c-vendingskvittering.json` beviser alle 49 kilde-RGB-transformasjoner og de tilsvarende nye RGBA-transformasjonene. 47 er vertikalvending, to er uendrede smålag. Korrekt ny B-komponent for 395 er brukt til 267, med egen filhash; det gamle uriktige røde munnfeltet er ikke med. Alle 57 leverte utsnitt er byte-identiske med de registrerte nye komponentene. 258 og 295 bruker samme nye komponent.

De sju egne motivene ble laget med tre C-bildekall. Første 257 hadde øyne som ikke passet under det gjenbrukte smålaget 385. Sluttvarianten beholder den nye kompatible 003/385-hodekomponenten og legger bare inn det kildeegne lille tan-feltet i øvre munnkant fra tredje bildekall. `c-257-lokalbevis.json` viser 6 × 4 felt og null endringer utenfor det. Den ene originale forskjellspikselen ligger ved (16,1), hvit (251,251,251) til tan (215,179,143); dette er en munnkantvariant, ikke en ny øyeform. Rel-arket viser nå begge øynene dekket av 385. Den forkastede hele nytegningen er beholdt som råforsøk.

288 fikk smal svart/hvit tannrad med originalens lille rosa markering, ikke den første store hvite sikksakkmunnen. 291 fikk enkel punktmunn uten første forsøks krumme streker. 274 har kun svart/hvit sideåpning, ikke rødt munnfyll. 289 beholder den kildeegne lille utstikkende tungen. 258/295 er blanke bakhoder uten nytt ansikt.

Visuelt kontrollert: alle åtte `c-ruteqa-*`, tre faktiske leveranseark, `c-rel-HD.png` og tre `c-tale-rel-r*.png`. Samme Max-identitet, opp-ned-retning, fraskilte lag og kropps-/hodeforhold består. Kontrollerte kilder er låst og uendret, 12 av 12.

Konkrete kvalitetsforbehold: HD-tenner og poter er tydeligere enn originalen. Egne 288/291 er noe lysere og har tynnere strek enn flere donorer. Noen sammensettinger har et lite synlig halsgap mellom avrundede HD-konturer, uten endret rel. Donorens svært svake alfakanter er bevart ved eksakt gjenbruk. Ingen av disse forholdene er omdøpt til kildepikselidentisk gjengivelse. De er synlige i rapportarkene for rotkontrollen.

Ingen runtime, motorimport eller ny individuell brukergodkjenning er utført. Ingen originalmasker, vektortrace eller geometriwarp er brukt. Ingen 003-filer, andre agenters jobber eller globale filer er endret.
