# -*- coding: utf-8 -*-
# ex_intro1.py
# author: C.F.Kwok
# date: 2018-1-17
from simp_py import oled,mon
import time
from ch_intro_font import CH_FONTS
TEXT_FILE='ch_intro.txt'
SCREEN_WIDTH=16 # 128/8
SCREEN_HEIGHT=64
FONT_HEIGHT=16
LINE_HEIGHT=18
#BITM={0: 1, 1: 2, 2:4, 3:8, 4:0x10,5:0x20,6:0x40,7:0x80}
BITM={0: 0x80, 1: 0x40, 2:0x20, 3:0x10, 4:0x8,5:0x4,6:0x2,7:0x1}
class INTRO:
    global time, oled, mon, SCREEN_WIDTH,SCREEN_HEIGHT,FONT_HEIGHT,CH_FONTS,BITM,LINE_HEIGHT
    
    def __init__(self,fn):
        self.oled=oled
        self.frm = oled.framebuf
        self.fn=fn
        f = open(fn, 'rb')
        self.lines=f.readlines()
        f.close()
        self.buf_size = SCREEN_WIDTH * SCREEN_HEIGHT

    def test_buf(self):
        buf= bytearray([0] * self.buf_size)
        OFS1= SCREEN_WIDTH*8
        OFS2 = SCREEN_WIDTH *16
        OFS3 = SCREEN_WIDTH *32
        OFS4 = SCREEN_WIDTH *63
        for i in range(SCREEN_WIDTH):
            buf[i]=0xff
            buf[i+OFS1]= 0xaa
            buf[i+OFS2]= 0x55
            buf[i+OFS3]= 0x81
            buf[i+OFS4]= 0xC3
        return buf
            
    def lines_to_buf(self,ofy):
        buf= bytearray([0] * self.buf_size)
        bufix=0 # buf idx, var in byte
        ofx=0 # line text startx in bit
        #ofy=0 # line text starty in bit
        byteofy,bitofy = divmod(ofy,LINE_HEIGHT)
        lines= self.lines[byteofy:]
        #print('ofy:%s byteofy:%s bitofy:%s len_lines:%s' % (ofy,byteofy,bitofy, len(lines)))
        
        line_n=0
        bufix_inc= (SCREEN_WIDTH * (LINE_HEIGHT - bitofy))
        while lines:
            pbufix = bufix
            line, lines= lines[0], lines[1:]
            line = line.strip()
            txt = line.decode('utf-8')
            ix = ofx
            byteofx,bitofx= divmod(ix,8)
            txt = txt[byteofx:]
            while txt:
                chx, txt = txt[0], txt[1:]
                #print('chx:%s bufix:%s' % (chx,bufix))
                fntx = CH_FONTS[chx]
                if len(fntx)==16:
                    # half width
                    bufix_ofs=0
                    n=bitofy
                    while n < 16:
                        loc = bufix + bufix_ofs
                        if loc >= len(buf):
                            break
                        buf[loc] = fntx[n]
                        bufix_ofs+= SCREEN_WIDTH
                        n+=1
                    bufix+=1
                else:
                    # full width
                    bufix_ofs=0
                    n=bitofy * 2
                    while n<31:
                        j=0
                        loc = bufix + bufix_ofs
                        if loc >= len(buf):
                            break
                        buf[loc]= fntx[n+j]
                        j+=1
                        loc = bufix + bufix_ofs + 1
                        if loc >= len(buf):
                            break
                        buf[loc]= fntx[n+j]
                        bufix_ofs += SCREEN_WIDTH
                        n+=2
                    bufix+=2
            # prepare next line
            ofx=0
            line_n+=1
            bitofy=0
            bufix= pbufix + bufix_inc
            bufix_inc =SCREEN_WIDTH * LINE_HEIGHT 
            if bufix >= len(buf):
                #print('return buf 0')
                return buf
        #print('return buf 1')
        return buf

    def draw_buf(self,buf):
        width= SCREEN_WIDTH * 8
        idx=0
        x=0
        y=0
        while 1:
            bx = buf[idx]
            for j in range(8):
                b = bx & BITM[j]
                if b:
                    self.frm.pixel(x,y,1)
                #else:
                #    self.frm.pixel(x,y,0)
                x+=1
            idx+=1
            if x>= width:
                x=0
                y+=1
                if y>= SCREEN_HEIGHT:
                    return
                
    def draw_last_line(self,buf,n):
        width= SCREEN_WIDTH * 8
        idx=SCREEN_WIDTH * (SCREEN_HEIGHT -n)
        x=0
        y=SCREEN_HEIGHT-n
        self.frm.fill_rect(0,y,width,n,0)
        #self.frm.fill(0)
        while 1:
            bx=buf[idx]
            for j in range(8):
                b = bx & BITM[j]
                if b:
                    self.frm.pixel(x,y,1)
                #else:
                #    self.frm.pixel(x,y,0)
                x+=1
            idx+=1
            if x>= width:
                x=0
                y+=1
                if y>= SCREEN_HEIGHT:
                    return                
                        
    def run(self):
        ofy=0
        lenx= (len(self.lines)-4) * LINE_HEIGHT
        buf =self.lines_to_buf(ofy)
        self.oled.fill(0)
        self.draw_buf(buf)
        self.oled.show()
        time.sleep(0.02)
        stp=1
        ofy=2
        for i in range(int(lenx/4)):
        #for ofy in range(1,lenx):
            self.oled.scroll(0,-4)
            buf =self.lines_to_buf(ofy)
            self.draw_last_line(buf,16)
            self.oled.show()
            time.sleep(0.02)
            ofy+=4
        
if __name__=='__main__':
    intro = INTRO(TEXT_FILE)
    intro.run()

