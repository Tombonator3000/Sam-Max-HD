# HD-motoren for Sam & Max

Kort versjon for Sam & Max. Alle detaljer om hvordan motoren virker, innstillingene, testkrokene og hva som er testet i The Dig, står i The Dig sin [HD-MOTOR.md](https://github.com/Tombonator3000/Dig-HD-Remake/blob/main/docs/HD-MOTOR.md).

## Status

- Patchen `engine/patches/0001-dighd-hd-grafikk.patch` er byte for byte den samme som i The Dig HD Remake, mot ScummVM-commit `c9091321` (`engine/SCUMMVM_COMMIT`).
- Den er ikke aktiv for Sam & Max. `DigHD::create` i `engines/scumm/dighd.cpp` returnerer uten å lage noe når spillet ikke er `GID_DIG`. Sam & Max kjører derfor uten HD, også med `DIGHD_MOD` satt. Rettingen for Esc i patchen virker også uten DigHD (se under).
- Miljøvariablene `DIGHD_*`, nøklene `dighd_*` i scummvm.ini og mod-formatet beholdes.
- Bygget her 10. oktober med `engine/build.sh` og startet med Sam & Max uten skjerm: spillet kjører som originalen. Ingen HD, fordi DigHD ikke er på.

## Hva patchen gjør

Spillet kjører uendret i 320 x 200 og 256 farger, med skript, lagring og lyd som før. Bare det siste steget endres: når et område sendes til skjermen (`drawStripToScreen`), bygger DigHD det samme området i 4x og full farge. For hver piksel avgjøres kilden ut fra hva som står i 8-bitsbufferen:

| Det som står der | Kilde |
| --- | --- |
| Uendret rombakgrunn, lik bakgrunnsbufferen og lik indeksbildet `roomNNN_idx.png` | `rooms/roomNNN.png` |
| Et objekt som nettopp er tegnet, og som stemmer med indeksbildet | `objects/objNNN_SS.png` |
| En kostymerute | `costumes/costumeCCC_NNN.png`, eller `costumeCCC_NNN_hd.png` for myke figurer |
| Tekst | HD-glyf laget av spillets egen font, eller HD-skriften (Exo 2) |
| Filmramme (SMUSH) | `san/FILM/NNNNN.png`. Brukes ikke i Sam & Max |
| Alt annet | Originalpikselen skalert opp |

Det som ikke kan avgjøres sikkert, vises som originalen. HD-grafikken kan derfor legges inn litt etter litt, og spillet kan spilles hele veien.

Resten, kort:

- **Farger:** HD-pikselen ganges med forholdet mellom fargen spillet viser og originalfargen. Det gir toning, palettbytte og skygger. Fargesykling går gjennom et glatt fargekart over 3 x 3 originalpiksler.
- **Figurer:** hver piksel en rute tegner, merkes med tegningen, ruten og verdien. Pikselen viser HD bare så lenge verdien står der.
- **Myke figurer:** figurer i glatt stil med ekte alfa legges over etter blokkene, bak z-masken og under tekst og menyer.
- **Klassisk grafikk:** valget HD Graphics i spillets egen meny (F5), Ctrl+H bytter, Ctrl+Shift+H gir gult felt der HD mangler.

## Det som må portes for v6

Fra skillen `scumm-hd-remake` og The Dig sin erfaring, sjekket mot ScummVM-kilden ved `c9091321`. Ingen av punktene er gjort.

1. **Slå på DigHD for Sam & Max.** `DigHD::create` må godta `GID_SAMNMAX`.
2. **Kostymer.** Sam & Max har klassiske kostymer (COST), som tegnes av `ClassicCostumeRenderer` i `costume.cpp`. Krokene for rutene (`beginActor`, `noteCel`) finnes bare i `akos.cpp`, og `beginActor` kalles i `base-costume.cpp` bare når `_akosRendering` er satt. Krokene må inn i `ClassicCostumeRenderer` (`drawLimb`, `paintCelByleRLE`).
3. **Figurfargene.** The Dig sitt uttrekk og motor kjenner AKOS-kodekene (1, 5 og 16), RGBS og AKPL. Klassiske kostymer har egen palett (`ClassicCostumeRenderer::setPalette`). Hvordan fargene skal leses i uttrekket og i motoren, må sjekkes.
4. **Tekst.** Teksten tegnes av `CharsetRendererClassic`. Kroken (`noteGlyph`) finnes bare i `CharsetRendererV7::drawCharV7`.
5. **Blast-objekter og blast-tekst.** Blast-objektene er v6-kode (`ScummEngine_v6::drawBlastObject`), og krokene der finnes allerede. En kommentar i `script_v6.cpp` tyder på at minispillet på motorveien bruker dem. Skillen nevner også blast-tekst. I ScummVM ved `c9091321` er `drawBlastTexts` og `removeBlastTexts` tomme i `ScummEngine_v6`, og køen for blast-tekst finnes bare i `ScummEngine_v7`. Hvordan Sam & Max tegner og fjerner tekst, må derfor sjekkes i spillet. `restoreCharsetBg` kaller `markRectAsDirty`, der patchen allerede nullstiller glyfene. Ikke testet.
6. **Ingen SMUSH.** Delene for filmer (`smush_player.cpp`, `nut_renderer.cpp`, filmrammer, undertekster over filmer) brukes ikke. `DIGHD_SKIP_VIDEO` gjør ingenting i v6. Mellomsekvensene og minispillene tegnes av motoren og går gjennom de samme krokene som resten.
7. **Menyraden.** `digHDMenuRow` i `gfx_gui.cpp` gir raden HD Graphics bare for `GID_DIG`. Sam & Max bruker samme funksjon (`ScummEngine_v6::setUpMainMenuControls`), men raden er plassert med v7-koordinatene, og v6-menyen bruker andre (`yConstantV6`). Plasseringen må lages for v6 og sjekkes i originalmenyen.
8. **Musepekeren.** Kroken for pekeren i HD finnes bare i `ScummEngine_v7::updateCursor`. Sam & Max bruker `ScummEngine::updateCursor`. Museposisjonen deles allerede på skalaen i `input.cpp`.
9. **XOR 0x69.** ScummVM dekrypterer filene selv (`GF_USE_KEY`). Det gjelder uttrekket i pipelinen, ikke motoren.

Rettingen for Esc i `script.cpp` (en mellomsekvens hoppes ikke over når skriptet som startet den er stoppet) er ikke knyttet til DigHD og gjelder alle spill i denne motoren, også Sam & Max nå. Ikke testet med Sam & Max.

Rekkefølgen fra The Dig: rom og objekter først, testet med en `nearest`-mod. Det beviser at krokene sitter riktig. Så figurer, tekst, farger og sykling, blast-objekter, menyen, pekeren og klassisk grafikk.

## Testkrokene

Krokene ligger i DigHD og virker derfor ikke for Sam & Max før DigHD er slått på. Alle er miljøvariabler. Kjør med `SDL_VIDEODRIVER=dummy` og `SDL_AUDIODRIVER=dummy`.

| Variabel | Hva | Merknad for Sam & Max |
| --- | --- | --- |
| `DIGHD_MOD`, `DIGHD_SCALE`, `DIGHD_CLASSIC`, `DIGHD_SHOW_MISSING`, `DIGHD_TEXT` | Mod-mappen, skala, klassisk grafikk, gult felt og tekstvalg | |
| `DIGHD_VERIFY` | Sammenligner skjermen med originalen og med hele skjermen bygget på nytt | Fant de fleste feilene i The Dig |
| `DIGHD_DUMP_DIR`, `DIGHD_DUMP_EVERY`, `DIGHD_DUMP_FLAT` | Lagrer skjermbilder, også med originalpikslene | |
| `DIGHD_BENCH`, `DIGHD_QUIT_AT` | Tidsmåling og avslutning etter N bilder | |
| `DIGHD_TEST_ROOM`, `DIGHD_TEST_AT`, `DIGHD_TEST_CAMX`, `DIGHD_TEST_CAMY` | Hopper til et rom og setter kameraet | |
| `DIGHD_TEST_KEYS`, `DIGHD_TEST_CLICKS` | Taster og klikk ved gitte bilder | |
| `DIGHD_TEST_OBJSTATE`, `DIGHD_TEST_OBJSTATE_AT`, `DIGHD_TEST_OBJSTATE_EVERY` | Setter objekter i hver tilstand | |
| `DIGHD_TEST_COSTUME`, `DIGHD_TEST_ACTOR`, `DIGHD_TEST_POS`, `DIGHD_TEST_PALETTE`, `DIGHD_TEST_CHORE_EVERY`, `DIGHD_TEST_WALK`, `DIGHD_TEST_CLIP` | Setter inn en skuespiller med et kostyme og spiller animasjonene, går eller klipper mot z-masken | `DIGHD_TEST_COSTUME` leser animasjonene fra AKOS (AKHD, AKCH) og må skrives om for klassiske kostymer |
| `DIGHD_SKIP_VIDEO` | Hopper over filmer | Ingen virkning, det er ingen SMUSH-filmer |
| `DIGHD_DEBUG_SOFT`, `DIGHD_DEBUG_BLAST`, `DIGHD_DEBUG_FACE` | Logger myke ruter, blast-objekter og valg i HD-skriften | |

Verktøyene rundt:

- `engine/test.sh`: lager en mod med `nearest` og sjekker at HD-bildet er likt originalen skalert opp (0 avvik, unntatt skalerte figurer).
- `tools/romtest.sh`: kjører hvert rom uten skjerm og lager rapport og kontaktark.
- Begge har fått Sam & Max sine filnavn og spill-ID, men kan ikke kjøres før DigHD er portet og uttrekket finnes. `engine/test.sh` stopper med en melding til da.

## Lærdom fra The Dig som gjelder her

Fra skillen. Detaljene står i The Dig sin HD-MOTOR.md.

- Pikselformatet: `createFormatRGBA32()` er rekkefølgen i minnet. Les kanalene med `rShift`, `gShift`, `bShift` og `aShift`.
- Paletten kan endres mellom tegningen av skuespillerne og sendingen til skjermen. Bygg det som trenger de nye pikslene, i kroken før `updateScreen`.
- PNG med tRNS blir RGBA i ScummVMs dekoder. Fjern tRNS og les den gjennomsiktige indeksen selv.
- Innstillinger lagres i `kApplicationDomain`.
- Patchen lages på nytt med `git add -N` på nye filer og `git diff` i ScummVM-kopien.
