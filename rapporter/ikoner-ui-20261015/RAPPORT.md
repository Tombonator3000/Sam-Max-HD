# Verb- og inventarikoner, 15. oktober 2026

Toms prioritering: start med ikoner til verbhjul og inventory. Dette går foran rekkefølgen i ORDRE. Tom ga også uttrykkelig ja til Python for rensing og presis plassering av de nytegnede ikonene.

## Leveranse

- `jobber/ikon07/resultat.png`: 22 bilder, inkludert 16 handlingspekere og seks andre spillbilder på det blandede originalarket.
- `jobber/ikon08/resultat.png`: fem handlingspekere og 42 inventar-/samtalebilder.
- `jobber/ikon09/resultat.png`: 48 inventar-/samtalebilder.
- `ikoner/verb-og-pekere/`: 21 separate RGBA-bilder fra rom 93.
- `ikoner/inventar-og-samtale/`: 90 separate RGBA-bilder fra rom 94.
- `ikoner/verbhjul/`: navngitte kopier for se, ta, snakk, bruk og inventar.
- `ikonmanifest.json` og `handlingsmanifest.json`: ressurs-ID, fil, mål, sjekksum og kobling til handling/alternativ peker/menyikon.
- `verbhjul-forhandsvisning.png`: forhåndsvisning av de fem grunnikonene.

Dette er grafikkleveransen. Selve verbhjulgrensesnittet er ikke implementert, og motor, pipeline og hd-mod er ikke endret.

## Kilder og avklaringer

Originalene og jobbmetadata er bevart. Originalens motiv og ruteplassering styrer innholdet. De godkjente rom-/figurankrene styrer tegnestilen. Ingen originalpiksler eller originalkonturmasker er brukt som ferdig grafikk.

For å løse de gamle motivspørsmålene ble SAMNMAX.000 og .001 hentet fra spilldata, og 1181 skript dekompilert med Ubuntu-pakken scummvm-tools 2.9.0-1build4. 1179 ble lest uten feil; de to kjente 0xBD-feilene består. Ingen spilldata eller nye skriptkopier er lagt i main. Koblinger til ikon-ID, objektskript, replikker og SHA-256 står i `ikon-identitet-fra-skript.json`.

Eksempler på rettede premisser:

- 891/892 er hvite Car Bomb-pekere, ikke manglende tegningsdetaljer.
- 1009 viser Cone of Tragedy.
- 1017 er oppdragspapirene/billettene fra kommissæren, ikke en tang.
- 1021 er humørringen.
- 1024 er pekannøttgodteri, 1026 til 1028 er forskjellige Bigfoot-hår-/skabbklumper, 1029 er føflekkmannens beholder, 1030 er hyssing.
- 1038 er tjære. 1040 er penger, ikke kikkert. 1042 er John Muir-grønnsaken, 1043 puten, 1044 robotmanualen og 1045 John Muir-portrettet.
- 1053/1054 er VR-sverd/nøkkel, 1055 Conroys tupé, 1057/1058 ishakke/korketrekker og 1060 kork.
- 1080 viser restaurantens ledninger/mekanisme.

Skript 1 setter menyikonene 879, 880, 881, 882 og 888. Skript 48/51 kobler se til verb 4, ta til 5, snakk til 6 og bruk til 3, med egne pekerbilder når handlingen ikke er tilgjengelig. Disse koblingene er bevart i manifestet, uten endring av spillreglene.

## Produksjon

Seks innebygde image_gen-kall. Eksakt bildemodellnavn var ikke eksponert. Fire råbilder bidrar til leveransen: tre grunnark og ett større rettingsark med tolv motiver. To andre rettingsforsøk ble forkastet, blant annet et forsøk som falt tilbake til pikselgrafikk. Sendte prompter og råbilder er bevart.

Første generering ga blant annet generisk Max-ansikt, ny Gator-tekst, feil totemmotiv og påfunn på noen portretter. Tolv motiver ble derfor generert på nytt som større komponenter. Valgte nye komponenter er renset for grønn bakgrunn og plassert etter originalens synlige bokser. `klargjor-ikoner.py.txt` gjenskaper leveransen. Både kildeidentiske fragmenter og de fire tomme beige kortene gjenbruker samme nye bildebytes.

Arkene er RGB 1536 x 1024 med bytepresis grå ytterkant og flat grønn bakgrunn. Magenta er ikke brukt som nytt fyll. De separate objektene har egen myk alfa. Originalboksene brukes til mål og plassering, ikke til å klippe tegningens omriss.

## Kontroll

- Alle tre faktiske resultat.png gir OK i uendret sjekk_leveranse.py.
- 117 metadatafelt er tatt med i fem original/HD-sammenligningsark og visuelt gjennomgått.
- 111 eksporterte ikoner har riktig RGBA-format, native mål, entydig ID og verifisert SHA-256.
- De kildeidentiske gruppene 1000/1002/1003, 1007/1012/1014 og 1064/1065/1066/1067 er eksportert byteidentisk.
- Alle 12 beskyttede jobbfiler er uendret.
- Grønn fargeforurensning langs noen mørke alfakanter ble rettet ved matting mot den nye tegningens innvendige farge.

Teknisk OK er ikke individuell godkjenning fra Tom. Nytegningen tolker små former, ansikter, totemglyfer og ulest tekst; sammenligningsarkene gjør disse valgene synlige.

Mottak i smhd gpt-inn, bygging av ny hd-mod og avspilling i spillet er ikke utført. Dagens ikonmottak bruker fortsatt originalens alfa ved import. De separate RGBA-filene bevarer den nye glatte alfaen for verbhjul/inventar; kontroller importens kanter og nøkkelfarge før de brukes i en ny spillpakke.

