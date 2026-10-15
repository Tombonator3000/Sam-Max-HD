from pathlib import Path
import json
from PIL import Image
r=Path(__file__).parent
jobs=['lag022_02_del3av3','lag047_02','lag052_01_del2av2','lag052_02_del1av2']
for j in jobs:
 base=Image.open(r/(j+'-forrige.png' if j=='lag047_02' else j+'-raa1.png')).convert('RGB')
 if j=='lag047_02':
  new=Image.open(r/(j+'-raa1.png')).convert('RGB');b=(768,208,928,272);base.paste(new.crop(b),b)
 if j.startswith('lag052'):
  new=Image.open(r/(j+'-detail4.png')).convert('RGB').resize((160,160),Image.Resampling.LANCZOS)
  bx=550 if j=='lag052_01_del2av2' else 934
  base.paste(new.crop((30,68,90,116)),(bx,748,bx+60,796))
 d=Path('jobber')/j;m=json.loads((d/'jobb.json').read_text());x,y,w,h=m['bilde_i_lerret']
 out=Image.new('RGB',(1536,1024),(128,128,128));out.paste(base.crop((x,y,x+w,y+h)),(x,y));out.save(d/'resultat.png')
