# t013.py
from network import mqtt
from simp_py import lcd
from machine import Pin
led = Pin(26,Pin.OUT)
led.value(0)
lcd.clear()
lcd.circle(100,100,30,lcd.RED,lcd.BLUE)

connected =False
def connected_cb(task):
    global connected
    connected=True

lights_changed=0
def data_cb(msg):
    global lights_changed
    name=msg[0]
    topic=msg[1]
    cont=msg[2]
    if cont=='on' or cont==b'on':
        lights_changed=1
    elif cont=='off' or cont==b'off':
        lights_changed=-1
    return lights_changed

mqttc = mqtt('lights','iot.eclipse.org',secure=False,connected_cb=connected_cb, data_cb=data_cb)
while not connected:
    time.sleep(0.1)

mqttc.subscribe('/lights')
while True:
    if lights_changed !=0:
        if lights_changed==1:
            led.value(1)
            lcd.circle(100,100,30,lcd.RED,lcd.YELLOW)            
        elif lights_changed==-1:
            led.value(0)
            lcd.circle(100,100,30,lcd.RED,lcd.BLUE)            
        lights_changed=0
    time.sleep(0.1)
