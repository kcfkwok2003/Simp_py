from simp_py import lcd,logging,buttonA,buttonB,buttonC
import gc
import time
import urequests

idx=1027
def get_info(idx):
  global urequests,time,logging
  try:
    logging.debug('requests.get +')
    response= urequests.get('https://api.coinmarketcap.com/v2/ticker/%d/' % idx)
    if response.reason=='OK':
      j= response.json()
      logging.debug('requests.get -')
      return j['data']
  except Exception as e:
    print ('idx:%s exc:%s' % (idx,e))
  logging.debug('requests.get --')
  
def make_tms(tm):
  global time
  tmx = time.localtime(tm)  #+ 8*60*60)
  MM = tmx[1]
  DD = tmx[2]
  hh = tmx[3]
  mm = tmx[4]
  tms ='%d-%d %02d:%02d' % (MM,DD,hh,mm)
  return tms

def show_data(x,y,data):
  global make_tms,lcd,logging
  logging.debug('show_data +')
  namex=data['name']
  sym = data['symbol']
  pr = data['quotes']['USD']['price']        
  tm = data['last_updated']
  tms = make_tms(tm)
  lcd.text(x,y,'%s (%s)' % (namex,sym))
  lcd.text(x,y+20,'USD %.04f' % pr)    
  lcd.text(x,y+40,'%s' % tms)
  logging.debug('show_data -')
  
if __name__=='__main__':
  old_data={}
  coins=[1,1027,1831]
  while 1:
    changed=False
    for idx in coins:
      data =get_info(idx)
      if data is not None:
        if idx in old_data.keys():
          if old_data[idx]['last_updated']== data['last_updated']:
            continue
        old_data[idx]=data
        changed=True
      gc.collect()
    if changed:
      logging.debug('lcd.clear +')
      lcd.clear()
      logging.debug('lcd.clear -')
      y=0
      for idx in coins:
        data= old_data[idx]
        show_data(0,y,data)
        y+=80

    expire= time.time() + 10
    while time.time() < expire:
      if buttonA.isPressed():
        print('buttonA is pressed')
      if buttonB.isPressed():
        print('buttonB is pressed, tft.on')
        tft.on()
      if buttonC.isPressed():
        print('buttonC is pressed, tft.off')
        tft.off()
      time.sleep(0.1)
