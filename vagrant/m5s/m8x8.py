#//reference: http://playground.arduino.cc/LEDMatrix/Max7219
#
from machine import Pin
DIN=13
SCK=12
CS =14
MAX_IN_USE=4

INTENSITY=0x01

LOW=0
HIGH=1

class M8X8:
    global SCK,DIN,CS,MAX_IN_USE,INTENSITY,Pin
    def __init__(self,sck=SCK,din=DIN,cs=CS,max_in_use=MAX_IN_USE,intensity=INTENSITY):
        self.max_in_use = MAX_IN_USE
        self.intensity=intensity
        #pins
        self.dataIn = Pin(din,Pin.OUT)
        self.clock= Pin(sck,Pin.OUT)
        self.load= Pin(cs,Pin.OUT)
        #max7219 reg define
        self.reg_noop= 0x00
        self.reg_digit0 = 0x01
        self.reg_digit1 = 0x02
        self.reg_digit2 = 0x03
        self.reg_digit3 = 0x04
        self.reg_digit4 = 0x05
        self.reg_digit5 = 0x06
        self.reg_digit6 = 0x07
        self.reg_digit7 = 0x08
        self.reg_decodeMode = 0x09
        self.reg_intensity= 0x0a
        self.reg_scanLimit = 0x0b
        self.reg_shutdown = 0x0c
        self.reg_displayTest= 0x0f        
        self.setup()
        
    def setup(self):
        global INTENSITY
        self.maxAll(self.reg_scanLimit, 0x07)
        self.maxAll(self.reg_decodeMode, 0x00)
        self.maxAll(self.reg_shutdown, 0x01)
        self.maxAll(self.reg_displayTest, 0x00)
        for e in range(1,9):
            self.maxAll(e,0)
        
        self.maxAll(self.reg_intensity, 0x0f & self.intensity)

    def loop(self):
        while 1:
            self._loop()

    def _loop(self):
        self.maxSingle(1,1)
        self.maxSingle(2,2)
        self.maxSingle(3,4)
        self.maxSingle(4,8)
        self.maxSingle(5,16)
        self.maxSingle(6,32)
        self.maxSingle(7,64)
        self.maxSingle(8,128)
        time.sleep(0.5)
        self.maxSingle(1,2)
        self.maxSingle(2,4)
        self.maxSingle(3,8)
        self.maxSingle(4,16)
        self.maxSingle(5,32)
        self.maxSingle(6,64)
        self.maxSingle(7,128)
        self.maxSingle(8,1)
        time.sleep(0.5)
        
    def putByte(self,data):
        global HIGH,LOW
        i = 8
        mask=None
        while i>0:
            mask = 0x01 << (i-1)
            self.clock.value(LOW)
            if data & mask:
                self.dataIn.value(HIGH)
            else:
                self.dataIn.value(LOW)
            self.clock.value(HIGH)
            i-=1

    def maxSingle(self,reg,col):
        global HIGH,LOW
        self.load.value(LOW)
        self.putByte(reg)
        self.putByte(col)
        self.load.value(LOW)
        self.load.value(HIGH)

    def maxAll(self,reg,col):
        global HIGH,LOW
        self.load.value(LOW)
        for c in range(self.max_in_use):
            self.putByte(reg)
            self.putByte(col)
        self.load.value(LOW)
        self.load.value(HIGH)

    def maxOne(self,n, reg,col):
        global HIGH,LOW
        self.load.value(LOW)
        c= self.max_in_use
        while c > n:
            self.putByte(0)  # noop
            self.putByte(0)
            c-=1
        self.putByte(reg)
        self.putByte(col)
        c = n-1
        while c >=1:
            self.putByte(0)
            self.putByte(0)
            c-=1
        self.load.value(LOW)
        self.load.value(HIGH)

    
def test():
    # M8X8(sck,din,cs,max_in_use,intensity)        
    mx=M8X8(12,13,14,2,1)    
    from ch_dat import CH_FONTS
    chx= CH_FONTS[u'\u5409']
    for i in range(8):
        bx, chx= chx[0], chx[1:]
        mx.maxOne(1,i,bx)
        bx, chx = chx[0],chx[1:]
        mx.maxOne(2,i,bx)
    for i in range(8):
        bx, chx= chx[0], chx[1:]
        mx.maxOne(3,i,bx)
        bx, chx = chx[0],chx[1:]
        mx.maxOne(4,i,bx)
        

#mx=M8X8(12,13,14,2,1)            
