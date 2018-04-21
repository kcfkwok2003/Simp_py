# t203.py
from machine import Pin,ADC,DAC
from simp_py import tft
p35 = ADC(Pin(35))
p25 = DAC(Pin(25))  # suppress speaker noise
while True:
  x= p35.read()
  p25.write(0)     # suppress speaker noise
  tft.tft.text(0,100,'x=%d %04x   ' % (x,x))
  time.sleep(1)

