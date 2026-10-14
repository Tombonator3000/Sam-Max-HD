# Mellomsekvenser og minispill

Kartlagt 14. oktober 2026 fra de dekompilerte skriptene (`work/skript`, `tools/dekompiler_skript.py`) og romtesten. Spørsmålet er hva motoren tegner selv, utenom rombakgrunner, objektbilder og kostymeruter, og om det får HD.

Sam & Max har ingen SMUSH-filmer. Alle mellomsekvensene er vanlige rom med kostymer og objekter, styrt av skript (`beginCutscene` og `endCutscene` står 374 ganger), og går gjennom de samme krokene som resten av spillet. Det som skiller seg ut, er noen få tegneoperasjoner i skriptene.

## Tegneoperasjoner utenom bilder

| Operasjon (antall i skriptene) | Hva motoren gjør | HD |
| --- | --- | --- |
| `drawBox` (86) | Fyller et rektangel med én palettfarge | Originalpiksler skalert opp. Flate felt ser like ut i 4x. I Car Bomb (rom 66) tegnes skipsmerkene piksel for piksel med `drawBox` (skript 207); de forblir blokkete, for det finnes ikke noe bilde å bytte ut |
| `superBlastObject` (31) | Blast-objekter: inventaret, veibitene i Highway Surfing, Car Bomb, snøkulen | HD (testet i rom 68, 10. oktober) |
| `setActorShadowMode` / `setupShadowPalette` (14 + 14), `actorOps.setShadowMode` (7) | Figurpiksler tegnes gjennom skyggetabellen: skyggene under figurene (farge 13) og hele aktører med modus 0x20 (lyskjegler og lysstråler) | HD fra 14. oktober: pikselen bygges fra HD-bakgrunnen og tones med fargeforholdet, som blast-skyggene. Testet i rom 16 (lyskjeglen på gulvet og lysstrålen fra døren) |
| `shiftShadowPalette` (4) | Endrer skyggetabellen underveis | Følger med, fordi tabellen leses når skjermen bygges |
| `loadFlObject` (72), `drawObjectAt` (69) | Objektbilder lånt fra et annet rom, eller tegnet et annet sted | HD når objektbildet finnes i modden. Testet i rulleteksten (rom 77, objekt 600 til 603 fra rom 67) |
| `darkenPalette` (198), `setPalColor` (52), `setPalette` (7), `swapPalColors` (2), `copyPalColor` (2) | Palettendringer: nedtoning, lys av og på, blink | HD tones med forholdet mellom fargen som vises og originalfargen |
| `colorCycleDelay` (7) | Fargesykling | Glatt fargekart, som i The Dig |
| `screenEffect` (26) | Overganger mellom rom | Går gjennom `drawStripToScreen` som alt annet. Ikke sett på hver for seg |
| `shakeOn` (7) | Risting av skjermen | Ristingen skaleres med HD-skalaen (`gfx.cpp`) |
| `noirMode` (2) | Skjult svart-hvitt-modus (tast b, skript 64). ScummVM gjør paletten grå når den lastes opp | Ikke testet: tastaturskriptet kjører ikke etter testhoppet. HD tones per fargekanal mot den grå paletten, så farger som skiller seg fra originalen kan skinne igjennom |
| `clearCharsetMask` (3) | Tømmer tekstlaget | `_textV6` sammenligner verdiene, så borte tekst gir ikke HD-glyfer |

## Minispill og mellomsekvenser per rom

| Rom | Hva | Det som tegnes særskilt |
| --- | --- | --- |
| 1 | LucasArts-logoen | 3 blast-objekter, 6 `drawBox` |
| 2 til 6 | Introen | Vanlige rom og kostymer |
| 10 | USA-kartet | Vanlig rom med objekter |
| 18, 19 | Wak-A-Rat | 5 lånte objekter, 6 `drawBox` (poengfelt) |
| 24, 25 | Gator Golf | Lånt objekt, skyggemodus |
| 26 | Dunk the Beast | Skyggepalett, risting |
| 29 | Inne i hyssingnøstet | 11 lånte objekter, 13 `drawObjectAt` |
| 31, 78 | Kikkerten | `drawObjectAt` (6 og 12), lånte objekter |
| 37 | Mystery Vortex | 29 `setPalColor`, skyggemodus |
| 47 | Bumpusville Sings | Skyggemodus på tre aktører |
| 49, 50 | Den virtuelle verdenen | Vanlige rom |
| 66 | Car Bomb | 16 `drawBox` (skipsmerkene), 4 blast-objekter, 2 lånte objekter |
| 67, 77 | Rulletekst | Lånte panelbilder, `drawBox`, font 5 (pyntet, uten HD-skrift) |
| 68, 69 | Highway Surfing | 19 blast-objekter, `setBlastObjectWindow`, fargesykling, `swapPalColors` |
| 70, 71, 91 | Påkledning | `drawObjectAt` (5, 4, 5), `drawBox` i rom 71, font 5 |
| 76 | Tilbakeblikk: Bruno i isen | Vanlige kostymer (Trixie, kostyme 103) |
| 79 | Snøkulen | 4 blast-objekter, risting |
| 84 | Max's Wax | `copyPalColor` |
| 90 | Sam og Max med pistoler | 4 `drawBox`, font 5 |

## Det som gjenstår

- Car Bomb-merkene blir blokkete. Skal de få HD, må skriptets `drawBox`-mønster kjennes igjen i motoren og byttes med et bilde. Det er skriptnivå (nivå 3 hos Double Fine) og trenger Toms ja.
- Noir-modusen må testes med et lagret spill der tastaturskriptet kjører.
- Overgangene (`screenEffect`) er ikke sett på hver for seg.
