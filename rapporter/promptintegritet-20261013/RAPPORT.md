# Gjenopprettet promptintegritet

Roots tekstnormalisering la til ett avsluttende LF i17 rapportprompter fra bestilling20–22. C kontrollerte eksplisitte prompt/hash-par og beviste den eksakte byteforskjellen. Root har fjernet bare dette ene LF, kontrollert førhash og gjenopprettet hver tidligere lagret SHA-256. Ingen tekst inne i promptene er endret.

Alle 224 tidligere leverte PNG-er er kontrollert uendret. Beskyttede jobbprompter, originaler og metadata er ikke berørt. Historiske manifestverdier er bevart, og de tilhørende samlede SHA-filene er oppdatert til korrekte rapportbytes. Leveringshjelperen normaliserer heretter bare Markdown; prompt- og oppskriftsbytes bevares eksakt.

C sin revisjon omfatter64 unike eksplisitte hashpar:47 var riktige og17 hadde det beviste ekstraLF. Inventaret fant også242 rapportprompter uten eksplisitt historisk prompt-SHA; disse er ikke erklært historisk byteverifisert. Den foreløpige vide koblingen til generelle bildehash ble forkastet før slutt og er dokumentert som analysefeil.

Bevis, filinventar og etterhash står i c-promptintegritet.json og root-reparasjon.json. Dette er en proveniensretting, ikke endret grafikk eller runtime-verifikasjon.
