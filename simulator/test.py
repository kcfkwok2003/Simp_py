# t017.py
from network import mqtt
from simp_py import lcd,tft
from machine import Pin,unique_id
import time
mqtt_id = str(unique_id())
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

from button import Button
buttonA = Button(39)
buttonB = Button(38)
buttonC = Button(37)
lcd.font(lcd.FONT_Comic, transparent=True, fixedwidth=False)
lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13,155,'ON',lcd.BLACK)
lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13+100,155,'OFF',lcd.BLACK)

mqttc = mqtt('lights','iot.eclipse.org',secure=False,connected_cb=connected_cb, data_cb=data_cb,clientid=mqtt_id)
while not connected:
    time.sleep(0.1)

mqttc.subscribe('/lights')
apressed=False
bpressed=False
while True:
    if buttonA.isPressed():
        if not apressed:
            apressed=True
            tft.on()
            mqttc.publish('/lights','on')
            lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.YELLOW)
            lcd.text(13,155,'ON',lcd.BLACK)
    else:
        if apressed:
            apressed=False
            lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
            lcd.text(13,155,'ON',lcd.BLACK)

    if buttonB.isPressed():
        if not bpressed:
            bpressed=True
            mqttc.publish('/lights','off')
            lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.YELLOW)
            lcd.text(13+100,155,'OFF',lcd.BLACK)
            time.sleep(0.1)
    else:
        if bpressed:
            bpressed=False
            lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
            lcd.text(13+100,155,'OFF',lcd.BLACK)
            
    if lights_changed !=0:
        tft.on()
        if lights_changed==1:
            led.value(1)
            lcd.circle(100,100,30,lcd.RED,lcd.YELLOW)            
        elif lights_changed==-1:
            led.value(0)
            lcd.circle(100,100,30,lcd.RED,lcd.BLUE)            
        lights_changed=0
    if buttonC.isPressed():
        tft.off()
    time.sleep(0.1)
