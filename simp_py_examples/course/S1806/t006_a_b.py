# t006.py
from simp_py import buttonA, buttonB
import time
while True:
  if buttonA.isPressed() and buttonB.isPressed():
    lcd.text(0,50, "A and B pressed")
  elif buttonA.isPressed() or buttonB.isPressed():
    lcd.text(0,50,"A or B pressed")
  else:
    lcd.text(0,50, "No button pressed")
  time.sleep(0.1)
