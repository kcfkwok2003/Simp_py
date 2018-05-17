from m5s_kyoco import INTRO, TEXT_FILE, CH_FONTS
from birthday_song import SONG
from simp_py import tft
from m5s_xled import XLED_CH

tft.tft.image(0,0,'kyoco_scaled.jpg')
intro=INTRO(TEXT_FILE,clr=False)
intro.run()
song= SONG(25)
song.loop(1)
x=XLED_CH(TEXT_FILE,CH_FONTS)
while 1:
  x.run()
