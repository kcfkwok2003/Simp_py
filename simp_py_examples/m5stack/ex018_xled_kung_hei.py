# -*- coding: utf-8 -*-
# ex_xled_ch.py
# author: C.F.Kwok
# date: 2018-01-15
from max7219 import M8x8
from ch_kung_hei_font import CH_FONTS
from simp_py import mon
import time
from machine import Pin,SPI
class XLED_CH:
    global M8x8, CH_FONTS,mon,time,Pin,SPI
    def __init__(self):
        spi = SPI(spihost=1,sck=Pin(19,Pin.OUT),mosi=Pin(23,Pin.OUT),miso=Pin(21,Pin.IN)) #,firstbit=SPI.LSB)
        #spi.init(sck=Pin(12,Pin.OUT),mosi=Pin(13,Pin.OUT)) #,firstbit=SPI.LSB)
        #spi.init(sck=Pin(19,Pin.OUT),mosi=Pin(23,Pin.OUT)) #,firstbit=SPI.LSB)
        self.mx =M8x8(spi,Pin(18,Pin.OUT),4)        
        #self.mx = M8x8(12,13,14,4,1)
        self.seqs=[u'\u798f',0,u'\u798f',0,u'\u798f',0,]
        self.ch2s = u'\u606d\u559c\u767c\u8ca1'
        self.ch3s = u'\u65b0\u6625\u5927\u5409'
        for chx in self.ch2s:
            self.seqs.append(chx)
        self.seqs.append(0)
        for chx in self.ch3s:
            self.seqs.append(chx)
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
        fntx = CH_FONTS[chx]
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
    x = XLED_CH()
    while 1:
        x.run()

