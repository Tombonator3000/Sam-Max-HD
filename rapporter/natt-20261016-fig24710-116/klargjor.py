from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
R=Path('rapporter/natt-20261016-fig24710-116')
G=Path('/home/tom/.codex/generated_images/01a14301-3097-74d3-b60d-7b7e9f23575b')

def clean(im):
 a=np.array(im.convert('RGBA')); a[a[:,:,3]<8]=0
 return Image.fromarray(a)

def corebox(im):
 a=np.array(im)[:,:,3]>=128;y,x=np.where(a)
 return (int(x.min()),int(y.min()),int(x.max()+1),int(y.max()+1))

def fit(im,box):
 # Tilpasning av nytegnet geometri, uten originalens pikselmaske.
 b=corebox(im); part=im.crop(b).resize((box[2]-box[0],box[3]-box[1]),Image.Resampling.LANCZOS)
 return part

def furface(im,box):
 part=im.crop(box);a=np.array(part);rgb=a[:,:,:3].astype(float)
 orange=(rgb[:,:,0]>rgb[:,:,1]*1.25)&(rgb[:,:,1]>rgb[:,:,2]*1.2)&(a[:,:,3]>128)
 labs,n=ndi.label(orange); sizes=np.bincount(labs.ravel());sizes[0]=0
 m=labs==sizes.argmax();m=ndi.binary_fill_holes(m);m=ndi.binary_dilation(m,iterations=4)
 a[:,:,3]=np.where(m,a[:,:,3],0);a[a[:,:,3]==0]=0
 return Image.fromarray(a)

raw=clean(Image.open(G/'exec-69b49543-373e-47a6-942b-19f0f8d80401.png'))
raw.save(R/'fig247_10-hoder-raa03.png')
old=Image.open(R/'fig247_10-for-retur.png').convert('RGBA')
# Slett bare gammel hatt og gammelt ansikt, uten hender, hjelm, kabel eller kropp.
mask=Image.new('L',old.size);d=ImageDraw.Draw(mask)
d.polygon([(546,263),(560,243),(571,224),(605,224),(613,257),(626,267),(632,295),(630,313),(613,322),(573,332),(542,324),(517,309),(505,295),(509,283),(535,276),(546,272)],fill=255)
d.polygon([(740,274),(757,258),(767,239),(802,236),(815,264),(834,272),(835,287),(846,305),(845,322),(824,335),(782,339),(755,329),(731,319),(725,306),(732,295),(763,288)],fill=255)
a=np.array(old);a[np.array(mask)>0]=0;out=Image.fromarray(a)
face3=furface(raw,(88,315,685,545)); part3=fit(face3,(516,270,627,328));out.alpha_composite(part3,(516,270))
stalk=raw.crop((430,76,522,329));part=fit(stalk,(579,224,604,273));out.alpha_composite(part,(579,224))
# Hatt 4 har allerede riktig HD-design. Bruk den opprinnelige nytegningen og senk ikke andre deler.
hat=old.crop((736,237,835,288));hatmask=Image.new('L',hat.size);hd=ImageDraw.Draw(hatmask);hd.polygon([(1,38),(23,31),(34,7),(50,0),(70,9),(76,31),(98,37),(98,48),(28,51),(1,45)],fill=255)
ha=np.array(hat);ha[:,:,3]=np.minimum(ha[:,:,3],np.array(hatmask));out.alpha_composite(Image.fromarray(ha),(736,237))
face4=furface(raw,(1201,378,1821,588));part4=fit(face4,(730,285,845,335));out.alpha_composite(part4,(730,285))
out=clean(out);out.save('jobber/fig247_10/resultat.png')
out.crop((496,208,896,352)).resize((1200,432),Image.Resampling.NEAREST).save(R/'fig247_10-hoder-slutt.png')

