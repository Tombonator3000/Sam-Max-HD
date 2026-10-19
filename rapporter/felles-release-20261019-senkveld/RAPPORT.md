# Felles senkveldspakke19. oktober2026

Begge pakker er bygget og kontrollert fra main346f27c0e5da1e2f3b8c29ce02ce6fb3c9e436f4 og hd-mod6513908aa6d47dd73abd58f6f101ff9641c25d6b.1776 native figurruter er med,122 flere enn forrige felles kveldspakke:82 gripearmruter og40 Sam-/Max-ruter i strikksele. Dette er et samlepunkt i pågående grafikkproduksjon, ikke ferdig HD-grafikk for hele spillet.

## Bygg og faktisk innhold

Linux-run39313474732 og Windows-run39313479357 er grønne. Begge er workflow_dispatch fra samme main-SHA. Mellom forrige kode01ee58f7 og denne er bare memory.md, todo.md, STATUS.md og log.md endret. Ingen produksjonskodeendring. Windows sitt ekstra push-bygg39303372380 fra forrige felles releasetag er ferdig og hadde ikke publisert en ny plattformpakke; det er ikke brukt her.

Begge faktiske binærpakker og begge SHA-filer er lastet ned. SHA-filene består, og alle fire GitHub-digester/størrelser stemmer med filene. Alle20017 runtime moddfiler er identiske mellom Linux, Windows og publisert modd. Bare mod-grenens README.md utelates av pakkeskriptene.1776 native i begge mod.json og i faktisk kostymemappe. BYGG.txt i begge pakker har riktig main og modd-SHA. Se bygggrunnlag-kontroll.json, nedlastinger-kontroll.json og moddfiler-kontroll.json.

Linux-AppImage:402512376 byte, SHA256 a5dbc153eb5928297f3c1f767cd43e7c7eeb4f4cd2611c10f3c2a730b8d992e3.
Windows-ZIP:513924851 byte, SHA256 8b88ebef75355300e624e5295211ebbc07bf433d3e388987aa328107f277b69b.

## Motorprøver fra den faktiske nedlastingen

Ni prøver med uendret nedlastet Linux-binær, spillfiler og modd. Inventar, akvarium, cafeteriarør, fire animasjoner for152 og to for309. Alle122 nye ruter er registrert tegnet.469 skjermbufferkontroller totalt,415 fra figurstart uten avvik. Seks kjente160-avvik ved frame36 før testfigur i rom28/61 er som tidligere grunnlag; øvrige målinger null. Alle ni utvalgte motorbilder er sett i to kontaktark. Fire native PNG-er fra pakken er vist uten endring eller skalering i forhåndsvisningen, med kilde-SHA-er.

Den nye Linux-produksjonsbinæren har SHA256 c00096cbbee45c4e56ad7f0ae1e677f02aabe1cb7073992fa695fe79d5803c23. Den er ikke samme fil som forrige nedlastingsbinær, men er bygget fra samme uendrede produksjonskode. Ni rålogger med SHA-manifest, BYGG.txt og testhjelpere er bevart. CI består Linux-oppstart og Debian12; Windows består arbeidsflytens automatiserte oppstartstest. Ingen naturlig gjennomspilling, interaktiv Windows-test eller ny nettleserprøve her.

## Grafikkens kontrollstatus

Kilder og faktiske prompter ligger i rapporter/sam-gripearm-20261019 og sam-max-sele-20261019. Begge leveranser er teknisk mottatt, visuelt sett og motorobservert, med dokumenterte omrissmerknader. Ingen ny Tom-godkjenning eller separat Claude-kontroll. Alle tidligere publiserte PNG-er og tre stasher er bevart.175 av1758 figurjobber har resultat,1583 mangler pluss returer. Neste åtte jobber ved Frog Rock og dinosaurtannen er bare klargjort i frog-rock-og-tau-20261019, ikke nytegnet eller telt som leveranse.

Publisering: kontroller er ferdige. Ny felles draft opprettes og verifiseres før publisering. Se publisert.json når den finnes for faktisk release-ID, tidspunkt, opplastingsdigester og Latest-kontroll. Ikke kall en draft eller denne kontrollrapporten i seg selv en publisert release.
