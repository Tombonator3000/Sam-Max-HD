from pathlib import Path
import json,hashlib,subprocess,datetime
from zoneinfo import ZoneInfo
import numpy as np
from PIL import Image
R=Path('rapporter/natt-20261016-fig24710-116')
JOBS=['fig247_10','fig116_02','fig116_03','fig116_04']
now=datetime.datetime.now(ZoneInfo('Europe/Oslo')).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
entries=[];sourcehash={}
for j in JOBS:
 p=Path('jobber')/j;data=json.loads((p/'jobb.json').read_text());a=np.array(Image.open(p/'resultat.png').convert('RGBA'))
 check=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True)
 (R/f'{j}-egenkontroll.txt').write_text(check.stdout+check.stderr)
 assert check.returncode==0,(j,check.stdout)
 rows=[]
 for c in data['ruter']:
  x,y,x1,y1=c['synlig'];wx0=(16+x-4)*4;wy0=(8+y-4)*4;wx1=(16+x1+4)*4;wy1=(8+y1+4)*4
  window=a[wy0:wy1,wx0:wx1,3]>128;yy,xx=np.where(window)
  box=[int(wx0+xx.min()),int(wy0+yy.min()),int(xx.max()-xx.min()+1),int(yy.max()-yy.min()+1)]
  row={k:c[k] for k in ['bilde','kostyme','rute','lag','animasjon','retning']};row['rect']=box;rows.append(row)
 (R/f'rutekart-{j}.json').write_text(json.dumps({j:{'ruter':rows}},ensure_ascii=False,indent=2)+'\n')
 for name in ['referanse.png','original_1x.png','prompt.txt','jobb.json']:
  current=(p/name).read_bytes();committed=subprocess.check_output(['git','show',f'HEAD:{p/name}'])
  assert current==committed, str(p/name)
  sourcehash[str(p/name)]=hashlib.sha256(current).hexdigest()
 entry={'jobb':j,'resultat':str(p/'resultat.png'),'sha256':sha(p/'resultat.png'),'forsok':4 if j=='fig247_10' else (2 if j!='fig116_04' else 1),'ruter':len(rows),'rutekart':str(R/f'rutekart-{j}.json'),'egenkontroll':'OK','kontrollfil':str(R/f'{j}-egenkontroll.txt'),'visuelt_kontrollert_statisk':True,'importert':False,'motoravspilt':False,'godkjent_av_Tom':False,'klar_for_mottak':True}
 entries.append(entry)
 # Sammenligning på grå bakgrunn med original til venstre.
 raw=Image.open(p/'referanse.png').convert('RGB').resize((768,512))
 im=Image.open(p/'resultat.png').convert('RGBA');bg=Image.new('RGBA',im.size,(128,128,128,255));bg.alpha_composite(im)
 pair=Image.new('RGB',(1536,512));pair.paste(raw,(0,0));pair.paste(bg.convert('RGB').resize((768,512)),(768,0));pair.save(R/f'{j}-sammenligning.png')
 common=f'''Dato: {now}

Verktøy: innebygd image_gen.imagegen. Eksakt modellnavn vises ikke. Python, Pillow, numpy og scipy i prosjektets eksisterende miljø er brukt til tillatt alfarensing, komponentuttrekk og presis plassering. Ingen installasjon eller pipelineendring.

Original_1x.png, referanse.png og hovedark/sam.png er kontrollgrunnlag. Originalen styrer motiv, palett, positur og 4x-geometri. Hovedarket styrer Sam-identitet og strek. ANALYSE.md, GJENNOMGANG.md og remake-skillen i lokal main er lest. Prompt.txt er sendt ordrett i første bildeforsøk. Beskyttede jobbfiler er byteidentiske med HEAD. Eldre sha256_prompt i jobb.json stemmer ikke med dagens promptfil; filen er ikke endret i denne økten. Faktiske kildehash er dokumentert i rapporten.

Leveranse: hele lerretet, 1536 x 1024, ekte alfa. Rutekart inkluderer samtlige synlige deler, også adskilte små prikker. Originalmasker brukes til kontroll og komponentmål, ikke til å klippe den nytegnede produksjonskonturen.

Egenkontroll: OK, {len(rows)} av {len(rows)} ruter OK. Systemets python3 mangler numpy. Samme kontrollskript er kjørt med /home/tom/Sam-Max-HD/.venv/bin/python uten installasjon. Kontrollutskrift: {R}/{j}-egenkontroll.txt.

Statisk visuell egenkontroll er utført mot original og godkjent hovedark, også på grå bakgrunn. Leveransen er klar for Claudes mottakskontroll. Importert: nei. Motoravspilt: nei. Animasjonstiming, faktisk hode/kropp-sammensetting i motoren og Toms godkjenning: ikke kontrollert.

SHA-256: {entry['sha256']}

Rapport, råforsøk, presiseringer, plassering og rutekart: {R}/.
'''
 if j=='fig247_10':
  specific='''Retur for costume247_1967 og 1968, rute 3 og 4. Sam løfter VR-hjelmen i rom 48. Rute 3 har nå en smal lyseblå hattestilk uten synlig brem, flatpresset ansikt og to lukkede øyestreker. Rute 4 har lav brem, lukkede øyestreker og liten svart åpen munn under snuten. Totalt fire bildeforsøk i denne økten. Første helarkforsøk ble forkastet; avgrenset nytegning ble rettet og skjøtene reparert med bildeverktøyet. Separate presiseringer gjelder den konkrete returen; den generiske beskrivelsen av begge figurene er ikke motivfasit for disse Sam-rutene. hovedark/max.png var bilde tre i første forsøk.

Rute 1, 2, 5 og 6 er byteidentiske i RGBA med forrige leveranse. Hender, kabler, slips og grønne hjelmpiksler er bevart. Bare hodefeltene og de smale ermeflatene som avdekkes av endret hatt, er satt inn fra nytegningen. Ny alfa gjelder de endrede hodefeltene. Strekkfasen er sammenlignet med originalen; motoravspilling gjenstår.

'''
 else:
  specific=f'''Kostyme 116 i rom 25, Gator Golf. {data['innhold']}. Sam balanserer og beveger seg ved alligatorene. Grønne alligatordeler er bevart i rutene som har dem, og er ikke lagt inn i rutene som mangler dem.

'''
  if j in ['fig116_02','fig116_03']:
   specific+='''To bildeforsøk berører dette arket: ett helark og én delt, separat retting av alligatorhodet. Første forsøk hadde to tydelige øyne. Originalen viser ett synlig øye i profil. Korrigert hode er nytegnet med bildeverktøyet etter originalutsnittet og plassert i hver berørt rute. Det delte hodeforsøket er brukt i fem ruter på fig116_02 og fig116_03 til sammen. Tåkontakt og den grønne flaten under føttene er sammenlignet statisk.

'''
  else:specific+='Ett bildeforsøk. De åtte gang- og balansestillingene er bevart, uten alligatordeler på dette arket.\n\n'
  specific+='''Enkelte ruter har én adskilt blå originalpiksel langt fra hovedfiguren. Sam er skalert etter hovedkomponenten, ikke etter boksen som inkluderer prikken. Prikken er bevart ved presis plassering av en liten blå flate fra den nytegnede jakken. Dette bevarer motivantall og ruteomfang uten å forstørre kroppen. Den samlede ruteboksen og hovedfiguren er kontrollert hver for seg.

'''
 (p/'notat.md').write_text(f'# {j}\n\n'+specific+common)
