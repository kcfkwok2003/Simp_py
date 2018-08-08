from button import Button
from simp_py import tft
buttonB = Button(38,'B')
buttonC = Button(37,'C')
while True:
  if buttonB.pressed():
    tft.on()
  if buttonC.pressed():
    tft.off()
