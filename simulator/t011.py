# t011.py
from machine import Pin
from simp_py import lcd
#pin : 21 
px= Pin(39, Pin.IN)
while True:
  if px.value()==0:
    lcd.text(0,100," on  ")
  else:
    lcd.text(0,100,"off  ")
  time.sleep(0.1)

