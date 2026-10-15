# Ny levering av lag052_05_del2av2

Dato: 15. oktober 2026.
Verktøy: innebygd image_gen. Modellnavn ble ikke vist i verktøyresultatet.
Antall bildekall i denne økten: 2. En tidligere avvist leveranse forelå.

## Kilde og motiv

Rom 52, Savage Jungle Inn, lobbyen. Originalen og den relevante godkjente romreferansen er sett før nytegning. Jobbens referanse.png, original_1x.png, jobb.json og retur.md styrer motiv, palett, tilstand og koordinater. Ressursbanken og romnotatet identifiserer øglen, tukanen og steinhodet i lobbyen. ANALYSE.md og remake-skillen i lokal main er lest.

Objekt 486 viser øglens munnfase 05, i romrektangel [232, 152, 24, 24]. På dette lerretet er det [544, 720, 96, 96]. Godkjent stilreferanse: jobber/rom052_del2av2/resultat.png. Hode, øye og kropp fra det godkjente rommet beholdes rundt selve munnendringen.

Bare munnfasen til objekt 486 er satt inn i det godkjente HD-rommet.

## Nytegning og plassering

Første kall brukte prompt.txt ordrett, returteksten og presisering av de aktuelle tilstandene. referanse.png var bilde én og det godkjente rommet bilde to. Senere utsnittskall brukte forstørret original som formfasit og godkjent rom som stilreferanse. Fullromsforsøket gjenga ikke den lille tilstanden godt nok. De supplerende promptene og rå kandidatene ligger i ../../rapporter/natt-lag052-20261015/.

Den siste munntegningen er skalert til 96 x 96 og plassert med et tillegg på 1 HD-piksel mot høyre og 4 ned inne i utsnittet. Plasseringen ble bestemt ved minste RGB-avvik mot originalen på objektets synlige piksler, innen et søkevindu på én originalpiksel. Originalens objektalfa er oppskalert med bikubisk interpolasjon. Alfaen flyttes ikke. Python gjør bare rensing, størrelse, plassering og sammensetting av nytegnet grafikk. Det er ikke tegnet nye former med kode.

Hele leveransen er 1536 x 1024. Den øverste og nederste rammen på 112 piksler er ensfarget #808080. Rombildet utenfor objektene er gjenbrukt fra det godkjente HD-rommet. Ingen beskyttede jobbfiler eller kode er endret.

## Kontroll

== lag052_05_del2av2 (lag): jobber/lag052_05_del2av2/resultat.png
OK    hele bildet (lerret): skift 0.05, blokker 0.41, kantlikhet 0.96
   Utfall: OK

Mottakets lesende check_pieces og piece_problem er også kjørt mot prosjektets eksisterende uttrekk. Ingen objekter meldes manglende eller tegnet om. Målinger:

- obj486_05: kantlikhet 0.883, mot bakgrunn 0.506.

Sammenlignet visuelt med originalen, godkjent stil og de øvrige leverte munnfasene. Ingen rød tunge er lagt til. Tekst og øvrige romelementer følger godkjent romreferanse.

Teknisk OK er ingen godkjenning fra Tom. Ingen motoravspilling, skjerm- eller lydtest er utført. Claude må kontrollere utklippingen og munnfasene etter mottak. De små overgangene mot den eksisterende HD-bakgrunnen bør sees i spillstørrelse, særlig tukanens nebbrot i lag 03.

SHA-256 resultat.png: 58de1bde05da77560334a6e1381b780b60f70251b9ca8333164e40c487cc1b75
SHA-256 stilreferanse: 72fc7d6f5fc17c760c573d6648b97d8a12adae758d18a336e072a570a4315fb8
SHA-256 referanse.png: 196aa09b03a93db76b80e134ec353eb8ff2bc6bdceabb6854b4e1b6780b2aea1
