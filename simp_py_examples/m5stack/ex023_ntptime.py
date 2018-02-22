
def run():
    from simp_py import tft
    import time
    import machine
    TIMEZONE=8

    ofstime=0
    phh=0
    xhh=0
    rtc = machine.RTC()
    uptime=int(time.time())
    while 1:
        for i in range(3):
            try:
                rtc.ntp_sync('pool.ntp.org')
                break
            except:
                time.sleep(1)
        while 1:
            YYYY,MM,DD,xhh,mm,ss,_,_=rtc.now()
            ut = int(time.time()- uptime)
            ss1 ='%d-%d-%d %d' % (YYYY,MM,DD,ut)
            hh = (xhh+ TIMEZONE) % 24
            ss2 ='%02d:%02d:%02d m%d' % (hh,mm,ss,gc.mem_free())
            tft.tft.rect(0,80,128,20,0,0)
            tft.tft.text(0,80,ss1)
            tft.tft.text(0,100,ss2)
            time.sleep(1)
            gc.collect()

if __name__=='__main__':
    run()
