# t105.py
from simp_py import lcd
import time
cnt=10
while cnt >=0:
  lcd.text(10,100, 'count: %s '  % cnt)
  cnt -=1
  time.sleep(1)
