# Pakkesamlepunkt3695,oppstartsfeil undersøkes

Fryserarket fig293_03 er helt levert32/32 og native3695 er publisert med alle21939 filhash bekreftet. Nativefrys beholdes.

Linux-bygg39782177395 er grønt. Windows-bygg39782182412 kompilerte og pakket,men oppstartstesten stoppet med SDL_BlitSurface:src invalid før spillet ble lastet. Fellesrelease er ikke oppdatert. Kode 3fe3177a100e1348b1a71ba58726e623f151cd1c,hd-mod f0f7b641177cec8661d7c0cbf68c5faef9eb31f6.

Samme feil er gjenskapt lokalt med SurfaceSDL og innebygd tema. GDB plasserer feilen i SurfaceSdlGraphicsManager::internUpdateScreen under endGFXTransaction før spilloppstart. En avgrenset deferral før videoMode.setup testes i codex/windows-sdl-start. Ingen godkjent motorretting er flettet ennå.

Se windows-bygg39782182412-feil.log/.json,sdl-oppstart-lokal.json,bygg-startet.json og lokal-kontrollstart.json. Ingen feilprøve regnes bestått.

Lokal retting består nå fire ferske oppstarter med HD-motoren og3000-bilders nearest-kontroll med alle kostymer:12 bufferkontroller og12 originale sammenligninger uten avvik. Standardtestens1..20 manglet introens21/22/23/26 og ga glatt fallback; den komplette nearest-modden retter bare testgrunnlaget. Første lokale rebuild manglet HD-kilder og ble avbrutt,og ett scriptforsøk hadde blandet runtime. Ingen slike forsøk regnes bestått. ScummVM-pin og HD-patch0001 er urørt. Kode-PR klargjøres; ingen fellesrelease er oppdatert ennå.

PR35 er flettet etter grønn CI og hentet med ff-only. Kode d738f535b685ea627e82f0dcf1c83ee9b0bea170. Begge pakker skal bygges på nytt fra denne committen etter grønn eksakt main-CI. Første byggeforsøk bevares. Nativefrys beholdes,og fellesrelease kalles fortsatt ikke oppdatert.
