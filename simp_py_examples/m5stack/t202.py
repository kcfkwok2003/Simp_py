# t202.py
from machine import Pin
from simp_py import tft,mon
pins=[]
for px in [2,5]:
  pins.append(Pin(px, Pin.IN,Pin.PULL_DOWN))
for px in [35,36]:
  pins.append(Pin(px, Pin.IN))  
v=0
while True:
  v=0
  for p in pins:
    v= v << 1
    if p.value()==1:
      v= v | 1
  s="v=%02d 0x%02x" % (v, v)
  tft.tft.text(0,100,s,0xff)
  time.sleep(0.1)
