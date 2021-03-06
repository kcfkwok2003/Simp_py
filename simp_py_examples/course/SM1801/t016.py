# t016.py
from machine import Pin,ADC
from simp_py import lcd
import time

sensor = ADC(Pin(35,Pin.IN))
relay = Pin(26,Pin.OPEN_DRAIN)
relay_off = lambda : relay.value(1)
relay_on  = lambda : relay.value(0)
relay_off()

lcd.clear()
lcd.circle(270,50,30,0xffffff, lcd.NAVY)

while True:
    v = sensor.read()
    lcd.text(0,0,'sensor:%s     ' % v)
    if v > 1000:
        relay_on()
        lcd.circle(270,50,30,0xffffff, lcd.CYAN)
    else:
        relay_off()
        lcd.circle(270,50,30,0xffffff, lcd.NAVY)
    time.sleep(0.1)

