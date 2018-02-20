# ex_sin.py
# author: C.F.Kwok
# date: 2018-1-5
from simp_py import tft
from math import sin, radians
import time
class SIN:
    global tft
    def __init__(self):
        self.init_plot()
        tft.tft.clear()
        
    def run(self):
        global sin, radians        
        ang=0
        for x in range(320):
            v = int(round((sin(radians(ang * 4 )) + 1.05) * 120))
            self.plot(x,v)
            ang +=1
            if ang>=90:
                ang=0
            time.sleep(0.02)
            
    def init_plot(self):
        self.tscale = 0.02
        self.vmax = 255
        self.ymax = 200
        self.xmax = 319
        self.yscale = self.ymax / self.vmax
        
    def plot(self,x,v):
        y = self.ymax - round(v * self.yscale)
        tft.tft.pixel(x, y,0xffff00)
        self.show_value(v,self.vmax)
            
    def show_value(self,v,vmax):
        tft.tft.text(10,210,'%s' % v)
        tft.tft.text(100,210,'%s' % vmax)
        
        
if __name__=='__main__':
    t = SIN()
    t.run()            

