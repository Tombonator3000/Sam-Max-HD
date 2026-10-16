from pathlib import Path
import datetime,hashlib,json,subprocess
from zoneinfo import ZoneInfo
import numpy as np
from PIL import Image
R=Path('rapporter/natt-20261016-0720')
JOBS=['fig116_05','fig116_06','fig116_07','fig116_08']
now=datetime.datetime.now(ZoneInfo('Europe/Oslo')).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
entries=[];sourcehash={};checks=[]
for job in JOBS:
 p=Path('jobber')/job;j=json.loads((p/'jobb.json').read_text());im=Image.open(p/'resultat.png')
 assert im.mode=='RGBA' and im.size==(1536,1024)
 a=np.array(im);assert (a[:,:,3]==0).any() and ((a[:,:,3]>0)&(a[:,:,3]<255)).any()
 r=subprocess.run(['/home/tom/Sam-Max-HD/.venv/bin/python','verktoy/sjekk_leveranse.py',str(p/'resultat.png')],capture_output=True,text=True)
 (R/f'{job}-egenkontroll.txt').write_text(r.stdout+r.stderr)
 assert r.returncode==0,(job,r.stdout,r.stderr)
 checks.append(r.stdout)
 rows=[]
 for c in j['ruter']:
  x,y,xx,yy=c['synlig'];ox,oy=j['plassering'];wx=max(0,(ox+x-4)*4);wy=max(0,(oy+y-4)*4);ex=min(1536,(ox+xx+4)*4);ey=min(1024,(oy+yy+4)*4)
  m=a[wy:ey,wx:ex,3]>128;ys,xs=np.where(m);assert len(xs)
  row={k:c[k] for k in ['bilde','kostyme','rute','lag','animasjon','retning']}
  row['rect']=[int(wx+xs.min()),int(wy+ys.min()),int(xs.max()-xs.min()+1),int(ys.max()-ys.min()+1)];rows.append(row)
 (R/f'rutekart-{job}.json').write_text(json.dumps({job:{'ruter':rows}},ensure_ascii=False,indent=2)+'\n')
 for name in ['referanse.png','original_1x.png','prompt.txt','jobb.json']:
  current=(p/name).read_bytes();head=subprocess.check_output(['git','show',f'HEAD:{p/name}'])
  assert current==head,str(p/name)
  sourcehash[str(p/name)]=hashlib.sha256(current).hexdigest()
 entries.append({'jobb':job,'resultat':str(p/'resultat.png'),'sha256':sha(p/'resultat.png'),'ruter':len(rows),'rutekart':str(R/f'rutekart-{job}.json'),'forsok':1 if job in JOBS[:2] else 4,'egenkontroll':'OK','kontrollfil':str(R/f'{job}-egenkontroll.txt'),'visuelt_kontrollert_statisk':True,'importert':False,'motoravspilt':False,'godkjent_av_Tom':False,'klar_for_mottak':True})
 detail={
 'fig116_05':'''Fem ruter. Først Sam forfra, deretter fire stillinger sett bakfra. Animasjon 8 avsluttes, og animasjon 9 begynner. Ingen alligatordeler er lagt til. Ett helarkforsøk med prompt.txt ordrett.''',
 'fig116_06':'''Syv ruter. Seks balanse- og oppreisingsstillinger sett bakfra, deretter Sam i høyreprofil. Animasjon 9 fortsetter, og animasjon 10 begynner. Ingen alligatordeler er lagt til. Ett helarkforsøk med prompt.txt ordrett.''',
 'fig116_07':'''Ni ruter i animasjon 11. De fem første har bare Sam. De fire siste har de opprinnelige grønne alligatordelene ved føttene. Bakfra er beholdt som bakfra. Ett helarkforsøk med prompt.txt ordrett og en separat motivpresisering. Tre delte bildeforsøk gjelder den avgrensede alligatorrettingen: to for småfragmentene og ett for sammenhengende hode og rygg. Totalt fire bildeforsøk berører arket.''',
 'fig116_08':'''Seks ruter. Første rute er Sam i høyreprofil med alligatordeler. De neste fire viser balanse sett bakfra med alligatordeler. Siste rute har bare Sam. Animasjon 12 avsluttes, og animasjon 13 begynner. Ett helarkforsøk med prompt.txt ordrett og en separat motivpresisering. De samme tre delte bildeforsøkene for alligatorrettingen som på fig116_07 er brukt. Totalt fire bildeforsøk berører arket.'''
 }[job]
 extra=''
 if job in JOBS[2:]:
  extra='''\n\nFørste helarkforsøk ga for runde grønne fragmenter og et feil alligatorhode. Endelig alligator er nytegnet etter originalen med ett synlig profiløye, lave ryggformer og blå vannkant. Et kildeutsnitt samler bare de grønne og blå originalpikslene som faktisk er synlige i de ni berørte originalrutene. Dette avklarer ryggen der Sam skjuler forskjellige deler i forskjellige stillinger. Samlingen er redigeringsgrunnlag, ikke produksjonsgrafikk. Den første separate småfragmenttegningen beholdt pikselblokker og er forkastet. Andre småfragmenttegning brukes til venstre og høyre fragment. Den nye heltegningens midtdel brukes til alligatorhodet og den sammenhengende ryggen. Sam tegnes over denne flaten ved fotkontakten. Det tidligere delte profilhodet fra forrige nattgruppe ble prøvd i en mellomversjon, men brukes ikke i sluttfilen.\n\nAlle ni alligatorstillinger er sammenlignet på tvers av fig116_07 og fig116_08. Antall deler, ett øye, lokal grønn palett, blå vannkant og fravær av alligator på de øvrige rutene er kontrollert statisk. Ingen ny motoravspilling eller timingkontroll er gjort.'''
 if job!='fig116_08':
  extra+='''\n\nOriginalen har små adskilte blå enkeltpiksler utenfor Sams hovedform. Hovedfiguren er tilpasset etter sin egen komponentboks. De separate prikkene er bevart med en liten flate fra den nytegnede blå jakken. De inngår i rutekartet. Dette hindrer at prikkene blåser opp Sam ved skalering.'''
 else:
  extra+='''\n\nDen andre originalruten har en adskilt blå enkeltpiksel utenfor Sams hovedform. Den er bevart separat med en liten flate fra den nytegnede jakken. Den inngår i rutekartet.'''
 note=f'''# {job}

Dato: {now}

Kostyme 116 i rom 25, Gator Golf. Sam balanserer og beveger seg ved alligatorene. Dette er avklart i figurregisteret i kodearbeidstreet og sammenholdt med originalrutene. {detail}{extra}

Verktøy: innebygd image_gen.imagegen. Eksakt modellnavn vises ikke. Python, Pillow, numpy og scipy i prosjektets eksisterende miljø er brukt til tillatt alfarensing, komponentuttrekk og presis plassering. Ingen installasjon eller pipelineendring.

Original_1x.png, referanse.png, hovedark/sam.png og stil/fig002_01.png er sett før nytegning. Hovedarket er bilde to i helarkforsøket. Originalen styrer motiv, lokal palett, stilling, proporsjoner og 4x-geometri. Hovedarket styrer Sams identitet og strek. Den generiske beskrivelsen av høyrevendte ruter overstyrer ikke de synlige bakfra-stillingene i originalen. ORDRE.md, BESTILLING.md, AGENTS.md, ANALYSE.md, GJENNOMGANG.md, nattoverleveringen og den lokale remake-skillen er lest.

Råforsøk og fullstendige brukte prompter ligger i {R}/. Prompt.txt og øvrige beskyttede jobbfiler er byteidentiske med HEAD. Faktiske kildehash er ført i kildehash.json. Eventuelle eldre hashfelt i jobb.json er ikke endret.

Leveranse: hele lerretet, 1536 x 1024, ekte alfa med myke kanter. Bakgrunnssmitte med svært lav alfa er fjernet. Originalmaskene brukes til analyse og målbokser, aldri til å klippe den nytegnede produksjonskonturen.

Egenkontroll: OK, {len(rows)} av {len(rows)} ruter OK. Systemets python3 mangler numpy. Den uendrede kontrollen er derfor kjørt med /home/tom/Sam-Max-HD/.venv/bin/python uten installasjon. Utskrift: {R}/{job}-egenkontroll.txt.

Statisk visuell egenkontroll mot original og godkjent hovedark er utført. Klar for Claudes mottakskontroll. Importert: nei. Motoravspilt: nei. Animasjonstiming, faktisk sammensetting i motoren og Toms godkjenning er ikke kontrollert. Ingen avgjørende motivspørsmål er uavklart for dette arket.

SHA-256: {sha(p/'resultat.png')}
'''
 (p/'notat.md').write_text(note)

