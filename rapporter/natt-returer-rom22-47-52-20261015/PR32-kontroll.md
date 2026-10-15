# Avgrenset kontroll av PR 32, 15. oktober 2026

Ingen kode er endret, duplisert eller flettet. gh pr view 32 ble forsøkt, men api.github.com var utilgjengelig fra sandkassen. Grønn CI er opplyst av Tom, ikke bekreftet på nytt. Git pull stoppet fordi Git-metadata utenfor arbeidskopien er skrivebeskyttet.

Lokal origin/codex/hd-masker-inventory peker på 930ad41d3dfd797cfa33c3458828324607d53f63. Motorendringen i engine/patches/0001-dighd-hd-grafikk.patch er lest mot lokal origin/main. Forrige detaljerte gjennomgang er bevart i ../natt-fire-returer-20261015/PR32-kontroll.md.

Konkrete observasjoner i denne økten:

1. beginClassicCel nullstiller _recordSlot før den søker mykt bilde. Harde bilder går videre til noteCel etter dekodingen. recordCelPixel kontrollerer slot og destinasjonsadresse før tabelltilgang.
2. Ved palettmaske lagres eldre tegnings seq, slot og code. Stakkede masker beholder tidligere pre-verdi. Det støtter at masken omfarger det som ligger under, også når underlaget er en figur.
3. Native romobjekter lastes fra objNNN_SS_hd.png før eldre fil. objectGain mellomlagres per _palVersion, med 0 i bildet og 1 som første palettversjon. Første bruk beregner derfor faktoren.
4. drawSoftObjectEdges avgrenser arbeidet til objektets skjermrektangel, med xstart, screenTop og topline. Bakgrunnskilden velges fra aktive eldre objekter med riktig tilstand og tegnerekkefølge. Et slikt underlags egen alfa blandes videre med rommet.
5. Objektets gain bruker 8 brøkbiter mens rommets tintFactors bruker 16. Den undersøkte blandingen bruker >>8 for objekt og >>16 for rom, og håndterer rommets negative spesialverdi.

Ingen ny konkret kodefeil er påvist innen dette avgrensede omfanget. Vilkårlig mange overlappende transparente objektlag, fade under avspilling, fart og faktisk spillvisning er ikke verifisert her. Ingen bygg eller skjerm-/lydtest er kjørt i denne grafikkøkten. Dette er ikke en flettingsgodkjenning. PR 32 er urørt, og fig091_03 til 05 er ikke tegnet om.
