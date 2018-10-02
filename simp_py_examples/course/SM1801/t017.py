# t017.py
import time
from simp_py import lcd
from rtc import RTC

x=RTC()
while True:
    s=x.now()
    lcd.text(0,100,s)
    time.sleep(1)
    
