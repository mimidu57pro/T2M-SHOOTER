import base64,json,os,glob
t=open('template.html').read()
m={'car':'v34','over':'over','top':'top','front':'front','rear':'rear','battery':'battery','brushless':'brushless','brushed':'brushed'}
imgs={k:'data:image/webp;base64,'+base64.b64encode(open(f'{v}.webp','rb').read()).decode() for k,v in m.items()}
from PIL import Image
import io
from PIL import ImageChops, ImageFilter
def recenter(im, pad=.16, out=420):
    im=im.convert('RGB'); w,h=im.size
    g=im.convert('L').filter(ImageFilter.GaussianBlur(1))
    # background is bright and smooth: object = clearly darker or coloured pixels
    hsv=im.convert('HSV'); s=hsv.split()[1]
    m=ImageChops.lighter(g.point(lambda v:255 if v<170 else 0), s.point(lambda v:255 if v>60 else 0))
    box=m.getbbox() or (0,0,w,h)
    cx=(box[0]+box[2])/2; cy=(box[1]+box[3])/2; side=max(box[2]-box[0],box[3]-box[1])*(1+2*pad)
    side=min(max(side,120),max(w,h)*1.3)
    canvas=Image.new('RGB',(int(side),int(side)),im.getpixel((w-3,3)))
    # paint a soft studio backdrop so padding blends in
    bgc=Image.new('RGB',canvas.size); 
    for y in range(canvas.size[1]):
        pass
    side=min(side,w,h); x0=int(min(max(cx-side/2,0),w-side)); y0=int(min(max(cy-side/2,0),h-side))
    canvas=Image.new('RGB',(int(side),int(side)))
    canvas.paste(im,(-x0,-y0))
    return canvas.resize((out,out),Image.LANCZOS)
for f in glob.glob('../r3d/out/*.png'):
    recenter(Image.open(f)).save('crops/x_'+os.path.basename(f)[:-4]+'.webp','WEBP',quality=84)
ph={os.path.basename(f)[:-5]:'data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in glob.glob('crops/*.webp')}
out=t.replace('const IMG = __IMAGES__;','const IMG = '+json.dumps(imgs)+';\nconst PH = '+json.dumps(ph)+';')
open('pirate-shooter-lab.html','w').write(out)
open('preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'+out+'</body></html>')