# Første Sam-rute. Råbildet har tre adskilte nytegnede komponenter.
raw=clean(Image.open(G/'exec-80a91f4e-1042-454b-aefc-4ac0f735395d.png'));raw.save(R/'fig116_02-raa01.png')
out=Image.new('RGBA',(1536,1024))
# Sam og alligatorhode er sammenhengende. Flytt de synlige delene etter originalens kontaktlinje.
# Først grov samlet plassering, så egenkontroll og visuell inspeksjon.
part=fit(raw.crop((35,35,610,365)),(80,48,520,288));out.alpha_composite(part,(80,48));out.save('jobber/fig116_02/resultat.png')

# Ark 3 og 4: bevar alle nytegnede ruter og tilpass hver enkelt til den beskyttede originalens boks.
import json
for job, filename, crops in [
 ('fig116_03','exec-cf400dcb-16fe-4165-9fbc-9f4f3c3b4202.png',[(30,40,540,350),(550,40,1070,350),(30,358,525,658),(548,358,1065,658),(1130,358,1465,661),(45,660,405,980),(430,660,780,980),(830,660,1120,980),(1228,660,1470,980)]),
 ('fig116_04','exec-e8663a2e-e13c-40ed-b404-aacf50780357.png',[(70,130,370,487),(445,138,756,489),(800,140,1110,488),(1170,144,1490,490),(60,600,414,942),(421,571,791,943),(794,583,1167,941),(1184,572,1488,945)]),
]:
 raw=clean(Image.open(G/filename));raw.save(R/f'{job}-raa01.png')
 data=json.load(open(f'jobber/{job}/jobb.json'));out=Image.new('RGBA',(1536,1024))
 for c,b in zip(data['ruter'],crops):
  x0,y0,x1,y1=c['synlig'];box=((16+x0)*4,(8+y0)*4,(16+x1)*4,(8+y1)*4)
  part=fit(raw.crop(b),box);out.alpha_composite(part,box[:2])
 out.save(f'jobber/{job}/resultat.png')

# Bygg retur på nytt med bare den gamle ansikts- og hattemasken fjernet.
raw=clean(Image.open(G/'exec-69b49543-373e-47a6-942b-19f0f8d80401.png'))
out=Image.open(R/'fig247_10-for-retur.png').convert('RGBA');a=np.array(out)
for box in [(503,273,634,334),(722,284,851,341)]:
 x0,y0,x1,y1=box;part=a[y0:y1,x0:x1];rgb=part[:,:,:3].astype(float)
 orange=(rgb[:,:,0]>rgb[:,:,1]*1.25)&(rgb[:,:,1]>rgb[:,:,2]*1.2)&(part[:,:,3]>128)
 m=ndi.binary_fill_holes(orange);m=ndi.binary_dilation(m,iterations=2)
 part[m]=0
# Gammel hatt 3 fjernes med et avgrenset utsnitt som ikke berører hender og ermer.
mask=Image.new('L',out.size);d=ImageDraw.Draw(mask)
d.polygon([(543,266),(560,260),(566,242),(570,229),(578,225),(592,228),(601,239),(603,258),(624,267),(625,276),(555,278),(543,272)],fill=255)
a[np.array(mask)>0]=0;out=Image.fromarray(a)
part3=fit(furface(raw,(88,315,685,545)),(516,270,627,328));out.alpha_composite(part3,(516,270))
part=fit(raw.crop((430,76,522,329)),(579,224,604,273));out.alpha_composite(part,(579,224))
part4=fit(furface(raw,(1201,378,1821,588)),(730,285,845,335));out.alpha_composite(part4,(730,285))
out=clean(out);out.save('jobber/fig247_10/resultat.png')
out.crop((496,208,896,352)).resize((1200,432),Image.Resampling.NEAREST).save(R/'fig247_10-hoder-slutt.png')

