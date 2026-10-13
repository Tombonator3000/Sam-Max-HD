# Kilde-QA, bestilling 12 A

Alle fire jobbers original_1x.png, referanse.png, jobb.json og prompt.txt er lest før generering. GRUNNLAG og root-kildeplan er lest. Godkjent stil/rom007_del1av2.png gir strek/pensel, mens originalpalett og motivtilstand styrer.

Rom054 er tomt boblebad med steinring, to separate sølvhåndtak, mørkt paviljongtak/gitter, livring, benk med rødt felt, planter og bakre basseng med fire søyler og rød sklie. Ingen personer, ekstra damp eller nye bobler.

Rom055 har fire oppreiste utskårne oransje påler. Deres fire individuelle relieffrekker og konturer er sett i 1x og 4x. Vi kjenner ikke sikre navn eller funksjoner for hver stiliserte utskjæring og legger ikke til tenner, ansikter eller tekst ut fra ikonassosiasjon. Tak, palmer, sklie og svarte forgrunnsblader beholdes.

Obj523_01 og obj524_01 er pool-totem-2/-3 i originalregisteret, men tilstand 01 viser avdekket bassengområde med grå flat baseplate. Ingen ny stående påle skal stå i midten. 523 viser grønn palmerefleks i vannet; 524 har brun/oransje og svart refleks og en avklipt pålekant til høyre. Den fargede vannformen i 524 tolkes som refleks fra kildens plassering og farger, ikke en bevist and, skapning eller båt. Interaksjonsmekanikk er ikke runtime-testet.

Overlapp i romkoordinater [152,8,8,152] er sammenlignet: 65 av 1216 piksler er ulike. De to tilstandene får derfor egne tegninger. Se a-overlappbevis.json. Ingen byteidentisk overlapp påstås.

Alle lerret er 1536 x 1024 RGB. Motivrektangler følger jobb.json, padding er nøyaktig 128. Ordinær presis samlet skalering/plassering er autorisert. Ingen originalsilhuettmaske eller lokal geometriwarp. Ordrett prompt er bevart med dokumenterte kildepresiseringer. Runtime, motorimport og ny individuell brukergodkjenning er false.

## Sluttkontroll

Tomt boblebad, to håndtak, fire bakre søyler, steinring, tak/gitter, livring, benk, sklie og planter er visuelt kontrollert. Ingen person eller ny damp.

Fire påler med individuelle utskjæringer, baser, tak/palmer, basseng, sklie og avklipte svarte blader er visuelt kontrollert. Ingen nye navn eller figurer.

Avdekket tilstand med to palmestammer, bakre takfragment, grønn vannrefleks, steinrand og grå flat baseplate. Ingen sentral stående påle. Første forsøk FEIL 1.57/1.55/0.80 ble avvist; andre gir OK 0.03/0.10/0.97.

Avdekket tilstand med sentralt tak, benk/gitter, brun/svart vannrefleks, steinrand og grå flat baseplate. Bare kildens avklipte pålekant til høyre. Ingen ny skapning eller påle i midten. OK 0.35/0.87/0.86.

Alle fire har teknisk OK og eksakt RGB 128-padding. Alle 40 låste kilder i kildehash.json er verifisert uendret i a-kildebevis.json. Sammenligning: a-samlet-qa.png. Resultater/hashes: a-leveranser.json. Råforsøk og presis samlet plassering finnes i a-prosessering.json og a-oppskrift.py.txt. Ingen byteidentisk overlapp mellom objekttilstandene påstås. Eksakt bildemodell er ikke eksponert. Runtime og individuell ny brukergodkjenning er fortsatt false.

De fire ekstra kildene i ekstra-kildehash.json er også verifisert. a-kildebevis.json omfatter dermed totalt 44 uendrede kilder.
