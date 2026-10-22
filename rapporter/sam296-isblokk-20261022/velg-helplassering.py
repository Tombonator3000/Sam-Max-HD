from pathlib import Path
from PIL import Image,ImageDraw
from scipy import ndimage as nd
import numpy as np,json,math,sys,hashlib
O=Path(__file__).resolve().parent;K=O/'kall'/sys.argv[1];q=json.loads((K/'verktøyresultat.json').read_text());assert q['rute']==1922
a0=np.array(Image.open(K/(sys.argv[2] if len(sys.argv)>2 else 'prototype-under-kontroll.png')));s=np.array(Image.open(K/'original-native-kontroll.png'));plans=json.loads((O/'kall/S008/sluttkandidat-kontroll.json').read_text())['fester'];version=sys.argv[3] if len(sys.argv)>3 else 'v3';prototype=K/('prototype-'+version+'.png')
def mask(v,cls):
 r,g,b=v[:,:,:3].astype(float).transpose(2,0,1);o=v[:,:,3]>128
 if cls=='hud':return o&(r>160)&(g<175)&(b<155)&(b>.65*g)&(r>1.3*g)
 return o&(np.maximum.reduce([r,g,b])<100)&(np.maximum.reduce([r,g,b])-np.minimum.reduce([r,g,b])<40)
yy,xx=np.where(mask(s,'hud')[9::4,9::4]);pts=np.array([9.5+yy*4,9.5+xx*4]);rows=[]
for dy in range(-3,4):
 for dx in range(-3,4):
  im=Image.new('RGBA',Image.fromarray(a0).size);im.alpha_composite(Image.fromarray(a0),(dx,dy));a=np.array(im);fs=[]
  for e in plans:
   x,y,xx,yy=e['fast_kilde_ROI_HD'];reg=np.zeros(a.shape[:2],bool);reg[y:yy,x:xx]=True;ys,xs=np.where(mask(a,'mork')&reg);xy=[float(xs.mean()),float(ys.mean())];fs.append(dict(navn=e['navn'],avvik_HD=math.dist(xy,e['original']['xy']),egen_midt=xy,kilde_midt=e['original']['xy'],fast_kilde_ROI_HD=e['fast_kilde_ROI_HD']))
  ds=nd.map_coordinates(nd.distance_transform_edt(~mask(a,'hud')),pts,order=1);mx=max(float(ds.max()),*(e['avvik_HD']for e in fs));sm=s[:,:,3]>=128;cm=a[:,:,3]>=128;iou=float((sm&cm).sum()/(sm|cm).sum());cov=float((sm&cm).sum()/sm.sum());rows.append(dict(shift=[dx,dy],maks=mx,maks_hud=float(ds.max()),fester=fs,IoU=iou,dekning=cov))
rows.sort(key=lambda e:e['maks']);(K/('helplassering-alle-fester-'+version+'.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n');best=rows[0];im=Image.new('RGBA',Image.fromarray(a0).size);im.alpha_composite(Image.fromarray(a0),tuple(best['shift']));assert np.array(im)[:,:,3].sum()==a0[:,:,3].sum();im.save(prototype);passed=q['tekniske_porter_bestatt']and best['maks']<=3 and best['IoU']>=.6 and best['dekning']>=.8;rec=dict(**best,kall=sys.argv[1],rute=1922,native_sha256=hashlib.sha256(prototype.read_bytes()).hexdigest(),native_fil=prototype.name,native_maal=list(im.size),teknisk_og_fester_bestatt=passed,visuelt_sett=False,originalmaske=False,originalfragmenter=False,lokal_flytting=False,egen_alfa=True,hel_plassering_HD=best['shift'],native_mottatt=False,publisert=False);(K/'sluttkandidat-kontroll.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
board=Image.new('RGB',(800,710),'#304050');d=ImageDraw.Draw(board)
for i,(v,label)in enumerate([(Image.fromarray(s),'Original 4x, kun kontroll'),(im,sys.argv[1]+' egen 4x, helplassering')]):
 bg=Image.new('RGBA',v.size,'#87959e');bg.alpha_composite(v);board.paste(bg.convert('RGB').resize((v.width*2,v.height*2),Image.Resampling.NEAREST),(12+i*400,34));d.text((12+i*400,10),label,fill='white')
board.save(K/'sluttkandidat-visuell.png');print(sys.argv[1],'pass',passed,json.dumps(best,ensure_ascii=False))
