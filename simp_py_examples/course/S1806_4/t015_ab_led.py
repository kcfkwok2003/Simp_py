# t015.py (A:on, B:off)
import time
from simp_py import lcd
from button import Button
from machine import Pin
led = Pin(26,Pin.OUT)
led.value(0)
buttonA= Button(39)
buttonB= Button(38)

apressed=False
bpressed=False
while True:
    if buttonA.isPressed():
        if not apressed:
            apressed=True
            led.value(1)
    else:
        apressed=False
    if buttonB.isPressed():
        if not bpressed:
            bpressed=True
            led.value(0)
    else:
        apressed=False
    time.sleep(0.1)
