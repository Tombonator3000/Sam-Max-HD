# Bestilling 16 A: kilder og samlet visuell kontroll

Fire leveranser: obj649_01, obj650_01, obj668_01 og obj669_01. GRUNNLAG.md, root-kildeplan.md, metadata, originale 1x-bilder, 4x-referanser og ordrette promptfiler er lest før produksjon. Begge intakte skilt ble sammenlignet før tegning. Kildenavn fra objektregisteret er surf-sign, surf-sign-left, surfin-start-line og surfin-finish-line. Ressursnavnene beviser ikke runtime-rekkefølge eller nøkkelfargebehandling.

## Identitet og antall

649 har tom grønn tavle med lys grønn kant, to synlige vertikale støtter ved venstre og høyre side, øvre/nedre skinne, ett synlig skråstag i høyre åpne felt og fem nedre avrundede fester ved tavlen. Dette er bevart. Ingen ny tekst, tall, pil eller Score er lagt inn. Oransje/gult felt er avklipt langs venstre ytterkant som i originalen.

650 viser metallbakside/fagverk uten grønn tavle: seks vertikale støtter definerer fem åpne felt, med fem skråstag fra øvre venstre mot nedre høyre, og to lange horisontale skinner. Venstre ytterstolpe fortsetter under nedre skinne. Antall og retninger er bevart, uten speiling eller ny plate. Samme avklipte oransje/gule venstrefelt er bevart.

668 og 669 er lave banemarkeringer på svart, ikke skilt eller målbuene. STARTING LINE og FINISH LINE er visuelt lest bokstav for bokstav i nye bilder og originaler. Gul overlinje, store mellomrom og flat skråstilt bokstavform er beholdt. Ingen stolper, biler, ruteflagg eller asfalt er lagt til. Motivfeltet er nøyaktig 1184 × 64 ved (176,480).

## Verktøy og geometri

Én generering per jobb med innebygd ChatGPT-bildegenerator. Eksakt modellnavn er ikke eksponert. Originalprompt er lagret ordrett med separat kildepresisering. Godkjent stil/rom007_del1av2.png er brukt som referanse for malt kvalitet, ikke innhold. Romnotens HUD, Score og biler er eksplisitt utelukket fra 649/650.

Råbilder og produksjonsprompter er bevart som a-JOBB-raa.png og a-JOBB-prompt.txt. Hele genererte motivrektangler er beskåret og skalert til metadatafeltet med LANCZOS og plassert på nytt lerret med eksakt RGB (128,128,128) padding. 649/650 har 800 × 352 ved (368,336); 668/669 har 1184 × 64 ved (176,480). Ingen originalmasker, vektortrace, warp eller lokale konturforskyvninger. a-oppskrift.py.txt rekonstruerer fra råbildene og sammenligner byteverdier med resultatene.

| Jobb | Uendret egenkontroll | Global / blokk / kant |
| --- | --- | --- |
| obj649_01 | SJEKK | 0,07 / 1,01 / 0,98 |
| obj650_01 | SJEKK | 0,65 / 1,30 / 0,84 |
| obj668_01 | SJEKK | 0,13 / 1,23 / 0,94 |
| obj669_01 | OK | 0,11 / 0,18 / 0,99 |

## Begrensninger

De tre SJEKK-resultatene er ikke merket OK. 649 har glattere, rundere kant og fester; originalens lille mørke hakk i høyre tavlekant er ikke gjengitt identisk. 650 har rundere metallprofil og tydeligere høylys, med mørkere åpne felt enn originalens svake grålilla trekantskygger. De seks støttene og fem diagonalene er kontrollert, men alle tverrsnitt og lokale konturer er ikke identiske. 668 sine bokstaver er litt glattere og høyere i noen partier, og SJEKK reflekterer lokal formforskjell. 669 har riktig lesbar tekst og teknisk OK; dette betyr heller ikke pikselidentisk typografi.

[a-samlet-qa.png](a-samlet-qa.png) er sett med original og HD ved siden av hverandre. [a-leveranser.json](a-leveranser.json) inneholder slutt-SHA256, rå-SHA256, utsnitt og kontrollfil. [a-kildebevis.json](a-kildebevis.json) verifiserer alle 40 låste kilder uendret. Metadataenes historiske prompt-hashavvik er ikke endret.

Ingen motorimport, bygg, Highway Surfing-komposisjon, faktisk timing eller runtime er testet. Ingen ny individuell brukergodkjenning er påstått. Parent håndterer samlet batch, kø og Git.
