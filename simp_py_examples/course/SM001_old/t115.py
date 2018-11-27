from simp_py import tft
lcd = tft.tft
from button import Button
pins = [39,38,37]   # list
names ={ 39:'Button A', 38: 'Button B', 37: 'Button C'}  # dictionary
buttons =[]
for pin in pins:
  btnx = Button(pin, names[pin])
  buttons.append(btnx)
while True:
  for btnx in buttons:
    if btnx.pressed():
      lcd.text(0,50, '%s is pressed' % btnx.name)
