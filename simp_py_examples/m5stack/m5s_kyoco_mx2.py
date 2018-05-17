from m5s_kyoco import INTRO, TEXT_FILE, CH_FONTS
from birthday_song import SONG
from simp_py import tft

tft.tft.image(0,0,'kyoco_scaled.jpg')
intro=INTRO(TEXT_FILE,clr=False)
intro.run()
song= SONG(25)
song.loop(1)
while 1:
  pass
