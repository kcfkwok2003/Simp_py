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
if synced:
  lcd.text(0,50, 'time is synced    ')
else:
  lcd.text(0,50, 'time sync failured')
