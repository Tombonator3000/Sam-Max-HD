# Bestilling 27 – gruppe C, kilde- og leveransekontroll

Fem leveranser er skrevet med uendret egenkontroll OK. Alle 40 låste kildefiler er kontrollert uendret. Ingen Git, motor-/pipelinekode eller globale logger er endret. Runtime og ny individuell brukergodkjenning er ikke verifisert.

## Kilde og tilstander

Grunnlaget er B sin kildeplan, metadata, originale komposisjoner og nærbilder. Filnavnene alene har ikke bestemt motiv. 015 er to ulike små mekaniske tilstander: lav treplattform med flat grønn pute, og separat liten grålilla vekt. Vektlaget beholder grunnrommets øvrige plattform; det er ikke en kopi av plattformlaget. 012 er grønn kaktusskulptur med brun sombrero, rødt tørkle, to armer og lav grå sokkel. Den samordnede nytegnede 26-bakgrunnen har røde klipper og er kontrollert mot A sin SHA `99862986164f546199b6d27bef06e96d61e1cc3dabc0b1c8f09849556416cf01`.

017 har åtte objekter i én hel komposisjon: åpnet WIN-front med små røde/lyse former (innholdets identitet uavklart), tom linseholder, hevede to røde grep, åpen Trixiedør med mørkt interiør og rødt nedre felt, tre egne vimpler og propell. Ingen person er lagt i døråpningen. Overlappsfeltets objekter er med i begge deler selv om metadata fordeler dem mellom delene. Skilt, øvrige vinduer, gjerder, kabel og bakgrunn er gjenbrukt fra riktig nytegnet grunnrom.

## Produksjon og rettinger

Innebygd ChatGPT imagegen; eksakt modellnavn er ikke eksponert. Hver lagrede prompt begynner med den urørte jobbprompten og har separat kildepresisering. Første lokale nærbildeforsøk for 012/015 endret proporsjoner/kanter for mye. De er bevart, men valgt forsøk 2 bruker hele kildekomposisjonen og grunnrommet som referanser. Første 012 gav objekt-FEIL 0,41; første 015 gav SJEKK 0,58 og 0,52. Sluttforsøkene gir henholdsvis 0,967, 0,801 og 0,657 i objektfeltene. Ingen teknisk terskel er endret.

015 og 012 bruker bare det nygenererte metadatarektangelet, 3 px rektangulær kantblending og byteidentisk nytegnet grunnlag utenfor feltet. Ingen originalpiksler eller originalkonturmasker er brukt i resultatet. Kaktusfeltet erstatter også det tidligere 133-motivet fullstendig.

017 bruker én 2528 × 800-master fra de allerede overlappskonsistente HD-grunnrommene. Åtte nygenererte objektfelt er innfelt, deretter er begge 1536 × 800-klipp tatt ved x = 0 og x = 992. 544 × 800-overlappen er byteidentisk. Motivet står ved y = 112 på RGB 1536 × 1024; padding er nøyaktig 128.

Egen nærkontroll fant en gammel rød linsebue som grunnrommet hadde tegnet ovenfor metadatarektangelet. Et 12 HD px høyere rektangulært klipp fra samme nygenererte tomfelt fjerner dette. Faktisk innklipp i fullmaster er [1024,340,96,76]. Resten utenfor de åtte feltene med denne eksplisitte utvidelsen er byteidentisk med grunnmasteren. Førversjonen er bevart.

Vimpelinnklippene hadde svake blå rektangelgrenser. Et jevnt bilineært additivt RGB-felt, estimert robust fra grenseforskjell mellom nytegnet felt og nytegnet grunnrom, sammenpasser fargetonen. Ingen geometri eller originaldata inngår. Mål/koeffisienter er i c-017-grensetone.json; maksimal korreksjon er omtrent 11 av 255. Etterkontroll av fullmasteren viser sammenhengende himmel og tom linseholder uten den røde resten.

## Visuell kontroll og begrensninger

c-objektqa-1..3.png viser original / valgt HD / grunnrom for alle 11 objektrektangler, med c-objektkontroll.json som målebevis. Alle 11 er faktisk kontrollert. De åtte 017-feltene har korrelasjoner 0,912–0,982; tallene erstatter ikke motivkontroll. c-familie.png og c-017-fullmaster.png er også inspisert samlet.

Kaktusens hattmønster, munnendemerker og materialstrøk er tydeligere, kroppen glattere. Plattformens grønne topp er mer rettkantet; vekten er en glattere trapesplate enn originalens små knekker og har familiens laveste korrelasjon 0,657. Vimpler, grep og WIN-rand er rundere/blankere enn kilden. Propellen følger riktig diagonal, men har samme generelle HD-avrunding som grunnrommet. Disse er konkrete tegningsforbehold, ikke bekreftet pikselidentitet. Ingen ny figur eller gjenstand er observert.

Se c-leveranser.json for SHA-256, valgte råforsøk, eksakte prompt-SHA og kontrollfiler; c-komposisjonsbevis.json for geometri, padding, overlapper og bytekontroll. Oppskrifter er bevart som .py.txt. Ingen faktisk spillmotor-/animasjonstest er utført.
