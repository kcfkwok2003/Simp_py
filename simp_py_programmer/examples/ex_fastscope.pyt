# ex_fastscope.py
# author: C.F.Kwok
# date: 2018-1-6
from array import array
from simp_py import oled, mon
from math import sin, radians
from machine import Pin,ADC,DAC,Timer,PWM
# 1.63 -> 1830
VOLT_F=1.63/1830
VMAX=4095
class FASTSCOPE:
    def __init__(self,inp,ref):
        global Pin,ADC,DAC,array,PWM
        global oled
        self.oled=oled
        self.buf=array('H',[])
        self.frm = oled.framebuf

        self.inp = ADC(Pin(inp,Pin.IN))
        self.init_plot()
        self.init_refw(ref)
        self.oled.fill(0)
        self.oled.show()
        self.init_timer()
        
    def init_timer(self):
        global Timer
        self.tm = Timer(3)
        self.tm.init(period=1,mode=1,callback=self.tcallback)

    def tcallback(self,tm):
        global mon
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
        import time
        while 1:
            if len(self.buf)>128:
                self.plot_buf()
                self.buf=array('H',[])
            self.out_refw()
            time.sleep(self.tscale)

    def init_refw(self,ref):
        self.duty=0
        self.out = Pin(ref,Pin.OUT)
        self.pwmout = PWM(self.out)
        self.pwmout.freq(5)
        self.pwmout.duty(self.duty * 100)
        
    def out_refw(self):
        self.duty+=1
        if self.duty>10:
            self.duty=0
        self.pwmout.duty(self.duty * 100)            
            
    def init_plot(self):
        self.x=0
        self.tscale = 0.02
        self.vmax = 4096
        self.ymax = 50
        self.set_yscale()
        self.xmax = 127

    def new_plot(self):
        self.vmax = max(self.buf[:128])
        self.set_yscale()
        self.oled.fill(0)

    def plot_buf(self):
        self.new_plot()
        v=0
        for x in range(128):
            v=self.buf[x]
            self.plot(x,v)
        self.show_value(v,self.vmax)
        self.oled.show()
        
    def plot(self,x,v):
        y = self.ymax - round(v * self.yscale)
        self.frm.pixel(x, y,1)

            
    def show_value(self,v,vmax):
        global VOLT_F
        self.frm.fill_rect(0,53,128,10,0)
        volt = VOLT_F * v
        self.oled.text('%.2fV' % volt, 0,53)
        self.oled.text('%s' % v, 50, 53)
        self.oled.text('%s' % vmax, 90,53)
        
        
# pin34: input
# pin25: ref
t = FASTSCOPE(34,25)    
t.run()            
