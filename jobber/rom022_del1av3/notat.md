# rom022_del1av3

Dato: 13. oktober 2026. To fullsceneforsøk med innebygd image_gen. Eksakt modellnavn er ikke eksponert.

## Kilde og motiv

Mørk Tunnel of Love-kulisse. Første del viser tre stablede CORN DOGS-kasser, grønn slangeaktig skapning og to mennesker i hulekulissen, samt blått skjelett med kost. Hele masteren bevarer også grønt monster med kvinne, HOT-skilt, rør/panel og slottsscenen med tre figurer. Ingen identitetsnavn er gjettet; figurene er dokumentert som visuelle roller i attraksjonskulissen.

Kilden er beskyttet jobbmetadata og originalreferanse, lest med origin/main:docs/gpt-romnotater.csv. Alle originaldeler er sett før produksjon. Godkjent kontorbilde er kun stilstøtte. Originalprompter er bevart ordrett med avgrenset tillegg om fullscene, skilt, figurantall og identitet.

## Leveranse

Resultatet er1536x1024, scene [0,112,1536,800] og eksakt #808080 padding. Hele genererte panoramaet er normalisert med Lanczos til kildens fullsceneformat, uten lokal warp. Delene klippes fra én master. Rom021-overlapp1152 er byte-identisk.

Rom022-fullmasteren er3168x1024. Bare del1 er levert i denne bestillingen. Del2 og del3 SKAL senere klippes fra samme SHA-låste master med x816 og x1632, ingen ny uavhengig generering. Register og klippeoppskrift finnes i rapporten.

Referanse SHA-256: 24c454fbf281b2fd21e0e883aeb018b7d8aee3129ff8cdc58faea925d3372cc8
Resultat SHA-256: 380c2f0b672de4f238005d51f77ef01066364e74b05565524f5e7bf73bcc3cfb
Fullmaster SHA-256: 007b7381ef3505d28d7aba4f27cf06aa14607c30c9ab71c8b7b4e5bcedf42af9

Uendret sjekk_leveranse.py: OK. Kontrollutdata er bevart i rom022_del1av3-kontroll.txt. Tolv bestillingskilder og åtte ekstra kilder for rom022 del2/del3 er kontrollert uten avvik.

Visuell egenkontroll omfatter original/fullscene, tydelige skilt og hovedfigurenes roller, antall og posisjoner. Små finger-, fjær-, tann- og plakat-/kulissedetaljer er tolket fra lave pikselmengder og er ikke bevist detaljidentiske. Jevnere skygger og overflateform enn originalen er synlig. Kontroll av spillets animerte objekter oppå disse bakgrunnene gjenstår.

Runtime=false. Nybildegodkjenning=false. Ingen påstand om godkjent motorintegrasjon eller ny visuell godkjenning fra Tom.

## Korrigering etter kontroll

Forsøk1 ga FEIL. Forsøk2 bevarte flate konturer bedre, men hadde systematisk horisontal kompresjon. Global plassering er derfor korrigert: motivet normaliseres fra3168x800 til3201x795 og plasseres ved x=-4,y=112 på3168x1024. Nederste fem motivpiksler fylles med svart som den tomme mørke bunnflaten. Ingen lokal warp eller originalkontur er brukt. Del1 er OK med blokk0,75/kantlikhet0,926. Fremtidig del2 er målt OK; del3 er SJEKK med blokk1,96/kantlikhet0,845. Disse to delene er ikke levert nå. Begge må skjæres fra den korrigerte masteren; del3 trenger særskilt kontroll før senere levering.

Oppdatert ved bestilling006: høyre felt x2560 til3168 er nytegnet fra original og skjøtt med48 piksler overgang mellom HD-kandidater. Del1 er byte-uendret. Del3 er nå OK; tidligere SJEKK er avklart. Se bestilling006 for råretting og kontroll. Masterhash over er oppdatert.
