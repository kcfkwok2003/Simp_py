# ex_uresp.py
# author: C.F.Kwok
# date: 2017-12-11
import time
from simp_py import mon
while 1:
    if mon.chk_ureq():
        ureq=mon.get_ureq()
        mon.data['ureq']=ureq
        uresp = 'Your req is %s' % ureq
        mon.put_uresp(uresp)
    time.sleep(1)
