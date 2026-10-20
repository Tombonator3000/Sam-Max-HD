# Feil premiss i fig346_27 til43

Disse 17 jobbene, 44 ruter, skal ikke produseres som en gyldig animasjon. Kostymetabellen slutter ved byte145. Oppslag36 leser byte146/147, som er lagmasken07 00 til den første ekte animasjonen. Den får dermed offset7 inn i kostymets format/palett. Dette er målt i de faktiske spillfilene, se kildefeil-raw36.json. Motorens eksisterende testkrok følger det samme ekstra oppslaget og lager et feil lag-/ruteforløp. At21 av44 ble tvangstegnet, er ikke et gyldig spillforløp.

Lokalt201 viser346 med chore6 og7, ikke9. De gyldige346-jobbene01 til26 er allerede publisert, og ingen av dem endres. Ikke gjenta den lange raw36-prøven. Ingen nye resultatfiler, bildekall eller native er laget for27 til43. Beskyttede filer er beholdt og jobber står åpne med kildefeil, ikke ferdig eller godkjent.

Koden må senere få ressursgrensekontroll gjennom en testet PR. Ikke endre numAnim-sammenligningen globalt ut fra dette ene funnet; ScummVMs låste kode tillater selv siste indeks. Eksisterende publisert grafikk bevares. Fortsett uavhengig gyldig produksjon med fig345_01, Sam i samme kildebekreftede alkove.
