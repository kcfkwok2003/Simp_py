# filename: button.py
from simp_py import lcd

class Button:
  def __init__(self,pin,name):
    from machine import Pin
    self.inp = Pin(pin, Pin.IN)
    self.name = name

  def isPressed(self):
    return self.inp.value()==0

if __name__=='__main__':
  btnA = Button(39,'A')
  lcd.text(0,15,'%s pressed:%s' % (btnA.name, btnA.isPressed()))
