# t005.py
from simp_py import buttonA, buttonB, buttonC
import time
names = ['A','B','C']   # list
buttons ={ 'A': buttonA, 'B': buttonB, 
'C': buttonC}  # dictionary

while True:
  for name in names:
    btnx = buttons[name] 
    if btnx.isPressed():
      lcd.text(0,50, "%s is pressed" % name)
  time.sleep(0.1)
