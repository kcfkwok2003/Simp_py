# ex_triwave_scope.py
# author: C.F.Kwok
# date: 2017-12-27
from simp_py import oled
class TRIWAVE_SCOPE:
    def __init__(self):
        global oled
        from machine import Pin,DAC
        self.oled = oled
        self.frm = self.oled.framebuf
        p25 = Pin(25,Pin.OUT)
        self.da25 = DAC(p25)
        self.x=0
        self.yscale=64.0/255
        self.oled.fill(0)
        self.oled.show()
        
    def run(self):
        import time
        step=40
        v=0
        inc=step
        while 1:
            self.da25.write(v)
            v+=inc
            if v>=255:
                v=255
                inc=-step
            elif v<=0:
                v=0
                inc=+step
            self.plot(v)
            time.sleep(0.02)

    def plot(self,v):
        y = round(v * self.yscale)
        self.frm.pixel(self.x, y,1)
        self.oled.show()
        self.x+=1
        if self.x>=127:
            self.x=0
            self.oled.fill(0)
            self.oled.show()
            

t = TRIWAVE_SCOPE()    
t.run()
