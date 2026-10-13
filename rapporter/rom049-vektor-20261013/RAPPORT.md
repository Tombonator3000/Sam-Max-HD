# Rom049 etter uttrykkelig metodevalg

VR-rommet er rekonstruert som presise fargeflater og levert med egenkontroll **OK**: skift 0,01, blokk 0,07 og kantlikhet 1,00. Dette erstatter den visuelt avviste kandidaten i bestilling 11. Tom valgte vektormetoden direkte; han har ikke individuelt godkjent dette nye bildet.

De 41 originalfargene er bevart som flate SVG-fyll. Felles grenser forenkles én gang og gjenbrukes, med uendrede kildeknutepunkter og maksimal kjedeavstand 0,8 originalpiksel. 532 rasterregionløkker er bevart. Antallet beskriver rastertopologi, ikke designfasetter. PNG rendres fra vektorbanene, uten innebygd originalbitmap eller silhuettmaskering av generert kunst.

Root og [uavhengig Astra-QA](b-uavhengig-qa.md) har sett kilde, geometri og resultat. Slottets vinduer, hule, sverd og plasseringer er bevart. Separat diagnose fant ingen egentlige kryss mellom de 3709 segmentene, men er ikke et komplett matematisk topologibevis. SVG har ingen gradient, bitmap eller ny tekstur. Kantfarger i PNG er antialiasdekning.

**Synlig begrensning:** Noen trappekanter består ved små og tette knutepunkter, særlig sverdet og deler av fjell-/hulekantene. Andre grenser er lange rene linjer. Resultatet skal ikke omtales som jevnt utglattet overalt eller pikselidentisk. Forbeholdet følger [leveransemanifestet](fremdrift.json).

Fire beskyttede jobbfiler er kontrollert uendret mot den låste bestilling 11-basisen. Fem avviste bildeforsøk er bevart; tidligere normalisert kandidat og notat finnes også her. [Metodevalget](TOMS-METODEVALG.json), [geometri](geometri.json), [SVG-master](rom049-master.svg), [PNG-master](rom049-master.png), oppskrift og kontrollutskrift er bevart.

Ingen motorimport, originalmasker, dynamisk palett, timing, faktisk spillvisning eller ny individuell bildegodkjenning er verifisert. Andre avvik beholder status.
