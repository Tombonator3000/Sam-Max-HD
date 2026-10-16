from pathlib import Path
from PIL import Image
import json,hashlib,subprocess
import numpy as np
from datetime import datetime
from zoneinfo import ZoneInfo
R=Path('rapporter/produksjon-20261016');when=datetime.now(ZoneInfo('Europe/Oslo')).isoformat(timespec='seconds');jobs=['fig249_02','fig249_04','fig249_05','fig249_06','fig249_07','fig249_08'];deliveries=[];locked=[]
for job in jobs:
 p=Path('jobber')/job;j=json.loads((p/'jobb.json').read_text());im=Image.open(p/'resultat.png').convert('RGBA');a=np.array(im);sha=hashlib.sha256((p/'resultat.png').read_bytes()).hexdigest();rows=[]
 for name in ['referanse.png','original_1x.png','prompt.txt','jobb.json']:
  f=p/name;old=subprocess.check_output(['git','show','HEAD:'+str(f)]);assert old==f.read_bytes();locked.append({'fil':str(f),'sha256':hashlib.sha256(old).hexdigest()})
 for c in j['ruter']:
  x,y,xx,yy=c['synlig'];x0=max(0,(16+x-4)*4);y0=max(0,(8+y-4)*4);x1=min(1536,(16+xx+4)*4);y1=min(1024,(8+yy+4)*4);ys,xs=np.where(a[y0:y1,x0:x1,3]>128);assert len(xs)
  rows.append({k:c[k] for k in ['bilde','kostyme','rute','lag','animasjon','retning']}|{'rect':[int(x0+xs.min()),int(y0+ys.min()),int(xs.max()-xs.min()+1),int(ys.max()-ys.min()+1)]})
 (R/f'rutekart-{job}.json').write_text(json.dumps({job:{'sha256_resultat':sha,'ruter':rows}},ensure_ascii=False,indent=2)+'\n')
 result=(R/f'{job}-egenkontroll.txt').read_text();state='SJEKK' if 'Utfall: SJEKK' in result else 'OK';assert 'FEIL' not in result
 meaning='Sam i den virtuelle verdenen, rom49: sverdbevegelse, dragehjerte og nøkkel. Originalens kostyme249 styrer positur, palett og retninger; hovedark/sam.png er godkjent stilreferanse.'
 extra='Bare munndelen costume249_257 er endret. Seks gangruter er uendret mot godkjent HEAD. Direkte dekning 0,9034 og snitt/union 0,8833. Tidligere godkjenning gjelder gammel SHA; denne rettingen er ikke automatisk Tom-godkjent.' if job=='fig249_02' else 'Nytt ark. Ikke Tom-godkjent. Sammenlignet visuelt med originalen på grå bakgrunn. Omrissmerknadene i egenkontrollen står åpne. Ingen automatisk visuell godkjenning.'
 (p/'notat.md').write_text(f'# {job}\n\nDato: {when}, Codex.\n\n{meaning}\n\nVerktøy: innebygd image_gen. Intern bildemodell er ikke oppgitt. Python brukt til rensing og nøyaktig plassering, etter Toms tidligere autorisasjon dokumentert i log.md 15. oktober. Hele lerretet er 1536 x 1024 med ekte alfa.\n\n{extra}\n\nEgenkontroll: {state}. Se ../../{R}/{job}-egenkontroll.txt og sammenligningsbildet. Ingen motorimport eller spillavspilling utført. Råforsøk, endelige prompter, SHA og rutekart ligger i ../../{R}/.\n\nSHA-256: {sha}\n')
 deliveries.append({'jobb':job,'resultat':str(p/'resultat.png'),'sha256':sha,'ruter':len(rows),'nye_ruter':1 if job=='fig249_02' else len(rows),'rutekart':str(R/f'rutekart-{job}.json'),'egenkontroll':state,'visuelt_kontrollert_av':'Codex, ikke godkjent i motor','godkjent_av_Tom':False,'importert':False,'motoravspilt':False})
