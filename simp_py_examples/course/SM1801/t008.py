# t008.py
from simp_py import lcd,buttonA
import time
cnt=10
while cnt >=0:
 lcd.text(10,10, "count: %s "  % cnt)
 cnt -=1
 if buttonA.isPressed():
   continue
 time.sleep(1)
