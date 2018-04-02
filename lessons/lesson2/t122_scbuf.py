# scbuf.py
from buf import Buf

class Scbuf(Buf):
  def __init__(self, data, n=10):
    super().__init__(data,n)
    self.s=0

  def prev(self):
    self.s  -= self.n
    if self.s <0:
      self.s=0
    self.show(self.s)

  def next(self):
    if (self.s + self.n) < len(self.data):
      self.s += self.n
    self.show(self.s)

if __name__=='__main__':
  dt=['111','222','333']
  bf=Scbuf(dt)
  bf.show()
