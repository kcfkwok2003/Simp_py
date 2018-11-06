# button.py
from input import DigitalInput
from machine import Pin

class Button(DigitalInput):
  def __init__(self,pin_no, callback=None, trigger=Pin.IRQ_FALLING):
    pin =Pin(pin_no, Pin.IN)
    DigitalInput.__init__(self, pin,callback=callback, trigger=trigger) 

  def isPressed(self):
    return self.pin.value()==0

if __name__=='__main__':
  from simp_py import lcd
  btnA = Button(39)
  while True:
    if btnA.isPressed():
      lcd.text(0,15,'buttonA pressed')
    else:
      lcd.text(0,15,'buttonA not pressed')
