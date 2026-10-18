# Felles Linux- og Windows-release, 18. oktober 2026

Publisert og bekreftet Latest 2026-10-18 13:59 norsk tid: https://github.com/Tombonator3000/Sam-Max-HD/releases/tag/sam-max-hd-2026-10-18.

Begge pakkene bruker main ed7a1face8286a3737c8b63d6876572d7b3c5ebd og hd-mod f7a3f275d62de5327d5a0d08153dfbc17ffdb9c9, 1386 native HD-ruter. 96 nye ruter fra fig307_01 til 05 og fig312_01 til 05 er med. Ingen ny motor-/pipelinekode; main-forskjellen siden forrige fellespakke er dokumentasjon. Native filer, alle tidligere grafikkfiler og grafikkildene er bevart.

Linux-bygg 39124246281 og Windows 39124248206 er grønne. Linux har bestått oppstart og Debian 12; Windows har bestått automatisert oppstart med HD og MT-32. Begge pakker er lastet ned og SHA-256 er kontrollert mot sjekksumfilene. Alle 19 627 runtime moddfiler i hver pakke er byteidentiske med publisert modd og hverandre. Bare README.md utelates av pakkeskriptene. 1386 native i begge og i mod.json.

Første sammenligning av kodefeltet i BYGG.txt ventet full commit-id, mens byggefilen med hensikt oppgir kort id. Denne kontrollen stoppet; sammenligningen er rettet til å bekrefte kort id mot full id fra begge GitHub-byggene. Ingen pakke eller byggefil er endret. Se bygggrunnlag-kontroll.json.

Den nedlastede Linux-pakkens uendrede produksjonsmotor, spill og modd er prøvd lokalt i ni forløp. Inventar, akvarium, cafeteriarør, Sam opp ned med blinking/tale, Sam i sele med ståing/tale, første automatiske strikkhoppsyklus og deretter hele chore7. Alle ni avsluttet normalt. Første 500-bilders strikkhoppsyklus viste bare de ti forberedelsesrutene; den går gjennom flere retninger før neste chore. En egen 440-bilders chore7-prøve viste de 34 øvrige. Alle 44 kostyme312-ruter er dermed observert i produksjonspakken uten lokal retningskrok. Alle 96 nye ruter er separat sett og registrert i den lokale grafikk-QA-en, se ../strikkhopp-20261018.

404 skjermbufferkontroller i pakkekontrollen. De fire rom61-prøvene krever det allerede kjente avviket 160 ved frame 36 før figurstart og null etterpå. 350 målinger fra figurstart uten avvik; alle øvrige målinger er også null. Oppstartsavviket er tidligere gjenskapt med forrige publiserte modd, og er ikke rettet her. Z-kantmålingene er ikke null. Dette er tvungne, avgrensede prøver med dummy lyd/skjerm og null musikk. Kopierte saves og isolerte HOME-/XDG-mapper; brukerens egne innstillinger og lagringer er ikke rørt. Ikke full naturlig gjennomspilling, nettleseravspilling eller interaktiv Windows-test.

Åtte utvalgte stillbilder er visuelt kontrollert: åpent inventar, akvarium og blått cafeteriarør uten de tidligere rosa feltene i dette utvalget; Sam opp ned med blinking/tale; Sam i sele med ståing/tale og Sam som løfter Max. De faktiske bildene ligger her. Synlige grunnmotiv-/bakgrunnsrester og originalbaserte figurer gjenstår. Kanter og øvrige kjente feil er ikke erklært løst. Den første motoroversikten valgte inventaret etter lukking; endelig oversikt bruker bildet av åpent inventar ved frame 120.

Fire filer ble lastet opp i draft. Tag-oppslaget i REST svarte 404 før utkastet var publisert, så utkastets metadata ble hentet med den eksisterende release-id 416422940. Ingen ny eller duplisert release ble laget. Alle fire filstørrelser og GitHubs SHA-256-digester ble kontrollert mot lokale filer før publisering. Deretter satt publisert med Latest og bekreftet via releases/latest. Eldre releaser er bevart.

128 av 1758 figurjobber har resultat, 1630 mangler pluss returer og stilkontroll. De 96 nye har ikke separat Claude-kontroll eller Toms nye stilgodkjenning. Neste Sam-ark fig314_01 til 04, så fig294_01 til 02. Natt-automatikken er fortsatt pauset.

Se release-notater.md, nedlastinger-kontroll.json, moddfiler-kontroll.json, linux-kontroll.json, linux-hopp-kontroll.json, linux-samlet-kontroll.json og byggmetadata. Rålogger er bevart byteidentisk i motorlogger.zip; skript er lagt ved som .py.txt. De kan kjøres fra en separat jobbmappe med nedlastede/utpakkede pakker, ikke direkte fra dette rapportutdraget uten pakkene.

![Ny grafikk i den nedlastede Linux-pakken](sam-max-hopp-sekvens.png)
