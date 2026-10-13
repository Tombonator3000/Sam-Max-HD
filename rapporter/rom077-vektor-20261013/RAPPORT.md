# Rom077 med presis vektorrekonstruksjon

Tom valgte uttrykkelig metoden for dette rommet etter fem avviste imagegenforsøk. Begge deler er nå levert med **OK**: del1 0.00/0.00/1.00, del2 0.05/0.99/1.00. NativeSVG og PNG har én felles2560×800master, klipp x0/x1024 og512×800byte-identisk overlapp. Alle åtte beskyttede kilder er uendret. Tidligere bestilling17-kandidat/status er historikk og erstattes av denne leveransen.

Source har seks flate farger. Alle24fargeregionløkker beholdes, med34delte grensekjeder. Ingen bitmap/gradient er innebygd iSVG. Fem midtkomponenter inklusive apex og **fire**asymmetriske sideprikker er bevart. Tidligere omtale av tre sideprikker var en tellefeil; uavhengig pikselkontroll avklarte fire. Ingen ny strek, bil eller tekst er lagt til.

Ordinær grenseutjevning har toleranse0.8kildepx. To veisidekjeder er utjevnet med1.6, målt faktisk største avvik1.5269. Endepunkter og kildeknutepunkter står fast. Dette glatter rastertrappen og bevarer den store kileformen, med dokumentert konturavvik. Enkelte små opprinnelige knekk/steg består rundt de tette apex-/horisontforbindelsene. Uavhengig kontroll fant ingen strenge segmentkryssinger; det er ikke et fullstendig matematisk topologibevis.

PNG fra første PILrasterisering fikk én svak ekstra rød rad utenfor nativeSVG. En scanlinerasteriserer ved16samples/kildepx, samplesentre og halvåpne intervaller følger native even-odd-fyll og løste dette. Endelig motivbbox[1280,268,2560,532] er eksakt. SVGgeometrien var uendret. Førversjoner er bevart. Dette er en konkret rasterretting, ingen originalmaskering, originaloppskalering eller endring av checkerterskler.

Kildevalg, metodevalg, vektoroppskrift, geometri, kildehash, førversjoner, begge egenkontroller og uavhengig Astra-QA er bevart. Grafikkleveranse er verifisert, men ingen ny individuell bildegodkjenning, import, nøkkelfarge/masker eller faktisk romvisning/runtime er utført.
