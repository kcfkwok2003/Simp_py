from kyoco_fontx import CH_FONTS
TEXT_FILE='kyoco.txt'
#from %{ch_fontx}s import CH_FONTS
# e.g. ch_intro_fontx.py
#TEXT_FILE='%{ch_txt}s'   # e.g. ch_intro.txt

from simp_py import tft,mon
import framebuf
import time
SCREEN_WIDTH=16 # 128/8
SCREEN_HEIGHT=128
FONT_HEIGHT=16
LINE_HEIGHT=18
#BITM={0: 1, 1: 2, 2:4, 3:8, 4:0x10,5:0x20,6:0x40,7:0x80}
BITM={0: 0x80, 1: 0x40, 2:0x20, 3:0x10, 4:0x8,5:0x4,6:0x2,7:0x1}
class INTRO:
    global time, oled, mon, SCREEN_WIDTH,SCREEN_HEIGHT,FONT_HEIGHT,CH_FONTS,BITM,LINE_HEIGHT,framebuf
    
    def __init__(self,fn):
        self.fn=fn
        f = open(fn, 'rb')
        self.lines=f.readlines()
        f.close()
        self.buf_size = SCREEN_WIDTH * (SCREEN_HEIGHT+2)
        self.fbuf = framebuf.FrameBuffer(bytearray(SCREEN_WIDTH * 8 * SCREEN_HEIGHT),SCREEN_WIDTH*8,SCREEN_HEIGHT,framebuf.MONO_HLSB)
        self.fbuf.fill(0)
        tft.tft.clear()
        self.buf= bytearray([0] * self.buf_size)
        
    def clear_buf(self):
        for i in range(len(self.buf)):
            self.buf[i]=0
            
    def lines_to_buf(self,ofy):
        self.clear_buf()
        buf = self.buf
        bufix=0 # buf idx, var in byte
        ofx=0 # line text startx in bit
        #ofy=0 # line text starty in bit
        byteofy,bitofy = divmod(ofy,LINE_HEIGHT)
        lines= self.lines[byteofy:]
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
                    self.fbuf.pixel(x,y,1)
                    #self.frm.pixel(x,y,1)
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
        self.fbuf.fill_rect(0,y,width,n,0)
        #self.frm.fill_rect(0,y,width,n,0)
        #self.frm.fill(0)
        while 1:
            bx=buf[idx]
            for j in range(8):
                b = bx & BITM[j]
                if b:
                    self.fbuf.pixel(x,y,1)
                    #self.frm.pixel(x,y,1)
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
        self.fbuf.fill(0)
        #self.oled.fill(0)
        self.draw_buf(buf)
        #self.oled.show()
        self.show()
        time.sleep(0.02)
        stp=1
        ofy=2
        for i in range(int(lenx/4)):
        #for ofy in range(1,lenx):
            self.fbuf.scroll(0,-4)
            buf =self.lines_to_buf(ofy)
            self.draw_last_line(buf,16)
            self.show()
            time.sleep(0.02)
            ofy+=4

    def show(self):
        mc_width = SCREEN_WIDTH *8
        for ix in range(mc_width):
            for iy in range(SCREEN_HEIGHT):
                ic = self.fbuf.pixel(ix,iy)
                if ic==1:
                    ic = 0xffff00
                else:
                    ic=0
                tft.tft.pixel(ix*2, iy*2,ic)
                
if __name__=='__main__':
    intro = INTRO(TEXT_FILE)
    intro.run()

