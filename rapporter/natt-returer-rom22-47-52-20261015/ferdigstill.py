from pathlib import Path
import hashlib,json,subprocess,sys
from PIL import Image,ImageDraw
import numpy as np
r=Path(__file__).parent
jobs=['lag022_02_del3av3','lag047_02','lag052_01_del2av2','lag052_02_del1av2']
locked=json.loads((r/'beskyttede-kilder.json').read_text())
assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in locked.items())
notes={
'lag022_02_del3av3':('1 nytt forsøk','Tunnel of Love, rom 22. Originalen viser en åpen mørk dør, den sentrale øksefiguren og Henrik VIII med hånden løftet. Obj228_02 er tegnet i den løftede posituren, med hånd og erme samlet. Bilde to var jobber/rom022_del3av3/resultat.png. Hele den nytegnede scenen brukes, med renset grå ramme.','Se særlig at hånden ikke etterlater det nedhengende ermet fra hvilestillingen når motoren klipper og setter sammen tilstanden.'),
'lag047_02':('1 nytt forsøk','Bumpusville Sings, rom 47. Obj442_01 er øvre del av det brune dyrehodet ved høyre kant av sceneskiltet. Originalens øre- og øyeparti skiller seg fra rombakgrunnen. Bilde to var jobber/rom047/resultat.png. Bare det nytegnede rektangelet [768,208,160,64] er satt inn i forrige levering. De øvrige tilstandene, inkludert det lille øyet obj453_01, er beholdt.','Første helbilde bestod egenkontrollen, men den strengere kontrollen fant at obj453_01 manglet. Den kandidaten er derfor ikke levert som helbilde. Kontroller dyrehodets overgang ved faktisk avspilling.'),
'lag052_01_del2av2':('4 nye forsøk','Savage Jungle Inn, rom 52. Obj486_01 er en liten munnfase på den hvilende grønne øglen, ikke en ny figur. Originalen og det godkjente jobber/rom052_del2av2/resultat.png styrer identitet og palett. Første helbilde ga riktig tilstand, men la til røde munnmerker. Forsøk 2 kopierte hvilestillingen for mye og ble forkastet. Forsøk 3 beholdt uønskede grå blokker. Forsøk 4 fjerner de oppdiktede innvendige merkene. Bare et nytegnet felt [550,748,60,48] fra siste forsøk er plassert i helbildet.','Kontroller munnfasen mot tilstand 02 og de senere fasene i spillet. Automatisk kantlikhet er ikke godkjenning av hele animasjonen.'),
'lag052_02_del1av2':('4 nye forsøk','Savage Jungle Inn, rom 52. Obj483_02 er tukanens åpne nebb. Obj486_02 er øglens neste munnfase med en liten kjølig grålilla flate foran i gapet. Bilde to var jobber/rom052_del1av2/resultat.png. Første helbilde ga riktig tilstand, men la inn varme munnmerker. Forsøk 2 kopierte hvilestillingen for mye. Forsøk 3 ga flere grå blokker enn originalen. Forsøk 4 beholder én liten grålilla flate og fjerner de øvrige merkene. Bare feltet [934,748,60,48] fra siste nytegning er satt inn i helbildet.','Den lille grålilla flaten er bevart som form fra originalen uten å gi den en ny betydning. Kontroller faseovergangen i motoren før visuell godkjenning.')}
manifest={'dato':'2026-10-15','gren':'gpt-arbeid','verktoy':'innebygd image_gen','modell':'Eksakt modellversjon ikke eksponert','ny_generering_antall':10,'leveranser':[],'figurark':False,'runtime_testet':False}
qa=Image.new('RGB',(1536,4*366),(128,128,128));draw=ImageDraw.Draw(qa)
for i,j in enumerate(jobs):
 d=Path('jobber')/j; m=json.loads((d/'jobb.json').read_text());p=d/'resultat.png';im=Image.open(p);assert im.size==(1536,1024) and im.mode=='RGB'
 a=np.asarray(im); x,y,w,h=m['bilde_i_lerret'];mask=np.ones(a.shape[:2],dtype=bool);mask[y:y+h,x:x+w]=False;assert np.all(a[mask]==128)
 sha=hashlib.sha256(p.read_bytes()).hexdigest()
 run=subprocess.run([sys.executable,'-B','verktoy/sjekk_leveranse.py',str(p)],capture_output=True,text=True);(r/(j+'-egenkontroll.txt')).write_text(run.stdout+run.stderr);assert run.returncode==0
 n,meaning,uncertain=notes[j]
 txt=f'# {j}\n\n15. oktober 2026. {n}. Innebygd image_gen er brukt til all nytegning. Eksakt modellversjon er ikke eksponert.\n\n{meaning}\n\nPrompt.txt er brukt ordrett som første del av hovedforsøket, med returteksten og separate kildepresiseringer etterpå. Beskyttede promptfiler og originaler er uendret. Alle brukte prompter og råforsøk er bevart i rapporter/natt-returer-rom22-47-52-20261015. Python er brukt til rensing av grå ramme og presis plassering av nytegnet grafikk etter Toms uttrykkelige tillatelse. Ingen originalkontur er brukt som klippemaske.\n\nLevering: RGB PNG, 1536 x 1024, eksakt grå ramme. Egenkontroll: OK. Den strengere kontrollen med smhd.gpt.check_pieces og piece_problem består også for alle objekter i jobben. Rapport: [RAPPORT.md](../../rapporter/natt-returer-rom22-47-52-20261015/RAPPORT.md).\n\nResultat SHA-256: {sha}\n\n{uncertain} Ingen motorimport, skjerm-/lydtest eller ny godkjenning fra Tom er gjort i denne økten.\n'
 (d/'notat.md').write_text(txt)
 manifest['leveranser'].append({'jobb':j,'resultat':str(p),'sha256':sha,'egenkontroll':'OK','forsok':1 if i<2 else 4,'bilde_to':m['bilde_to']})
 for k,(label,f) in enumerate([('Original',d/'referanse.png'),('Godkjent rom',Path(m['bilde_to'])),('Levering',p)]):
  part=Image.open(f).convert('RGB').resize((512,341),Image.Resampling.LANCZOS);qa.paste(part,(k*512,i*366+25));draw.text((k*512+5,i*366+6),j+' '+label,fill='white')
qa.save(r/'leveranser-kontaktark.png');(r/'leveranser.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Fire resultater og notater lagret. Beskyttede kilder uendret. Egenkontroll OK. Grå rammer eksakte.')
