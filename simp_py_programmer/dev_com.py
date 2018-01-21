import socket
from exc import get_exc_details
from kivy.logger import Logger
import thread
from Queue import Queue
import time

class DEV_COM:
    def __init__(self,ip=None, dev_com_cb=None):
        self.ip=ip
        self.dev_com_cb= dev_com_cb
        self.sock=None
        #self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected=False
        self.send_queue = Queue(100)
        self.recv_queue = Queue(100)
        self.mon_cb=None
        thread.start_new_thread(self.thread_send, ())
        thread.start_new_thread(self.thread_recv, ())        

        
    def thread_recv(self):
        while 1:
            try:
                self._thread_recv()
            except:
                exc = get_exc_details()
                Logger.info('kcf: thread_recv exc:%s' % exc)
                time.sleep(1)

    def _thread_recv(self):
        while 1:
            if self.connected:
                try:
                    msg = self.sock.recv(1024)
                except:
                    exc = get_exc_details()
                    Logger.info('kcf: thread_recv exc:%s' % exc)
                    if self.dev_com_cb:
                        self.dev_com_cb('',exc)
                    time.sleep(1)
                    self.connected=False
                    self.sock.close()
                    return
                if msg:
                    Logger.info('kcf: thread_recv msg:%s' % `msg`)
                    if self.dev_com_cb:
                        self.dev_com_cb(msg)
                    else:
                        self.recv_queue.put(msg)
            
    def thread_send(self):
        while 1:
            try:
                self._thread_send()
            except:
                exc = get_exc_details()
                Logger.info('kcf: thread_send exc:%s' % exc)
            time.sleep(1)

    def _thread_send(self):
        while 1:
            ping=False
            msg = self.send_queue.get()
            if 'ping' in msg[:6]:
                Logger.info('kcf: ping in msg')
                ping=True
            if not self.connected:
                self.connect(ping=ping)
            if self.connected:
                Logger.info('kcf: msg send %s' % `msg`)
                msglen =len(msg)
                totalsent=0
                if ping:
                    self.sock.settimeout(5)
                else:
                    self.sock.settimeout(60)
                while totalsent < msglen:
                    sent=0
                    try:
                        sent = self.sock.send(msg[totalsent:])
                    except:
                        exc = get_exc_details()
                        Logger.info('kcf: thread_send exc:%s' % exc)
                        if self.dev_com_cb:
                            self.dev_com_cb('',exc)
                        self.connected=False
                        self.sock.close()
                        return
                        
                    if sent ==0:
                        self.recv_queue.put('connection broken\n')
                        raise RuntimeError("socket connection broken")
                    totalsent= totalsent + sent
                Logger.info('kcf: msg sent')
            else:
                self.recv_queue.put('connection failure\n')
                
    def connect(self,ip=None,ping=False):
        if ip:
            self.ip=ip
        self.server_addr=(self.ip, 8080)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if ping:
            self.sock.settimeout(5)
        else:
            self.sock.settimeout(20)
        try:
            Logger.info('kcf: connect to %s' % `self.server_addr`)
            self.sock.connect(self.server_addr)
            self.connected=True
            Logger.info('kcf: connected')
        except:
            exc = get_exc_details()
            Logger.info('kcf: connect exc:%s' % exc)
            if self.dev_com_cb:
                self.dev_com_cb('','Connection failure')
            
    def send(self, msg, ip=None):
        if ip:
            self.ip=ip
        self.send_queue.put(msg)
        return

    def recv(self):
        msg=''
        try:
            msg = self.recv_queue.get_nowait()
        except:
            pass
        return msg
    
    def close(self):
        Logger.info('kcf: dev_com.close')
        self.connected=False
        self.sock.close()

def test_upload(ip):
    f=open('seve_py_dat/test1.py','rb')
    cont = f.read()
    f.close()
    cont = '\x02\nsvtest\n'+ cont +'\x03\n\x04\n'
    dev_com = DEV_COM(ip)
    dev_com.connect()
    dev_com.send(cont)
    dev_com.close()

def test_reset(ip):
    cont = '\x02\nreset\n\x03\n\x04\n'
    dev_com = DEV_COM(ip)
    dev_com.connect()
    dev_com.send(cont)
    dev_com.close()    

def test_upload_wifi_config(ip):
    f=open('wifi_config.py','rb')
    cont = f.read()
    f.close()
    cont = '\x02\nsvwifi\n'+ cont +'\x03\n\x04\n'
    dev_com = DEV_COM(ip)
    dev_com.send(cont)
    while 1:
        time.sleep(1)
        msg = dev_com.recv()
        if msg:
            print msg
            dev_com.close()
            break

    
if __name__=='__main__':
    ip='192.168.4.1'
    #test_reset(ip)
    test_upload_wifi_config(ip)
    import sys
    sys.exit()
    
    
