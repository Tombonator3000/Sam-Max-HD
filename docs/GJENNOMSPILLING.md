# Gjennomspillingsagenten

En Claude-økt spiller Sam & Max HD fra start til slutt uten skjerm, lagrer i hvert nytt område og skriver ned feil den finner. Den styrer spillet med `tools/styr.py` gjennom styringskanalen i HD-motoren (`DIGHD_STYRING`, se `controlFrame()` i `dighd.cpp`).

Tom starter den med `tools/gjennomspill.sh` (se nederst). Resten av dokumentet er instruksen agenten følger.

## Mål

1. Spill hele spillet, i spillets rekkefølge, med HD-modden.
2. Finn feil og skriv dem i `work/gjennomspill/FUNN.md` med bevis.
3. Lagre i hvert nytt rom og før hver vanskelig del. De lagrede spillene trengs til `tools/romtest.sh --lagret` (de 12 rommene som henger etter testhoppet).

## Slik spiller du

Alt går gjennom `tools/styr.py`. Les `tools/styr.py --help` først.

```sh
tools/styr.py start                   # fra begynnelsen (eller: start --slot N fra et lagret spill)
tools/styr.py hoyreklikk 1 1          # neste markør
tools/styr.py klikk 120 80 vent 200 bilde
tools/styr.py klikkting 64 kontroll bilde   # klikk på ting 64 (telefonen), vent på kontrollen, ta bilde
tools/styr.py markor se               # bytt til se-markøren (gå, se, hånd, snakk, figur)
tools/styr.py status
tools/styr.py stopp
```

- Koordinatene er originalpiksler, 320 x 200. Bildene er 1280 x 800, så del på 4.
- Klikk på ting med `tools/styr.py klikkting NR` (nummeret fra tinglisten). Den regner ut hvor tingen er når klikket skjer. Brede rom ruller når Sam går, så et punkt fra en eldre status kan være feil. Bruk `klikk X Y` for steder uten ting (gulvet, kanten av bildet, samtaleikonene).
- Etter hvert kall skriver `styr.py` en status. Den viser rommet, om du har kontrollen, markøren, replikken som vises, tingene på skjermen med navn og hvor du skal klikke, inventaret og det som vises uten HD.
- Se på bildet etter hvert viktig steg (Read på PNG-filen). Ta `bilde` når du kommer inn i et nytt rom, etter at noe har endret seg, og når du lurer på noe.
- Bytt markør med `tools/styr.py markor gå|se|hånd|snakk|figur`. Den finner et tomt sted (over en ting hopper spillet over gå-markøren) og høyreklikker ett klikk om gangen til markøren er riktig. Send ikke flere høyreklikk i samme kall; markøren skifter variant over ting, og rekkefølgen blir lett feil. Markørene: gå (889, over noe 890), se (883, 875), hånd (884, 876), snakk (885, 877), hånd med figur (886, 878).
- Ting uten navn i listen er ofte utganger, trapper og dører. Prøv dem med gå-markøren. Eksempel: trappen ned fra gangen (rom 8) er ting 82 uten navn nede til venstre, mens `sam-hall-upstairs` er trappen opp, som Sam ikke vil gå i («Not since the accident»).
- Utganger kan også være kanten av bildet. Gå mot kanten der en sti eller dør fører ut.
- Inventaret er esken nede til venstre. Klikk på den for å åpne. Klikk på en ting for å ta den som markør, og så på det du vil bruke den på.
- Samtaler i Sam & Max har ikoner, ikke tekst. Ta bilde og klikk på ikonene.
- Etter et gåklikk har du fortsatt kontrollen mens Sam går. Bruk `vent 150` til `vent 400` før du ser hva som skjedde. Etter et klikk som starter noe (en samtale, en mellomsekvens), bruk `kontroll`.
- `tast period` hopper over en replikk. `tast escape` hopper over en mellomsekvens. Hopp gjerne over lange samtaler du har sett.
- Rett etter et rombytte kan tinglisten være tom. Vent 30 bilder og spør igjen.
- Minispillene (Wak-A-Rat, Highway Surfing, Car Bomb, Gator Golf og de andre) kan være vanskelige å spille med klikk. Prøv litt, ta bilder av dem, og hopp videre hvis det ikke går.

## Veien gjennom spillet

`docs/GJENNOMGANG.md` sier sted for sted hva som skjer, hvem som er der og hvilke ting som hører til hvilket rom. Bruk den sammen med det du vet om spillet (Derek Waites gjennomgang fra 1993 og andre kjente løsninger). Står du fast mer enn 30 handlinger på samme sted:

1. Se på alle tingene i rommet med se-markøren, og snakk med alle.
2. Prøv tingene i inventaret på det som er i rommet.
3. Gå til kartet (USA-kartet i bilen, rom 10) og prøv et annet sted.
4. Prøv tingene uten navn, kantene av bildet og alle tingene med alle fire markørene.
5. Skriv i `FREMDRIFT.md` hva du har prøvd, og gå videre til neste område hvis spillet lar deg.

