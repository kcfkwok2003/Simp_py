# t206.py
from machine import Pin

count=0
def show(v):
  global count
  from simp_py import tft
  tft.tft.text(0,100,'%s %s' % (v,count))
  
def keypressed(v):
  from micropython import schedule    
  global count, show
  count+=1
  schedule(show,(v))

p39= Pin(39,Pin.IN)
p39.irq(keypressed,trigger=Pin.IRQ_FALLING)
