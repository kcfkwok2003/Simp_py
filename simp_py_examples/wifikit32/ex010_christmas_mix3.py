# ex_christmas_pwm.py
# author: C.F.Kwok
# date: 2017-12-12
from array import array
DUTY_ON=512
DUTY_OFF=0
PIEZO_PIN=21
#note
C=2441
D=2741
E=3048
F=3225
G=3654
A=4058
B=4562
C2=4882
SONG=array('H',  [E,E,E,E,E,E,E,G,C,D,E,F,F,F,F,F,E,E,E,E,D,D,E,D,G])
NOTE_LEN=bytearray([1,1,2,1,1,2,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,2])

mc_width= 128
mc_height= 63
mc_bits = bytearray([
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0c, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x80, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0xe0, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x38, 0xe0, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x1c, 0xc0, 0xf0, 0x01, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x0e, 0xc0, 0x98, 0x81, 0x0f, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0xc0, 0x8c, 0xc1,
   0x0e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80,
   0x03, 0xe0, 0x86, 0x61, 0x0e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x80, 0x01, 0xe0, 0x83, 0x31, 0x0e, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x01, 0xe0, 0xc1, 0x19,
   0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0,
   0xc0, 0xe0, 0xc1, 0x0c, 0x07, 0x08, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0xe0, 0x80, 0xf1, 0xc0, 0x04, 0x03, 0x0c, 0x06, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe0, 0x00, 0x73, 0xc0, 0x86,
   0x03, 0x0c, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x60,
   0x00, 0x73, 0xe0, 0x83, 0xe1, 0x0c, 0x07, 0x63, 0x00, 0x02, 0x00, 0x00,
   0x00, 0x00, 0x30, 0x60, 0x00, 0x3b, 0xe0, 0xc1, 0xb9, 0x3e, 0x9f, 0x73,
   0x00, 0x06, 0x00, 0x00, 0x00, 0x00, 0x7c, 0xe0, 0x80, 0x39, 0xe0, 0xc0,
   0xbc, 0xba, 0xdf, 0x7b, 0x00, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x7c, 0xc0,
   0xc0, 0x18, 0xf0, 0xc0, 0x5c, 0xbb, 0xdc, 0x39, 0x80, 0x1f, 0x00, 0x00,
   0x00, 0x00, 0xfe, 0xc0, 0xc1, 0x1c, 0x70, 0xe0, 0x2e, 0x99, 0xcc, 0x38,
   0xc0, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x78, 0x80, 0x33, 0x0c, 0x78, 0x60,
   0x8e, 0xdd, 0xee, 0x1c, 0x01, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x30, 0x00,
   0x0e, 0x0e, 0x38, 0x60, 0x86, 0x4c, 0xf6, 0x9e, 0x01, 0x06, 0x00, 0x00,
   0x00, 0x00, 0x10, 0x00, 0x00, 0x06, 0x1c, 0x70, 0xc6, 0x6c, 0x76, 0xde,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07, 0x1c, 0x70,
   0x7e, 0x3c, 0xfe, 0x6f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x07, 0x0c, 0x60, 0x3c, 0x18, 0xc6, 0x3e, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x80, 0x03, 0x0c, 0x60, 0x00, 0x00, 0x00, 0x1f,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0xc0,
   0x00, 0x00, 0xf0, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x80, 0x03, 0x00, 0xfc, 0x03, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x8e, 0x03,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0xc3, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe1, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x18, 0x00,
   0x00, 0xbc, 0x78, 0x3c, 0xfc, 0x00, 0x0f, 0x5f, 0xfe, 0x8f, 0x03, 0x70,
   0x00, 0x00, 0x7e, 0x00, 0x00, 0xc6, 0x79, 0x38, 0xfc, 0x07, 0x87, 0x73,
   0xee, 0x9f, 0x03, 0x78, 0xc0, 0x80, 0xe3, 0x00, 0x00, 0xc3, 0x71, 0x38,
   0x1c, 0x0f, 0xc7, 0x61, 0xe6, 0x9c, 0x07, 0x78, 0xc0, 0x80, 0xc1, 0x00,
   0x80, 0x83, 0x71, 0x38, 0x1c, 0x0e, 0xc7, 0x40, 0xe6, 0x98, 0x07, 0x38,
   0xc0, 0xc1, 0xc1, 0x00, 0x80, 0x01, 0x70, 0x38, 0x1c, 0x0e, 0xc7, 0x40,
   0xe0, 0x80, 0x07, 0x3c, 0xe0, 0xc1, 0x81, 0x00, 0xc0, 0x01, 0x70, 0x38,
   0x1c, 0x0e, 0xc7, 0x01, 0xe0, 0x80, 0x0f, 0x3c, 0xe0, 0xc1, 0x01, 0x00,
   0xc0, 0x01, 0x70, 0x38, 0x1c, 0x0e, 0xc7, 0x03, 0xe0, 0x80, 0x0e, 0x3c,
   0xe0, 0x83, 0x03, 0x00, 0xc0, 0x01, 0x70, 0x38, 0x1c, 0x0f, 0x87, 0x07,
   0xe0, 0x80, 0x1e, 0x7e, 0xb0, 0x83, 0x0f, 0x00, 0xc0, 0x01, 0x70, 0x3f,
   0xdc, 0x03, 0x07, 0x1f, 0xe0, 0x80, 0x1c, 0x7a, 0x90, 0x03, 0x1f, 0x00,
   0xc0, 0x01, 0x70, 0x3c, 0xfc, 0x03, 0x07, 0x3e, 0xe0, 0x80, 0x1c, 0x7a,
   0x90, 0x03, 0x7e, 0x00, 0xc0, 0x01, 0x70, 0x38, 0x3c, 0x07, 0x07, 0x7c,
   0xe0, 0x80, 0x38, 0x3b, 0x18, 0x07, 0xf8, 0x00, 0xc0, 0x01, 0x70, 0x38,
   0x1c, 0x0f, 0x07, 0xf0, 0xe0, 0x80, 0x38, 0x39, 0x08, 0x07, 0xf0, 0x00,
   0xc0, 0x01, 0x70, 0x38, 0x1c, 0x0e, 0x07, 0xe0, 0xe0, 0x80, 0x78, 0x39,
   0xf8, 0x07, 0xc0, 0x01, 0xc0, 0x01, 0x70, 0x38, 0x1c, 0x0e, 0x07, 0xc0,
   0xe0, 0x80, 0xf0, 0x78, 0x08, 0x0f, 0xc0, 0x01, 0x80, 0x01, 0x71, 0x38,
   0x1c, 0x0e, 0x47, 0xc0, 0xe0, 0x80, 0xf0, 0x38, 0x0c, 0x4e, 0xc0, 0x01,
   0x80, 0x03, 0x71, 0x38, 0x1c, 0x0e, 0x47, 0xc0, 0xe0, 0x80, 0xf0, 0x78,
   0x04, 0xce, 0xc0, 0x00, 0x00, 0x83, 0x70, 0x3c, 0x1c, 0x0e, 0xc7, 0xe0,
   0xe0, 0x80, 0xe0, 0x78, 0x04, 0xde, 0xc0, 0x00, 0x00, 0x4e, 0x78, 0x3e,
   0x3c, 0x1e, 0xc7, 0x71, 0xe0, 0xc1, 0x61, 0x78, 0x0e, 0xde, 0x61, 0x00,
   0x00, 0x38, 0x00, 0x00, 0x1c, 0x1c, 0x47, 0x1e, 0xe0, 0x80, 0x01, 0x38,
   0x04, 0x40, 0x3c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

pat=bytearray([0,0,0,0,0,0,0,
               4,0,0,0,0,0,0,
               8,4,0,0,0,0,0,
               16,8,4,0,0,0,0,
               32,16,8,4,0,0,0,
               64,32,16,8,4,0,0,
               128,64,32,16,8,4,0,
               255,128,64,32,16,8,4,
               128,255,128,64,32,16,8,
               64,128,255,128,64,32,16,
               32,64,128,255,128,64,32,
               16,32,64,128,255,128,64,
               8,16,32,64,128,255,128,
               4,8,16,32,64,128,255,
               0,4,8,16,32,64,128,
               0,0,4,8,16,32,64,
               0,0,0,4,8,16,32,
               0,0,0,0,4,8,16,
               0,0,0,0,0,4,8,
               0,0,0,0,0,0,4,
               0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,])

BITM={0: 1, 1: 2, 2:4, 3:8, 4:0x10,5:0x20,6:0x40,7:0x80}
from simp_py import oled,mon
import time
class Christmas:
    def __init__(self):
        global PIEZO_PIN, DUTY_OFF, oled
        from machine import PWM,Pin
        self.mute=False
        self.usr_btn=machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
        self.frm = oled.framebuf
        pin_nos=bytearray([2,17,5,18,23,19,22])
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

        piezo_pin=Pin(PIEZO_PIN,Pin.OUT)
        self.pwm_pin = PWM(piezo_pin)
        self.pwm_pin.duty(DUTY_OFF)
        
    def run(self):
        global mc_bits,BITM,mc_width
        self.draw_mode=True
        self.x=0
        self.y=0
        self.mc_idx=0
        self.m=0
        self.note_idx=0
        self.note_stt=0        
        while 1:
            while 1:
                if self.m >=128:
                    self.draw_mode=True
                    self.x=0
                    self.y=0
                    self.m=0
                    self.mc_idx=0                    
                if  self.note_stt==3:
                    self.note_idx=0
                    self.note_stt=0
                    break
                self.j=0
                tmo = time.ticks_ms()+100
                while 1:
                    if self.usr_btn.value()==0:
                        self.mute=True
                    self.play_melody()
                    if self.note_stt==3:
                        break
                    tick_ms = time.ticks_ms()
                    if tick_ms <tmo:
                        self.draw()
                        continue
                    tmo = tick_ms+100
                    mon.data['tmo']=tmo
                    mon.data['tick_ms']=tick_ms
                    if not self.draw_mode:
                        if not self.scroll():
                            break
                    
            gc.collect()


    def draw(self):
        global mc_bits,mc_width
        if self.draw_mode:
            if self.mc_idx >= len(mc_bits):
                self.draw_mode=False
                return
        else:
            time.sleep(0.02)
            return
        bx = mc_bits[self.mc_idx]
        for j in range(8):
            b = bx & BITM[j]
            if b:
                self.frm.pixel(self.x,self.y,1)
            else:
                self.frm.pixel(self.x,self.y,0)
            self.x+=1
        if self.x >= mc_width:
            self.x=0
            self.y+=1
        self.mc_idx+=1
        #oled.show()
                
    def scroll(self):
        global pat
        for i in range(self.num_pins):
            k= self.j+i
            if k >= len(pat):
                break
            dx = pat[self.j+i]
            self.Pwms[i].duty(dx)
        self.j+= self.num_pins
        if self.j >=len(pat):
            return False
        oled.scroll(-1,0)
        oled.show()
        self.m+=1
        mon.data['m']=self.m
        return True

    def play_melody(self):
        global DUTY_ON, DUTY_OFF, SONG,NOTE_LEN
        if self.note_stt==0:
            self.pwm_pin.freq(SONG[self.note_idx])
            if not self.mute:
                self.pwm_pin.duty(DUTY_ON)
            self.note_tmo=time.ticks_ms() + 400 * NOTE_LEN[self.note_idx]
            self.note_stt=1
        elif self.note_stt==1:
            tick_ms = time.ticks_ms()
            if tick_ms < self.note_tmo:
                return
            self.pwm_pin.duty(DUTY_OFF)
            self.note_tmo = tick_ms + 50
            self.note_stt=2
        elif self.note_stt==2:
            tick_ms = time.ticks_ms()
            if tick_ms < self.note_tmo:
                return
            self.note_stt=0
            self.note_idx+=1
            if self.note_idx>= len(SONG):
                self.note_idx=0
                self.note_stt=3

                              
test=Christmas()
test.run()
