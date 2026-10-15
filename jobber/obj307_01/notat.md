# Siste returretting 15. oktober 2026

To nye bildeforsøk. Første forsøk rettet ikke skjøten tilstrekkelig. Andre forsøk fikk originalens topp og den godkjente obj304_01 vist sammen. Bare den nytegnede toppstripen ble tatt ut. Motivet er øvre grålilla innfatning på myntkikkerten i rom 31, tilstand 01, med to skruer, fasetter og avskåret svart åpning. Myntsliss og landskap fra den generelle romprompten hører ikke til denne stripen. Presiseringen står separat i rapportens promptfiler.

Stil og skjøtgrunnlag: jobber/obj304_01/resultat.png. Stilankeret stil/rom007_del1av2.png er også sett. Nedre objekt er bevart helt uendret. Etter nytegningen er små RGB-sprang renset over de siste åtte HD-radene, bare der originalen viser samme flate på begge sider. Ingen ny motivtegning i Python. Se rens_skjot.py og obj307-skjot-ferdig.png i rapporten. Skjøten er sett samlet uten motoren. Ingen ny spilltest eller godkjenning fra Tom.

Innebygd image_gen. Eksakt modellnavn vises ikke. Dato 15. oktober 2026. Originalen i 1x og 4x og relevante godkjente HD-referanser er sett før nytegning. AGENTS.md, ORDRE.md, BESTILLING.md, ANALYSE.md, GJENNOMGANG.md, NATT-HANDOFF.md og remake-skillen fra lokal main er lest. Python brukes bare til rensing, plassering, skalering og kontroll av nytegnet grafikk etter Toms tillatelse.

Leveransen er 1536 x 1024 RGB med eksakt grå ramme RGB 128,128,128. Beskyttede jobbfiler er bytekontrollert uendret mot HEAD. Ingen kodeendring, commit eller push i økten. Git pull ble forsøkt, men Git-metadata ligger utenfor sandkassens skrivbare område. Rapporten skiller lokal kontroll fra motorimport og Toms godkjenning.

Egenkontroll: OK. Skift 0.37, blokker 0.36 originalpiksler, kantlikhet 0.956.

Resultat SHA-256: 6c19372fc43fd626eeb3c912409445bdf68b44bfe05dd2e7d80e4c1720de8306.

[Råforsøk, prompter, sammenligninger og kontrollrapport](../../rapporter/nattrunde-fire-20261015/RAPPORT.md).

## Tidligere notat, bevart som historikk

# obj307_01

To nye forsøk. Forsøk 2 er levert. Stilanker: stil/rom007_del1av2.png. Motivet er bare øverste 320 x 40 originalpiksler av myntkikkertens grålilla innfatning i rom 31, objekt 307, tilstand 01. To mørke skruer, asymmetrisk fasett, blå himmel på sidene og avskåret svart åpning beholdes.

Romnotatets myntsliss, 25-centtekst og landskap beskriver hele rommet og inngår ikke i toppstripen. Presiseringen ligger i separate promptfiler. Første nye forsøk glattet bort skillet mellom de to øvre fasettene og fikk FEIL. Andre forsøk bevarer skillet og består. Motivet er klippet rektangulært ved [128,432,1280,160] uten skalering. Ingen originalmaske.

Egenkontroll: OK. Globalt skift 0,16, største blokkskift 0,13 originalpiksler, kantlikhet 0,960. Overgangen mot nabopanelet er ikke testet i motoren.

SHA-256: a25fe3d6d28ca26e70be36f87821de19f57b50e38f9e0d0a70b25083c38aa87b.

Innebygd image_gen, eksakt modellnavn ikke eksponert. Dato: 15. oktober 2026. Originalen i 1x og 4x og relevant godkjent stilbilde er sett før tegning. Prompt.txt er brukt ordrett med returteksten og separat kildepresisering. Beskyttede kilder er SHA-256-kontrollert uendret mot HEAD.

Python er brukt etter Toms tillatelse til presis plassering, egen alfa og grå ramme. 1536 x 1024 RGB, eksakt RGB128-ramme. Original, tidligere levering, ny levering og overlegg er visuelt sammenlignet. Ingen ny motorimport, full animasjonsavspilling eller godkjenning fra Tom.

Råforsøk, prompter, forrige levering, oppskrift, kontroll, sjekksummer og sammenligningsbilder: [nattrapport](../../rapporter/natt-fire-returer-20261015/RAPPORT.md).
