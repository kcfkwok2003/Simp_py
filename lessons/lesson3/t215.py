# t215.py
from machine import Pin, PWM
import time
import array
p26 = PWM(Pin(26))
duty=0
p26.duty(duty)
while 1:
  while duty < 90:
    duty+=10
    p26.duty(duty)
    time.sleep(0.3)
  p26.duty(100)
  time.sleep(1)
  while duty >10:
    duty -=10
    p26.duty(duty)
    time.sleep(0.3)
  p26.duty(0)
  time.sleep(1)
  
