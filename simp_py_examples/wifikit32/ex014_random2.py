from random import seed,uniform
from simp_py import oled, mon
import time
def run():
    global oled, time,seed,uniform
    frm = oled.framebuf
    seed(1)
    for i in range(100):
        for j in range(100):
            x = round(uniform(0,1) * 128)
            y = round(uniform(0,1) * 64)
            frm.pixel(x,y,1)
        oled.show()
        time.sleep(0.02)
    oled.fill(1)
    oled.show()
    time.sleep(1)
    seed(1)
    for i in range(100):
        for j in range(100):
            x = round(uniform(0,1) * 128)
            y = round(uniform(0,1) * 64)
            frm.pixel(x,y,0)
        oled.show()
        time.sleep(0.02)
    oled.fill(0)
    oled.show()

if __name__=='__main__':
    run()
