"""Skriver analyseindekser og galleri. Ingen spillfiler eller produksjonsjobber endres."""
from pathlib import Path
import json,csv,re,hashlib,html,shutil
from collections import defaultdict,Counter
b=Path(__file__).resolve().parent;root=b.parents[3];meta=json.loads((b/'kostymer-originalmetadata.json').read_text());rooms=json.loads((b/'rom-originalmetadata.json').read_text());fig=json.loads((b/'figurer.json').read_text());sources=root/'work/skript'
assign=defaultdict(list)
for p in sorted(sources.rglob('*.txt')):
 actor='ukjent'
 for no,line in enumerate(p.read_text().splitlines(),1):
  m=re.search(r'actorOps.setCurActor\(([^)]+)\)',line)
  if m:actor=m[1]
  m=re.search(r'actorOps.setCostume\((\d+)\)',line)
  if m:assign[int(m[1])].append((str(p.relative_to(sources)),no,actor,line.strip()))
labels=defaultdict(set)
for f in fig:
 for cid in f['costumes']:labels[cid].add(f['name'])
for cid in [103,104,105]:labels[cid].add('Trixie, tilbakeblikk')
labels[107].add('Trixie sammen med Flambé, tilbakeblikk')
labels[108].add('Bruno og Trixie sammen, tilbakeblikk')
for cid in [237,239,243]:labels[cid].add('Bruno, eventuelt sammensatt med andre')
labels[264].add('Bigfoot-eldsten')
labels[254].add('Uidentifisert person, må avklares')
labels[219].add('Ressurs brukt av robotskuespiller 7, visuelt innhold må avklares')
labels[220].add('Sam med robot, sammensatt rute')
with (b/'kostymer-348.csv').open('w') as fh:
 w=csv.writer(fh,lineterminator="\n");w.writerow(['kostyme','identitet_eller_kobling','grunnlag','lagringsrom_ikke_nodvendigvis_bruksrom','ruter_med_bilde','tomme_ruter','lag','dekoderadvarsler','skriptreferanser','produksjonsklar'])
 for key,c in sorted(meta.items(),key=lambda x:int(x[0])):
  cid=int(key);name=' / '.join(sorted(labels[cid]));basis='originalark og skript, se figurnotater'
  if not name:
   actors={a[2] for a in assign[cid]}
   if actors=={'2'}:name='Ressurs på Sam-skuespiller 2, andre figurer kan være med';basis='statisk skriptkobling, ikke ferdig motivanalyse'
   elif actors=={'3'}:name='Ressurs på Max-skuespiller 3, andre figurer kan være med';basis='statisk skriptkobling, ikke ferdig motivanalyse'
   else:name='Uavklart';basis='skal ikke gis oppdiktet navn'
  w.writerow([cid,name,basis,c['room'],len(c['cels']),len(c['tomme_ruter']),','.join(map(str,sorted({x['lag'] for x in c['cels']}))),len(c['advarsler']),'; '.join(f'{a[0]}:{a[1]} actor={a[2]}' for a in assign[cid]),'nei'])
