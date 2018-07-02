# t306.py
from machine import Pin
p2=Pin(2,Pin.OUT)
while True:
  p2.value(0)  # 0V
  time.sleep(2)
  p2.value(1)  # 3.3V 
  time.sleep(2)

