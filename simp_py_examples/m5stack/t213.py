# t213.py
from simp_py import tft
from machine import Pin
tft.tft.text(0,100,'pulse output test')
en=Pin(35,Pin.OUT)
en.value(0)
pdirx =Pin(2,Pin.OUT); pstepx=Pin(5,Pin.OUT)
def step(direction,pdir,pstep,step):
  pdir.value(direction)
  for i in range(step):
    pstep.value(1)
    time.sleep_us(800)
    pstep.value(0)
    time.sleep_us(800)
while True:
  step(False,pdirx,pstepx,100)
  time.sleep(1)
  step(True,pdirx,pstepx,100)
  time.sleep(1)
  