# Originalarkene har også enkelte adskilte blå piksler. De skal ikke blåse opp hovedfiguren.
# Komponentboksene brukes bare til plassering og mål. Ingen originalkontur klipper nytegningen.
def pieces(im):
 a=np.array(im);lab,n=ndi.label(a[:,:,3]>=128);parts=[]
 for i,s in enumerate(ndi.find_objects(lab)):
  size=int((lab[s]==i+1).sum())
  if size<100: continue
  m=ndi.binary_dilation(lab==i+1,iterations=3)
  aa=a.copy();aa[:,:,3]=np.where(m,aa[:,:,3],0);aa[aa[:,:,3]==0]=0
  parts.append((size,Image.fromarray(aa)))
 return [p for size,p in sorted(parts,key=lambda v:-v[0])]

# Nytegnet blå flate fra Sams jakke. Bevarer kildearkets små, separate blå prikker.
blue=clean(Image.open(G/'exec-e8663a2e-e13c-40ed-b404-aacf50780357.png')).crop((192,280,196,284))
blue.save(R/'nytegnet-blaa-prikk.png')
for job in ['fig116_02','fig116_03','fig116_04']:
 data=json.load(open(f'jobber/{job}/jobb.json'));original=np.array(Image.open(f'jobber/{job}/original_1x.png').convert('RGB'))
 out=Image.new('RGBA',(1536,1024));raw=Image.open(R/f'{job}-raa01.png').convert('RGBA')
 if job=='fig116_02':crops=[(35,35,610,365)]
 elif job=='fig116_03':crops=[(30,40,540,350),(550,40,1070,350),(30,358,525,658),(548,358,1065,658),(1130,358,1465,661),(45,660,405,980),(430,660,780,980),(830,660,1120,980),(1228,660,1470,980)]
 else:crops=[(70,130,370,487),(445,138,756,489),(800,140,1110,488),(1170,144,1490,490),(60,600,414,942),(421,571,791,943),(794,583,1167,941),(1184,572,1488,945)]
 for c,crop in zip(data['ruter'],crops):
  x,y,x1,y1=c['synlig'];om=np.abs(original[y:y1,x:x1].astype(int)-np.array(data['bakgrunn'])).sum(2)>24
  lab,n=ndi.label(om);comps=[];dots=[]
  for i,s in enumerate(ndi.find_objects(lab)):
   size=int((lab[s]==i+1).sum());b=[(16+x+s[1].start)*4,(8+y+s[0].start)*4,(16+x+s[1].stop)*4,(8+y+s[0].stop)*4]
   (dots if size==1 else comps).append((size,b))
  source=pieces(raw.crop(crop));comps.sort(key=lambda v:-v[0])
  assert len(source)==len(comps),(job,c['bilde'],len(source),len(comps))
  for im,(_,b) in zip(source,comps):out.alpha_composite(fit(im,b),b[:2])
  for _,b in dots:out.alpha_composite(blue,b[:2])
 out.save(f'jobber/{job}/resultat.png')

# Siste bildeforsøk reparerer skjøtene. Bytt kun området som var dekket av gammelt hode/hatt,
# inkludert smale ermeflater som først blir synlige når den gamle hattebremmen er borte.
raw=clean(Image.open(G/'exec-4ba8e94b-52a2-40b1-a80c-42a815eda08e.png'))
raw.save(R/'fig247_10-hoder-raa04.png')
patch=raw.resize((400,144),Image.Resampling.LANCZOS)
base=Image.open(R/'fig247_10-for-retur.png').convert('RGBA');m=Image.new('L',(400,144));d=ImageDraw.Draw(m)
d.polygon([(70,18),(112,18),(120,48),(136,58),(135,106),(117,119),(80,127),(44,116),(11,97),(7,77),(28,65),(37,55),(63,50)],fill=255)
d.polygon([(271,27),(310,27),(321,57),(342,64),(352,104),(330,125),(296,136),(261,125),(233,113),(226,97),(231,83),(260,72)],fill=255)
# Lett antialias på den manuelle komposisjonsgrensen, ikke på figurens originalomriss.
from PIL import ImageFilter
m=m.filter(ImageFilter.GaussianBlur(0.5));base.paste(patch,(496,208),m)
base=clean(base);base.save('jobber/fig247_10/resultat.png')
im=base.crop((496,208,896,352));bg=Image.new('RGBA',im.size,(210,210,210,255));bg.alpha_composite(im);bg.convert('RGB').resize((1200,432)).save(R/'247-hoder-slutt-graa.png')

