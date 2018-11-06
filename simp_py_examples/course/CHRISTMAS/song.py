from machine import Pin,PWM
from simp_py import mon
from array import array
import time
c = 261
d = 294
e = 329
f = 349
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 523
cSH = 554
dH = 587
dSH = 622
eH = 659
fH = 698
fSH = 740
gH = 784
gSH = 830
aH = 880
DUTY_ON=99
DUTY_OFF=0

class SONG:
  def __init__(self,pinx):
    global Pin,PWM
    self.mute=False
    self.speaker=PWM(Pin(pinx,Pin.OUT))
    self.speaker.duty(0)
    self.running=False
    
  def mute_on(self,v=None):
    self.mute=True

  def mute_off(self,v=None):
    self.mute=False
    
  def set_notes(self, notes, durations):
      self.notes=notes
      self.durations=durations
      
  def play(self):
      global DUTY_ON,DUTY_OFF
      self.running=True
      for i in range(len(self.notes)):
        if self.mute:
          break
        self.speaker.freq(self.notes[i])
        self.speaker.duty(DUTY_ON)
        time.sleep_ms(self.durations[i])
        self.speaker.duty(DUTY_OFF)
        time.sleep(0.05)
      self.running=False

  def is_running(self):
    return self.running
    
if __name__=='__main__':
  from button import Button
  from machine import Pin
  NOTES1=[a,a,a,f,cH,a,f,cH,a]
  DURATIONS1=[500,500,500,350,150,500,350,150,650]
  song=SONG(25)
  song.set_notes(NOTES1,DURATIONS1)
  btnA=Button(39, song.mute_off, trigger=Pin.IRQ_FALLING)
  btnA=Button(38, song.mute_on, trigger=Pin.IRQ_FALLING)
  while True:
    song.play()
    time.sleep(1)
  
