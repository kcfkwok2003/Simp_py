# button.py
from input import DigitalInput
from machine import Pin
import time

class Button(DigitalInput):
  def __init__(self,pin_no, callback=None, trigger=Pin.IRQ_FALLING):
    pin =Pin(pin_no, Pin.IN)
    DigitalInput.__init__(self, pin,callback=callback, trigger=trigger) 

  def isPressed(self):
    return self.pin.value()==0

if __name__=='__main__':
  from simp_py import lcd
  bcnt=0
  def bpressed(v):
    global bcnt
    bcnt+=1
    #print('v:%s %s %s' % (v.pid, v, Pin(38)))
    lcd.text(0,30,'bcnt:%s' % bcnt)
      
  btnA = Button(39)
  btnB = Button(38, bpressed,trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING)
  while True:
    if btnA.isPressed():
      lcd.text(0,15,'buttonA pressed')
    else:
      lcd.text(0,15,'buttonA not pressed')
    time.sleep(0.1)
