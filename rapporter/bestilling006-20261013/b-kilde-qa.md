# Kilde-QA for rom022 del2/del3 og rom028

Rom022-delene bruker felles master med del1 i bestilling005. Opprinnelig del3-SJEKK var lokalisert til høyre kolonne x2656..3168 i master. Originalkilde og eksisterende stil ble brukt til innebygd nytegning av utsnittet x2560..3168,y112..912. Dette fjernet geometriavviket uten lokalt deformasjonsfelt. En48 pikslers overgang mellom HD-kandidater fjerner synlig skjøt; ingen originalpiksler eller silhuettmasker brukes.

Masteren er nå låst til SHA007b7381ef3505d28d7aba4f27cf06aa14607c30c9ab71c8b7b4e5bcedf42af9. Del1 var byte-uendret etter rettingen. Hele x0..2559 var urørt, og dermed part2/3-overlappen. Del2/3 klippes ved x816/x1632. Begge720 piksler overlapp er kontrollert bytevis. Den endelige del3-kontrollen gir OK.

Hyssingmuseet er identifisert gjennom rommetadata og kildebildet. Store brune tråder er del av hyssingnøstet, ikke gardiner. Utstillingene, benkene, vinduet, avsperringen og tavlen er beholdt. Navn/funksjon på den lille gjenstanden under glass er ikke gjettet; den er beskrevet som den buede hyssingdelen kilden viser. Uleselig tavletekst er ikke gjort til nye ord.

Alle tre leveranser består uendret sjekk_leveranse.py. Tolv beskyttede kilder matcher hashlåsen. Råforsøk, prompter, mellomkontroll og oppskrifter er bevart. Ingen Git- eller kodeendringer. Runtime=false, nybildegodkjenning=false. Små detaljer og faktisk objekt-/animasjonsintegrasjon er ikke fullt verifisert.
