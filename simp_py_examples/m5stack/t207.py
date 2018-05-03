# t207.py
from machine import Timer
import time
def show(tt):
  from simp_py import tft
  tft.tft.text(0,100,'%02d:%02d:%02d' % tt)

def timer_isr(tm):
  from time import localtime    
  from micropython import schedule
  global show
  YYYY,MM,DD,hh,mm,ss,_,_=localtime()  
  schedule(show,(hh,mm,ss))

tm = Timer(1)
tm.init(period=1000, mode=1, callback= timer_isr)
