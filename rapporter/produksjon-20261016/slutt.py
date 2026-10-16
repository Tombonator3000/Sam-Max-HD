from pathlib import Path
exec(Path('rapporter/produksjon-20261016/klargjor.py').read_text().split('rows={}')[0])
import shutil
for job in ['fig249_06','fig249_07']:shutil.copyfile(R/(job+'-kandidat.png'),Path('jobber')/job/'resultat.png')
raw=Image.open(R/'fig249_07-raa.png').convert('RGBA')
drop=raw.crop((625,30,675,115));puddle=raw.crop((540,915,585,930))
for name,part in [('draape',drop),('dam',puddle)]:
 a=np.array(part);a[a[:,:,3]<128]=0;part=Image.fromarray(a);part.save(R/(name+'-ren.png'))
drop=Image.open(R/'draape-ren.png');puddle=Image.open(R/'dam-ren.png');key=Image.open(R/'sam-cle-raa.png').convert('RGBA')
p=Path('jobber/fig249_08');j=json.loads((p/'jobb.json').read_text());orig=np.array(Image.open(p/'original_1x.png').convert('RGB'));out=Image.new('RGBA',(1536,1024))
from scipy import ndimage as ndi
for c in j['ruter']:
 x,y,xx,yy=c['synlig'];sub=orig[y:yy,x:xx];r,g,b=[sub[:,:,k].astype(float) for k in range(3)];m=np.any(sub!=j['bakgrunn'],2);red=(r>80)&(g<65)&(b<65)&(r>g*2.5)&(r>b*2.5)&m;body=m&~red;ys,xs=np.where(body);target=[(16+x+int(xs.min()))*4,(8+y+int(ys.min()))*4,int(xs.max()-xs.min()+1)*4,int(ys.max()-ys.min()+1)*4];place(out,key,target)
 lab,n=ndi.label(red)
 for k,s in enumerate(ndi.find_objects(lab),1):
  sy,sx=s;w=(sx.stop-sx.start)*4;h=(sy.stop-sy.start)*4;target=[(16+x+sx.start)*4,(8+y+sy.start)*4,w,h];place(out,puddle if w>h*2 else drop,target)
out.save(p/'resultat.png')
for job in ['fig249_02','fig249_04','fig249_05','fig249_06','fig249_07','fig249_08']:
 p=Path('jobber')/job;out=Image.open(p/'resultat.png').convert('RGBA');bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out);bg.convert('RGB').save(R/(job+'-graa.png'))
 pair=Image.new('RGB',(3072,1024));pair.paste(Image.open(p/'referanse.png'),(0,0));pair.paste(bg.convert('RGB'),(1536,0));pair.resize((1536,512)).save(R/(job+'-sammenligning.png'))
 res=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True);(R/(job+'-egenkontroll.txt')).write_text(res.stdout+res.stderr);print(res.stdout);assert res.returncode<2,job
