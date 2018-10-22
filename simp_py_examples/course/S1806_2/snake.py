from simp_py import tft,lcd
from random import seed, uniform
import time
from machine import Pin
from button import Button

seed(int(time.time()))
class ButtonDir:
  def __init__(self):
    self.x=0; self.y=0
    self.hz=0 # button direction 1 : vertical, 0: horizontal
    lcd.text(self.x,self.y,'|')

  def is_hz(self):
    return self.hz

  def change(self):
    self.hz = 1 - self.hz
    if self.hz:
      lcd.textClear(self.x,self.y,'|')
      lcd.text(self.x,self.y,'=')
    else:
      lcd.textClear(self.x,self.y,'=')      
      lcd.text(self.x,self.y,'|')
      
class SNAKE:
  global lcd,tft,uniform
  def __init__(self):
    self.snake=[[4,10],[4,9],[4,8]]
    self.dirx=0
    self.diry=1
    self.food=[10,20]

    self.place_food()
    self.place_snake()
    
  def place_food(self):
    x = round(uniform(1,30))
    y = round(uniform(1,20))
    while True:
      if [x,y] in self.snake:
        x = round(uniform(1,30))
        y = round(uniform(1,20))
      else:
        break
    self.food=[x,y]
    lcd.text(x*10,y*10,'*')

  def place_snake(self):
    for x,y in self.snake:
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
    xt,yt = self.snake.pop()
    lcd.textClear(xt*10,yt*10,'#')
    x,y = self.snake[0]
    x,y = self.go_dir(x,y)
    self.snake.insert(0,[x,y])
    if self.food == [x,y]:
      self.snake.append([xt,yt])
      self.place_food()
    self.place_snake()
    
if __name__=='__main__':
  lcd.clear()  
  bdir = ButtonDir()
  snake=SNAKE()
  
  def Apressed(v):
    global snake,tft,bdir
    print('Apressed')
    if bdir.is_hz():
      snake.go_left()
    else:
      snake.go_up()
      
  def Bpressed(v):
    global snake,tft,bdir
    print('Bpressed')
    bdir.change()
    tft.on()
      
  def Cpressed(v):
    global snake,btnA
    print('Cpressed')
    if btnA.isPressed():
      tft.off()
    if bdir.is_hz():
      snake.go_right()
    else:
      snake.go_down()
      
  btnA = Button(39,Apressed,trigger=Pin.IRQ_FALLING)
  btnB = Button(38,Bpressed, trigger=Pin.IRQ_FALLING)
  btnC = Button(37,Cpressed, trigger=Pin.IRQ_FALLING)

  while True:
    time.sleep(0.2)
    snake.go()
