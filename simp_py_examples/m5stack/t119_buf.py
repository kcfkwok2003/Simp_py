# buf.py
from simp_py import tft
lcd=tft.tft
class Buf:
  global lcd
  def __init__(self, data, n=10):
    self.data=data
    self.data.sort()
    self.n=n

  def show(self, s=0):
    y=0
    lcd.clear()
    for item in self.data[s:s+self.n]:
      lcd.text(0,y,item)
      y+=20

if __name__=='__main__':
  dt=['aaa','bbb','ccc']
  bf = Buf(dt)
  bf.show()
