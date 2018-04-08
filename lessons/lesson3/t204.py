# t204.py
# 100 -> 0.295V
# 600 -> 2.06V
# v = 0.00353 x - 0.058
from machine import Pin,ADC
from simp_py import tft
p35 = ADC(Pin(35,Pin.IN))
while True:
  x= p35.read()
  tft.tft.text(0,100,'x=%d %04x   ' % (x,x))
  v = 0.00353 * x - 0.058
  tft.tft.text(0,120,'v=%.02fV   ' % v)
  time.sleep(1)
