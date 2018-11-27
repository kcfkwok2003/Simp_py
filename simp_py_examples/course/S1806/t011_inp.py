# t011.py
from machine import Pin
from simp_py import lcd
import time
inp= Pin(21, Pin.IN)
while True:
  if inp.value()==0:
    lcd.text(0,100,"on ")
  else:
    lcd.text(0,100,"off")
  time.sleep(0.1)