old=np.array(Image.open(R/'fig249_02-godkjent-foer.png').convert('RGBA'));new=np.array(Image.open('jobber/fig249_02/resultat.png').convert('RGBA'));mask=np.ones(old.shape[:2],bool);mask[668:732,64:136]=False;assert np.array_equal(old[mask],new[mask])
(R/'beskyttede-filer.json').write_text(json.dumps({'kontrollert':when,'filer':locked,'seks_gangruter_uendret':True},ensure_ascii=False,indent=2)+'\n')
(R/'fremdrift.json').write_text(json.dumps({'dato':when,'verktøy':'innebygd image_gen','antall_bildekall':11,'nye_ark':5,'nye_ruter':32,'rettede_ruter':1,'leveranser':deliveries},ensure_ascii=False,indent=2)+'\n')
(R/'RAPPORT.md').write_text(f'''# HD-produksjon {when}

Fem nye Sam-ark i kostyme249, 32 ruter, og rettet munndel i fig249_02. Innebygd image_gen brukt, 11 bildekall. Kilder: ORDRE.md fra 08:44, ANALYSE.md, GJENNOMGANG.md, originale jobbfiler og godkjent hovedark/sam.png. Ingen ukjent figur eller gjenstand krevde nytt walkthrough-oppslag. Lag083 er fortsatt avhengig av godkjent rom083 og er ikke omtegnet.

## Leveranser og kontroll

- fig249_02: bare munndelen rettet. Egenkontroll OK. Alle seks gangruter byteidentiske med godkjent HEAD utenfor munnvinduet. Direkte omrissdekning 0,9034, snitt/union 0,8833. Ny SHA trenger mottak; tidligere godkjenning gjelder forrige bilde.
- fig249_04: fem nye ruter, egenkontroll OK.
- fig249_05: fem nye ruter, SJEKK på 153, 155 og 156. Glød fjernet med et smalt bildekall, kontrollert på grå bakgrunn. Størrelse/plassering innenfor kontrollen; omriss må vurderes.
- fig249_06: elleve nye ruter, SJEKK på 167 til 169. Den rene første komposisjonen beholdes. Nyere delingsforsøk ga kantrester og er forkastet. Kroppene i kildeidentiske faser må vurderes for flimmer i mottaket.
- fig249_07: seks nye ruter, SJEKK på 171 til 174. Den rene første komposisjonen beholdes, uten de mislykkede delingsforsøkene. Dråpeformer og omriss må kontrolleres nærmere.
- fig249_08: fem nye ruter, SJEKK på alle fem, snitt/union rundt 0,72 til 0,73. Samme nytegnede kropp brukt for de fem kildeidentiske kroppene. Små røde deler er plassert separat fra originale posisjoner med generert dråpe/dam. Ikke godkjent som ferdig animasjon.

To ark OK og fire SJEKK, ingen FEIL i endelig egenkontroll. SJEKK betyr åpne merknader, ikke ferdiggodkjenning. Ingen ny import, hd-mod, utgivelse eller motoravspilling. Tom har ikke godkjent de nye SHA-ene. status.csv og ORDRE.md er overlatt til mottaket.

## Sporbarhet

Endelige filer er jobber/fig249_02/resultat.png og jobber/fig249_04 til fig249_08/resultat.png. Fremdrift og rutekart er skrevet fra faktiske sluttfiler og alfa over128. De 24 beskyttede jobbfiler er bytekontrollert mot HEAD. Prompter er bevart her; grunnpromptene er uendret i jobbmappene. Notatene skiller kontroll, godkjenning og import.

klargjor.py beskriver første plassering; deler.py og siste-deler.py er bevarte mellomforsøk og skal ikke kjøres som sluttproduksjon. slutt.py setter sammen den valgte sluttgruppen fra rene kandidater. Forkastede forsøk skal aldri brukes som stilankere. De rå bildefilene har ofte farge i helt gjennomsiktige piksler, og derfor er visuell kontroll gjort etter alfakomposisjon på grått.
''')
entry=f'\n\n## {when} (Codex, videre HD-produksjon)\n\n- Fem nye Sam-ark fig249_04 til fig249_08, 32 ruter, og rettet munndel i fig249_02. Innebygd image_gen, 11 bildekall, originale ruter og godkjent Sam-hovedark brukt. Python-rensing/plassering innenfor tidligere autorisasjon.\n- Endelig egenkontroll: fig249_02 og fig249_04 OK; fig249_05 til fig249_08 SJEKK, ingen FEIL. Omrissmerknader står åpne; mislykkede delingsforsøk forkastet. Seks godkjente gangruter uendret. Munndekning 0,9034, IoU 0,8833.\n- 24 beskyttede jobbfiler uendret. Faktiske slutt-SHA, rutekart, prompter, råforsøk, notater og sammenligninger i rapporter/produksjon-20261016. Ingen ny Tom-godkjenning, import, hd-mod, release eller motoravspilling.\n'
p=Path('log.md');p.write_text(p.read_text()+entry)
p=Path('todo.md');p.write_text(p.read_text()+f'\n\n## Videre produksjon {when}\n\n- [x] Tegnet fig249_04 til fig249_08 og rettet bare munndelen i fig249_02. Rapport: rapporter/produksjon-20261016.\n- [ ] Mottak og visuell vurdering av nye SHA-er. To ark OK, fire SJEKK. Ikke tell 32 nye ruter som importert ennå.\n- [ ] Vurder omriss og gjentatte kroppsfaser i fig249_05 til fig249_08 før ferdiggodkjenning.\n')
p=Path('STATUS.md');p.write_text(p.read_text()+f'\n\n## HD-produksjon {when}\n\nFem nye ark med32 ruter og én munndelretting levert til kontroll i gpt-arbeid. fig249_02 og fig249_04 har egenkontroll OK; fig249_05 til fig249_08 SJEKK. Ingen ny import eller motoravspilling. Se rapporter/produksjon-20261016/RAPPORT.md.\n')
print('Dokumentert',len(deliveries),'leveranser,',len(locked),'beskyttede filer, 32 nye ruter og 1 retting')
