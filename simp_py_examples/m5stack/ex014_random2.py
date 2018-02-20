from random import seed,uniform
from simp_py import tft, mon
import time
def run():
    global tft, time,seed,uniform
    seed(1)
    color=0xff
    for i in range(100):
        for j in range(100):
            x = round(uniform(0,1) * 320)
            y = round(uniform(0,1) * 240)
            z = x % 4
            if z==0:
                color=0xffffff
            elif z==1:
                color=0xff00
            elif z==2:
                color=0xff0000
            else:
                color=0xff
            tft.tft.pixel(x,y,color)
        time.sleep(0.02)
    time.sleep(1)
    seed(1)
    for i in range(100):
        for j in range(100):
            x = round(uniform(0,1) * 320)
            y = round(uniform(0,1) * 240)
            tft.tft.pixel(x,y,0)
        time.sleep(0.02)


if __name__=='__main__':
    run()
