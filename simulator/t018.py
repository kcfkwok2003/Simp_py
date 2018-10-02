# t018.py

from machine import Pin,ADC
from simp_py import lcd
import time

from rtc import RTC
rtc_server= RTC()

from network import mqtt
connected =False
def connected_cb(task):
    global connected
    connected=True


mqttc = mqtt('/plant/drip','iot.eclipse.org',secure=False,connected_cb=connected_cb)
while not connected:
    time.sleep(0.1)

sensor = ADC(Pin(35,Pin.IN))
relay = Pin(26,Pin.OPEN_DRAIN)
relay_off = lambda : relay.value(1)
relay_on  = lambda : relay.value(0)
relay_off()

lcd.clear()
lcd.circle(270,50,30,0xffffff, lcd.NAVY)
published=False
while True:
    v = sensor.read()
    lcd.text(0,0,'sensor:%s     ' % v)
    if v > 1000:
        relay_on()
        lcd.circle(270,50,30,0xffffff, lcd.CYAN)
        if not published:
            time_stamp = rtc_server.now()
            lcd.text(0,50,time_stamp)
            mqttc.publish('/plant/drip',time_stamp)
            published=True
    else:
        published=False
        relay_off()
        lcd.circle(270,50,30,0xffffff, lcd.NAVY)
    time.sleep(0.1)
