# Pågående pakkesamlepunkt

Native er frosset på d4b182a532ae139f4bb663cc835fabdffcc8cab6 med3641. Ikke start nye pakkebygg eller publiser ny native før denne runden og taggbygget er avsluttet. Linux-run39731808824 og Windows-run39731812958 er grønne. Linux er faktisk lastet ned,og alle21884 modfilhash er bekreftet. Avspilling i faktisk Linux-pakke kjører under out/felles-release-20261022-lee-harvey/motor-pakke.py.

Kjør bare gjenstående steg etter statusfilene. hent-status.py og hent-pakker.py gjenbruker eksisterende nedlastinger. kontroller-pakker.py kontrollerer begge. analyser-pakke.py trenger pakke-front4.json,pakke-gyldige.json,pakke-primaer.json. Se deretter de tre45-galleriene og fire hele skjermbilder før visuell.py. Commit/push egen pakkerapport før publiser-felles.py,og kjør taggkontroll.py når forventet taggbygg er registrert og grønt. sluttrapport.py oppdaterer dokumentasjon etter faktisk publisering. Ikke kall fellesrelease oppdatert før kvitteringen foreligger.
