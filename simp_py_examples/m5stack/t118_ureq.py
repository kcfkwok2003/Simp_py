from simp_py import mon, tft
lcd = tft.tft
while True:
  if mon.chk_ureq():
    ureq = mon.get_ureq()
    uresp = 'your req is %s' % ureq
    mon.put_uresp(uresp)
    lcd.text(0,50,'ureq is “%s' % ureq)
  time.sleep(0.1)
