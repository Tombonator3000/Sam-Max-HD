# Kilde-QA for bestilling 19 A

Tre leveranser er fremstilt med innebygd imagegen. Eksakt modellnavn er ikke eksponert. Originalprompter er lagret ordrett, fulgt av separat kildepresisering. Godkjent stil/rom007_del1av2.png er penselreferanse; originalenes motiv, palett og geometri har prioritet.

## Identitet og orientering

Kildegrunnlag: jobb.json, original_1x.png og referanse.png for rom079-delene og obj819_01; c-kildeplan.md og GRUNNLAG.md; sammensatt original rom079-original-full.png. Den lesevendte kildeanalysen bekrefter 180 graders rotasjon av venstre kule. Den gamle promptens «mirrored» er feil og overstyrt eksplisitt. Ingen ekstra speiling er utført.

Begge romkuler beholder brune fingre, grå mansjett, mørk frakk, blå/svart skjev sokkel, rød/oransje innside, tre spisse svarte trær med gule kanter, skjev bygning og hvite glassreflekser. Ingen snø, vinterlandskap, kork eller separate håndressurser er lagt til. Høyre kule er rettvendt. De store gule ordene THE MYSTERY VORTEX er kontrollert i begge orienteringer.

Den lille røde kursive teksten tolkes som Enjoy ut fra kildeglyfene. Første generering gjorde denne forløperen utydelig. Et smalt imagegen-forsøk rettet lesbarheten i alle tre avbildninger. Dette er ny håndtegnet bokstavtolkning, ikke påstand om bokstavidentiske former. De røde bokstavene og deres presise kildeform bør fortsatt inngå i rotens visuelle mottak.

## Egen variant

Obj819 har egen cyan/blå bølgebakgrunn. Kildeplanens sammenligning påviser 27 807 ulike originalpiksler mot venstre romfelt. Den er derfor generert fra sin egen referanse og ikke klippet fra rommaster. Kuleidentitet, hånd, tre trær, bygning og opp-ned-retning er visuelt sammenlignet samlet. Bølgebåndene har mykere overganger i HD; lavoppløselige fargebånd er ikke kopiert inn.

## Råbilder og behandling

Rommaster: a-master-raa01.png, opprinnelig 1983 × 793, helskalert med Lanczos til 2560 × 1024 og klippet [0,112,2560,912]. Dette er ren skalering av nytegningen. a-fullmaster01.png bevarer før-etikettbildet.

Etikettforsøket a-master-etikett-raa02.png har hvit topp/bunn. Klipp [0,23,2171,701], helskalering til 2560 × 800. Kun rektanglene [828,90,981,284] og [1586,520,1720,690] er kopiert til den første nytegnede masteren. Rektanglene omfatter litt tilgrensende sokkel og bokstavkant. Ingen originalpiksler eller konturmasker brukes. Resten av masteren er byte-identisk før/etter.

Objektets a-obj819_01-raa01.png har riktig 1536 × 1024. Motivfeltet [128,112,1408,912] ble rotert 180 grader kun for lesbar etikettredigering. a-obj819-etikett-raa02.png ble helskalert til 1280 × 800; rektangel [298,524,439,695] ble kopiert til den nytegnede varianten. Deretter ble hele motivfeltet rotert tilbake 180 grader. Utenfor etikettboksen er den første nytegningen byte-identisk. Analysebilder er tydelig navngitt og er ikke leveranseorientering.

a-oppskrift.py.txt gjenskaper resultater, kildebevis, manifest, kontrollfiler og samlet QA fra råfilene. Alle koordinater over er x1,y1,x2,y2 med eksklusiv høyre/nedre kant. Ingen lokal warp, originalsilhuettmaskering, terskelendring eller originalgrafikk i HD-utdata.

## Kontroll og begrensning

Rom079 leveres fra én 2560 × 800 master, klipp x0 og x1024. Overlapp 512 × 800 har null ulike piksler. Alle resultater er 1536 × 1024 med eksakt nøytral RGB128-padding. 40 av 40 beskyttede kildefiler har uendret SHA256.

Uendret sjekk_leveranse.py gir to OK for romparet og SJEKK for obj819. Obj819 har liten lokal korrelasjonsforskyvning, rapportert i egen kontrollfil, ikke skjult eller omklassifisert til OK. Ingen FEIL i disse tre sluttresultatene. Samlet motiv-/tekst-/orienteringskontroll er utført på a-samlet-qa.png og de lesevendte tekstnærbildene.

Dette er produksjonsleveranser klare for rotens mottak, med synlig SJEKK-forbehold. Ingen runtime, skripttiming, palettrotasjon, transparens eller motorkomposisjon er testet. Ingen ny individuell brukergodkjenning påstås.

- [Samlet original og HD](a-samlet-qa.png)
- [Manifest og hashes](a-leveranser.json)
- [Kilde- og bytebevis](a-kildebevis.json)
- [Reproduserbar oppskrift](a-oppskrift.py.txt)
