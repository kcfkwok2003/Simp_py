from simp_py import tft
from random import seed, uniform
import time
from machine import Pin
from button import Button
btnA = Pin(39, Pin.IN)
btnB = Pin(38, Pin.IN)
btnC = Pin(37, Pin.IN)
seed(int(time.time()))
class SNAKE:
  global tft,uniform
  def __init__(self):
    self.snake=[[4,10],[4,9],[4,8]]
    self.dirx=0
    self.diry=1
    self.food=[10,20]
    tft.tft.clear()
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
    tft.tft.text(x*10,y*10,'*')

  def place_snake(self):
    for x,y in self.snake:
      tft.tft.text(x*10,y*10,'#')

  def go_dir(self,x,y):
    x+= self.dirx
    if x*10 > 320:
      x=0
    y+= self.diry
    if y*10 > 240:
      y=0
    return x,y

  def go_left(self):
    self.dirx=-1

  def go_right(self):
    self.dirx=1

  def go_down(self):
    self.diry=1
    self.dirx=0
    
  def go(self):
    xt,yt = self.snake.pop()
    tft.tft.text(xt*10,yt*10,' ')
    x,y = self.snake[0]
    x,y = self.go_dir(x,y)
    self.snake.insert(0,[x,y])
    if self.food == [x,y]:
      self.snake.append([xt,yt])
      self.place_food()
    self.place_snake()
    
if __name__=='__main__':
  snake=SNAKE()
  
  def Apressed(v):
    global snake
    snake.go_left()
      
  def Bpressed(v):
    global snake
    snake.go_down()
      
  def Cpressed(v):
    global snake
    snake.go_right()
        

  btnA.irq(Apressed, trigger=Pin.IRQ_FALLING)
  btnB.irq(Bpressed, trigger=Pin.IRQ_FALLING)
  btnC.irq(Cpressed, trigger=Pin.IRQ_FALLING)

  while True:
    time.sleep(0.2)
    snake.go()
