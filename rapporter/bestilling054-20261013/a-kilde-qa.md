# A: fire Max-ark ferdige

Fig005_01, fig005_02, fig005_03 og fig235_01 er levert som ekte RGBA. Alle fire får OK fra uendret sjekk_leveranse.py. [a-leveranser.json](a-leveranser.json) har faktiske slutt-SHA og kontrollfiler. Alle16 beskyttede kilder er uendret. Donorer er mottatt i53-commit1f1eb68ec6813f90ebda64917a38315f370f1df1 og kontrollert mot B-manifestet før bruk.

67 ruter gjenbruker kildebeviste nye donor-cels. Fig005_01 beholder hele pilotkomposisjonen byteidentisk som raster; fig005_02 har samme PNG-SHA som mottatt00302. Fig005_03 tar bare de åtte aktuelle bakre gåposene fra00303, og tilfører den ene egne nye cel000. Fig235_01 tar bare åtte grunnlag fra piloten. Ingen av de to SJEKK-rutene551/552, eller neserettet179, inngår i disse fire arkene. Deres donorstatus er ikke endret.

[a-celkart.json](a-celkart.json) dokumenterer de68 valgte rutene med donorhash, utsnittshash, alfa-boks og egne festemetadata. Nye deler er klippet med12 HD-pikslers transparent margin rundt synlig-boksen, uten skalering eller originalmaskering. Åtte pikslers margin var for liten for enkelte gamle pilotantialfakanter;12 rommer dem. Metadatarektangler kan ha større tomt område enn synlig, så sluttkart og nærbilder bruker synlig. Rekt-klipping i første diagnostiske nærbilde fanget toppen av naboruter; det er korrigert i gjeldende QA, ikke slettet fra et produktbilde. Endringen påvirket ingen slutt-SHA.

## Ny cel000

To innebygde imagegen-kall: en ny hel Max-pose og en lokal kinnretting. Rot bekreftet identiteten og ba om fjerning av den nye hvite kinnflekken. Bare rektangelet[245,898,320,960] fra andre NYE råbilde ble brukt i første. Resten av råbildet er byte-uendret. Helkomponentskalering til124×212 ga kun124 endrede HD-piksler i[105,411,121,423] mot før-kinn-kandidaten. Ører, hender, føtter, liten munn og én rosa nese er beholdt. Ingen rekvisitt er lagt til. Se [kinnbevis](a-cel000-kinnbevis.json), [kandidat mot kilde](a-cel000-kandidatqa.png), ordrett prompt og egen kildepresisering. Eksakt bildemodell er ikke eksponert.

## Visuell kontroll og små lag

Alle fire helscener og seks feltark er sett. Den tegnede serien beholder egne bak-/front-/sideposeringer, potefarger, rosa neser og munnvarianter. Donorens noe rundere modellering og antialiasing er arvet, ikke nytegnet på nytt. Cel000 følger egen kildepose og har en roligere liten munn, ikke det brede standardgliset.

Øyelokk512/513 i00501 og23501 er sett særskilt som to separate lyse komponenter per rute, uten utfylling mellom dem. Uendret checker hopper over svært små kilder; [a-oyelokk-slutt.json](a-oyelokk-slutt.json) oppgir nye alfaarealer. Byteidentitet med hver egen pilotcel er bevist. [Rel-komposisjon](a-rel-levert-komposisjon.png) viser kropp/hode/øyelokk på egne originalfester, samt cel000. Statiske skjøter og lukkede øyelokk er kontrollert, ikke motoravspilling.

[Helbilde](a-helscene-qa.png), feltark[1](a-levert-feltqa-1.png), [2](a-levert-feltqa-2.png), [3](a-levert-feltqa-3.png), [4](a-levert-feltqa-4.png), [5](a-levert-feltqa-5.png), [6](a-levert-feltqa-6.png). Grå QA-flate er bare visningsbakgrunn; PNG-leveransene er transparente.

Oppskrifter: [gjenbruk](a-gjenbruk-lever.py.txt), [rel](a-rel-slutt.py.txt), [ny komponent](a-cel000-plasser.py.txt), [lokal retting](a-cel000-kinnretting.py.txt). Raw01/raw02 og valgt sammensatt råbilde er bevart. Ingen donor/kilde/Git/globalfil eller produktkode er endret. Runtime og ny individuell brukergodkjenning er false.
