# todo.md

Det som gjenstår, viktigst først. Kryss av når noe er gjort, og logg det i `log.md`.

## Neste

- [x] Trappetrinn rundt bilen i rom 9: myk alfa for romobjekter og kanten lagt over HD-rommet i motoren (PR 29, 15. oktober)
- [x] PR 28 og PR 29 flettet; Linux, Windows og nettsiden bygget på nytt fra main (15. oktober 18:00)
- [x] Samme patch i Dig-HD-Remake (Dig PR 57, venter på fletting)
- [ ] Tom fletter PR 30 (objektleveranser.json i importpakke)
- [x] Kontroll av PR 32 (Codex, native inventarkort og glassmasker i motoren): koden lest, fem funn i `docs/KONTROLL-PR32.md` (15. oktober 22:20, natt). Ikke bygget eller kjørt, maskinen har ingen C++-kompilator
  - [ ] Codex: felles bilde for blast og romobjekt gir `softEdge = false` når blast lastes først (funn 1)
  - [ ] Se bilen i rom 9 i en nedtoning med PR 32 (kanten tones nå med rommets farge, funn 3)
  - [ ] Tom fletter PR 32, og avgjør om Dig skal få samme endring (funn 4)
- [x] Mottaket måler Sam091 uten den løse fotresten (measure_mask), så 8 ruter står feilaktig til gjennomsyn (rettet 15. oktober 20:25, `myk.py` versjon 6, på grenen samarbeid/natt-2026-10-15)
  - [x] Neste `tools/gpt_runde.sh` etter fletting tar inn de 11 rutene (fig091_03 til 05, fig209_03, fig272_02); fjern da beskjeden om ny tegning i ORDRE.md. Sjekket 16. oktober 05:30: myke.json versjon 6 har alle 11 som ok (970 ok, 0 til gjennomsyn), og ORDRE.md i gpt-arbeid nevner ikke fig091 lenger. Ikke sett i spillet
  - 15. oktober 20:05: fig091_03 (rute 1955, ny utgave) og fig091_04 sett av Claude, bokser like originalen i 4x, holdes likevel ute og ordren ber om ny tegning. Beskjed i ORDRE.md om ikke å tegne dem på nytt. Når mottaket er rettet, kommer de inn uten ny leveranse
- [x] GitHub-innlogging og push fra denne maskinen er rettet i nattoppsettet. Gjentatte faktiske push til gpt-arbeid, hd-mod og nattgrenen er bekreftet på GitHub; ingen uavklart pushblokkering fra 15. oktober 20:04
- [x] Mottaket retter hele bilder som er forskjøvet 0,25 til 1,5 originalpiksler (klipper på nytt der innholdet ligger, ikke figurark), 16. oktober 00:24, nattgrenen. Tørrkjøring på de 32 sjekk-jobbene: 12 blir godkjent, 7 til får bedre plassering men står fortsatt til sjekk
  - [x] Tatt i bruk og visuelt plasseringskontrollert 16. oktober: obj602_01 av Claude, de øvrige elleve av Codex rundt 01:42. Original, mottaksbilde og fargelåst bilde sett; hele rom60 også sett for delskjøten. Ingen åpenbar ny feilplassering eller avklipping. Ikke motoravspilt eller stilgodkjent av Tom
