from m5s_kyoco import INTRO, TEXT_FILE, CH_FONTS
from birthday_song import SONG
from simp_py import tft
import time
from button import Button
btnA=Button(39,'A')
btnB=Button(38,'B')
btnC=Button(37,'C')
tft.tft.image(0,0,'kyoco_scaled.jpg')
intro=INTRO(TEXT_FILE,clr=False)
intro.run()
song= SONG(25)
song.loop(1)
while 1:
  if btnB.pressed():
    tft.on()
    song.mute=False
    song.loop(1)
  elif btnC.pressed():
    tft.off()
  elif btnA.pressed():
    tft.on()
  time.sleep(0.2)
