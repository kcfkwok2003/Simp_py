#raise NotImplementedError
#import dbm
import time
class GDATA1:
    def __init__(self):
        pass

gdata1 = GDATA1()

SIM_MAX=1022
SIM_STEP=30
class ADC:
    def __init__(self,pin):
        self.pin=pin
        self.v=0
        self.dir=SIM_STEP
        
    def read(self):
        self.v+=self.dir
        if self.v> SIM_MAX:
            self.dir=-SIM_STEP
        if self.v==0:
            self.dir=SIM_STEP
        return self.v

class Pin:
    PULL_UP=0
    PULL_DOWN=1
    IN=1
    OUT=3
    OPEN_DRAIN=7
    IRQ_RISING=1
    IRQ_FALLING=2
    def __init__(self, pid, mode=None, pull=-1, value=None,drive=None, alt=None):
        self.pid =pid
        self.init(mode,pull,value,drive,alt)

    def init(self, mode=-1, pull=-1, value=None,drive=None, alt=None):
        if mode is not None:
            self.mode = mode        

    def value(self, x=None):
        if x is not None:
            gdata1.pins.set(self.pid, x)
        return gdata1.pins.get(self.pid)
    
    
    def irq(self, trigger=None, handler=None):
        print('irq trigger:%s handler:%s' % (trigger, handler))
        if handler is not None:
            gdata1.pins.set_callback(self.pid,trigger,handler,self)
            
    def on(self):
        pass

    def off(self):
        pass

    def mode(self,mode=None):
        pass

class PINS:
    states={}
    handlers={}
    def __init__(self):
        pass

    def set_callback(self,p,trigger,handler,pinx):
        PINS.handlers[p]= (trigger,handler,pinx)
        
    def set(self, p, v):
        #print('PINS.set %s:%s' % (p,v))
        if p in PINS.handlers:
            trigger, handler,pinx = PINS.handlers[p]
            if trigger & pinx.IRQ_FALLING==pinx.IRQ_FALLING:
                if v==0:
                    handler(pinx)
            if trigger & pinx.IRQ_RISING==pinx.IRQ_RISING:
                if v==1:
                    if p in PINS.states:
                        if PINS.states[p]==0:
                            handler(pinx)
        PINS.states[p]=v            


    def get(self, p):
        #v = self.states.get(p,1)
        v = PINS.states.get(p,1)
        return int(v)

class RTC:
    def __init__(self):
        pass

    def ntp_sync(self, host):
        pass

    def now(self):
        return time.localtime()

def unique_id():
    return None

class PWM:
    def __init__(self,pin):
        self.pin=pin
        self.dutyx=0
        self.freqx=0

    def duty(self,dutyx):
        self.dutyx=dutyx

    def freq(self,freqx):
        self.freqx=freqx
        
    
pins=PINS()
gdata1.pins=pins

    
