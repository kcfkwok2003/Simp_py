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
        s ='%d-%d-%d %02d:%02d' % (YYYY,MM,DD,hh,mm)
        return s
    
if __name__=='__main__':
    import time
    x = RTC()
    s = x.now()
    print('now:%s' % s)

        
