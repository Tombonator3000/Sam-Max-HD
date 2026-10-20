# Kildekontroll av falske kostymeruter

Analyse av alle 348 COST-ressurser i denne spillutgaven, uten kode- eller spilldataendring. Minstehypotesen er å avvise ikke-null animasjonspekere lavere enn data_offsets + num_anim * 2, altså inn i header/tabell. Inklusiv animasjonsiterasjon beholdes, slik ScummVMs låste ClassicCostumeLoader bruker `anim > _numAnim`. Ingen global endring av numAnim er gjort.

256 ressurser har et slikt lavt ekstra oppslag. Bare animasjonskoblinger fra disse oppslagene holdes utenfor i analysen. Antall unike celtargets går fra 16206 til 15838, en forskjell på 368. Ingen av de 368 rutene som bare kom fra slike oppslag, overlapper de 2418 publiserte native-rutene. Alle publiserte native og beskyttede originaler er urørt. De kjente 344/raw32 -> 3 og 346/raw36 -> 7 er inkludert; også 341/raw56 -> 7. Det nylig kildeklargjorte 342 har ekte raw5 -> 138, men ekstra raw32 -> 1. Den første bunken med ni gyldige 342-mål er uendret.

Dette er analyse og en avgrenset rettingshypotese, ikke en implementert eller godkjent katalogretting. Bibliotekskilden scumm-v6-kostymer-skygge-og-soppelruter er lest, og lokale primærkilder er pipeline/smhd/v6grafikk.py samt ScummVMs costume.cpp. Før kodeendring må det lages meningsfulle syntetiske regresjoner for både ekte siste animasjon og lav headerpeker, og gyldige ressurskoblinger må sammenlignes. Kode skal gå gjennom testet PR. Ingen kodearbeid er påbegynt i den gjenbrukbare PR34-arbeidsmappen.

Ikke regenerer eller slett eksisterende jobbfiler fra denne analysen, og ikke endre den historiske nevneren 1758 ennå. Klassifiser berørte jobber og returer etter en verifisert PR. Grafikkproduksjon kan fortsette med de kildebekreftede jobbene. Spillavledet bevis ligger bare på gpt-arbeid.
