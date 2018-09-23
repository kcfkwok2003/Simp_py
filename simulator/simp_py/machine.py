#raise NotImplementedError
import dbm

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

    def value(self,x=None):
        v='1'
        with dbm.open('pin_states','c') as ps:
            if x is not None:
                ps[str(self.pid)] = str(x)
            v = ps.get(str(self.pid), 1)
        #print('value: %s' % v)
        return int(v) 
    
    def irq(self):
        pass

    def on(self):
        pass

    def off(self):
        pass

    def mode(self,mode=None):
        pass

    
