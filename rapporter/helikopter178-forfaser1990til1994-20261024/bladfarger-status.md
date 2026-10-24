# Fase1987: bladfarger og grønne stagfester

H311..H315 er fem nye faktiske innebygde image_gen-kall, totalt 139 mottatte råbilder. Dette er rettinger i én åpen fase av fig178_02, ikke fem leverte figurjobber. Råbilder, faktisk prompt/argumenter, referansehasher, kontroll og notater er bevart. H316 er ikke startet, forberedt eller reservert.

| Prøve | Positive materialfester | Rå RGB positiv/ekstra | Vurdering |
| --- | ---: | ---: | --- |
| H311 | 10 | 274/6230 | Liten grå dash beholdt; ett grønt feste bedre. Mellomtrinn. |
| H312 | 18 | 279/6449 | For bredt lyst innvendig gråbånd, grønne gap borte. Retur. |
| H313 | 11 | 276/6350 | Mørkere grått, men bånd fortsatt for bredt og grønne felter feil. Retur. |
| H314 | 12 | 282/6401 | Grønn halebase tilbake, men tre brune fester tapes og oransje driver. Retur. |
| H315 | 9 | 271/6182 | Lite grønt fremre stagfeste tilbake. Holdt arbeidskontrollpunkt, fortsatt retur. |

Alle fem har 0/0 form/åpning ved uendret frosset hel skalering/flytt og 3 HD/12 prosent-porter. H315 har fortsatt svart 1, grått 5, grønt 3 positive materialfester. Blått/gull/brunt/lavendel har 0 positive. Ekstra klassepiksler er 10 sort, 25 blått, 101 gull, 158 grått, 14 brunt, 189 grønt, 1 lavendel. Gyllenaksent er 101 mot H310s 95 og alle rå 22 RGB-diagnoser beholdes. Tallene gir ingen teknisk eller visuell godkjenning alene.

Kildekontrollen nyanserte H311s formulering: grått er også et innvendig bånd, ikke bare nedre bladkant. Ni 8-nabogrupper i originalens grå piksler er fargeområder, ikke ni gjenstander. Den nedre innvendige gruppen bruker RGB 55/71/115, den store øvre 55/71/115/151. Dette er dokumentert før H312/H313. H312 får tilbake to gamle grå fester, men mister andre og tegner et for stort lyst bånd. H313 reduserer grå positive til tre, men har sju grønne feil og 292 ekstra grå klassepiksler; den overtar ikke H315s blad. Originalens små refleksfarger og gull 39,15/47,21 er bevart. Sam er eneste godkjente stilanker.

Fem egne heltegninger og native-PNG/RGBA er gjenskapt byteeksakt fra 20 egne råbilder under en sperre mot originalbilder/masker som produksjonsbilder. H315s sluttpiksler har ti direkte råopphav: H266/H267/H268/H270/H299/H300/H309/H310/H311/H315. Egen alfa er byteidentisk med H310. Bare egne RGB, egne myke rektangler og hele egne genererte blad brukes. Ingen originale masker/piksler eller kildepunktpåmaling. Se replay-bladfarger.json og rutekart-bladfarger.json.

H315 er lokalt motorobservert i én NY faktisk 160 bilders avspilling sammenlignet med bevart tidligere faktisk baseline fra kilde 03ff8106b2fd95a490d5df91ae2e62618abbc30a, samme binær og oppsett. Ny kjøring har 148 nullkontroller, 120/120 null etter frame 40. Kandidaten har én tapsfri WebP-rute ekstra, midlertidig 3734 native, med exact RGBA også under alfa0. Det er én nødvendig hardlenket komplett kandidat fra fersk publisert hd-mod c80099158b30fb08fa0cb670acb112bf14fd58f4, ikke et nytt native mottak. Alle 21978 aktive modhash og tekniske PNG er uendret.

Den unike 1987-ruten finnes i frame 108 ved 39,67,72x36. Lokal original-ROI 144,260,456,420 rundt hele ruten med native marger er byteidentisk; H315 endrer 13272 HD-piksler der. Helskjermtilstander utenfor ROI divergerer. Matching på rom, hele original-RGBA og celkall gir 52 hele par og 108 uparede tilstander per kjøring. Dette er bare lokal motorobservasjon av konstruert aktør 29 i rom 35. Ingen helskjermregresjon, naturlig gjennomspilling eller ny Windows-/webtest er hevdet. Baseline er eksplisitt gjenbrukt, ikke feilaktig merket som en ny kjøring. Strace dekker bare rename/unlink, ingen faktisk WebP-open/read. Motorpar og hele H315-bildet er sett. Se bladfarger-H315-motor-kontroll.json.

Tre kandidatspesifikke filer og fullmanifest er bevart. Fullkandidaten ryddes først etter kildecommit er pushet og faktisk hentet tilbake; SHA-festet journal blir bladfarger-rydding.json. Ingen nye fulle Git-/spilldatakopier, dobbeltlagrede nedlastinger eller nye pakkebygg. Fire uendrede releasevedleggs ID/størrelser/sjekksummer er lest på nytt; tidligere faktisk nedlastede og innholdskontrollerte Linux 392411640 byte og Windows 544532414 byte beholdes enkeltvis.

Fortsatt 508/1758 hele figurjobber,1250 uten resultat pluss returer/sluttkontroll,3733 publiserte native, fig178_02 20/24 og familie 178 32/102. Alle 9174 beskyttede filer, derav 9064 jobb/hovedark, og tre opprinnelige stasher er uendret. Ingen ny hel resultat.png, formelt native mottak, publisert modgrafikk/pakke eller Tom-/Claude-godkjenning. H289/1988 og H252/1990 er uendret; øvrige åpne faser fortsetter. Ingen nødvendig ny Tom-avklaring. Automatikken ACTIVE; all grafikk og sluttkontroll gjenstår.

Faktisk målt utenfor ROI: 17330 HD-avvik; hele originalskjermen har 16096 avvik. Disse holdes atskilt fra byteidentisk lokal original-ROI.