(R/'kildehash.json').write_text(json.dumps(sourcehash,indent=2)+'\n')
(R/'fremdrift.json').write_text(json.dumps({'dato':now,'gren':'gpt-arbeid','verktøy':'image_gen.imagegen','modell':'Eksakt modellnavn ikke vist','leveranser':entries,'teller':{'levert':4,'ruter':24,'visuelt_kontrollert_statisk':4,'importert':0,'motoravspilt':0,'godkjent_av_Tom':0},'hoppet_over':[{'jobber':['lag083_01','lag083_02','lag083_03','lag083_04'],'grunn':'ORDRE krever godkjent rom083. Rommet står til sjekk. ANALYSE dokumenterer feil skybeskrivelse og palett for lagerrom83; motivet brukes i rom54. Objekt835 avventer avklaring.'}]},ensure_ascii=False,indent=2)+'\n')
(R/'RAPPORT.md').write_text(f'''# Fire grafikkleveranser

Dato: {now}

Levert: fig247_10, fig116_02, fig116_03 og fig116_04. Fire ark og 24 ruter. Fire ark er statisk visuelt kontrollert, null er importert og null er motoravspilt i denne økten. Ingen ny godkjenning fra Tom.

Alle fire består egenkontrollen. Råforsøk, kildehash, sammenligninger, rutekart og konkrete begrensninger ligger her og i jobbnotatene. Bildene er laget med innebygd imagegen. Originalpromptene er brukt ordrett i første forsøk; de konkrete returforsøkene og alligatorrettelsen har egne presiseringer.

Fig247_10 retter originalens hattestrekking og ansiktsuttrykk i rute 3 og 4. De fire øvrige rutene er byteidentiske med den tidligere leveransen. Originalens grønne hjelmfarge er bevart.

Fig116_02 til 04 bevarer Sam ved alligatorene i rom25. Fem alligatorhoder er rettet fra to øyne til originalens ene profiløye. Små adskilte blå originalprikker er bevart separat, så de ikke blåser opp figurens bredde.

Lag083_01 til 04 er hoppet over fordi ORDRE krever godkjent rom083 og rommet fortsatt står til sjekk. Dessuten dokumenterer ANALYSE at skybeskrivelsen og lagerrompaletten er feil: objektene brukes ved boblebadet i rom54. Objekt835 har uavklart bart/munn. Ikke produser lagene etter kjent feil premiss.

Git pull ble forsøkt, men FETCH_HEAD ligger i skrivebeskyttet Git-metadata utenfor arbeidsroten. Grenen er gpt-arbeid. Ingen commit, push, grenbytte eller kodeendring er gjort.

Systemets python3 mangler numpy. Prosjektets eksisterende Python-miljø kjører samme sjekk_leveranse.py. Ingen installasjon ble gjort. Beskyttede filer er kontrollert byte for byte mot HEAD og er uendret.
''')
(R/'todo.md').write_text('''# Videre kontroll hos Claude

Kontroller mottak og faktisk motoravspilling av de fire leveransene, særlig strekkovergangen i fig247_10 og kontakt med alligatorflatene i kostyme116. Ingen motoravspilling er utført her.

Grafikkobservasjon utenfor de fire jobbene: fig116_01/resultat.png ser også ut til å ha to tydelige øyne på alligatorhodene. Sammenlign med originalens ene synlige profiløye før arket godkjennes. Det arket er ikke endret i denne økten.

Avklar og godkjenn riktig rom83-grunnlag før lag083 produseres. Originalpaletten skal være rom54. Objekt835 avventer den tidligere dokumenterte bart/munn-avklaringen.

Ingen nye konkrete kodebehov funnet i denne grafikkøkten. De kjente pipelineoppgavene i kodesporet er ikke duplisert.
''')
print('4 leveranser, 24 ruter, alle OK. Beskyttede filer uendret mot HEAD.')
