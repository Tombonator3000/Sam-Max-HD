# Fire grafikkjobber i natt, 16. oktober 2026

Levert: 4 jobber. Statisk visuelt kontrollert: 4 jobber. Importert i denne økten: 0. Motoravspilt: 0. Ny godkjenning fra Tom: 0.

| Jobb | Innhold | Nye bildeforsøk | Egenkontroll |
| --- | --- | --- | --- |
| fig259_02 | 3 beige Max-håndlag, retur | 1 | OK, 3 av 3 ruter |
| lag026_02 | obj275_02, fall ved glassburet | 1 | OK |
| lag026_03 | obj275_03, neste falltilstand | 1 | OK |
| lag032_01_del1av2 | obj313_01, obj316_01, obj317_01 | 3 | OK |

Originaler og godkjente hovedark eller rombilder er sett før hvert bildeverktøykall. ORDRE.md, BESTILLING.md, AGENTS.md, ANALYSE.md, GJENNOMGANG.md, nattoverleveringen og remake-skillen i den lokale main-arbeidsmappen er lest. CLAUDE.md finnes ikke i denne arbeidsmappen. OPPDRAG-GPT.md ble ikke funnet på prosjektroten; Toms uttrykkelige nattordre i chatten styrer denne runden.

Den vesentlige visuelle rettelsen var taubanedøren i obj313_01. Første kandidat bestod målingene, men viste feil tilstand. Den leveres ikke urettet. Den endelige objektlappen er nytegnet fra et forstørret originalutsnitt og plassert presist med Python. Jobbnotatet beskriver hvert forsøk. Håndarket er også nytegnet med bildeverktøyet, deretter renset og plassert i de tre opprinnelige rutene med ekte alfa.

Sjekksummer og importstatus står i fremdrift.json. Rutekartet for Max har x,y,bredde,høyde for faktisk alfa over 128. Egenkontrollfilene inneholder full utskrift fra det uendrede kontrollskriptet, kjørt med Python 3 fra prosjektets eksisterende .venv. Ingen installasjon er gjort. Visuell objektkontroll er oppdatert til siste leveranse.

Git pull ble forsøkt før arbeidet, men blokkert av skrivebeskyttet FETCH_HEAD utenfor sandkassen. Grenen er gpt-arbeid. Ingen grenbytte, commit, push, PR, fletting eller historieendring er utført. Nattløpet må ta hånd om commit og innhenting. Beskyttede jobbfiler er urørt.

Claude må kontrollere import og sammensetting, særlig de separate Max-håndlagene, tilstandene 02 og 03 i rom 26 og taubaneobjektet i rom 32. Full animasjon med alle figurdelene samlet, overgang til rom32 del 2 og faktisk motorvisning er ikke verifisert. PR32 og Sam091 er ikke kontrollert på nytt eller endret.

## Eksisterende metadataavvik

Jobbmetadataenes lagrede prompt-sjekksum stemmer ikke med dagens prompt.txt i jobber/fig259_02/prompt.txt, jobber/lag026_02/prompt.txt, jobber/lag026_03/prompt.txt, jobber/lag032_01_del1av2/prompt.txt. Alle fire beskyttede filer per jobb er like HEAD, kontrollert byte for byte. Avviket fantes derfor i det tilgjengelige grunnlaget og er ikke rettet her. Dagens prompt.txt er brukt ordrett. Se kildekontroll.json for de faktiske sjekksummene.
