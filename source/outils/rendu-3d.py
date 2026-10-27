import os,base64,json,sys
from playwright.sync_api import sync_playwright
jobs=json.load(open(sys.argv[1]))
os.makedirs('out',exist_ok=True)
with sync_playwright() as pw:
    b=pw.chromium.launch(args=["--use-gl=swiftshader","--enable-webgl","--ignore-gpu-blocklist"])
    pg=b.new_page(viewport={'width':900,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+os.path.abspath('render.html')); pg.wait_for_timeout(500)
    if errs: print(errs[:3]); sys.exit(1)
    for n,j in jobs.items():
        d=pg.evaluate("j=>renderJob(j)",j)
        open(f'out/{n}.png','wb').write(base64.b64decode(d.split(',')[1])); print('done',n,flush=True)
    b.close()
