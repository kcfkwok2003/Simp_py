# t203.py
from machine import Pin,ADC
from simp_py import tft
p35 = ADC(Pin(35,Pin.IN))
while True:
  x= p35.read()
  tft.tft.text(0,100,'x=%d %04x   ' % (x,x))
  time.sleep(1)
