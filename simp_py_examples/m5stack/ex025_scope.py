# ex_fastscope.py
# author: C.F.Kwok
# date: 2018-1-6
from array import array
from simp_py import tft, mon
from math import sin, radians
from machine import Pin,ADC,DAC,Timer,PWM
import time

VOLT_F=1.4/419
VMAX=4095
PCOLOR=0xffff
class FASTSCOPE:
    global tft,mon,PCOLOR,VOLT_F,VMAX,Pin,ADC,DAC,array,PWM,Timer,time
    def __init__(self,inp,ref):
        self.buf=array('H',[])
        self.inp = ADC(Pin(inp,Pin.IN))
        self.init_plot()
        self.init_refw(ref)
        tft.tft.clear()
        self.init_timer()
        
    def init_timer(self):
        self.tm = Timer(2)
        self.tm.init(period=1,mode=1,callback=self.tcallback)

    def tcallback(self,tm):
        try:
            self.buf.append(self.inp.read())
        except Exception as e:
            mon.log_exc(e)
            
    def set_yscale(self):
        if self.vmax==0:
            self.yscale=1
        else:
            self.yscale = self.ymax / self.vmax
        
    def run(self):
        while 1:
            if len(self.buf)>self.xmax:
                self.plot_buf()
                self.buf=array('H',[])
            #self.out_refw()
            time.sleep(self.tscale)

    def init_refw(self,ref):
        self.duty=50
        self.out = Pin(ref,Pin.OUT)
        self.pwmout = PWM(self.out)
        self.pwmout.freq(10)
        self.pwmout.duty(self.duty)
        
    def out_refw(self):
        self.duty+=10
        if self.duty>=100:
            self.duty=0
        self.pwmout.duty(self.duty)            
            
    def init_plot(self):
        self.x=0
        self.tscale = 0.02
        self.vmax = 4096
        self.ymax = 199
        self.set_yscale()
        self.xmax = 320

    def new_plot(self):
        self.vmax = max(self.buf[:self.xmax])
        self.set_yscale()
        tft.tft.clear()

    def plot_buf(self):
        self.new_plot()
        v=0
        for x in range(self.xmax):
            v=self.buf[x]
            self.plot(x,v)
        self.show_value(v,self.vmax)
        
    def plot(self,x,v):
        y = self.ymax - round(v * self.yscale)
        tft.tft.pixel(x,y, PCOLOR)

    def show_value(self,v,vmax):
        volt = VOLT_F * v
        tft.tft.text(0,200,'%.2fV' % volt)
        tft.tft.text(100,200,'%s' % v)
        tft.tft.text(200,200,'%s' % vmax)
        
        
if __name__=='__main__':
    # (input/ADC, ref/DAC)
    t = FASTSCOPE(35,26)    
    t.run()            
