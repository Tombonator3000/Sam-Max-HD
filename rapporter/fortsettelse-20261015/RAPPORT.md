# Fortsettelse av grafikkarbeidet 15. oktober 2026

## Levert

Rutekart for alle 73 leverte figurark, 931 ruter. Mottaket i main kunne tidligere lese kart for bare 2 ark. De andre kartene manglet, hadde en annen struktur eller brukte feltnavn mottaket ikke leser. Det falt da tilbake til radgjetting, som utelot små, separate deler.

De åtte `rutekart-*.json`-filene bruker mottakets eksisterende format: jobbnavn, `ruter`, `bilde` og `rect: [x,y,bredde,høyde]`. Hver boks omfatter alle sammenhengende kjerner som tilhører ruten, også løsrevne hender, øyelokk og rekvisittdeler. Ingen PNG-er, beskyttede jobbfiler, motor- eller pipelinefiler er endret.

## De 12 returrutene

Alle de 12 rutene øverst i ORDRE hadde to tegnede komponenter. Radgjettingen tok bare med én. Kartene kobler nå begge:

- fig002_05: costume002_257 til costume002_261.
- fig004_01, fig007_01 og fig236_01: rute 256.
- fig091_03: rute 1953.
- fig091_04: rute 1956.
- fig091_05: rute 1963 og 1966.

Sams lille hånd var altså tegnet i atlaset. Den forsvant ved tilordning av delene, ikke fordi PNG-en bare inneholdt én hånd. For costume004_256 økte direkte omrissdekning fra 71,3 til 91,3 prosent. Snitt/union økte fra 0,638 til 0,803. Målingene for alle 12 ligger i `returruter-kontroll.json`. Dette er analyse av atlaset før mottakets skalering og plassering, ikke en spilltest.

## Kontroll

- Det uendrede mottakets `route_maps` leser nå alle 73 kart.
- `parts` og `assign_by_map` kobler hver tegnet alfakjerne til nøyaktig én rute. Ingen kjerner blir utelatt eller delt mellom ruter.
- Alle 931 rutene har en boks. Kildesjekksummene for 365 filer er uendret, inkludert de 73 leverte PNG-ene.
- Egenkontrollen er kjørt på alle 73 eksisterende ark: 69 OK, 4 SJEKK, ingen FEIL. SJEKK gjelder fig003_03, fig007_03, fig007_06 og fig066_03. Tidligere dokumenterte tegningsavvik er beholdt.
- Alle 12 returrutene har etter ny tilordning minst 80 prosent direkte omrissdekning og snitt/union minst 0,6.

Kontrollen er gjentakbar med `lag-rutekart.py.txt` og `sjekk-returruter.py.txt`, Python med numpy, Pillow og scipy, og main/pipeline i PYTHONPATH. Skriptene leser bilder og skriver bare JSON. De endrer ingen bildebytes.

Det er ikke kjørt nytt fullstendig `myke-figurer`-mottak, bygd ny hd-mod, publisert nye spillpakker eller avspilt animasjonene i motoren. De 12 rutene skal derfor prøves gjennom mottaket før returlisten krysses av. Ingen ny individuell bildegodkjenning er påstått.

## Tidligere arbeid og gjenværende filer

65 fremdriftsrapporter og den siste ordren fra 15. oktober er gjennomgått. Den opprinnelige chatten var ikke tilgjengelig i denne økten. Brukeropplysninger, godkjente hovedark, stilpilot og tidligere kildeavklaringer er bevart i repoets rapporter og analyse.

Filstatus ved kontrollen, som ikke er det samme som mottaksgodkjenning:

| Type | Har resultat.png | Mangler resultat.png |
| --- | ---: | ---: |
| Romjobber | 115 | 0 |
| Store objekter | 86 | 0 |
| Lagjobber | 268 | 28 |
| Ikonark | 6 | 3 |
| Figurark | 73 | 1685 |

Alle rom- og objektjobber har altså filer, men ORDRE inneholder fortsatt avviste leveranser og kjente tegningsfeil. Fig002_06 og fig007_02 er blant de ufullstendige figurarkene.

## Nye bildeforsøk som ikke er levert

Seks innebygde image_gen-kall er gjort: tre håndforsøk og ett forsøk hver på obj187_05, obj307_01 og obj811_01. Ingen av disse erstatter eksisterende resultat.png. Håndforsøkene ga farget alfaslør og endret andre deler; objektforsøkene fikk FEIL på blokkforskyvning. De gamle leveransene er beholdt, og råforsøkene er lagret lokalt. Eksakt bildemodellnavn var ikke eksponert.

Obj307_01s generiske romprompt nevner landskap og myntspor, men det aktuelle objektet er bare øvre metallstripe av kikkerten, med to skruer. Et separat kildekorrigert promptnotat er bevart; den beskyttede prompten er uendret. Obj811_01 viser midtstripen av kikkertfronten og Sams hender med tomt svart bildefelt.

Neste grafikkarbeid følger ORDRE: nytt mottak av rutekartene først, deretter avviste objekt- og lagjobber, hele lapp-tilstander, obj995s alfa/tekst, ikonarkene og figurarkene. Motivavklaringer som allerede er dokumentert gjelder fortsatt.

