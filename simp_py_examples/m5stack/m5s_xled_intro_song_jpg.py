from m5s_kyoco import INTRO, TEXT_FILE, CH_FONTS
from m5s_xled import XLED_CH
from birthday_song import SONG
from simp_py import tft

if __name__=='__main__':
    intro = INTRO(TEXT_FILE)
    intro.run()
    song = SONG(25)
    song.loop()
    tft.tft.image(0,0,'kyoco.jpg')
    x = XLED_CH(TEXT_FILE,CH_FONTS)
    while 1:
        x.run()
        
