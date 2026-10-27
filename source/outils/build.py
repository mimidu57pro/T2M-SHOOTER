import base64,json,os,glob
t=open('template.html').read()
m={'car':'v34','over':'over','top':'top','front':'front','rear':'rear','battery':'battery','brushless':'brushless','brushed':'brushed'}
imgs={k:'data:image/webp;base64,'+base64.b64encode(open(f'{v}.webp','rb').read()).decode() for k,v in m.items()}
from PIL import Image
import io
for f in glob.glob('../r3d/out/*.png'):
    im=Image.open(f).convert('RGB').resize((420,420),Image.LANCZOS); im.save('crops/x_'+os.path.basename(f)[:-4]+'.webp','WEBP',quality=84)
ph={os.path.basename(f)[:-5]:'data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in glob.glob('crops/*.webp')}
out=t.replace('const IMG = __IMAGES__;','const IMG = '+json.dumps(imgs)+';\nconst PH = '+json.dumps(ph)+';')
open('pirate-shooter-lab.html','w').write(out)
open('preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'+out+'</body></html>')
