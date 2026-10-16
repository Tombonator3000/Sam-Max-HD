# Returleveranse fig091_03

Dato: 15. oktober 2026. Gren: gpt-arbeid.

Rettet costume091_1955 etter ORDRE.md. Hele arket leveres som RGBA på 1536 x 1024 med ekte alfa. De andre tolv rutene er bevart pikselidentisk. Returen har ingen egen retur.md; ordreteksten og forhandsvisning/myk_fig091_03.png er brukt.

## Kilde og motiv

Originalen er jobbens referanse.png og original_1x.png. Sam holder et blått lokk med en gul stjerne. Kroppen er avskåret, og en liten brun fotrest står separat nedenfor. Hoveddelens kildeboks på HD-lerretet er [1096,672,276,212], fotresten [1096,904,28,44]. Hele rutens høyde er 276 piksler med mellomrommet og fotresten. Hoveddelen skal derfor ikke strekkes til denne høyden.

hovedark/sam.png er godkjent stilreferanse. Den styrer Sams identitet, dress, hatt og strek; originalen styrer positur, geometri, rekvisitt og avkutting. ANALYSE.md, GJENNOMGANG.md og remake-skillen fra lokal main er lest. Tidligere forklaring av måleforskjellen i rapporter/videre-grafikk-20261015/RAPPORT.md er beholdt som bakgrunn, men fritar ikke konturene for kontroll.

## Verktøy og forsøk

Innebygd image_gen, to bildeforsøk. Eksakt modellnavn vises ikke. prompt.txt ble brukt ordrett med separat returpresisering. Beskyttede jobbfiler er ikke endret. Faktiske prompter, råbilder og førbilde ligger i rapporter/natt-fig091_03-20261015/.

Første forsøk endret hele arket og ble forkastet. Andre forsøk brukte et utsnitt av originalruten som bilde en, Sam-hovedarket som bilde to og den tidligere ruten som feilbeskrivelse i bilde tre. Den nye hoveddelen og den nye fotresten ble beskåret etter sin egen alfa og skalert hver for seg til originalens komponentbokser med Lanczos. Python/Pillow er bare brukt til denne plasseringen og alfaopprydding, ikke til å tegne motivet. Ingen originalmaske eller lokal deformering er brukt. Oppskriften er bevart i plassering.py.txt. Alfa under 16 er nullstilt, og resten normalisert fra 254 til 255 før plassering.

## Kontroll

Uendret verktoy/sjekk_leveranse.py gir OK, 13 av 13 ruter OK. Kjørt med eksisterende Python 3.12 fra Codex-runtime siden systemets python3 mangler numpy. Ingen global installasjon ble gjort.

Rute1955s snitt delt på union mot originalkonturen på fast plass steg fra 0,857 til 0,928. Dette er en ekstra omrissmåling, ikke Toms visuelle godkjenning. Hovedfigur, hatt, grep, lokk og separat fotrest er sammenlignet visuelt med originalen. Resten av arket er pikselidentisk med førbildet. Rutekart for alle 13 ruter og SHA256 står i rapportens fremdrift.json.

SHA256 for resultat.png: 322eca10b29b94409b0391e9ab86e4775c9cfeccd1fe8f11eb87f9c1ea2fc5ca.

Usikkerhet: Små indre ansiktsstreker og fingre er fortsatt tegnetolkninger. Avspilling av hele animasjonen i motoren, importkontroll hos Claude og Toms visuelle vurdering er ikke utført her. Bare rute1955 er nytegnet i denne leveransen.

Git pull ble forsøkt, men sandkassen nektet skriving til FETCH_HEAD utenfor arbeidsmappen. Ingen grenbytte, commit, push eller historikkendring er gjort.
