# Kilde-QA for rom021 og rom022

Rom021 viser inngangen til Tunnel of Love med to rosa vingede cupider, én rød hornet djevel, skjev steinfasade og TUNNEL OF LOVE med hjerte som O. Rom022 er en mørk kulisse med ulike horror-/eventyrtablåer. Sammenhengen er underholdningsattraksjonen, ikke nye personer i forgrunnen.

Alle fem originaldeler er visuelt lest og knyttet til jobbmetadata. docs/gpt-romnotater.csv i origin/main bekrefter inngangsskiltet og CORN DOGS/HOT inne. Cupider, djevel, skjelett med kost, monster som bærer kvinne og slottstabåets tre figurer er beholdt som forskjellige motiv. Egennavn eller udokumentert fortelling er ikke lagt til.

Originalpromptene er bevart med en nødvendig teknisk presisering for én felles fullscene. Rom021-master1920x1024 gir del1 ved x0 og del2 ved x384. Overlapp1152 er array_equal. Rom022-master3168x1024 kommer fra alle tre originaldeler og gir utsnitt ved x0,816,1632, bredde1536. Bare del1 er levert nå; de øvrige to skal klippes senere fra samme master. b-fullmaster-register.json låser masterens SHA og alle klippebokser.

Tolv beskyttede kilder fra gjeldende bestilling og åtte ekstra fra rom022 del2/del3 matcher hashlåsene. Ingen beskyttede filer er endret. Ett innebygd bildeverktøyforsøk for rom021 og to for rom022; verktøyet oppgir ikke eksakt modellversjon.

Visuell egenkontroll er ikke motor- eller brukergodkjenning. Små tegn/anatomidetaljer er tolkninger, mens skiltord, antall hovedfigurer og hovedgeometri er sammenlignet. Runtime=false og nybildegodkjenning=false. Ingen Git-, kode- eller globale dokumentmutasjoner er utført.

Rom022 ble korrigert etter teknisk FEIL, uten lokal warp. Se b-rom022-globalplassering.py.txt og masterregisteret for eksakt global skala/plassering. Første kandidat er bevart separat. Endelig del1 er OK, fremtidig del2 er OK, del3 er SJEKK (blokk1,96), og er ikke levert. Den korrigerte masteren skal gjenbrukes ved neste bestilling.

Tillegg bestilling006: tidligere del3-SJEKK er rettet med innebygd nytegning av høyre ikke-overlappende region. Ingen del1-piksler eller part2/3-overlapp er endret; dette er kontrollert bytevis. Den oppdaterte masteren gir nå OK for del3. Registerets nye masterhash er gjeldende.
