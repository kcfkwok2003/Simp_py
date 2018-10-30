from simp_py import tft
lcd = tft.tft
listx = range(100)   # range() ->  listx : [0,1,2,3, … 99]
color= 0xff0000
for x in listx:      # keyword for, in
  lcd.pixel(x, 50, color)
