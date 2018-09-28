# t004.py
from simp_py import lcd

color= 0xff0000
xs = range(10,100,2)
ys = range(20,200,4)
zs = zip(xs,ys)  # ((10,20), (20,40), ..)
for x,y in zs:
  lcd.pixel(x, y, color)