- [x] Ikonark levert på en annen flat farge enn bestilt (ikon01 på grønt, ikke magenta) fikk magenta glorie rundt ikonene etter fargelåsen, også i modden (obj661_01 til obj670_01). Fargelåsen bruker nå arkfargen som er levert (16. oktober, nattgrenen)
  - [x] Tatt i bruk i hd-mod 8f3f82a7 og sett av Codex 16. oktober: de fire PNG-filene er sammenlignet med original og førbilder. Kraftig magentaglorie tydelig redusert, identisk alfa og størrelse. Enkelte grønne/lilla kantpiksler gjenstår på bilene. ikon01 står fortsatt til sjekk (blokkavvik 1,3)
  - [x] Rens de gjenværende grønne/lilla kantpikslene på obj661_01, obj662_01 og obj663_01, og kontroller obj670_01 samtidig. Bevar form og alfa, sammenlign original og ny modd på mørk og lys bakgrunn. Ny retting skal ha Codex-kodekontroll; visuell etterkontroll og motoravspilling gjenstår før dette regnes helt ferdig
    - [x] Kantrens i mottaket for ikonark (`clean_sheet_edge` i `gpt.py`), 16. oktober, nattgrenen. Tørrkjørt på de 163 ikonene i modden: grønt på bilene 692/944/351 til 0/3/0 piksler, magenta 447/445/463 til 113/29/74, magentastripen på obj670_01 borte, alfa uendret
    - [x] Codex: kodekontroll av kantrensen ecd9ec0e, 03:21 den 16. oktober. 62 pipelinetester og tørrkjøring på 163 ikoner
    - [x] Tatt i bruk i hd-mod 55f976de. Codex har sett 22 faktiske PNG mot original og førbilder på mørk og lys bakgrunn, blant annet bilene, obj670_01, grønne felt i obj824_01 og utvalg fra ikon07/08. Tydelig færre fargerester, ingen åpenbar ny skade på ekte farger i utvalget. Alle 163 har uendret størrelse/alfa. Mørk lilla og trappetrinn gjensto i denne modden; ikke motoravspilt
    - [x] Litt mørk lilla står igjen langs taket på obj661_01 (blanding av svart og magenta som ikke ligner en ren blanding). Rettet 16. oktober: kantpiksler med arkfargens fargetone som ikke er en ren blanding, mister fargetonen (lysstyrken står), med vern to originalpiksler fra samme fargetone i originalen
      - [x] Codex: kodekontroll av andre trinn de951ff7, 04:15 den 16. oktober. 63 pipelinetester og kontroll på 163 ikoner
      - [x] Andre trinn sett i publisert hd-mod 183850f6 og bekreftet byteidentisk for alle 163 ikoner i sluttmodd 037f4298. Codex sammenlignet 14 PNG mot original/før/etter på mørk og lys bakgrunn: biltak/bakrute, obj824_01, logoen og utvalg fra ikon07/08. Mørk lilla redusert, ingen åpenbar ny skade på ekte farger i utvalget. Alle 163 har uendret alfa/størrelse, 47 endret RGB; trappetrinn og logoens lyse magenta står. Ikke motoravspilt. Bevis: output/natt-kantrens-trinn2-20261016 i Codex-arbeidsmappen
      - [ ] obj049_01 (LucasArts-logoen): den lyse magenta kanten rundt figuren og øyevippene står fortsatt, rettes ikke av kantrensen (står allerede i grafikkordren)
- [x] RAPPORT.md fra gpt-inn sa «Ferdige figurruter: 0 av 15661» selv om 970 figurruter ligger i modden: figurarkene i glatt stil får status levert og tas inn av `smhd myke-figurer` etter gpt-inn. Linjen sier nå hvor mange ark som er levert til figurmottaket og at rutene telles i ORDRE.md og myke.json (a9d26856, nattgrenen). Codex-godkjent 16. oktober 05:15 med 64 pipelinetester; rapportlinjen oppdateres ved neste import
- [ ] Rester etter opplukking i kontoret (rom 7), kanter rundt Sam og hammeren i Wak-A-Rat, chatrammene i spillet (grafikerens rapport 15. oktober 18:06)
- [ ] Se Sam og Max foran bilen i rom 9 og bilen som kjører bort
- [x] Første natteskift med Claude og Codex er i gang etter prøveturen 15. oktober. Nattløpet stopper 16. oktober klokken 08:00; nattkontroll følger med

- [x] Innført kildetro motiv- og designanalyse før HD-produksjon i `docs/skills/scumm-hd-remake/SKILL.md`, med henvisninger fra arbeidsinstruksene (12. oktober 2026)

- [x] Løs konfliktene i PR 2 mot main uten å miste motorarbeidet fra PR 3 (12. oktober, Codex)

### Oppsett (10. oktober)

- [x] Repoet satt opp med AGENTS, README, memory, todo, log, STATUS, .gitignore og CI-sjekk mot spillfiler
- [x] Spillfilene hentet fra Drive og lagt i grenen `spilldata` med sjekksummer, MONSTER.SOU i deler på 90 MB
- [x] Utgaven bekreftet med MD5: engelsk CD-utgave
- [x] Samme oppsett som Dig-HD-Remake: `engine/`, `pipeline/` (`smhd`), `tools/`, `docs/`, `spill.sh`, arbeidsflyter, grenene `hd-mod` og `gpt-arbeid`
- [x] ScummVM ved c9091321 med patchen bygget, og Sam & Max startet uten skjerm (uten HD)
- [ ] Tom skrur av lenkedelingen på Drive-mappen `Scummvm` (den trengs ikke lenger)
- [ ] Tom starter `./spill.sh` på laptopen og ser at spillet starter med bilde og lyd

