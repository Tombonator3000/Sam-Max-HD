# Max, kostyme 3: fig003_02–05

Kildeanalyse 14. oktober 2026. Dette omfatter bare fire Max-ark, 66 ruter i 20 ressursgrupper. Ingen produksjonsbilder er endret eller generert i denne analysen. 16 beskyttede filer er låst i `b-kildehash.json`. Hovedark, levert pilot, stilreferanse, originalmetadata og pilotgodkjenning er låst i `b-ankerhash.json`.

## Identitet og grunnlag

Alle fire originalark, det godkjente Max-hovedarket og pilotens faktiske resultat er sett. Max har kremhvit kropp, lange ører med rosa innside foran, små mørke øyne, liten rosa nese, bred tannmunn, kort kropp og store bare poter. Bakfra har hodet ingen nye øyne, munn eller rosa øreinnside. Kildens skyggelag er beige/gråbrunt og må ikke bli ny rekvisitt eller påkledning. Ingen hatt, klær eller holdt gjenstand er synlig i disse 66 rutene.

Originalmetadata finnes i `konsept/2026-10-12/kostymer-originalmetadata.json`, nøkkel `3`. Kostyme 3 bruker rom 1, format 0x58 og 16 palettindekser. Arkbakgrunnen er cyan RGB [0,200,200], ikke kostymets transparente indeks 255. Ferdige ark skal ha ekte RGBA, med både cyan og grå padding helt transparente. Referansefeltet er [64,32,1408,960] på 1536 × 1024; rutegeometrien er originalskala 4. Hovedarkets dimensjoner skal ikke brukes til å skalere figurens kropp uavhengig av kilden.

`b-ruteregister.json` bevarer alle originalrektangler, synlige bokser, HD-bokser, cel, animasjon, retning, lag, nr, rel-koordinater og move-koordinater. Rel bestemmer sammensetting, ikke rutens plass i det pakkede arket. Move er dokumentert, men ikke lagt til hvert stillbilde som om det var en ekstra lokal offset. Ressurslisten er deduplisert og beviser ikke tidsforløp, varighet eller runtime.

## De fire arkene

| Ark | Antall | Faktisk innhold |
|---|---:|---|
| fig003_02 | 23 | 12 separate frontvendte talehoder, cel 406–419 i metadataens rekkefølge; tre bakhoder 424/423/422; åtte frontvendte hele gangfigurer 132–139. Munner skifter mellom tannrekker, åpne mørke felt og utstrakt tunge. Ikke fyll på kropp under hodelagene. |
| fig003_03 | 19 | Åtte bakvendte hele gangfigurer 140–147. Deretter sju hodeløse kroppsstillinger i animasjon 6: høyre 158–160, front 163/164, bak 167/168. To egne små lag 4-striper 551/552. Til slutt to frontvendte helfigurer 173/174 med armstilling ut til siden. |
| fig003_04 | 8 | To frontvendte helfigurer 175/176 med hevet fot og åpen hånd. To høyrefigurer 178/179 med utstrakt arm, samt separat mørkere hånd 307. To foroverbøyde høyrefigurer 184/185 og separat mørkere hånd 313. Lag 2 må tegnes separat og kobles til riktig kropp. |
| fig003_05 | 16 | To frontvendte figurer 171/172 med hånd lavt ved bakken. Fire høyre håndvarianter 308–311 og to lave håndvarianter 314/315. Åtte egne bakhoder: 432/433/434, 427 og 428–431; ørene endrer vinkel og høyde. |

Retning 1 er høyre, 2 mot oss og 3 bort. Retning 0 viser de samme ressursene som 1 i metadata; det gir ikke tillatelse til å legge til ekstra venstreruter i disse arkene.

## Lag og små detaljer

`b-sammensetting-1.png` til `-3.png` viser 25 diagnostiske originalkomposisjoner etter rel-koordinatene. Kildens cyan er bare fjernet for disse lesbare diagnosebildene. Diagnostisk kildealfa må aldri brukes til produksjonsmaskering.

Fronttalehodene passer over pilotkropp 128, bakhodene over 130. Animasjon 6 sine hodeløse kropper passer med hvilende pilothoder 385/384/386. De små rutene 551/552 ligger ved rel(-4,-22), akkurat ved bakhodets nedre hals-/kroppsskjøt. De er ikke frontøyne eller munn: originalkomposisjonen plasserer dem på bakre nakkekant. Den nøyaktige funksjonsbetegnelsen er usikker, men laget, formen og sammensettingen er konkrete. Hver rute er 9 × 2 kildepiksler med 16 synlige piksler, og rutene skiller seg i fem fargepiksler i nederste rad. De skal ikke dedupliseres. Checkerens grense på 20 kildepiksler gjør at disse må få egen eksplisitt QA, inkludert 36 × 8 HD-ramme og beholdt egen tonevariant.

Hånd 307 og variantene 308–311 ligger over kropp 179; hånd 313 og variantene 314/315 over 185. De har egne fingeråpninger, håndflater og avskjæringer. En åpen hånd skal ikke bli en ny holdt ting. Animasjon 10 og 13 gjenbruker 178/179/307; 11 og 15 gjenbruker 184/185/313. Animasjon 14 avsluttes i ressurslisten med 307. Animasjon 21 inkluderer til slutt 432, som allerede finnes tidligere i samme leveranseark. Det skal ikke tegnes en tilfeldig ny variant for en gjenbrukt cel.

## Gestus og usikkerhet

Gange og tale er tydelige og uavhengige. De øvrige gruppene viser sikkert arm ut, arm opp, kropp bøyd ned, hånd lavt og bakhodets ørevipping. Jeg finner ingen sikker rekvisitt som krever et navn. Ord som plukke opp, bruke, vinke eller balansere er funksjonstolkninger, ikke bevist av disse metadataene. Bevegelsesformen kan tegnes uten å oppfinne funksjon eller objekt. Rot får særlig beskjed om 551/552 og at deres lag 4-betydning ikke må arves fra pilotens frontøyelokk.

## Produksjons- og kontrollplan

Bruk innebygd imagegen, ordrett jobbprompt med separat kildepresisering, hovedark og godkjent pilot. Nytegningens egen alfa er eneste produksjonsalfa. Komponentgrupper kan genereres separat for konsistens, men hver cel må spores til riktig original og plasseres i sitt eget pakkerektangel. Ingen originalsilhuett, konturtrace eller lokal warp for å oppnå teknisk samsvar.

Først tale-/ganggruppene mot pilotens eksisterende hoder og gangstil. Deretter hodeløse kropper og håndlag, med sammensatt QA på originale rel-koordinater. Hold alle særegne munn-/øre-/fingerstillinger separate. Vis hele familien på lys og mørk bakgrunn for å avsløre cyanrester eller uekte transparens. Kontroller alle 66 ruter manuelt og teknisk, inkludert de to 16-pikselrutene som standardkontrollen kan hoppe over. Ingen runtime, timing eller ny individuell brukergodkjenning er bekreftet.
