from pathlib import Path
from datetime import datetime,timezone
from PIL import Image
from smhd.myk import CORE,GOOD_IOU,GOOD_COVER,_iou
import numpy as np,json,hashlib,subprocess,shutil,re
P=Path('/home/tom/Sam-Max-HD');A=P/'work/.gpt-gren';O=Path(__file__).resolve().parent;R=A/'rapporter'/O.name;M=P/'mods/gpt';C=O/'mod-sam2963697'
read=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def git(w,*a):return subprocess.check_output(['git',*a],cwd=w,text=True).strip()
def inv(d):return{p.relative_to(d).as_posix():sha(p)for p in d.rglob('*')if p.is_file()}
assert not R.exists()and not C.exists();assert(CORE,GOOD_IOU,GOOD_COVER)==(128,.6,.8)
prev=read(A/'rapporter/sam293-siste-fryserrute-20261022/start.json');files=read(A/'rapporter/felles-release-20261022-fryserark/moddfiler-3695.json');assert len(files)==21939 and inv(M)==files
protected=prev['beskyttede'].copy();assert len(protected)==1432 and all(sha(A/f)==h for f,h in protected.items())
for jid in ['fig296_01','fig296_02']:
 for f in ['referanse.png','original_1x.png','prompt.txt','jobb.json']:
  p=A/'jobber'/jid/f;protected[p.relative_to(A).as_posix()]=sha(p)
for f,h in read(O/'kildeplan.json')['beskyttede'].items():assert sha(A/'jobber/fig296_01'/f)==h
stash=git(P,'stash','list','--format=%H').splitlines();assert stash==prev['stash'];assert not git(P,'status','--porcelain')and not git(A,'status','--porcelain');remote={line.split()[1].removeprefix('refs/heads/'):line.split()[0]for line in git(P,'ls-remote','origin','refs/heads/main','refs/heads/gpt-arbeid','refs/heads/hd-mod').splitlines()};assert remote==dict(main='46663bf46ce6d8eabcd0c76db9b582d882e86c44',**{'gpt-arbeid':'ad82c5ca1f34dfb99f43499b0eb2be22df4552db','hd-mod':'f0f7b641177cec8661d7c0cbf68c5faef9eb31f6'});assert not read(A/'rapporter/felles-release-20261022-fryserark/bygg-startet.json')['native_frosset']
R.mkdir();save(R/'start.json',dict(tid_utc=datetime.now(timezone.utc).isoformat(),remote=remote,native=3695,pakker_native=3695,hele_figurjobber=506,total_figurjobber=1758,filer=files,beskyttede=protected,stash=stash,kildeplan_start_utc=read(O/'kildeplan.json')['start_utc'],snapshot_bekrefter_tidligere_1432_og8_nye_kilder=True))
for p in O.iterdir():
 if p.name in ['mod-sam2963697']:continue
 if p.is_dir():shutil.copytree(p,R/p.name)
 else:shutil.copy2(p,R/p.name)
CTX=P/'out/sam296-kilde-20261022';D=R/'kildekontekst';D.mkdir();proof=read(CTX/'bevis/kilde296-start1.json');assert proof['exit']==0 and proof['native_antall']==3695 and len(proof['tegninger'])==11
for name,e in proof['tegninger'].items():
 if not 1920<=e['cel']<=1928:continue
 f=Path(e['fil']);assert sha(f)==e['sha256'];shutil.copy2(f,D/f.name);flat=f.with_name(f.stem+'_flat.png');shutil.copy2(flat,D/flat.name)
