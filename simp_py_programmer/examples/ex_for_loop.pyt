# ex_for_loop.py
# author: C.F.Kwok
# date: 2017-12-11
from simp_py import oled
import time
for i in range(10):
    oled.fill(0)
    oled.text('%s' % i, 0, 10)
    oled.show()
    time.sleep(1)
