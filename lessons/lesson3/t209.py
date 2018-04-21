# t209.py
from machine import Pin
count=0
def show(v):
  global count
  from simp_py import tft
  tft.tft.text(0,100,'%s %s' % (v,count))
def counting(v):
  from micropython import schedule
  global count, show
  count+=1
  try:
    schedule(show,(v))
  except:
    pass
p2 = Pin(2, Pin.IN,Pin.PULL_UP)
p2.irq(counting,trigger=Pin.IRQ_RISING)
