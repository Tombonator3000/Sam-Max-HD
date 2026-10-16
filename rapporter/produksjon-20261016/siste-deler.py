from pathlib import Path
exec(Path('rapporter/produksjon-20261016/klargjor.py').read_text().split('rows={}')[0])
R=Path('rapporter/produksjon-20261016')
key=Image.open(G/'exec-0a9144c3-cffc-4174-94cb-b579c12088d3.png').convert('RGBA');key.save(R/'sam-cle-raa.png')
for job in ['fig249_07','fig249_08']:
 p=Path('jobber')/job;j=json.loads((p/'jobb.json').read_text());orig=np.array(Image.open(p/'original_1x.png').convert('RGB'));out=Image.open(p/'resultat.png').convert('RGBA');a=np.array(out)
 for c in j['ruter']:
  if c['rute']<175: continue
  x,y,xx,yy=c['synlig'];sub=orig[y:yy,x:xx];r,g,b=[sub[:,:,k].astype(float) for k in range(3)];m=np.any(sub!=j['bakgrunn'],2)&~((r>80)&(r>g*2)&(r>b*2));ys,xs=np.where(m);bx=(16+x+int(xs.min()))*4;by=(8+y+int(ys.min()))*4;w=int(xs.max()-xs.min()+1)*4;h=int(ys.max()-ys.min()+1)*4
  # Retain the separately placed red droplets. Replace only body pixels in this cel.
  win=a[(8+y)*4:(8+yy)*4,(16+x)*4:(16+xx)*4];rr,gg,bb=[win[:,:,k].astype(float) for k in range(3)];red=(rr>80)&(gg<65)&(bb<65)&(rr>gg*2.5)&(rr>bb*2.5);win[~red]=0
  out=Image.fromarray(a);place(out,key,[bx,by,w,h]);a=np.array(out)
 out.save(p/'resultat.png')
 bg=Image.new('RGBA',out.size,(128,128,128,255));bg.alpha_composite(out);bg.convert('RGB').save(R/(job+'-graa.png'))
 res=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True);(R/(job+'-egenkontroll.txt')).write_text(res.stdout+res.stderr);print(res.stdout)
p=Path('jobber/fig249_02');old=Image.open(R/'fig249_02-godkjent-foer.png').convert('RGBA');mouth=Image.open(G/'exec-67aa9367-eac4-45c0-bfcb-40e0c4edd23c.png').convert('RGBA');mouth.save(R/'munn-raa.png');a=np.array(old);a[668:732,64:136]=0;out=Image.fromarray(a);place(out,mouth,[80,684,40,32]);out.save(R/'fig249_02-kandidat.png');out.save(p/'resultat.png')
a0=np.array(old);a1=np.array(out);outside=np.ones(a0.shape[:2],bool);outside[668:732,64:136]=False;assert np.array_equal(a0[outside],a1[outside]);print('Seks gangruter byteidentiske utenfor munnvinduet')
j=json.loads((p/'jobb.json').read_text());orig=np.array(Image.open(p/'original_1x.png').convert('RGB'));mask=np.any(orig[163:171,4:14]!=j['bakgrunn'],2);mask=np.repeat(np.repeat(mask,4,0),4,1);draw=np.array(out)[684:716,80:120,3]>=128;print('Munn dekning',float((mask&draw).sum()/mask.sum()),'IoU',float((mask&draw).sum()/(mask|draw).sum()))
res=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True);(R/'fig249_02-egenkontroll.txt').write_text(res.stdout+res.stderr);print(res.stdout)