with (b/'rutekart-original.csv').open('w') as fh:
 w=csv.writer(fh,lineterminator="\n");w.writerow(['kostyme','rute','lag','kode','bredde','hoyde','rel_x','rel_y','move_x','move_y','identisk_bilde_som','tomhendelse','kilde'])
 for key,c in meta.items():
  for x in c['cels']:w.writerow([key,x['cel'],x['lag'],x['kode'],x['w'],x['h'],x['rel_x'],x['rel_y'],x['move_x'],x['move_y'],x.get('samme_bilde_som',''),False,f'costume{int(key):03d}_{x["cel"]:03d}.png'])
  for cid in c['tomme_ruter']:w.writerow([key,cid,cid//128,cid%128,0,0,'','','','','',True,'ingen PNG'])
with (b/'skript-kostymekoblinger.tsv').open('w') as fh:
 w=csv.writer(fh,delimiter='\t',lineterminator='\n');w.writerow(['kostyme','skript','linje','skuespilleruttrykk','kommando'])
 for cid,entries in sorted(assign.items()):
  for p,no,actor,line in entries:w.writerow([cid,p,no,actor,line])
objnames={}
for line in (b/'objektnavn-original.tsv').read_text().splitlines():
 if line.startswith('#'):continue
 parts=line.split('\t')
 if len(parts)>=4:objnames[(int(parts[0]),int(parts[1]))]=parts[3]
with (b/'objektbilder-959.csv').open('w') as fh:
 w=csv.writer(fh,lineterminator="\n");w.writerow(['rom','objekt_id','tilstand_hex','internt_originalnavn','format','x','y','bredde','hoyde','kilde','betydning_bekreftet'])
 for r,v in rooms['rooms'].items():
  for o in v['objects']:
   for state in o['states']:w.writerow([r,o['id'],state,objnames.get((o['id'],int(r)),''),o['kind'][state],o['x'],o['y'],o['w'],o['h'],f'obj{o["id"]:03d}_{state}.png','nei, krever motivkontroll'])
# Bevar utvalgte 1x-originaler og de nøyaktige skriptene brukt som identitetsbevis.
orig=b/'referanser/originaler';orig.mkdir(exist_ok=True)
evidence=b/'kildebevis';evidence.mkdir(exist_ok=True)
for f in fig:
 for s in f['sources']:
  p=root/s['file'];dst=orig/p.name
  if not dst.exists():shutil.copy2(p,dst)
 for name in f['evidence']:
  p=sources/name
  if p.exists():
   dst=evidence/name;dst.parent.mkdir(parents=True,exist_ok=True)
   if not dst.exists():shutil.copy2(p,dst)
for name in ['globale/scrp_120.txt','globale/scrp_102.txt','rom_052/lokal_206.txt','rom_032/inngang.txt','rom_026/lokal_205.txt','globale/scrp_092.txt','globale/scrp_094.txt']:
 p=sources/name;dst=evidence/name;dst.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() and not dst.exists():shutil.copy2(p,dst)
notes={
'sam':'Første kandidat avvist: oppdiktet hvitt lynmerke på hattebåndet. Ny kandidat skal ha vanlig bånd. Proporsjoner må fortsatt måles mot samlet original.',
'max':'Første kandidat avvist: trekantede sagtenner. Ny kandidat har blokktegnet tannrad. Hode, ører og kropp må kontrolleres gjennom alle taleruter.',
'lee-harvey':'Første kandidat avvist: harde pikselkanter og feil tolkning av bevegelsesstreker. Ny kandidat har glatte konturer og ingen oppdiktede ansiktsutstikkere.',
'sam-max-bigfootdrakt':'Første kandidat avvist: hvit hånd ble et ekstra Max-hode. Ny kandidat må vise bare Sam-snute, Max med blond tupé og Max sin hvite hånd. Dette er en forkledning, ikke en ny art.',
'bruno':'Spiss pelslokk, brun pels og brede føtter er bevart som konseptretning. Sammenlign også den frosne tilbakeblikkvarianten før paletten låses. 242 inneholder ruter med både Bruno og Sam.',
'bigfoot-dorvakt':'Foldede armer og bandasjeaktige lyse fotpartier må bevares. De hvite feltene er ikke grunnlag for å finne på sko. Senere fil-/pedikyrhandling må vurderes separat.',
'bigfoot-eldste':'Langt lyst skjegg, medaljong og vifteformet hodepynt med røde tupper er synlige i kilden. Ikke kall hodepynten grener uten bedre bevis. Egennavn er ikke etablert.',
'bigfoot-kvinne':'Portrettstudie fra hodelag. Kropp finnes i andre lag og er ikke ferdig vurdert. Figuren er den kvinnelige vakten ved bassenginngangen, ikke Trixie.',
'bigfoot-gjest-265':'Portrettstudie. Skuespiller 6 i rom 53 er dokumentert. Egennavn mangler. Ikke bruk bandmedlemmenes navn fra rulleteksten på denne personen.',
'bigfoot-gjest-266':'Portrettstudie. Skuespiller 5 i rom 53 er dokumentert. Kropp finnes som eget lag. Grå pels og ansiktsfarge må kontrolleres i aktiv rompalett.',
'doug':'Kostyme 102 er Doug. 103 til 105 viser Trixie i tilbakeblikket. Konseptet bruker bare Doug. Skålinnholdet er ikke sikkert identifisert; blå former må ikke låses som blåbær uten dialog-/objektbevis.',
'shuv-oohl':'Kort kroppsform, runde briller, rød bart, sparsomt rødt hår og lilla skjorte er referansepunkter. Ikke gjenbruk Doug som ansiktsmal.',
'conroy-bumpus':'Tupé, bar hodebunn og flere handlingskostymer er tilstander av samme mann. Auberginer formet som hodet hans er objekter, ikke personer.',
'kushman-brodrene':'Begge ansikter, sammenvoksingen og de to ulike uttrykkene er bevart som konseptretning. Tilknytning og bein må følges i hele animasjonen.',
'flambe':'Bar mage, lilla turban/bukse og grønt belte er identitetsankere. 107 inneholder også Trixie. Luefjær, håndredskap og ild skal ikke blandes sammen.',
'trixie':'Lang hals, gult antrekk, hatt og mørk hestehale beholdes. Halspartiene skal behandles som originalens utforming, ikke gis ny metall-/tre-/robotforklaring. Tilbakeblikket har andre klær.',
}
for f in fig:
 v2=b/'bilder'/f'{f["id"]}-v2.png';v1=b/f['concept'];f['concept']=str((v2 if v2.exists() else v1).relative_to(b))
 if v2.exists():f['prompt']='prompter/'+f['id']+'-v2.txt'
 f['status']='konseptkandidat, ikke produksjonsgodkjent' if (b/f['concept']).exists() else 'konsept mangler, diskplass nødvendig'
 f['analysis']=notes.get(f['id'],'Identitet og kildeark er ført opp. Konsept og full animasjonskontroll gjenstår.')
 f['approved_by_user']=False;f['runtime_verified']=False
(b/'figurer.json').write_text(json.dumps(fig,ensure_ascii=False,indent=2)+'\n')
lines=['# Figur- og objektanalyse før HD-konvertering','','Dette er en delvis konseptleveranse og et kontrollgrunnlag. Ingen av bildene er et godkjent spritesheet. HD-produksjonen er ikke startet.','','## Kilder og omfang','','Sam & Max Hit the Road, engelsk CD-utgave. Indeks-MD5: `d917f311a448e3cc7239c31bddb00dd2`. Uttrekket omfatter 348 kostymer, 16 052 PNG-ruter og 17 tomme ruter, 83 rombilder og 959 objektbilder. Kostymer er ressurser, ikke en telling av personer.','','Brukeren ba om konsept av hvert monster og korrekt analyse av navn, personer og objekter. Arbeidet tar foreløpig med skapninger og øvrige figurer i Sam & Max. Spørsmålet om dette omfanget er riktig, er sendt til brukeren og ikke besvart. 33 motivgrupper er undersøkt; det er ikke bevist at listen dekker alle distinkte skapninger i hele spillet.','','Kildearkene er originale pikselbilder forstørret med nearest. De er merket ORIGINAL. Konseptbildene er laget med den innebygde ChatGPT-bildegeneratoren. Verktøyet oppgir ikke eksakt modellnavn. Det er derfor ikke grunnlag for å påstå en bestemt modellversjon.','','## Feil som analysen forebygger','','- Doug er kostyme 102. Kostyme 103 til 105 er Trixie i tilbakeblikket, bekreftet i globalt skript 120. 107 inneholder Flambé og Trixie; 108 inneholder Bruno og Trixie. Det er ikke nye monstre.','- Bruno, Bigfoot-dørvakten, eldsten og gjestene er egne identiteter. En kostymeressurs kan også inneholde mer enn én person.','- Kostyme 158 viser hodet med lilla turban, briller og grått skjegg. Kokken bruker 159/160 i rom 32. De skal ikke slås sammen.','- Evelyn Morrison er den blonde figuren i kostyme 253, koblet til skuespiller 4 i rom 52 og navngitt i lokalt skript 206. Kostyme 254 viser en annen person som ennå ikke er sikkert navngitt.','- Sam og Max i Bigfoot-drakten er en sammensatt forkledning. Hvite fingre bak Max er en hånd, ikke et tredje hode.','- Conroys tupé er et objekt. Auberginer formet som hodet hans er også objekter.','- OBNA-navn i objekttabellen er interne utviklernavn. De er ikke automatisk navnene spilleren ser.','- Bandet og danserne i rom 53 er synlige i bakgrunnen. Klikkområdene 494/495 gir ikke egne eksporterte PNG-bilder i rooms.json. Ingen figur skal tildeles bandnavn bare fordi navnet finnes i rulleteksten.','- Den ansatte i Mystery Vortex er opp ned. Rosa hud øverst i råbildet er ikke et rosa hodeplagg.','','## Viktig begrensning i animasjonsgrunnlaget','','`pipeline/smhd/v6grafikk.py` samler hver rutekode bare én gang per animasjonslag (`c not in codes`) og utelater kontrollkodene 0x79, 0x7A og 0x7B. Listen `animasjoner[*].ruter` er derfor en ressursliste i første forekomst-rekkefølge, ikke et komplett avspillingsspor med gjentakelser, venting og varighet. Den må ikke brukes alene til å bygge eller godkjenne spritesheet-avspilling. Originalens kommandostrøm eller faktiske motoravspilling må brukes før produksjon. Ingen motor- eller pipelinekode er endret her.','','## Krav før spritesheets','','1. Identitet må være avklart for hvert kostyme og hver sammensatt rute. Uavklarte rader i kostymetabellen skal ikke få et oppdiktet navn.','2. Bekreft aktiv bruksrompalett og skuespillerpalett. Lagringsrommets palett i eksporten er bare startreferansen, særlig for frosne figurer, skygger og masker.','3. Behold original `cel`, `lag`, `kode`, mål, `rel_x`, `rel_y`, `move_x`, `move_y`, speiling og tomme ruter. Rute-ID er `lag * 128 + kode`.','4. Lag referanser for hode og kropp samlet i de faktiske retningene. Portrettstudier her gir ikke tillatelse til å finne på usett anatomi.','5. Behold originalens avspillingsrekkefølge, gjentakelser og tempo. En fast skalle skal ikke skifte størrelse når munnen beveger seg.','6. Kontroller hånd mot rekvisitt, fotpunkt, feste mellom lag, z-masker og relevante tilstandsoverganger i spillet.','7. Produksjonsark må ha ekte alfa, myke konturer, rutekart og SHA-256. De grå konseptarkene er ikke alfaressurser.','8. Tom godkjenner konsept/stil. Stilpiloten med ett rom og ett figurark må deretter kontrolleres i motoren før serieproduksjon.','','## Kontrollnivå','','- Originaluttrekk: 0 dekoderfeil i rooms.json og ved kostymeuttrekket. Begge grafikkfiler er hentet fra spilldata og MD5 er kontrollert. Talearkivet er ikke hentet eller testet.','- Dekompilering: 1179 av 1181 skript uten feil; 2 kjente descumm-feil er fortsatt åpne.','- Hele kostymeoversikten er sett i seks kontaktark. Dette viser én representativ rute per kostyme, ikke alle animasjoner.','- Konseptkandidater er sammenlignet visuelt med sine kildeark. Konkrete avvik er registrert og egne rettelser laget. Ingen kandidat er merket godkjent av Tom.','- Spillet er ikke bygget eller kjørt på nytt. Ingen hode/kropp-kontroll i motor, avspillingskontroll, mod-import eller spritesheet-test er utført.','- Systemdisken gikk full. Bare egne, nyopprettede regenererbare spill-/uttrekks-/dekompileringsfiler er flyttet til RAM-disken. Ingen eksisterende brukerfiler er slettet. Leveranse, kildeutvalg, metadata og skriptbevis ligger i gpt-arbeid.','- RAM-kildene under /tmp er midlertidige. De utvalgte 1x-originalene og skriptbevisene er bevart i leveransen. Hele uttrekket kan regenereres med prosjektets verktøy når diskplass finnes.','','## Figurenes identitet og konseptkontroll','']
for f in fig:
 lines += ['### '+f['name'],'',f"Type: {f['kind']}. Kostyme: {', '.join(map(str,f['costumes']))}. Status: **{f['status']}**.",'',f['identity'],'',f['analysis'],'',f"[Originalreferanse]({f['reference']})"+(f" · [Konsept]({f['concept']})" if (b/f['concept']).exists() else '')+f" · [Prompt]({f['prompt']})",'', 'Skriptbevis: '+', '.join(f'[{x}](kildebevis/{x})' for x in f['evidence'] if (evidence/x).exists())+'.','']
lines+=['## Åpne identiteter og rester','','Elmo er nevnt på postkortet i rom 26, men en bestemt tegnet ressurs er ikke sikkert koblet til ham. Kostyme 254, robotskuespillerens synlige innhold, frosne Bigfoot-varianter og eventuelle andre skapninger krever videre kontroll. De har ikke fått oppdiktede egennavn eller godkjente konsepter.','','Resten av konseptbildene og mer utfyllende kildekontroll krever ledig diskplass. Se galleriet og figurer.json for nøyaktig hvilke motiver som mangler.']
(b/'ANALYSE.md').write_text('\n'.join(lines)+'\n')
cards=[]
for f in fig:
 esc=html.escape;present=(b/f['concept']).exists();image=(f'<a href="{f["concept"]}"><img loading="lazy" src="{f["concept"]}" alt="Konsept av {esc(f["name"])}"></a>' if present else '<div class="missing">Konsept mangler. Kilde og analyse er bevart.</div>')
 cards.append(f'<article data-kind="{esc(f["kind"])}"><h2>{esc(f["name"])}</h2><p class="status">{esc(f["status"])}</p><p>{esc(f["identity"])}</p><div class="pair"><a href="{f["reference"]}"><img loading="lazy" src="{f["reference"]}" alt="Originalreferanse"></a>{image}</div><p>{esc(f["analysis"])}</p><p>Kostymer: {", ".join(map(str,f["costumes"]))} · <a href="{f["prompt"]}">Prompt</a></p></article>')
count=sum((b/f['concept']).exists() for f in fig)
page='''<!doctype html><html lang="no"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sam & Max: identitet før HD</title><style>body{font:17px/1.55 system-ui,sans-serif;background:#121b24;color:#e5e9ec;margin:0 auto;max-width:1280px;padding:28px}h1{font-size:34px}a{color:#90d7ff}header{border-bottom:1px solid #466074;padding-bottom:24px}.intro{max-width:900px}.controls{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}input,select{padding:12px;font:inherit;background:#203344;color:inherit;border:1px solid #68859b;border-radius:6px}input{min-width:280px;flex:1}article{background:#1c2b38;border:1px solid #405465;border-radius:10px;padding:22px;margin:22px 0}h2{margin:0 0 6px}.status{color:#ffd08b;font-size:14px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:center}.pair img{max-width:100%;max-height:640px;object-fit:contain;background:#aaa}.missing{background:#253847;border:1px dashed #708596;padding:32px}small{color:#c1cad1}[hidden]{display:none!important}@media(max-width:700px){body{padding:14px}.pair{grid-template-columns:1fr}h1{font-size:26px}}</style><header><h1>Identitet før HD-konvertering</h1><p class="intro">Originalreferanser, konseptkandidater og avklaringer for Sam & Max Hit the Road. Originalen vises til venstre, konseptet til høyre. Klikk et bilde for full størrelse.</p>'''+f'<p><strong>{count} av {len(fig)} planlagte motivgrupper har konseptkandidat.</strong> Ingen er produksjonsgodkjent. Full disk hindrer resten.</p>'+'''<p><a href="ANALYSE.md">Full analyse</a> · <a href="kostymer-348.csv">348 kostymer</a> · <a href="objektbilder-959.csv">959 objektbilder</a> · <a href="rutekart-original.csv">Originalt rutekart</a></p></header><div class="controls"><input id="q" placeholder="Søk etter navn, kostyme eller kjennetegn" aria-label="Søk"><select id="kind" aria-label="Type"><option value="">Alle typer</option>'''+''.join(f'<option>{html.escape(k)}</option>' for k in sorted({f['kind'] for f in fig}))+'''</select></div><main>'''+''.join(cards)+'''</main><script>const q=document.querySelector('#q'),kind=document.querySelector('#kind');function filter(){for(const x of document.querySelectorAll('article'))x.hidden=!(x.textContent.toLocaleLowerCase('nb').includes(q.value.toLocaleLowerCase('nb'))&&(!kind.value||x.dataset.kind===kind.value));}q.addEventListener('input',filter);kind.addEventListener('change',filter);</script></html>'''
(b/'index.html').write_text(page)
stats={'costumes':len(meta),'png_cels':sum(len(c['cels']) for c in meta.values()),'empty_cels':sum(len(c['tomme_ruter']) for c in meta.values()),'object_images':sum(len(o['states']) for r in rooms['rooms'].values() for o in r['objects']),'concept_subjects':len(fig),'subjects_with_concepts':count,'remaining_concepts':len(fig)-count,'runtime_verified':False,'user_approved':False,'pipeline_changed':False,'location':'gpt-arbeid, lokalt'}
(b/'STATUS.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n');print(json.dumps(stats,ensure_ascii=False))
