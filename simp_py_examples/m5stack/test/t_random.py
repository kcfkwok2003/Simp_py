# t_random.py
from simp_py import lcd
import random as r
import time
r.seed(10)
for i in range(100):
    for j in range(100):
        x = r.randint(1,319)
        y = r.randint(1,239)
        z = r.randint(0xff00,0xffffff)
        lcd.pixel(x,y,z)
    time.sleep(0.1)
r.seed(10)
for i in range(100):
    for j in range(100):
        x = r.randint(1,319)
        y = r.randint(1,239)
        z = r.randint(0xff00,0xffffff)        
        lcd.pixel(x,y,0)
    time.sleep(0.1)
    

    
