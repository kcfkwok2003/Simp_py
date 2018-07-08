# ref: https://github.com/DFRobot/micropython-dflib/tree/master/ADXL345
from machine import Pin,I2C
import ADXL345
import time
from simp_py import tft
i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)
adx = ADXL345.ADXL345(i2c)

while True:
    x=adx.xValue
    y=adx.yValue
    z=adx.zValue
    tft.tft.text(0,100,"acc:%d,%d,%d    " %(x,y,z))
    time.sleep_ms(50)
