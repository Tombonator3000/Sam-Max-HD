# Brutte Highway Surfing-skilt, kildeplan

Avgrenset analyse av obj664_01 til obj667_01. Ingen generering eller kildeendring. Alle fire originaler og 4x-referanser er sett, og jobbmetadata og prompter er lest. Navn er kontrollert i `konsept/2026-10-12/objektbilder-959.csv`. Intakte obj649_01 og obj650_01 er sett som sammenheng, ikke som erstatning for bruddformene. Roots `original-kontaktark.png` og låste `kildehash.json` er tilgjengelige i denne mappen.

## Identiteten er et skiltbrudd

Registeret navngir 664 og665 `surf-left-broke-sign-1` og `surf-left-broke-sign-2`, og666 og667 `surf-right-broke-sign-1` og `surf-right-broke-sign-2`. Hvert objekt har registrert tilstand01; tallene1/2 beskriver ulike navngitte bruddbilder, ikke to tilstander under samme ID. Bildene viser sammenkrøllede og spredte deler av metallskilt og støtteverk. Bruddklasene er ikke fugler, dyr, monstre, ansikter eller grønn væske.

Intakt obj649 viser grønn skiltforside med lys kant og metallstøtte til høyre. Obj650 viser metallbaksidens grålilla horisontale og diagonale avstivning med stolpe til venstre. Den sammenhengen og navnene støtter at venstrebruddene664/665 hovedsakelig viser **metallbaksiden**, mens høyrebruddene666/667 hovedsakelig viser **grønn forside**. Dette er kildebasert motividentifikasjon, ikke en kjørt kollisjonssekvens i motoren. Det er ingen grunn til å speilvende ett sett for å lage det andre.

## Geometri og innhold per bilde

Alle leveranser er RGB, 1536 × 1024, skala4 med RGB128-padding. Det svarte feltet inne i motivrektangelet er del av kilden. Ingen ekstra transparens, sammenbinding av fragmenter eller gjenoppbygging av et helt skilt skal antas.

| Jobb | Original | HD-felt [x,y,b,h] | Må bevares |
| --- | --- | --- | --- |
| obj664_01 | 224 × 104 | [320,304,896,416] | Venstre oppreiste metallstolpe med to tverrfester. Tett klump grålilla, bøyde rammer og mørke platebaksider. Små grønne glimt mellom fragmenter. Store svarte hull inne i klumpen. |
| obj665_01 | 288 × 192 | [192,128,1152,768] | Samme venstrestolpe, mer spredte bruddstykker. Stor buet/grenet metallgruppe øverst til venstre, separate deler oppe til høyre, nedre høyre og langs nedre kant. Bredt svart tomrom i midten. |
| obj666_01 | 224 × 112 | [320,288,896,448] | Høyrestolpe med to tverrfester. Tett samling revne grønne skiltflater, lys ytterkant og synlige grålilla metallbakkanter. Hakk, folder, løse biter og svarte hull. |
| obj667_01 | 280 × 192 | [208,128,1120,768] | Høyrestolpe fortsatt synlig. Stor grønn diagonal plateflate mot nedre høyre, lang bøyd øvre kant og flere adskilte småbiter til venstre og nederst. Stort svart sentralt/venstre tomrom. |

Objekt_i_rom er [0,0,bredde,høyde] for alle fire. Lokal region er det samme. Tallene er ingen fullscene eller panoramaoverlapp: ingen master skal oppstå ved å lime bruddbildene sammen. I fase2 er fragmentene mer spredt, og beskjæringen og canvasplasseringen endres med kildens størrelse.

## Farger, tekst og usikkerhet

Venstrebruddets grå, lilla og nesten svarte metall er dominerende; de grønne småfeltene er spor av skiltflaten på vridde deler. Høyrebruddet er sterkt grønt med svært lyse grønnhvite merker og kanter, grålilla baksider og svart mellomrom. Bevar denne betydningsbærende forskjellen gjennom begge bilder i hvert sett. Ikke gjør venstrebrudd grønt eller høyrebrudd til bart metall av hensyn til en ensartet stil.

De lyse småformene på grønne deler kan inneholde fragmenter av skiltskrift eller høylys. Ingen sammenhengende skilttekst er sikkert lesbar i disse fire kildene. Kopier synlige glyf- og lysformer, ikke gjett veinavn, poengtekst eller et helt ord. Intakt649 er tomt i dette uttrekket og gir ingen tillatelse til å skrive tekst på bruddstykkene. Ikke tolk de lyse feltene som øyne eller tenner.

## Produksjonspresisering og kontroll

Behold ordrett jobbprompt og legg til at dette er ett bestemt bruddlag av et metallskilt, med den angitte siden, paletten, spredningen og stolpen. Glatting av dithering må ikke fylle de svarte hullene, slå sammen frittliggende stykker eller legge til glød, røyk eller flygende skapninger. Sammenlign begge venstrebilder og begge høyrebilder som familier og sammenlign med de intakte forside-/baksidekildene.

Fragmentenes nøyaktige antall må kontrolleres visuelt ved tegning: små ditheringpunkter og tynne forbindelser gjør et rent komponenttall til et usikkert mål på antall fysiske deler. Faktisk timing, kollisjonsretning og hvilke små skriftsplinter som tilhører samme bokstav er ikke dokumentert her. Runtime og ny individuell brukergodkjenning er uverifisert.
