#raise NotImplementedError
import paho.mqtt.client as mqttx
import socket
from select import select
import time

class GDATA2:
    pass

gdata2 = GDATA2()
gdata2.run=None

class mqtt:
    def __init__(self,name,server,password=None,port=-1,autoreconnect=0,clientid=None,cleansession=False,keepalive=120,qos=0,retain=0,secure=False,data_cb=None,connected_cb=None,disconnected_cb=None,subscribed_cb=None,unsubscribed_cb=None,published_cb=None):
        print('mqtt init')
        self.name=name
        self.server = server
        self.port = port
        if port ==-1:
            if secure:
                port = 8883
            else:
                port = 1883
        self.port = port
        self.connected_cb= connected_cb
        self.data_cb = data_cb
        self.published_cb = published_cb
        self.subscribed_cb = subscribed_cb
        self.mqttc = mqttx.Client()
        self.mqttc.on_connect=self.on_connect
        self.mqttc.on_message = self.on_message
        self.mqttc.on_publish = self.on_publish
        self.mqttc.on_subscribe = self.on_subscribe
        print('server:%s port :%s' % (self.server,self.port)
)        
        self.mqttc.connect(self.server, self.port,60)
        self.mqttc.socket().setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        
        print('connecting...')
        self.sock = self.mqttc.socket()
        
        gdata2.run=self.run

    def run(self):
        if self.sock:
            #print ('sock:%s ' % self.sock)
            sock = self.sock
            wsocks = []
            if self.mqttc.want_write():
                wsocks=[sock]
            r,w,e = select([sock],wsocks, [], 0.1)
            if sock in r:
                self.mqttc.loop_read()
            if sock in w:
                self.mqttc.loop_write()
            self.mqttc.loop_misc()
            
            
    def on_connect(self, mqttc, obj, flags, rc):
        print('on_connect rc:' + str(rc))
        if self.connected_cb:
            self.connected_cb(rc)

    def on_message(self, mqttc, obj, msg):
        print('msg:' +msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        print('data_cb:%s' % self.data_cb)
        if self.data_cb:
            data = [self.name, msg.topic,msg.payload,msg.qos]
            print('data:%s' % data)
            res =self.data_cb(data)
            print('data_cb res:%s' % res)
            
    def on_publish(self, mqttc, obj, mid):
        print("pub mid: " + str(mid))


    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))


    def publish(self, topic, value):
        print ('publish %s %s' % (topic, value))
        self.mqttc.publish(topic, value)

    def subscribe(self,topic):
        self.mqttc.subscribe(topic)
        

if __name__=='__main__':
    connected=False
    def connected_cb(task):
        global connected
        print('[{}] connected'.format(task))
        connected=True

    def data_cb(msg):
        topic = msg[1]
        cont = msg[2]
        print('topic:%s cont:%s' % (topic,cont))
        return 1011
    
    mqttc = mqtt('kcf','iot.eclipse.org', secure=False, connected_cb=connected_cb, data_cb=data_cb)
    while not connected:
        mqttc.run()
        time.sleep(0.1)
    mqttc.subscribe('/lights')
    while True:
        mqttc.publish('/lights','hi on')
        exp =time.time()+5
        while True:
            mqttc.run()
            time.sleep(0.1)
            if time.time() > exp:
                break
        mqttc.publish('/lights','hi off')
        exp = time.time() +5
        while True:
            mqttc.run()
            time.sleep(0.1)
            if time.time() > exp:
                break
        
