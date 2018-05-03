# t210a.py
from machine import Pin
import time
from simp_py import tft
count=0
a=Pin(2,Pin.IN,Pin.PULL_UP) # dt
b=Pin(5,Pin.IN,Pin.PULL_UP) # clk
ap=a.value()
while 1:
  av=a.value()
  if av != ap:
    bv=b.value()
    if bv==av:
      count+=1
    else:
      count-=1
    tft.tft.text(0,100,'count:%d   ' % (count,))
    ap=av
    #time.sleep_us(500)
