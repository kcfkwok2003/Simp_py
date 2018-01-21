from simp_py import oled
import time
import ntptime
TIMEZONE=8

ofstime=0
phh=0
xhh=0
while 1:
    for i in range(3):
        try:
            ntpt = ntptime.time()
            ut = time.time()
            ofstime = ntpt - ut
            _,_,_,phh,_,_,_,_=time.localtime(ntpt)
            break
        except:
            time.sleep(1)
    while 1:
        ut = time.time()
        YYYY,MM,DD,xhh,mm,ss,_,_=time.localtime(ut+ ofstime)
        if xhh !=phh:
            phh=xhh
            break
        ss1 ='%d-%d-%d %d' % (YYYY,MM,DD,ut)
        hh = (xhh+ TIMEZONE) % 24
        ss2 ='%02d:%02d:%02d m%d' % (hh,mm,ss,gc.mem_free())
        oled.framebuf.fill_rect(0,40,128,20,0)
        oled.text(ss1,0,40)
        oled.text(ss2,0,50)        	    
        oled.show()
        time.sleep(1)
        gc.collect()
