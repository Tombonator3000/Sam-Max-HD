# Leveransenotat

Nattgate med lav bil og fire lykter, lykt/bygningsfasade, Sam og Max som mørke silhuetter, månesigd og stjerner. Første nytegning valgt; forsøk 2 la til en lysere munn på Max og er ikke brukt. SJEKK: global forskyvning 1,09 og blokk 1,85 originalpiksler. Bilen/lyktens små konturer og stjerneformer avviker noe. Intern svart toppstripe på 20 HD-piksler beholdt.

Innebygd ChatGPT imagegen, 2 forsøk. Eksakt bildemodell er ikke eksponert. Originalprompt brukt ordrett med separat kildepresisering. Alle råforsøk og faktisk brukte prompter ligger i rapportmappen. Ikke utførte planprompter er merket i proveniens.

Nøyaktig 1536 × 1024, motivfelt [128,368,1280,288] og RGB128-padding. Ren gråskala. Autorisert global monoton tonekomprimering av nygenererte piksler til dette panelets originale toneområde; målinger og formel i b-tonemaaling.json og oppskriften. Ingen lokale histogramkart, originalmasker, vektortrace eller geometrisk warp.

Egenkontroll: SJEKK. Teknisk kontroll er ikke runtime eller ny individuell brukergodkjenning. Begge er false. Små detaljkonturer er HD-tolkning, og faktiske kredittlag er ikke motortestet.

Resultat SHA256: a6fcd7bb2b602d7ff134afcaa75a8f814182c3d92e06ed62bc56cc02bfe172b9

Kildehash: [{"fil": "jobber/obj775_01/referanse.png", "sha256": "f94255227220f21465a1816b3d61d6291cd77e2288da54819e70b9ef3c7ac5ac"}, {"fil": "jobber/obj775_01/original_1x.png", "sha256": "0bdc5d951a6b4bbf09281c9a0ad32f829ad782133055e17a81c086f685957053"}, {"fil": "jobber/obj775_01/prompt.txt", "sha256": "8ad5dad6c898188ad7018804b363915a4f6d9911599c578ca2e40e914b0a2255"}, {"fil": "jobber/obj775_01/jobb.json", "sha256": "facc144c91b49e5440b0c7e46e9900eb988d21af704ebf46841a934bd7b09ee8"}]

## Avgrenset stjerneoverstyring

To manglende småstjerner er komponert fra en faktisk nygenerert stjerne i samme HD-bilde. Bare [984,408,4,4] og [892,440,4,4] er endret, resten er byte-identisk. Ingen originalfarger eller originalpikselmasker er brukt. Uendret checker er fortsatt SJEKK. Historisk B-manifest beholdes; gjeldende SHA finnes i root-775-overstyring.json.

Gjeldende resultat SHA256: b545e39550dbe19da9904ca11021c1778e5f8e51db006c57774949b293437944
