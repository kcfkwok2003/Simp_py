from simp_py import lcd, tft
import time
from pr_fontx import read_texts,pr_texts
from button import Button
from machine import Pin
from christmas_song import song
import sys

from text1_fontx import CH_FONTS
from text2_fontx import CH_FONTS as fontx2
from text3_fontx import CH_FONTS as fontx3

CH_FONTS.update(fontx2)
CH_FONTS.update(fontx3)
pages=[]
for fn in ['text1.txt','text2.txt','text3.txt']:
  pages.append(read_texts(fn))

def mute_off(v):
  global song,tft
  song.mute_off()
  tft.on()

def mute_on(v):
  global song,tft
  song.mute_on()
  tft.on()

def tft_off(v):
  global tft
  tft.off()
  

btnA=Button(39, mute_off, trigger=Pin.IRQ_FALLING)
btnB=Button(38, mute_on, trigger=Pin.IRQ_FALLING)
btnC=Button(37, tft_off, trigger=Pin.IRQ_FALLING)

def thread_run():
  global song
  while True:
    song.play()
    time.sleep(2)

if sys.platform=='esp32':
  import _thread
  _thread.start_new_thread('song',thread_run,())

while True:
  for i in range(1,4):
    expire=time.time()+5
    lcd.image(0,0,'photo%d_scaled.jpg' % i)
    pr_texts(0,0,pages[i-1],CH_FONTS)
    while True:
      if not song.is_running():
        break
      time.sleep(0.5)
    while True:
      if time.time() > expire:
        break
      time.sleep(1)
