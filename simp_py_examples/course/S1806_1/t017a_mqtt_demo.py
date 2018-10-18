# t017a.py
from mqtt_robust import MQTTClient
from simp_py import lcd
from machine import Pin, unique_id
import time
mqtt_id = str(unique_id())
led = Pin(26,Pin.OUT)
led.value(0)
lcd.clear()
lcd.circle(100,100,30,lcd.RED,lcd.BLUE)

lights_changed=0
def sub_cb(topic,cont):
    print(topic,cont)
    global lights_changed
    if cont=='on' or cont==b'on':
        lights_changed=1
    elif cont=='off' or cont==b'off':
        lights_changed=-1
    return lights_changed    

from button import Button
buttonA = Button(39)
buttonB = Button(38)
lcd.font(lcd.FONT_Comic, transparent=True, fixedwidth=False)
lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13,155,'ON',lcd.BLACK)
lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13+100,155,'OFF',lcd.BLACK)

mqttc =MQTTClient(mqtt_id,'iot.eclipse.org')
mqttc.DEBUG=True
mqttc.set_callback(sub_cb)
print('connecting')
if not mqttc.connect(clean_session=False):
    print('subscribe')
    mqttc.subscribe(b'/lights')
print('done')

apressed=False
bpressed=False
while True:
    msg = mqttc.check_msg()
    if msg:
        print('msg:',msg)
    if buttonA.isPressed():
        if not apressed:
            apressed=True
            mqttc.publish(b'/lights','on')
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
            mqttc.publish(b'/lights','off')
            lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.YELLOW)
            lcd.text(13+100,155,'OFF',lcd.BLACK)
            time.sleep(0.1)
    else:
        if bpressed:
            bpressed=False
            lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
            lcd.text(13+100,155,'OFF',lcd.BLACK)
            
    if lights_changed !=0:
        if lights_changed==1:
            led.value(1)
            lcd.circle(100,100,30,lcd.RED,lcd.YELLOW)            
        elif lights_changed==-1:
            led.value(0)
            lcd.circle(100,100,30,lcd.RED,lcd.BLUE)            
        lights_changed=0
    time.sleep(0.1)
