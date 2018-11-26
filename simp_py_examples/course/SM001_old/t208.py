from simp_py import tft
lcd = tft.tft
lcd.clear()
import machine
rtc = machine.RTC()
while 1:
  try:
    rtc.ntp_sync('pool.ntp.org')
  except:
    time.sleep(1)
    continue
  tuplex = rtc.now()
  YYYY,MM,DD,hh,mm,ss,_,_ = tuplex
  ss = '%d-%d-%d %02d:%02d:%02d' % (YYYY,MM,DD,hh,mm,ss)
  lcd.text(0,50,ss)
  time.sleep(1)