### Analyse (`docs/ANALYSE.md`)

- [x] Tell rom, størrelser, z-plan, paletter, fargesykling, objektbilder og kostymer (`smhd info`)
- [x] Romliste som CSV (`docs/rom-oversikt.csv`, uten navn)
- [x] Navn på rommene i romlisten (13. oktober, alle 85)
- [x] Ruter per kostyme, animasjoner og retninger (`costumes.json`, 16 052 ruter)
- [x] Hvilke objekter som har BOMP-bilde (103 blast-objektbilder, `kind` i rooms.json)
- [x] Dekompiler alle skriptene med descumm (`tools/dekompiler_skript.py`, 1179 av 1181)
- [x] Finn hvilke rom og palett hvert kostyme vises i fra skriptene (`tools/kostymer.py`, `docs/kostymefarger.csv`, 13. oktober)
- [x] Se de kostymene som står med «trolig» i `docs/figurer.csv` i spillet, og rulletekstpanelene i rom 67 og 77 (14. oktober): kostyme 103 er Trixie (skript 120), panelene (objekt 600 til 603 lånt fra rom 67) får HD i rom 77. Rulleteksten avslørte to feil i HD-skriften, rettet
- [x] Finn mellomsekvensene og minispillene som tegnes av motoren (14. oktober, `docs/MINISPILL.md`). Figurskygger og lyskjegler (skyggetabellen) får nå HD
- [x] Car Bomb (rom 66): skipsmerkene glatte i HD (Toms ja 14. oktober; merket tegnes som glyf med xBR)
- [x] Noir-modusen (tast b): HD-bildet blir grått (14. oktober)
- [x] Utviklermodus: «Sam og Max HD - utvikler.bat» (hopp til rom eller last lagret spill, i vindu), `tools/romtest.py --lagret MAPPE`, testkroken `DIGHD_TEST_SCRIPT` (14. oktober)
- [ ] Tom lagrer i hvert nytt område under gjennomspillingen og sender lagrede spill; romtest `--lagret` på dem tester de 12 rommene som henger etter testhoppet
- [x] Hvilke kostymer som er Sam, Max og de andre (`docs/figurer.csv`, 13. oktober)

### Motor (`docs/HD-MOTOR.md`)

