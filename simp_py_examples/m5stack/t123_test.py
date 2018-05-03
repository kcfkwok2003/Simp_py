from scbuf import Scbuf
from getfs import getfs

if __name__=='__main__':
  fs = getfs()
  bf = Scbuf(fs)
  bf.show()
  while True:
    time.sleep(1)
    bf.next()
    time.sleep(1)
    bf.prev()
