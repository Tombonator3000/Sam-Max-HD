from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import numpy as np
r=Path('rapporter/natt-lobby052-20261015')
room=Image.open('jobber/rom052_del2av2/resultat.png').convert('RGB')
raw09=Image.open(r/'lag052_09_del2av2-raa1.png').convert('RGB')
raw10=Image.open(r/'lag052_10_del2av2-raa1.png').convert('RGB')
strips={}
for k,box,size in [(7,(608,288,728,432),(12,16)),(8,(638,200,738,416),(12,16))]:
 a=Image.open(r/f'lag052_{k:02d}_del2av2-detail2.png').convert('RGB').crop(box)
 p=np.asarray(a);mask=((p[:,:,2].astype(int)-p[:,:,1])>14)&(p[:,:,2]>65)
 rgba=a.convert('RGBA');rgba.putalpha(Image.fromarray((mask*255).astype('uint8')))
 rgba=rgba.resize(size,Image.Resampling.LANCZOS);rgba.save(r/f'lag052_{k:02d}_del2av2-nytegnet-stripe.png');strips[k]=rgba
for k in range(7,11):
 j=f'lag052_{k:02d}_del2av2';base=room.copy()
 # Only the re-painted object rectangle is inserted into the approved room.
 patch=raw10.crop((544,720,640,816))
 if k==7:
  # State 07 has the exposed slit. Later phases use the closed upper lid.
  eye=raw09.crop((580,724,616,760))
  ea=Image.new('L',eye.size,0);ImageDraw.Draw(ea).rectangle((1,1,34,34),fill=255);ea=ea.filter(ImageFilter.GaussianBlur(.6))
  patch.paste(eye,(36,4),ea)
 if k in strips:
  x,y=(588,744) if k==7 else (592,736)
  patch.paste(strips[k],(x-544,y-720),strips[k])
 if k==9:
  # The original has only the short tip of the same cool strip in state 09.
  tip=strips[8].resize((8,8),Image.Resampling.LANCZOS)
  patch.paste(tip,(52,20),tip)
 alpha=Image.new('L',(96,96),255)
 # One-pixel soft outer rectangle, no original contour mask.
 alpha=Image.new('L',(96,96),0);ImageDraw.Draw(alpha).rectangle((1,1,94,94),fill=255);alpha=alpha.filter(ImageFilter.GaussianBlur(.5))
 base.paste(patch,(544,720),alpha)
 base.paste((128,128,128),(0,0,1536,112));base.paste((128,128,128),(0,912,1536,1024));base.save(Path('jobber')/j/'resultat.png')
