# Fire lagjobber, 16. oktober 2026

Levert: 4 ark med 8 objektbilder. Visuelt kontrollert av Codex: 4 ark. Importert i denne økten: 0. Motoravspilling: ikke utført. Toms godkjenning: ikke innhentet. Alle fire sluttleveranser har OK i egenkontrollen. Claude må kontrollere importerte objekter og tilstander mot faktisk HD-rom før mottaket godkjennes.

Arbeidet følger de fire første jobbene i ORDRE.md datert 16. oktober klokken 01:04. Ingen av disse hadde retur.md. Det er ikke tatt andre produksjonsjobber eller gjentatt kontroll av PR32.

| Jobb | Forsøk | Skift | Største blokkavvik | Kantlikhet | Utfall |
| --- | --- | --- | --- | --- | --- |
| lag032_03_del1av2 | 1 | 0,02 | 0,15 | 0,95 | OK |
| lag035_01_del1av2 | 2 | 0,05 | 0,58 | 0,95 | OK |
| lag035_02_del2av2 | 1 | 0,03 | 0,26 | 0,95 | OK |
| lag041_01_del1av2 | 2 | 0,17 | 0,60 | 0,92 | OK |

Skift og blokkavvik er i originalpiksler. Kontrollutskriftene ligger ved siden av denne rapporten med jobbnavnet og suffikset -kontroll.txt.

## Filer og promptgrunnlag

Verktøyet var innebygd image_gen. Eksakt modellnavn var ikke eksponert. Alle fire første forsøk brukte prompt.txt ordrett, referanse.png som bilde én og jobbens bilde_to som bilde to. Korrigeringsforsøk brukte i tillegg forrige kandidat som bilde tre. Korreksjonspromptene er bevart i denne rapportmappen.

| Leveranse og notat | Første prompt | Endelig prompt |
| --- | --- | --- |
| [lag032_03_del1av2](../../jobber/lag032_03_del1av2/notat.md) | [prompt.txt](../../jobber/lag032_03_del1av2/prompt.txt) | samme |
| [lag035_01_del1av2](../../jobber/lag035_01_del1av2/notat.md) | [prompt.txt](../../jobber/lag035_01_del1av2/prompt.txt) | [forsøk 2](prompt-lag035_01_del1av2-forsok2.txt) |
| [lag035_02_del2av2](../../jobber/lag035_02_del2av2/notat.md) | [prompt.txt](../../jobber/lag035_02_del2av2/prompt.txt) | samme |
| [lag041_01_del1av2](../../jobber/lag041_01_del1av2/notat.md) | [prompt.txt](../../jobber/lag041_01_del1av2/prompt.txt) | [forsøk 2](prompt-lag041_01_del1av2-forsok2.txt) |

Hvert resultat ligger som resultat.png i samme jobbmappe som notatet. [leveranser.json](leveranser.json) angir alle filstier, SHA256, bilde to, forsøk og kontrollstatus. [kildehash.json](kildehash.json) inneholder SHA256 for de 16 beskyttede jobbfilene. Alle 16 er også sammenlignet byte for byte med HEAD og er uendret.

Sluttbildene er 1536 x 1024 med eksakt flat #808080-ramme over y=0..111 og y=912..1023. Pillow ble brukt til denne rammen. Ingen skalering, geometriwarp eller sammensetting er brukt i sluttleveransene. Et forkastet sammensettingsforsøk for Frog Rock fikk synlig skjøt og er ikke levert.

## Motiv og tilstand

Originaler, HD-rom, objektuttrekk og ressursbanken er undersøkt før tegning. Spillet er engelsk CD-utgave. Rommene 32, 35 og 41 har én palett hver, kontrollert i eksisterende work/extract/rooms.json. Objektuttrekkenes kontaktark er [objektgrunnlag.png](objektgrunnlag.png). Original og sluttbilde er vist ved siden av hverandre i [sammenligning-1-3.png](sammenligning-1-3.png) og [sammenligning-4.png](sammenligning-4.png).

Fiskedekket bevarer grønt fiskeinnhold i den gule beholderen, tilstand obj317_02. World of Fishs første lag viser tom plass etter venstre bøtte, to ulike fiskeposisjoner og vannkrusning. Første kandidat arvet en ekstra bøtte fra HD-rommet og fikk FEIL på obj322_01. Den ble erstattet med en korrigert generering. Andre lag viser obj329_01, fisken på nettet vendt mot venstre. Disse tilstandene er kontrollert hver for seg.

Frog Rock viser obj384_01, en helt opak lapp med tom vei og himmel etter bilen. Originalens tomme veitilstand går foran bilen i HD-referansen. Første kandidat fikk SJEKK med blokkavvik 1,06. Andre kandidat strammet skyformene og fikk OK.

Til neste runde: originalreferansen til Frog Rock har et lite brunt innslag på steinen helt til høyre, som ikke er med i HD-rommet eller dette sluttbildet. Det ligger utenfor obj384_01. De neste jobbene lag041_01_del2av2 og lag041_02_del2av2 dekker obj385_01 og obj385_02 ved denne steinen. Kontroller riktig betydning, innhold og tilstand der før tegning. Ikke bruk denne leveransen som fasit for det motivet.

## Arbeidsmiljø og overlevering

Grenen er gpt-arbeid. Utgangspunktet er 0a150fb93ef6286101390c3e7ea38ec0d84d1b39. Git pull ble forsøkt, men Git kunne ikke skrive FETCH_HEAD i /home/tom/Sam-Max-HD/.git/worktrees/-gpt-gren, som er utenfor sandkassens skrivbare område. Det er ikke gjort commit, push, grenbytte, PR eller fletting.

Systemets python3 manglet NumPy. Kontrollen ble derfor kjørt med prosjektets eksisterende miljø, uten installasjon:

```sh
PATH=/home/tom/Sam-Max-HD/.venv/bin:$PATH python3 verktoy/sjekk_leveranse.py jobber/<jobb>/resultat.png
```

Ingen kode er endret, og ingen konkret ny kodeblokkering ble påvist. Nattløpets skript må committe de fire resultatene, notatene og denne rapportmappen, deretter la Claude kontrollere og importere dem. Teknisk OK og Codex sin visuelle kontroll er ikke motoravspilling eller Toms godkjenning.
