from simp_py import tft
from btc_price import get_btc_info
from button import Button
from song import *
btnA=Button(39,'A')
btnB=Button(38,'B')
btnC=Button(37,'C')
NOTES1=[a,a,a,f,cH,a,f,cH,a]
DURATIONS1=[500,500,500,350,150,500,350,150,650]
song=SONG(25)
song.set_notes(NOTES1,DURATIONS1)
pv=0
while 1:
  btc_info= get_btc_info()
  if btc_info['result']=='OK':
    btc = btc_info['btc']
    ts = btc_info['time']
    v_max = btc_info['max']
    v_min = btc_info['min']
    if pv != btc:
      tft.tft.clear()
      tft.tft.font(tft.tft.FONT_Comic)
      tft.tft.text(0,1,'BTC Price',0xffffff)
      tft.tft.text(0,40,'$%.02f' % btc, 0xffffff)
      tft.tft.font(tft.tft.FONT_DejaVu18)
      tft.tft.text(0,90, 'MAX:$%.02f' % v_max, 0x00ff00)
      tft.tft.text(0,130, 'MIN:$%.02f' % v_min, 0xff0000)
      tft.tft.font(tft.tft.FONT_Default)        
      tft.tft.text(0,180,'Update time:',0x888888)
      tft.tft.text(0,200,ts,0x888888)
      if pv>0:
        if btc >= pv:
          tft.tft.triangle(280,90,270,110,290,110,0xff00,0xff00)
        else:
          tft.tft.triangle(270,130,290,130,280,150,0xff0000,0xff0000)
      pv= btc      
  else:
    tft.tft.text(0,200,'result:%s' % btc_info['result'])
  nxttime=time.time() + 10
  while True:
    if time.time() > nxttime:
      break
    if btnA.pressed():
      tft.on()
      song.play()
    if btnB.pressed():
      tft.on()
    if btnC.pressed():
      tft.off()
