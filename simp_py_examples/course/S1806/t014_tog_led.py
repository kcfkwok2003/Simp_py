# t014.py (toggle)
import time
from simp_py import lcd
from button import Button
from machine import Pin

led = Pin(26,Pin.OUT)
led.value(0)
buttonA= Button(39)
apressed=False
while True:
    if buttonA.isPressed():
        if not apressed:
            apressed=True
            led.value(1- led.value())
    else:
        if apressed:
            apressed=False
            #led.value(0)
    time.sleep(0.1)
