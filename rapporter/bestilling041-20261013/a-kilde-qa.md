# Samlet kilde- og leveransekontroll 41/42

19 bilder er klare for rotens mottakskontroll. Uendret kontrollverktøy gir 19 OK; alle 37 metadatafelt er også målt eksplisitt i manifestene. Dette er teknisk og visuell egenkontroll, ikke runtime, import eller ny individuell brukergodkjenning.

Alle 92 låste kilde- og grunnromsfiler er uendret, dokumentert i a-kildehashkontroll.json. Råbilder, separate kildepresiseringer etter ordrett jobbprompt og oppskrifter er bevart. 22 faktiske innebygde imagegen-kall er fordelt med 12 i 41 og 10 i 42. Eksakt modellnavn er ikke eksponert.

## VR-rommet og kablene

Tom valgte uttrykkelig «Bruk presis vektorrekonstruksjon for VR-rommet». Rot har bekreftet at lag049_01, samme rom uten sverd, omfattes av denne beslutningen. a-lag049_01-metodevalg.json peker på den opprinnelige beslutningen. Valgt resultat er native SVG med kildens 40 farger, delte grensekjeder og RDP 0,8, rendret med samplesenter, halvåpne intervaller og even-odd-regel. Ingen bitmap eller gradient er innebygd. Hele motivet er rekonstruert; bakgrunnsbyteidentitet mot gammel rom049-PNG påstås ikke. Tre imagegen-forsøk er bevart, men ikke valgt. De historiske a-049-fargeqa.png og fargeforsøkene viser derfor ikke valgt lag049_01. Gjeldende bilder finnes i a-slutt-fullsceneqa og a-slutt-objektqa.

Lag049_02 beholder sverdet og grunnrommet. Det nye hjertet har egen kilderotasjon. Bare genererte røde piksler ble isolert og forenklet til kildens to rødfarger med dokumentert RGB-kriterium i a-049-farge-og-felt.py.txt. Ingen originalmaske ble brukt. Kanten er mer avrundet enn vektorvarianten; begge følger sine egne kilder, men har ulik detaljbehandling.

050-kablene beholder egne farger, tilkoblinger og bare/tilkoblede ender. Røde skjermfelt har riktige egne plasseringer. Feltunionen ble utvidet åtte HD-piksler og blandet fire piksler innover for å unngå rester og skjøter. Konturen er mer malt og avrundet enn originalens trappetrinn.

## Hele 052-familien

01 og 02 har hver sin 1920 × 800 master, klipp x=0/384 og byte-identisk 1152-pikslers overlapp. a-overlapp-sluttbevis.json bekrefter begge. Alle samtidige objekter fra begge kildehalvdeler er inkludert.

Kildeplanens gamle omtale av 480_01 som lukket dør var for grov. Riktig motiv har forskjøvne, skrå blad og synlig midtsone. Dette er rettet med et eget genereringsforsøk; telefonboksens innvendige grå former er også bevart. Ingen symmetrisk normalisering av dørene. 02 har sin egen åpne inngang. 03 og 12 fikk nye øyeforsøk som bevarer smale lukkede lokk uten rund pupil. Felt 489 har bare 107 endrede kildepiksler, felt 488 bare 12; begge er kontrollert som egne felt. 04 fjerner fuglen, men beholder pinnen. Øvrige tilstander arver riktig grunninngang og telefonboks.

05 til 10 har hver sin nytegning av grå/grønne snutefelt. Små kontur- og toneforskjeller er bevart som ulike kandidater, med glattere malte flater. De er ikke påstått pikselidentiske oppskaleringer eller runtime-verifisert animasjonsrekkefølge. 11 har eget fotfelt. Ingen nye tenner eller tunge er lagt inn.

Se [manifest 41](a-leveranser.json), [manifest 42](../bestilling042-20261013/a-leveranser.json), a-slutt-fullsceneqa-1.png til -4.png og a-slutt-objektqa-1.png til -7.png. Disse viser alle 19 fullscener og 37 faktiske metadatafelt, original ved siden av HD.
