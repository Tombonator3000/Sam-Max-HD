# Status

16. oktober 19:35: Arbeidsmodd hd-mod 9fbf5a67 er publisert og hentet tilbake med SHA256SUMS-kontroll: 1134 native figurruter, 39 flere enn a6c286bd. Tilleggene er 38 Sam-ruter i VR-verdenen og den lille inventory-esken, costume001_002. Tidligere grafikk er bevart byteidentisk. Esken er sett i spillet med inventaret åpnet/lukket, 280 bilder uten skjermbufferavvik. Sam-rutene er registrert og sett i tvunget motoravspilling. Munndelen costume249_257 er fortsatt holdt ute fordi motorbildet viser pikseltrinn og dårlig skjøt. Kunstig hopp til rom49 gir et kort ekstra skjermbufferavvik som må undersøkes; naturlige rombytter er ikke kontrollert. Ingen ny motorkode publisert. Nedlastingspakkene har fortsatt a6c286bd og 1095 native ruter. Direkte opptelling: 105 av 1758 figurjobber har resultat, 1653 mangler, og noen leverte ark trenger retting. [Grafikk, før/etter og kontrollrapport](https://github.com/Tombonator3000/Sam-Max-HD/tree/gpt-arbeid/rapporter/figurer-videre-20261016).

16. oktober 12:29: [Felles Linux- og Windows-utgave](https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/sam-max-hd-2026-10-16) er publisert som Latest. Begge bruker kode 9b5a9197 med PR32 og hd-mod a6c286bd, 1095 native figurruter. Linux er bygget på nytt, og begge pakker er lastet ned og sjekksumkontrollert. Alle 19 336 moddfiler er byteidentiske mellom pakkene. Linux består oppstart og Debian 12; inventar, akvarium og cafeteriarør er kjørt og sett med null skjermbufferavvik. Første akvariumstart i SDL dummy feilet før spillet lastet; prøve med pakkens motor og minimal ini består. Windows består automatisert HD-/MT-32-oppstart, men interaktiv spilling er ikke kontrollert her. Nettutgaven er allerede oppdatert med PR32. Øks-/bakgrunnsrester, hele animasjonsforløp, faktisk opptak og bilavreise gjenstår. [Kontrollrapport](https://github.com/Tombonator3000/Sam-Max-HD/blob/gpt-arbeid/rapporter/felles-release-20261016/RAPPORT.md).

Oppdatert 14. oktober 2026.

## Kort

Repoet har samme oppsett som The Dig HD Remake, kopiert og tilpasset Sam & Max. Spillfilene ligger i `spilldata`, ScummVM med HD-patchen bygger og kjører spillet, all originalgrafikken er trukket ut, alle skriptene er dekompilert, og HD-motoren er på for Sam & Max: rom, objekter, blast-objekter, figurer og teksten får HD fra en mod, og HD Graphics kan slås av og på i originalmenyen (14. oktober). All grafikken er klargjort som jobber til ChatGPT (13. oktober). Første grafikkrunde er tatt inn 14. oktober: 76 rom, 841 objektbilder og 919 figurruter i HD ligger i `hd-mod` (24f561d, 14. oktober; 12 ruter med feil omriss holdes ute), resten vises som originalen.

## Det som virker

| Del | Hva | Hvordan det er testet |
| --- | --- | --- |
| Spillfiler | SAMNMAX.000, SAMNMAX.001, MONSTER.SOU (i to deler) og de to MT-32-ROM-filene i `spilldata`, hentes og sjekkes med `tools/hent_spilldata.sh` | Fersk klone av main 86952bf og `tools/hent_spilldata.sh` 10. oktober: MONSTER.SOU satt sammen, SHA-256 for alle fem filer stemmer |
| Utgave | Engelsk CD-utgave | MD5 av SAMNMAX.000 funnet i ScummVMs `scumm-md5.h` |
| Motor | ScummVM c9091321 med `engine/patches/0001-dighd-hd-grafikk.patch` (The Dig sin, utvidet for v6) | `engine/build.sh` og `git apply --check` mot c9091321 her 10. oktober. Spillet kjører fra `game/` uten skjerm |
| HD i motoren | Rom, objekter, blast-objekter og kostymeruter (klassiske kostymer) får HD fra modden. Pekeren går gjennom DigHD. Ctrl+H bytter | `engine/test.sh`: 0 avvik og "background without HD 0" i alle dumper. Romtest i alle 85 rom med nearest-mod: 62 rom ok, 0 krasj, 0 forskjøvet, 0 skjermavvik; 12 hang etter testhoppet (skriptfeil uten riktig spilltilstand). Figurer i kontoret: 0,26 til 0,29 prosent avvik i kantene av skalerte figurer. Blast-objektene i rom 68 med HD. Ikke testet med skjerm |
| `./spill.sh` | Henter spillfiler og `hd-mod`, bygger motoren og starter spillet | Kjørt her uten skjerm: tom `hd-mod` hentet, motoren bygget, spillet startet uten mod med `--programvare` (OpenGL finner ingen grafikkmodus uten skjerm) |
| Pipeline | `smhd info` og `gamedata.py` leser v6 (XOR 0x69) og v7 | `smhd info` mot spillfilene: 85 rom, 63 med z-plan, 43 med sykling, 959 objektbilder, 348 kostymer. `pytest` 13. oktober: 40 tester uten spillfiler og 3 med, alle bestått |
| Nettsidekoden | `engine/pages` tilpasset Sam & Max (filfilter, MONSTER.SOU-deler, samnmax) | `node --test`: 16 bestått. Ikke bygget for nettleser |
| Linux-pakken | `tools/pakke_linux.sh` lager pakken uten HD-mod | AppDir laget her og startet uten skjerm: spillet kjente igjen utgaven og kjørte. AppImage og arbeidsflyten er ikke kjørt |
| Indeksverktøy | `tools/indeks_info.py game/SAMNMAX.000` | Kjørt mot spillfilene |
| Uttrekk | `smhd extract`: 83 rombakgrunner, 959 objektbilder (856 SMAP, 103 BOMP), 16 052 kostymeruter fra 348 kostymer, med rooms.json og costumes.json | Kjørt mot spillfilene 10. oktober, 0 feil. Alle rom og ett bilde fra hvert kostyme sett på i kontaktark; rom 2 med objektene på plass stemmer. Enhetstester for alle kodekene og en game-test med tellingene. Ikke sammenlignet piksel for piksel med motoren |
| Skript | `tools/bygg_descumm.sh` og `tools/dekompiler_skript.py`: 1181 skript til `work/skript` | 1179 uten feil, 2 stopper på opkoden 0xBD (ingen virkning i v6). Talereplikker, skriptnumre og romnumre kontrollert mot spillfilene |
| Grafikkjobber | `smhd gpt-pakke --figurer alle`: 2 hovedark (Sam, Max), 115 romjobber for 76 rom, 86 objektjobber, 296 lagjobber (701 bilder), 9 ikonark (163 bilder) og 1758 figurark (15 661 ruter fra 343 kostymer). `smhd gpt-ordre` skriver ORDRE.md med bare stilpiloten til stilankerne finnes | Laget mot spillfilene 13. oktober i `work/gpt`. Stikkprøver av referanser og prompter sett på. Ikke sendt til grafikeren, ingen bilder laget ennå |
| Egenkontroll | `tools/sjekk_leveranse.py` sjekker en leveranse før grafikeren committer: forskyvning og kanter for rom, objekter, lag og ikoner; størrelse, plass og omriss per rute for figurark; høyder for hovedark | Testet med syntetiske leveranser (riktig gir OK, rute 15 prosent for stor gir FEIL, rom forskjøvet 3 px gir FEIL) og i `pytest`. Ikke prøvd på ekte ChatGPT-bilder |
| Myke figurer | `myk.py` versjon 6: skalerer og plasserer hver rute etter originalen og merker grupper der tegnet størrelse spriker mer enn 12 prosent. Ved flere leveranser av samme jobb velges den med sha256 lik filen. Løse utliggere (Sams fotrest i kostyme 91) måles med på begge sider når grafikeren har tegnet dem | Enhetstester med syntetiske ark. Kjørt på ekte leveranser 15. oktober (til en midlertidig mappe, ikke i modden): 931 ruter ok, 0 til gjennomsyn (før 920 og 11). Ikke sett i spillet |
| Kostymepaletter | `tools/kostymer.py` finner rommene hvert kostyme brukes i fra skriptene; `docs/kostymefarger.csv` gir 8 kostymer riktig palett i uttrekket. Skyggepiksler (indeks 13) tas bort fra figurarkene | `smhd extract` kjørt på nytt; game-test sjekker paletten for Sam. Rom 92 sett i motoren med samme farger som uttrekket |
| build-mod | Mod med automatisk oppskalering fra uttrekket | `smhd build-mod --method lanczos --kostymer 2,3`: 83 rom, 950 objektbilder, 175 kostymeruter. Objektbildene i rom 81 og 82 (ingen bakgrunn) tas ikke med |
| HD-tekst og menyraden | Teksten på skjermen og i originalmenyen tegnes med HD-skriften; HD Graphics står i originalmenyen (F5) | 14. oktober: introen med undertekster og menyen med `DIGHD_VERIFY` (0 piksler ikke bygget på nytt), klikk på HD Graphics gir klassisk grafikk, `engine/test.sh` 0 avvik. Romtest i alle 85 rom med den nye motoren og modden: 71 lastet, 61 ok med HD-bakgrunn, 0 krasj, 0 forskjøvet, 0 skjermavvik, svarte felt i 2 kjøringer (tegnefeil), 11 hang etter testhoppet som før. Ikke spilt med skjerm |
| HD-mod fra grafikeren | `smhd gpt-inn`, `smhd myke-figurer` og `smhd build-mod --egne work/gpt-ferdig`, publisert med `tools/mod_gren.sh send mods/gpt` | 14. oktober: gpt-inn godkjente 419 leveranser (31 til sjekk, 26 avvist). Romtest med modden: 71 av 85 rom lastet, 61 ok med HD-bakgrunn, 0 krasj, 0 forskjøvet, 0 skjermavvik; 11 hang etter testhoppet som før; små svarte felt (17 til 78 px) i 24 kjøringer. Kontoret sammenlignet med originalen: riktig, bare inventarikonet er fortsatt originalt. Ikke spilt med skjerm. 15. oktober 14:30: ny runde med de rettede rutekartene og ikonene: 76 rom, 958 objektbilder (111 ikoner med egen myk alfa, `smhd myke-ikoner`, PR 24) og 923 figurruter, publisert i hd-mod. Pekeren i rom 7 sett uten skjerm med det myke ikonet. Inventaret ikke sett i spillet. 16. oktober: manuelle avvisninger i `docs/gpt-avvisninger.csv` gjelder også figurark med ekte alfa (1ec0d92f); avvist SHA gir retur i ORDRE, ny SHA gir levert. Testet med regresjonstest og `pytest` (65 grønne, med game/), kontrollert av Codex. Tatt i bruk i full `gpt_runde.sh` 16. oktober 07:36 til 07:46 |

## Ikke portet eller ikke testet

- The Dig er ikke testet med den utvidede patchen her (filene er ikke i dette repoet).
- Kostymefargene: åtte kostymer har fått paletten fra rommene de brukes i. Resten bruker hjemrommet, som stemmer for de fleste, men er ikke sjekket kostyme for kostyme i spillet. Rulletekstpanelene (objekt 600 til 603, lånt fra rom 67) er sett i rom 77 med HD 14. oktober.
- Promptene i `gpt.py` og `figur.py` er skrevet om for Sam & Max, men ikke prøvd i ChatGPT. Første runde er levert og tatt inn 14. oktober.
- Figuridentiteten: navnene i `docs/figurer.csv` kommer fra replikkene i skriptene. Den eneste som sto med «trolig» (kostyme 103), er bekreftet som Trixie fra skript 120.
- Spillet er ikke spilt med skjerm og lyd her. Musikken går med Roland MT-32-emulering og ROM-filene fra spilldata (fra 14. oktober); testet uten lydkort (ROM-ene lastes, spillet går 1500 bilder uten feil), ikke hørt.
- Nettsiden: eget repo finnes ikke, ikke bygget eller prøvd.

## Ikonetterkontroll på nattgrenen, 2026-10-16 02:29

Kode 6ea6d4b0 er Codex-kontrollert med 60 pipelinetester og brukt i hd-mod 8f3f82a7. Fire ikon01-bilder er sammenlignet med original og førbilder: kraftig magentaglorie redusert, alfa og størrelse uendret. Små grønne/lilla kantpiksler gjenstår på bilene og er ført til videre retting i todo.md. Før/etter-bilder og hasher er sikret lokalt. Dette er kontroll av PNG-filene, uten motoravspilling eller Toms stilgodkjenning. Nattens kode er ikke flettet til main eller bygget inn i nye Linux-/Windows-pakker.


## Kantrens på nattgrenen, 2026-10-16 04:18

Første trinn ecd9ec0e er brukt i hd-mod 55f976de: uendret størrelse/alfa på alle 163 ikon-PNG og separat Codex-etterkontroll av 22 utvalgte på mørk og lys bakgrunn. Fargerestene er tydelig redusert, men trappetrinn og tynne mørke/lilla streker gjensto. Andre trinn de951ff7 er Codex-kodegodkjent med 63 pipelinetester; nybygd modd og visuell etterkontroll av dette trinnet gjenstår. Ikke motoravspilt, ikke Toms stilgodkjenning, ikke flettet til main eller lagt i nye nedlastingspakker.


## Andre kantrinn i sluttmodd, 2026-10-16 05:18

De951ff7 er brukt i hd-mod 183850f6, med alle 163 ikon-PNG bekreftet byteidentiske også i 037f4298. Alfa/størrelse uendret på alle 163; 47 har justert RGB. Codex har sett 14 PNG på mørk og lys bakgrunn: mørk lilla på biltak redusert uten åpenbar ny skade på ekte farger i utvalget. Trappetrinn og LucasArts-logoens lyse magenta står fortsatt. Ikke motoravspilt, ikke Toms stilgodkjenning eller ny nedlastingspakke.


## VR-hjelmfarger, 2026-10-16 05:53

Fig247_02 er sendt i retur etter separat Codex-kontroll: fire ruter mangler originalens grønne kuppelbånd, som står i de andre kontrollerte arkene. Dette er en konkret farge-/kontinuitetsfeil. Neste import utelater de fire rutene til ny versjon godkjennes. Ingen motoravspilling eller Toms stilgodkjenning.


## Toms godkjenning 2026-10-16 08:45

Tom har godkjent de 72 nattjobbenes konkrete resultater i chatten. Gjeldende SHA-er står i rapporter/godkjenning-20261016/godkjenning.json på gpt-arbeid. Godkjenningen gjelder leveransen, mens dokumenterte gjenværende grafikkfeil og motoravspilling fortsatt må følges opp. Nattkoden er samlet i PR33 med grønn CI. De fire siste figurarkenes notater, fremdrift og rutekart er ferdigstilt fra de bevarte bildene; importresultatet logges etter ordinær mottaksrunde.

Importen 2026-10-16 08:51 er ferdig. Publisert og tilbakehentet hd-mod a6c286bd: 76 rom, 959 objektbilder og 1095 native figurruter. Av de 21 siste rutene er 20 importert og én munndel holdt ute av teknisk kontroll (costume249_257, dekning 0,783). SHA256SUMS og faktisk native pikselinnhold er kontrollert. Alle 72 resultatfiler har uendret SHA fra Toms godkjenning. Ingen ny motoravspilling eller pakkebygging.

PR33 ble flettet av Tom 16. oktober 08:44 etter grønn CI. Nattens pipelinekode er med i main fra 3c6d2572. De etterfølgende godkjennings- og mottakskvitteringene er også registrert her. PR32 for motoren står fortsatt åpen.


## Videre Sam-figurer, 2026-10-16 22:15

Gator Golf fig117_01 til 08 og ny munndel i fig249_02 er levert og importert i hd-mod 9a855936: 92 nye native bilder, 1226 totalt. Alle tidligere PNG-er bevart. 13 tvungne animasjoner, alle 91 Gator Golf-ruter sett i motoren, 390 skjermbufferkontroller uten avvik. Tre egenkontrollmerknader om omriss er dokumentert; separat mottak godtar alle 98 ruter inkludert seks eksisterende gangeruter. Ikke naturlig gjennomspilling, separat Claude-kontroll eller Toms nye stilgodkjenning. Kjent kunstig rom49-hopp med 160 avvik står uendret. Nedlastingspakkene har fortsatt a6c286bd og 1095 native ruter. Se rapporter/fortsett-20261016-kveld på gpt-arbeid for bilder, prompter og per-SHA-kvittering.


## Sam opp ned, 2026-10-17 11:12

17. oktober 11:12: Fem Sam opp ned-ark fig204_01 til 05 er publisert i hd-mod 5212c395 med 64 nye native ruter, totalt 1290. Blinklag og øyeplassering er kontrollert i motoren etter retting. Alle tidligere PNG-er bevart. Denne økten: 13 nye Sam-ark med 155 ruter og én ny munndel, 156 nye native filer. 63 av 64 ruter i opp ned-bunken er sett tegnet; rute286 er ikke observert. 118 av 1758 figurjobber har resultat, 1640 mangler pluss returer. Neste Sam-ark fig307_01. Natt-automatikken er pauset. Plattformpakkene fra 17. oktober har 1226; nye bygg med 1290 er startet.

Egenkontroll 61 OK, én SJEKK om omriss, to små blinkruter kontrollert særskilt. Separat native mottak: 64 OK med uendrede grenser. Alle 64 sett som PNG mot originalene; 63 registrert tegnet i motoren. Fire siste blink-/snakkeprøver av korrigert kandidat har 130 skjermbufferkontroller uten avvik. Ikke naturlig gjennomspilling, separat Claude-kontroll eller Toms nye stilgodkjenning. Kjent kunstig rom49-hopp og andre motiv-/animasjonsfeil står fortsatt åpne. Se rapporter/opp-ned-20261016 på gpt-arbeid.
