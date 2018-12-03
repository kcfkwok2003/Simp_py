import urequests
from simp_py import mon
import re
import time,sys
r_tm = r'(\d\d\d\d)-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)'
re_tm = re.compile(r_tm)
pv_update=''
v_min=999999999
v_max=0
ts=''
btc=0
def get_btc_info():
  global urequests,time,re_tm,pv_update,v_min,v_max,mon,ts,btc
  try:
    response = urequests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    if response.reason==b'OK' or response.reason=='OK':
      j= response.json()
      updated = j['time']['updatedISO']
      print('updated:%s pv_update:%s' % (updated,pv_update))
      if updated != pv_update:
        m = re_tm.match(updated)
        vs = []
        for i in range(1,7):
          vs.append(int(m.group(i)))
        vs.append(0)
        vs.append(0)
        if not sys.platform=='esp32':
          vs.append(0)
        tm = int(time.mktime(tuple(vs))) + 8 *60*60 # TZ+8
        vv =time.localtime(tm)
        YYYY=vv[0]
        MM=vv[1]
        DD=vv[2]
        hh=vv[3]
        mm=vv[4]
        ss=vv[5]
        ts = '%s-%02d-%02d %02d:%02d:%02d' % (YYYY,MM,DD,hh,mm,ss)
        btc = j['bpi']['USD']['rate_float']
        if btc > v_max:
          v_max=btc
        if btc < v_min:
          v_min =btc
    else:
      response.close()
      return {'result': response.reason}
    response.close()
  except Exception as e:
    raise
    mon.log_exc(e)
    return {'result':'exc'}
  pv_update= updated
  return {'btc':btc, 'time':ts, 'result':'OK', 'max':v_max,'min':v_min}


if __name__=='__main__':
  while 1:
    btc_info=get_btc_info()
    print(btc_info)
    time.sleep(10)
