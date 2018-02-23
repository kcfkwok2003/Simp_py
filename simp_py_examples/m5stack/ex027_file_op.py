import time
from simp_py import mon
import os
class URESP:
    global mon,time,os
    def __init__(self):
        pass

    def user_loop(self):
        while 1:
            if mon.chk_ureq():
                ureq = mon.get_ureq().strip()
                args= ureq.split(b' ')
                if args[0]==b'ls':
                    self.do_ls()
                elif args[0]==b'rm':
                    self.do_rm(args)
                    
            time.sleep(0.1)

    def do_rm(self,args):
        for fn in args[1:]:
            if fn==b'main.py' or fn==b'boot.py':
                continue
            os.remove(fn)
        mon.put_uresp(b'ok')
        
    def do_ls(self):
        fs = os.listdir()
        txt=b''
        for fn in fs:
            txt+=b'%s\n' % fn
        mon.put_uresp(txt)


if __name__=='__main__':
    ux=URESP()
    ux.user_loop()