# Én synlig alligatorøyne i riktig profil. Tidligere forsøk hadde to øyne.
headraw=clean(Image.open(G/'exec-3ac30cc6-a50d-4beb-b2c6-07b4caf2deb3.png'));headraw.save(R/'alligator-hode-raa01.png')
for job in ['fig116_02','fig116_03']:
 out=Image.open(f'jobber/{job}/resultat.png').convert('RGBA');data=json.load(open(f'jobber/{job}/jobb.json'))
 for c in data['ruter']:
  if job=='fig116_03' and c['rute']>1932:continue
  x0,y0,x1,y1=c['synlig'];bx=(16+x0+12)*4;by=(8+y1-9)*4
  # Fjern bare grønt, sort og øyehøylys i det gamle hodefeltet, aldri Sams føtter.
  a=np.array(out);box=(bx-4,by-4,bx+100,by+36);x,y,xx,yy=box;sub=a[y:yy,x:xx];rgb=sub[:,:,:3].astype(float)
  green=(rgb[:,:,1]>rgb[:,:,0]*1.18)&(rgb[:,:,1]>rgb[:,:,2]*.8)&(sub[:,:,3]>64)
  m=ndi.binary_fill_holes(green);m=ndi.binary_dilation(m,iterations=1)
  brown=(rgb[:,:,0]>rgb[:,:,1]*1.2)&(rgb[:,:,1]>rgb[:,:,2]*1.2)
  m&=~brown;sub[m]=0;out=Image.fromarray(a)
  part=fit(headraw,(bx,by,bx+100,by+36));out.alpha_composite(part,(bx,by))
 out=clean(out);out.save(f'jobber/{job}/resultat.png')

# Bevar hele den tidligere leveransen byte for byte utenfor de to redigerte hodefeltene.
old=np.array(Image.open(R/'fig247_10-for-retur.png').convert('RGBA'));new=np.array(Image.open('jobber/fig247_10/resultat.png').convert('RGBA'))
allow=Image.new('L',(400,144));dd=ImageDraw.Draw(allow)
dd.polygon([(70,18),(112,18),(120,48),(136,58),(135,106),(117,119),(80,127),(44,116),(11,97),(7,77),(28,65),(37,55),(63,50)],fill=255)
dd.polygon([(271,27),(310,27),(321,57),(342,64),(352,104),(330,125),(296,136),(261,125),(233,113),(226,97),(231,83),(260,72)],fill=255)
allowed=np.zeros(old.shape[:2],bool);allowed[208:352,496:896]=np.array(allow.filter(ImageFilter.GaussianBlur(.5)))>0
rgb=old[:,:,:3].astype(float)
green=(rgb[:,:,1]>rgb[:,:,0]*1.3)&(rgb[:,:,1]>rgb[:,:,2]*1.15)&(old[:,:,3]>128)
allowed[green]=False
# Håndhud før ansiktshøyden tilhører alltid det bevarte grepet.
for box in [(496,208,696,270),(704,208,896,282)]:
 x,y,xx,yy=box;part=rgb[y:yy,x:xx];hand=(part[:,:,0]>part[:,:,1]*1.2)&(part[:,:,1]>part[:,:,2]*1.2)&(old[y:yy,x:xx,3]>128)
 allowed[y:yy,x:xx]&=~hand
final=old.copy();final[allowed]=new[allowed];Image.fromarray(final).save('jobber/fig247_10/resultat.png')
