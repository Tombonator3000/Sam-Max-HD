# Frog Rock og hyssingen til dinosaurtannen

Codex 2026-10-19 22:49. Åtte nye resultatark: fig215_01 til 04 og fig300_01 til 04. 75 nye native ruter fra 66 eksakt ulike hele originalutsnitt og 175 ulike RGBA-delsignaturer. Kandidaten har 1 851 native ruter. Faktisk publisert SHA og tilbakehenting føres i mottak-publisert.json etter kontroll. 183 av 1 758 figurjobber har nå resultat, 1 575 mangler resultat pluss returer og sluttkontroll.

## Motiv og kilder

215 er Sam som strør mystisk føflekkpulver over Bigfoot-hår på Frog Rock, ikke brennende føtter. Sam er bevisst diagonalt avskåret ved steinen. De siste tolv rutene viser bare hår og pulver som løfter seg og blir borte. Rom 41, lokalt originalskript 202, setter kostyme 215 ved 331,127 med kamera 320.

300 er den lyse hyssingen som brukes til dinosaurtannen, ikke den grønne bungeestrikken fra 309. Vanlig blågrå dress, ingen sele eller briller. De siste fire kroppsfasene har grå støvpuffer, siste ark bare hyssing. Rom 58, lokalt originalskript 201, kobler kostyme 300 til tannsekvensen via nærbildet i rom 85 og Max sin sluttkommentar.

Originalene, GJENNOMGANG.md, riktig kostymefelt i figurer.csv, fire originale motorforløp og godkjent Sam-hovedark er sett. De kopierte originalskriptene har proveniens og SHA; tidligere og nåværende spillfiler er byteidentiske. [Derek Waites walkthrough](https://www.justadventure.com/walkthrough/sam-max-hit-the-road-cheats/) bekrefter bruken av hårprøvene med pulver og av hyssing til dinosaurtannen; kostyme-ID-ene er bekreftet av spillkildene.

Bibliotekskilder: losninger/grafikk/figurark-fast-storrelse.md, scumm-v6-kostymer-skygge-og-soppelruter.md og losninger/bygg/publisert-mod-er-fasit.md fra prosjektbiblioteket. Eksisterende mottak v6 og kontrollopplegg brukes; opphavets teststatus erstatter ikke målprosjektets prøver. Ingen produksjonskode er endret.

## Nytegning og rettinger

14 vellykkede innebygde image_gen-kall, ingen CLI/API-fallback, avslag eller avbrudd. 13 råbilder brukt helt eller delvis. J01 er bevart som forkastet utkast; J02 retter for fyldige hårklumper. O retter småfragmenter. Bare P sin første brune hårdel er brukt; fem gule varianter ble for hårete og er utelatt. N gir separate genererte materialer for kildebekreftede pulverkorn, hårfragmenter, støv, hyssing og små knuter. Faktiske prompter og strukturerte forespørsler, råfiler og SHA-kvitteringer ligger her. Eksakt modellnavn vises ikke av verktøyet.

39 store Sam-komponenter og 17 større hår/pulverklumper er nytegnet. Alle 2 695 komponentforekomster i de 66 ulike originalene har en dokumentert generert del. Identiske hele originalruter gir byteidentiske native filer. Sam sin nedhengende hånd i 1920/1955 er også sett forstørret: original og nytegning har samme tre synlige fingerender i denne vinkelen. Flere fingre skal ikke legges til uten kildestøtte.

Python er brukt etter Toms tillatelse. Originalmasker brukes bare til analyse, komponentbokser, farger og banekoordinater. Ingen hard original silhuettmaske klipper de nye motivene. Generert hyssing er plassert mykt langs en PCHIP-glattet originalkurve. Små kompakte knuter er behandlet separat; store skjulingsgap beholdes. Effektdelene har 0,5 HD-piksel bredere generert strek og enkelt-hyssingen 0,25 HD-piksel, så korn og tråd ikke blir borte i lavere dekning. Ingen kontrollgrenser er endret.

16 rene magenta RGB-avrundinger ved alfa 1 i prototypebilder er erstattet med nærmeste gyldige genererte RGB; med kildealiasene er det 18 produksjonspiksler. All alfa og øvrige piksler er uendret. Ingen tidligere publiserte grafikkfiler er endret.

## Kontroller

Egenkontroll 64 OK, 11 SJEKK, 0 FEIL. Omrissmerknader: costume215_1948, costume215_1957, costume215_1958, costume215_1959, costume215_1960, costume215_1961, costume215_1962, costume215_1963, costume215_1966, costume215_1967, costume300_1946. Disse er ikke kalt OK. Native v6-mottak: 75 OK, 0 til gjennomsyn, 0 manglende og 0 tekniske feil. Alle beskyttede 32 kilde-SHA-er stemmer. Alle 20 012 tidligere PNG-er og 20 018 tidligere filstier er bevart; bare mod.json endres i kandidaten. Tre opprinnelige stasher er urørt.

Alle 75 er visuelt sett som original/native/motor, med syv kontaktark og fire hele sceneutsnitt. Rom 41 sine første kontrollutsnitt var feilplassert ved at kameraets venstrekant 160 ikke var trukket fra verdenskoordinaten. Kontrollbildene er rettet og sett igjen; dette var ikke en feil i motoren. Ingen endret grafikk ble skjult av de svarte utsnittene.

Faktisk nedlastet senkveldsmotor, SHA c00096cbbee45c4e56ad7f0ae1e677f02aabe1cb7073992fa695fe79d5803c23, med pakkens egne spilldata og biblioteker. Fire grunnlagsprøver med 1 776 og fire nye animasjonsprøver med 1 851. Alle 75 nye ruter registrert tegnet, 300 skjermbufferkontroller, 264 fra figurstart uten avvik. Fire kjente avvik 160 ved frame 36 før testfiguren finnes også i grunnlaget. Ingen lokal retningskrok. Kopierte saves og isolert HOME/XDG per prøve. Etter RGB-rens er alle fire sluttforløp kjørt igjen; 556 av 600 dumpfiler beholdt samme SHA, 44 endret SHA. Ikke påstå at samtlige bilder er byteidentiske etter rens.

Dette er egenkontroll, native mottak og motorobservasjon. Det er ikke naturlig gjennomspilling, separat Claude-kontroll eller ny Tom-stilgodkjenning. Ingen ny Windows-/nettleserprøve. Felles publisert Linux-/Windows-pakke sam-max-hd-2026-10-19-senkveld har 1 776 og mangler de 75 nye; pakker oppdateres ved neste samlepunkt. Ny grafikk skal ikke inn i main.

Neste uavhengige arbeid er fig168_01 til 03, deretter fig336_01 til 03. Kildeavklar hver i spillkontekst før generering. Tidligere avviste golf-E og VR-G skal ikke bestilles på nytt eller omgås. Automatisk grafikkfortsettelse er fortsatt aktiv.