for f in ['kilde296-start1.json','kilde296-start1.log.gz']:shutil.copy2(CTX/'bevis'/f,D/f)
shutil.copy2(CTX/'kilde-motor.py',D/'kilde-motor.py.txt')
selected=[('S006','prototype-v2.png',1920),('S013','prototype-v4.png',1922)];chosen=[];mapping=[];board=Image.new('RGBA',(1536,1024));J=A/'jobber/fig296_01';job=read(J/'jobb.json');assert not(J/'resultat.png').exists();assert len(list(A.glob('jobber/fig*/resultat.png')))==506
for call,fn,cel in selected:
 K=R/'kall'/call;q=read(K/'sluttkandidat-kontroll.json');assert q['teknisk_og_fester_bestatt'];im=Image.open(K/fn).convert('RGBA');assert sha(K/fn)==q['native_sha256'];t=next(t for t in job['ruter']if t['rute']==cel);x,y,w,h=t['rekt'];assert im.size==(w*4+16,h*4+16);src=Image.open(P/f'work/extract/costumes/costume296_{cel}.png').convert('RGBA');assert src.size==(w,h);iou,cov=_iou(np.array(im)[:,:,3]>=CORE,np.repeat(np.repeat(np.array(src)[:,:,3]>0,4,0),4,1),-8,-8);assert iou>=GOOD_IOU and cov>=GOOD_COVER
 q['visuelt_sett']=True;save(K/'sluttkandidat-kontroll.json',q);entry=dict(bilde=t['bilde'],jobb='fig296_01',canonical=t['bilde'],kostyme=296,rute=cel,lag=t['lag'],fil='costumes/'+t['bilde']+'_hd.png',prototype=(K/fn).relative_to(A).as_posix(),sha256=sha(K/fn),prototype_sha256=sha(K/fn),kall=call,snitt_union=iou,dekning=cov,native_hel_plassering_HD=q['hel_plassering_HD'],egen_alfa=True,originalmaske=False,originalfragmenter=False,prototype_visuelt_sett=True,motorobservert=False,publisert=False,Tom_godkjent=False,Claude_godkjent=False);chosen.append(entry)
 dx,dy=(job['plassering'][0]+x)*4-8,(job['plassering'][1]+y)*4-8;layer=Image.new('RGBA',board.size);layer.alpha_composite(im,(dx,dy));assert not((np.array(board)[:,:,3]>0)&(np.array(layer)[:,:,3]>0)).any();board.alpha_composite(layer);ys,xs=np.where(np.array(im)[:,:,3]>=CORE);mapping.append(dict(**entry,rect=[dx+int(xs.min()),dy+int(ys.min()),int(np.ptp(xs)+1),int(np.ptp(ys)+1)],native_ok=True,native_marg_hd=8))
board.save(R/'fig296_01-delresultat.png');digest=sha(R/'fig296_01-delresultat.png');save(R/'rutekart-fig296_01.json',{'fig296_01':dict(sha256_resultat=digest,ruter=mapping)});missing=[e['bilde']for e in job['ruter']if e['rute']not in[1920,1922]];assert len(missing)==7
D=O/'ark/fig296_01';D.mkdir(parents=True)
for f in ['referanse.png','original_1x.png','prompt.txt','jobb.json']:shutil.copy2(J/f,D/f)
board.save(D/'resultat.png');test=subprocess.run([str(P/'.venv/bin/python'),str(A/'verktoy/sjekk_leveranse.py'),str(D/'resultat.png')],cwd=A,text=True,capture_output=True);log=test.stdout+test.stderr;(R/'fig296_01-egenkontroll.txt').write_text(log);errors=re.findall(r'^FEIL\s+(costume\d+_\d+):',log,re.M);assert not set(errors)&{e['bilde']for e in chosen}and set(errors)<=set(missing),log
partial=dict(jobb='fig296_01',resultat='rapporter/'+R.name+'/fig296_01-delresultat.png',sha256=digest,ruter=2,nye_ruter=2,tidligere_ruter=0,rutekart='rapporter/'+R.name+'/rutekart-fig296_01.json',laget=True,levert=False,delvis=True,mangler=missing,egenkontrollert=True,visuelt_kontrollert=True,native_mottatt=False,motorobservert=False,publisert=False,i_fellespakke=False,godkjent_av_Tom=False,claude_kontroll=False)
G=O/'diagnostisk-gren';shutil.copytree(D,G/'jobber/fig296_01');GR=G/'rapporter'/R.name;GR.mkdir(parents=True);shutil.copy2(R/'rutekart-fig296_01.json',GR/'rutekart-fig296_01.json');shutil.copy2(R/'fig296_01-delresultat.png',GR/'fig296_01-delresultat.png');save(GR/'fremdrift.json',dict(leveranser=[partial],diagnostisk_delark_ikke_levert=True));auto=O/'automatisk-mottak';subprocess.run([str(P/'.venv/bin/smhd'),'myke-figurer','--gren',str(G),'--extract',str(P/'work/extract'),'--ut',str(auto),'--jobb','fig296_01','--forhandsvisning',''],cwd=P,check=True);rep=read(auto/'myke.json');save(R/'automatisk-mottak.json',rep)
for e in chosen:assert rep['ark']['fig296_01']['ruter'][e['bilde']]['status']=='ok'
assert rep['ruter_ok']==2 and rep['ruter_mangler']==7
shutil.copytree(M,C)
for e in chosen:assert not(C/e['fil']).exists();shutil.copy2(A/e['prototype'],C/e['fil']);assert sha(C/e['fil'])==e['sha256']
meta=read(C/'mod.json');assert meta['costume_cels']==3695;meta['costume_cels']=3697;save(C/'mod.json',meta);newfiles=inv(C);assert len(newfiles)==21941 and set(newfiles)-set(files)=={e['fil']for e in chosen}and{f for f,h in files.items()if newfiles[f]!=h}=={'mod.json'}
save(R/'kandidatfilhash.json',newfiles);save(R/'egen-native.json',dict(ruter=chosen,nye_native=2,native_totalt=3697,kandidat=str(C),fast_4x=True,marg_original=[2,2],egen_alfa=True,originalmaske=False,originalfragmenter=False,diagnostisk_eksport_ikke_importert=True,tidligere_filer_bevart=21939,filer=21941,png=sum(f.endswith('.png')for f in newfiles)));partial['native_mottatt']=True
calls=[]
for K in sorted((R/'kall').iterdir()):
 q=read(K/'verktøyresultat.json');a=read(K/'args.json');entry=dict(kall=K.name,raa_sha256=sha(K/'raa.png'),prompt_sha256=sha(K/'prompt-faktisk.txt'),faktiske_argumenter_sha256=sha(K/'args.json'),referanser=[dict(fil=f,sha256=sha(Path(f)))for f in a['referenced_image_paths']],valgt=K.name in['S006','S013'],status='VALGT_DELLEVERANSE'if K.name in['S006','S013']else'KVALITETSRETUR');calls.append(entry);q.update(status=entry['status'],visuell_native_kontroll=K.name in['S006','S013'],levert=False,native_mottatt=K.name in['S006','S013'],publisert=False);save(K/'verktøyresultat.json',q)
