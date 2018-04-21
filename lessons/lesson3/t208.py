# t208.py
from machine import Pin, time_pulse_us
from simp_py import tft
inp= Pin(39)
while True:
  pw=time_pulse_us(inp, 0, 10000000)
  if pw <0 :
    continue
  tft.tft.text(0,100,"pw:%s      " % pw)
  pw=time_pulse_us(inp, 0, 10000000)
  if pw <0 :
    continue
  tft.tft.text(0,120,"pw:%s      " % pw)
# note: this program will lost communication

