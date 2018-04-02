from simp_py import tft
lcd = tft.tft
color= 0xff0000
xs = range(10,100,2)
ys = range(20,200,4)
zs = zip(xs,ys)
for x,y in zs:
  lcd.pixel(x, y, color)