assert len(calls)==14;save(R/'alle-kall.json',calls);save(R/'kvalitetsreturer.json',[e for e in calls if not e['valgt']]);save(R/'delark-kontroll.json',dict(hele_arkets_egenkontroll=test.returncode,hele_arket_ferdig=False,produserte_FEIL=0,ruter=2,manglende_ikke_leverte_maal=missing,FEIL_kun_tomme_maal=errors,original_jobb_json_bevart=sha(D/'jobb.json')==sha(J/'jobb.json'),terskler_uendret=True));save(R/'fragmentvern.json',dict(nye_egne_hele_rutetegninger=2,originalfragmenter_i_kandidat=False,diagnostisk_eksport_ikke_importert=True,native_fra_egen_prototype_sha=True,porter=dict(CORE=128,IoU=.6,dekning=.8,affin_min=.88,affin_maks=1.12),hel_ark_levert=False))
save(R/'fremdrift.json',dict(leveranser=[],delvise_leveranser=[partial],nye_jobber_levert=0,nye_native=2,native_totalt=3697,grunnlag_native=3695,innebygde_bildekall=14,vellykkede_bildekall=14,avviste_bildekall=0,kvalitetsreturer=12,ulike_hele_egne_malerier_valgt=2,hele_rgba_aliasmal=0,hele_figurjobber_med_resultat=506,total_figurjobber=1758,gjenstar=1252,laget_valgte_ruter=2,egenkontrollert=2,native_mottatt=2,visuelt_sett=2,motorobservert=0,publisert=0,Tom_godkjent=0,Claude_godkjent=0,pakker_native=3695,pakker_mangler_native=2,native_frosset=False))
save(R/'egen-visuell-plan.json',dict(visuelt_sett=True,ark=[dict(fil='fig296_01-delresultat.png',sha256=digest,visuelt_sett=False)],ruter=[dict(kall=c,fil='kall/'+c+'/sluttkandidat-visuell.png',sha256=sha(R/'kall'/c/'sluttkandidat-visuell.png'),visuelt_sett=True)for c in['S006','S013']]))
save(R/'kontrollstarter.json',dict(ikke_bestatte_starter=[dict(hjelper='rens-grasole.py',feil='SyntaxError: and450 uten mellomrom, før filskriving. Rettet og kjørt på nytt, første start regnes ikke bestått.')],ingen_motor_eller_pipelineendring=True))
shutil.copy2(__file__,R/'start-og-lever.py.txt');print('Kandidat3697,2/9 delruter,2 automatiskOK/7 mangler.14 råbilder og prompter bevart. Beskyttede',len(protected),'stash3 uendret.')
