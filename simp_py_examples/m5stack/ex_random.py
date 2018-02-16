from simp_py import tft,mon
from random import random
import time
def run():
    global tft, time, random
    while 1:
        x = round(random() * 320)
        y = round(random() * 240)
        z = round(random() * 0xffffff)
        tft.tft.pixel(x,y,z)
        mon.data['x']=x
        mon.data['y']=y
        time.sleep(0.02)
    
run()
