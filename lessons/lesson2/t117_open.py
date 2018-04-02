from simp_py import tft
lcd=tft.tft
f=open('test.py','r')
lines = f.readlines()
y=0
for line in lines[:10]:
  lcd.text(0,y, line)
  y+=20
time.sleep(1)
y=0
for line in lines[10:20]:
  lcd.text(0,y, line)
  y+=20
