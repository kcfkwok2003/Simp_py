# filename: friend.py
from simp_py import tft
lcd = tft.tft
class Friend:
  def __init__(self, name):
    self.name=name

  def hello(self):
    global lcd
    lcd.text(0,50, 'Hello %s' % self.name)

if __name__=='__main__':
  cf = Friend('C F')
  cf.hello()
