# Kontroll av PR 32 (Claude, 15. oktober 2026, natt)

PR 32 «Rett native inventarkort og glassmasker i HD-motoren» fra Codex, grenen `codex/hd-masker-inventory` (aeef1572 og flettingen 930ad41d). CI grønn (pipeline og nettleser). Ikke flettet og ikke rettet her; funnene er til Codex og Tom.

## Hvordan

- ScummVM ved `c9091321` hentet til en mappe i /tmp. Patchen fra main og patchen fra PR 32 lagt på hver sin kopi, begge gikk rent på. Kodeforskjellen mellom dem lest i sin helhet (4 filer: `base-costume.cpp`, `costume.cpp`, `dighd.cpp`, `dighd.h`, 316 linjer diff).
- Patchen i natt-grenen er byte for byte lik patchen i `origin/main`, så forskjellen er bare PR 32.
- Lest koden rundt: `loadImage`, objektbanen (`noteObject`), `blastSlot`, `noteCel`, `celImage`, `tintFactors`, fargetoningen i sammensetningen og `drawSoftObjectEdges`.
- Sjekket de 113 `objects/*_hd.png` i `mods/gpt`: alle har nøyaktig 4x størrelse uten marg, så alle blir tatt inn av den nye objektbanen. Inventarikonene (obj874 til obj894, obj995 til obj1086) er SMAP-objekter i rom 93 og 94, altså vanlige romobjekter, slik PR-en sier. obj049 er BOMP (blast) i rom 1.
- Ikke bygget og ikke kjørt: maskinen har ingen C++-kompilator (`configure` finner ingen), og ingenting er installert. `engine/test.sh` (nearest) og romtesten er derfor ikke kjørt med PR 32. Codex skriver selv at nearest ikke gir 0 avvik (kontoret 3193 med både gammel og ny motor).

## Funn

1. Felles buffer for blast og romobjekt (lav i dag, kan gi feil senere). `_objectImages` bruker samme nøkkel (objekt << 8 | tilstand) i `noteObject` og `blastSlot`. `blastSlot` laster `_hd.png` med `pad = true`, og da regnes ikke `softEdge` ut (bare når `pad` er av). Den nye objektbanen laster med `pad = false` og setter `soft` og `softEdge`. Tegnes samme objekt og tilstand først som blast og så som romobjekt i samme rom, får romobjektet `soft = true` men `softEdge = false`: `drawSoftObjectEdges` hopper over det, og alfaen i kortet vises som hel farge. Har filen marg, blir romobjektet i tillegg forskjøvet med `padX * 4`, siden sammensetningen leser `hd` uten marg. Ingen av dagens filer har marg, og ingen inventarikoner er BOMP, så dette treffer trolig ikke nå. Forslag: sett `softEdge` også i `blastSlot` når margen er 0, eller la `softEdge` følge av alfaen uansett `pad`.

2. Fargetoningen for myke romobjekter er nå ett snitt for hele bildet (`objectGain`), ikke per piksel (`tintFactors`). Det er bevisst (nøkkelfargekanter i inventaret), men har to følger som bør stå i `docs/HD-MOTOR.md`: en palettendring som bare gjelder noen få farger i objektet (et blink, en markering) spres som en svak toning over hele kortet; og en kanal der alle synlige originalpiksler er 0 får faktor 256 og blir ikke mørkere når bildet toner ut. `capped` er slått av for disse bildene, så svarte konturer kappes ikke lenger mot fargene rundt. Ved vanlig nedtoning til svart blir snittet 0, så det skal virke. Ikke sett i spillet.

3. Endret oppførsel for de myke kantene fra PR 29 (bilen i rom 9). Før ble rompikselen under kanten tonet med objektets snittfaktor; nå tones den med rommets egen faktor per piksel (`tintFactors` på romkoden). Det er trolig riktigere, men det endrer et godkjent resultat og står ikke i PR-teksten. Bilen i rom 9 bør ses i en nedtoning før fletting.

4. Patchen er ikke lenger felles med The Dig. AGENTS.md og logg 15. oktober sier at motorpatchen er byte for byte lik i begge repoer (Dig PR 57). PR 32 endrer `base-costume.cpp` (`recordCelPixel` kalles nå også for klassiske kostymer) og objektbanen. The Dig bruker AKOS og har ingen myke romobjekter, så det skal ikke endre noe der, men det er ikke kjørt (PR-en sier det samme). Enten tas samme endring inn i Dig, eller avviket noteres i `docs/HD-MOTOR.md`.

5. Små ting:
   - Diagnoserapporten for objekter (rundt linje 4864 i `dighd.cpp`) sjekker bare `objNNN_SS.png`, ikke `_hd.png`. Viser «no» for et objekt som bare har `_hd.png`. I dagens mod finnes begge, så det treffer ikke nå.
   - En `_hd.png` med marg gir nå en advarsel i objektbanen («is WxH, expected») før den faller tilbake til `objNNN_SS.png`. Én gang per rom og bilde, ufarlig.
   - `objectPaletteGain` hopper over den gjennomsiktige indeksen, men ikke piksler som er skjult av `_mask.png` (`opacity`). Påvirker bare snittet litt.

## Det som ser riktig ut

- `beginClassicCel` setter `_recordSlot = -1` først, så harde nearest-kostymer får den gamle koblingen etter dekoding, og `recordCelPixel` gjør ingenting for dem. `noteCel` med `precise` kalles før dekodingen, i samme rekkefølge som AKOS.
- `compData.sourceColumn` telles i den felles dekoderen (også ved klipping og skalering), så kildekolonnen er riktig også for klassiske kostymer.
- `digPaletteMask` settes for `_shadowMode & 0x20` og for farge 13 med skyggetabell, de to stedene klassiske kostymer leser fra skjermen. `shadowMode` brukes i `dighd.cpp` bare for kostymer uten `precise`, så klassisk 0x20 forveksles ikke med AKOS-modusene 1 og 3.
- `objectGain` bufres med `_palVersion`, som starter på 1 og økes hver gang `setPalette` endrer noe. `gainPal` starter på 0, så første kall regner alltid ut.
- Klippingen i `drawSoftObjectEdges` (r0 til r1, c0 til c1) bruker samme koordinater (`vs.xstart`, `vyOff`) som `drawSoftBlasts`, og HD-bildet uten marg dekker bare objektets rute.
- Søket etter objektlaget under (`below`) tar bare aktive objekter med lavere `seq`, i riktig tilstand og synlige på pikselen.

## Konklusjon

Ingen funn som stopper fletting av det som treffer dagens innhold. Funn 1 bør rettes eller noteres, og funn 3 bør ses i spillet. Tom avgjør flettingen.
