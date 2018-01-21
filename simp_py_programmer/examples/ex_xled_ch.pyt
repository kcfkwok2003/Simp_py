# -*- coding: utf-8 -*-
# ex_xled_ch.py
# author: C.F.Kwok
# date: 2018-01-15
from m8x8 import M8X8
from ch_dat import CH_FONTS
from simp_py import mon
import time
class XLED_CH:
    global M8X8, CH_FONTS,mon,time
    def __init__(self):
        self.mx = M8X8(12,13,14,4,1)
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
        
    def loop(self):
        while 1:
            self.__loop()

    def __loop(self):
        while 1:
            if self.state >= len(self.seqs):
                self.state=0
            chx = self.seqs[self.state]
            if chx==0:
                self.clr_ch()
                time.sleep(0.5)
                self.state+=1
                continue
            self.put_ch(chx)
            self.state+=1
            time.sleep(1)

    def clr_ch(self):
        for i in range(1,9):
            self.mx.maxOne(1,i,0)
            self.mx.maxOne(2,i,0)
            self.mx.maxOne(3,i,0)
            self.mx.maxOne(4,i,0)
            
    def put_ch(self,chx):
        fntx = CH_FONTS[chx]
        for i in range(1,9):
            bx, fntx = fntx[0],fntx[1:]
            self.mx.maxOne(1,i,bx)
            bx, fntx = fntx[0],fntx[1:]
            self.mx.maxOne(2,i,bx)
        for i in range(1,9):
            bx, fntx = fntx[0],fntx[1:]
            self.mx.maxOne(3,i,bx)
            bx, fntx = fntx[0],fntx[1:]
            self.mx.maxOne(4,i,bx)                        
            
                

x = XLED_CH()
x.loop()
