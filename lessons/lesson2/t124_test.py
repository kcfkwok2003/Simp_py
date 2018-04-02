import time
from button import Button
from scbuf import Scbuf
from getfs import getfs

bf = Scbuf(getfs())
bf.show()
btnA = Button(39,'A')
btnB = Button(38,'B')
while True:
  if btnA.pressed():
    bf.next()
  if btnB.pressed():
    bf.prev()
  time.sleep(1)
