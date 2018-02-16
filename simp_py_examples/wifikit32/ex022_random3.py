from random import seed,uniform
from simp_py import oled, mon
from machine import Pin, PWM
import time

def run():
    global oled, time,seed,uniform,Pin,PWM
    st = bytearray([512,128,64,32,16,8,2,0])
    pin_nos=bytearray([2,17,5,18,23,19,22,21])
    num_pins=len(pin_nos)
    Pwms=[]
    for i in range(num_pins):
        print('i:%d' % i)
        pn = pin_nos[i]
        #print('pn: i:%s %s' % (i,pn))
        Pwmx = PWM(Pin(pin_nos[i], Pin.OUT))
        Pwms.append(Pwmx)
    for i in range(num_pins):
        Pwms[i].freq(500)
        Pwms[i].duty(0)
        
    frm = oled.framebuf
    seed(1)
    m=0
    k=0
    for i in range(100):
        for j in range(100):
            x = round(uniform(0,1) * 128)
            y = round(uniform(0,1) * 64)
            frm.pixel(x,y,1)
            k = y % 8
            m = st[x % 8]
        Pwms[k].duty(m)
        oled.show()
        time.sleep(0.02)
    oled.fill(1)
    oled.show()
    time.sleep(1)
    seed(1)
    for i in range(100):
        for j in range(100):
            x = round(uniform(0,1) * 128)
            y = round(uniform(0,1) * 64)
            frm.pixel(x,y,0)
            k = y % 8
        Pwms[k].duty(x)            
        oled.show()
        time.sleep(0.02)
    oled.fill(0)
    oled.show()

if __name__=='__main__':
    while 1:
        run()
