import machine
import ssd1306
import sys
import time

import m5stack

tft = m5stack.Display()
lcd = tft.tft

class MON:
    def __init__(self):
        self.history=[]
        self.hist_len=20
        self.data={}
        self.ureqs=[]
        self.dev_info={}
        self.cl=None

    def put_uresp(self,msg):
        # put user resp
        if self.cl:
            resp=b'\x02\nuresp\n%s\n\x03\n' % msg
            try:
                self.cl.send(resp)
            except:
                print('send exc')
                self.set_mon_cl(None)
                self.cl.close()
        else:
            print('put_uresp without cl')

    def set_mon_cl(self,cl):
        self.cl=cl
        
    def set_dev_info(self,key,v):
        self.dev_info[key]=v
        
    def get_dev_info(self,key):
        return self.dev_info.get(key,'')

    def put_ureq(self,msg):
        print('mon.put_ureq')
        self.ureqs.insert(0,msg)
        if len(self.ureqs) > 10:
            self.ureqs.pop()

    def chk_ureq(self):
        return len(self.ureqs)

    def get_ureq(self):
        if len(self.ureqs)>0:
            return self.ureqs.pop()

    def set_hist_len(self,lenx):
        if lenx >100:
            lenx=100
        self.hist_len=lenx

    def clean_hist(self):
        self.history=[]
        
    def hist(self,msg):
        self.history.insert(0,msg)
        if len(self.history) > self.hist_len:
            self.history.pop()

    def get_hist(self):
        txt=''
        for i in range(len(self.history)):
            txt+=self.history[i]
        return txt
        
    def log_exc(self,exc):
        f=open('exc.txt','w')
        sys.print_exception(exc,f)
        f.close()
        f=open('exc.txt')
        mon.data['_exc']=f.read()
        f.close()
        
mon = MON()

