# Produksjons-QA, Bestilling 19 C

Kildeanalyse og primærkildeavklaring ligger i c-kildeplan.md. Originalene er sett individuelt og samlet. Alle fire tomme håndtilstander er selvstendige; ingen magnet/ring er lagt til. Fem fingre og negler, brun rynket hud, grønne ledd, gule punkter og svarte mellomrom er sammenlignet.

## obj828_01
Source-only omtegning 2 retter feil størrelse/posisjon i forsøk 1. Diagonalt avklipt håndledd, ett separat grønt segment og fem fingre/negler er bevart.

## obj829_01
Forsøk 1 med hele genererte feltet [256,204,1024,612] helskalert til [256,208,1024,608]. To grønne segmenter og åpen hånd er bevart.

## obj830_01
Forsøk 1 med lokal imagegen-korreksjon av nedre gule pivot fra forsøk 2. Kilden viser delvis skjult punkt, ikke en hel rund knapp. Endelig kompositt bare [616,378,44,44], 4 px rektangulær kantblanding. Resten byte-identisk med før-korreksjonskandidat.

## obj831_01
Selvstendig tegning fra 831-originalen, ikke gjenbruk av 830. Egen leddvinkel/fingerspredning og fullt synlig nedre gult punkt. SJEKK står uendret: mindre konturer/plassering er ikke helt kildelike.

828 første forsøk fikk FEIL 2.16 / 4.02 / 0.66 og er bevart, ikke valgt. 830 lokal korreksjon ble først prøvd over 120 × 96; dette ga synlig leverkantforskjell, så endelig endringsfelt ble snevret inn til 44 × 44 rundt det nytegnede punktet. Ingen originalsilhuettmaske brukes. Resten er kontrollert byte-identisk.

B har kontrollert første C-familie read-only og bekreftet håndidentiteten; jeg har kontrollert B-821/822 og meldte tilsvarende pivotforskjell i 822. Begge familier har sterkere negle-/metallhøylys enn kilde, et dokumentert stilsærtrekk. C slår ikke 830/831 sammen. c-samlet-qa.png er oppdatert og sett etter korrigeringene; 830 er også sett separat.

Tre resultater er OK. 831 er SJEKK med lokalt avvik 1.22 originalpiksler, ikke friskmeldt av god motividentitet. Ingen flytting/warp for å jage FFT. Alle lerret/padding er målt; alle 40 beskyttede kilder er SHA-uendret. Råforsøk, fullprompter, utsnitt, kontrollutdata og oppskrift er bevart. Runtime, faktisk animasjonsrekkefølge, import og ny individuell brukergodkjenning er ikke utført.
