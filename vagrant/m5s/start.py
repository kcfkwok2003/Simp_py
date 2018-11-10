# start.py
# author: C.F.Kwok
# date: 2017-12-20
import machine
import network
from simp_py import tft,mon,lcd
import time
import _thread

mach_id = machine.unique_id()
HEADER = 'SIMP_PY 1.2'
BOARD = 'm5stk'
SERVER_PORT=8080
STA_ESSID ='testssid'
STA_PASSW ='testpwd'
AP_DEFAULT=1
AP_ESSID = 'SIMP_PY-%02X%02X' % (mach_id[-2],mach_id[-1])
AP_AUTHMODE=3
AP_PASSW='12345678'
PASSF_INFO1='No valid passkey'
PASSF_INFO2='Wait 10s'
DEF_HOST_CODE='---'

class START:
    global HEADER,SERVER_PORT,PASSF_INFO1,PASSF_INFO2,AP_ESSID,AP_AUTHMODE,mon,tft, BOARD
    def __init__(self,passcode=None):
        global STA_ESSID, STA_PASSW, AP_DEFAULT, AP_PASSW,DEF_HOST_CODE
        from passcodelib import  PASSCODELIB as SEC
        from app import APP
        self.ap=None
        self.passf =False
        self.wifiset=False
        if passcode is None:
            try:
                f=open('pass.key')
                passcode=eval(f.read())
                f.close()
            except:
                print('no pass.key')
                passcode=""
        secx = SEC()
        HOST_CODE=DEF_HOST_CODE
        if secx.veri(passcode,True):
            self.passf=True
            try:
                self.wifiset=True                
                from wifi_config import STA_ESSID, STA_PASSW, AP_DEFAULT, AP_PASSW,HOST_CODE
            except:
                print('import wifi_config exc')
            self.AP_DEFAULT=AP_DEFAULT
            self.AP_PASSW=AP_PASSW
            self.HOST_CODE= HOST_CODE
        else:
            self.AP_DEFAULT=1
            self.AP_PASSW=AP_PASSW
            self.HOST_CODE= HOST_CODE
        self.STA_ESSID=STA_ESSID
        self.STA_PASSW=STA_PASSW
        self.server_port= SERVER_PORT
        if ':' in HOST_CODE:
            try:
                self.server_port=int(HOST_CODE.split(':')[-1])
            except:
                pass
        print('port:%s' % self.server_port)
        self.app=APP(self.passf)
        uid = secx.get_uid()
        self.app.uid= uid
        self.app.psk=passcode
        self.app.header=HEADER
        self.app.board=BOARD
        self.app.HOST_CODE=bytearray( self.HOST_CODE)

    def is_ap(self):
        if self.ap is None:
            return False
        return self.ap.active()

    
    def start(self):
        print ('starting')
        lcd.text(0,0,'Scanning...')
        lcd.text(0,20,'Press A to')
        lcd.text(0,40,'skip test')
        info=['']
        if self.AP_DEFAULT:
            self.setup_ap()
            essid= AP_ESSID
            info=self.ap.ifconfig()
        else:
            essid=self.STA_ESSID
            self.setup_wlan()
            wt = time.time() + 10
            while 1:
                if self.sta.isconnected():
                    info=self.sta.ifconfig()
                    break
                if time.time() > wt:
                    break
            if not self.sta.isconnected():
                self.sta.active(False)
                self.setup_ap()
                essid= AP_ESSID
                info=self.ap.ifconfig()
        lcd.clear()
        lcd.text(0,0,HEADER)
        lcd.text(0,20,essid)
        lcd.text(0,40,info[0])
        lcd.text(0,60,self.HOST_CODE)
        if not self.passf:
            lcd.text(0,80,PASSF_INFO1)
            lcd.text(0,100,PASSF_INFO2)

        self.ip_info= info
        self.myip=info[0]
        self.essid = essid        
        mon.set_dev_info('myip',self.myip)
        mon.set_dev_info('essid',self.essid)
                         
    def setup_wlan(self):
        sta = network.WLAN(network.STA_IF)
        sta.active(True)
        sta.scan()
        #print('sta connect %s %s' % (self.STA_ESSID, self.STA_PASSW))
        sta.connect(self.STA_ESSID, self.STA_PASSW)
        self.sta=sta
        
    def setup_ap(self):
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid=AP_ESSID)
        if AP_AUTHMODE:
            ap.config(authmode=AP_AUTHMODE, password=self.AP_PASSW)
        self.ap=ap
        
def start(passcode=None):
    import micropython
    micropython.alloc_emergency_exception_buf(100)    
    global time
    main = START(passcode)
    main.start()
    from server import SERVER
    server = SERVER(host=main.myip,port=main.server_port)
    main.server=server
    _thread.start_new_thread('server',server.server_th,(main,))       
    _thread.start_new_thread('app',main.app.test_th,(main,))
    return main
    
