import time
from network import mqtt
from simp_py import lcd
from button import Button
buttonA= Button(39,'a')
buttonB = Button(38,'b')
buttonA.isPressed=buttonA.pressed
buttonB.isPressed=buttonB.pressed

connected=False
def connected_cb(task):
    global connected
    print("[{}] connected".format(task))
    connected=True

lights_changed=0
def data_cb(msg):
    global lights_changed
    name=msg[0]
    topic = msg[1]
    cont = msg[2]
    
    print('name:%s cont:%s %s' % (name,cont,type(cont)))
    if cont==b'on' or cont=='on':
        lights_changed=1
    elif cont==b'off' or cont=='off':
        lights_changed=-1
    #lcd.text(0,0,cont)
    return lights_changed

lcd.clear()
lcd.font(lcd.FONT_Comic, transparent=True)
lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13,155,'ON',lcd.BLACK)
lcd.roundrect(100,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
lcd.text(13+100,155,'OFF',lcd.BLACK)



mqttc = mqtt('kcf','iot.eclipse.org',secure=False,connected_cb=connected_cb, data_cb=data_cb)
while not connected:
    time.sleep(1)

mqttc.subscribe('/lights')

apressed=False
bpressed=False
while True:
    if buttonA.isPressed():
        if not apressed:
            apressed=True
            mqttc.publish('/lights','on')
            #lcd.circle(100,100,30,lcd.RED,lcd.YELLOW)
            lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.YELLOW)
            lcd.text(13,155,'ON',lcd.BLACK)            
            time.sleep(0.1)
    else:
        if apressed:
            apressed=False
            lcd.roundrect(10,150,80,40,5,lcd.RED,lcd.LIGHTGREY)
            lcd.text(13,155,'ON',lcd.BLACK)            
    if buttonB.isPressed():
        if not bpressed:
            bpressed=True
            mqttc.publish('/lights','off')
            #lcd.circle(100,100,30,lcd.RED,lcd.BLUE)
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
            lcd.circle(100,100,30,lcd.RED,lcd.YELLOW)
        elif lights_changed==-1:
            lcd.circle(100,100,30,lcd.RED,lcd.BLUE)
        lights_changed=0
    time.sleep(0.1)

