# Numerisk diagnose av blokk-FFT

2026-10-13. Avgrenset read-only undersøkelse for kodeeiers mottak. Ingen produksjonsbilder, terskler eller pipelinefiler endret. Varianter eksisterer kun i minnet.

## Dokumentert resultat

**Ja: uendret compare/judge gir FEIL på originaler som kun har fått et symmetrisk GaussianBlur(radius=2) på samme pikselrutenett.** Ingen translasjon, skalering av motiv, rotasjon eller warp inngår. Filtrering endrer likevel kantprofiler og kan viske ut små detaljer; dette er ikke en påstand om at den filtrerte varianten er akseptabel HD-grafikk eller at alle geometriske nivåkurver forblir identiske.

Identisk original ×4 med nearest-neighbor gir begge steder OK, skift=0, blokk=0, kantlikhet=1. BOX-returen i compare er eksplisitt bytekontrollert lik varianten før 4×-replikasjon. Mild Gaussian 0.5/1.0, median 3/5, gamma 0.8/1.2 og fargekvantisering til trinn32 gir alle OK. Dermed viser denne avgrensede testen ikke FEIL fra rene punktvise fargeendringer eller de milde ditherfiltrene.

| Kilde/variant | Utfall | Global skift | Maks blokk | Kantlikhet |
|---|---|---:|---:|---:|
| obj187_05 / identisk | OK | 0 | 0 | 1 |
| obj187_05 / Gaussian 2 | FEIL | 0.08 | 16.02 | 0.934 |
| obj307_01 / identisk | OK | 0 | 0 | 1 |
| obj307_01 / Gaussian 2 | FEIL | 1.24 | 7.03 | 0.923 |
| obj187_05 / aktuell produksjon, kun lest | FEIL | 0.15 | 7.92 | 0.973 |
| obj307_01 / aktuell produksjon, kun lest | FEIL | 0.13 | 19.94 | 0.941 |

## Blokk og toppstyrke

Alle koordinater er originalpiksler, x,y,b,h. Varians/std gjelder kantbildet etter kontrollens egen luminans/blur/gradient, ikke RGB-varians.

- **187 Gaussian2:** blokk [0,0,69,80], estimert dx=-16.020/dy=0.031. Kantvarians original/variant 3.8186/1.9503, std 1.9541/1.3965, blokk-korrelasjon 0.9278. Valgt FFT-topp 0.1610, neste adskilte topp 0.1409, ratio 1.1427, PSR 12.36. Samme blokk som produksjonsfeilen: blå bakgrunn/gardinkant og liten klubbedel. Produksjonens ratio 1.1060, PSR 9.35.
- **307 Gaussian2:** blokk [212,0,106,40], dx=-6.387/dy=-2.936. Varians 26.1535/11.8826, std 5.1141/3.4471, blokk-korrelasjon 0.9240. Topp 0.1987, neste 0.1743, ratio 1.1403, PSR 14.79. Dette er høyre blokk, **ikke** samme blokk som produksjonsfeilen.
- **307 aktuell produksjon:** midtblokk [106,0,106,40], dx=14.005/dy=14.198. Varians 31.4570/32.0126, std 5.6086/5.6580; blokk-korrelasjon hele 0.9850. Topp 0.06163 og neste 0.06129: ratio 1.00562, PSR 4.04. Nesten like sterke adskilte topper; den valgte toppen ligger langt fra null selv om de utransformerte kantbildene korrelerer høyt.

Confidence-tallene er **kun diagnostikk**, ikke nye godkjenningskriterier eller kalibrerte sannsynligheter. PSR=(topp−middel sidefelt)/std sidefelt; sidefelt ekskluderer et periodisk 7×7-felt rundt maksimum. Topp-ratio bruker maksimum utenfor dette feltet. Hele definisjonen finnes i oppskriften. Identiske kontrollers enorme PSR/ratio skyldes tilnærmet null sidefelt, og skal ikke leses som en meningsfull prosent.

## Årsak som faktisk er vist, og hva som er hypotese

Kontrollens dokumenterte mekanisme er fasekorrelasjon av kantbilder med Hann-vindu, frekvensvis normalisering og ubetinget valg av høyeste topp, deretter maksimum av blokkenes avstander. Blokker utelates bare hvis kant-std <0.001. Ingen av de problematiske blokkene er i nærheten av denne grensen. compare/judge bruker verken topp-ratio, PSR eller blokk-korrelasjon som confidence-sjekk.

Derfor kan en konkurrerende fasekorrelasjonstopp bli rapportert som stor geometrisk forskyvning etter filtrering alene. For 307-produksjon er lav toppseparasjon direkte målt; problemet kan ikke forklares bare som «for lav varians», siden midtblokkens std er høyere enn sideblokkenes. Repetitive/lite særpregede kantprofiler og endret skygge/dither som gir frekvensmessig tvetydighet er en plausibel forklaring, ikke isolert bevist årsak for akkurat de genererte bildene. Testen fritar ikke art fra visuell geometri- eller semantikkontroll, og gir ingen hjemmel til å omgå eksisterende mottak.

## Reproduksjon og proveniens

Kjør fra .gpt-gren:

```bash
/home/tombonator3000t/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 rapporter/kontroll-fft-20261013/diagnose.py.txt
```

Oppskriften importerer compare, judge og phase_shift fra uendret verktoy/sjekk_leveranse.py; confidence-beregningen observerer samme FFT-formel uten å erstatte den. Den forhåndsdefinerte serien er endelig og inneholder ingen parameterjakt mot produksjonsbildene. Skriver bare diagnose.json i denne rapportmappen. JSON inneholder alle blokker og varianter, kilde-/produksjons-SHA256, kontrollkode-SHA256 og miljøversjoner.

Kontrollkode SHA256: 3cc10afe9cbdaffab4976ddbf9e53d70148d9f412beb3bb609f44db86b0c2ed6.

Lest bakgrunn: bestilling005/c-blokkdiagnose.json, root-blokkdiagnose.json og c-kilde-qa.md; bestilling008/a-top-blokkdiagnose.json, a-top-blokkdiagnose02.json og a-kilde-qa.md. Aktuell 187-kandidat har 7.92 (senere enn den historiske 7.86); aktuell 307 har 19.94, samme som andre A-forsøk. Ingen tidligere kontrollstatus er omskrevet.
