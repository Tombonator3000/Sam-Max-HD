# LeChuck Pizza: brukeravklart retting

Tom avklarte 13. oktober 2026 at pizzaesken skal si «LeChuck Pizza», en Monkey Island-referanse. Ett nytt innebygd imagegen-kall erstatter den feiltolkede etiketten i begge leverte rom070-deler. Root har lest den nye teksten og sett den i hele kostymegruppen. Begge faktiske resultatfiler er teknisk OK med uendret checker. Ingen runtime eller ny individuell godkjenning av selve rettingsbildet er påstått.

Bare masterfelt [1290,48,200,84] er endret: 16 114 RGB-piksler, null utenfor. Masteren er 1920 × 800, med klipp x = 0 og 384. Overlapp 1152 × 800 er byteidentisk. De åtte beskyttede original-/referanse-/prompt-/metadatafilene er uendret. Historiske rapporter og mastere fra bestilling 17 beholdes som bevis for den tidligere leveransen; aktuell master, hasher og kontroll er i denne rapporten og de to jobbnotatene.

`prompt-01.txt` inneholder ordrett jobbprompt og separat brukerrettelse. `raa-01.png` er det nye imagegen-resultatet. `oppskrift.py.txt` reproduserer smalt nytt innklipp med hel nedskalering og 2 px rektangulær fjæring mellom nytegnete bilder. Ingen originalmasker, kildepiksler som ny kunst, warp eller vektortrace. Eksakt bildemodell er ikke eksponert.

## Berørte senere lag

Read-only sporing av originaler og metadata bekrefter følgende. Disse lagene er foreløpig ikke levert:

- Rom070/obj690 er [288,8,96,64], på HD-lerret del1 [1152,144,384,256] og del2 [768,144,384,256].
- Lag070_01 viser fravær/silhuett av pizzaantrekket, med to kildefarger og 3003 endrede originalpiksler i feltet. Esken skal ikke legges tilbake der.
- Lag070_02 begge deler og lag070_03 del1 har kildeidentisk boks690 med grunnrommet, og skal arve den korrigerte esken.
- Lag071_06 har Max med den samme esken, obj750_01, romrektangel [200,104,96,64], HD [928,528,384,256]. Nytegningen skal bruke den avklarte teksten.
- Lag071_02/pizzalue og lag071_12/pizzastykke er egne rekvisitter. Navnene gir ikke grunnlag for å legge inn mer tekst der.

## Ny regel og andre direkte avklaringer

Tom ba uttrykkelig om spørsmål når motivets betydning er uklar. Dette gjelder videre arbeid i oppdraget. Uavklart innhold holdes igjen mens uavhengige, avklarte jobber fortsetter.

Etter spørsmål med originale utsnitt avklarte Tom samtidig at obj260_01 er stangfot på brygga, og obj269_01 er søl eller vannplask fra Dunk the Beast-tanken. Dette er ført videre til agentene og kildeplanene for bestilling 30/31. Det erstatter tidligere funksjonsusikkerhet; det gir ikke grunnlag for å legge til nye detaljer utenfor de faktiske kildene.
