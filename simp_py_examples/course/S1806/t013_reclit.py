# t013.py
from simp_py import lcd
from light import Light
import time
class RectLight(Light):
    global lcd
    def __init__(self,x,y,w,h,r,on_color,off_color):
        super().__init__(x,y,r,on_color,off_color)
        self.w=w; self.h=h
    def turn_on(self):
        lcd.roundrect(self.x,self.y,self.w,self.h,self.r,lcd.RED,self.on)
    def turn_off(self):
        lcd.roundrect(self.x,self.y,self.w,self.h,self.r,lcd.RED,self.off)

lcd.clear()
light1=RectLight(100,100,40,40,5,lcd.YELLOW,lcd.BLUE)
light2=RectLight(200,100,40,40,5,lcd.RED,lcd.BLUE)
while True:
    light1.turn_on(); light2.turn_off()
    time.sleep(1)
    light1.turn_off(); light2.turn_on()
    time.sleep(1)
    
