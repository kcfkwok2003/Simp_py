# app.py
# author: C.F.Kwok
# date: 2017-12-20
import gc
import machine
from simp_py import mon,tft
import sys
import time
import _thread
BUTTON_A_PIN= const(39)
class APP:
    global mon,tft, BUTTON_A_PIN
    def __init__(self,passf=True):
        self.passf=passf
        self.usr_btn =machine.Pin(BUTTON_A_PIN,machine.Pin.IN)

    def test_th(self):
        _thread.allowsuspend(True)
        x=0
        if not self.passf:
            txt='.'
            for i in range(10):
                tft.tft.text(0,100,txt)
                time.sleep(1)
                txt+='.'
            txt+='ok'
            tft.tft.text(0,100,txt)

        while True:
            tft.tft.rect(0,120,320,60,0,0)
            gc.collect()
            ntf = _thread.getnotification()
            if ntf:
                if ntf== _thread.EXIT:
                    return
                elif ntf == _thread.SUSPEND:
                    while _thread.wait() != _thread.RESUME:
                        pass
                else:
                    pass
                    
            if self.usr_btn.value()!=0:
                cont=''
                try:
                    print('read test.py')
                    f=open('test.py')
                    cont=f.read()
                    f.close()
                except:
                    print('no test.py')
                    tft.tft.text(0,120,b'No test.py')
                    return
                mon.data={}
                mon.data['_state']=b'run'
                try:
                    self.cont=cont
                    tft.tft.text(0,120,'Run test.py')
                    print('exec test.py')
                    exec(cont,globals(),{'__name__':'__main__'})
                    print('exec done')
                    tft.tft.text(0,200, 'test.py end')

                except Exception as e:
                    f=open('exc.txt','w')
                    sys.print_exception(e,f)
                    f.close()
                    f=open('exc.txt')
                    mon.data['_exc']=f.read()
                    f.close()
                    tft.tft.text(0,200,'test.py has exc')

                mon.data['_state']=b'stopped'

                while 1:
                    ntf= _thread.wait(30000)
                    if ntf:
                        if ntf==_thread.EXIT:
                            return
            else:
                time.sleep(2)
                while self.usr_btn.value()==0:
                    time.sleep(1)
                tft.tft.text(0,60,'Press key to')
                tft.tft.text(0,80,'clear wifi')
                tft.tft.text(0,100,'settings')
                while self.usr_btn.value()!=0:
                    time.sleep(1)
                import os
                os.remove('wifi_config.py')
                tft.tft.clear()
                tft.tft.text(0,0,'Wifi settings')
                tft.tft.text(0,20,'cleared')
                while 1:
                    time.sleep()
                        
                
app=APP()
        
