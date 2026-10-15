# Feilrunde 2, 15. oktober 2026

Tom meldte feil i den nedlastede Linux-/Windows-pakken og ga Codex uttrykkelig lov til å rette motoren og lage PR. Denne runden leverer to rettede Sam-ark, kantvask av 110 separate ikoner og dokumentasjon av motortestene. Den generelle arbeidsdelingen mellom Claude og Codex beholdes.

## Grafikk som er klar for mottak

- `jobber/fig002_01/resultat.png` og `jobber/fig004_01/resultat.png`: tredje finger på hånden til venstre i Sams frontvendte kropp, rute 128. 134 uvedkommende kantpiksler er fjernet per ark. Egenkontroll: 7 av 7 hovedruter OK per ark. Lokal myk import: 18 ruter OK, ingen til sjekk eller manglende. Kostyme 2 er satt sammen og sett i motoren i [testbildet](sam-hand-spilltest.png); kostyme 4 er importkontrollert, men ikke vist separat. Tom har ikke godkjent den nye hånden.
- [Ikonmanifestet](../ikoner-ui-20261015/ikonmanifest.json) peker på de oppdaterte ordinære RGBA-filene. 17 134 grønne mattepiksler i kanten av 110 av 111 ikoner er erstattet med lokal motivfarge. Alfa, størrelse og plassering er uendret for alle 111. Fem verbhjulaliaser er byteidentiske med sine grunnikoner. Motivenes grønne interiør er bevart. Detaljer: [ikon-kantvask.json](ikon-kantvask.json).
- [Rutekart](rutekart-sam.json) og [fremdrift](fremdrift.json) har SHA-256 for de nye Sam-arkene. Bruk dette kartet ved neste myke import. De åtte beskyttede referanse-, original-, prompt- og metadatafilene er uendret.

Originalens frontvendte hånd er også svært forenklet. Tre fingre er Toms uttrykkelige rettelse, ikke en påstand om at tre fingre kan telles sikkert i akkurat denne originalruten. Originalen og det godkjente `hovedark/sam.png` ble undersøkt før den lokale rettingen. Ett forsøk med innebygd bildegenerator, modellnavn ikke eksponert: [prompt](sam-prompt01.txt), [råbilde](sam-raa01.png), [presis Python-oppskrift](klargjor-grafikk.py.txt). Python-rensing og plassering er uttrykkelig tillatt av Tom tidligere i samtalen.

Samle-ZIP-en fra tidligere i dag er et historisk øyeblikksbilde og inneholder ikke denne runden. Hent de ordinære filene og det oppdaterte ikonmanifestet fra repoet, ikke de gamle ikonkopiene fra ZIP-en.

## Motorrettingen

