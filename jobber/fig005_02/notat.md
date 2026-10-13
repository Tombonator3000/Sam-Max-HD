# fig005_02

23 ruter levert som ekte RGBA med transparent bakgrunn/padding. Kildeidentiske ruter gjenbrukt fra mottatt Max003, med egne målmetadata og byteidentiske nye celutklipp inkludert alfamargin. Cel000 i00503 er egen nytegning med innebygd imagegen og lokal kinnretting. Ingen originalmaske eller lokal warp. Eksakt bildemodell er ikke eksponert.

SHA256: afcb5daa277562c4c8a9a5c5c1ea6b6323beef4f08917594b3a797dc42515e78

Uendret checker: OK. Se rapporter/bestilling054-20261013/a-celkart.json og a-kilde-qa.md for proveniens, individuelle bokser, øyelokk, rel og begrensninger. Runtime og ny individuell brukergodkjenning er ikke utført.

## Kildetro munnretting 2026-10-14

De kildeidentiske munnfeltene 418 er rettet med nye, lokalt genererte svart/hvite munnfelter fra bestilling 058. Originalen har ikke rødt i disse feltene. Bare RGB inne i de dokumenterte munnrektanglene er erstattet; all alfa og alle øvrige atlaspiksler er uendret. Førversjonen er bevart i `rapporter/bestilling058-20261013/root-fig005_02-for-munn.png`. Bevis: `rapporter/bestilling058-20261013/root-maxmunn-rettingbevis.json`.

Ny SHA-256: `9469c98ea53587212d81a28a011301ec56aba7dce29ee01dc504f89dec03b6ef`. Egenkontroll: OK. Ingen ny individuell brukergodkjenning, import eller runtime-test.
