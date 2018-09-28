# t017.py
from machine import Pin,ADC, RTC
from simp_py import lcd
import time

sensor = ADC(Pin(35,Pin.IN))
relay = Pin(26,Pin.OPEN_DRAIN)
relay_off = lambda : relay.value(1)
relay_on  = lambda : relay.value(0)
relay_off()

lcd.clear()
lcd.circle(270,50,30,0xffffff, lcd.NAVY)

rtc=RTC()
timex = rtc.now()
msg = 'started@%s   ' % timex
lcd.text(0,0,msg)
while True:
    v = sensor.read()
    lcd.text(0,0,'sensor:%s     ' % v)
    if v > 1000:
        relay_on()
        timex = rtc.now()
        msg = 'drip@%s    ' % timex
        lcd.text(0,0,msg)
        lcd.circle(270,50,30,0xffffff, lcd.CYAN)
    else:
        relay_off()
        lcd.circle(270,50,30,0xffffff, lcd.NAVY)
    time.sleep(0.1)

