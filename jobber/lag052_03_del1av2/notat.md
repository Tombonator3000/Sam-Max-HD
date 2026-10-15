# Ny levering av lag052_03_del1av2

Dato: 15. oktober 2026.
Verktøy: innebygd image_gen. Modellnavn ble ikke vist i verktøyresultatet.
Antall bildekall i denne økten: 4. En tidligere avvist leveranse forelå.

## Kilde og motiv

Rom 52, Savage Jungle Inn, lobbyen. Originalen og den relevante godkjente romreferansen er sett før nytegning. Jobbens referanse.png, original_1x.png, jobb.json og retur.md styrer motiv, palett, tilstand og koordinater. Ressursbanken og romnotatet identifiserer øglen, tukanen og steinhodet i lobbyen. ANALYSE.md og remake-skillen i lokal main er lest.

Objekt 486 viser øglens munnfase 03, i romrektangel [232, 152, 24, 24]. På dette lerretet er det [928, 720, 96, 96]. Godkjent stilreferanse: jobber/rom052_del1av2/resultat.png. Hode, øye og kropp fra det godkjente rommet beholdes rundt selve munnendringen.

Tukanens lukkede øye, den olivengrønne folden ved nebbet og knekket ved nebbroten er fulgt fra originalens obj489_01. To utsnittsforsøk ble gjort. Den siste tegningen brukes. Endringsalfa er hentet fra forskjellen mellom originalens tilstand og rombakgrunnen, utvidet én originalpiksel, skalert mykt og tonet over seks HD-piksler i ytterkanten. Dette unngår en skarp firkant i veggen. Det gjøres ingen ny motivtolkning av den rare formen ved nebbroten.

## Nytegning og plassering

Første kall brukte prompt.txt ordrett, returteksten og presisering av de aktuelle tilstandene. referanse.png var bilde én og det godkjente rommet bilde to. Senere utsnittskall brukte forstørret original som formfasit og godkjent rom som stilreferanse. Fullromsforsøket gjenga ikke den lille tilstanden godt nok. De supplerende promptene og rå kandidatene ligger i ../../rapporter/natt-lag052-20261015/.

Den siste munntegningen er skalert til 96 x 96 og plassert med et tillegg på 1 HD-piksel mot høyre og 3 ned inne i utsnittet. Plasseringen ble bestemt ved minste RGB-avvik mot originalen på objektets synlige piksler, innen et søkevindu på én originalpiksel. Originalens objektalfa er oppskalert med bikubisk interpolasjon. Alfaen flyttes ikke. Python gjør bare rensing, størrelse, plassering og sammensetting av nytegnet grafikk. Det er ikke tegnet nye former med kode.

Hele leveransen er 1536 x 1024. Den øverste og nederste rammen på 112 piksler er ensfarget #808080. Rombildet utenfor objektene er gjenbrukt fra det godkjente HD-rommet. Ingen beskyttede jobbfiler eller kode er endret.

## Kontroll

== lag052_03_del1av2 (lag): jobber/lag052_03_del1av2/resultat.png
OK    hele bildet (lerret): skift 0.06, blokker 0.14, kantlikhet 0.97
   Utfall: OK

Mottakets lesende check_pieces og piece_problem er også kjørt mot prosjektets eksisterende uttrekk. Ingen objekter meldes manglende eller tegnet om. Målinger:

- obj486_03: kantlikhet 0.884, mot bakgrunn 0.554.
- obj489_01: kantlikhet 0.975, mot bakgrunn 0.691.

Sammenlignet visuelt med originalen, godkjent stil og de øvrige leverte munnfasene. Ingen rød tunge er lagt til. Tekst og øvrige romelementer følger godkjent romreferanse.

Teknisk OK er ingen godkjenning fra Tom. Ingen motoravspilling, skjerm- eller lydtest er utført. Claude må kontrollere utklippingen og munnfasene etter mottak. De små overgangene mot den eksisterende HD-bakgrunnen bør sees i spillstørrelse, særlig tukanens nebbrot i lag 03.

SHA-256 resultat.png: a6d21fc7bc8fd4cc2b6bad1f958460f6da1ae89ea11f096fab2786482c81e3e7
SHA-256 stilreferanse: 5234df630c7e81bfe6c07aa00c3ba9d47c329c888fbfc234783a825dcc980669
SHA-256 referanse.png: 8bbdb8e4c2cb7b648132457a1d5440ef7b2a655bfdc7f01e582985d948fa151a
