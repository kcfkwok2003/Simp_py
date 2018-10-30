from simp_py import tft
lcd = tft.tft
lcd.clear()
import time
cnt=10
while cnt >=0:
  lcd.text(10,10, 'count: %s '  % cnt)
  cnt -=1
  time.sleep(1)