Koden ligger i [codex/hd-masker-inventory](https://github.com/Tombonator3000/Sam-Max-HD/tree/codex/hd-masker-inventory) som PR mot main. Ingen spillbilder eller spillfiler legges i kodegrenen.

Tre årsaker er rettet:

1. Inventar- og samtalekort tegnes som ordinære romobjekter. Denne veien leste de gamle maskeklippede PNG-ene selv om rene `_hd.png`-bilder fantes. Den bruker nå de native RGBA-filene, deres egen alfa og en bufret, samlet palettfaktor. Det hindrer nøkkelfarger i originalpikslene fra å farge HD-kanten.
2. Gjennomsiktighet i et inventarkort viser nå inventaresken under kortet. Den viste tidligere rommet bak hele esken. Bare aktive, eldre objektlag vurderes som underlag.
3. Klassiske kostymer med myk HD registrerer nå de faktiske pikslene dekoderen skriver, inkludert palettmasker og laget under. Dette fjerner rosa/blå feiltolkning i akvariet og cafeteriarøret. Hard nearest-visning beholder sin tidligere koblingsvei.

Native romobjektbilder må i denne rettingen fortsatt ha nøyaktig 4x størrelse uten marg. Malte romobjektkanter fra PR 29 beholdes. Denne rettingen gjør ikke mangelfulle animasjonstilstander til komplette tegninger.

## Spillkontroll

Kjørt uten skjerm med SDL dummy, isolert konfigurasjon, kopier av lagringer og en lokal prøvemod. Brukerens spillprosess og lagringer er ikke endret. Grunnlaget var main `c52ffe6e` med samme motorpatch som senere main `1c4ff977`, HD-mod `9512fd8`, nye Sam-ruter og de kantvaskede ikonene. Sammenligningsmotoren kom fra Linux-pakken publisert rundt 18:03 norsk tid, SHA-256 `15663e1089f44665d97dc4e8770326664f8217fea085adcc3cd1ea474e678be0`. Claude publiserte senere HD-mod `dd43c31` med forrige grafikkrunde; denne prøvemodden er ikke en test av hele den nyere utgivelsen.

| Kontroll | Resultat og bilde |
| --- | --- |
| Inventar, rom 30, åpne og lukke | Rene kort og jevn eskekant: [før](inventory-for.png), [etter](inventory-etter.png), [lukket](inventory-lukket.png). 280 bilder, 5,3 sekunder i siste kjøring |
| Akvarium, rom 16 | Rosa/blå felt er borte, figurlaget bak glasset beholdes: [før](akvarium-for.png), [etter](akvarium-etter.png) |
| Cafeteriarør, rom 30 | Blått glass og figuren inni røret vises: [før](cafeteria-for.png), [etter](cafeteria-etter.png). Ingen rosa flate i den testede bevegelsen |
| Sam, frontkropp | Tredje finger synlig i [motorbildet](sam-hand-spilltest.png), kostyme 2, rute 128 |
| Bilen, rom 9 | [Stillbilde med mykere omriss](bil-kontroll.png). Testhopp plasserer figurer kunstig; bilens avreise er ikke testet |
| Kontoret, forsøk på opptak | Testen lukket inventaret, men klikket på objekt 0, ikke gjenstanden. Beviser ikke at restene etter opptak er løst |
| Tunnel of Love, rom 22 | [Rester fortsatt synlige](tunnel-fortsatt-feil.png) i øks-/bakgrunnsovergangen |
| Tivoliets utstilling, rom 16 | [Tilstandskontroll](hall-tilstandskontroll.png). Skriptet overstyrer enkelte tvungne tilstander; ikke bevis for en feilfri hel animasjon |

Siste tre kjernekontroller avsluttet normalt og ga 0 forskjell mellom skjermbuffer og full gjenoppbygging. Dette måler rester i tegnebufferen, ikke om en malt bakgrunn eller lapp forestiller riktig motiv. Z-kantmålingene er ikke null. [Verifiserte resultater](verifisert-resultater.json), [bredere test](sluttest-resultater.json), [Sam-test](sam-posed-resultater.json), [nearest-sammenligning](nearest-release-resultater.json) og [relevante logglinjer](spilltest-logg.txt) er bevart.

Nearest-kontrollen er ikke pikselidentisk: kontoret har 3193 av 1 024 000 kraftige avvik både med utgivelsesmotoren og rettingen, 0,312 prosent. Cafeteria hadde 475 i utgivelsen og 542 i prøven, 0,046 og 0,053 prosent. Dette er dokumentert, ikke rapportert som null.

Kodekontroller: ScummVM bygget, patch anvendt på ren låst ScummVM-base og alle 30 resulterende kildefiler sammenlignet byte for byte; 51 pipelinetester og 19 nettlesertester bestått. Grafikkontroll: [kontroller-leveranse.py.txt](kontroller-leveranse.py.txt) sjekker alle filhashene, alfaformene, aliasene og de beskyttede kildene.

## Gjenstående arbeid

- Øksen i rom 22 trenger sammenhengende bakgrunn og tilstander. Det statiske HD-rommet inneholder en annen øksestilling enn animasjonslappene; å bygge hele skjermen på nytt fjerner ikke dette innholdet.
- Kranhodet, objekt 154, og Chicken Dumpling, objekt 155, må gjennomgås i alle faktiske bevegelser. Komplette motivbilder finnes bare for noen tilstander fra tidligere leveranse. Ikke gjenbruk én tilstands tegning som alle de andre.
- Opptak og rester på gulvet må kontrolleres med et faktisk vellykket opptak og riktig kameratilstand. Bilens avreise må også spilles gjennom.
- Sam/hammer i Wak-A-Rat og øvrige samtalekort må kontrolleres i hele animasjonen med denne motoren.
- Ny motor, oppdatert grafikkimport og nye Linux-/Windows-/webbygg må gjennomføres etter kodekontroll. Denne runden er ikke i Toms nedlastede pakke ennå.

Se [overleveringen til nattløpet](NATT-HANDOFF.md). Ingen automatisering eller melding til Claude er opprettet fra denne chatten.
