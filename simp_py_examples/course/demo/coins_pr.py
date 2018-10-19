import urequests
from simp_py import lcd,tft
from button import Button
import time
import gc

idx=1027
def get_info(idx):
  global urequests,time
  try:
    response= urequests.get('https://api.coinmarketcap.com/v2/ticker/%d/' % idx)
    if response.reason==b'OK':
      j= response.json()
      return j['data']
  except Exception as e:
    print ('idx:%s exc:%s' % (idx,e))

def make_tms(tm):
  global time
  tmx = time.localtime(tm+ 8*60*60)
  YYYY,MM,DD,hh,mm,ss,_,_=tmx
  tms ='%d-%d %02d:%02d' % (MM,DD,hh,mm)
  return tms

def show_data(x,y,data):
  global make_tms,lcd
  namex=data['name']
  sym = data['symbol']
  pr = data['quotes']['USD']['price']        
  tm = data['last_updated']
  tms = make_tms(tm)
  lcd.text(x,y,'%s (%s)' % (namex,sym))
  lcd.text(x,y+20,'USD %.04f' % pr)    
  lcd.text(x,y+40,'%s' % tms)
      
if __name__=='__main__':
  btnA=Button(39)
  btnC=Button(37)
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
      lcd.clear()
      y=0
      for idx in coins:
        data= old_data[idx]
        show_data(0,y,data)
        y+=80
    now = time.time()
    exp = now + 10
    while now < exp:
      if btnA.isPressed():
        tft.on()
      if btnC.isPressed():
          tft.off()      
      time.sleep(0.5)
      now = time.time()
