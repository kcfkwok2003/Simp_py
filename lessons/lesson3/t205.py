# t205.py
# 100 -> 0.295V
# 600 -> 2.06V
# v = 0.00353 x - 0.058
# ref: http://www.instructables.com/id/How-to-Use-the-Sharp-IR-Sensor-GP2Y0A41SK0F-Arduin/
# GP2Y0A41SK0F
# distance = 13* pow(volts, -1)

# ref:https://forum.arduino.cc/index.php?topic=22604.0
# GP270A02YK0F
# cm = 60.495 * pow(volts, -1.1907)

from machine import Pin,ADC
from simp_py import tft
p35 = ADC(Pin(35,Pin.IN))
while True:
  x= p35.read()
  tft.tft.text(0,100,'x=%d %04x   ' % (x,x))
  v = 0.00353 * x - 0.058
  tft.tft.text(0,120,'v=%.02fV   ' % v)
  dist = 60.495*pow(v, -1.1907)
  if dist <150:
    tft.tft.text(0,140,'dist=%d cm   ' % dist)
  else:
    tft.tft.text(0,140,'dist > 150 cm   ')
  time.sleep(1)
  
