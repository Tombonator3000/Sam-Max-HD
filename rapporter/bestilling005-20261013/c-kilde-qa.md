# Kilde-QA gruppe C

Fem jobber undersøkt i1x/4x før produksjon. Sam og Max-hovedark samt rom018-HD brukt som identitets-/stilgrunnlag. De to siste objekt187-tilstandene dekker henholdsvis venstre fremre og høyre fremre hull med rød treklubbe. Kildens skjulte hull ble ikke lagt til. Sam beholder grep, frakk, pels, mansjett og slips. Ingen rotter eller ekstra fingre.

Rom019 er varianten uten poengtavle. Samme fem tomme hull og blå draperier. Max tilhører objekt199, ikke bakgrunnsrommet. Objekt199 viser kildens klubbekontakt mot Max-hodet, lange bøyde/avskårne ører, smale øyne og pote ved kinnet. Ikke erstattet med standarduttrykket fra hovedarket. Objekt202 er tomt brett/Sams torso med fem hull, uten hender eller klubbe. Metadata og kildens faktiske avkutting styrer alle utsnitt.

Rom019, objekt187_06 og objekt199_01 får OK. Objekt187_05 og objekt202_01 har fortsatt FEIL i FFT-blokktesten, selv om globalforskyvning er0.15/0.16 og kantlikhet0.97. Dette er ikke rapportert som bestått. Uavhengig diagnose hos root pågår. I05 er avviket øvre venstre69x80blokk med blå bakgrunn/gardinkant og liten del av klubbetopp. Gjenbruk av en kildeverifisert identisk73x68blå bakgrunn fra03 rettet ikke problemet og er ikke brukt i sluttkandidaten, som er en ny generering. I202 var eksakt rom019-uttrekk kildeidentisk i1x, men ga FFT18.38/4.61 i øvre bakgrunnsblokker. Deretter to nye genereringer; første endret utsnitt og ble forkastet, andre bruker korrekt rektangel men gir blokk5.98. Ingen terskelendring, testing uten kontroll eller flytting av figur for å jage et FFT-toppunkt.

Råforsøk, promper, førversjoner og oppskrift bevart. Alle leveranselerret er1536x1024 med eksakt RGB128padding. Runtime/import/animert maskesamspill og ny brukergodkjenning er uverifisert/false. Beskyttede kilder og kode uendret.

## Oppfølging etter uavhengig diagnose

Root og agent A kontrollerte 05/202 uavhengig. Samme blokkavvik som over er reprodusert; en bakgrunns-/FFT-hypotese støttes, men algoritmefeil er ikke bevist. For05 ble et smalt nytt bilde-edit visuelt sømløst og holdt figur/brett byte-uendret, men fortsatt FEIL7.92. Et ytterligere fullforsøk var dårligere og forkastet. 05 er fortsatt uavklart og ikke klar for mottak.

202 ble laget på nytt av root fra beskyttet originalprompt med kildepresisering; sluttstatus SJEKK0.93/1.11/0.91. Kandidaten leveres med dette forbeholdet, ikke som OK. Se root202-filer og oppdatert jobbnotat. Sluttstatus i femmeren er8OK,1SJEKK,1FEIL. Ingen kontrollterskel/kodeendring.
