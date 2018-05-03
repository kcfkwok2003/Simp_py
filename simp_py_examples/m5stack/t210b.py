# t210b.py
from machine import Pin
from simp_py import tft
count=0
def counting(v):
  global count, show,a,b,ap
  av = a.value()
  if av !=ap:
    bv = b.value()
    if bv==av:
      count+=1
    else:
      count-=1
btnA= Pin(39,Pin.IN)
a = Pin(5, Pin.IN,Pin.PULL_UP)
b = Pin(2, Pin.IN,Pin.PULL_UP)
ap= a.value()
a.irq(counting,trigger=Pin.IRQ_RISING| Pin.IRQ_FALLING)
pcount=-1
while 1:
  if btnA.value()==0:
    count=0
  if pcount != count:
    pcount=count
    tft.tft.text(0,100,'count:%s    ' % (count,))
  #time.sleep(0.1)
