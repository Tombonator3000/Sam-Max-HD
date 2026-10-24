# Kompakt spillerpakke og ryddet arbeidslagring

Spillerpakken er 392 MB Linux eller 545 MB Windows, med spillet, tale, motor og dagens HD-mod. Windows-innholdet er 659 MB utpakket. Modden er 369 MB. Arbeidsmappens omtrent 90 GB var utviklingsdata, ikke spillerens nedlasting. Dagens pakker og alle 21978 modfiler er SHA-kontrollert uendret. Ingen oppløsning, RGBA eller alfa er endret. Hele HD-produksjonen er fortsatt uferdig.

PR 37 er flettet i main 2e5f0ebd0c56556248798d4a7a675fd0b69cca36 etter grønne tester: 79 pipeline-tester, 10 nye pakkestørrelseskontroller og et faktisk Windows-bygg med vellykket oppstart. Det nye bygget måler 544532389 byte nedlasting og 659179020 byte innhold. Begge pakkeskriptene stopper over 1000 MB nedlasting eller 2000 MB utpakket, og avviser arbeidsmapper. README peker på ferdigpakkene; kodekloning er grunn og begrenset til main. Se docs/PLASSBRUK.md. Ingen ny felles release er utgitt, siden motor og HD-innhold er uendret.

49 gamle Git-metadatakopier, 230 identiske spilldatafiler og 293895 identiske PNG-kopier er fjernet etter kontroll. Alle 245 særskilte gamle Git-metadataobjekter er bevart i delt objektlager og en verifisert 3,3 MB metadatafil, pushet og faktisk hentet tilbake før sletting. Alle 44330 beholdte PNG-kilder er hashkontrollert. Ingen unike bilder eller beskyttede jobbgrunnlag er slettet. De tre opprinnelige stashene og aktive worktrees er bevart.

Prosjektets du-måling er redusert fra 90.03 til 50.84 GB på sluttmålet. Observert ledig plass økte med 31.58 GB. Btrfs deler extents og har forsinket frigjøring, så dette skilles fra 38.52 GB summerte duplikatbytes. Journalene oppgir fjernet sti, hash og beholdt kilde. Arkivrefs for gamle publiseringer beholdes; ingen Git-historikk er prunet eller omskrevet.

Videre: ett Git-objektlager, én kanonisk spilldatakilde, én nødvendig modkandidat per bunke og én kopi av hver gjeldende nedlastingspakke. Behold råbilder, unike kilder, stilankere og relevante kontrollbevis i gpt-arbeid; fjern verifiserte mellomkopier etter bunken. Historiske out-modmapper kan være ufullstendige og skal ikke brukes som ny komplett mod.

Grafikkbunken H296..H300 er sikret separat: totalt 124 råbilder, H299/1987 er arbeidskontrollpunkt med materialretur, H289/1988 er uendret. Ingen ny hel figurjobb, native mottak eller motorstatus. Fortsatt 508/1758 hele figurjobber og 3733 native. H301 er ikke startet. Ingen nødvendig ny Tom-avklaring; automatikken ACTIVE. Biblioteksøk etter diskplass ga ingen relevante treff; systemet er kontrollert mot lokale kilder og faktisk pakkeinnhold.
