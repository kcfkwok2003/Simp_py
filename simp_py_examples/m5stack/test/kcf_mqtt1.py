import time
from network import mqtt

connected=False
def on_connected(task):
    global connected
    print("[{}] connected".format(task))
    connected=True
    
mqttc = mqtt('kcf','iot.eclipse.org',secure=True,connected_cb=on_connected)
while not connected:
    time.sleep(1)

while True:
    mqttc.publish('/lights','hello on')
    time.sleep(5)
    mqttc.publish('/lights','hello off')
    time.sleep(5)
