from simp_py import lcd
import random as r
import time as t
r.seed(10)
for i in range(100):
    for j in range(100):
        x = r.randint(1,319)
        y = r.randint(1,239)
        z = r.randint(0xff00,0xffffff)
        lcd.pixel(x,y,z)
    t.sleep(0.1)
    
r.seed(10)
for i in range(100):
    for j in range(100):
        x = r.randint(1,319)
        y = r.randint(1,239)
        z = r.randint(0xff00,0xffffff)
        lcd.pixel(x,y,0)
    t.sleep(0.1)    
