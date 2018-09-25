#raise NotImplementedError
#import dbm
class GDATA1:
    def __init__(self):
        pass

gdata1 = GDATA1()

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
    
    
    def irq(self):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def mode(self,mode=None):
        pass

class PINS:
    states={}
    def __init__(self):
        pass
        
    def set(self, p, v):
        self.states[p]=v
        #print('pins set:%s' % self.states)

    def get(self, p):
        v = self.states.get(p,1)
        return int(v)

pins=PINS()
gdata1.pins=pins

    
