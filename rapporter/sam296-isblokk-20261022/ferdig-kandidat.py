from pathlib import Path
from PIL import Image,ImageFilter,ImageDraw
from scipy import ndimage as nd
import numpy as np,json,hashlib,math
O=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def color(a,cls):
 r,g,b=a[:,:,:3].astype(float).transpose(2,0,1);o=a[:,:,3]>128
 if cls=='hud':return o&(r>160)&(g<175)&(b<155)&(b>.65*g)&(r>1.3*g)
 if cls=='varm':return o&(r>g*1.2)&(g>b*1.15)
 return o&(np.maximum.reduce([r,g,b])<100)&(np.maximum.reduce([r,g,b])-np.minimum.reduce([r,g,b])<40)
plans={'S006':dict(shift=[0,1],anchors=[('varm-ovre','varm',[8,8,24,68]),('varm-midt','varm',[8,150,28,174]),('varm-nedre','varm',[8,174,24,224]),('svart-fragment','mork',[8,80,28,116])]),'S008':dict(shift=[0,-2],anchors=[('ovre-morkt-felt','mork',[8,8,44,64]),('venstre-morkt-felt','mork',[8,88,28,114]),('hoyre-morkt-felt','mork',[36,88,76,136]),('nedre-fot','mork',[8,248,48,296])])}
for name,plan in plans.items():
 K=O/'kall'/name;q=json.loads((K/'verktøyresultat.json').read_text());assert q['tekniske_porter_bestatt'];own=Image.open(K/'egen-renset.png');aa=np.array(own)[:,:,3].copy();rgb=own.convert('RGB').filter(ImageFilter.ModeFilter(5));own=rgb.convert('RGBA');own.putalpha(Image.fromarray(aa));assert np.array_equal(np.array(own)[:,:,3],aa);own.save(K/'egen-RGB-modusrens-v2.png')
 fx,fy=q['skala'];x0,y0,_,_=q['egen_core_bbox'];proto=own.transform(tuple(q['native_maal']),Image.Transform.AFFINE,(1/fx,0,x0-8/fx,0,1/fy,y0-8/fy),Image.Resampling.BICUBIC);a=np.array(proto);core=a[:,:,3]>=128;a[nd.distance_transform_edt(~core)>1.5]=0;proto=Image.fromarray(a);shifted=Image.new('RGBA',proto.size);shifted.alpha_composite(proto,tuple(plan['shift']));assert np.array(shifted)[:,:,3].sum()==a[:,:,3].sum();proto=shifted;a=np.array(proto);proto.save(K/'prototype-v2.png');src=Image.open(K/'original-native-kontroll.png');s=np.array(src);sm=s[:,:,3]>=128;cm=a[:,:,3]>=128;iou=float((sm&cm).sum()/(sm|cm).sum());cov=float((sm&cm).sum()/sm.sum());anchors=[]
 for label,cls,rect in plan['anchors']:
  x,y,xx,yy=rect;reg=np.zeros(sm.shape,bool);reg[y:yy,x:xx]=True;values=[]
  for v in [s,a]:
   ys,xs=np.where(color(v,cls)&reg);assert len(xs)>0;(values.append(dict(areal=len(xs),xy=[float(xs.mean()),float(ys.mean())])))
  anchors.append(dict(navn=label,klasse=cls,fast_kilde_ROI_HD=rect,original=values[0],egen=values[1],avvik_HD=math.dist(values[0]['xy'],values[1]['xy'])))
 skin=color(s,'hud');skinown=color(a,'hud');yy,xx=np.where(skin[9::4,9::4]);pts=np.array([9.5+yy*4,9.5+xx*4]);dist=nd.distance_transform_edt(~skinown);ds=nd.map_coordinates(dist,pts,order=1)if len(xx)else np.array([]);mx=float(ds.max())if len(ds)else 0
 passed=iou>=.6 and cov>=.8 and mx<=3 and all(v['avvik_HD']<=3 for v in anchors)
 rec=dict(kall=name,rute=q['rute'],native_sha256=sha(K/'prototype-v2.png'),native_maal=list(proto.size),egen_raa_sha256=q['raw_sha256'],IoU=iou,dekning=cov,fast_4x=True,egen_alfa=True,hel_plassering_HD=plan['shift'],fester=anchors,kildehudpunkter=len(xx),maks_hudpunkt_HD=mx,port_HD=3,teknisk_og_fester_bestatt=passed,RGB_rens='ModeFilter5 på egen RGB før helskala;alfa identisk,ingen originalgeometri',egen_RGB_alfa_identisk=True,originalmaske=False,originalfragmenter=False,lokal_flytting=False,visuelt_sett=False,native_mottatt=False,publisert=False)
 (K/'sluttkandidat-kontroll.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
 board=Image.new('RGB',(max(800,(proto.width*2+40)*2),max(660,proto.height*2+45)),'#304050');d=ImageDraw.Draw(board)
 for i,(v,label)in enumerate([(src,'Original 4x, kun kontroll'),(proto,name+' RGB-rens og helplassering v2')]):
  bg=Image.new('RGBA',v.size,'#87959e');bg.alpha_composite(v);board.paste(bg.convert('RGB').resize((v.width*2,v.height*2),Image.Resampling.NEAREST),(12+i*(board.width//2),34));d.text((12+i*(board.width//2),10),label,fill='white')
 board.save(K/'sluttkandidat-visuell.png');print(name,'pass',passed,'IoU',iou,'hud',mx,'fester',[(v['navn'],round(v['avvik_HD'],3))for v in anchors])
