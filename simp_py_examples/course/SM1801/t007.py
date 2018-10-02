# t007.py
from simp_py import lcd
import time
cnt=10
while cnt >=0:
 lcd.text(10,10, "count: %s  "  % cnt)
 cnt -=1
 time.sleep(1)



