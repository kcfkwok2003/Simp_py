# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import socket
from select import select
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata,flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and  
    # reconnect then subscriptions will be renewed.
    client.subscribe("hello/world")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print( "Topic: ", msg.topic+'\nMessage: '+str(msg.payload))
    
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
print('connect to ...')
#client.connect("iot.eclipse.org", 1883, 60)
mqttc.connect("test.mosquitto.org", 1883, 60)


mqttc.socket().setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
print('loop_forever')

c=0
while True:
    sock = mqttc.socket()
    if not sock:
        break
    r,w,e = select([sock],[sock] if mqttc.want_write() else [], [], 10)
    idle =True
    if sock in r:
        mqttc.loop_read()
        idle=False
    if sock in w:
        mqttc.loop_write()
        idle = False
    mqttc.loop_misc()
    time.sleep(0.01)
        
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()
