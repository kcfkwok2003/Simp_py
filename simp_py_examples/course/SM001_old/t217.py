from btc_price import get_btc_info
from simp_py import lcd
import time
while 1:
  btc_info = get_btc_info()
  if btc_info['result']=='OK':
    btc = btc_info['btc']
    updated= btc_info['time']
    lcd.text(0,140,updated)
    lcd.text(0,160,'btc:%.04f  ' % btc)
    f=open('btc.dat','a')
    f.write('%s %.04f\n' % (updated,btc))
    f.close()
  time.sleep(10)
