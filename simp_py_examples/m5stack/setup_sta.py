# setup_sta.py
import network
from simp_py import tft
ESSID='AAAAAM'
PASSW='xxxxxxxx'
sta = network.WLAN(network.STA_IF)
if sta.isconnected():
  sta.active(False)
  time.sleep(1)
sta.active(True)
sta.connect(ESSID, PASSW)
while not sta.isconnected():
    time.sleep(1)
ip= sta.ifconfig()[0]
tft.tft.text(0,140,ESSID)
tft.tft.text(0,160,ip)
