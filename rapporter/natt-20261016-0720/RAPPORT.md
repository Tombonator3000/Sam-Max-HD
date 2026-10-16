# Fire grafikkleveranser

Dato: 2026-10-16T07:36:18.845355+02:00

Levert: fig116_05, fig116_06, fig116_07 og fig116_08. Fire ark og 27 ruter. Fire ark er statisk visuelt kontrollert. Null er importert, null er motoravspilt og ingen er godkjent av Tom i denne økten.

Alle 27 ruter består den uendrede egenkontrollen. Hvert ark har resultat.png, notat.md, rutekart, kontrollutskrift og SHA-256 under leveranser i fremdrift.json. Hele lerretet er 1536 x 1024 med ekte alfa. Beskyttede jobbfiler er bytekontrollert mot HEAD og er uendret.

Kostyme116 viser Sam ved alligatorene i Gator Golf, rom25. Originalene og hovedark/sam.png styrer identitet, drakt, stilling og strek. Front, profil og bakfra-stillinger er bevart. Fig116_05 og fig116_06 har ingen alligatordeler. Fig116_07 har fire alligatorstillinger og fig116_08 har fem. Delene er nytegnet etter riktig originalpalett med ett profiløye, lave grønne ryggformer og blå vannkant. De små adskilte blå kildeprikkene er bevart uten å forstørre Sam. Alligatorrettingen har en egen kildesamling av de delene som faktisk er synlige gjennom originalanimasjonen. Ingen originalpikselkunst brukes i produksjonsfilene.

Sju kall til bildeverktøyet: fire helark, to forsøk på små alligatorfragmenter og ett på hode og sammenhengende rygg. Første småfragmentforsøk er forkastet fordi det beholdt de firkantede pikselblokkene. De valgte nytegningene er renset og plassert presist med Python etter Toms tillatelse. Ingen pipelinekode er endret. Endelig grafikk og fotkontakt er sammenlignet statisk mot originalen, også på grå bakgrunn. Timing og motorvisning gjenstår.

Lag083_01 til 04 står først i ordren, men kravet om godkjent rom083 er ikke oppfylt. Rommet står til sjekk i status.csv. ANALYSE dokumenterer at lagerrommets palett og skybeskrivelse er feil for objektene som brukes i rom54. Objekt835 avventer dessuten motivavklaring. Lagjobbene er derfor hoppet over, og de neste fire avklarte jobbene er tatt i ordensrekkefølge.

Returen for fig247_02 var allerede rettet i leveransen fra 06:18 og er ikke gjentatt. Fig091_03 til 05 og kontrollen av PR32 er ikke gjentatt.

Git pull ble forsøkt. Sandkassen kan ikke skrive FETCH_HEAD i Git-metadataene utenfor arbeidsmappen. Grenen er fortsatt gpt-arbeid. Ingen commit, push, grenbytte, PR eller fletting er gjort. Nattverktøyet kan ta med resultat.png, notat.md og denne rapportmappen.

Systemets python3 mangler numpy. Prosjektets eksisterende Python-miljø kjører samme kontrollskript uten installasjon. Den eksterne henten av remake-skillen feilet; lokal kopi i /home/tom/Sam-Max-HD/docs/skills/scumm-hd-remake/SKILL.md er lest.