- [x] Slå på DigHD for `GID_SAMNMAX` (10. oktober)
- [x] Rom og objekter, testet med `nearest`-mod (0 avvik, `engine/test.sh`) og romtest i alle rom
- [x] Kroker for figurer i `ClassicCostumeRenderer` (testet i kontoret og med `DIGHD_TEST_COSTUME=2`)
- [x] Merkene per piksel i v6, der teksten legges over i `_compositeBuf` (`blitVirtScreen` med `vsSrc`)
- [x] Blast-objekter (bildet som faktisk tegnes; testet i rom 68)
- [x] Pekeren (`ScummEngine::updateCursor`), ikke sett på skjerm
- [x] Ctrl+H bytter HD og klassisk
- [x] Tekst i `CharsetRendererClassic` (HD-glyfer som i The Dig), med eget lag for tekstlaget i v6 (14. oktober)
- [x] Menyvalget HD Graphics i originalmenyen for v6 (14. oktober, testet med F5 og klikk)
- [x] Sjekk om blast-tekst brukes i Sam & Max: nei, bare blast-objekter (14. oktober)
- [ ] Romtest: finn en måte å komme inn i de 12 rommene som henger etter testhoppet (lagret spill eller objekttilstander). Sjekket 14. oktober: rom 11 stopper på «state -1 is out of bounds» og rom 50 på «readArray: invalid array 261», fordi variablene ikke er satt uten vanlig spill. Krever lagrede spill fra en ekte gjennomspilling
- [x] Test The Dig med den utvidede patchen (15. oktober): patchene slått sammen, felles patch i begge repoer (Dig-PR)
- [x] Piksler rundt HD-figurene (Toms skjermbilde 14. oktober): kantene på skalerte figurer merkes nå riktig, og ruter uten HD-bilde i kostymer med myke ruter glattes i motoren (15. oktober)
- [x] Kanten mot forgrunnen (z-masken) glattes med xBR (15. oktober)
- [x] Ressursbanken (`docs/GJENNOMGANG.md`) sendt til `gpt-arbeid` som GJENNOMGANG.md, med lenke i AGENTS.md der (15. oktober)
- [x] Små svarte felt i rom 8 og 28: forskjeller i ChatGPTs maling (mørkebrune partier i rekkverket malt nesten svart), ikke motoren. Til grafikkordren
- [ ] Grafikkordre: animasjonstilstander som bare er lapper (flaggene og propellen i rom 17, 19 objekter i alt) må tegnes som hele bilder og klippes etterpå; inventaresken (obj995) trenger egen alfa så kanten blir myk; obj049 (LucasArts-logoen) har magentaflekker fra ChatGPT; ikonene i rom 93 og 94 er Scale4x til ikonarkene er tegnet
- [x] Ny grafikk fra `gpt-arbeid` 15. oktober tatt inn: rettede rutekart (920 av 931 ruter), 111 ikoner med egen myk alfa (`smhd myke-ikoner`, PR 24), hd-mod publisert
- [ ] Tom fletter PR 24 (mottaket for myke ikoner), så nettsiden og pakkene bygges på nytt med den nye modden
- [x] Linux-pakken bygget på nytt med modden fra 15. oktober (release «linux», 15:57)
- [x] PR 26 flettet
- [x] Importpakken 15. oktober 16:17 tatt inn (`smhd importpakke`, PR 28), hd-mod og Linux-pakken oppdatert
- [ ] Tom fletter PR 28
- [ ] Se bassenget i rom 54 (objekt 833, 834, 836) i spillet; rom 54 henger etter testhoppet
- [ ] obj835 (bart eller åpen munn) venter på Toms avklaring
- [x] Windows-pakken bygget på nytt med den nye modden
- [ ] Se inventaret i spillet med de nye ikonene (testhoppet åpner det ikke; krever lagret spill eller å spille dit)
- [ ] Tom ser på det nye Max-ikonet (obj1008_01) og de andre ikonene
- [ ] 11 figurruter til gjennomsyn (fig091_03 til 05, fig209_03, fig272_02): var målefeil i mottaket (utligger tegnet, men målt bare i originalen). Med versjon 6 er alle 11 ok; se dem i spillet etter neste runde
- [ ] Hakking på nettsiden (Tom 14. oktober). 15. oktober: SIMD i nettbygget (hele skjermen 20 til 30 ms i Chromium), bakgrunnshentingen venter ved grense fra GitHub (429 ga ventetid også for filene spillet trengte). Gjort: HD-pakken hentes i bakgrunnen, fargetoningen er raskere (15 til 11 ms per skjerm), `?adlib` for å sammenligne med MT-32. Tom tester igjen. Nettsiden henter nå HD-pakken i bakgrunnen. Hele skjermen tar 14 til 22 ms å bygge her; i nettleseren kan nedtoninger og rulling bli tunge. Mål med `DIGHD_BENCH` i nettleseren og se på å bygge bare det som er endret ved palettbytter

### Pipeline

- [x] Uttrekket med egne dekodere for SMAP, BOMP og COST (`pipeline/smhd/v6grafikk.py`, `eksport_v6.py`)
- [x] Uttrekk av rom, objekter og kostymeruter som indekserte PNG med JSON, i samme format som The Dig
- [x] `smhd build-mod` med automatisk oppskalering (testet)
- [x] Sammenlign uttrekket med motoren: alle bakgrunnspiksler finner HD-bildet sitt med nearest-mod ("background without HD 0")
- [x] `build-mod` tar med objektbildene i rom uten bakgrunn (rom 81 og 82, 9 bilder), skalert alene (14. oktober)
- [x] `engine/test.sh` og `tools/romtest.sh` med Sam & Max
- [x] Prompter og figurnavn i `gpt.py` og `figur.py` skrevet for Sam & Max (13. oktober)

### Grafikk

