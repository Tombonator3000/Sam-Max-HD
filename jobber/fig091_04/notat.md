# Returleveranse fig091_04

Dato: 15. oktober 2026. Gren: gpt-arbeid.

Rettet costume091_1957, costume091_1958, costume091_1959, costume091_1960 og costume091_1961 etter ORDRE.md og forhandsvisning/myk_fig091_04.png. Det finnes ingen egen retur.md. Hele arket leveres som RGBA på 1536 x 1024 med ekte alfa. Costume091_1956 og alt utenfor de fem returrutenes områder er bevart pikselidentisk.

## Kilde og motiv

Jobbens original_1x.png og referanse.png er sett sammen med hovedark/sam.png og den returnerte forhåndsvisningen. ANALYSE.md, GJENNOMGANG.md og remake-skillen fra lokal main er lest. Figurregisteret i main, docs/figurer.csv, identifiserer kostyme 91 som Sam med blå eske med stjerne i rom 20, Trixies vogn. Romnotatet bekrefter stjernen på esken. Sam løfter lokket i denne animasjonen. Originalens palett, lokkvinkel, grep, avskårne kropp og separate brune fotrest er formgrunnlaget. Sams godkjente hovedark styrer identitet og tegnestil.

Originalene for 1958 til 1961 er pikselidentiske etter uttrekk av rutene, også fotresten. Samme nye tegning er derfor brukt i alle fire. Dette er kildeidentisk gjenbruk, ikke en forenkling av forskjellige positurer. Originalens nedbøyde hode og den lille horisontale mørke ansiktsåpningen er bevart. Ingen bein eller nedre kropp er føyd til.

## Verktøy og forsøk

Innebygd image_gen, tre bildeforsøk. Eksakt modellnavn er ikke eksponert. prompt.txt er brukt ordrett i alle tre kall med separat returpresisering. Første forsøk på hele arket flyttet og forstørret motivene og ble forkastet. Forsøk to tegnet den felles nedbøyde posituren fra originalutsnittet, med Sam-hovedarket som bilde to. Forsøk tre tegnet 1957 fra originalutsnittet med samme hovedark. Alle faktiske prompter og råbilder er bevart i rapporter/natt-fig091_04-20261015/.

Bildene er tegnet med bildeverktøyet. Python/Pillow er brukt til teknisk plassering av de nye komponentene i produksjonsarket: hoveddel og fotrest er beskåret etter den nye alfaen og skalert hver for seg med Lanczos til originalens komponentbokser. Alfa under 16 er nullstilt og resten normalisert fra 254 til 255. Ingen originalmaske eller lokal deformering er brukt. Oppskriften ligger i plassering.py.txt i rapportmappen.

## Kontroll

Uendret verktoy/sjekk_leveranse.py gir OK, 6 av 6 ruter OK. Systemets python3 mangler numpy, så kontrollen er kjørt med eksisterende Python 3.12 fra Codex-runtime. Ingen pakker er installert.

Fast omrissmåling, snitt delt på union, steg fra 0,8520 til 0,9279 i hver av rutene 1958 til 1961. For 1957 endret den seg fra 0,9598 til 0,9356. Den nye 1957 har altså noe lavere samlet omrissoverlapp enn førbildet, selv om den består egenkontrollen. Målingen gjelder hele rutens synlige deler, inkludert fotresten. Det er ikke en måling av figuridentitet eller Toms visuelle godkjenning.

Rutekart for alle seks ruter, fremdrift.json, sjekksum, kontrollutskrift og geometrimålinger ligger i rapportmappen. De fire beskyttede jobbfilene er kontrollert uendret med SHA256. Førbildet og forrige notat er bevart der.

SHA256 for resultat.png: b68183fdc6cbd471d5e273da0e425cf927cd7cb27760da9cb3a16bf077f81122.

Usikkerhet: Små ansiktsstreker, fingre og innvendige folder er fortsatt tegnetolkninger. Hender og fotrester har mykere kurver enn originalpikslene. Hele animasjonen er ikke avspilt i motoren, og import hos Claude og Toms visuelle vurdering gjenstår.

Git pull ble forsøkt, men sandkassen nektet skriving til FETCH_HEAD utenfor arbeidsmappen. Arbeidet bruker eksisterende lokal ordre. Ingen grenbytte, commit, push eller historikkendring er gjort. fig091_03 var allerede levert i forrige lokale commit og ble hoppet over. Denne økten leverer bare fig091_04.
