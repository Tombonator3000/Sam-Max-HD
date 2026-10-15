# lag052_09_del2av2

15. oktober 2026. 1 egne bildeverktøyforsøk. Innebygd image_gen. Eksakt modellversjon er ikke eksponert.

Rom 52, Savage Jungle Inn, lobbyen. obj486_09 er én av de små ansiktsfasene på den hvilende grønne øglen. Originalens hode, snute, kjeve, øyelokk og kjølige grålilla form er fasit. Betydningen av den lille grålilla formen er ikke gitt et nytt navn. Referanse.png, original_1x.png, det originale RGBA-objektet i work/extract og nabofasene er sammenlignet. Godkjent stilreferanse: jobber/rom052_del2av2/resultat.png, vedlagt som bilde to i første forsøk. GJENNOMGANG.md og docs/gpt-romnotater.csv bekrefter rommet og øglemotivet.

Første kall bruker prompt.txt ordrett, etterfulgt av returteksten og en separat detaljpresisering. Returen gjaldt at objektets fase manglet. Alle brukte prompter og råbilder ligger i rapporter/natt-lobby052-20261015. Beskyttede kilder er uendret.

Det korte grålilla innslaget er hentet fra det nytegnede detaljforsøket for tilstand 08 og tilpasset originalens [596,740,8,8]. Den lukkede øvre øyelokksfasen er beholdt.

Felles munn og kjeve er hentet fra den nye tegningen av tilstand 0A, siden originalene har samme nedre former. Dette fjerner oppdiktede røde munnmerker fra de første forsøkene. Bare objektfeltet [544,720,96,96] er satt inn i det godkjente rommet. Python er brukt til alfa, presis plassering, tilpasning til originalmål og flat grå ramme etter Toms tillatelse. Selve nytegningen er gjort med bildeverktøyet. Originalens pikselkontur er ikke brukt som klippemaske.

Resultat: RGB PNG, 1536 x 1024. Egenkontroll: OK. Maskert objektkontroll: 0.888 mot originalobjektet, 0.676 mot bakgrunnen, ingen problemmelding. Standard python3 mangler NumPy. Sluttkontrollen er kjørt med python3 fra prosjektets eksisterende .venv via PATH. Ingen installasjon eller kodeendring.

Visuelt sammenlignet med original og godkjent rom i kontaktarket faser-ferdig.png. Øyet, de tre ulike grålilla fasene, munn, farger, plassering og overgangen til resten av hodet er kontrollert. Dette er bildekontroll, ikke avspilling i motoren. Claude må kontrollere faktisk alfaklipp og alle tilstandsbytter ved import. Ingen import, skjermtest, lydtest eller ny godkjenning fra Tom er gjort her.

SHA-256: 227b9965f2ac1525b55ffeba7b65c5595f440c7aa078a48ec925e783cf02ed37

[Samlet rapport](../../rapporter/natt-lobby052-20261015/RAPPORT.md).
