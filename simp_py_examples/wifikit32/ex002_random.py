from random import random
from simp_py import oled, mon
import time
def run():
    global oled, time, random
    frm = oled.framebuf
    while 1:
        x = round(random() * 128)
        y = round(random() * 64)
        frm.pixel(x,y,1)
        oled.show()
        mon.data['x']=x
        mon.data['y']=y
        time.sleep(0.02)
    
run()
