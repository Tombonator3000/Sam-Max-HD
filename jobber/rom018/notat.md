# rom018

Dato: 13. oktober 2026. Ett innebygd image_gen-forsøk for dette rommet. Eksakt modellnavn er ikke eksponert.

## Kilde og innhold

Sam ved Wak-A-Rat. Hatt, snute, tunge på høyre kinn, dress og blåsvart slips følger originalen. Fem tomme svarte hull i brettet og tomt svart tellefelt er bevart. HIT 20 WIN og begge stjernene er kontrollert. Bokstekst på kassens front beholder avskjæringen i originalen.

Kilde: beskyttet jobbmetadata og originalreferanse, lest sammen med origin/main:docs/gpt-romnotater.csv. Godkjent Sam-hovedark styrer identitet/strek for rom018, ikke positur, fargebytte eller nye detaljer. For rom017 er godkjent kontor kun stilstøtte. Originalpromptene er bevart ordrett med separat kildepresisering i rapportmappens rom018-prompt.txt.

## Leveranse og egenkontroll

Resultatet er 1536x1024 med eksakt grå padding. Rom017-delene er skåret fra én 2528x1024-master etter global Lanczos-normalisering fra 1971x798; ingen lokal warp er brukt. Overlapp på544 piksler er byte-identisk. Rom018 har originalformat1536x1024 og kun padding normalisert.

Uendret sjekk_leveranse.py: OK. Kontrollutdata i rom018-kontroll.txt. Tolv beskyttede kildefiler er kontrollert mot kildehash.json uten avvik.

Referanse SHA-256: 01f47726e6e7ca5b8827d74fb7ad009bed21d380899f0e835426e72a30dcda26
Resultat SHA-256: 3ab52bae1cd6b2837901eda9cdd98f7da869a5e92a0e05f2eaef4ed4760937de

Visuell egenkontroll omfatter motiv, hovedgeometri og skilt. Små gjerdespisser, blomster og teltflatedetaljer er nytegnet fra pikselklynger; eksakt detaljidentitet utover kontrollert hovedinnhold er ikke bevist. Bildene har jevnere skygger og noe mer overflateform enn originalen.

Runtime=false. Nybildegodkjenning=false. Motorintegrasjon, klikkflater, kostyme-/objektlag og Toms kontroll av disse nye bildene er ikke utført. Rom018 er egnet som samme roms relevante bakgrunnsreferanse for obj187-arbeidet, men dette dokumenterer ikke ferdig import.
