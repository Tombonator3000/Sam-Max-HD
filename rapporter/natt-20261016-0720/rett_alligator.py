# Avgrenset grafikkarbeid, ikke pipelinekode. Sam beholdes; nytegnede alligatorflater plasseres bak.
from pathlib import Path
import json
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
R=Path('rapporter/natt-20261016-0720')

def pieces(im):
 a=np.array(im.convert('RGBA'));a[a[:,:,3]<8]=0
 labs,n=ndi.label(a[:,:,3]>128);res=[]
 for i,s in enumerate(ndi.find_objects(labs),1):
  size=int((labs[s]==i).sum())
  if size<100:continue
  aa=a.copy();m=ndi.binary_dilation(labs==i,iterations=3);aa[~m]=0
  res.append((size,Image.fromarray(aa)))
 return [im for s,im in sorted(res,key=lambda p:-p[0])]

def box(im):
 a=np.array(im)[:,:,3]>128;y,x=np.where(a)
 return (int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1))

def place(out,im,target):
 x,y,w,h=target;b=box(im);sx=w/(b[2]-b[0]);sy=h/(b[3]-b[1]);m=3
 part=im.crop((b[0]-m,b[1]-m,b[2]+m,b[3]+m));part=part.resize((round(part.width*sx),round(part.height*sy)),Image.Resampling.LANCZOS)
 a=np.array(part);a[a[:,:,3]<8]=0;part=Image.fromarray(a)
 out.alpha_composite(part,(x-round(m*sx),y-round(m*sy)))

main=pieces(Image.open(R/'alligator-hel-forsok1.png'))[0]
tail,tip=pieces(Image.open(R/'alligator-lapper-forsok2.png'))
evidence={}
for job in ['fig116_07','fig116_08']:
 p=Path('jobber')/job;data=json.load(open(p/'jobb.json'));a=np.array(Image.open(p/'resultat.png').convert('RGBA'));before=a.copy()
 Image.fromarray(before).save(R/f'{job}-for-alligatorretting.png')
 newgreen=Image.new('RGBA',(1536,1024));rows=[]
 for i,c in enumerate(data['ruter']):
  if (job=='fig116_07' and i<5) or (job=='fig116_08' and i==5):continue
  x,y,xx,yy=c['synlig'];left=(16+x)*4;bottom=(8+yy)*4
  rx0,ry0,rx1,ry1=left-4,bottom-52,left+444,bottom+4
  sub=a[ry0:ry1,rx0:rx1];rgb=sub[:,:,:3].astype(float)
  brown=(rgb[:,:,0]>rgb[:,:,1]*1.25)&(rgb[:,:,1]>rgb[:,:,2]*1.2)
  blue=(rgb[:,:,2]>rgb[:,:,1]*1.05)&(rgb[:,:,1]>rgb[:,:,2]*.65)&(rgb[:,:,2]>rgb[:,:,0]*1.1)
  body=(brown|blue)&(sub[:,:,3]>64)
  keep=ndi.binary_dilation(body,iterations=2)
  green=(rgb[:,:,1]>rgb[:,:,0]*1.3)&(rgb[:,:,1]>rgb[:,:,2]*1.05)
  keep&=~green
  # Dette er alfarensing etter nytegningens egne farger, ikke originalmaskeklipping.
  sub[~keep]=0
  places=[[left+48,bottom-36,232,36],[left,bottom-24,40,20],[left+288,bottom-20,152,20]]
  for im,t in zip([main,tip,tail],places):place(newgreen,im,t)
  rows.append({'bilde':c['bilde'],'alligatorbokser':places,'renset_felt':[rx0,ry0,rx1-rx0,ry1-ry0]})
 out=newgreen;out.alpha_composite(Image.fromarray(a));out.save(p/'resultat.png')
 evidence[job]=rows
(R/'alligator-plassering.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')

for job in ['fig116_05','fig116_06','fig116_07','fig116_08']:
 original=Image.open(f'jobber/{job}/referanse.png').convert('RGB');out=Image.open(f'jobber/{job}/resultat.png').convert('RGBA')
 bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out);bg.convert('RGB').save(R/f'{job}-graa.png')
 pair=Image.new('RGB',(3072,1024));pair.paste(original,(0,0));pair.paste(bg.convert('RGB'),(1536,0));pair.resize((1536,512)).save(R/f'{job}-sammenligning.png')
 if job in ['fig116_07','fig116_08']:
  b=(72,40,528,300) if job=='fig116_08' else (348,368,804,608)
  pair=Image.new('RGB',(912,260));pair.paste(original.crop(b),(0,0));pair.paste(bg.convert('RGB').crop(b),(456,0));pair.save(R/f'{job}-alligator-kontroll.png')
