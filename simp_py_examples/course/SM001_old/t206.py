from simp_py import tft
lcd = tft.tft
lcd.clear()
from button import Button
btnA = Button(39,'A')
import time
cnt=10
while cnt >=0:
  lcd.text(10,10, 'count: %s '  % cnt)
  cnt -=1
  if btnA.pressed():
    continue
  time.sleep(1)
