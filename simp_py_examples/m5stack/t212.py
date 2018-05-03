# t212.py
from machine import Pin
p26=Pin(26,Pin.OPEN_DRAIN)
while True:
  p26.value(0)  # 0V
  time.sleep(2)
  p26.value(1)  # ?V 
  time.sleep(2)

