# t204.py
# 54 -> 0V
# 500 -> 1.60V
# v = 0.00359 x - 0.194
from machine import Pin,ADC,DAC
from simp_py import tft
p35 = ADC(Pin(35,Pin.IN))
p25 = DAC(Pin(25))  # suppress click sound
while True:
  x= p35.read()
  tft.tft.text(0,100,'x=%d %04x   ' % (x,x))
  v = 0.00359 * x - 0.194
  tft.tft.text(0,120,'v=%.02fV     ' % v)
  time.sleep(1)