- [x] Alle grafikkjobbene laget med hovedark, fast størrelse i figurarkene og egenkontroll (`tools/sjekk_leveranse.py`), 13. oktober
- [x] Jobbene lagt i `gpt-arbeid` (13. oktober, c96f80b)
- [x] PR 4 (grafikkjobbene) flettet til main (13. oktober, e0baba9)
- [x] Stilpilot: hovedark Sam og Max, rom 7 og fig002_01 og fig003_01 levert, kontrollert, sett i motoren og godkjent av Tom; stilankere i `stil/` (godkjent 13. oktober)
- [x] Aktiver bestillingen og første grafikkrunde: gpt-inn, myke figurer, build-mod, romtest, `hd-mod` e85f760 og ny ordre i `gpt-arbeid` (14. oktober)
- [ ] Neste grafikkrunder med `tools/gpt_runde.sh`: avvisningene først, så resten av GRAFIKKLISTE (ikoner 46 av 163, lag 534 av 701, objekter 83 av 86)
- [x] Se på de 15 figurrutene som myke-figurer merket til gjennomsyn (14. oktober): 12 med feil omriss (blant annet Max uten esken) holdes nå utenfor modden og står øverst i ordren; 3 med bare størrelsesavvik er med
- [x] Finn hvor de små svarte feltene i romtesten kommer fra (14. oktober): spredte piksler fra mørke streker grafikeren har tegnet en piksel ved siden av. Romtesten teller nå bare sammenhengende felt; 2 kjøringer igjen (benken i rom 28, en strek i rom 85), begge tegnefeil, ikke motorfeil
- [x] `tools/gpt_gren.sh send` stopper når AGENTS.md i `gpt-arbeid` har linjer som ikke står i `docs/gpt-arbeid-AGENTS.md` (14. oktober)
- [x] Testrom for dynamisk lys på GitHub Pages (`lystest/`, 13. oktober). Tom slår på Pages med GitHub Actions som kilde
- [ ] Dynamisk lys med normalkart og luminansmaske, etter godkjent stilpilot (Tom 13. oktober): valgfritt for spilleren (av som standard, eget valg i menyen), ingen kastede skygger. Prøv først i ett rom (kontoret med lampen) med normalkart regnet ut fra HD-bildene og lyset av og på med en tast. Lyset legges inn før fargeforholdet fra paletten, så nedtoning og blink fortsatt virker. Rommene har lyset malt inn, så det må vurderes i spillet om det løfter eller bare endrer

### Spillbart for Tom

- [x] `./spill.sh` fra repoet (starter originalspillet)
- [x] Linux-pakken: bygget fra main (407d763) og testet 15. oktober: AppImage lastet ned fra releasen, pakket ut og kjørt uten skjerm i rom 17 (HD-modden, Atkinson, MT-32)
- [x] Windows-pakken: arbeidsflyten Windows-pakke bygger ScummVM med HD-patchen i MSYS2, legger ved spillet og HD-modden og publiserer release "windows" (14. oktober)
- [ ] Tom tester Windows-pakken
- [x] Nettsiden: repoet `Sam-Max-HD-Web` med arbeidsflyt som bygger og publiserer (14. oktober). Siden henter spillet uten nøkkel
- [x] Nettsiden publisert på https://tombonator3000.github.io/Sam-Max-HD-Web/ (14. oktober); testet i Chromium uten skjerm
- [ ] Tom tester nettsiden på PC og mobil
- [ ] Windows-pakken starter ikke på Toms jobb-PC (startfila lukker seg); startfilene viser nå feilkode og logg (%APPDATA%\SamMaxHD\scummvm.log)
- [x] MT-32-musikk (14. oktober): motoren bygges med `--enable-mt32emu`, ROM-filene fra spilldata ligger i Linux- og Windows-pakken, og `engine/run.sh`, startfilene, AppImage og nettsiden velger `--music-driver=mt32`
- [x] `--enable-mt32emu` (14. oktober)
- [ ] Kodeoppgave: avgrens romnotatet for rom 71 i `docs/gpt-romnotater.csv`, som feilaktig ber om "PUSH ME!" for hele rommet. Skiltteksten varierer mellom tilstandene og skal kopieres fra originalreferansen; lag071_05/obj719_01 viser "$1.00 EACH". Undersøk først hvordan endret romnotat påvirker prompt-hasher, ny ordre og allerede godkjente jobber. Bevar riktige leveranser og aktive beskyttede prompter; gjør eventuell regenerering i en ledig fase og la Codex kontrollere endringen. Dette er en konkret feil i grafikkgrunnlaget innen nattens kodeoppdrag. Returordren har overstyrt romnotatet i den nå godkjente rettingen.

## Senere

- [ ] Vurder én felles kode-repo for alle LucasArts-HD-spillene (tanken fra 9. oktober), når Sam & Max og Zak trenger samme motor
- [ ] Slå på push-utløseren i `.github/workflows/linux.yml` når HD virker
