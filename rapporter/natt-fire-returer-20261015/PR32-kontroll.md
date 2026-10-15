# Avgrenset statisk kontroll av PR32

15. oktober 2026. Ingen fletting eller kodeendring. GitHub-tilkoblingen via gh pr view 32 feilet. Dagens PR-hode og CI kunne ikke hentes på nytt. Tom opplyser at PR32 har grønn CI; det er ikke uavhengig bekreftet i denne økten.

Gjennomgått lokal origin/codex/hd-masker-inventory ved 930ad41d3dfd797cfa33c3458828324607d53f63. Motorrettingen er aeef157213f565e066ad50d020a5b77e0479c9fe. Sammenligningsgrunnlag er lokal main 1c4ff9773c42df878ada3bcd13bb524dd26f82fb. Dette er statisk kontroll av lokal kode, ikke en ny bygge- eller spilltest.

Konkrete observasjoner:

1. Ordinære romobjekter prøver objNNN_SS_hd.png før eldre objNNN_SS.png. Native bildet merkes soft og softEdge. Det dekker den dokumenterte filvalgsfeilen for inventar og samtalekort.
2. objectGain har gainPal knyttet til _palVersion. Startverdiene 0 og 1 gir beregning ved første bruk. Endret palett ugyldiggjør faktoren. Romobjekt- og blast-veiene bruker samme faktor. Omregningen fra 8 til 16 brøkbiter før applyTint er eksplisitt.
3. Transparente kortpiksler søker aktivt eldre objekt som underlag, med sekvensrekkefølge, tilstand og bounds kontrollert. Underlag med egen alfa blandes videre med rommet. Full rekursjon gjennom vilkårlig mange transparente objektlag er ikke etablert av denne gjennomgangen.
4. beginClassicCel nullstiller _recordSlot før mykhetskontrollen. beginActor og noteCel nullstiller også sporet. Dekoderen melder faktisk piksel etter skriving og registrerer om skyggemodus eller palettindeks 13 transformerte pikselen under. Harde ruter beholder noteCel etter dekoding.
5. active[256] og soft[256] er kontrollert mot begge innsettingspunkter for _drawn. Nye plasser avvises ved 255 oppføringer, slik at undersøkt løkke er innen tabellgrensen.
6. Løkken for myke objektkanter avgrenses til objektbildet med xstart, screenTop og virtuell skjerms topline. Fartseffekten er ikke målt på nytt.

Ingen konkret feil som krever ny retting er påvist innen gjennomgått omfang. Native romobjekter krever fortsatt 4x uten marg. Bygg, fade under avspilling, overlappende glassmasker og skriptstyrte tilstandsbytter er ikke retestet. Tidligere spillbevis og begrensninger står i feilrunde2-rapporten og er ikke gjort om til nye resultater her. PR32 er verken flettet eller duplisert.
