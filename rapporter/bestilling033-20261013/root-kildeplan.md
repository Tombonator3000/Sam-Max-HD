# Kildeplan for bestilling 33

Root har sett alle ti originalkompositter, elleve objektfelt, det sammensatte panoramaet og alle fem målerstillingene, inkludert tre fra bestilling 34. De 40 beskyttede kildefilene og 32 ekstra kontekstfiler er låst. Hele leveranser er RGB1536 ×1024 med motiv [0,112,1536,800] og padding128. Ingen ny individuell brukergodkjenning eller runtime er utført.

## Restauranten, videre gnister og frie ledninger

De tre lag030-jobbene fortsetter serien i bestilling32. lag030_05 viser obj301_05 i [112,136,40,32], en blå/hvit elektrisk gnistgruppe mot gulvet til venstre for den svarte sirkulære åpningen. 46 kildepiksler er endret mot grunnrommet. lag030_07 viser obj301_06 samme sted, med færre små gnistpunkter, 22 endrede piksler. Ikke dupliser tidligere gnisttilstander eller tegn stor lynbue. lag030_06 viser obj299_01 i [104,136,48,32], to egne frie blå/hvite ledningsender ved åpningen, 162 endrede piksler. Ikke overfør den lange ledningen fra lag030_02 i bestilling32. Ingen av disse tre har kildeendringer utenfor sitt felt. Samme agent som lager de fire lag030-jobbene i32 bør eie disse tre.

## Panoramaet med tre separate kikkertdeler

lag031_01 del1 og del2 er samme kildekomposisjon. Bruk samlet master2496 ×800, avledet fra kilderegion x0..624; klipp ved x0 og960 til hver1536-bredde. Overlapp576 ×800 skal være byte-identisk. Originalenes overlapp er allerede bekreftet likt i root-familiebevis.json. Det er ikke fire lagdeler selv om rommet totalt har fire deler. Her leveres bare de to bestilte regionene.

Samlet aktive felt: obj310_01 [40,0,176,24] oppe, obj309_01 [336,128,72,72] nede til venstre for obj306_01 [440,128,72,72]. Del1 sin metadata eier bare310, men viser også48 kildepiksler av309 ved høyre kant. Dette er3387 endrede kildepiksler utenfor del1s egen metadata, ikke feil. Bruk unionen av alle tre felter i felles master. Landskapet og de svarte områdene rundt skal beholdes.

310_01 er en avskåret nedre rund rød/oransje linse-/lupekant med grå innside øverst i kompositten, ikke en komplett ny kikkert. 309 er et venstre panelstykke med myntsliss/avskåret 25¢, brun/gul kobberleder rundt skrue og hvit/lyseblå kabel. 306 er et separat høyre panelstykke med kobberleder og blå kabel. Bevar alle hakk, avskjæringer og svart mellomrom mellom delene. Det skal ikke fylles med et helt kikkertpanel.

## Flyttede ledningsfelt og andre lupeposisjon

lag031_02 viser obj310_02 samme rekt som310_01, men med annen avskåret linseposisjon øverst og en smal grå metallkant med buer nederst i feltet. Bevar svart avstand mellom disse formene; ingen hel ny lupe. lag031_03 viser obj311_01 i [0,0,72,72], den blå ledningen og metallplaten helt øverst til venstre. lag031_04 viser obj312_01 samme plass, hvit/lyseblå ledning med myntsliss. Disse to har egne synlige grønnlige fine konturer fra den faktiske komposittpaletten. Ingen generell palettkorrigering er bestilt. Vis hvert felt mot riktig original og hold avskjæringen mot landskapet. Bare egne rektangler endres.

## Fem egne viserposisjoner med samme underlag

lag031_05 og06 i33 viser obj305_01/02 [280,136,80,40]. De tre neste posisjonene obj305_03/04/05 i34 er låst og sett som kontekst. Viseren peker fra slakt venstre gjennom skrått venstre, rett opp, skrått høyre og slakt høyre. Den skal beholde samme pivot, bredde og grå metallidentitet, ikke få nye tall eller knapper.

Alle fem kompositter har obj308_01 som underlag. Det registrerte underlaget ligger i rom[0,128,320,72], så bare romx240..320 av underlaget synes i del2. Root har bevist at innsetting av dette originale rektangulære utsnittet gjenskaper samtlige kildepiksler utenfor eget305felt, i alle fem tilstander. Bruk derfor eksisterende levert HD obj308_01 som nytt underlag: fra dets motiv [128,368,1280,288], klipp lokale motivx960..1280 og lim inn ved leveranse [0,624,320,288]. Deretter kommer nytegnet305felt ved [160,656,320,160]. Ingen originalpiksler eller kildemasker brukes til ny kunst.

Underlaget er allerede levert med egenkontrollOK i bestilling8, SHA0b18ae890130f959252d444c82c965a6b7651fa644e5fd77b417b965ca4d67ca. At toppdelen obj307 fra samme historiske master fortsatt harFEIL gjør ikke dette nederste utsnittet til en ny godkjent toppdel. Ingen endring i307s status. Root-familiebevis dokumenterer 4031 originale underlagspiksler utenfor305 i disse komposittene. Verifiser pikselidentitet utenfor faktisk underlags- og feltunion, ikke bare305.

## Leveranse og kontroll

Innebygd bildeverktøy med riktig egen original og godkjent HD-stil, beskyttede jobbprompter beholdt og kildepresisering i egen logg. Vanlig presis skalering og innplassering av nye komponenter er autorisert. Ingen vektorunntak, originalkonturmasker, originalpiksler som ferdig kunst eller lokale geometriwarper. Bevar kun faktiske motivfragmenter. Uendret checker og eksplisitt kontroll av elleve metadatafelt, underlag, helscener, innklippskanter og panoramaoverlapp. Root eier Git og globale logger. Planen er produksjonsgrunnlag, ikke fullført leveranse.
