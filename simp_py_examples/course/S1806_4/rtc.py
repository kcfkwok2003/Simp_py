# rtc.py
TZ=28800
import time as t
class RTC:
    global t
    def __init__(self):
        global TZ
        import machine
        self.rtc = machine.RTC()
        self.synced=False
        self.td=0
        self.tz=TZ
        
    def sync(self):
        self.synced=False
        try:
            self.rtc.ntp_sync('pool.ntp.org')
            self.synced=True
        except:
            pass

    def now(self, form='s'):
        if self.td==0:
            self.td = int(t.mktime(t.localtime()) - t.mktime(t.gmtime()))
        if not self.synced:
            self.sync()
        if form=='s':
            return self.now_str()
        return self.rtc.now()

    def now_str(self):
        tx = t.localtime(int(t.time()) - self.td + self.tz)
        YYYY = tx[0]
        MM = tx[1]
        DD = tx[2]
        hh = tx[3]
        mm = tx[4]
        ss = tx[5]
        s ='%d-%d-%d %02d:%02d:%s' % (YYYY,MM,DD,hh,mm,ss)
        return s
    
if __name__=='__main__':
    from simp_py import lcd
    lcd.clear()
    rtc = RTC()
    while True:
        s = rtc.now()
        lcd.text(10,10,s)
        t.sleep(1)
        
        
