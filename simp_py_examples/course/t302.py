# t302.py
from machine import Pin
from simp_py import tft,mon
p2 = Pin(2, Pin.IN,Pin.PULL_DOWN)
p5 = Pin(5, Pin.IN,Pin.PULL_DOWN)
p35 = Pin(35, Pin.IN)
p36 = Pin(36, Pin.IN)
while True:
  v0 = p2.value()
  v1 = p5.value()
  v2 = p35.value()
  v3 = p36.value()
  v = v3 * 8 + v2 * 4 + v1 * 2 + v0 * 1
  s="v=%02d 0x%02x" % (v, v)
  tft.tft.text(0,100,s,0xff)
  time.sleep(0.1)
