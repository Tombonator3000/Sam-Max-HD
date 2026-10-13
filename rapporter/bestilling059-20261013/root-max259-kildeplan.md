# Max259: kildegrunnlag før pakking

Begge originale ark og alle 20 kilde-/donorpar er sett. Dette er Max, med tre separate kroppslag, tre hoder, to små øyelag, fire hele gestusposer og åtte løse hånd-/armlag. Ingen ny rekvisitt finnes i disse kildene. De avskårne hendene er egne lag, ikke manglende heldekkende figurer.

Alle 20 synlige originalfelt har byteidentisk RGB og form med de valgte fig003-donorene. Alle synlige rel-opprinnelser er også identiske, delta (0,0). Atlasplasseringen er forskjellig og bestemmes av målarkenes egne bokser. Kildemetadata har rom52/palett0, 16 farger og speil=false. Skriptregisteret knytter kostyme259 til actor3 i rom052/lokal202 ved linje34/66. Det er en registerkobling, ikke bevis på gjennomlest fullscript eller spilletiming.

Planen er å kopiere dokumenterte nye RGBA-komponenter med åtte pikslers transparent sikkerhetskant, uten resampling, ny fargelegging eller originalmasker. Smålag512/513 inneholder to separate kremfargede deler hver. Hender har den mørkere beige skyggen fra de tidligere rettede003-donorene. De nye konturene er rundere og mørkere enn pikseloriginalen; dette er synlig og godtas innen den godkjente pilotstilen.

Etter pakking skal begge ark kontrolleres med uendret sjekkverktøy, samt alle egne rel-sammensettinger, håndvarianter og små øyelag. Kildelåser og valgt donorstatus er i root-max259-kildehash.json. Produksjonspakking, individuell brukergodkjenning og runtime er separate tilstander.

Måling før pakking viste at seks003-pilotutsnitt har svak randalfa på høyst2 av255 ved den åtte piksler brede sikkerhetskanten. Den er derfor nesten, men ikke fullstendig, transparent. Ingen synlig motivkontur treffer utsnittsgrensen. Eksakte RGBA-bytes innenfor det dokumenterte rektangelet bevares; dette er ikke en påstand om at vilkårlige alfapiksler utenfor rektangelet tas med.
