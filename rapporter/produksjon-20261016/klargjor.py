from pathlib import Path
import json,hashlib,subprocess
from PIL import Image
import numpy as np
R=Path('rapporter/produksjon-20261016');G=Path('/home/tom/.codex/generated_images/01a14446-b0b5-7af1-a0a2-e4aecc260337')
RAWS={'fig249_04':'exec-2182ccbf-a9ff-401a-8d6a-08e196f7c918.png','fig249_05':'exec-bccc506d-4eba-4f81-b80a-6bcd991c9676.png','fig249_06':'exec-7d7a5451-65bd-4c46-933b-fa073af65abd.png','fig249_07':'exec-36140d8f-733f-4cb9-8c5d-8ed3395946b7.png','fig249_08':'exec-94c5e48f-22fa-48c7-8f9d-074e2510d4b7.png'}
CROPS={'fig249_04':[(25,25,520,430),(25,450,330,850),(345,445,660,850),(685,455,1080,850),(1080,455,1520,850)],'fig249_05':[(10,40,350,470),(355,90,780,470),(780,90,1050,470),(1050,90,1520,470),(10,480,470,900)],'fig249_06':[(55,20,310,385),(315,20,600,385),(605,20,840,385),(845,40,1150,385),(1150,40,1510,385),(40,390,380,700),(385,390,715,700),(720,390,1040,700),(1050,390,1400,700),(45,700,355,1010),(355,700,650,1010)],'fig249_07':[(40,40,510,500),(510,25,950,500),(960,25,1450,500),(40,500,520,1000),(525,500,955,1000),(960,500,1470,1000)],'fig249_08':[(90,25,385,440),(440,25,735,440),(795,25,1090,440),(1140,25,1450,440),(25,450,320,875)]}
def box(im):
 a=np.array(im)[:,:,3]>128;y,x=np.where(a)
 return (int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1))
def place(out,im,target):
 b=box(im);x,y,w,h=target;sx=w/(b[2]-b[0]);sy=h/(b[3]-b[1]);m=3
 part=im.crop((b[0]-m,b[1]-m,b[2]+m,b[3]+m)).resize((round((b[2]-b[0]+2*m)*sx),round((b[3]-b[1]+2*m)*sy)),Image.Resampling.LANCZOS)
 a=np.array(part);a[a[:,:,3]<8]=0;part=Image.fromarray(a)
 out.alpha_composite(part,(x-round(m*sx),y-round(m*sy)))
rows={}
for job,rawfile in RAWS.items():
 p=Path('jobber')/job;j=json.loads((p/'jobb.json').read_text());raw=Image.open(G/rawfile).convert('RGBA');raw.save(R/(job+'-raa.png'))
 out=Image.new('RGBA',(1536,1024));data=[]
 for c,cut in zip(j['ruter'],CROPS[job]):
  x,y,xx,yy=c['synlig'];target=[(16+x)*4,(8+y)*4,(xx-x)*4,(yy-y)*4]
  place(out,raw.crop(cut),target);data.append({'bilde':c['bilde'],'malboks':target,'raautsnitt':cut})
 out.save(R/(job+'-kandidat.png'));rows[job]=data
 bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out);bg.convert('RGB').save(R/(job+'-graa.png'))
 # Checker resolves metadata relative to the job folder; leave invalid candidates only in report.
 candidate=p/'resultat.png';assert not candidate.exists();out.save(candidate)
 res=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(candidate)],capture_output=True,text=True)
 (R/(job+'-egenkontroll.txt')).write_text(res.stdout+res.stderr);print(res.stdout)
(R/'plassering.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
