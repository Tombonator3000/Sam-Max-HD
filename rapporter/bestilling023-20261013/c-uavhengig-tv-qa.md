# Uavhengig TV-QA – tidlig kontroll og etterkontroll

B arbeider fortsatt med kandidatfamilien. Dette er en tidlig read-only vurdering av b-tv-kandidat02.png og b-tv-raa03.png mot b-tv-objektkontaktark.png og c-mikro-kildegrunnlag.png. Filene i jobbmappene er ikke erklært sluttkandidater. Ingen bilder er endret av C.

Tredje atlas er et bedre utgangspunkt enn andre: flatere profilformer og rektangulært nederste betjeningsfelt. Andre atlas har tre runde betjeningsformer, mens kilden har to rundere/ovale og ett nederste mørkt rektangulært felt. Vurderingen er ikke en godkjenning av alle tredjeatlasets tilstander.

Konkrete funn sendt til B:

- Tilstand 05 i tredje atlas, øverst til høyre: den lille separate lyse utstikkeren under den lange profilens midtre munnfelt ser ut til å mangle. Original05 har et slikt lite hvitt/lyst felt under hovedformen.
- Tilstand 08, midterste rad til høyre: den nedoverrettede formen er stor og hvit; original08 har hovedsakelig lys beige/oransje nederst. Kontroller både fargefordeling og den faktiske 07→08-endringen.
- 0A/0B, nederste rad midt/høyre: venstre figur har langstrakt svart munn i begge nytegningene. Original0B har et kortere, høyere svart merke enn0A. Øyeendringen i høyre profil er synlig, men erstatter ikke munnendringen.
- 04/09 inneholder tilfeldige tilleggsforskjeller. Originalens eneste forskjell er svart→rosa ved romkoordinat (150,100). B har varslet en lokal korrigering med felles øvrig komponent.

Kildens venstre øyne er små mørke punkt-/kantformer; store runde øyne i andre atlas normaliserer dem for mye. Tredje atlas ligger nærmere med enkle mørke former. Ingen figur-/filmidentitet er bevist eller navngitt.

Sluttkontroll skal utføres på B sine uttrykkelig valgte filer når manifest/notater er klare. Den omfatter alle ni TV-tilstander, indikator076 bare i lag03, bytebevart riktig grunnrom utenfor de autoriserte feltene, konkrete mikrobokser og hash. Checker-OK alene godkjenner ikke disse små tilstandene. Runtime og ny individuell brukergodkjenning er uverifisert.

## Sluttkontroll av valgt familie etter rettinger

B sitt sluttmanifest er nå lest og alle ni resultat-SHA kontrollert mot filene. De gjennomgåtte kandidatene er gjenfinnbare i c-tv-kandidathash.json. c-tv-kandidat-mikro.png dokumenterer kilde/HD-utsnittene før den aller siste øyeklipprettingen; c-0B-oeye-etter.png viser siste retting. De tidligere funnene over er beholdt som sporbar historikk.

Tilstand03 har utstrakt hvit munnlinje og det mørke nedre feltet.04 har den kompakte hvit/røde formen.05 har nå det lille nedre lyse feltet som manglet i første tredjeatlas.06 og07 bevarer de forskjellige nedre lyse/mørke feltene i den lange profilen.08 har nå beige nedre form i stedet for det store hvite feltet. Profilene er fortsatt mer avrundede og enkelte mørke/lyse felt større enn originalpiksler; dette er konkrete tegningsforbehold, ikke en påstand om pikselidentisk rekonstruksjon.

04→09: svart munnmerke i venstre figur er borte og erstattet med varm hud/rosa farge i09, som kildens ene endring ved (150,100). Nykomposisjonene er byteidentiske utenfor den lokale boksen [598,507,10,11]; 110 HD-piksler endres. Dette er en kildebasert nytegnet lokal tilstand, ikke oppskalering av originalens ene piksel. At feltet er større enn4×4 er oppgitt; den faktiske motivendringen er visuelt bekreftet.

0A→0B: høyre øye blir brun horisontal markering og venstre munn blir kortere/løftet. C fant først en svart restprikk på x636..639,y495..496 som lå akkurat nedenfor B sitt for korte innfellingsrektangel. B utvidet klippet av den allerede genererte korreksjonen, uten nygenerering. Etterkontroll viser nå brune/hudtoner på samtlige tidligere svarte punkter (blant annet rundt RGB123,51,31 og166,94,54), ingen gjenværende svart prikk der. Samlet endres412HD-piksler mellom0A/0B i de to dokumenterte lokale feltene. De to variantene er ikke deduplisert.

076-indikator: lag03 har det lysere grønne feltet; lag04 og de senere lagene har det mørkere grunnromsfeltet. c-indikator-hd.png viser forskjellen. Lyset er jevnere og noe mer lysende enn originalens trinnvise grønnflater; ingen ny apparatfunksjon hevdes. Rødt telefonrør og vanlig vindusstilling følger riktig rom007-grunnanker.

Separat bytekontroll av alle ni fullbilder fant null endringer mot godkjent rom007-del1 utenfor TV-boksen, med076-boksen som eneste ekstra tillatte felt i lag03. Dermed er øvrige telefon-/vindutilstander, mørke tomrom og bakgrunn korrekt gjenbrukt; lag02 sin feilaktige bakgrunn er ikke brukt. B dokumenterer10/10 faktiske perobjektkontroller og alle ni uendrede checkerutfall erOK. Teknisk kontroll erstatter ikke detaljfunnene over.

Ingen gjenværende avgjørende tilstandsforveksling funnet etter rettingen. Familien er klar for roots mottaksvurdering med de oppgitte form-/lysforbeholdene. Det er ikke verifisert import, runtime, faktisk avspillingstiming eller ny individuell brukergodkjenning. C har ikke endret noen jobbilder eller B-filer.
