# -*- coding: utf-8 -*-

import sys
import os
from PIL import Image,ImageDraw,ImageFont
#FONT_PATH='../fonts'
#FONT_METRIC=16
#DRAW_METRIC=(16,18)
FONT_PNG='/storage/emulated/0/data/simp_py_png'

class CH2DAT:
    def __init__(self,font,font_metric,draw_metric,save_png=False,top_cut=2):
        self.font= font
        self.font_metric=font_metric
        self.draw_metric= draw_metric
        self.save_png=save_png
        self.top_cut=top_cut
        
    def to_dat(self,txt):
        im = Image.new('1',self.draw_metric,color=1)
        draw = ImageDraw.Draw(im)
        real_w,real_h = draw.textsize(txt,font=self.font)
        print 'txt:%s w:%s h:%s' % (`txt`,real_w,real_h)
        draw.text((0,0),txt,font=self.font)
        del draw
        vv = ord(txt)
        fn = '%s-%02x%02x' % (txt, (vv>>8), (vv& 0xff))
        if self.save_png:
            if not os.path.isdir(FONT_PNG):
                os.makedirs(FONT_PNG)
            im.save('%s/ch-%s.png' % (FONT_PNG,fn), 'PNG')
        dat =list(im.getdata())
        print 'dlen:', len(dat)
        return  self.to_bytes(dat, real_w, real_h)

    def to_bytes(self,dat, real_w,real_h):
        idx=0
        bytes=[]
        if self.font_metric==16:
            if self.top_cut==2:
                dat = dat[32:]  # drop 1st 2 lines, assume it is blank
            elif self.top_cut==1:
                dat = dat[16:-16]  # drop 1st line, & last line assume it is blank
            elif self.top_cut==0:
                dat = dat[:-32]  # drop last 2 lines
            else:  # no top_cut
                pass
        while dat:
            bs, dat= dat[:8], dat[8:]
            bytes.append(self.b2byte(bs))
            bs, dat= dat[:8], dat[8:]
            if real_w==8:
                continue   # ignore for another 8bit for 8bit width
            bytes.append(self.b2byte(bs))
            
        return bytes
    
    def b2byte(self,bs):
        byte=0
        for bx in bs:
            byte = byte *2 + bx
        return byte
            

def conv_lines(lines, out_path, font_path, font_metric, draw_metric,save_png=False,top_cut=2):
    font = ImageFont.truetype(font_path,font_metric)
    ch2dat = CH2DAT(font,font_metric,draw_metric,save_png,top_cut)
    i=0
    fonts={}
    for line in lines:
        txts = line.decode('utf-8')
        for txt in txts:
            if txt.strip()=='':
                continue
            if fonts.has_key(txt):
                continue
            dat =ch2dat.to_dat(txt)
            fonts[txt]= dat
    # add space
    fonts[u' ']=ch2dat.to_dat(u' ')
    xmap=""
    txt="# -*- coding: utf-8 -*-\n"
    keys=fonts.keys()
    keys.sort()
    txt+='CH_FONTS={\n'
    for key in keys:
        xmap+="%s:%s\n" % (`key`, key.encode('utf-8'))
        txt+="%s:bytearray([\n" % `key`
        i=0
        for bx in fonts[key]:
            i+=1
            txt+='0x%02x,' % (bx ^ 0xff)
            if (i % 8)==0:
                txt+='\n'
        txt+=']),\n'
    txt+='}\n'
    f=open(out_path,'wb')
    f.write(txt)
    f.close()
    f=open(out_path+'.map','wb')
    f.write(xmap)
    f.close()
    report='handle %s characters and write to %s' % (len(keys), out_path) 
    return report

if __name__=="__main__":
    font_path='/storage/emulated/0/data/simp_py_fonts/GNUUnifont9FullHintInstrUCSUR.ttf'
    out_path='fontx16.py'
    font_metric=16
    draw_metric=(16,18)
    f=open('ch_intro.txt','rb')
    lines=f.readlines()
    print conv_lines(lines,out_path,font_path,font_metric,draw_metric)
    
