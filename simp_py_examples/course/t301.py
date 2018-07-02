# t301.py
from machine import Pin
from simp_py import tft
p21= Pin(21, Pin.IN)
while True:
  if p21.value()==0:
    tft.tft.text(0,100," on")
  else:
    tft.tft.text(0,100,"off")
  time.sleep(0.1)
