# HD-motoren for Sam & Max

Kort versjon for Sam & Max. Alle detaljer om hvordan motoren virker, innstillingene, testkrokene og hva som er testet i The Dig, står i The Dig sin [HD-MOTOR.md](https://github.com/Tombonator3000/Dig-HD-Remake/blob/main/docs/HD-MOTOR.md).

## Status

- Patchen `engine/patches/0001-dighd-hd-grafikk.patch` er The Dig sin patch mot ScummVM-commit `c9091321` (`engine/SCUMMVM_COMMIT`), utvidet for Sam & Max 10. oktober. The Dig skal virke som før; det er ikke testet her, fordi The Dig-filene ikke er i dette repoet.
- DigHD er på for The Dig og Sam & Max (`GID_SAMNMAX`) når `DIGHD_MOD` eller `dighd_mod` er satt.
- I Sam & Max får rom, objekter, blast-objekter, kostymerutene og teksten på skjermen HD (14. oktober). Menyraden HD Graphics står i originalmenyen (F5), og teksten i menyen har også HD.
- Miljøvariablene `DIGHD_*`, nøklene `dighd_*` i scummvm.ini og mod-formatet beholdes.

### Testet 10. oktober

- `engine/test.sh` (nearest-mod med rom, objekter og kostyme 1 til 20, 3000 bilder fra start): 0 av omtrent 1 million HD-piksler skiller seg sterkt fra originalen i alle dumper, og skjermen er lik hele skjermen bygget på nytt. Hver bakgrunnspiksel fant HD-bildet sitt ("background without HD 0"), så uttrekket stemmer piksel for piksel med det motoren tegner.
- `tools/romtest.sh --mod test-nearest --kamera ett` (alle 85 rom): 62 rom med HD-bakgrunn, 0 krasj, 0 forskjøvne bilder, 0 kjøringer der skjermen er ulik hele skjermen bygget på nytt. 12 rom hang etter testhoppet (skriptfeil fordi spillet ikke er i riktig tilstand, for eksempel "state -1 is out of bounds" i rom 11), 3 rom byttet til rom 0, 7 rom er mindre enn skjermen og testes ikke, og rom 67 er svart.
- Kostymer: med en nearest-mod med alle 16 052 ruter i kontoret (rom 7) får Sam og Max HD-ruter. Avviket er 0,26 til 0,29 prosent av skjermen, i kantene av figurene, fordi de er skalert (motorens skalatabell mot en jevn skalering i DigHD, som i The Dig). `DIGHD_TEST_COSTUME=2` spilte alle animasjonene til Sam med HD-ruter og 0 avvik.
- Blast-objekter: i motorveispillet (rom 68) får alle veibitene HD (for eksempel 6907 av 6907 piksler for objekt 604).
- Ctrl+H bytter mellom HD og klassisk grafikk.

### Testet 14. oktober

- Menyraden: F5 i introen (bilde 1500) åpner originalmenyen med raden «HD Graphics» under Text Speed, avkrysset. Et klikk på ruten (108,151) gir klassisk grafikk («DigHD: classic graphics» i loggen, ingen HD-piksler etterpå). Rammen er 14 piksler høyere nedover, resten står der det sto.
- Teksten: introen med `--subtitles` til bilde 6000 har HD-tekst (opptil 4158 HD-tekstpiksler per bilde) i HD-skriften, og «0 screen pixels differ» i alle 60 kontroller med `DIGHD_VERIFY`.
- `engine/test.sh`: 0 av omtrent 1 million HD-piksler skiller seg sterkt fra originalen; HD-teksten telles for seg, som i The Dig.
- Patchen passer mot en ren `engines/scumm` ved `c9091321` (`git apply --check`).
- Figurskygger og lyskjegler: klassiske kostymer tegner farge 13, og hele aktører med skyggemodus 0x20, gjennom skyggetabellen (`base-costume.cpp`). En slik figurpiksel bygges nå fra HD-bakgrunnen under og tones med fargeforholdet, som blast-skyggene (`_shade`), når figurens eget bilde ikke har den fargen der. Rom 16 (freakshowet): lyskjeglen på gulvet og lysstrålen fra døren er glatte, «shaded figure px» i loggen, og `DIGHD_VERIFY` gir 0 piksler som ikke er bygget på nytt. Se også `docs/MINISPILL.md`.
- Rulleteksten (rom 77, `DIGHD_TEST_ROOM=77`): panelene som lånes fra rom 67 (`loadFlObject`, objekt 600 til 603) får HD (42 880 HD-objektpiksler). Teksten avslørte to feil i HD-skriften, rettet samme dag: (1) i en font med tynne bokstaver i tykk kant valgte skriften kanten som bokstav, og e, c og r ble store svarte former. Når fargen som er valgt ligger ytterst og en annen ligger helt inni, tegnes glyfen nå fra fontbildet. (2) Font 5 er en pyntet font med bare store bokstaver (rulleteksten, påkledningen, Bumpusville); den er tatt ut av HD-skriften (`skrift.py`) og skaleres fra fontbildet, så formen blir som i originalen.

## Felles patch med The Dig

Fra 15. oktober 2026 er patchen den samme her og i Dig-HD-Remake. Endringene i begge siden 10. oktober er slått sammen tre-veis (felles base: Dig main 36cd09f). Fra Dig kom blant annet presise figurmerker for AKOS (bare v7), palettmasker, myke blast-objekter og objektpiksler som eier sitt område (`opacity`). Det som gjelder bestemte kostymer og objekter i The Dig, er sperret med `GID_DIG`. Objektoppslaget krever nå at den siste tegnede tilstanden fortsatt er objektets tilstand, og en tidligere tilstand teller fortsatt der den siste er gjennomsiktig (lappene i rom 17 og 21). Testet: `engine/test.sh` 0 avvik, romtesten som før, The Dig intro og romtest like med Digs egen patch. Detaljer i `docs/HD-MOTOR.md` i Dig-repoet.

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
- **Skalerte figurer** (15. oktober, etter Toms skjermbilde med piksler rundt Sam og Max): ScummVM skalerer klassiske kostymer med en skalatabell som hopper over bestemte rader og kolonner, ikke jevnt, og kan tegne én piksel utenfor rektangelet den oppgir. Merkingen (`markCel`) regnet med jevn skalering, så kantpikslene ble ikke merket som figurens og ble stående som originalpiksler rundt HD-figuren. Nå tas en piksel rundt en skalert rute med når den skiller seg fra bakgrunnen, har en farge som passer koden like ved i originalruten (`nearCode`), og ingen annen rute i samme tegning eier den. Testen av skygger og effekter under myke ruter (`softCelColour`) ser på kodene rundt punktet på samme måte.
- **Toms runde 14. oktober (tekstrester, nedtoning, peker, forgrunn, animerte objekter):**
  - Tekst med svart skygge som slettes ved å male over med svart (sceneskifte) beholdt skyggepikslene som HD-bokstaver, og ga prikkete tekst på svart skjerm. En piksel av én farge i glyfen teller nå bare mens en nabo i glyfens andre farge står der (`textAt`), og kanten av en HD-glyf inn i en gjennomsiktig piksel tegnes i v6 bare der tekstlaget er gjennomsiktig.
  - En piksel som er svart i originalen og fortsatt svart, kan ikke tones. Ved nedtoning til svart ble HD-pikselen (omriss som blander seg med fargene ved siden av) stående lys. Den blir nå ikke lysere enn fargene rundt den er nå (3 x 3 originalpiksler). Fordi pikselen avhenger av naboene, bygger `writeRect` én piksel ekstra rundt hvert område.
  - Pekeren glattes som figurene uten HD-bilde (xBR og Scale4x, kuttet ved halv alfa fordi pekeren har nøkkelfarge). `DIGHD_DUMP_DIR` lagrer også pekeren (`cursor_NNNNNN.png`).
  - Z-planmasken (forgrunnen) skaleres med xBR der kanten krysser en myk figur, så kanten mot stoler og tau ikke blir 4 x 4-trinn.
  - Objekter husker hver tilstand for seg. Noen animasjoner tegner en tilstand som bare er en lapp over den forrige (flaggene i rom 17); der lappen er gjennomsiktig, brukes den forrige tilstandens HD-bilde, men bare der (ellers ga propellen spøkelser).
- **Blast-objekter tegnet med fargetabell eller skalert** (de små LucasArts-logoene i introen): pikselen får HD-bildet også når fargen som vises er en annen enn koden i bildet, så lenge forholdet ikke er ekstremt (`wildColour`), og HD-pikselen tones fra bildets egen farge (`tintFactors` med koden). Skalerte BOMP-objekter (`scale_x`, `scale_y` sendes til `beginBlast`) slår opp nærmeste piksel med samme farge i bildet. De små logoene gikk fra 32 til 99,8 prosent HD.
- **HD-skriften** er Atkinson Hyperlegible (fet) fra 15. oktober, etter Toms ønske om mer lettlest tekst. Exo 2 ligger igjen som variant i `pipeline/smhd/skrift.py`.
- **Fart** (15. oktober): profilering med callgrind viste at fargetoningen (`tinted`) tok 55 prosent av tiden når hele skjermen bygges, med tre divisjoner per HD-piksel. Faktorene regnes nå én gang per originalpiksel (`tintFactors`, fast komma), og HD-pikslene ganges bare (`applyTint`). Hele skjermen i kontoret gikk fra rundt 15 til rundt 11 ms på maskinen her. Resten er de myke figurene (14 prosent) og selve byggingen.
- **Ruter uten HD-bilde i et kostyme med myke ruter:** modden har bare indeksbildet (`costumeCCC_NNN_idx.png`), og motoren lager en glatt utgave selv (`smoothCel`): omrisset med xBR (myk alfakant), fargene med Scale4x, en originalpiksels marg. Det gjelder for eksempel Sams hender (kostyme 4, rute 256), der den malte ruten er holdt tilbake. Uten dette sto slike ruter som blokker ved siden av de malte figurene.
- **Klassisk grafikk:** valget HD Graphics i spillets egen meny (F5), Ctrl+H bytter, Ctrl+Shift+H gir gult felt der HD mangler.

## Det som må portes for v6

Fra skillen `scumm-hd-remake` og The Dig sin erfaring, sjekket mot ScummVM-kilden ved `c9091321`. Punkt 1, 2, 3, 4, 6 og 9 er gjort 10. oktober, teksten (5) og menyraden (8) 14. oktober.

1. **Slå på DigHD for Sam & Max.** Gjort: `DigHD::create` godtar `GID_SAMNMAX`. Testhoppet leser romstørrelsen fra RMHD i v6-formatet.
2. **Kostymer.** Gjort: `ClassicCostumeRenderer::drawLimb` setter rutenummeret (lag * 128 + kode), `markAsDirty` husker rektangelet, og `paintCelByleRLE` kaller `noteCel` etter `byleRLEDecode`. `beginActor` i `base-costume.cpp` kalles nå også for klassiske kostymer. `DIGHD_TEST_COSTUME` leser animasjonene fra COST-hodet.
3. **Figurfargene.** Klassiske kostymer har egen palett (`ClassicCostumeRenderer::setPalette`) som peker på indekser i rompaletten. Uttrekket lagrer de indeksene i `_idx.png`. Når spillet viser andre farger (andre rom, skuespillerpalett), tones HD-pikselen etter forholdet mellom fargene, som i The Dig.
4. **v6 tegner teksten i et eget lag.** Gjort: `drawStripToScreen` legger tekstlaget over bufferen i `_compositeBuf` før det sendes videre i v6. DigHD får nå både den sammensatte kopien (verdiene) og området i bufferen (for merkene per piksel). Uten dette fikk ingen figurpiksler HD.
5. **Tekst.** Gjort 14. oktober: `CharsetRendererClassic::printCharIntern` melder hver glyf (`digHDNoteGlyph`) før `drawBitsN`. Tekst i hovedskjermen havner i tekstlaget (`_textSurface`), som er i skjermkoordinater; DigHD har et eget lag for det (`_textV6`) og slår opp med skjermposisjonen, så glyfene følger teksten også når kameraet står et annet sted. Det glyfen dekker, hentes fra bufferen under (`vsSrc`), ikke fra tekstlaget. Teksten i originalmenyen går gjennom `drawString` til bufferen i hovedskjermen og får HD på samme måte (3515 HD-tekstpiksler i menyen, testet 14. oktober).
6. **Blast-objekter og blast-tekst.** Blast-objektene er v6-kode (`ScummEngine_v6::drawBlastObject`). Gjort: Sam & Max ber om bilde 0, og motoren bruker da bilde 1; kroken får nå bildet som faktisk tegnes, så `objNNN_01.png` brukes. En kommentar i `script_v6.cpp` tyder på at minispillet på motorveien bruker dem. Skillen nevner også blast-tekst. Sjekket 14. oktober: skriptene har ingen blast-tekst, bare blast-objekter (31 kall til `superBlastObject` og ett til `setBlastObjectWindow` i `work/skript`). I ScummVM ved `c9091321` er `drawBlastTexts` og `removeBlastTexts` tomme i `ScummEngine_v6`, og køen for blast-tekst finnes bare i `ScummEngine_v7`. Hvordan Sam & Max tegner og fjerner tekst, må derfor sjekkes i spillet. `restoreCharsetBg` kaller `markRectAsDirty`, der patchen allerede nullstiller glyfene. Ikke testet.
7. **Ingen SMUSH.** Delene for filmer (`smush_player.cpp`, `nut_renderer.cpp`, filmrammer, undertekster over filmer) brukes ikke. `DIGHD_SKIP_VIDEO` gjør ingenting i v6. Mellomsekvensene og minispillene tegnes av motoren og går gjennom de samme krokene som resten.
8. **Menyraden.** Gjort 14. oktober: `digHDMenuRow` gir raden også for `GID_SAMNMAX`. I v6 står ruten på `yConstantV6 + 45` og teksten på `yConstantV6 + 48`, og den ytre og indre rammen blir 14 piksler høyere nedover.
9. **Musepekeren.** Gjort: kroken ligger nå også i `ScummEngine::updateCursor`, som Sam & Max bruker. Ikke sett på en ekte skjerm.
10. **XOR 0x69.** ScummVM dekrypterer filene selv (`GF_USE_KEY`). Det gjelder uttrekket i pipelinen, ikke motoren.

Rettingen for Esc i `script.cpp` (en mellomsekvens hoppes ikke over når skriptet som startet den er stoppet) er ikke knyttet til DigHD og gjelder alle spill i denne motoren, også Sam & Max nå. Ikke testet med Sam & Max.

Rekkefølgen fra The Dig: rom og objekter først, testet med en `nearest`-mod. Det beviser at krokene sitter riktig. Så figurer, tekst, farger og sykling, blast-objekter, menyen, pekeren og klassisk grafikk.

Lista over det som vises uten HD (fra Dig PR 52, 15. oktober): mens spillet spilles i HD, skriver motoren alt som står på skjermen som originalpiksler fordi modden mangler HD-bilde, til `dighd-uten-hd.txt` i lagringsmappen (Linux-pakken: `~/.local/share/sam-max-hd/saves/`). Én linje per bilde og rom: type (rute, objekt, rom, film), id som i modden, rom, hvor mange bilder det sto der, flest piksler i ett bilde og når det ble sett først. Svart, rom 0, klassisk grafikk og bakgrunn under myke figurer telles ikke. `DIGHD_MANGLER=0` slår av. Beskrevet i `docs/HD-MOTOR.md` i Dig-repoet, under «Liste over det som vises uten HD».

## Testkrokene

Krokene ligger i DigHD og virker for Sam & Max. Alle er miljøvariabler. Kjør med `SDL_VIDEODRIVER=dummy` og `SDL_AUDIODRIVER=dummy`.

| Variabel | Hva | Merknad for Sam & Max |
| --- | --- | --- |
| `DIGHD_MOD`, `DIGHD_SCALE`, `DIGHD_CLASSIC`, `DIGHD_SHOW_MISSING`, `DIGHD_TEXT` | Mod-mappen, skala, klassisk grafikk, gult felt og tekstvalg | |
| `DIGHD_VERIFY` | Sammenligner skjermen med originalen og med hele skjermen bygget på nytt | Fant de fleste feilene i The Dig |
| `DIGHD_DUMP_DIR`, `DIGHD_DUMP_EVERY`, `DIGHD_DUMP_FLAT` | Lagrer skjermbilder, også med originalpikslene | |
| `DIGHD_BENCH`, `DIGHD_QUIT_AT` | Tidsmåling og avslutning etter N bilder | |
| `DIGHD_TEST_ROOM`, `DIGHD_TEST_AT`, `DIGHD_TEST_CAMX`, `DIGHD_TEST_CAMY` | Hopper til et rom og setter kameraet | |
| `DIGHD_TEST_KEYS`, `DIGHD_TEST_CLICKS` | Taster og klikk ved gitte bilder | |
| `DIGHD_TEST_SCRIPT` | Starter et skript med argumenter ved et gitt bilde, `900:207:3/4/1` (lokalt skript 207 med 3, 4 og 1). For minispill og effekter som er vanskelige å nå | Lagt til 14. oktober |
| `DIGHD_TEST_OBJSTATE`, `DIGHD_TEST_OBJSTATE_AT`, `DIGHD_TEST_OBJSTATE_EVERY` | Setter objekter i hver tilstand | |
| `DIGHD_TEST_COSTUME`, `DIGHD_TEST_ACTOR`, `DIGHD_TEST_POS`, `DIGHD_TEST_PALETTE`, `DIGHD_TEST_CHORE_EVERY`, `DIGHD_TEST_WALK`, `DIGHD_TEST_CLIP` | Setter inn en skuespiller med et kostyme og spiller animasjonene, går eller klipper mot z-masken | For klassiske kostymer leses animasjonene fra COST-hodet (alle med en offset). Noen kostymer har animasjoner som peker utenfor kostymet (se `advarsler` i costumes.json) |
| `DIGHD_SKIP_VIDEO` | Hopper over filmer | Ingen virkning, det er ingen SMUSH-filmer |
| `DIGHD_DEBUG_SOFT`, `DIGHD_DEBUG_BLAST`, `DIGHD_DEBUG_FACE` | Logger myke ruter, blast-objekter og valg i HD-skriften | |

Verktøyene rundt:

- `engine/test.sh`: lager en mod med `nearest` og sjekker at HD-bildet er likt originalen skalert opp (0 avvik, unntatt skalerte figurer).
- `tools/romtest.sh`: kjører hvert rom uten skjerm og lager rapport og kontaktark.
- Begge virker med Sam & Max (se Testet over).

## Lærdom fra The Dig som gjelder her

Fra skillen. Detaljene står i The Dig sin HD-MOTOR.md.

- Pikselformatet: `createFormatRGBA32()` er rekkefølgen i minnet. Les kanalene med `rShift`, `gShift`, `bShift` og `aShift`.
- Paletten kan endres mellom tegningen av skuespillerne og sendingen til skjermen. Bygg det som trenger de nye pikslene, i kroken før `updateScreen`.
- PNG med tRNS blir RGBA i ScummVMs dekoder. Fjern tRNS og les den gjennomsiktige indeksen selv.
- Innstillinger lagres i `kApplicationDomain`.
- Patchen lages på nytt med `git add -N` på nye filer og `git diff` i ScummVM-kopien.
