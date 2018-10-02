# rtc.py
import machine

class RTC:
    def __init__(self):
        import machine
        self.rtc = machine.RTC()
        self.synced=False
        
    def sync(self):
        self.synced=False
        try:
            self.rtc.ntp_sync('pool.ntp.org')
            self.synced=True
        except:
            pass

    def now(self, form='s'):
        if not self.synced:
            self.sync()
        if form=='s':
            return self.now_str()
        return self.rtc.now()

    def now_str(self):
        tx = self.rtc.now()
        YYYY = tx[0]
        MM = tx[1]
        DD = tx[2]
        hh = tx[3]
        mm = tx[4]
        ss = tx[5]
        s ='%d-%d-%d %02d:%02d:%02d' % (YYYY,MM,DD,hh,mm,ss)
        return s
    
if __name__=='__main__':
    import time
    from simp_py import lcd
    x = RTC()
    while True:
        s = x.now()
        lcd.text(0,0,s)
        time.sleep(1)

        
