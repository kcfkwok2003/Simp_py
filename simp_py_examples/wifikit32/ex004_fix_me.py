# ex004_fix_me.py
# author: C.F.Kwok
# date: 2017-12-14
  import time
pat=bytearray([0,0,0,0,0,0,0,0,
               4,0,0,0,0,0,0,0,
               8,4,0,0,0,0,0,0,
               16,8,4,0,0,0,0,0,
               32,16,8,4,0,0,0,0,
               64,32,16,8,4,0,0,0,
               128,64,32,16,8,4,0,0,
               255,128,64,32,16,8,4,0,
               128,255,128,64,32,16,8,4,
               64,128,255,128,64,32,16,8,
               32,64,128,255,128,64,32,16,
               16,32,64,128,255,128,64,32,
               8,16,32,64,128,255,128,64,
               4,8,16,32,64,128,255,128,
               0,4,8,16,32,64,128,255,
               0,0,4,8,16,32,64,128,
               0,0,0,4,8,16,32,64,
               0,0,0,0,4,8,16,32,
               0,0,0,0,0,4,8,16,
               0,0,0,0,0,0,4,8,
               0,0,0,0,0,0,0,4,
               0,0,0,0,0,0,0,0,])

class TestPwm:
    def __init__(self):
        from machine import PWM,Pin
        pin_nos=bytearray([2,17,5,18,23,19,22,21])
        self.num_pins=len(pin_nos)
        Pwms=[]
        for i in range(self.num_pins):
            print('i:%d' % i)
            pn = pin_nos[i]
            print('pn: i:%s %s' % (i,pn))
            Pwmx = PWM(Pin(pin_nos[i], Pin.OUT))
            Pwms.append(Pwmx)
        for i in range(self.num_pins):
            Pwms[i].freq(500)
            Pwms[i].duty(0)
        self.Pwms=Pwms

    def run(self):
        #global pat
        while 1:
            time.sleep(1)
            j=0
            while 1:
                time.sleep(0.1)
                for i in range(num_pins):
                    k= j+i
                    if k >= len(pat):
                        break
                    dx = pat[j+i]
                    self.Pwms[i]-duty(dx)
                j+= self.num_pins
                if j >=len(pat):
                    break
test=TestPwm()
test.run()
        
