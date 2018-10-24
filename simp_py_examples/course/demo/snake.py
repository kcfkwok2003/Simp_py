from simp_py import tft,lcd
from random import seed, uniform
import time
from machine import Pin
from button import Button

seed(int(time.time()))

class FOOD:
  global lcd
  def __init__(self):
    self.pos=[10,20]

  def new(self,trunk):
    x = round(uniform(1,30))
    y = round(uniform(1,20))
    while True:
      if [x,y] in trunk:
        x = round(uniform(1,30))
        y = round(uniform(1,20))
      else:
        break
    self.pos=[x,y]
    lcd.text(x*10,y*10,'*')    

  def is_catch(self,x,y):
    if self.pos==[x,y]:
      return True
    
class SNAKE:
  global lcd,tft,uniform,food
  def __init__(self):
    self.trunk=[[4,10],[4,9],[4,8]]
    self.dirx=0
    self.diry=1
    food.new(self.trunk)
    self.draw()
    
  def draw(self):
    for x,y in self.trunk:
      lcd.text(x*10,y*10,'#')

  def go_dir(self,x,y):
    x+= self.dirx
    if x*10 > 320:
      x=0
    if x<0:
      x=32
    y+= self.diry
    if y*10 > 240:
      y=0
    if y<0:
      y=24
      
    return x,y

  def go_left(self):
    self.dirx=-1
    self.diry=0
    
  def go_right(self):
    self.dirx=1
    self.diry=0
    
  def go_down(self):
    self.diry=1
    self.dirx=0

  def go_up(self):
    self.diry=-1
    self.dirx=0
    
  def go(self):
    xt,yt = self.trunk.pop()
    lcd.textClear(xt*10,yt*10,'#')
    x,y = self.trunk[0]
    x,y = self.go_dir(x,y)
    self.trunk.insert(0,[x,y])
    if food.is_catch(x,y):
      self.trunk.append([xt,yt])
      food.new(self.trunk)
    self.draw()
    
if __name__=='__main__':
  lcd.clear()
  food = FOOD()
  snake=SNAKE()
  
  def Apressed(v):
    global snake,tft
    print('Apressed')
    snake.go_left()
      
  def Bpressed(v):
    global snake,tft
    print('Bpressed')
    tft.on()
    if snake.diry==0:
      snake.go_up()
    else:
      if snake.diry==1:
        snake.go_up()
      else:
        snake.go_down()
        
  def Cpressed(v):
    global snake,btnA
    print('Cpressed')
    if btnA.isPressed():
      tft.off()
    snake.go_right()
      
  btnA = Button(39,Apressed,trigger=Pin.IRQ_FALLING)
  btnB = Button(38,Bpressed, trigger=Pin.IRQ_FALLING)
  btnC = Button(37,Cpressed, trigger=Pin.IRQ_FALLING)

  while True:
    time.sleep(0.2)
    snake.go()
