exec(Path('rapporter/produksjon-20261016/klargjor.py').read_text().split('rows={}')[0])
from scipy import ndimage as ndi

def isred(a):
 r,g,b=[a[:,:,k].astype(float) for k in range(3)]
 return (r>80)&(g<25)&(b<25)&(r>g*5)&(r>b*5)
def parts(a,mask):
 labels,n=ndi.label(mask);result=[]
 for k,s in enumerate(ndi.find_objects(labels),1):
  yy,xx=s;component=labels==k
  if component.sum()<2: continue
  aa=a.copy();aa[~component]=0
  result.append(Image.fromarray(aa).crop((xx.start-2,yy.start-2,xx.stop+2,yy.stop+2)))
 return result
atlas=np.array(Image.open(R/'fig249_07-raa.png').convert('RGBA'));redparts=parts(atlas,isred(atlas)&(atlas[:,:,3]>128))
records={}
for job in ['fig249_06','fig249_07','fig249_08']:
 p=Path('jobber')/job;j=json.loads((p/'jobb.json').read_text());orig=np.array(Image.open(p/'original_1x.png').convert('RGB'));raw=Image.open(R/(job+'-raa.png')).convert('RGBA');out=Image.new('RGBA',(1536,1024));records[job]=[]
 for c,cut in zip(j['ruter'],CROPS[job]):
  x,y,xx,yy=c['synlig'];sub=orig[y:yy,x:xx];m=np.any(sub!=j['bakgrunn'],axis=2);red=isred(sub)&m
  om=m&~red;ys,xs=np.where(om);target=[(16+x+int(xs.min()))*4,(8+y+int(ys.min()))*4,int(xs.max()-xs.min()+1)*4,int(ys.max()-ys.min()+1)*4]
  source_cut = CROPS[job][4] if job=='fig249_06' and c['rute'] in [163,164,165] else CROPS[job][8] if job=='fig249_06' and c['rute'] in [167,168,169] else cut
  part=np.array(raw.crop(source_cut));rm=isred(part)&(part[:,:,3]>=128)
  # The heart is held in the connected main figure for the first seven cels.
  split=job!='fig249_06' or c['rute']>=167
  if not split:
   place(out,Image.fromarray(part),[(16+x)*4,(8+y)*4,(xx-x)*4,(yy-y)*4]);continue
  part[ndi.binary_dilation(ndi.binary_fill_holes(rm),iterations=5)]=0
  labs,count=ndi.label(part[:,:,3]>128)
  sizes=np.bincount(labs.ravel());sizes[0]=0;main=labs==sizes.argmax()
  part[~ndi.binary_dilation(main,iterations=3)]=0
  place(out,Image.fromarray(part),target)
  lab,n=ndi.label(red);droplets=[]
  for k,s in enumerate(ndi.find_objects(lab),1):
   sy,sx=s;w=(sx.stop-sx.start)*4;h=(sy.stop-sy.start)*4;dx=(16+x+sx.start)*4;dy=(8+y+sy.start)*4
   # All parts are generated artwork. Match each original droplet's bounding box independently.
   def score(im):
    b=box(im);candidate=im.crop(b).resize((w,h),Image.Resampling.LANCZOS);draw=np.array(candidate)[:,:,3]>=128;expected=np.repeat(np.repeat(lab[sy,sx]==k,4,0),4,1);return -float((draw&expected).sum()/max(1,(draw|expected).sum()))
   selected=min(redparts,key=score);place(out,selected,[dx,dy,w,h]);droplets.append([dx,dy,w,h])
  records[job].append({'bilde':c['bilde'],'kropp':target,'rode_deler':droplets})
 out.save(p/'resultat.png')
 bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out);bg.convert('RGB').save(R/(job+'-graa.png'))
 res=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True);(R/(job+'-egenkontroll.txt')).write_text(res.stdout+res.stderr);print(res.stdout)
(R/'delplassering.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
