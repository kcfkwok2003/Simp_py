# ref:https://github.com/tuupola/micropython-mpu9250

import micropython
from machine import I2C, Pin, Timer
from mpu9250 import MPU9250

micropython.alloc_emergency_exception_buf(100)

i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = MPU9250(i2c)

def read_sensor(timer):
    global sensor
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)

print("MPU9250 id: " + hex(sensor.whoami))

timer_0 = Timer(0)
timer_0.init(period=1000, mode=Timer.PERIODIC, callback=read_sensor)
