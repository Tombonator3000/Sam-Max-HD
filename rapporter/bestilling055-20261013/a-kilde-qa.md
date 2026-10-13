# Max006 sluttkontroll

32 ruter: åtte kildebeviste nye pilotkomponenter og 24 nye a17-positurer i grupper på 7, 7 og 10. Ingen rekvisitt eller ubekreftet funksjonsbetegnelse er tilføyd. Retning, lag, fargefamilie, ørevariasjoner, lave/strakte stillinger og potefelt er kontrollert mot originalene. Kildelåsens åtte filer er verifisert uendret.

Tre innledende innebygde bildekall og to avgrensede øyerettinger. De to siste redigeringsbildene endret canvas og bakgrunn og er derfor ikke brukt som helbilder. Bare seks små nye øyerektangler er sammenpasset med eksisterende ny art, med tre piksler lineær kantblanding. Alfa og alle piksler utenfor de dokumenterte rektanglene er byte-uendret. 272 og 264 har smale svarte øyne, 265 lukkede grå øyne. 273 beholder smale lukkede streker.

Nytegnet alfa er renset utelukkende fra egen alfa: verdi under 40, eller mer enn to piksler fra egen alfa ≥128, blir transparent. Synlig kjerneboks plasseres med helskalering i premultiplisert RGBA; ingen originalmaske, tracing eller lokal deformasjon. RGB settes til null ved alfa null. Pilotfeltene kopieres med 12 pikslers kantmargin.

Uendret checker gir 13/13 og 17/17 OK. 512/513 faller under checkerens småfeltsgrense og er derfor kontrollert som konkrete, ikke-tomme pilotbytekopier i a-oyelokk-kontroll.json. De 32 feltene er sett samlet i a-slutt-feltqa-1..4.png. Rel-ark bruker original rel pluss forskjellen mellom synlig og rekt, ikke felles fotlinje.

Begrensninger: runde penselformer, fingre og skygger er stiliserte. Teknisk OK er ikke runtime- eller individuell brukergodkjenning. Faktisk animasjonshastighet, lagrekkefølge og motorfeste er ikke kjørt her. Metadata er ikke endret.
