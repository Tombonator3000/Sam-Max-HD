# Bestilling 52 – Sam, fig002_02–07

Kildeanalyse 14. oktober 2026. Ingen bildegenerering eller resultatendring utført. De 14 leveransene i 49/50 er frosset for rotkontroll. Denne planen eier bare seks Sam-ark; A sine ikoner er ikke berørt.

## Dokumentert grunnlag

24 beskyttede filer er låst i `c-kildehash.json`: jobb.json, prompt.txt, referanse.png og original_1x.png for hvert ark. `c-ankerhash.json` låser hovedark, pilot, originalmetadata og brukerens pilotgodkjenning. `c-rutekart-kilde.json` inneholder alle 72 rutene, eksakte originalrektangler, synlighetsbokser, HD-bokser, animasjon, retning, lag, cel og relative sammensettingskoordinater. `c-original-kontaktark.png` viser alle seks originaler. De 17 `c-sekvens-*.png` viser gruppene separat i lagret ressursrekkefølge. `c-original-lagsammensetting.png` viser fem originalkomposisjoner med pilotkropper, nye talehoder og håndlag på dokumenterte rel-koordinater. Ingen av disse kildeutsnittene eller diagnostiske alfaene skal brukes som produksjonsmasker.

Kostyme 2 bruker rom 1-paletten, format 0x58, 16 palettindekser. Originalmetadata oppgir transparent indeks 255 for flere komponenter, men 251 for animasjon 7. Leveransearkenes egen bakgrunn er likevel eksplisitt magenta [255,0,255]; palettindeks og arkbakgrunn må ikke blandes. Figuren er Sam, dokumentert både i jobbmetadata, hovedark og levert pilot.

`TOMS-GODKJENNING.json` fra stilpiloten dokumenterer brukerens godkjenning 13. oktober. Pilotnotatets eldre formulering om manglende visuell godkjenning er historisk og overstyres av denne. Motorimport og runtime er fortsatt uverifisert.

## De seks arkene

| Ark | Ruter | Faktisk innhold og lag |
|---|---:|---|
| fig002_02 | 22 | 8 helfigurer i høyrevendt gangsyklus, animasjon 2/retning 1/lag 1, cel 150–157. Deretter 14 separate høyrevendte **hele hoder med hatt**, animasjon 4/retning 1/lag 3. Ikke bare løse munner og ikke helfigurer. |
| fig002_03 | 15 | 13 frontvendte talehoder på lag 3, animasjon 4/retning 2; deretter 2 bakvendte hoder, retning 3. Hatt, ører, snute og halsavkutting inngår i hver rute. |
| fig002_04 | 8 | Frontvendt gangsyklus, animasjon 2/retning 2/lag 1, cel 141–148. Egne føtter, armposisjoner og kroppsvugging. |
| fig002_05 | 13 | 8 bakvendte gangruter, cel 132–139; deretter 5 **håndlag med to adskilte brune deler i hver rute**, cel 257–261, animasjon 6/retning 1/lag 2. Tomrommet mellom hendene er nødvendig. |
| fig002_06 | 11 | 5 høyrevendte helfigurer, animasjon 7, cel 171–175: hendene beveges sammen foran bryst/slips og overkroppen endres. Deretter animasjon 10 i tre retninger med utstrakt hånd; animasjon 11 i tre retninger med kroppen bøyd ned og hånd nær bakken. |
| fig002_07 | 3 | Animasjon 12 i tre retninger: hevet åpen hånd og egen lent/balansert kroppspositur. Cel 164,160,168. Ingen synlig holdt rekvisitt i disse tre kildene. |

Retning 1 er høyre, 2 mot oss og 3 bort, i samsvar med jobbtekst og synlig original. Retning 0 deler cels med 1 i originalmetadata; prompten beskriver venstrevending som speiling. Det skal ikke opprettes ekstra venstreruter.

## Sammenheng som ikke må mistes

Animasjon 4 bruker også hvilende hoder som allerede finnes i fig002_01: 385 (høyre), 384 (front) og 386 (bak). De er utelatt fra de nye arkene fordi samme cel allerede er levert. Høyre ressursliste ender på 385; frontlisten har 384 mellom 417 og 423; baklisten ender på 386. Animasjon 6 gjenbruker pilotens håndcel 256 etter 257–261. Animasjon 8 gjenbruker 174,173,172,171 fra animasjon 7 i motsatt rekkefølge. Nye stillbilder må derfor kontrolleres mot eksisterende hvilestillinger og begge bevegelsesretninger.

