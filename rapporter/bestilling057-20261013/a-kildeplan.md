# Sam272, seks ark før produksjon

Alle seks helark og 79 nærfelt er sett. 24 beskyttede jobbfiler er låst i a-kildehash.json. Ingen nytegning eller jobbfiler er endret. a-kildebevis.json beskriver hver rutes palett, rel, retning, lag og sammenlikning med Sam002. Ingen av de 79 synlige RGB-utklippene er identisk med en Sam002-rute. Familien inneholder 45 unike RGB-utklipp, med kildebeviste repetisjoner i a-familiebevis.json.

## Identitet og konkret kilde

Sam har brun pels, blågrå dress og hatt, hvit skjorte og mørk blå/svart stripet slips. Alle rutene er hele Sam i retning 1, lag 15. Dette er rekvisittoverleveringer ved boblebadet, ikke vanlige separate talehoder. Oppdeling i seks ark er ikke seks selvstendige animasjoner.

Den lagrede dekompileringen konsept/2026-10-12/kildebevis/rom_054/obj_0515_verb.txt knytter aktør 2 direkte til kostyme272 og konkrete gjenstandsgrener:

| Ark | Ruter | Synlig motiv og kildebevis |
|---|---:|---|
| 01 + 02 | 17 + 7 | Lys pute med grønne slyngformer. Registerets objekt428 heter bedroom-pillow. Skriptgrenen begynner ved 0B8C, kostyme272 ved 0CED, animasjon6 ved 0D08. Dialog ved 0E44 om hair tonic og ved 0E9D om å stjele puter. Metadata kaller eksportsekvensen animasjon1, så skriptets6 må ikke overskrive eksportmetadata. Ingen karttekst eller kontinent skal tegnes på puten. |
| 03 | 13 | Elfenbensfarget, bøyd dinosaurtann. Objekt571-gren fra056C, kostyme272 ved0685, animasjon7 ved0697. Dialog ved07D1 kaller den en genuine dinosaur tooth. Tannen tipper fra nedoverholdt til vannrett før fraværsrutene. |
| 04 | 20 | Lang lilla aubergineform med grønn stilk/blad og konkret profil. Objekt548-gren fra088C, kostyme272 ved09B9 og animasjon8 ved09D2. Dialog ved0AED sier combination of man and nature. Prosjektets konseptanalyse omtaler auberginer formet som Conroys hode, men akkurat548s personlikhet må spores mot tilhørende ikon før eventuell nytegning. Ikke gjør den til ordinær glatt aubergine eller legg til ansiktsdetaljer som ikke vises. |
| 05 + 06 | 19 + 3 | Oransje/gul håndholdt vortex med blå underkant, ikke mat eller skål. Objekt272-gren fra0121, kostyme272 ved024D, animasjon9 ved025F, eksplisitt hand-held vortex ved03F5. Bevar de små løse blå/gule punktene i forsvinningsrutene1993/1994. |

Dette er statisk primærkildeanalyse av lagret skript. Ingen runtime-avspilling er gjort. Tidsrekkefølge på tvers av eksportark skal ikke gjettes fra arknummer.

## Format og komponentfelle

Alle ark leveres senere med ekte RGBA på 1536 × 1024, ingen synlig magenta eller grå bakgrunn. Atlasplassering styres av hvert arks metadata, 4× synlig plassering med 64/32 HD-pikslers opprinnelse. Originalmetadata med rel_x, rel_y, kode, lag og move beholdes. Verdensorigin for et synlig utsnitt er rel + synlig_xy minus rekt_xy.

Cel1941 i fig272_02 er en viktig unntaksrute: synlig [200,4,323,74] er faktisk 123 piksler bred, fordi én separat beige kildepiksel finnes ved atlas(322,24), lokalt(122,20), RGB(179,147,119). Sam står i venstre del. Hele figurkroppen skal aldri skaleres til123 piksler bred. Kroppens egen komponent og det fjerne punktet må plasseres hver for seg fra ny art. Punktet er påvist i kilden og må ikke slettes som antatt støy. Ingen kildebasert silhuettmaske er tillatt.

## Produksjonsplan

Tegn et konsistent Sam-grunnmotiv etter godkjent hovedark, men bevar kildens egne kroppsholdninger, hodevinkler, håndgrep og rel-forskyvninger. Del de 45 unike formene i små semantiske grupper for pute, tann, lilla/grønn gjenstand og vortex. Bruk kun dokumentert identiske kilder til kopiering av nye komponenter. Ikke kopier bare like positurer som har andre munn-/hånd-/rekvisittpiksler.

Bevar putens fire hjørner og slyngmønster uten tekst, tannens bøyning og hvite base, lillaformens hakk/profil og stilk, samt vortexens blå kant og siste løse punktrester. Sam skal ikke få ekstra fingre eller ny hode-/hattstørrelse når rekvisitten forsvinner. Kildeark01/02 og05/06 må kontrolleres som sammenhengende familier.

Før produksjon: avklar548s konkrete ikonforbindelse. Resten har tilstrekkelig motivbevis i lagret primærkilde. Etter produksjon: uendret checker, alle79 felt i lik visuell størrelse, RGBA-/bakgrunnskontroll, separate komponent- og rel-ark, SHA/proveniens, kontroll av de små punktene. Teknisk OK er ikke motor-/runtimebevis.

## Tillegg: 548 er John Muir-formet squash, ikke Conroy

Den offisielle LucasArts-hintboken side35 skiller uttrykkelig mellom Bumpus-formet aubergine for parykktyveriet og Muir-formet squash for totem3. Kilde: https://www.mocagh.org/lucasfilm/sammax-hintbook.pdf, søkbart tekstutdrag fra gjenstandstabellen. Den lagrede548-grenen aktiverer state524/518 og omtaler kombinasjonen menneske/natur. Dette bekrefter at animasjon8 er overlevering av John Muir-formet squash. Side27 omtaler Bumpus-auberginen ved grønnsaksmuseet, som er et annet motiv.

a-548-ikon-kontekst.png sammenlikner originalene1037 og1042 med cel1964. 1042 har lang lys grå profil/skjegg og grønn topp, mens1037 har mørk hårtopp og rundere form. 548s konkrete håndholdte profil stemmer med den lange Muir-varianten og er i stor grad skjult bak Sams hånd. Dette er visuell sammenheng og primærkildebekreftet gjenstandsidentitet, ikke et påstått runtimebevis for inventar-ID til ikon-ID. Ingen ekstra ansiktstrekk skal hentes inn bak hånden. Den tidligere formuleringen om mulig Conroy-profil er dermed tilbakevist, ikke produksjonsgrunnlag.
