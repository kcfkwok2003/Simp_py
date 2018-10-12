# -*- coding: utf-8 -*-
import time
import paho.mqtt.client as mqtt
mqttc = mqtt.Client("python_pub")
#mqttc.connect("test.mosquitto.org", 1883)
mqttc.connect("iot.eclipse.org", 1883)
while 1:
    mqttc.publish("/lights", "ON")
    #mqttc.loop(5) #timeout = 2s
    time.sleep(5)
    mqttc.publish('/lights','OFF')
    #mqttc.loop(5)
    time.sleep(5)
