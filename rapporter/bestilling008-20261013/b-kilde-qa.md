# Bestilling 8 gruppe B, kilde-QA

Fire resultater levert fra tre innebygde imagegen-kall, ett forsøk per motiv. Eksakt modellnavn ikke eksponert. Ordrette originalprompter med presiseringer, alle råbilder og oppskrifter bevart. Se b-kildeplan.md for identitet/kilder og b-leveranser.json for resultat/master SHA256.

- Rom032: fiskedekk, rød dør, fiskeskilt, vindu/blomsterkasse, støttebein, gjerder, taubane/kabel og stripestang er bevart. Ingen besøkende eller operatør lagt til. Trådgrupper og løs tråd følger originalens retninger. Begge delene fra én fullmaster; overlapp 1152×800 byte-identisk.
- Rom033: lav kameravinkel, åpen mørk dør, gjerder/støtter, aksel, sky og hyssinggrupper følger eget originalutsnitt. Dørtilstanden er bevisst forskjellig fra rom032. Ingen personer i tomrommet.
- Rom034: løs hyssing med originalkurve og delt/frynset ende; bakgrunnen forblir kryssende lag av hyssing. Ingen saks/hånd/dyr, ingen ny knute. Detaljeringen av de små fibre/endene er en HD-tolkning.

Uendret sjekk_leveranse.py: alle fire OK. Kantlikhet henholdsvis 0.96, 0.96, 0.94 og 0.87. Ingen forsøk skjult. RGB-pad #808080 og canvas 1536×1024, egenkontroll mot aktuelle jobbmetadata. Alle 16 beskyttede filer for gruppen er SHA256-sammenlignet mot kildehash.json og uendret. Ingen Git-mutasjoner eller produktkodeendringer.

Begrensninger: visuell kontroll av statiske bilder er utført, men ikke SCUMM-kompositering, faktisk produktvisning eller gameplay. Glattere shading og mikrokonturer kan avvike fra pikseloriginalen. Runtime=false; ny_brukergodkjenning=false. Ingen påstand om at disse nye bildene er individuelt godkjente stilankere.
