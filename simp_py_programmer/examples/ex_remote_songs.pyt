from machine import Pin,PWM
from simp_py import mon
from array import array
import time
# note
C=2441
D=2741
E=3048
F=3225
G=3654
A=4058
B=4562
C2=4882
DUTY_ON=512
DUTY_OFF=0

jingle_bells_s=array('H',  [E,E,E,E,E,E,E,G,C,D,E,F,F,F,F,F,E,E,E,E,D,D,E,D,G])
jingle_bells_l=bytearray([1,1,2,1,1,2,1,1,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,2,2])
little_lamb_s =array('H', [B,A,G,A,B,B,B,A,A,A,B,B,B,B,A,G,A,B,B,B,A,A,B,A,G,G])
little_lamb_l= bytearray([1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,2])
songs_info={
    b'jingle bells': [jingle_bells_s, jingle_bells_l],
    b'little lamb': [little_lamb_s, little_lamb_l],
    }
        
class SONGS:
    def __init__(self,pinx):
        global Pin, PWM
        self.speaker=PWM(Pin(pinx, Pin.OUT))
        self.speaker.duty(0)

    def run(self):
        global time, mon, songs_info
        while 1:
            if mon.chk_ureq():
                ureq = mon.get_ureq()
                song_info = songs_info.get(ureq,[None,None])
                if song_info[0]:
                    uresp= b'%s played' % ureq
                    mon.put_uresp(uresp)                    
                    self.play(song_info)
                else:
                    uresp= b'No music played'
                    mon.put_uresp(uresp)
            time.sleep(0.02)
            
    def play(self,song_info):
        global DUTY_ON, DUTY_OFF
        song = song_info[0]
        note_len=song_info[1]
        for i in range(len(song)):
            self.speaker.freq(song[i])
            self.speaker.duty(DUTY_ON)
            time.sleep(0.4 * note_len[i])
            self.speaker.duty(DUTY_OFF)
            time.sleep(0.05)
            

songs = SONGS(21)
songs.run()
