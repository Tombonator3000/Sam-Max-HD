# Produksjons-QA, bestilling 21 C

Alle 40 beskyttede kilder er uendret. Kildeplan/GRUNNLAG og faktisk referanse er brukt før generering.

## obj995_01

To source-only forsøk. Forsøk 1 hadde for blanke kanter og er bevart som avvist; forsøk 2 er mattere og valgt. Svak sentral emblem-/glyfstruktur er beholdt som uleselige fragmenter uten antatt ord/logo. Brune tomfelt og svart ytterområde beholdt. Fortsatt synlig restavvik: kantene og indre delingslinjer er mer modellerte/mørkt omrammede enn originalens femfargeflate. Kandidaten må vurderes visuelt av root; teknisk OK alene friskmelder ikke materialfølelsen.

## obj996_01

Avklippet UI-stripe med beige felter, svart mellomrom og delvis synlige symboler. Ingen komplette ikoner er lagt til utenfor utsnittet. Første forsøk manglet to svært svake brune fragmenter i et svart mellomrom. Forsøk 2 er lokal source-only imagegen med kilde-/HD-utsnitt; det nygenererte feltet ble helskalert og bare [544,528,104,32] innfelt. Alt utenfor rektangelet er byteidentisk med første kandidat. Fragmentene er ikke tolket som et nytt lesbart ord. De synlige blå/oransje ikonstrekene er renere enn originalpiksler, men uten nye felt.

## lag002_01

Ett imagegen-forsøk med lagoriginal og levert rom002-HD som bilde to. Hele rommet er nytegnet; grunnrommet er derfor IKKE byteidentisk utenfor objektene. Seks komponenter er kontrollert: lav mørk bilrutedel med oransje lys uten hel bil; lys nedrast stein; mørk stein ved pæren; lite oransje/gult panellys; limekrans ved blå kule; lilla krans ved grønn kule. Full opak RGB-romkompositt, ingen atlas/alfa/nøkkelfarge. Ingen objekter fra lag002_02..05. Nærbilder og tall er i c-seksobjekt-qa.png og c-seksobjekt-kontroll.json. Kransenes små tagger og steinenes bruddstreker er HD-tolkninger, ikke eksakt pikselidentisk detalj. Ekte lagkomposisjon/import/runtime er ikke testet.

## Seksobjektkontroll

Uendret checker har helbilde OK 0,03 / 0,09 / 0,97. Alle seks bokser er målt med checkerens egne compare/corr-funksjoner, uten endrede terskler. Kantkorrelasjoner 0,9792 / 0,9476 / 0,9804 / 0,8308 / 0,9521 / 0,9511 i metadatarekkefølge. Alle kildekantstandardavvik er over 1 og alle bokser minst 4 piksler: ingen av de seks ble hoppet over. c-seksobjekt-qa.png er faktisk kilde/HD-utsnitt fra eksakte bokser. Dette beviser plassering/kantlikhet, ikke runtime eller hver liten elektrisk tagg.

## Levering og begrensninger

Tre resultater og notater ligger i jobbene. Obj995 har klar_for_mottak=false grunnet konkret visuell material-/kontrastvurdering, til tross for teknisk OK. Obj996 og lag002 er kandidater klare for roots mottak med nevnte detaljforbehold. Ingen ny individuell godkjenning, import eller runtime hevdes. Hele lagrommet er nytegnet; bare UI-gaprettingen har byteidentisk omkringliggende motiv. Råfiler, eksakte prompter, førkandidater, kontroller og oppskrift er bevart.
