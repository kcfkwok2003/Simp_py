from m5s_kyoco import INTRO, TEXT_FILE, CH_FONTS
from m5s_xled import XLED_CH

if __name__=='__main__':
    intro = INTRO(TEXT_FILE)
    intro.run()
    x = XLED_CH(TEXT_FILE,CH_FONTS)
    while 1:
        x.run()
        
