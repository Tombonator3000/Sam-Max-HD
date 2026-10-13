# Bestilling 18 B, kilde-QA

Fire separate grå kredittillustrasjoner er levert med resultat, notat, råforsøk, faktisk brukte prompter, proveniens og reproduksjonsoppskrifter. Alle 40 beskyttede kilder er uendret. GRUNNLAG og b-kildeplan er fulgt. Ingen Git, globale logger eller pipeline er endret.

## Kontrollstatus

| Jobb | Forsøk | Valgt | Uendret checker, global/blokk/kant | Status |
| --- | --- | --- | --- | --- |
| obj774_01 | 1 | 1 | 0,93 / 1,18 / 0,76 | SJEKK |
| obj775_01 | 2 | 1 | 1,09 / 1,85 / 0,88 | SJEKK |
| obj776_01 | 1 | 1 | 0,51 / 0,29 / 0,93 | OK |
| obj777_01 | 3 | 2 med lokal retting fra 3 | 0,15 / 0,08 / 0,94 | OK |

774 og 775 er ikke kalt teknisk OK eller klare for mottak i manifestet. Små forskyvninger og konturavvik består. Ingen FEIL er skjult eller terskel endret. De tidligere kontrollene viser at 775 først fikk FEIL ved feil behandling av den interne svarte toppstripen, og 777 måtte omtegnes. Den endelige 777 følger kildens komposisjon bedre.

## Motiv og rettinger

774 beholder Max til venstre, Sam til høyre, utstrakte hender, foreshortening og stjerneutslag. Nye finger-, tann- og stjernespisskonturer er ikke pikselidentiske. En formulering i første presisering knyttet den store foten til Sam; den synlige tegningen og kilden viser fot-/beinforløp fra Max. Den faktisk sendte prompten er bevart uendret som proveniens, mens denne QA-en presiserer anatomien.

775 beholder nattgate, bilens fire lykter, lykt, bygning, månesigd og de to mørke silhuettene. Andre forsøk introduserte en tydeligere tannmunn på Max og er forkastet. Første forsøk er valgt med dokumentert SJEKK. Stjerneformene, bilens små konturer og lyktens vinkler avviker noe; noen punkter har fått rundere lysform. Ingen påstand om identisk småstjerneantall.

776 beholder bylandemerker, vindusrekker, lyskegle og langøret symbol samt to figurer bakfra. Ingen tekst eller ekstra gjest. Små vindusformer, skystrøk og kantlys er HD-tolkning. Ikke sertifisert identisk antall av hver lille vindusrute.

777 beholder bilinteriør, diagonale vindusrammer, speil med hengende ornament, håndgrep, Sam bak rattet og Max foran med lange bakoverstrakte ører. Nærkontroll avklarte at Max har smale vertikale øyestreker i kilden; presiseringens omtale av horisontale/halvlukkede øyne var for streng og støttes ikke av det forstørrede utsnittet. Ingen slik feilretting er utført. En prikk og kapsellignende liten form i Sams munn ble derimot korrigert med innebygd imagegen. Bare et fast rektangel [712,512,88,45] inne i den nygenererte munnen er erstattet. Resten er verifisert byte-identisk. Ingen originalkonturmaske eller innlimte originalpiksler. Nytegnet munninnhold er kontrollert som tenner og skyggeflater.

## Palett, plassering og proveniens

Alle resultatene er 1536 × 1024 med motivfelt [128,368,1280,288] og eksakt RGB128-padding. R=G=B i samtlige resultatpiksler. 775 og 777 beholder den tilsiktede svarte toppstripen som inngår i motivet.

Første råforsøk var for lyse og hadde små kanalavvik. Etter roots uttrykkelige videreføring av brukerens bildebehandlingsautorisasjon brukes én global monoton komprimering av det nygenererte gråfeltet:
`f(x)=round(x/(1+x*(1/M-1/G)))`, der G er faktisk generert maksimum etter helskalering og M er originalens maksimum. Dette bare reduserer toneverdier, bevarer rangorden og bruker ingen lokale histogrammer eller kildemasker. M er 99,107,131,99 for de fire panelene. Både før-, etter- og sluttmålinger er bevart i b-tonemaaling.json; mellomtoner og mørke figurer er vurdert i b-familie.png. Bilpanelets lokale nytegning har allerede mørkt gråområde under 99 og tonekomprimeres ikke en gang til.

Bildegeneratorens eksakte modellnavn er ikke eksponert. Første forsøk brukte originalen, godkjent stilanker og hovedark med uttrykkelig palettoverstyring. Senere helforsøk brukte bare originalen. Lokalforsøket brukte eget HD-utsnitt og originalutsnitt. Planprompter for ikke utførte andre forsøk på 774 og 776 er uttrykkelig merket ubrukte i b-proveniens.json.

Samlet visuell sammenligning er gjort i b-familie.png, original til venstre og valgt HD til høyre. Dette er ikke motorimport, skriptprøving av kredittsekvensen eller ny individuell brukergodkjenning. Runtime=false og ny_brukergodkjenning=false.
