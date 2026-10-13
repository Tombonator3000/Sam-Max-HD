# Native vektorkandidater for rom090 og obj901_01

Tom svarte uttrykkelig «Bruk presis vektorrekonstruksjon for begge» om akkurat disse to jobbene. Root formidlet ordren 13. oktober 2026. [Metodevalget](TOMS-METODEVALG.json) låser dette avgrensede omfanget. Det er ingen generell tillatelse til vektormetoden for andre jobber.

Begge kandidatene får **OK** fra uendret sjekk_leveranse.py i separate rapportkloner med de fire eksakte kildefilene. Produksjonsjobbene er ikke overskrevet. Root tar mottak og eventuell levering. Teknisk OK er ikke runtime eller ny individuell bildegodkjenning.

| Kandidat | Globalt skift | Blokkskift | Kantlikhet |
|---|---:|---:|---:|
| [rom090 PNG](rom090-kandidat.png) / [SVG](rom090-kandidat.svg) | 0.01 | 0.03 | 1.00 |
| [obj901_01 PNG](obj901_01-kandidat.png) / [SVG](obj901_01-kandidat.svg) | 0.02 | 0.15 | 1.00 |

## Kilder og metode

Original_1x er geometrisk og fargemessig kilde. [Åtte kildehash](kildehash.json) er kontrollert uendret. Tidligere imagegen-kandidater er arkivert med egne hash i tidligere-resultathash.json og vises sammen med original og native vektor i [før/etter-kontaktarket](samlet-foer-etter.png).

Oppskriften er avledet fra den korrigerte rom077-oppskriften; kildehash og tilpasninger står i [metodeproveniens.json](metodeproveniens.json). Den bruker et kildenativt, plant nett av delte fargegrenser. Hver grensekjede forenkles én gang og gjenbrukes på begge sider. Kryss-/endeknutepunktene står fast. Ordinær RDP-toleranse er 0.8 originalpiksel på ALLE kjeder; særunntaket 1.6 for veisider i rom077 er fjernet. Små lukkede løkker som ville kollapse beholdes med sine originale vektorknutepunkter.

SVG inneholder bare native polygonstier med even-odd-fyll og flate kildefarger, samt nøytral padding i lerretversjonen. Ingen bitmap, image-element, gradient eller ekstern ressurs er innebygd. Dette er uttrykkelig autorisert rekonstruksjon av kildegeometri; det er ikke imagegen eller en påstand om ny frihåndstegning. Ingen originalmaske legges over en avvist generering.

PNG rasteriserer de samme vektorstiene ved samplesentre, med halvåpne intervaller og even-odd-scanlinerendering. 16 samples per originalpiksel area-gjennomsnittes til 4x med BOX. Dermed unngås den gamle PIL-feilen med inkluderende endepunkter. Mellomtoner finnes ved antialiaserte kanter; flate felt beholder kildefargene. Rasterdekningen er målt uten hull ved alle samplesentre. Dette alene er ikke et generelt matematisk topologibevis.

## Geometri og visuelt innhold

Rom090: 320 x 120 blir 1280 x 480 ved [128,272] på 1536 x 1024. Alle 41 farger og 2274 regionløkker beholdes. 5680 delte grensekjeder går fra 19 124 til 14 999 registrerte knutepunkter, med maksimalt målt avvik 0.8 originalpiksel. Den tette dekoren på hyllene er bevart; enkelte små trappekanter står derfor fortsatt tydelig. Sam-hodets kildeuttrykk og hatten, to avskårne Max-ører, tomt blått felt, toppbuer og draperifolder er sammenlignet visuelt. Ingen Max-kropp, ansikt eller pistoler er lagt inn. Draperiet følger nå kildens faktiske fargeregioner fremfor imagegen-forsøkets nye folder.

Obj901_01: 128 x 128 blir 512 x 512 ved [512,256]. Alle åtte kildefarger og elleve regionløkker beholdes. 30 grensekjeder går fra 1117 til 127 knutepunkter. Maksimalt målt avvik er 0.8 originalpiksel. Den tomme røde bakgrunnen, trinnvise mørke sømmen, brune høyrekanten og avskårne sokkelflaten følger kilden. Imagegen-forsøkets tydeligere ovale rand er ikke videreført. Hår og støtte er fortsatt fraværende.

Begge motivgrenser måler nøyaktig [0,0,320,120] og [0,0,128,128] i originalkoordinater. Alle kjedeendepunkter er kontrollert mot kilden, og avstanden fra hvert kildeknutepunkt til nærmeste segment i sin nye kjede er målt. Padding er eksakt RGB128 overalt utenfor metadatarektangelet; motivet er byte-identisk med den separate rasteriserte motivfilen. Detaljene står i rom090-geometriqa.json og obj901_01-geometriqa.json. Ingen global eller lokal flytting er gjort.

## Proveniens og begrensninger

[leveranser.json](leveranser.json) inneholder kandidat-SHA, format, kontrollstatus og hash av checker/oppskrifter. [rekonstruer.py.txt](rekonstruer.py.txt), [forbered.py.txt](forbered.py.txt) og [kontroller.py.txt](kontroller.py.txt) er rapportoppskrifter; motor-/pipelinekode er ikke endret. De native motiv-SVG-ene har originalens viewBox med 4x fysisk størrelse. Kandidat-SVG-ene har hele 1536 x 1024-lerretet med riktig oversettelse og 4x-skalering.

Visuelt før/etter er kontrollert mot faktisk original og tidligere forsøk. Resultatet prioriterer kildegeometri og flat palett; rom090 blir ikke en ny malerisk frihåndsvariant. Begrensningen er særlig synlig i tett smågrafikk, som ikke er fjernet eller oppfunnet på nytt. Ingen import, runtime, publisering eller ny individuell bildeaksept er utført. Uavhengig QA og endelig mottak håndteres videre av root/C.

## Endelig mottak

Root har sett original, tidligere kandidat og vektor sammen, lest C sin kontroll og kjørt uendret checker på de faktiske jobbleveransene: begge OK. PNG og notat er lagt i jobbmappene. Kandidatbeskrivelsen over gjelder tidligere status før dette mottaket; aktuell leveransestatus står i fremdrift.json og root-mottak.json. Ingen ny individuell bildeaksept, motorimport eller runtime.