for p in [Path('hovedark/sam.png'),Path('stil/fig002_01.png'),Path('ORDRE.md'),Path('ANALYSE.md')]:sourcehash[str(p)]=sha(p)
(R/'kildehash.json').write_text(json.dumps(sourcehash,ensure_ascii=False,indent=2)+'\n')
(R/'fremdrift.json').write_text(json.dumps({'dato':now,'gren':'gpt-arbeid','verktøy':'image_gen.imagegen','modell':'Eksakt modellnavn ikke vist','leveranser':entries,'teller':{'levert':4,'ruter':27,'visuelt_kontrollert_statisk':4,'importert':0,'motoravspilt':0,'godkjent_av_Tom':0},'bildeforsok':{'helark':4,'delte_alligatorforsok':3,'totalt':7},'hoppet_over':[{'jobber':['lag083_01','lag083_02','lag083_03','lag083_04'],'grunn':'ORDRE krever godkjent rom083. Status er sjekk. ANALYSE dokumenterer feil lagerrompalett og skybeskrivelse. Objektene brukes i rom54, og objekt835 avventer avklaring av bart/munn.'}]},ensure_ascii=False,indent=2)+'\n')
(R/'RAPPORT.md').write_text(f'''# Fire grafikkleveranser

Dato: {now}

Levert: fig116_05, fig116_06, fig116_07 og fig116_08. Fire ark og 27 ruter. Fire ark er statisk visuelt kontrollert. Null er importert, null er motoravspilt og ingen er godkjent av Tom i denne økten.

Alle 27 ruter består den uendrede egenkontrollen. Hvert ark har resultat.png, notat.md, rutekart, kontrollutskrift og SHA-256 under leveranser i fremdrift.json. Hele lerretet er 1536 x 1024 med ekte alfa. Beskyttede jobbfiler er bytekontrollert mot HEAD og er uendret.

Kostyme116 viser Sam ved alligatorene i Gator Golf, rom25. Originalene og hovedark/sam.png styrer identitet, drakt, stilling og strek. Front, profil og bakfra-stillinger er bevart. Fig116_05 og fig116_06 har ingen alligatordeler. Fig116_07 har fire alligatorstillinger og fig116_08 har fem. Delene er nytegnet etter riktig originalpalett med ett profiløye, lave grønne ryggformer og blå vannkant. De små adskilte blå kildeprikkene er bevart uten å forstørre Sam. Alligatorrettingen har en egen kildesamling av de delene som faktisk er synlige gjennom originalanimasjonen. Ingen originalpikselkunst brukes i produksjonsfilene.

Sju kall til bildeverktøyet: fire helark, to forsøk på små alligatorfragmenter og ett på hode og sammenhengende rygg. Første småfragmentforsøk er forkastet fordi det beholdt de firkantede pikselblokkene. De valgte nytegningene er renset og plassert presist med Python etter Toms tillatelse. Ingen pipelinekode er endret. Endelig grafikk og fotkontakt er sammenlignet statisk mot originalen, også på grå bakgrunn. Timing og motorvisning gjenstår.

Lag083_01 til 04 står først i ordren, men kravet om godkjent rom083 er ikke oppfylt. Rommet står til sjekk i status.csv. ANALYSE dokumenterer at lagerrommets palett og skybeskrivelse er feil for objektene som brukes i rom54. Objekt835 avventer dessuten motivavklaring. Lagjobbene er derfor hoppet over, og de neste fire avklarte jobbene er tatt i ordensrekkefølge.

Returen for fig247_02 var allerede rettet i leveransen fra 06:18 og er ikke gjentatt. Fig091_03 til 05 og kontrollen av PR32 er ikke gjentatt.

Git pull ble forsøkt. Sandkassen kan ikke skrive FETCH_HEAD i Git-metadataene utenfor arbeidsmappen. Grenen er fortsatt gpt-arbeid. Ingen commit, push, grenbytte, PR eller fletting er gjort. Nattverktøyet kan ta med resultat.png, notat.md og denne rapportmappen.

Systemets python3 mangler numpy. Prosjektets eksisterende Python-miljø kjører samme kontrollskript uten installasjon. Den eksterne henten av remake-skillen feilet; lokal kopi i /home/tom/Sam-Max-HD/docs/skills/scumm-hd-remake/SKILL.md er lest.
''')
(R/'todo.md').write_text('''# Videre kontroll hos Claude

Ta imot og importer fig116_05 til 08 med de fire rutekartene. Sammenlign faktisk motorvisning, særlig skiftet mellom Sam alene og Sam på alligatorene. Kontroller fotkontakt, ruterekkefølge og overgangene mellom animasjon 8, 9, 10, 11, 12 og 13. Ingen motoravspilling eller ny import er utført her.

Lag083_01 til 04 må vente til riktig rom083-grunnlag er avklart og godkjent. Bruk rom54s palett for objektene som tegnes der. Objekt835 avventer det tidligere dokumenterte spørsmålet om bart/munn.

Ingen nye konkrete kodebehov er funnet i denne grafikkøkten. Den kjente avvist-SHA-feilen og alfakontrollen hører til kodesporet og er ikke endret eller kontrollert på nytt her.
''')
print(''.join(checks))
print('4 ark, 27 ruter. Resultater, notater, kontrollfiler, rutekart og kildehash lagret. Beskyttede filer uendret mot HEAD.')
