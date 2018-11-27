# t008.py
from simp_py import lcd
import time
from button import Button
buttonA=Button(39)
cnt=10
while cnt >=0:
  lcd.text(10,10, "count: %s  "  % cnt)
  cnt -=1
  if buttonA.isPressed():
    break
  time.sleep(1)



