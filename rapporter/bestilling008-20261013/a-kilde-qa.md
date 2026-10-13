# Kilde-QA for kikkertpanelet

Dato: 2026-10-13. Lest GRUNNLAG.md og b-kildeplan.md. Alle tre original1x, referanse4x, jobbmetadata og felles prompt er lest. Motiv: ett myntkikkertpanel med topp307, midt304, bunn308, samme oppgitte tilstand01, ikke alternative apparater.

Originalene er satt sammen vertikalt uten endring til320x200, så skalert med nærmeste nabo kun som genereringsreferanse til1280x800. Referansen ligger på1536x1024 RGB128 ved[128,112]. Originalsamlingen er bevart som a-panel-original1x.png og a-panel-reference.png. Denne sammenstillingen endrer ingen beskyttede kilder.

Identitet og antall: lilla/grå kapsling, to mørke skruer øverst og fire lyse nede. Dobbelbuet svart synsåpning med neseparti/nedre hakk, kildens grønne landskap, barskog, lys vei og lille skilt. Ingen ny skilttekst. Nedre panel har 25¢, én loddrett myntsliss, spak med vifteformet skala og svart åpning avklipt i nederkant. To brune avkuttede hender og hvite mansjetter/lyseblå ermer beholdes uten navn, hode eller kropp.

Kildeplanen dokumenterer at referansene er kompositt over rombakgrunnen. Synlig landskap tegnes kildetro, uten å hevde at objektets åpning skal være ugjennomsiktig ved import. Originalmaske/import håndteres separat av Claude. Rom031-HD er ikke brukt som godkjent stilanker. Stil/rom007_del1av2.png er eneste supplerende stilanker; originalpalett og geometri styrer.

Leveransedelene klippes fra én1280x800 nytegnet fullmaster:307y[0,160),304y[160,512),308y[512,800). Deretter legges de i sine metadatarektangler på1536x1024RGB128. Ingen originalsilhuettmaske, lokal warp eller uavhengige generatorsømmer. Reassemblert leveranse skal være byte-identisk med master.

Kontroll av tekst, skrueantall, kontakter og åpning gjøres visuelt; uendret sjekk_leveranse.py kjøres separat. Import, masker, panoramabevegelse og runtime er ikke testet. Ny individuell brukergodkjenning=false.


## Sluttkontroll og begrensning

Valgt fullmaster02 fra to forsøk. Midt304 OK0.06/0.13/0.96; bunn308 OK0.29/0.85/0.93. Topp307 fortsatt FEIL0.13/19.94/0.94. Første toppforsøk hadde blokk51.42. Den nye toppens midtblokk over flat skygge/kapsling er fortsatt problemet; FFT-instabilitet er plausibel, men ikke bevist. Ingen unntak eller terskelendring er gjort. Toppleveransen skal derfor ikke kalles teknisk ferdig. Alle deler beholdes fra samme master; ingen blanding mellom forsøk. Sammenstilte leveransedeler er byte-identiske med1280x800-master. Seks skruer og25¢ er visuelt kontrollert. Nøyaktig importmaske og panoramasamspill er uprøvd.
