# t011_drwbtn.py
from simp_py import lcd
def drawButton(x,y,name):
    global lcd
    lcd.font(lcd.FONT_Comic, transparent=True)
    lcd.roundrect(x,y,80,40,5,lcd.RED,lcd.LIGHTGREY)
    lcd.text(x+5,y+5,name,lcd.BLACK)

drawButton(10,150,'ON')
drawButton(100,150,'OFF')

