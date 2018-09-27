# t015.py
from machine import Pin,ADC
from simp_py import lcd
import time
sensor = ADC(Pin(35,Pin.IN))
while True:
 x= sensor.read()
 lcd.text(0,100,'x=%d %04x   ' % (x,x))
 time.sleep(1)

