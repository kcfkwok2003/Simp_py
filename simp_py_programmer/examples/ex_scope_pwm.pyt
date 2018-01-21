# ex_scope_pwm.py
# author: C.F.Kwok
# date: 2018-1-5
from simp_py import oled
from math import sin, radians
from machine import Pin,ADC,DAC,PWM
# 1.63v -> 1830
VOLT_F=1.63/1830
class SCOPE:
    def __init__(self,inp,ref):
        global Pin,ADC,DAC
        global oled
        self.oled=oled
        self.frm = oled.framebuf
        self.out = Pin(ref,Pin.OUT)
        self.dac = DAC(self.out)
        self.inp = ADC(Pin(inp,Pin.IN))
        self.init_plot()
        self.init_refw()
        self.init_pwms()
        self.oled.fill(0)
        self.oled.show()

    def init_pwms(self):
        global PWM,Pin
        pin_nos=bytearray([2,17,5,18,23,19,22,21])
        self.num_pins=len(pin_nos)
        Pwms=[]
        for i in range(self.num_pins):
            print('i:%d' % i)
            pn = pin_nos[i]
            print('pn: i:%s %s' % (i,pn))
            Pwmx = PWM(Pin(pin_nos[i], Pin.OUT))
            Pwms.append(Pwmx)
        for i in range(self.num_pins):
            Pwms[i].freq(500)
            Pwms[i].duty(0)
        self.Pwms=Pwms
        
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
        self.ymax = 50
        self.set_yscale()
        self.xmax = 127

    def new_plot(self):
        self.x=0
        self.vmax = self.nvmax
        self.nvmax =0
        self.set_yscale()
        self.oled.fill(0)
        self.oled.show()
        
    def plot(self,v):
        if v > self.nvmax:
            self.nvmax = v
        if self.x==0:
            self.x+=1
            return
        y = self.ymax - round(v * self.yscale)
        self.frm.pixel(self.x, y,1)
        self.show_value(v,self.vmax)
        self.pwm_value(v)
        self.oled.show()
        self.x+=1
        if self.x>=self.xmax:
            self.new_plot()
            
    def show_value(self,v,vmax):
        global VOLT_F
        self.frm.fill_rect(0,53,128,10,0)
        volt = VOLT_F * v
        self.oled.text('%.2fV' % volt, 0,53)
        self.oled.text('%s' % v, 50, 53)
        self.oled.text('%s' % vmax, 90,53)

    def pwm_value(self,v):
        for i in range(8):
            self.Pwms[i].duty(0)
        n,r = divmod(v,512)
        for i in range(n):
            self.Pwms[i].duty(512)
        self.Pwms[n].duty(r)
        
# pin34: input
# pin25: ref
t = SCOPE(34,25)    
t.run()            
