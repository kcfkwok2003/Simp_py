from simp_py import tft
lcd = tft.tft
def hello(your_name):
  global lcd
  lcd.clear()
  lcd.text(0,0,'hello')
  lcd.text(0,20,'your name is %s' % your_name)

hello('CF')
