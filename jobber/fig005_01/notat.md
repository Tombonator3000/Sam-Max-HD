# fig005_01

28 ruter levert som ekte RGBA med transparent bakgrunn/padding. Kildeidentiske ruter gjenbrukt fra mottatt Max003, med egne målmetadata og byteidentiske nye celutklipp inkludert alfamargin. Cel000 i00503 er egen nytegning med innebygd imagegen og lokal kinnretting. Ingen originalmaske eller lokal warp. Eksakt bildemodell er ikke eksponert.

SHA256: 20f125fce533fe320a2a1715221c912a6128b218832de03586f6360db506551d

Uendret checker: OK. Se rapporter/bestilling054-20261013/a-celkart.json og a-kilde-qa.md for proveniens, individuelle bokser, øyelokk, rel og begrensninger. Runtime og ny individuell brukergodkjenning er ikke utført.

## Kildetro munnretting 2026-10-14

De kildeidentiske munnfeltene 395, 402 er rettet med nye, lokalt genererte svart/hvite munnfelter fra bestilling 058. Originalen har ikke rødt i disse feltene. Bare RGB inne i de dokumenterte munnrektanglene er erstattet; all alfa og alle øvrige atlaspiksler er uendret. Førversjonen er bevart i `rapporter/bestilling058-20261013/root-fig005_01-for-munn.png`. Bevis: `rapporter/bestilling058-20261013/root-maxmunn-rettingbevis.json`.

Ny SHA-256: `c3e080fc505c743a436e64c5a2e2bd1e7a9ccac0829011b8c6a82dc5dd4af70e`. Egenkontroll: OK. Ingen ny individuell brukergodkjenning, import eller runtime-test.
