# Bestilling 7, samlet rapport

Dato: 13. oktober 2026. Ti resultater er levert. Roots uendrede sluttkontroll gir **9 OK, 1 SJEKK og 0 FEIL**. Alle er RGB PNG på 1536 × 1024 med nøyaktig RGB128-padding og metadataenes motivfelt. Alle 40 beskyttede kilder har uendret SHA-256. Se [sluttkontroll](sluttkontroll.json) og [fremdrift med resultathasher og logger](fremdrift.json).

| Resultater | Antall | Teknisk status |
| --- | ---: | --- |
| rom029, obj294_01, obj295_01 | 3 | OK |
| obj293_01 | 1 | SJEKK |
| rom030_del1av2 og rom030_del2av2 | 2 | OK |
| rom031_del1av4 til rom031_del4av4 | 4 | OK |

Root har sammenlignet [originalkontaktarket](original-kontaktark.png) og [samlet HD-kontaktark](samlet-kontaktark.png). Stilpiloten er godkjent som produksjonsgrunnlag. De ti nye bildene er ikke individuelt visuelt godkjent av brukeren. Import, bygg, runtime og samspill med motorens masker er ikke verifisert.

Objektene 293, 294 og 295 viser den grønne golfballhenteren med Jesse James' inntørkede hånd som griper den røde fiskformede magneten. Den brune delen er hånd, ikke hyssing. Funksjonen er avklart fra søkeutdrag fra LucasArts' originale hintbok, trykt side 43; PDF-åpning feilet på størrelse. Dette er kildebevis, ikke runtime-observasjon. Tilstandenes plasseringer og tildekking av diagonal hyssing er bevart. Obj293 har fortsatt SJEKK med skift 0.89, blokk 1.24 og kantlikhet 0.88, samt små størrelsesavvik i neglspisser og gullledd. Første forsøk ble valgt fordi andre var dårligere. Rom029 har noe tydeligere høylys enn den mørke originalen. Se [A sin kilde-QA](a-kilde-qa.md).

Restauranten i rom030 bevarer SEAFOOD, FRESH FISH, garn, lamper og den tomme blå bakgrunnsflaten. De to delene er klippet fra én master; overlappen på 1408 × 800 piksler er byte-identisk. Små beslag og innholdsdetaljer er ikke bevist detaljidentiske; jevnere skygger og en svak blå gradient er synlige. Se [B sin kilde-QA](b-kilde-qa.md).

Rom031 er landskapslaget uten kikkertinnfatning eller myntsliss. Det feilaktige generiske romnotatet om kikkerten er korrigert i tilleggsprompten, mens beskyttet prompt.txt er urørt. Originalens svarte rektangulære felt inne i landskapsbildet er beholdt. Ingen oppdagede steder eller nye navn er lagt til; det lille skiltets uleselige tegn og den uavklarte grønne formen ved elven er beholdt uten gjettet betydning. Fire rågenereringer er samlet i én master med tre diskrete overganger på 64 piksler. Alle tre nabooverlapper på 576 × 800 piksler er byte-identiske. Små penselmerker er ikke påstått detaljidentiske. Se [C sin kilde-QA](c-kilde-qa.md).

Produksjonen brukte innebygd ChatGPT-bildegenerator og autorisert presis bildebehandling. Eksakt bildemodellnavn er ikke eksponert. Råforsøk, prompter, mastere, oppskrifter og logger er bevart i rapportmappen. Kontrollskriptet og beskyttede kilder er ikke endret.

Forrige bestilling 5 og 6 sine 20 lagrede PNG-filer er SHA-verifisert mot GitHub ved commit `2948b371dec36a5596df1e5080314c986e7f7744`. Dette omfatter også den uttrykkelig merkede FEIL-kandidaten obj187_05 og betyr ikke at den er teknisk godkjent. Se [pushkontroll for bestilling 5 og 6](bestilling005-006-pushkontroll.json). Denne verifikasjonen gjelder ikke en påstått publisering av bestilling 7.
