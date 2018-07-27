from machine import Pin,ADC
from simp_py import tft
from kcf_mqtt import KCF_MQTT
tft.tft.rect(0,220,120,20,0xffffff,0xff0000)  
def hk_conncb(task):
  tft.tft.rect(0,220,120,20,0xffffff,0x00ff00)
  tft.tft.text(2,222,'%s' % task)

def hk_disconncb(task):
  tft.tft.rect(0,220,120,20,0xffffff,0xff0000)
  tft.tft.text(2,222,'%s' % task)    

def hk_datacb(msg):
  topic = msg[1]
  cont = str(msg[2])
  while len(cont) < 39:
    cont +=' '
  if msg[1]=='kcf.drip':
    print('topic is kcf.drip')
    tft.tft.text(0,120,'>%s' %  cont[:19])
    tft.tft.text(0,140,'%s' % cont[19:])
  elif msg[1]=='kcf.drip1':
    print('topic is kcf.drip1')
    tft.tft.text(0,160,'>%s' %  cont[:19])
    tft.tft.text(0,180,'%s' % cont[19:])
      
p25_spk = Pin(25,Pin.OUT)
p25_spk.value(0)

p26_out = Pin(26,Pin.OPEN_DRAIN)
p26_out.value(1)

p35_in = ADC(Pin(35, Pin.IN))

mqtt = KCF_MQTT('eclipse','iot.eclipse.org', hk_conncb, hk_disconncb,hk_datacb)

while True:
  time.sleep(1)
  if mqtt.rtc_synced:
    break
  else:
    mqtt.sync_rtc()
  
subscribed=False
YYYY,MM,DD,hh,pmm,pss,_,_=mqtt.now()
sending=False
sendfx=0
dripping=False
drippingf=False
topic = 'kcf.drip'
topic1 = 'kcf.drip1'
msg='started at %d-%d %02d:%02d' % (MM,DD,hh,pmm)
while True:
  YYYY,MM,DD,hh,mm,ss,_,_=mqtt.now()
  if mqtt.connected:
    if not subscribed:
      subscribed=True
      mqtt.subscribe(topic)
      mqtt.subscribe(topic1)
    if mm != pmm:
      pmm = mm
      mqtt.publish(topic, msg)
      sending=True
      sendfx=0
    if ss != pss:
      tft.tft.text(0,100,'%d-%d %02d:%02d:%02d' % (MM,DD,hh,mm,ss))
      if dripping:
        if drippingf:
          tft.tft.circle(270,50,30,0xffffff,tft.tft.CYAN)
          drippingf=False
        else:
          drippingf=True
          tft.tft.circle(270,50,30,0xffffff,tft.tft.NAVY)
      else:
        if drippingf==False:
          drippingf=True
          tft.tft.circle(270,50,30,0xffffff,tft.tft.NAVY)
      pss=ss
  if sending:
    sendfx+=10
    if sendfx >100:
      tft.tft.rect(140,220,sendfx,20, 0x0,0x0)
      sending=False
    else:
      tft.tft.rect(140,220,sendfx,20, 0xffffff,0xffff00)
        
  v =p35_in.read()
  print ('a0:%d' % v)
  if v > 1000:
    dripping=True
    msg='driped at %d-%d %02d:%02d' % (MM,DD,hh,mm) 
    p26_out.value(0)
  else:
    dripping=False
    p26_out.value(1)
  time.sleep(0.1)
  
  
