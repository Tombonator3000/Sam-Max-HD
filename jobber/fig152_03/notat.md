# fig152_03, Sam i hyssingmuseet

Levert 19. oktober 2026. 10 spillruter i 1536 x 1024 RGBA. Resultat-SHA256: `2c389fd2d1cfc671681ce4d99a2736b0339114ee7691a932b54a9d6ea5982eaf`.

Motivet er Sam med grønn uttrekkbar pantograf/golfballhenter, Jesse James-hånden, rød fiskemagnet og humørring i rom28. Rutens originale utsnitt bestemmer hva som er synlig. De komplette kroppene i lag14 og de separate magnet-/ringdelene er beholdt som egne kildelag. Små brune grep er bevart fra kilden. Verktøy utenfor utsnittet er ikke lagt til.

Grunnlag: jobbens original_1x.png og referanse.png, Sam-hovedarket, rom28 i produksjonsmotoren, docs/GJENNOMGANG.md og walkthrough. Se premissretting.txt, KLARGJORT.md og ruteplan-unik.json i rapporter/sam-gripearm-20261019. Samme kildeidentiske RGBA-poser deler tegning etter eksakt sammenligning; hele bunken har 46 ulike poser og 82 spillruter.

Innebygd image_gen, eksakt modellnavn ikke vist. Hele bunken har 11 faktiske kall og 11 råbilder, hvorav ni brukes i sluttresultatet. Dette arket bruker unik-B-raa01.png, unik-C-raa01.png. De faktiske promptene, råbildene og SHA-kvitteringene ligger i rapportmappen; bildekall.json skiller utkast og brukte bilder. H01 retter en glemt fot, E02 forenkler håndfestet etter kilden, I01 retter 1923/1795, F02 gjenoppretter brune gripedeler og fjerner en oppdiktet grå tapp.

Python er brukt med Toms tillatelse til alfarydding og plassering med myke kanter. Generert alfa og kildebekreftede små deler beholdes. Ingen hard original pikselmaske er brukt til klipping. Beskyttede jobb- og referansefiler er uendret.

Egenkontroll: OK. Alle rutene OK. Native mottak godtar alle rutene med uendrede grenser. Alle er visuelt sammenlignet med original/native/motorutsnitt og registrert tegnet i produksjonsmotoren. Fire animasjoner i rom28 gir 264 kontroller fra figurstart uten avvik. Fire kjente oppstartsavvik før testfiguren er identiske med grunnlaget. Dette er tvungne animasjonsprøver, ikke naturlig gjennomspilling. Ingen ny Tom-godkjenning eller separat Claude-kontroll. Publisering og import står først bekreftet i mottak-publisert.json når den finnes.
