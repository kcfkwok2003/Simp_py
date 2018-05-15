# -*- coding: utf-8 -*-
# ex_xled_ch.py
# author: C.F.Kwok
# date: 2018-01-15
from max7219 import M8x8

from simp_py import mon
import time
from machine import Pin,SPI
class XLED_CH:
    global M8x8, mon,time,Pin,SPI
    def __init__(self,fn,ch_fonts):
        self.fn=fn
        self.ch_fonts= ch_fonts

        spi = SPI(spihost=1,sck=Pin(19,Pin.OUT),mosi=Pin(23,Pin.OUT),miso=Pin(21,Pin.IN)) #,firstbit=SPI.LSB)
        self.mx =M8x8(spi,Pin(18,Pin.OUT),4)        
        self.seqs=[]
        f=open(fn,'rb')
        lines=f.readlines()
        f.close()        
        for line in lines:
            line = line.strip()
            txt = line.decode('utf-8')
            for chx in txt:
                self.seqs.append(chx)
            self.seqs.append(0)
        self.seqs.append(0)
        self.state=0
        
    def run(self):
        while 1:
            if self.state >= len(self.seqs):
                self.state=0
                break
            chx = self.seqs[self.state]
            if chx==0:
                self.mx.fill(0)
                self.mx.show()
                time.sleep(0.5)
                self.state+=1
                continue
            self.mx.fill(0)
            self.put_ch(chx)
            self.mx.show()
            self.state+=1
            time.sleep(1)

            
    def put_ch(self,chx):
        BITM=[0x80,0x40,0x20,0x10,0x08,0x04,0x02,0x01]
        fntx = self.ch_fonts[chx]
        y=0
        for i in range(1,9):
            x=0
            bx, fntx = fntx[0],fntx[1:]
            for i in range(8):
                if bx & BITM[i]:
                    self.mx.pixel(x,y,1)
                x+=1
            bx, fntx = fntx[0],fntx[1:]
            for i in range(8):
                if bx & BITM[i]:
                    self.mx.pixel(x,y,1)
                x+=1
            y+=1
        y=0
        for i in range(1,9):
            x=16
            bx, fntx = fntx[0],fntx[1:]
            for i in range(8):
                if bx & BITM[i]:
                    self.mx.pixel(x,y,1)
                x+=1
            bx, fntx = fntx[0],fntx[1:]
            for i in range(8):
                if bx & BITM[i]:
                    self.mx.pixel(x,y,1)
                x+=1
            y+=1
        
                
if __name__=='__main__':
    from kyoco_fontx import CH_FONTS
    TEXT_FILE='kyoco.txt'    
    x = XLED_CH(TEXT_FILE, CH_FONTS)
    while 1:
        x.run()

