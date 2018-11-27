from simp_py import lcd
COLORS=[lcd.BLACK, lcd.NAVY, lcd.DARKGREEN]
for color in COLORS:
  lcd.rect(0, 100, 200,50,lcd.WHITE,color)
  time.sleep(1)
