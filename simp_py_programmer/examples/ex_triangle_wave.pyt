# ex_triangle_wave.py
# author: C.F.Kwok
# date: 2017-12-18
from simp_py import oled
class TRIANGLE_WAVE:
    def __init__(self):
        from machine import Pin,DAC
        p25 = Pin(25,Pin.OUT)
        self.da25 = DAC(p25)
        
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
            time.sleep(0.02)
            

t = TRIANGLE_WAVE()
t.run()
