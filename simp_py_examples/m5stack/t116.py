from simp_py import tft
lcd= tft.tft
from button import Button
btnA = Button(39,'A')
btnB = Button(38,'B')
while True:
  if btnA.pressed() and btnB.pressed():
    lcd.text(0,50, "A and B pressed")
  elif btnA.pressed() or btnB.pressed():
    lcd.text(0,50,"A or B pressed")
  else:
    lcd.text(0,50, "No button pressed")
  time.sleep(0.1)
