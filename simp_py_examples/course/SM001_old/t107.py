# t107.py
from simp_py import lcd
import time
lcd.clear()
while True:
  lcd.circle(100,100,50,lcd.RED,lcd.YELLOW)
  time.sleep(1)
  lcd.circle(100,100,50,lcd.RED,lcd.BLACK)
  time.sleep(1)
