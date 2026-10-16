from pathlib import Path
import json
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
R=Path('rapporter/natt-20261016-0720')
CROPS={
'fig116_05':[(40,100,350,520),(50,530,350,960),(390,530,730,960),(740,530,1120,960),(1140,530,1510,960)],
'fig116_06':[(40,50,380,400),(390,10,730,400),(735,80,1070,400),(1140,80,1450,400),(100,400,350,710),(440,400,680,710),(40,705,260,1024)],
'fig116_07':[(100,30,370,365),(440,30,740,365),(805,35,1110,365),(1150,35,1460,365),(50,365,350,700),(380,390,920,700),(940,390,1470,700),(40,690,580,1000),(600,690,1150,1000)],
'fig116_08':[(50,10,565,325),(50,330,565,650),(575,330,1095,650),(50,655,565,975),(590,655,1120,975),(1160,655,1440,975)]}

def clean(im):
 a=np.array(im.convert('RGBA'));a[a[:,:,3]<8]=0
 return Image.fromarray(a)

def components(im,minsize):
 a=np.array(clean(im));labs,n=ndi.label(a[:,:,3]>=128);out=[]
 for i,s in enumerate(ndi.find_objects(labs),1):
  size=int((labs[s]==i).sum())
  if size<minsize:continue
  keep=ndi.binary_dilation(labs==i,iterations=3)
  aa=a.copy();aa[:,:,3]=np.where(keep,aa[:,:,3],0);aa[aa[:,:,3]==0]=0
  out.append((size,Image.fromarray(aa)))
 return [im for size,im in sorted(out,key=lambda v:-v[0])]

def corebox(im):
 a=np.array(im)[:,:,3]>128;y,x=np.where(a)
 return [int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1)]

def place(out,im,box):
 x,y,w,h=box;b=corebox(im);sx=w/(b[2]-b[0]);sy=h/(b[3]-b[1]);m=3
 part=im.crop((b[0]-m,b[1]-m,b[2]+m,b[3]+m))
 part=part.resize((round(part.width*sx),round(part.height*sy)),Image.Resampling.LANCZOS)
 a=np.array(part);a[a[:,:,3]<8]=0;part=Image.fromarray(a)
 out.alpha_composite(part,(x-round(m*sx),y-round(m*sy)))

def original_components(data,c,orig):
 x,y,xx,yy=c['synlig'];m=np.any(orig[y:yy,x:xx]!=data['bakgrunn'],2);labs,n=ndi.label(m);out=[]
 for i,s in enumerate(ndi.find_objects(labs),1):
  size=int((labs[s]==i).sum());box=[(16+x+s[1].start)*4,(8+y+s[0].start)*4,(s[1].stop-s[1].start)*4,(s[0].stop-s[0].start)*4]
  out.append((size,box))
 return sorted(out,key=lambda v:-v[0])

# En blå flate fra nytegnet jakke bevarer kildens separate enkeltpiksler.
raw=clean(Image.open(R/'fig116_05-forsok1.png'))
blue=raw.crop((145,302,149,306));blue.save(R/'blaa-prikk-nytegnet.png')
placements={}
for job,crops in CROPS.items():
 data=json.load(open(f'jobber/{job}/jobb.json'));orig=np.array(Image.open(f'jobber/{job}/original_1x.png').convert('RGB'))
 raw=clean(Image.open(R/f'{job}-forsok1.png'));out=Image.new('RGBA',(1536,1024));rows=[]
 for c,crop in zip(data['ruter'],crops):
  targets=original_components(data,c,orig);dots=[b for s,b in targets if s==1];targets=[(s,b) for s,b in targets if s>1]
  parts=components(raw.crop(crop),100)
  assert len(parts)==len(targets),(job,c['bilde'],len(parts),len(targets))
  for im,(size,b) in zip(parts,targets):place(out,im,b)
  for b in dots:out.alpha_composite(blue,b[:2])
  rows.append({'bilde':c['bilde'],'raautsnitt':crop,'komponentbokser':[b for s,b in targets],'separate_prikker':dots})
 out.save(f'jobber/{job}/resultat.png');placements[job]=rows
(R/'plassering.json').write_text(json.dumps(placements,ensure_ascii=False,indent=2)+'\n')

# Profilhodet ble nytegnet og rettet i forrige nattgruppe. Originalen er samme form og palett.
# Det er sett på nytt sammen med originalutsnittet. Bare plassering og størrelse gjenbrukes her.
head=clean(Image.open('rapporter/natt-20261016-fig24710-116/alligator-hode-raa01.png'))
head.save(R/'alligator-profil-nytegnet.png')
for job in ['fig116_07','fig116_08']:
 data=json.load(open(f'jobber/{job}/jobb.json'));out=Image.open(f'jobber/{job}/resultat.png').convert('RGBA')
 for i,c in enumerate(data['ruter']):
  if (job=='fig116_07' and i<5) or (job=='fig116_08' and i==5):continue
  x,y,xx,yy=c['synlig'];bx=(16+x+12)*4;by=(8+yy-9)*4
  a=np.array(out);rx0,ry0,rx1,ry1=bx-3,by-5,bx+103,by+37
  sub=a[ry0:ry1,rx0:rx1];rgb=sub[:,:,:3].astype(float)
  brown=(rgb[:,:,0]>rgb[:,:,1]*1.25)&(rgb[:,:,1]>rgb[:,:,2]*1.25)&(sub[:,:,3]>128)
  protect=ndi.binary_dilation(brown,iterations=2)
  sub[~protect]=0
  out=Image.fromarray(a);place(out,head,[bx,by,100,36])
 out.save(f'jobber/{job}/resultat.png')

for job in CROPS:
 original=Image.open(f'jobber/{job}/referanse.png').convert('RGB')
 out=Image.open(f'jobber/{job}/resultat.png').convert('RGBA');bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out)
 pair=Image.new('RGB',(3072,1024));pair.paste(original,(0,0));pair.paste(bg.convert('RGB'),(1536,0));pair.resize((1536,512)).save(R/f'{job}-sammenligning.png')
 bg.convert('RGB').save(R/f'{job}-graa.png')
