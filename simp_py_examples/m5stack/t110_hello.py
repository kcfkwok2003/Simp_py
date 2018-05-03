# file name: hello.py
from simp_py import tft
lcd = tft.tft
def hello(namex):
  global lcd
  lcd.clear()
  lcd.text(0,0, 'hello')
  lcd.text(0,20,'your name is %s' % namex)

if __name__=='__main__':
  hello('C F')