Lag 3 sine talehoder plasseres over lag 1-kroppene 129/128/130, med lag 2-hånd 256 på høyre kropp. Eksempel 394 har rel(-13,-70), 412 rel(-12,-70), 390 rel(-13,-69). Håndvarianter 257–261 har rel_x -15 eller -14 og rel_y -29. Originalkomposisjonsarket viser at disse delene faktisk passer kroppen; de skal ikke gis ny hals, arm eller egen kroppsdel som fyller mellomrommet.

Originalmetadata er en deduplisert ressursliste i første forekomst-rekkefølge, **ikke** full avspilling med gjentakelser og varighet (`konsept/2026-10-12/ANALYSE.md`, avsnitt om animasjonsuttrekk). Sekvensarkene beviser derfor posefamilie og ressursrekkefølge, ikke animasjonstiming eller motoroppførsel. Ingen runtime-test er kjørt.

## Identitet og pilot

Sam er stor og bred over magen, med lang brun snute, mørk nese, hengende ører, liten blågrå fedora, blågrå dress/bukser, hvit skjorte og bredt mørkeblått/svart diagonalt stripet slips. Kilden og hovedarket viser **brune bare poter**, ikke påkledde sko. Ikke legg til såler, skolisser eller nye hansker. Hattens størrelse og snutens lengde må ikke vokse mellom gangruter og talehoder. Frontens ører må ikke bli høyreprofilens snute. Bakfra beholdes de to ørene og hattens særegne perspektiv.

Piloten er ni separate ruter, inkludert hodeløse kropper, to håndbiter i én rute og små øyelokk. De små lag 4-delene ble særskilt bekreftet som øyelokk, ikke munn. Pilotens tekniske kontroll utelot de to minste lokkrutene; separat kontroll dekket dem. Hovedarket er identitets- og tegningsanker; pilotens faktiske cel-størrelser, farger og sammensetting er nødvendig familieanker. Ny helfigur skal ikke blindt arve hovedarkets størrelse eller frontalpositur.

## Gestus og usikkerhet før produksjon

Animasjon 7 viser sikkert håndbevegelse ved bryst/slips, med fem ulike arm-/kroppsposisjoner. Et konkret navn som «justerer slips», «gnir hendene» eller «trekker fram en ting» er **ikke kildebevist her**. Jeg ser ikke en separat sikker rekvisitt som skal tegnes. Animasjon 10/11/12 har sikkert henholdsvis hånd ut, kropp bøyd ned, og hånd opp. En funksjon som bruk/plukk/vink er en mulig tolkning, ikke dokumentert funksjon fra disse metadataene. Før bildene bestilles bør rot sammenligne de viste gruppene med piloten og avgjøre om bevegelsesformen alene er tilstrekkelig, eller om særlig animasjon 7 krever brukeravklaring. Ingen slik rekvisitt skal oppfinnes.

## Leveransekontrakt og anbefalt rekkefølge

Alle ark er 1536 × 1024 med ekte RGBA. Kildens 352 × 240 felt ligger ved [64,32,1408,960], men både magenta og grå kildepadding skal være transparent i leveransen. Synlig boks [sx0,sy0,sx1,sy1] blir [64+4sx0,32+4sy0,64+4sx1,32+4sy1]. Rektanglene er rutepakking, ikke verdensposisjon; rel-koordinatene brukes først ved sammensatt QA. Rute- og hånddelantall skal bevares.

Anbefalt samlet eier for Sam-familien. Først etabler konsistent gangfamilie 02/04/05, deretter talehoder 02/03 mot pilotens tre hvilende hoder og kropper. Håndlag 05 kontrolleres både separat og over pilotkroppen. Til slutt gestusark 06/07 etter betydningsavklaring. Fordel genereringskall i håndterbare grupper; dette endrer ikke at samme ferdige ark må ha nøyaktig alle sine ruter.

Uendret `verktoy/sjekk_leveranse.py` kontrollerer ekte alfa, størrelser, sentre og omriss. Den hopper over kilder med færre enn 20 ikke-bakgrunnspiksler; alle 72 rutene må derfor også få eksplisitt telling/boks- og komponentkontroll. Ingen originalkontur skal brukes som produksjonsmaske for å tvinge en nytegning gjennom kontrollen. Slutt-QA må vise alle retninger sammen, hode/kropp/håndsammensetting og overganger til pilotens gjenbrukte cels. Teknisk OK kan ikke alene bevise riktig gestus, øye, munn eller klær.

Status: kildeplan og kontaktark klare; generering ikke startet, runtime false, ny individuell brukergodkjenning false.
