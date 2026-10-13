# Bestilling 7 C, kilde og sluttkontroll

Source-faithful-production og imagegen er lest før tegning. Alle fire originalreferanser er sett; originalene er samlet til rom031-kilde-fullscene-1x.png som kildebevis og sammenligningsgrunnlag. Metadata angir originalbredde1104, delbredde384 og offset0/240/480/720. Ingen kikkertinnfatning eller myntslisse finnes i dette laget. Det generiske romnotatet er derfor korrigert eksplisitt i tilleggsprompt, beskyttet prompt.txt er urørt.

Scenen består av sammenhengende bølgende jordbrukslandskap, mørke grønne skogbelter, bartrær, lyse grå veier, blå elv og lyse skyer. Det lille skiltet i del1 har uleselige brune tegn; ingen ord er gjettet. Den lille grønne formen ved elven er bevart uten å navngi eller gi den ny funksjon. Ingen oppdagede steder er lagt til som nye overlegg. Kildens palett og topologi styrer; godkjent kontor gir bare pensel/strek. Små nytegnede penselmerker er ikke påstått detaljidentiske.

Fire innebygde imagegen-kall, ett forsøk per del. Alle råforsøk og faktiske fullprompter bevart. Eksakt bildemodell er ikke eksponert. Fullmaster4416x800 har tre64px diskrete overganger uten geometriwarp. Hver1536x800del er skåret fra samme master; alle tre576x800overlapper er byte-identiske. Svarte rektangulære felt inne i originalbildet er beholdt; utenfor er RGB128padding. Hele fullscene og tre separate original/HD-skjøtpar er visuelt kontrollert.

Uendret sjekk_leveranse.py: alle fire OK. Del1 skift0.08/blokk0.43/kant0.96; del2 0.06/0.82/0.96; del3 0.06/0.83/0.96; del4 0.04/0.30/0.95. Alle40beskyttede kilder har uendret SHA-256. Resultathasher, råhash, logger og oppskrift finnes i c-leveranser.json.

Runtime/import/maskesamspill og ny individuell brukergodkjenning er uverifisert/false. Ingen Git, kode eller globale dokumenter er endret av denne gruppen.
