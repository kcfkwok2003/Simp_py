# ref:https://github.com/tuupola/micropython-mpu9250

import utime
from machine import I2C, Pin
from mpu9250 import MPU9250
from mpu6500 import MPU6500, SF_G, SF_DEG_S
from simp_py import tft

i2c = I2C(scl=Pin(22), sda=Pin(21))
mpu6500 = MPU6500(i2c, accel_sf=SF_G, gyro_sf=SF_DEG_S)
sensor = MPU9250(i2c, mpu6500=mpu6500)

print("MPU9250 id: " + hex(sensor.whoami))
tft.tft.clear()
tft.tft.text(0,0,"MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    tft.tft.text(0,40,"a1:%.05f    " % sensor.acceleration[0])
    tft.tft.text(0,60,"a2:%.05f    " % sensor.acceleration[1])    
    tft.tft.text(0,80,"a3:%.05f    " % sensor.acceleration[2])        
    tft.tft.text(0,100,"g1:%.05f    " % sensor.gyro[0])
    tft.tft.text(0,120,"g2:%.05f    " % sensor.gyro[1])
    tft.tft.text(0,140,"g3:%.05f    " % sensor.gyro[2])    
    tft.tft.text(0,160,"m1:%.05f    " % sensor.magnetic[0])
    tft.tft.text(0,180,"m2:%.05f    " % sensor.magnetic[1])
    tft.tft.text(0,200,"m3:%.05f    " % sensor.magnetic[2])    
    utime.sleep_ms(500)
