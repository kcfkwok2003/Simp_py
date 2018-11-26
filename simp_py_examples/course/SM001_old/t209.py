from simp_py import tft
lcd = tft.tft
import machine
rtc = machine.RTC()
synced = False
for i in range(3):
  try:
    rtc.ntp_sync('pool.ntp.org')
    synced = True
    break
  except:
    time.sleep(1)
if not synced:
  lcd.text(0,50, 'time sync failured')
else:
  while True:
    tuplex = rtc.now()
    YYYY,MM,DD,hh,mm,ss,_,_ = tuplex
    ss = '%d-%d-%d %02d:%02d:%02d' % (YYYY,MM,DD,hh,mm,ss)
    lcd.text(0,50,ss)
    time.sleep(1)    
  
