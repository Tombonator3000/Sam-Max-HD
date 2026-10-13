# Uavhengig motivkontroll av kartlagene

Kontroll av lag010_01 og lag010_02 forsøk 01, samt lag010_03 forsøk 02 etter lokal retting. Lag010_04 forsøk 01 er også kontrollert. De tre avvikene nedenfor beskriver første kandidat og er etterkontrollert i eget avsnitt. Ingen avgjørende tilstandsfeil gjenstår i denne gjennomgangen; tegningsforbeholdene består. Ingen resultatfiler er endret av B. SHA og samsvar med roots kontrollfiler ligger i [b-kart-shakontroll.json](b-kart-shakontroll.json). Alle de første 29 objektmålingene er OK, men det friskmelder ikke tilstandsfeilene nedenfor.

## Grunnlag

Lest root-kart-kildeplan.md, c-kildeplan.md, jobbmetadata og roots kontrollfiler. Sett alle sju originale kompositter og levert HD-grunnkart i root-kart-oversikt.png, alle 15 objektfamilier i root-kart-objektfamilier-1..3.png, de tre faktiske resultatfilene og alle 29 kilde/HD-objektpar i root-lag010_01..03-objektqa01.png. Egen forstørrelse finnes i [b-kart-tilstandsutsnitt.png](b-kart-tilstandsutsnitt.png) og [b-kart-antallsutsnitt.png](b-kart-antallsutsnitt.png).

## Konkrete avvik meldt til root

1. **Obj104_02 i lag03 har feil tegntilstand.** Originalen viser en nesten rett, loddrett grå/svart stav med separat punkt over spiralen. Nytegningen viser fortsatt krummet spørsmålstegn, som i01. Dette er en bortfalt tilstandsendring, ikke bare rundere HD-strek.
2. **Obj112_03 i lag03 har feil vimpelbøy.** Original02 ender med nedoverbøyd spiss; original03 har spiss som løfter seg mot høyre. Begge nytegningene har nedoverbøyd spiss. Den tredje vimpeltilstanden må skilles fra02.
3. **Obj106_02s rotasjon er svekket.** Original02 flytter den korte mørke markeringen mot øvre venstre og den andre markeringen mot venstre/ned. HD02 endrer konturen noe, men beholder omtrent01s øvre strek og nedre takform. Dette er et konkret markering-/rotasjonsavvik, selv om steinidentiteten består.

## Bevarte motiver og dokumenterbare tolkninger

Fisk103 har tre forskjellige munner, med cyan former som flytter oppover. Krokodille105 har lukket, lavt åpnet og høyt åpnet munn, med rosa/hvite felt bare i de åpne tilstandene. Gitar107 beholder tre hals-/kroppsvinkler og ulike noteplasseringer; i03 ligger noter ved venstre feltkant som i kilden. Burger111 øker avstand og synlig fyll gjennom tre trinn. Burger114 og115 har egne felt og riktig lave første tilstand, ikke ekstra burgere. Lag01/02/03 har henholdsvis10/9/10 dokumenterte objektfelt, alle synlige i gjennomgangen. Veifelt113_01 er svart vei med gul strek, uten oppdiktet surfer eller skilt.

Flagg101 beholder svart flagg, to stenger, hvitt langøret motiv og beinformer. Runde øyehull, tannrekke og kryssede bein er en mer eksplisitt HD-tolkning av den lille originalformen; nøyaktig antall originaltenner kan ikke utledes sikkert. Hyssingball102 har trådstruktur og forskjellige posisjoner/haleformer. Tomat110_01 beholder flat rød form, men ansiktet er mer smilende og toppen tydeligere stjerneformet. Telt112 har fått en rund rød neselignende form over inngangsbuen, mens originalen viser ett sammenhengende trappet rødt inngangsfelt. Dette er et motivforbehold, ikke bevist ny figur. Vulkan108_01 og dinosaur109_01 er mer avrundet og anatomisk tydelige, men identitet, hovedstilling, lemmer og lukkede tannfelt er gjenkjennelige.

Kontrollen beviser ikke identisk pikselgeometri, alle tann-/frøprikkantall eller animasjonstiming. Ingen ny individuell brukergodkjenning, import eller runtime er utført.

## Etterkontroll av lag03, forsøk 02

Faktisk resultat SHA256 er `3b62285ffabc07c3c40f0f9232ea6971e3788158b57fbe7fa9f5f5d705cb0cc1`, identisk med root-lag010_03-kontroll02.json. Sett root-lag010_03-objektqa02.png. Utropstegnet er nå rett med separat punkt; vimpelens spiss er hevet mot høyre, slik at03 skiller seg fra02. Steinmarkeringene er flyttet mot venstre. Den nedre markeringen er fortsatt en renere sammenhengende vinkel enn originalens atskilte småstreker; dette beholdes som tegningsforbehold. De to sikre tegntilstandsfeilene er rettet.

Uavhengig RGB-sammenligning mot første råkandidat viser NULL endrede motivpiksler utenfor de tre avtalte metadatafeltene. Alle ti objektmålinger er fortsatt OK. Bevis: [b-kart03-etterkontroll.json](b-kart03-etterkontroll.json). Alle 40 beskyttede kildefiler er kontrollert mot kildehash.json uten avvik.

## Lag04 og endelig kandidatkontroll

Sett faktisk lag010_04/resultat.png og root-lag010_04-objektqa01.png. Alle fem forventede objektfelt er til stede, uten ekstra destinasjonsmarkører. Stein106_03 vender spiss og markeringer annerledes enn de to foregående. Vulkan108_02 har høyere grå spiss/rød kant enn108_01 i lag02; palme og mørke småformer er beholdt. Dinosaur109_02 har synlig rød åpning mellom de hvite tannfeltene, i motsetning til det samlede lyse tannfeltet i109_01. Munnen er ennå ikke den store03-åpningen fra senere kildekompositt. Tomat110_02 er rundere enn110_01. Burger114_02 har høyere topp og mer synlig rødt/brunt fyll enn114_01 ved samme posisjon.

De renere tannspissene, palmebladene, steinstrekene, tomatansiktet og frøprikkene er HD-tolkninger. Kontrollen sertifiserer ikke nøyaktig antall hver tann eller frøprikk; det er ikke funnet en sikker manglende hoveddel eller ny tilstandsforveksling i lag04.

Endelige SHA256 er målt fra alle fire faktiske jobbleveranser og matcher roots respektive kontrollfiler:01/02/04 forsøk01,03 forsøk02. Samtlige 34 objektfelt er målt OK uten hoppede felt. Alle fire lerret er 1536 × 1024 med nøytral RGB128-padding rundt [128,112,1280,800]. Alle 40 beskyttede kilder er uendret. Maskinlesbart bevis og fulle SHA finnes i [b-kart-shakontroll.json](b-kart-shakontroll.json). Dette er uavhengig motiv-QA, ikke import-, runtime- eller brukergodkjenning.
