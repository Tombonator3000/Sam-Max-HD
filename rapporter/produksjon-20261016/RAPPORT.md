# HD-produksjon 2026-10-16T12:57:09+02:00

Fem nye Sam-ark i kostyme249, 32 ruter, og rettet munndel i fig249_02. Innebygd image_gen brukt, 11 bildekall. Kilder: ORDRE.md fra 08:44, ANALYSE.md, GJENNOMGANG.md, originale jobbfiler og godkjent hovedark/sam.png. Ingen ukjent figur eller gjenstand krevde nytt walkthrough-oppslag. Lag083 er fortsatt avhengig av godkjent rom083 og er ikke omtegnet.

## Leveranser og kontroll

- fig249_02: bare munndelen rettet. Egenkontroll OK. Alle seks gangruter byteidentiske med godkjent HEAD utenfor munnvinduet. Direkte omrissdekning 0,9034, snitt/union 0,8833. Ny SHA trenger mottak; tidligere godkjenning gjelder forrige bilde.
- fig249_04: fem nye ruter, egenkontroll OK.
- fig249_05: fem nye ruter, SJEKK på 153, 155 og 156. Glød fjernet med et smalt bildekall, kontrollert på grå bakgrunn. Størrelse/plassering innenfor kontrollen; omriss må vurderes.
- fig249_06: elleve nye ruter, SJEKK på 167 til 169. Den rene første komposisjonen beholdes. Nyere delingsforsøk ga kantrester og er forkastet. Kroppene i kildeidentiske faser må vurderes for flimmer i mottaket.
- fig249_07: seks nye ruter, SJEKK på 171 til 174. Den rene første komposisjonen beholdes, uten de mislykkede delingsforsøkene. Dråpeformer og omriss må kontrolleres nærmere.
- fig249_08: fem nye ruter, SJEKK på alle fem, snitt/union rundt 0,72 til 0,73. Samme nytegnede kropp brukt for de fem kildeidentiske kroppene. Små røde deler er plassert separat fra originale posisjoner med generert dråpe/dam. Ikke godkjent som ferdig animasjon.

To ark OK og fire SJEKK, ingen FEIL i endelig egenkontroll. SJEKK betyr åpne merknader, ikke ferdiggodkjenning. Ingen ny import, hd-mod, utgivelse eller motoravspilling. Tom har ikke godkjent de nye SHA-ene. status.csv og ORDRE.md er overlatt til mottaket.

## Sporbarhet

Endelige filer er jobber/fig249_02/resultat.png og jobber/fig249_04 til fig249_08/resultat.png. Fremdrift og rutekart er skrevet fra faktiske sluttfiler og alfa over128. De 24 beskyttede jobbfiler er bytekontrollert mot HEAD. Prompter er bevart her; grunnpromptene er uendret i jobbmappene. Notatene skiller kontroll, godkjenning og import.

klargjor.py beskriver første plassering; deler.py og siste-deler.py er bevarte mellomforsøk og skal ikke kjøres som sluttproduksjon. slutt.py setter sammen den valgte sluttgruppen fra rene kandidater. Forkastede forsøk skal aldri brukes som stilankere. De rå bildefilene har ofte farge i helt gjennomsiktige piksler, og derfor er visuell kontroll gjort etter alfakomposisjon på grått.
