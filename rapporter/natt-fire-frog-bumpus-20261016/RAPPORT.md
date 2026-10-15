# Fire lagjobber ved Frog Rock og Bumpusville

Dato: 16. oktober 2026. Levert: 4 ark med 7 objektbilder. Visuelt kontrollert av Codex: 4 ark og 7 objektutsnitt. Importert i denne økten: 0. Motoravspilling: ikke utført. Toms godkjenning: ikke innhentet. Alle fire leveranser har OK i egenkontrollen.

Arbeidet følger de fire første jobbene i ORDRE.md datert 16. oktober klokken 01:25. Ingen av dem hadde retur.md. Det er ikke gjentatt kontroll av PR32 eller tegnet om Sam091. Ingen kode er endret.

| Jobb | Forsøk | Skift | Blokkavvik | Kantlikhet | Utfall |
| --- | --- | --- | --- | --- | --- |
| lag041_01_del2av2 | 2 | 0.08 | 0.33 | 0.913 | OK |
| lag041_02_del2av2 | 2 | 0.21 | 0.22 | 0.915 | OK |
| lag043_01_del1av2 | 1 | 0.07 | 0.43 | 0.961 | OK |
| lag045_01 | 1 | 0.08 | 0.18 | 0.973 | OK |

## Grunnlag og visuell kontroll

[Objektgrunnlaget](objektgrunnlag.png) viser uttrekkene. [Sammenligningsarket](objektkontroll.png) viser original, ferdig leveranse og godkjent HD-rom ved jobbens eksakte objektposisjoner. [Leveransemanifestet](leveranser.json) fører filstier, SHA256, bilde to, prompt og målinger. [Kildehashene](kildehash.json) dekker alle 16 beskyttede jobbfiler, som også er sammenlignet byte for byte med HEAD.

Spillets eksisterende engelske CD-uttrekk er brukt. Rom 41, 43 og 45 har én palett hver i work/extract/rooms.json. Kildetro motiv og design er vurdert etter remake-skillen i origin/main (5f6bebaa5b9694507b5008198e8736bbaa4779ad), lest med git show. Ressursbanken og ANALYSE.md er lest sammen med originalene og jobbmetadataene. NATT-HANDOFF.md, forrige nattsrapport og prosjektbibliotekets OPPDRAG-GPT.md er lest for overleveringsstatus. CLAUDE.md finnes ikke her.

Frog Rock: Første bildeforsøk på begge tilstander fikk teknisk OK, men brunt materiale ble for vått og sprutaktig. Disse er forkastet visuelt. Andre forsøk følger ressursbankens hår/pulver og originalens tråder og to gule felt. Korrigeringspromptene er bevart i denne mappen. Forsøk 2 er de eneste leverte Frog Rock-bildene. Første forsøk ligger som brutto-filer for sporbarhet og skal ikke importeres.

Gang: obj392_01 er metallgrillen på Conroy-statuen, ikke den blå pluggen i den generelle rombeskrivelsen. Soverom: tom tilstand uten høyre pute, hår-/tupémotiv i nisjen, blå bok og trapp er fulgt fra originalene. Godkjent rom er stilgrunnlag, men styrer ikke en annen objekttilstand over originalen. Detaljer i tråder, pulver, gitter og bokmerker er HD-tolkninger av små pikselformer.

Alle første forsøk brukte prompt.txt ordrett og originalen som bilde én, godkjent rom som bilde to. Frog Rock-forsøk 2 brukte også bilde tre som beskrevet i jobbnotatene. Verktøy: innebygd image_gen. Eksakt modellnavn er ikke eksponert. Pillow brukes bare til flat grå ramme og dokumenterende sammenligningsark. Ingen skalering, flytting eller geometriwarp er brukt i leveransene.

## Overlevering

Utgangspunkt: bf788171436924ef22131e63fb32fd227c8f43f3, gren gpt-arbeid. Git pull ble forsøkt, men Git kunne ikke skrive FETCH_HEAD i /home/tom/Sam-Max-HD/.git/worktrees/-gpt-gren, som er skrivebeskyttet i sandkassen. Ingen commit, push, grenbytte, PR, fletting eller historikkendring er utført. Nattløpets skript må ta med resultat.png, notat.md og denne rapportmappen.

Kontrollene er kjørt med prosjektets eksisterende Python-miljø uten installasjon:

```sh
PATH=/home/tom/Sam-Max-HD/.venv/bin:$PATH python3 verktoy/sjekk_leveranse.py jobber/<jobb>/resultat.png
```

Claude må kontrollere og importere de sju objektbildene og vurdere klippekanter mot faktisk HD-rom, særlig de to Frog Rock-tilstandene og putens tomme tilstand. Filkontroll og automatisk OK dokumenterer ikke motoravspilling eller Toms godkjenning. Ingen ny konkret kodeblokkering er påvist.
