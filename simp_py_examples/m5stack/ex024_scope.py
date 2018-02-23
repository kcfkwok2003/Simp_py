# ex_scope.py
# author: C.F.Kwok
# date: 2018-2-23
from simp_py import tft
from math import sin, radians

VOLT_F=1.4/419
PCOLOR=0xffff
class SCOPE:
    global tft, PCOLOR,VOLT_F
    def __init__(self,inp,ref):
        from machine import Pin,ADC,DAC
        self.out = Pin(ref,Pin.OUT)
        self.dac = DAC(self.out)
        self.inp = ADC(Pin(inp,Pin.IN))
        self.init_plot()
        self.init_refw()
        tft.tft.clear()

    def set_yscale(self):
        if self.vmax==0:
            self.yscale=1
        else:
            self.yscale = self.ymax / self.vmax
        
    def run(self):
        import time
        while 1:
            v = self.inp.read()
            self.out_refw()
            self.plot(v)
            time.sleep(self.tscale)

    def init_refw(self):
        self.ang=0
        self.TCNT=10
        self.tcnt=self.TCNT

    def out_refw(self):
        global sin, radians
        v = int(round((sin(radians(self.ang * 4 )) + 1.05) * 120))
        self.dac.write(v)
        self.ang+=1
        if self.ang>=90:
            self.ang=0
            
    def init_plot(self):
        self.x=0
        self.tscale = 0.02
        self.vmax = 4096
        self.nvmax=0
        self.ymax = 199
        self.set_yscale()
        self.xmax = 320

    def new_plot(self):
        self.x=0
        self.vmax = self.nvmax
        self.nvmax =0
        self.set_yscale()
        tft.tft.clear()
        
    def plot(self,v):
        if v > self.nvmax:
            self.nvmax = v
        if self.x==0:
            self.x+=1
            return
        y = self.ymax - round(v * self.yscale)
        tft.tft.pixel(self.x,y,PCOLOR)
        self.show_value(v,self.vmax)
        self.x+=1
        if self.x>=self.xmax:
            self.new_plot()
            
    def show_value(self,v,vmax):
        #tft.tft.rect(0,200,320,40,0,0)
        volt = VOLT_F * v
        tft.tft.text(0,200,'%.2fV' % volt)
        tft.tft.text(100,200,'%s' % v)
        tft.tft.text(200,200,'%s' % vmax)
        
        
if __name__=='__main__':
    #  (input/AD, ref/DA)
    t = SCOPE(35,26)    
    t.run()            
