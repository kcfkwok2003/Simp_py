from simp_py import tft
lcd = tft.tft
lcd.clear()
from machine import Pin
btnA = Pin(39, Pin.IN)
while True:
  if btnA.value() == 0:
    lcd.text(10,10,'A is pressed ')
  else:
    lcd.text(10,10,'A is released')
  time.sleep(0.1)
