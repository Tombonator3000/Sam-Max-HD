# Kildeplan for bestilling 19

13. oktober 2026. Kun kildeanalyse og rapportfiler. Ingen generering, jobbfiler, globale logger eller Git er endret. Kildetro-skill er brukt. Alle ti originaler er sett i kontaktark og i 4× referanse; obj293 er også sett som kontekst. Metadata, låste promptbytes, ressursregisteret og romnotater fra origin/main er lest. 40 nåværende beskyttede kildefiler er låst i kildehash.json.

## Viktigste rettelse: «slangene» er hånd og redskap

Registerets snake-m og n-snake er interne navn. Originalene viser en brun, inntørket hånd med fem fingre og lange gule negler, festet ved grønn leddet golfballhenter. Dette er ikke levende slanger, ormer eller et nytt dyr. De røde/oransje formene i 821–823 er en fiskemagnet med grønne finner, øye og to grå metallender, ikke et levende dyr som skal få munn/anatomi.

LucasArts' offisielle hintbok, trykt side 14 og 33, beskriver at Jesse James' hånd kombineres med golfballhenteren og fiskemagneten for å hente mood ring fra hyssingballen. Dette støtter identiteten i de faktiske bildene. [Offisiell hintbok, skannet primærkilde](https://www.mocagh.org/lucasfilm/sammax-hintbook.pdf). Full PDF kunne ikke åpnes i webverktøyet på grunn av størrelsesgrense; relevante tekstutdrag ble tilgjengelige gjennom indeksert søk. Ingen lang tekst er kopiert.

## Rektangler og lag

Alle lerret er 1536 × 1024 med RGB128-padding. Tabellen bruker [x,y,b,h]. Alle objektene er SMAP og tilstand 01; dette betyr ikke at de er samme animasjonsfase.

| Jobb | Originalregion | HD-motivfelt | Objektets romposisjon |
| --- | --- | --- | --- |
| rom079 del1 | [0,0,384,200] | [0,112,1536,800] | ikke objekt |
| rom079 del2 | [256,0,384,200] | [0,112,1536,800] | ikke objekt |
| obj819_01 | [0,0,320,200] | [128,112,1280,800] | [0,0,320,200] |
| obj821_01 | [0,0,240,152] | [288,208,960,608] | [0,32,240,152] |
| obj822_01 | [0,0,240,152] | [288,208,960,608] | [0,0,240,152] |
| obj823_01 | [0,0,160,120] | [448,272,640,480] | [0,0,160,120] |
| obj828_01 | [0,0,168,120] | [432,272,672,480] | [0,0,168,120] |
| obj829_01 | [0,0,256,152] | [256,208,1024,608] | [0,0,256,152] |
| obj830_01 | [0,0,240,160] | [288,192,960,640] | [0,0,240,160] |
| obj831_01 | [0,0,240,160] | [288,192,960,640] | [0,0,240,160] |

Rom80 har metadata bredde 8 og rom82 bredde 0. Dette er ikke grunnlag for å klippe objektmotivet til rombredden eller finne på en bakgrunn. Svarte felt i objektoriginalene skal beholdes; faktisk transparens/motorbehandling er ikke testet.

## Rom079 og globe-cycler 819

Fulloriginalen er 640 × 200 og inneholder to store avbildninger av snøkulen med brune fingre, mansjett/frakk og blå bakgrunn. Venstre kule er opp-ned, høyre rettvendt. Kulerommet har en stilisert skjev bygning, tre mørke spisse trær med gule kanter, rød/oransje innside og hvite glassreflekser. Ikke erstatt innholdet med vinterlandskap, snøvær eller realistisk glass som skjuler den grafiske tegningen.

Tekst på svart/blå sokkel: THE MYSTERY VORTEX i gul/oransje skrift, med en liten rød kursiv forløper som visuelt leses som Enjoy. Den lille skriftens konkrete former må brukes som fasit fremfor automatisk typesetting. Ikke legg til ny tekst eller rett skjevheten.

Viktig geometrisk presisering: promptens «mirrored» om venstre tekst er upresis. En 180° analysevisning av obj819 gjør ordene normalt lesbare. Det er opp-ned/rotert motiv, ikke grunnlag for en ekstra horisontal speilvending. Analysebildet obj819-lesevendt-180-kun-analyse.png skal aldri brukes som leveranseorientering.

Deloverlapp 128 × 200 originalpiksler er byte-identisk som dekodet RGB: null avvik. Anbefalt én 2560 × 800 master, klipp x0 og x1024, overlapp 512 × 800. Ikke «samle» de to kuleavbildningene til én kule eller rette den venstre. Ingen ekstra romdel utenfor bestillingen trengs.

819 er en selvstendig variant av venstre 320 × 200, med sterkere blå/cyan bølgefelt i bakgrunnen. Sammenligning mot venstre 320 piksler av rommaster gir 27 807 ulike piksler av 64 000. Derfor skal den ikke blindt klippes fra vanlig rom079-master. Felles hånd/kuleidentitet skal bevares, men bakgrunnen følger 819. Registeret heter globe-cycler; navnet beviser ikke animasjonshastighet eller palettrotasjon.

Naboregisteret har globe-cork 814, globe-hand-1 til -4 (815–818) og globe-vortex 820. Disse er separate ressurser og skal ikke males inn i nåværende originaler. Hintboka støtter snøkulens senere forbindelse til kork og minivortex, men sier ikke hvilken runtime-tilstand disse konkrete bytes viser.

## Hånd + magnet, 821–823

- 821 / snake-m-5: to adskilte grønne leddsegmenter øverst/venstre, ett koblet til den store bøyde hånden. Fingrene holder fiskemagneten. Ingen farget ring ved metallendene. Gult leddpunkt og mørke grønne sideflater beholdes.
- 822 / snake-m-8: samme type grep og to grønne segmenter, men svart/grå ring og sterkt cyan/blå/grønn/lilla/rosa ringflate ligger ved magnetens nedre/høyre åpning. Ikke fjern ringen som «palettstøy». Figurplassering er ikke identisk med 821.
- 823 / snake-m-9: mindre originalfelt og annen avkutting. Ett separat grønt leddsegment øverst til venstre; håndleddet er diagonalt avklipt. Fiskemagnet og farget ring finnes, nedre/høyre kant klipper deler. Ikke fullfør den skjulte armen eller legg til segment nummer to.

Paletter: 821 har 28 RGB-farger, 822 har 98 og 823 har 97. Den store økningen følger den fargerike ringflaten. Svart er vanligste farge. Håndens brune rynker, gule negler, grønn mekanikk og fiskens røde/oransje/grønne/grå palett er konkrete kildeegenskaper. Ikke bruk Sams brune håndstil som identitet; dette er den inntørkede rekvisitten.

## Tom hånd, 828–831

- 828 / n-snake-2: ett øvre grønt segment og diagonalt avklipt håndledd; åpen hånd med fem fingre/negler og svart tomrom mellom fingrene. Ingen magnet eller ring.
- 829 / n-snake-3: større felt 256 × 152 med to grønne segmenter; åpen hånd i annen plass/pose enn 828. Begge gule leddpunkter tydelige.
- 830 / n-snake-4: 240 × 160, to segmenter; litt annen knekk/leddplassering og negler/fingerspredning. Nedre gule punkt er delvis avklipt/tildekket av formen.
- 831 / n-snake-5: samme feltmål som 830, men ny konkret pose. Ikke en duplikat: 5 535 piksler avviker, innen lokal bbox [0,6,234,153] med eksklusive høyre/nedre kanter. Både grønne ledd og hånd er endret.

828 har 18 unike RGB-farger; 829–831 har 20 hver. Svarte felt, mørkegrønt metall, lysgrønne kanter, gule leddpunkter/negler og brun hud er stabile identitetsankre. Ikke gjør negler til monsterklør eller håndflaten til et hode. Bevar fem fingre selv når perspektivet gir overlapp; ikke tegn ekstra fingre for å fylle hull.

Registeret viser også 824 snake-m-10 og 827 n-snake-1 som 72 × 48 nabodeler, samt mag-1/mag-2 i rom81. Ingen tilsvarende jobbmappe for 827 ble funnet ved direkte referanseoppslag. Disse er kontekst, ikke ekstra bestilte bilder. 293 snake-m-2 er sett med samme redskap i hyssingmiljø og støtter kontinuiteten. Ikke importer miljøbakgrunnen i de svarte nærbildene.

## Sammensetting, risiko og anbefalt arbeidsdeling

Rom079 er det eneste dokumenterte panoramaparet. Håndressursene er ulike tegnede tilstander med ulike felt/avkuttinger; de skal ikke settes ved siden av hverandre som panorama eller tvinges til identiske masker. Samlet familiekontroll er nødvendig for fingre, negler, grønne ledd, kontakt mellom hånd og magnet, samt ringens tilstedeværelse.

Anbefalt A: rom079 begge deler + obj819 (én konsistent kule-/håndfamilie, men egen bakgrunnsvariant). B: obj821/822/823 (grep, magnet og ringtilstander samlet). C: obj828/829/830/831 (tom hånd og grønn mekanikk samlet). B og C skal utveksle kildebasert identitetskontroll, ikke kopiere en feil generert variant. La én rotkontroll sammenligne alle sju håndvarianter ved avslutning.

Største feilrisikoer: generere slanger ut fra navn; gjøre fiskemagneten levende; bytte den inntørkede hånden til Sam/monster; speilvende venstre kule feil; normalisere skjeve bokstaver; kopiere feil blå bakgrunn til819; fylle svart tomrom; oppfinne fingre eller mekaniske forbindelser; fjerne/legge til ringen i feil tilstand; slå sammen830/831 som duplikater.

## Bevis og begrensninger

c-palettbevis.json inneholder målte RGB-paletter og vanligste farger. original-kontaktark.png, rom079-original-full.png og den tydelig merkede analysevendingen er kildebevis, ikke ny HD-grafikk. 40 kildehashes kontrolleres på nytt etter rapportskriving.

Ressursnavn og hintbok støtter gjenstandsidentitet og gåterelasjon. Rekkefølgen mellom enkeltbildene, timing, skript, runtime, transparens, fargebytte og faktisk motorkomposisjon er ikke verifisert. Ingen produksjon er startet. Ingen ny brukergodkjenning eller runtime-test påstås.
