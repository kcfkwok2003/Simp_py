import urequests
from simp_py import lcd, mon
while 1:
  try:
    response = urequests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    if response.reason==b'OK':
      data= response.json()
      updated=data['time']['updatedISO']
      btc = data['bpi']['USD']['rate_float']
      lcd.text(0,140,updated)
      lcd.text(0,160,'btc:%.04f  ' % btc)
    else:
      lcd.text(0,140,'err:%s' % response.reason)
  except Exception as e:
    mon.log_exc(e)
  time.sleep(10)
    
      
