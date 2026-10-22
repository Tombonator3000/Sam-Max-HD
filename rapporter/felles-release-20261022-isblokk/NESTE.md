# Gjenoppta ferdig kontrollert pakkesamlepunkt3701

Nyeste beslutning:Den autoriserte fellespubliseringen bruker alle utførte jobbtester og den uavhengige fullfil-/motorkontrollen. Se CI-jobbgrunnlag.md og ci-jobber-publiseringsgrunnlag.json. Linux sin overordnede status er fortsatt uavklart og beholdes som rådata. Etter publisering beholdes nativefrys gjennom forventet Windows-taggbygg. Les eventuell publisering-journal.json før gjenopptakelse.

Tidligere ventebeslutning nedenfor er historikk.

Les bygg-startet.json og ci-sluttregistrering-venter.json først. Linux39833114209 og Windows39833120392 er allerede startet og plattformpakkene publisert, hentet og kontrollert. Ikke dispatch, kanseller eller bygg på nytt for å omgå uavklart status. Native3701 er frosset.

Begge Linux-jobber er completed/success, men overordnet run og check-suite var fortsatt in_progress uten conclusion. Windows er completed/success. Se de lagrede primærdataene. Hent ny status med hent-status.py. Ved fortsatt pending:bevar frys, resultater og arbeid. Ingen brukeravklaring er nødvendig identifisert, men sluttstatus må bli entydig før fellespublisering. Ikke krev ny Tom-godkjenning for allerede autorisert publisering.

Når begge overordnede runs er completed/success:kjør hent-pakker.py, kontroller-pakker.py og kontroller-linux-nedlasting.py. Disse verifiserer eksisterende nedlastinger mot fersk metadata og fullfilkart, uten å clobbere. Begge faktiske pakker har allerede21944 riktige modfiler. Linux-binærhash er128c9c11755ee03ec88517e9a338a34bc808a6b7a01153ecc68cc2238d5f01d9. Ikke gjenta kjor-produksjon.py eller kjor-pakke.py;fire ferske avspillinger og analyser-pakke.py er allerede fullført,alle seks ruter sett,seks par/to hele bilder/22 faser visuelt sett. Ved endrede filhash:bevar gamle filer og undersøk før nye prøver. Ingen test fra annen bunke er gjenbrukt.

Kontroller at visualplanen og linux-kontroll.json fortsatt er SHA-festet og visuelt satt. Commit/push oppdaterte rapporter på gpt-arbeid slik at grenen er ren. Publiser deretter med publiser-felles.py,men les eventuell publisering-journal.json først;aldri gjenta et ukjent utfall. Den planlagte taggen er sam-max-hd-2026-10-22-isblokk og ingen fellesrelease er opprettet per denne statusen. Hjelperen oppretter kladd,laster opp fire kontrollerte vedlegg,publiserer og henter dem igjen.

Behold nativefrys gjennom det forventede Windows-taggbygget. taggkontroll.py bekrefter fjern-SHA,hele filkartet og grønt taggbygg før frys oppheves. Kjør deretter etter-publisering.py,commit/push gpt-arbeid og bare memory.md,todo.md,STATUS.md,log.md i main. Hent og bekreft siste rapporter,alle21945 native-modfilhash,1448 beskyttede inputfiler og tre stasher. Først da er fellesutgaven oppdatert. Fortsett fra sam296-vendefaser-20261022/RETUR.md,NESTE.md og S030. Ingen grafikk til main,ingen gamle nattprosesser,ingen ny kode uten testet PR.
