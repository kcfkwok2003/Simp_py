import urequests
from simp_py import mon
import re
import time
r_tm = r'(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)'
re_tm = re.compile(r_tm)
pv_update=''
v_min=999999999
v_max=0
try:
  from btc_mdt import v_min,v_max
except:
  pass
ts=''
btc=0
def get_btc_info():
  global urequests,time,re_tm,pv_update,v_min,v_max,mon,ts,btc
  try:
    response = urequests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    if response.reason==b'OK':
      j= response.json()
      updated = j['time']['updatedISO']
      if updated != pv_update:
        pv_update= updated
        m = re_tm.match(updated)
        vs = []
        for i in range(1,7):
          vs.append(int(m.group(i)))
        vs.append(0)
        vs.append(0)
        tm = int(time.mktime(vs)) + 8 *60*60 # TZ+8
        YYYY,MM,DD,hh,mm,ss,_,_=time.localtime(tm)
        ts = '%s-%02d-%02d %02d:%02d:%02d' % (YYYY,MM,DD,hh,mm,ss)
        btc = j['bpi']['USD']['rate_float']
        mchanged=False
        if btc > v_max:
          v_max=btc
          mchanged=True
        if btc < v_min:
          v_min =btc
          mchanged=True
        if mchanged:
          f=open('btc_mdt.py','w')
          f.write('v_min=%.04f\nv_max=%.04f\n' % (v_min, v_max))
          f.close()
    else:
      response.close()
      return {'result': response.reason}
    response.close()
  except Exception as e:
    mon.log_exc(e)
    return {'result':'exc'}
  return {'btc':btc, 'time':ts, 'result':'OK', 'max':v_max,'min':v_min}


if __name__=='__main__':
  while 1:
    btc_info=get_btc_info()
    print(btc_info)
    time.sleep(10)
