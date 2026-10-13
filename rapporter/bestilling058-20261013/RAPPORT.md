# Bestilling 58: Max-hoder og vertikalt vendt Max

Fem nye figurark med 90 ruter er levert: fig325_01/02 og fig205_01..03. Fire tidligere leverte ark er rettet: fig003_01/02 og fig005_01/02. Alle ni har OK fra uendret sjekkverktøy. De små øyelagene som verktøyet hopper over, er i tillegg kontrollert med kilde, alfa, donorbytes og visuell sammensetting. De fire rettingene øker ikke antallet ferdige jobber.

## Motiv og plassering

325 er Max. Alle 33 originalfeltene har eksakte partnere i leverte Max-kilder. Tre nye munnkomponenter er rettet lokalt; 30 komponenter er bytekopiert. Målmetadata har konsekvent rel-avvik (-1,+19) kildepiksler mot donor; målmetadata beholdes uten forskyvning inne i atlaset. To smålag har to lyse former hver og egne mål på 56 × 8 HD-piksler.

205 viser Max opp ned. 47 celler er vertikale vendinger av nye donorutklipp, og to smålag kopieres uten vending. Alle 49 transformasjonene er bevist med original RGB og ny RGBA. Åtte ruter er sju egne motiver, der 258 og 295 deler samme kilde og nye komponent. Cel257 bruker kompatibelt nytt donorhode med et generert munnkantfelt på 6 × 4 piksler. Alle 24 endrede RGBA-piksler, inkludert ni alfaendringer, ligger inne i dette feltet. Øyedekkingen med smålag385 er kontrollert i sammensettingen. Cel267 bruker den munnrettede395-komponenten før vertikal vending.

## Rettede tidligere ark

Tre kildeutsnitt, 395/402/418, hadde fått rødt i nye munnfelter som er svart/hvite i originalen. Nye lokale imagegen-felter er satt inn i seks forekomster på fire ark. Bare RGB i seks avgrensede rektangler er endret; alfa og alle øvrige atlaspiksler er identiske med førversjonen. Historiske donorbytes og gamle notater er bevart i `root-donorarkiv.json` og de tilhørende arkivfilene. B/C sine kvitteringer beskriver donorstatus ved pakking, og roots validator bruker arkivet når den sammenlikner gamle SHA-verdier.

## Verifisering og grenser

Root har sett hele325, relative sammensettinger, alle205 detaljark fra tidligere kontroll og oppdatert205-sammensetting etter257-retting. 90 nye ruter er kontrollert mot faktisk resultat, komponent, kilde, metadata og atlasgrenser. 36 beskyttede jobbfiler og fire kontekstfiler er uendret. Alle ni faktisk leverte filer har hver sin ferske kontrollrapport. Råbilder, faktisk sendte prompter, lokalbevis og SHA-spor ligger i rapportmappen.

Godkjent pilotstil videreføres. Glattere/rundere konturer og tydeligere tenner enn pikselkilden består; enkelte205-hodekonturer gir små mellomrom ved halsen med kildens uendrede rel. 288/291 er lysere i den nye tegningen, dokumentert i agentnotatene. Dette er grafikkleveranse til repoet. Ingen motorimport, spilltest eller ny individuell brukergodkjenning er påstått.

Arbeidet fortsetter med Sam272 og deretter Sam091/Max066. Max066s rasp med tilknyttet toalettnøkkel er kildeavklart fra LucasArts-hintboken i bestilling56.
