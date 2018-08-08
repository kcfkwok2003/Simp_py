from simp_py import lcd
v_min =999999999
v_max=0
f=open('btc.dat','r')
lines = f.readlines()
for line in lines:
  vs =line.split(' ')
  btc = float(vs[2])
  if btc > v_max:
    v_max = btc
  elif btc < v_min:
    v_min = btc
f.close()
lcd.text(0,140,'min:%.04f' % v_min)
lcd.text(0,160,'max:%.04f' % v_max)
