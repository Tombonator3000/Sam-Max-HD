# rom021_del2av2

Dato: 13. oktober 2026. Ett fullsceneforsøk med innebygd image_gen. Eksakt modellnavn er ikke eksponert.

## Kilde og motiv

To rosa, vingede cupidfigurer og én rød hornet djevel over den skjeve steinfasaden. TUNNEL OF LOVE er bevart med hjerte som O i LOVE. Begge trapper, rød plattform, huleåpninger, telt og forgrunn er kontrollert.

Kilden er beskyttet jobbmetadata og originalreferanse, lest med origin/main:docs/gpt-romnotater.csv. Alle originaldeler er sett før produksjon. Godkjent kontorbilde er kun stilstøtte. Originalprompter er bevart ordrett med avgrenset tillegg om fullscene, skilt, figurantall og identitet.

## Leveranse

Resultatet er1536x1024, scene [0,112,1536,800] og eksakt #808080 padding. Hele genererte panoramaet er normalisert med Lanczos til kildens fullsceneformat, uten lokal warp. Delene klippes fra én master. Rom021-overlapp1152 er byte-identisk.

Rom022-fullmasteren er3168x1024. Bare del1 er levert i denne bestillingen. Del2 og del3 SKAL senere klippes fra samme SHA-låste master med x816 og x1632, ingen ny uavhengig generering. Register og klippeoppskrift finnes i rapporten.

Referanse SHA-256: 415e3c5d01664211a07781de46df20eff2f9801b3f6a260aa085b20938d89103
Resultat SHA-256: eba5a9f18a42d5469247e7c31350e3714c26ca7e312bf6ebfd8b6fc44ed72010
Fullmaster SHA-256: 9df3e1e708d68d69e8c40348f1e7639086f20d5d8a331ea0318451679e2f77d7

Uendret sjekk_leveranse.py: OK. Kontrollutdata er bevart i rom021_del2av2-kontroll.txt. Tolv bestillingskilder og åtte ekstra kilder for rom022 del2/del3 er kontrollert uten avvik.

Visuell egenkontroll omfatter original/fullscene, tydelige skilt og hovedfigurenes roller, antall og posisjoner. Små finger-, fjær-, tann- og plakat-/kulissedetaljer er tolket fra lave pikselmengder og er ikke bevist detaljidentiske. Jevnere skygger og overflateform enn originalen er synlig. Kontroll av spillets animerte objekter oppå disse bakgrunnene gjenstår.

Runtime=false. Nybildegodkjenning=false. Ingen påstand om godkjent motorintegrasjon eller ny visuell godkjenning fra Tom.
