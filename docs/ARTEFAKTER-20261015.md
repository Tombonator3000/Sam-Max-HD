# Inventar og glassmasker, 15. oktober 2026

Tom meldte pikselkanter i inventaret, rosa felt ved akvariet og cafeteriarøret, rester ved bevegelige objekter og feil i Sams hånd. Tom ga Codex uttrykkelig tillatelse til å rette motoren og lage PR i denne runden.

Inventarkortene ble tegnet som ordinære romobjekter, men den veien lastet ikke de separate `objNNN_SS_hd.png`-filene. Den nye veien foretrekker disse filene når de har nøyaktig 4x størrelse uten marg. Native objekter bruker samlet, bufret palettfaktor, så originalens nøkkelfarge ikke farger de nye kantene. Gjennomsiktige kort viser aktive objektlag under, som inventaresken. Vanlig tegning og spillogikk beholdes.

Klassiske Byle-kostymer med myk HD registrerer nå faktiske dekoderskrivinger med `recordCelPixel`, slik AKOS allerede gjorde. Både `_shadowMode & 0x20` og palettindeks 13 med skyggetabell merkes som palettmasker. Dette bevarer tegningen under glass og hindrer at hele kostymets måleboks eier bakgrunn den ikke skrev. Hard nearest-kostymevisning bruker fortsatt den tidligere koblingen etter dekoding.

## Verifisert

- Bygget ScummVM mot uendret `engine/SCUMMVM_COMMIT` (`c9091321`). Lokal testbygging uten MT-32, med dummy skjerm/lyd. Produksjonens byggevalg er ikke endret.
- Generert patch anvendt på ren låst base, alle 30 resulterende kildefiler byteidentiske med bygget kilde. `git diff --check` i ScummVM-kilden består. Enkelte eksisterende kontekstlinjer i selve patchfilen gir falske whitespace-varsler når patchen behandles som vanlig tekst.
- 51 pipelinetester og 19 nettlesertester bestått. Tre game-tester ikke kjørt i denne pipelinerunden.
- Faktiske spillbilder: inventar åpner/lukker med rene native kort; akvariet bevarer figurlaget bak grønt glass; cafeteriarøret er blått uten rosa flate i testet bevegelse. Siste tre kjøringer ga null forskjell mellom skjermbuffer og full gjenoppbygging. Z-kantmålingene er ikke null.
- Nearest-sammenligning: kontoret 3193 av 1 024 000 kraftige avvik med både utgivelsesmotor og retting, 0,312 prosent. Cafeteria 475 mot 542, 0,046 mot 0,053 prosent. Ingen påstand om pikselidentisk nearest-kontroll.

[Bilder, testoppskrifter, resultater og nye grafikkfiler ligger bare i grafikkgrenen](https://github.com/Tombonator3000/Sam-Max-HD/blob/gpt-arbeid/rapporter/feilrunde2-20261015/RAPPORT.md). Testgrunnlaget er HD-mod `9512fd8` pluss nye Sam-ruter og kantvaskede ikoner. Senere publisert mod `dd43c31` er ikke hele grunnlaget for disse prøvene. Sammenligningspakken var Linux-utgaven fra rundt 18:03 norsk tid, ikke en test av alle senere utgivelser.

## Fortsatt åpent

Øks-/bakgrunnsrester i rom 22 er fortsatt synlige. Det statiske HD-rommet inneholder motiv som ikke stemmer med animasjonstilstandene; full gjenoppbygging av skjermen løser ikke dette. Kranhodet 154 og Chicken Dumpling 155 i rom 16 trenger kontroll i faktisk bevegelse og sammenhengende tilstander. Tvungne testtilstander blir delvis overstyrt av skriptene.

Opptakstesten traff objekt 0, ikke gjenstanden, og er derfor ikke bevis for at restene etter opptak er løst. Bilens avreise og hele Wak-A-Rat-/samtaleforløpet er ikke bekreftet. The Dig er ikke kjørt med denne utvidelsen. Ny kode, grafikkimport og Linux-/Windows-/webbygg må kontrolleres sammen før Tom får en ny testpakke.
