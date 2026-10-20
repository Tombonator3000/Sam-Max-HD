# Windows startprøve feilet før spillstart

Forsøk 1, run 39392600746, feilet med SDL_BlitSurface failed: Parameter src is invalid, før spillgjenkjenning og før HD-modden lastes. Kompilering og ZIP-bygg besto. Samme motorkode og SDL2 2.32.10 besto run 39386330283. Ingen konklusjon om rotårsak eller ny grafikkfeil fra denne forskjellen alene. Prosjektbiblioteket ga ingen treff på det konkrete symptomet eller Windows/ScummVM. ScummVMs eksisterende SDL-overflatekode er undersøkt; flere ulike kall kan gi samme tekst, så loggen alene beviser ikke hvilket som feiler.

Én omprøve av den feilende jobben kjøres med uendret kildekode, mod-SHA og startprøve. Ingen sjekk fjernes eller omgås. Første komplette logg og forrige grønne logg beholdes. Dersom den nye prøven også feiler, skal fellesutgivelsen fortsatt holdes tilbake og konkret SDL-startretting undersøkes. Linux-pakken er faktisk hentet og har 304 bufferkontroller null, alle ni nye og 24 returer observert. Fellesrelease er ikke oppdatert før Windows-pakken også er verifisert.

Forsøk 2 er nå grønt, med samme kode 144aa406 og mod-SHA 10734a9c, og uendret startprøve. Første feil er beholdt som uavklart SDL-oppstartsavvik. Dette beviser ikke at rotårsaken er løst. Den faktiske Windows-nedlastingen og grafikkinnholdet kontrolleres før fellesutgivelsen. Ingen tredje omprøve er kjørt.
