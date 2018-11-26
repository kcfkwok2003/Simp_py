from btc_price import get_btc_info
from simp_py import lcd
import time
cnt=5
pbtc=0
while cnt>0:
  btc_info = get_btc_info()
  if btc_info['result']=='OK':
    btc = btc_info['btc']
    if pbtc != btc:
      updated= btc_info['time']
      lcd.text(0,140,updated)
      lcd.text(0,160,'btc:%.04f (%s)  ' % (btc,cnt))
      f=open('btc.dat','a')
      f.write('%s %.04f\n' % (updated,btc))
      f.close()
      pbtc=btc
      cnt-=1
  time.sleep(10)
