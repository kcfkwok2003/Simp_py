# setup_ap.py
import network
from simp_py import tft
ESSID='ESP-AP'
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ESSID, password='xxxxxxxx', authmode=network.AUTH_WPA2_PSK)
ip= ap.ifconfig()[0]
tft.tft.text(0,140,ESSID)
tft.tft.text(0,160,ip)
