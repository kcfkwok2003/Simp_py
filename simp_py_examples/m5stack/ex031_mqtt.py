# mqtt example
# ref: loboris mqtt example
import network
import time
from simp_py import tft

connected=False
def conncb(task):
    global connected
    print("[{}] Connected".format(task))
    connected=True

def disconncb(task):
    print("[{}] Disconnected".format(task))

def subscb(task):
    print("[{}] Subscribed".format(task))

def pubcb(pub):
    print("[{}] Published: {}".format(pub[0], pub[1]))

def datacb(msg):
    print("[{}] Data arrived from topic: {}, Message:\n".format(msg[0], msg[1]), msg[2])

#mqtt = network.mqtt("test1", "192.168.0.105", user="wifimcu", password="wifimcu", cleansession=True, connected_cb=conncb, disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb)

# secure connection requires more memory and may not work
mqtt = network.mqtt("eclipse", "iot.eclipse.org", secure=True, cleansession=True, connected_cb=conncb, disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb)

# Wait until status is: (1, 'Connected')

while not connected:
    time.sleep(1)
    
print("subs to top1")
mqtt.subscribe('top1')
print("pubs to top1")
mqtt.publish('top1', 'Hi from Micropython')

while connected:
    time.sleep(1)
