# Bestilling 18 A: ny kikkertmaster og tre striper

Obj811_01, obj812_01 og obj813_01 er levert fra én ny 1280 × 800-master. B-kildeplan.md, GRUNNLAG.md, alle tre originalreferanser, jobbmetadata og dagens låste prompttekst er lest før produksjon. Originalene ble samlet i rekkefølgen 812, 811, 813. Tidligere bestilling 8 er ikke brukt som bildegrunnlag.

## Motiv og valgt resultat

Den svarte synsåpningen er tom. Den røde ringen med gul/oransje kant, to lyse skrå bånd, grålilla metall, avkuttede brune hender, hvite mansjetter, blå ermer og grønne felt ved mansjettene er bevart. 25¢, smal vertikal myntsliss, oppreist spak og vifteformet skala er visuelt kontrollert. Ingen landskap, ansikter, ekstra kropp eller ny tekst er satt inn.

Valgt bilde er tredje fullgenerering. De første to kant-til-kant-masterne endret apparatets høydefordeling og panelgeometri og ga FEIL. Tredje forsøk brukte originalmasteren på vanlig 1536 × 1024-canvas, med motiv [128,112,1280,800]. Dette ga riktig plassering uten lokal warp. Råbilder og kontrollfiler fra alle forsøk er bevart. Eksakt modellnavn er ikke eksponert; alle tre kall brukte innebygd ChatGPT-bildegenerator. Stil/rom007_del1av2.png var kun kvalitetsreferanse.

## Kildebegrunnet svartnormalisering

Originalmasterens palett har ingen ikke-svarte farger med maksimal RGB-kanal under 12. Den inneholder store tilsiktet helt svarte felter. Tredje generering la inn svært svake toner, blant annet 38345 piksler RGB (1,0,0), 12598 RGB (1,1,1) og 7590 RGB (1,1,0).

Kriteriet er nøyaktig max(R,G,B) < 12, anvendt på genererte piksler. Alle kvalifiserte piksler settes til RGB (0,0,0). Ingen kontur eller originalpikselmaske inngår. Av 1024000 masterpiksler kvalifiserte 273951; 183589 var allerede svarte, og 90362 ble faktisk endret. Etterpå er 273951 svarte. Endring per stripe: 812 15483, 811 64585, 813 10294. Største endrede kanalverdi var 11. Alle piksler utenfor kriteriet er byte-identiske før/etter.

a-svartnormalisering-bevis.json har full telling og kriterium. a-svartnormalisering-endrede-piksler.png viser endringene i magenta kun for QA. Bildet er undersøkt: endringene ligger hovedsakelig i den svarte åpningen og smale svarte utsparinger/omriss, myntsliss og nedre åpning. Håndflater, mansjetter, lyse bånd, hovedringen, gule høylys, synlige metallflater og skala er ikke overmalt av denne regelen. Enkelte nesten svarte antialiaspiksler i omriss normaliseres også; det er ikke påstått at antialias er byte-identisk med råbildet. Ingen kildefarge under terskelen som skulle vært synlig som egen mørk tone er identifisert.

Før normaliseringen hadde 811 global 0,13/kant 0,97, men blokk 39,15 og FEIL. Etter ren fargekorreksjon, uten flytting av geometri, er blokk 0,44 og OK. Dette støtter at de nesten svarte genererte tonene utløste en ustabil blokkregistrering i dette forsøket. Checkeren er uendret.

## Klipp og kontroll

| Jobb | Klipp fra master [x,y,b,h] | Plass på lerret | Global / blokk / kant | Utfall |
| --- | --- | --- | --- | --- |
| obj812_01 | [0,0,1280,160] | [128,432] | 0,21 / 0,32 / 0,97 | OK |
| obj811_01 | [0,160,1280,352] | [128,336] | 0,13 / 0,44 / 0,97 | OK |
| obj813_01 | [0,512,1280,288] | [128,368] | 0,13 / 0,10 / 0,97 | OK |

De tre utsnittene rekonstruerer fullmasteren byte-identisk, uten overlapp eller manglende rader. Master SHA256: 3ac231229f68aaf3be7e59cbc46cd6c713de01c53ac15320368f20b97552d37d. Alle sluttfiler er RGB 1536 × 1024 med eksakt RGB128-padding. Oppskriften gjenskaper master fra rå03, normaliserer svarte toner, dokumenterer utsnitt og sammenligner byteverdier. Ingen vektortrace, originalmaskering eller lokal geometriforflytning.

## Samlet visuell QA og begrensninger

a-samlet-qa.png viser original og valgt master side om side og er undersøkt samlet. Ringens øvre avklipp, båndenes to overlapp, nedre ringender og små nedre fester finnes i riktig region. Høyre øvre skrue og to nedre skruer er synlige; venstre øvre feste er dekket av båndet som i kilden. Første forsøk gjorde dette festet til en ny tydelig skrue og er ikke valgt. Hender og mansjetter fortsetter over stripegrensene uten søm. Nedre rektangulære åpning er fortsatt avklipt ved masterkanten.

HD har glattere båndfolder, tydeligere skruer og metallhøylys. Flatene rundt spaken er mer skarpt modellerte enn originalens grove toneskift; dette er en synlig stilforskjell, ikke en ny påstått mekanisk funksjon. Den tynne røde innerkanten og små antialiasdetaljer er ikke pikselidentiske. Teknisk OK sertifiserer ikke hver høylyskontur. Ingen gjenstående stor flytting eller manglende ring/bånd/hånd er identifisert i valgt master.

a-leveranser.json har slutt-SHA og kontrollfiler. a-kildebevis.json verifiserer alle 40 beskyttede kilder uendret og sammensettingen fra stripene. Første kontrollforsøk for kandidat02 brukte ved en feil en ikke-støttet --jobb-parameter; dette ble rettet ved å kjøre samme uendrede checker på ordinær jobb/resultat.png. De bevarte kontroll02-filene er de faktiske, vellykket utførte kontrollene og viser FEIL.

Ingen motorimport, transparent nøkkelfarge, runtime, skripthendelse eller ny individuell brukergodkjenning er testet/påstått.
