# mqtt example
# ref: loboris mqtt example
import network
from machine import Pin
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
    tft.tft.text(0,140,"from:%s" % msg[0])
    tft.tft.text(0,160,"topic:%s" % msg[1])
    tft.tft.text(0,180,"msg:%s" % msg[2])
    
# secure connection requires more memory and may not work
mqtt = network.mqtt("eclipse", "iot.eclipse.org", secure=True, cleansession=True, connected_cb=conncb, disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb)

# Wait until status is: (1, 'Connected')

while not connected:
    time.sleep(1)
    
print("subs to top1")
mqtt.subscribe('top1')

cnt=0
btn=Pin(39,Pin.IN)
while connected:
    if btn.value()==0:
        cnt+=1
        mqtt.publish('top1', 'count:%s' % cnt)
    time.sleep(1)
