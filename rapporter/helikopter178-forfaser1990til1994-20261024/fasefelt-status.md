# Fem rettingskall på fem åpne faser, fortsatt returer

H301..H305 er fem faktiske innebygde image_gen-kall for fasene 1987, 1988, 1989, 1986 og 1990 i den påbegynte fig178_02-bunken. Totalt er 129 råbilder mottatt. Råbilder, faktiske prompter, argumenter, referansehash og egne kontrollprøver er bevart. Dette er fem rettingskall på deler av én figurjobb, ikke fem leverte jobber. Ingen ny hel resultat.png, native mottak, motoravspilling, publisert modgrafikk eller Tom-/Claude-godkjenning.

H301 endrer grå malingsfelt på venstre hovedblad. Glatt egen kontur er bevart med 0/0 form/åpning, men 23 grå materialfester feiler mot H299s fem. H299/bare-vindu-egen-alfa beholdes med totalt 13 positive materialfester. En separat Python-prøve på H299 gir blått 0/0 fra egne reflekslag, men ny lavendelfeil og en synlig delt grå/hvit vindusskjøt. Den velges ikke og telles ikke som nytt bildekall.

H302 deler det sammenhengende sidebeltet i 1988, men nye polygoner, en for lys oransje kroppsflate og synlig rektangelovergang består. Global brunkalibrering alene beskytter ikke denne råvarianten mot oransje drift: brunmedian [197,103,20] gir gain [0.583756,0.572816,0.8], mens vern av egne lyseste varme toner lar store kroppsfelter forbli lyse. Ingen slik prøve skal overta H289 bare fordi alfa er bevart. H289/utsnitt-egenbbox beholdes uendret.

H303 tar opp 1989. Det nye halefeltet fjerner den runde svarte hetten og sølvinnsatsene og tegner en smal grå diagonal. Halerotoren er fortsatt for høyt plassert, og to gamle grønne deler ligger igjen under. Ny egen RGBA brukes bare i et mykt eget rektangel; form/åpning feiler 20/8. Ikke hel erstatning for H255.

H304 retter den kildebekreftede røde tippen i 1986. Begge originale rødfarger beholdes som rødt. Summen av de to rå RGB-klassenes positive/ekstra avvik går fra 2/89 i H258 til 1/57. Dette er et avgrenset delforarbeid; ett rødt kildefeste og den hele fasens form, hale, vindusfelt og sidefelt gjenstår. Grå halediagonal er ikke et landingsledd. Tre generiske sidepaneler skal ikke bli en ny fasemal.

H305 reduserer vilkårlige brune fasetter og amberstriper i 1990. Hele egen alfa og parent246s frosne transform er bevart, med 0/0 form/åpning og snitt/union 0.877887. Overgangen i eget rektangel er fortsatt lesbar; to flere grå kildefester og én færre grønn gir totalt 16 positive materialfester mot parentens 15. Dette er ingen bestått hel erstatning for H252/eget-rent-kontrollpunkt. Historisk motorbevis for H252 gjelder ikke H305.

| Kall | Fase | Direkte form/åpning | Separat materialkontroll form/åpning | Positive materialfester | RGB-klasser | RGB positiv/ekstra |
| --- | --- | --- | --- | --- | --- | --- |
| H301 | 1987 | 0/0 | 0/0 | 33 | 22 | 287/6176 |
| H302 | 1988 | 3/0 | 2/0 | 84 | 22 | 283/5643 |
| H303 | 1989 | 20/8 | 20/7 | 129 | 21 | 285/5920 |
| H304 | 1986 | 29/0 | 24/0 | 103 | 24 | 262/4666 |
| H305 | 1990 | 0/0 | 0/0 | 16 | 21 | 285/8291 |

Materialkontrollens samlede helflytt holdes atskilt fra direkte lagret native. Den senker ingen grense og endrer ingen piksel. Alle rå RGB-diagnoser, ekstra klassepiksler, 3 HD-grenser og 12 prosent-porter er bevart. Et lavere enkeltfelt-tall er ingen hel godkjenning.

Seks egne komposisjoner og alle seks native-PNG/RGBA er byteeksakt gjenskapt fra 26 egne råbilder med aktiv bildevakt. Tidligere foreldre H299, H289 og H252 gjenskapes fra sine tidligere råkjeder; H255 og H258 er egne rå direkte. Ingen originalbilder eller originalmasker åpnes under produksjonsreplay. Originalene leses bare til kontroll. Hele egne lerret, myke egne rektangler, egen alfa og frosne skalarer brukes. Se replay-fasefelt.json og rutekart-fasefelt.json. Alle fem nye råbilder, de seks egne komposisjonene og native-kontrollparene er visuelt sett. Sam er eneste godkjente stilanker; tidligere arbeidsprøver er ikke stilankre.

Fersk telling er 508/1758 hele figurjobber, 1250 uten resultat pluss returer/sluttkontroll, 3733 native, fig178_02 20/24 og familie178 32/102. Alle 9174 beskyttede filnavn, hvorav 9064 i jobber/hovedark, tre opprinnelige stasher og alle 21978 aktive modhash er uendret. Fersk hd-mod er c80099158b30fb08fa0cb670acb112bf14fd58f4. Fire eksisterende releasevedleggs ID/navn/størrelse/digest er uendret. Tidligere faktisk Linux-/Windows-innholdskontroll gjelder. Ingen ny full modkopi, tale-/Git-kopi, pakkearkivnedlasting eller sletting er laget i denne bunken.

Gjenoppta H299/1987 eller uavhengige åpne faser. H304 kan brukes som dokumentert rødt delforarbeid, ikke som godkjent heltegning. H289/1988 og H252/1990 beholdes som rene tidligere kontrollpunkt. Ikke dupliser publiserte 1995..2021 uten retur. H306 er ikke startet eller reservert. All grafikk og sluttkontroll gjenstår. Ingen nødvendig ny Tom-designavklaring; automatikken ACTIVE.

Bibliotekets figurark-fast-storrelse.md er brukt med uendrede lokale skalarporter. Søket figurark/alfa/refleks/fargefelt ga ikke en ny direkte løsning; utvidet figurark-søk fant eksisterende PASS-kort. Ingen motor-/pipelinekodeendring, bildefallback, omgåelse av grenser, force-push eller gammel nattprosess. H291s historiske verktøyavvisning er fortsatt bevart uten råfil.
