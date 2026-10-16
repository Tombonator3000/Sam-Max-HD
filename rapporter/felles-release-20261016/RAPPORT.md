# Felles Linux- og Windows-utgave, 16. oktober 2026

Tom ba om å flette alt laget arbeid og legge en ny Linux-pakke sammen med Windows. [Felles releasen](https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/sam-max-hd-2026-10-16) er publisert klokken 12:28 norsk tid og bekreftet som Latest gjennom GitHub-API-et. Fire ferdig opplastede filer: AppImage, Windows-ZIP og hver sin SHA-256-fil. Gamle plattformreleaser er bevart.

## Samlet arbeid

Alle kode-PR-er 1 til 33 er flettet, og ingen åpen PR ble funnet. Nattgrenens pipeline, verktøy og arbeidsflyter er identiske med main. PR32 er med i motoren. Kontrollerte tegninger ligger på gpt-arbeid og i hd-mod a6c286bd. Ingen spillgrafikk er lagt i main.

De tre gamle stashene er i tillegg arkivert under rapporter/bevart-stash-20261016, 53 filer med sjekksummer. De opprinnelige stashene er beholdt. Den eldre obj187_05-kandidaten erstatter ikke den nyere godkjente leveransen. Alle 72 resultat-SHA-er fra Toms godkjenning er kontrollert uendret. Arkiverte fremdrifts- og rutekartfiler ligger under ekstra underkataloger og treffes ikke av mottakets rapporter/*-mønstre. Ingen ny import eller svekking av teknisk kontroll er utført.

## Bygg og kontroll

Begge pakkene bruker kildecommit 9b5a9197 og hd-mod a6c286bd. Windows var allerede bygget 09:30 i kjøring 38866752358, med vellykket oppstart, HD og MT-32. Linux ble bygget på nytt i kjøring 38886201631 og publisert i plattformreleasen klokken 12:23, etter vellykket oppstartstest og Debian 12-test.

Begge pakkene er lastet ned, og sjekksummene består. Hver pakkes 19 336 moddfiler er sammenlignet byte for byte med den publiserte modden. Begge har 1095 native figurruter og 113 native objektbilder. Ingen forskjell i HD-innhold. Alle fire felles release-assetters størrelse og SHA-256 er kontrollert mot de lokale filene før publisering.

Linux-pakkens inventar, akvarium og cafeteriarør er kjørt med kopier av testlagringene, avslutningskode 0 og null skjermbufferavvik i alle målte bilder. De tre skjermbildene er sett: rene inventarkort, grønt akvarium og blått rør uten de tidligere rosa feltene. Z-kantmålingene er fortsatt ikke null.

Første akvariumoppstart med AppRun/SDL dummy stoppet før spillet lastet, med SDL_BlitSurface/NULL surface. Inventar og cafeteria besto i samme prøve. Akvariet ble deretter kjørt med pakkens uendrede motor og grafikk, minimal ini, gfx-mode=normal og builtin GUI. Denne prøven består. Det første forsøket og loggen er bevart separat; ingen pakkeendring eller påstand om rettet generell SDL-oppstart. Brukerens innstillinger og lagringer er ikke endret.

Interaktiv Windows-spilling er ikke kontrollert her. Nytegning, munndelen costume249_257, bakgrunns-/øksestillinger, hele animasjonsforløp, faktisk opptak og bilavreise gjenstår som før. Nettmotoren er allerede oppdatert fra PR32; ingen ny nettbygging i denne runden.

Se [publiseringskvitteringen](publisert.json), [samlet Linux-kontroll](linux-kontroll.json), [Windows-modd](windows-moddkontroll.json) og [Linux-modd](linux-moddkontroll.json). De tre skjermbildene og loggene ligger her sammen med den faktiske releasebeskrivelsen.
