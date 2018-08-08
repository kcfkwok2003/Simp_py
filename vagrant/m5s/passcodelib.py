# passcodelib.py
# author: C.F.Kwok
# date: 2018-1-18
import hashlib
class Machine:
    def unique_id(self):
        return b'\x00\x00\x00\x00'
try:
    import machine
except:
    machine = Machine()
PHASH = 6227048663865  # simplepython

SECRETS=[1,2,3,4,5]
try:
    from simp_py_sec import SECRETS
except:
    pass

def make_phash(pass1):
    global hashlib, SECRETS
    N1,N2,N3,N4,N5 = SECRETS
    x = hashlib.sha1(pass1)
    y = hashlib.sha1(pass1[N1:])
    vs = x.digest()
    ws = y.digest()
    phash=0
    for v in vs[N2:]:
        if type(v)!=type(1):
            v= ord(v)
        phash=phash*N3 + v
    for v in ws[N4:]:
        if type(v)!=type(1):
            v= ord(v)
        phash=phash*N5 + v        
    return phash

class PASSCODELIB:
    global PAHSH
    def __init__(self, pw=''):
        self.pw=pw

    def get_uid(self):
        uid = machine.unique_id()
        txt=''
        for i in range(len(uid)):
            v = uid[i]
            if type(v)!=type(1):
                v=ord(v)
            txt+='%02X' % v
        return txt
            
    def enc(self, uidtxt=None):
        if not make_phash(self.pw)==PHASH:
            print ('fail')
            return
        if uidtxt is None:
            uidtxt=self.get_uid()
        print(uidtxt)
        v = make_phash(uidtxt)
        return v

    def ienc(self,uidtxt, intern=False):
        if not intern:
            return
        v = make_phash(uidtxt)
        return v

    def veri(self,passcode, intern=False):
        if not intern:
            return False
        ehash = self.ienc(self.get_uid(), intern)
        if passcode == ehash:
            return True

    def get_app(self,passcode,intern=False):
        if not intern:
            return False
        if self.veri(passcode, intern):
            print('get_app ok')
            from app import APP
            app=APP()
            return app
        return None



    
