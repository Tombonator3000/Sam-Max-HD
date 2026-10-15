from pathlib import Path
import json,sys
sys.path.insert(0,'/home/tom/Sam-Max-HD/pipeline')
from PIL import Image
from smhd.gpt import _load_job,check_pieces,piece_problem
r=Path('rapporter/natt-lobby052-20261015');out={}
for j in sys.argv[1:]:
 d=Path('jobber')/j;m=json.loads((d/'jobb.json').read_text());job=_load_job(m)
 x,y,w,h=m['bilde_i_lerret'];im=Image.open(d/'resultat.png').crop((x,y,x+w,y+h))
 cs=check_pieces(Image.open(d/'original_1x.png'),im,job,Path('/home/tom/Sam-Max-HD/work/extract'))
 out[j]={k:dict(v,problem=piece_problem(v)) if v else None for k,v in cs.items()}
print(json.dumps(out,indent=2))
(r/'mottak-siste.json').write_text(json.dumps(out,indent=2)+'\n')
