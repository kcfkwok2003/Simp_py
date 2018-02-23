import time
from simp_py import mon
import os
class URESP:
    global mon,time,os
    def __init__(self):
        os.mountsd()

    def user_loop(self):
        while 1:
            if mon.chk_ureq():
                ureq = mon.get_ureq().strip()
                args= ureq.split(b' ')
                if args[0]==b'ls':
                    self.do_ls()
                elif args[0]==b'rm':
                    self.do_rm(args)
                elif args[0]==b'sd2f':
                    self.do_sd2f(args)
                elif args[0]==b'lsf':
                    self.do_lsf()
                    
            time.sleep(0.1)

    def do_sd2f(self,args):
        for fn in args[1:]:
            if fn==b'main.py' or fn==b'boot.py':
                continue
            fn1= b'/sd/' + fn
            fn2= b'/flash/' + fn
            f1 = open(fn1,'rb')
            f2 = open(fn2,'wb')
            dt = f1.read(500)
            while dt:
                f2.write(dt)
                dt = f1.read(500)
            f1.close()
            f2.close()
        mon.put_uresp(b'ok')
                
    def do_rm(self,args):
        for fn in args[1:]:
            if fn==b'main.py' or fn==b'boot.py':
                continue
            fn= b'/sd/' + fn
            os.remove(fn)
        mon.put_uresp(b'ok')
        
    def do_ls(self):
        fs = os.listdir('/sd')
        txt=b''
        for fn in fs:
            txt+=b'%s\n' % fn
        mon.put_uresp(txt)

    def do_lsf(self):
        fs = os.listdir('/flash')
        txt=b''
        for fn in fs:
            txt+=b'%s\n' % fn
        mon.put_uresp(txt)        


if __name__=='__main__':
    ux=URESP()
    ux.user_loop()
