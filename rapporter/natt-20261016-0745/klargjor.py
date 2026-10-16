from pathlib import Path
import json, subprocess
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
R=Path('rapporter/natt-20261016-0745')
JOBS=['fig116_09','fig249_01','fig249_02','fig249_03']
CROPS={
'fig116_09':[(140,45,510,325),(610,45,965,325),(1060,25,1420,330),(175,340,510,635),(175,650,510,940)],
'fig249_01':[(60,10,340,350),(60,350,350,700)],
'fig249_02':[(50,20,290,380),(290,20,545,380),(545,20,865,380),(865,20,1120,380),(1120,20,1390,380),(50,385,450,740)],
'fig249_03':[(10,50,420,490),(430,50,775,490),(760,50,1150,490),(1145,50,1530,490),(0,540,420,970),(430,540,795,970),(785,540,1230,970)]}
def clean(im):
 a=np.array(im.convert('RGBA'));a[a[:,:,3]<8]=0;return Image.fromarray(a)
def pieces(im,minsize=50):
 a=np.array(clean(im));labs,n=ndi.label(a[:,:,3]>128);parts=[]
 for i,s in enumerate(ndi.find_objects(labs),1):
  size=int((labs[s]==i).sum())
  if size<minsize:continue
  aa=a.copy();aa[~ndi.binary_dilation(labs==i,iterations=3)]=0
  parts.append((size,Image.fromarray(aa)))
 return [im for s,im in sorted(parts,key=lambda t:-t[0])]
def box(im):
 y,x=np.where(np.array(im)[:,:,3]>128);return [int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1)]
def place(out,im,target):
 x,y,w,h=target;b=box(im);sx=w/(b[2]-b[0]);sy=h/(b[3]-b[1]);m=3
 part=im.crop((b[0]-m,b[1]-m,b[2]+m,b[3]+m));part=part.resize((round(part.width*sx),round(part.height*sy)),Image.Resampling.LANCZOS)
 out.alpha_composite(clean(part),(x-round(m*sx),y-round(m*sy)))
def body(im):
 a=np.array(clean(im));r,g,b=[a[:,:,i].astype(float) for i in range(3)]
 green=(g>r*1.3)&(g>b*1.05);a[green]=0
 ys,xs=np.where(a[:,:,3]>128);bottom=ys.max();low=np.indices(a.shape[:2])[0]>bottom-46
 brown=(r>g*1.25)&(g>b*1.15)&(a[:,:,3]>64)
 a[low&~ndi.binary_dilation(brown,iterations=2)]=0
 return pieces(Image.fromarray(a),100)[0]
main,tail=pieces(Image.open(R/'alligator2-forsok.png'))
evidence={}
for job in JOBS:
 p=Path('jobber')/job;j=json.load(open(p/'jobb.json'));orig=np.array(Image.open(p/'original_1x.png').convert('RGB'))
 raw=clean(Image.open(R/(job+'-forsok2.png' if job in ['fig116_09','fig249_03'] else job+'-forsok1.png')))
 out=Image.new('RGBA',(1536,1024));rows=[]
 for i,c in enumerate(j['ruter']):
  x,y,xx,yy=c['synlig'];target=[(16+x)*4,(8+y)*4,(xx-x)*4,(yy-y)*4]
  if job=='fig116_09':
   sub=orig[y:yy,x:xx];r,g,b=[sub[:,:,k].astype(float) for k in range(3)];m=np.any(sub!=j['bakgrunn'],2)
   green=(g>r*1.3)&(g>b*1.05);blue=(b>g*1.1)&(r<70);low=np.indices(m.shape)[0]>=m.shape[0]-12
   m&=~green;m&=~(low&(blue|(r+g+b<80)))
   labs,n=ndi.label(m);items=[]
   for k,s in enumerate(ndi.find_objects(labs),1):
    size=int((labs[s]==k).sum());bb=[(16+x+s[1].start)*4,(8+y+s[0].start)*4,(s[1].stop-s[1].start)*4,(s[0].stop-s[0].start)*4];items.append((size,bb))
   items.sort(reverse=True);target=items[0][1]
   bottom=(8+yy)*4;left=(16+x)*4
   place(out,main,[left+152,bottom-40,252,40]);place(out,tail,[left,bottom-24,144,24])
   part=body(raw.crop(CROPS[job][i]));place(out,part,target)
   bluepatch=clean(Image.open('rapporter/natt-20261016-0720/blaa-prikk-nytegnet.png'))
   for size,bb in items[1:]:
    if size==1:out.alpha_composite(bluepatch,bb[:2])
  elif job=='fig249_02' and i==6:
   part=pieces(Image.open(R/'mouth-forsok.png'))[0];place(out,part,target)
  else:
   part=pieces(raw.crop(CROPS[job][i]),100)[0];place(out,part,target)
  rows.append({'bilde':c['bilde'],'malboks':target,'raautsnitt':CROPS[job][i] if i<len(CROPS[job]) else None})
 out.save(p/'resultat.png');evidence[job]=rows
 bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out);bg.convert('RGB').save(R/f'{job}-graa.png')
 pair=Image.new('RGB',(3072,1024));pair.paste(Image.open(p/'referanse.png'),(0,0));pair.paste(bg.convert('RGB'),(1536,0));pair.resize((1536,512)).save(R/f'{job}-sammenligning.png')
 res=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True)
 (R/f'{job}-egenkontroll.txt').write_text(res.stdout+res.stderr);print(res.stdout)
(R/'plassering.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
