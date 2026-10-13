# Bestilling 28 A: minispillleveranser

Fire filer er produsert i seks innebygde imagegen-kall. Eksakt modell er ikke eksponert. Uendret checker gir fire OK; alle ni metadatafelt er målt, ingen hoppet over, med kantkorrelasjon 0,890 til 0,952. Manifestet er `a-leveranser.json`. Alle 40 beskyttede kilder og åtte ekstra kontekstfiler er uendret, dokumentert i `a-kildehashkontroll.json`.

Kildegrunnlaget er `a-kildeplan.md`, registerradene/palettene i `a-feltbevis.json` og familiebeviset. Første nye øyefeltforsøk la til en uønsket tredje mørk form. Det er bevart som råforsøk 01 og ikke valgt. Forsøk 02 har bare de to avskårne krem/grå fragmentene med to korte mørke øyestreker. Ingen komplett Max er lagt inn i rom018.

Sam-øyne og tunge i lag018_01 er kildeidentiske med grunnrommet og gjenbruker rom018-HD direkte. Lag018_02 har det kildeegne blikket, den lave tungeformen og en liten separat nesefirkant. Lag018_03 har lukkede øyne og annen rundere tunge. Hvert nye Sam-uttrykk er generert som ett samlet ansiktsutsnitt, med samme kildeoverlapp mellom194/195. For å bevare uendret kjeve-/øregrense settes to indre rektangler fra dette SAMME nye bildet inn: [1004,250,116,66] og [1032,320,100,56]. Dette er vanlig rektangulær komposisjon, ikke originalkonturmaskering eller lokal warp. Fire HD-pikslers kantovergang brukes mot det nye HD-rommet.

Lag019_01 har egne bøyde Max-ører med rosa innside, avskåret venstre øre/pote, små øyne/nese og tannrekke ved brettkanten. Sam har arm nede. Ingen poengpanel eller arm-/redskapsunderlag fra lag019_03 er importert. Max-feltet er hentet fra fullkontekstgenerering, med presis metadatarektangelplassering.

Alle fem hull er fortsatt tomme i hver fil. Rom018 beholder HIT 20 WIN, to stjerner og tomt svart tellefelt. Rom019 har ikke poengpanel. Øvrig rominnhold er byte-identisk med riktig allerede levert rom-HD utenfor metadataunionen. Filer er opake RGB 1536 x 1024, motiv [128,112,1280,800], nøytral padding nøyaktig128. Ingen originalpiksler er brukt som nytegnet resultat, ingen vektor eller silhouette-maske.

`a-samlet-kontaktark.png` og `a-objektqa.png` viser alle originaler og leveranser. Begge er visuelt sett etter siste sammensetting. Små felt er nytegnet med mer overflateform og antialiasering, særlig nesefeltet; de er ikke påstått farge-/pikselidentiske. Ingen runtime, import, poenglogikk eller timing er testet. Ingen ny individuell brukergodkjenning. Root tar samlet mottak.

Reproduksjon: `a-forbered-produksjon.py.txt` lager referanseutsnitt/prompter; råbildene er bevart med SHA og verktøyproveniens i manifestet. `a-sammensetting.py.txt` lager leveransene; `a-sluttkontroll.py.txt` lager målinger, hash, notater og QA. Den tidligere sammensettingsoppskriften er bevart for sporbarhet og brukes ikke som sluttmetode.

Sluttkontroll av 196-feltet avdekket en mørkere blå stripe fra generatoren mellom de to avskårne øyefeltene. Den blå fargen i det NYGENERERTE feltet er derfor erstattet med riktig NYTEGNET rombakgrunn etter RGB-kriteriet i a-blaafeltbevis.json. Ingen originalpiksler eller originalkonturmaske brukes. Kremfargede felter og mørke øyemerker beholdes, med myk blanding bare i generert blå antialias. Den gjentatte uendrede kontrollen er OK, og korrelasjonen for 196 er nå 0.951366. Alle ni felt er fortsatt OK. Oppskriften a-sammensetting.py.txt er faktisk kjørt før siste manifest og kontaktark.
