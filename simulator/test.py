from simp_py import lcd
from btc_price import get_btc_info
pv=0
while True:
  btc_info= get_btc_info()
  if btc_info['result']=='OK':
    btc = btc_info['btc']
    ts = btc_info['time']
    v_max = btc_info['max']
    v_min = btc_info['min']
    if pv != btc:
      lcd.clear()
      lcd.font(lcd.FONT_Comic)
      lcd.text(0,1,'BTC Price',0xffffff)
      lcd.text(0,40,'$%.02f' % btc, 0xffffff)
      lcd.font(lcd.FONT_DejaVu18)
      lcd.text(0,90, 'MAX:$%.02f' % v_max, 0x00ff00)
      lcd.text(0,130, 'MIN:$%.02f' % v_min, 0xff0000)
      lcd.font(lcd.FONT_Default)        
      lcd.text(0,180,'Update time:',0x888888)
      lcd.text(0,200,ts,0x888888)
      if pv>0:
        if btc >= pv:
          lcd.triangle(280,90,270,110,290,110,0xff00,0xff00)
        else:
          lcd.triangle(270,130,290,130,280,150,0xff0000,0xff0000)
      pv= btc      
  else:
    lcd.text(0,200,'result:%s' % btc_info['result'])
  time.sleep(10)
  
