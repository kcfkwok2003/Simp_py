from simp_py import tft
from machine import I2C,Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S
from button import Button
btnA= Button(39,'A')
btnB=Button(38,'B')
btnC=Button(37,'C')

spk= Pin(25,Pin.OUT)
spk.value(0)
i2c = I2C(scl=Pin(22), sda=Pin(21))
mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf= SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500)
print("MPU9250 id:" +hex(sensor.whoami))
def close_eye():
  tft.tft.ellipse(100,120,40,40,15,0xffffff,0xffffff)
  tft.tft.ellipse(220,120,40,40,15,0xffffff,0xffffff)
  tft.tft.arc(100,80,40,2,135,225,0x00,0x00)
  tft.tft.arc(220,80,40,2,135,225,0x00,0x00)

def clip_v(v,scalex, maxv):
  v = v * scalex
  if v > maxv:
    return maxv
  return int(v)

def eye_pos(x,y,px,py):
  if px is not None:
    tft.tft.circle(100+px,120+py,15,0xffffff,0xffffff)
    tft.tft.circle(220+px,120+py,15,0xffffff,0xffffff)      
  tft.tft.circle(100+x,120+y,15,0x00,0x00)
  tft.tft.circle(220+x,120+y,15,0x00,0x00)
  
def open_eye(fill=True):
  if fill:
    tft.tft.ellipse(100,120,40,40,15,0x00,0xffffff)
    tft.tft.ellipse(220,120,40,40,15,0x00,0xffffff)
  else:
    tft.tft.ellipse(100,120,40,40,15,0x00)
    tft.tft.ellipse(220,120,40,40,15,0x00)
    
tft.tft.clear(0xffffff)
tft.tft.arc(100,100,40,6,-45,45,0x00,0x00)
tft.tft.arc(220,100,40,6,-45,45,0x00,0x00)
px=None
py=None
open_eye(fill=True)
isOpen=True
while True:
  x = clip_v(sensor.acceleration[0], 25, 25) 
  y = - clip_v(sensor.acceleration[1], 25, 25)
  if px is not None:
    if abs(px-x) >5 or abs(py-y) >5:
      if not isOpen:
        open_eye(fill=True)
        isOpen=True
      eye_pos(x,y,px,py)
      open_eye(fill=False)
      px=x
      py=y      
  else:
    isOpen=True
    eye_pos(x,y,px,py)
    open_eye(fill=False)    
    px=x
    py=y
  if btnA.pressed():
    #open_eye(fill=True)
    close_eye()
    isOpen=False
  if btnC.pressed():
    tft.off()
  if btnB.pressed():
    tft.on()
  time.sleep(0.1)
