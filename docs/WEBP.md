# Tapsfri WebP i HD-motoren

Fargebildene kan lagres som tapsfri WebP med ekte alfa. Motoren prøver samme
filnavn med `.webp` først og deretter `.png`. Prioriteten mellom myk og flat
figur er fortsatt `_hd.webp`, `_hd.png`, flat WebP, flat PNG. Rom, objekter,
pekere, figurer, skrifter og SAN-filmruter bruker denne leseren.

`_idx.png` og `_mask.png` beholdes som PNG. Palettindeksene styrer blant annet
fargetoning, gjennomsiktighet og skygger. Like RGB-farger betyr ikke like
indeksverdier. Originale jobbgrunnlag, råbilder og `resultat.png` endres ikke.

## Konvertering

Fra et installert pipeline-miljø:

```sh
python -m smhd.webp mods/gpt out/webp-kandidat --workers 4
```

Kildemappen endres ikke. Målmappen må være ny og utenfor kilden. Hvert fargebilde
kodes med `lossless=True`, `exact=True`, kvalitet 100 og metode 6. Det dekodes på
nytt og sammenlignes som RGBA, inkludert RGB under helt gjennomsiktige piksler.
En PNG beholdes hvis WebP blir større. Ingen bilder skaleres eller kvantiseres.
16-bits bilder, animasjoner, symbolske lenker og tvetydige PNG/WebP-par avvises.

`webp-migration.json` oppgir gamle og nye filnavn, SHA-256, dimensjoner,
pikselhash og størrelser. `complete` må være sann. `SHA256SUMS` omfatter alle
filer i den ferdige kandidaten, også migreringsrapporten. Verifiser denne
kandidaten i motoren før den erstatter en publisert mod. Kilde-SHA og fjern-SHA
skal kontrolleres igjen før publisering. Publiser med gammel mod som Git-forelder
slik at de erstattede PNG-filene fortsatt kan hentes fra historikken.

Nye grafikkleveranser kan fortsatt mottas som PNG. Ved samling til mod skal den
ferdige kandidaten konverteres med samme kontroll, uten å legge igjen utdaterte
PNG/WebP-par. Ikke bygg en ny mod fra et eldre grafikkgrunnlag.

## Bygg og kontroll

Linux trenger `libwebp-dev`. Windows bruker MSYS2-pakken
`mingw-w64-x86_64-libwebp`; pakkeskriptet tar med DLL-avhengighetene. Nettleseren
bruker libwebp 1.6.0 bygget fra kilde med låst SHA-256, sammen med den eksisterende
låste Emscripten-versjonen. Lisensen følger Pages-pakken.

`WebP-motor` i Actions bygger Linux og nettleseren. Linux-prøven konverterer
et utvalg fra publisert mod og sammenligner faktisk avspilling mot PNG i tre kontrollerte
scener med samme motor og tilfeldighetsfrø. Bildenes rå RGBA sammenlignes.
Dette er formatkontroll, ikke en ny visuell stilgodkjenning. Pipeline- og
nettsidetestene dekker også alfa, dupliserte palettfarger og blandede modmapper.

Plassbruk i `out/` omfatter mange gamle fullkopier, nedlastinger og motorbilder.
Tapsfri WebP i selve modden løser bare en liten del av dette. Gamle kopier fjernes
først etter dokumentert kontroll mot en beholdt kilde eller utgivelse.

Størrelsesgrenser for spillerpakker og fast plassrutine for arbeidskopier er dokumentert i [PLASSBRUK.md](PLASSBRUK.md). Tapsfri komprimering og original oppløsning beholdes.
