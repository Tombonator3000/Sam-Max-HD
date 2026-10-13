# Gruppe B: Rom 084

Alle tre deler er levert fra én nytegnet master på 3840 x 800. Delene starter ved x = 0, 1152 og 2304. Begge overlapper på 384 x 800 er byte-identiske. Canvas er 1536 x 1024, motivet står ved (0,112), og padding er nøytral RGB(128,128,128). Alle 40 låste kilder er kontrollert uendret.

## Kilde og motiv

Originaldelene danner tre separate, skjeve fargekort med hvite rammer på mørk blå bakgrunn. Det er tre forekomster av «Wax Me». Den generiske beskrivelsen av en fargestiftboks og «MAX'S WAX» gjelder ikke denne kilden og er uttrykkelig korrigert i tillegg til de ordrette jobbpromptene.

Venstre kort beholder Sam i gråblå dress og hatt med kamera mellom hendene, Max ved den store grønne krokodillens åpne munn, rosa munninteriør, busker og den gule/lilla vindmøllen. Max sin kontakt med munnen er beholdt. Midtkortet viser Sam og Max i bil under vann, rosa blekksprut med to gule øyne, den store grønne fisken, den store lilla fisken, tre små grønne fisker og én brun fisk. Bilen har ikke blitt ubåt, og figurene har ikke fått hjelmer. Høyre kort beholder Max med buet sabel og gult feste, Sam med gul turban, grønn juvel og oransje instrument, stor brun/oransje kobra med grønt sprut mot nesen og to grønne slangehoder bak Max. Kurv, slynger og avkuttinger følger kilden.

## Forsøk og kontroll

To felles genereringsforsøk er bevart. Første forsøk ga SJEKK på del 1 og FEIL på del 2 og 3. Andre forsøk brukte originalen som motivgrunnlag på nytt. Ingen feilgenerert grafikk ble brukt som identitetsanker. Innebygd ChatGPT imagegen ble brukt; eksakt bildemodell er ikke eksponert.

Den andre rågenereringens samlede motivfelt ble beskåret ved (0,136,2164,589) og helskalert til 3840 x 800 med LANCZOS. Ingen lokal geometriwarp, originalsilhuettmasker, originalpikselinnliming eller separat generering av delene er brukt.

Uendret sjekk_leveranse.py gir OK for alle tre: del 1 har skift 0,28 / blokk 0,32 / kantlikhet 0,94; del 2 har 0,27 / 0,26 / 0,95; del 3 har 0,14 / 0,29 / 0,95. Sluttføringsoppskriften bekrefter også eksakt masterklipp, padding, overlapp og ordrette originalprompter i begge sendte prompter.

## Visuelle forbehold

Hovedidentitet, kostymer, sceneinnhold, kortrekkefølge og alle tre tekster er bevart. Nytegningen har glattere og mer volumskapende skygger. Max sin øyespalte og tanngard på venstrekortet er mer regelmessig tegnet, og små tenner, bobler og skyggekonturer er ikke dokumentert punkt for punkt som identiske. Dette er konkrete detaljforbehold, selv om geometrikontrollen er OK. Det er ikke funnet sikre manglende hovedaktører, ekstra skilt eller nye rekvisitter ved samlet visuell kontroll.

Se b-familie.png, b-rom084-krokodille-detalj.png, b-leveranser.json og b-proveniens.json. Råforsøk, sendte prompter og oppskrifter er bevart. Klar for roots mottak med oppgitte forbehold; runtime er ikke prøvd og ingen ny individuell brukergodkjenning er gitt.
