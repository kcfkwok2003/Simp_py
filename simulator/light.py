# light.py
import time
from simp_py import lcd
class Light:
    global lcd
    def __init__(self,x,y,r,on_color,off_color):
        self.x=x; self.y=y; self.r=r
        self.on=on_color; self.off=off_color
    def turn_on(self):
        lcd.circle(self.x,self.y,self.r,lcd.RED,self.on)
    def turn_off(self):
        lcd.circle(self.x,self.y,self.r,lcd.RED,self.off)

if __name__=='__main__':
    lcd.clear()
    light1 = Light(100,100,40,lcd.YELLOW,lcd.BLUE)
    light2 = Light(200,100,40,lcd.RED,lcd.BLUE)
    while True:
        light1.turn_on(); light2.turn_off()
        time.sleep(1)
        light1.turn_off(); light2.turn_on()
        time.sleep(1)
    
