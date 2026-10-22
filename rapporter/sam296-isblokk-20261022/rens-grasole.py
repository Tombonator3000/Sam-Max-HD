from pathlib import Path
from PIL import Image
from scipy import ndimage as nd
import numpy as np,json,hashlib
O=Path(__file__).resolve().parent;K=O/'kall/S013';q=json.loads((K/'verktøyresultat.json').read_text());a=np.array(Image.open(K/'egen-renset.png'));r,g,b=a[:,:,:3].astype(float).transpose(2,0,1)
# Den egenmalte høyre mørke delen har brun såle. Originalen har grå indeksfarge71.
# Velg hele egen RGB-komponent, aldri originalens geometri eller pikselmaske.
warm=(a[:,:,3]>0)&(r>20)&(r<130)&(r>g*1.5)&(g>b*1.3);labels,n=nd.label(warm,np.ones((3,3)));roi=np.zeros(warm.shape,bool);roi[457:547,606:685]=True;ids,counts=np.unique(labels[roi&warm],return_counts=True);assert len(ids);label=int(ids[np.argmax(counts)]);mask=labels==label;yy,xx=np.where(mask);bb=[int(xx.min()),int(yy.min()),int(xx.max()+1),int(yy.max()+1)];assert 600<=bb[0]<bb[2]<=690 and 450<=bb[1]<bb[3]<=550,bb;assert mask.sum()>500
alpha=a[:,:,3].copy();a[mask,:3]=[71,71,71];assert np.array_equal(a[:,:,3],alpha);Image.fromarray(a).save(K/'egen-RGB-grasole.png');fx,fy=q['skala'];x0,y0,_,_=q['egen_core_bbox'];im=Image.fromarray(a).transform(tuple(q['native_maal']),Image.Transform.AFFINE,(1/fx,0,x0-8/fx,0,1/fy,y0-8/fy),Image.Resampling.BICUBIC);aa=np.array(im);core=aa[:,:,3]>=128;aa[nd.distance_transform_edt(~core)>1.5]=0;Image.fromarray(aa).save(K/'prototype-rgb-grasole.png')
rec=dict(type='egen_brun_soleskygge_til_kildegraa',kilde_RGB=[71,71,71],kildebevis='Original1922 i regionx48..76,y92..132 har144 grå71-piksler og448 svarte;egen brun51,19,0 er ikke kildefargen i sålen',egen_RAA_RGB_maske_sha256=hashlib.sha256(mask.tobytes()).hexdigest(),egen_komponent_bbox=bb,piksler=int(mask.sum()),alfa_identisk=True,geometri_identisk=True,ingen_originalmaske=True,ingen_originalfragmenter=True,ingen_lokal_flytting=True);(K/'egen-graasole-rens.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n');print(rec)
