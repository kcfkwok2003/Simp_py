# ex_sin.py
# author: C.F.Kwok
# date: 2018-1-5
from simp_py import oled
from math import sin, radians
import time
class SIN:
    def __init__(self):
        global oled
        self.oled = oled
        self.frm = oled.framebuf
        self.init_plot()
        self.oled.fill(0)
        self.oled.show()
        
    def run(self):
        global sin, radians        
        ang=0
        for x in range(128):
            v = int(round((sin(radians(ang * 4 )) + 1.05) * 120))
            self.plot(x,v)
            ang +=1
            if ang>=90:
                ang=0
            time.sleep(0.02)
            
    def init_plot(self):
        self.tscale = 0.02
        self.vmax = 255
        self.ymax = 50
        self.xmax = 127
        self.yscale = self.ymax / self.vmax
        
    def plot(self,x,v):
        y = self.ymax - round(v * self.yscale)
        self.frm.pixel(x, y,1)
        self.show_value(v,self.vmax)
        self.oled.show()
            
    def show_value(self,v,vmax):
        self.frm.fill_rect(0,53,128,10,0)
        self.oled.text('%s' % v, 50, 53)
        self.oled.text('%s' % vmax, 90,53)
        
        
if __name__=='__main__':
    t = SIN()
    t.run()            

