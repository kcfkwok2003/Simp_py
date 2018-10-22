# t016_rtc.py
from machine import RTC
from simp_py import lcd
import time as t
rtc = RTC()
synced=False
lcd.clear()
td=0
tz=28800
while True:
    lcd.clear()
    if not synced:
        try:
            lcd.text(10,10,'syncing')
            rtc.ntp_sync('pool.ntp.org')
            td = int(t.mktime(t.localtime()) - t.mktime(t.gmtime()))
            print('td:%d' % td)
            synced=True
        except:
            pass
    else:
        if td==0:
            td = int(t.mktime(t.localtime()) - t.mktime(t.gmtime()))
            print('td:%d' % td)            
        tx=t.localtime(int(t.time())- td +tz)
        YYYY=tx[0]; MM=tx[1]; DD=tx[2]
        hh=tx[3]; mm=tx[4]; ss=tx[5]
        lcd.text(10,10,'%d-%d-%d %02d:%02d:%02d' % (YYYY,MM,DD,hh,mm,ss))
    t.sleep(1)
        
        
