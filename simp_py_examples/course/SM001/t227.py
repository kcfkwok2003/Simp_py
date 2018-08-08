from simp_py import lcd,tft
from btc_price import get_btc_info
from button import Button
from song import *
btnB=Button(38,'B')
btnC=Button(37,'C')
NOTES1=[a,a,a,f,cH,a,f,cH,a]
DURATIONS1=[500,500,500,350,150,500,350,150,650]
song=SONG(25)
song.set_notes(NOTES1,DURATIONS1)
HI_TRIGGER=6538
LO_TRIGGER=6518
hi_triggered=False
lo_triggered=False
pv=0
while 1:
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
      if not hi_triggered:
        if btc > HI_TRIGGER:
          hi_triggered=True
          song.play()
      if not lo_triggered:
        if btc < LO_TRIGGER:
          lo_triggered=True
          song.play()
          
  else:
    lcd.text(0,200,'result:%s' % btc_info['result'])
  nxttime=time.time() + 10
  while True:
    if time.time() > nxttime:
      break
    if btnB.pressed():
      tft.on()
    if btnC.pressed():
      tft.off()