Gi aldri opp før tiden er ute. Kommer du ikke videre, bruk resten av økten til å se nøye på HD-grafikken i rommene du har nådd: alle tingene med se-markøren, alle tilstandene du kan få fram, og sammenlign med originalen.

## Lagring

- Lagre med `tools/styr.py "lagre N Rom 17 midway"`. N fra 2 og oppover, et nytt nummer for hvert sted. Plass 1 brukes til hurtiglagring underveis.
- Lagre i hvert nytt rom, før minispill, før valg du ikke kan angre, og før du avslutter økten.
- Skriv hvert lagrede spill i `FREMDRIFT.md` (nummer, rom, hva som er gjort).
- Krasjer eller henger spillet, start fra siste lagring med `tools/styr.py start --slot N`.

## Hva som er en feil

Skriv alt dette i `FUNN.md`:

| Slag | Hva |
| --- | --- |
| `uten-hd` | Noe vises uten HD (står i `uten HD nå` i statusen, og er gult i `_gult.png`) |
| `grafikk` | HD-bildet er feil: flyttet, feil størrelse, feil figur eller ting, noe mangler eller er lagt til, feil farge, tekst eller skilt som ikke stemmer med originalen. Sammenlign alltid med `_flat.png`. `styr.py` melder felter der HD avviker mye fra originalen; se på dem, men husk at figurer i HD har mykere kanter og kan avvike litt uten å være feil |
| `kant` | Sømmer, hakk, rester eller rammer rundt figurer og ting, svarte eller fargede glorier |
| `tekst` | Replikker eller menyer med feil tegn (originalen i `_flat.png` er fasit) |
| `motor` | Noe tegnes på feil sted eller i feil lag (figur foran noe den skal stå bak), flimmer, feil etter rombytte |
| `krasj` | Spillet stopper. Ta med slutten av `scummvm.log` |
| `heng` | Spillet svarer ikke, eller du får aldri kontrollen tilbake |
| `spill` | Spillet oppfører seg ikke som originalen (en ting virker ikke, en dør åpner seg ikke) |

Kjente feil som allerede er funnet 17. oktober 2026, så du ikke skriver dem på nytt:

- `tekst`: tegnet `^` i spillets tekst er tre prikker i spillets skrift, men HD-skriften tegner `^` («Loading Sounds...Please Wait», «people...except Max» og alle andre).
- `grafikk`: hodet og ørene til Max er større og står annerledes enn i originalen i kontoret (rom 7).
- `grafikk`: figurer som ikke er tegnet i HD ennå (katten i rom 9, Flambe i rom 15), skaleres opp automatisk og ser uskarpe ut. Gult-bildet viser dem ikke. Skriv dem likevel én gang per figur og rom, så vi ser hvilke som mangler mest.

## FUNN.md

Én oppføring per feil, nyeste nederst:

```
## 0042 rom 17: Wak-A-Rat-hammeren uten HD
- slag: uten-hd
- hva: Hammeren i Sams hånd vises med originalpiksler (costume112_004).
- bilde: bilder/0042_wakarat.png, utsnitt funnbilder/0042_hammer.png
- lagret: plass 7 (rett før minispillet)
- slik får du det fram: lagret spill 7, klikk på Wak-A-Rat med hånden
```

- Lag utsnitt som bevis: `tools/styr.py utsnitt BILDENR X Y B H navn` (HD, original og gult side om side).
- Samme feil på flere steder: skriv den én gang og list stedene.
- Skriv hva du ser, ikke hva du tror årsaken er. Er du usikker, skriv det.

## FREMDRIFT.md

Hold `work/gjennomspill/FREMDRIFT.md` oppdatert, så neste økt kan fortsette der du slapp:

- hvor du er (rom, hva som er gjort i området),
- lagrede spill (nummer, rom, kort beskrivelse),
- hva som gjenstår i området og neste mål,
- hva du har prøvd uten hell.

## Regler

- Ikke endre filer i repoet. Alt du skriver, går i `work/gjennomspill/`.
- Ikke push, ikke commit, ikke installer noe. `tools/gjennomspill.sh` legger funnene ut på GitHub.
- Skriv på norsk, uten emoji og uten tankestrek.
- Økten har et antall minutter. Sjekk tiden med `date` innimellom, og avslutt først når minuttene er brukt.
- Når økten er over: lagre, oppdater `FREMDRIFT.md`, kjør `tools/styr.py stopp`, og skriv `SEGMENT FERDIG` som siste linje. Er hele spillet spilt, skriv `SPILLET FERDIG`.

## For Tom: slik starter du den

```sh
tools/gjennomspill.sh                 # spiller til 08:00, i økter på 45 minutter
tools/gjennomspill.sh --timer 2       # to timer
touch work/gjennomspill/STOPP         # stopper etter økten som går
```

Skriptet tar en kopi av HD-modden og motoren først, så natteskiftet kan bygge ny modd samtidig uten at spillet mister filer. Etter hver økt legger det `FUNN.md`, `FREMDRIFT.md`, utsnittene og de lagrede spillene i grenen `gjennomspilling` og pusher den. Bildene og de lagrede spillene er fra spillet og hører ikke hjemme i `main`.
