# t012.py
from machine import Pin
led=Pin(26,Pin.OUT)
while True:
 led.value(0)  # 0V
 time.sleep(1)
 led.value(1)  # 3.3V
 time.sleep(1)

