# ex_birthday_song.py
# author: C.F.Kwok
# date: 2018-1-7
# ref: http://forum.arduino.cc/index.php?topic=178460.0

import time
from machine import Pin

class SONG:
    def __init__(self,pinx):
        global Pin
        self.speaker = Pin(pinx,Pin.OUT)
        self.length = 28 # nnumber of notes
        self.notes='GGAGcB GGAGdc GGxecBA yyecdc'
        self.beats = bytearray([2, 2, 8, 8, 8, 16, 1, 2, 2, 8, 8,8, 16, 1, 2,2,8,8,8,8,16, 1,2,2,8,8,8,16])
        self.tempo=150
        self.tones={
            'C':1915,'D':1700,'E':1519,'F':1432,'G':1275,'A':1136,'B':1014,
            'c':956,'d':834,'e':765,'f':593,'g':468,'a':346,'b':224,
            'x':655,'y':715,
            }
        self.SPEE=5
        
    def playTone(self, tone, duration):
        global time
        i=0
        while i < duration * 1000:
            self.speaker.value(1)
            time.sleep_us(tone)
            self.speaker.value(0)
            time.sleep_us(tone)
            i += tone *2

    def playNote(self, note, duration):
        newduration = duration / self.SPEE
        self.playTone(self.tones[note], newduration)

    def loop(self):
        global time
        while 1:
            for i in range(self.length):
                if self.notes[i] ==' ':
                    time.sleep_ms(self.beats[i] * self.tempo)
                else:
                    self.playNote(self.notes[i],self.beats[i] * self.tempo)
                time.sleep_ms(self.tempo)
            time.sleep(1)
            
song = SONG(21)
song.loop()
