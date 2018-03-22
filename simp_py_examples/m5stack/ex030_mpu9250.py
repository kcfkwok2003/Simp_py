# ref:https://github.com/tuupola/micropython-mpu9250

import utime
from machine import I2C, Pin
from mpu9250 import MPU9250
from simp_py import tft

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))
tft.tft.clear()
while True:
    a1,a2,a3= sensor.acceleration
    tft.tft.text(0,0,'acceleration')
    tft.tft.text(0,20,'%.3f      ' % a1)
    tft.tft.text(0,40,'%.3f      ' % a2)
    tft.tft.text(0,60,'%.3f      ' % a3)
    
    g1,g2,g3 = sensor.gyro
    tft.tft.text(0,80,'gyro')
    tft.tft.text(0,100,'%.3f      ' % g1)
    tft.tft.text(0,120,'%.3f      ' % g2)
    tft.tft.text(0,140,'%.3f      ' % g3)
    
    m1,m2,m3 = sensor.magnetic
    tft.tft.text(0,160,'magnetic')
    tft.tft.text(0,180,'%.3f      ' % m1)
    tft.tft.text(0,200,'%.3f      ' % m2)
    tft.tft.text(0,220,'%.3f      ' % m3)    
    
    utime.sleep_ms(300)
