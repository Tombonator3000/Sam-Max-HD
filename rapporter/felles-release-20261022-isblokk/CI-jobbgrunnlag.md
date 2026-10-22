# Publiseringsgrunnlag fra utførte tester

Begge faktiske Linux-jobber er completed/success,inkludert oppstartstest,Debian-test,pakkeopplasting og avsluttende jobbsteg. Windows-kjøringen er completed/success. Begge faktiske pakker,fire vedleggsdigester,alle21944 runtime-modfiler og seks relevante native motorbilder er uavhengig kontrollert. Hele nativegrunnlaget er SHA-festet og uendret. Det er tilstrekkelig grunnlag for den allerede autoriserte fellespubliseringen.

Den overordnede Linux-run/check-suite er fortsatt in_progress uten conclusion. Dette beholdes som rådata og opplyses i release og rapport;årsaken hevdes ikke kjent. Ingen GitHub-status endres,ingen jobb avbrytes eller dispatches på nytt,ingen grafikkport senkes,og ingen kode eller godkjenningsregel i repoets arbeidsflyter endres. Den første lokale hjelpevaktens krav om oppdatert oppsummeringsstatus var et oppsettvalg,ikke et nytt krav fra Tom. Publiseringen bygger nå på de faktisk utførte testene og direkte pakkekontrollen.

ci_jobber.py kontrollerer bare denne ene kjøringen39833114209,attempt1,på nøyaktig12cfa381c23ca584086814fd8495c5c91bebea7c. Den krever akkurat de to forventede,terminalt vellykkede jobbene og de tre navngitte pakke/teststegene. Alle andre kjøringer og eventuelle nye attempts må vurderes vanlig. Nativefrys beholdes til det forventede Windows-taggbygget er grønt og alle faktiske pakkearbeidere er avsluttet. Ingen overordnet Linux-conclusion forfalskes.

## Sluttregistrering

Ved sluttrevisjonen 2026-10-22 kl. 19:43 UTC var også den overordnede Linux-kjøringen completed/success. GitHub oppgir updated_at 19:34:20 UTC. Se linux-jobber-sluttrevisjon.json. Avviket ovenfor beskriver tilstanden ved publisering og er nå løst. Windows-main, Windows-taggbygg og main-testene er bestått. Alle pakker er ferdige og nativefrys er opphevet. Ingen CI-status er endret av oss.
