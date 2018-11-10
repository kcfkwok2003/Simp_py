# app.py
# author: C.F.Kwok
# date: 2017-12-20
import gc
import machine
from simp_py import mon,tft,lcd
import sys
import time
import _thread
BUTTON_A_PIN= const(39)
class APP:
    global mon,tft, BUTTON_A_PIN
    def __init__(self,passf=True):
        self.passf=passf
        self.usr_btn =machine.Pin(BUTTON_A_PIN,machine.Pin.IN)

    def test_th(self,main):
        self.main=main        
        _thread.allowsuspend(True)
        x=0
        if not self.passf:
            txt='.'
            for i in range(10):
                lcd.text(0,100,txt)
                time.sleep(1)
                txt+='.'
            txt+='ok'
            lcd.text(0,100,txt)

        while True:
            lcd.rect(0,120,320,60,0,0)
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
                if self.main.is_ap():
                    lcd.text(0,120,'Press A to run')
                    while self.usr_btn.value()!=0:
                        time.sleep(0.5)
                cont=''
                try:
                    print('read test.py')
                    f=open('test.py')
                    cont=f.read()
                    f.close()
                except:
                    print('no test.py')
                    lcd.text(0,120,b'No test.py')
                    return
                mon.data={}
                mon.data['_state']=b'run'
                try:
                    self.cont=cont
                    lcd.text(0,120,'Run test.py')
                    print('exec test.py')
                    exec(cont,globals(),{'__name__':'__main__'})
                    print('exec done')
                    lcd.text(0,200, 'test.py end')

                except Exception as e:
                    f=open('exc.txt','w')
                    sys.print_exception(e,f)
                    f.close()
                    f=open('exc.txt')
                    mon.data['_exc']=f.read()
                    f.close()
                    lcd.text(0,200,'test.py has exc')

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
                lcd.text(0,80,'Press A to')
                lcd.text(0,100,'clear wifi')
                lcd.text(0,120,'settings')
                while self.usr_btn.value()!=0:
                    time.sleep(1)
                import os
                os.remove('wifi_config.py')
                lcd.clear()
                lcd.text(0,0,'Wifi settings')
                lcd.text(0,20,'cleared')
                while 1:
                    time.sleep()
                        
                
app=APP()
        
