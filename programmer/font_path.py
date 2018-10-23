from kivy.utils import platform
from kivy.core.text import LabelBase
from kivy.logger import Logger
import os

PREFERED=['simsun.ttc','NotoSansCJK-Regular.ttc','DroidSansFallback.ttf','Roboto-Regular.ttf','DroidSans.ttf','HYSerif_Regular.ttf','NotoSerif-Regular.ttf','Roboto-Regular.ttf','DroidSans.ttf']

fonts_dir=LabelBase.get_system_fonts_dir()
font_names=''
paths=[]
Logger.info('kivy: kcf: fonts_dir:%s' % `fonts_dir`)
for dirx in fonts_dir:
    font_names+=dirx +'\n'
    fs = os.listdir(dirx)
    for fx in fs:
        #Logger.info('kivy: kcf: f:%s' % fx)
        font_names+= fx +'\n'
        if fx in PREFERED:
            paths.append(os.path.join(dirx, fx))

FONT_NAMES_FILE='/storage/emulated/0/data/font_names.txt'
if not os.path.isfile(FONT_NAMES_FILE):
    f=open('/storage/emulated/0/data/font_names.txt', 'wb')
    f.write(font_names)
    f.close()
    
#print 'paths:%s' % `paths`
FONT_PATH =''
if paths:
    found=False
    for fx in PREFERED:
        #print 'fx:%s' % fx
        for i in range(len(paths)):
            #print 'paths[%d]:%s  (%s)' % (i, paths[i], os.path.basename(paths[i]))
            if fx in paths[i]:
                FONT_PATH = paths[i]
                found=True
                break
        if found:
            break
Logger.info( 'kivy: kcf: FONT_PATH: %s' % FONT_PATH)

