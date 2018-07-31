import socket
import sys
import _thread
import machine
import gc
from simp_py import mon,tft
class CLIENT:
    def __init__(self,pr_recv):
        self.pr_recv=pr_recv
        self.cl=None

    def set_cl(self,cl):
        self.cl=cl

    def send(self,msg):
        if self.cl:
            if self.pr_recv:
                print('cl tx:',msg)
            self.cl.send(msg)

    def close(self):
        if self.cl:
            if self.pr_recv:
                print('cl close')
            self.cl.close()
        
class SERVER:
    global mon,gc
    def __init__(self,host='0.0.0.0',port=8080):
        addr = socket.getaddrinfo(host,port)[0][-1]
        self.pr_recv=False
        self.client=CLIENT(self.pr_recv)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)        
        self.s.bind(addr)
        self.s.listen(1)
        print('listening on', addr)
        
    def send(self,cl,msg):
        cl.send(msg)
        if self.pr_recv:
            print('tx:',msg)
            
    def get_mon_info(self):
        txt=b''
        exc= mon.data.get(b'_exc',None)
        if exc:
            txt+=b'_exc:\n%s' % exc
            txt+=b'_state:%s\n' % mon.data['_state']
            return txt
        if mon.history:
            hist = mon.get_hist()
            txt+=b'hist\n'
            txt+=b'_state:%s\n' % mon.data['_state']
            txt+=b'_mem_free:%s\n' % gc.mem_free()
            txt+=b'hist:\n%s' % hist
            return txt
        mon.data['_mem_free']=gc.mem_free()
        keys = mon.data.keys()
        for key in keys:
            v = mon.data[key]
            if type(v) in [type(1),type(0.1),type(b''),type('')]:
                txt+=b'%s:%s\n' % (key,v)
        
        return txt

    def server_th(self,main):
        self.passf = main.app.passf
        self.uid = main.app.uid
        self.psk =main.app.psk
        self.header= main.app.header
        self.board=main.app.board
        _thread.allowsuspend(True)
        while True:
            ntf = _thread.getnotification()
            if ntf:
                if ntf == _thread.EXIT:
                    return
                elif ntf==_thread.SUSPEND:
                    while _thread.wait() != _thread.RESUME:
                        pass
            
            cl, addr = self.s.accept()
            cl.settimeout(60)
            print ('conn from',addr)
            data=b''
            first_line=None
            is_content =None
            self.fd=None
            reset=False
            monx=False
            kamon=False
            ureq=False
            ginfo=False
            b64=False
            execf=False            
            fn=''
            self.client.set_cl(cl)
            mon.set_mon_cl(self.client)
            while True:
                gc.collect()
                try:
                    ss= cl.recv(100)
                    if self.pr_recv:
                        print('rx:', ss)
                except:
                    print('client timeout')
                    mon.set_mon_cl(None)                    
                    cl.close()
                    break
                self.ss = ss
                if ss==b'':
                    mon.set_mon_cl(None)                    
                    cl.close()
                    print ('disc from',addr)
                    break
                data+=ss
                ssx=b''
                #print('data:',data)
                self.data=data
                if b'\n' in data:
                    ss= data.split(b'\n')
                    #print('ss:',ss)
                    for sx in ss[:-1]:
                        if first_line:
                            first_line=False
                            sx = sx.strip()
                            if sx ==b'svtest':
                                print('svtest')
                                self.fd=open('test.py','wb')
                                is_content=True
                            elif sx[:7]==b'svfile:':
                                fn = sx[7:]
                                if fn==b'main.py' or fn==b'boot.py':
                                    fn = 'test.py'
                                print('svfile:%s' % fn)
                                self.fd=open(fn,'wb')
                                is_content=True
                                if fn[-4:]==b'.b64':
                                    b64=True
                            elif sx==b'svwifi':
                                print('svwifi')
                                self.fd=open('wifi_config.py','wb')
                                is_content=True
                            elif sx==b'reset':
                                reset=True
                                print('reset')
                            elif sx==b'stmon':  # start mon
                                monx=True
                                print('stmon')
                            elif sx==b'kamon':  # keep alive mon
                                kamon=True
                            elif sx==b'endmon':  # end mon
                                monx=False
                                print('endmon')
                            elif sx==b'ureq':
                                print('ureq')
                                ureq=True
                            elif sx==b'ginfo':
                                print('ginfo')
                                ginfo=True
                            elif sx==b'exec':
                                print('exec')
                                execf=True                                
                            else:
                                pass
                        else:
                            if sx==b'\x03':
                                #print('ETX')
                                if self.fd:
                                    self.fd.close()
                                if kamon:
                                    kamon=False
                                    mon_info= self.get_mon_info()
                                    mon_txt = b'\x02\nmresp\n%s\n\x03\n' % mon_info
                                    #print('loc:',loc_info)
                                    try:
                                        self.send(cl,mon_txt)
                                    except:
                                        print('send exc')
                                        mon.set_mon_cl(None)
                                        cl.close()
                                        break
                                elif ginfo:
                                    resp=b'\x02\nresp\ninf%s:%s\npsk%s:%s\nok\n\x03\n' % (self.board,self.header,self.uid,self.psk)
                                    if not self.passf:
                                        resp=b'\x02\nresp\ninf%s:%s\npsk%s:???\nok\n\x03\n' % (self.board,self.header,self.uid)
                                    try:
                                        self.send(cl,resp)
                                    except:
                                        print('send exc')
                                        mon.set_mon_cl(None)
                                        cl.close()

                                        break                                    
                                else:
                                    resp=b'\x02\nresp\nok\n\x03\n'
                                    try:
                                        self.send(cl,resp)
                                    except:
                                        print('send exc')
                                        mon.set_mon_cl(None)
                                        cl.close()

                                        break
                                if b64:
                                    import ubinascii,os
                                    f1=open(fn)
                                    f2=open(fn[:-4],'wb')
                                    line=f1.readline()
                                    while line:
                                        binx=ubinascii.a2b_base64(line)
                                        f2.write(binx)
                                        line=f1.readline()
                                    f1.close()
                                    f2.close()
                                    os.remove(fn)
                                first_line=None
                                is_content=None
                                ureq=False
                                ginfo=False
                                b64=False
                                fn=''
                            elif sx==b'\x02':
                                #print('STX')
                                first_line=True
                                self.fd=None
                            elif sx==b'\x04':
                                print('EOT')
                                mon.set_mon_cl(None)
                                cl.close()
                                if reset:
                                    machine.reset()
                                break
                            elif is_content:
                                if self.fd:
                                    self.fd.write(sx)
                                    self.fd.write('\n')
                            elif ureq:
                                mon.put_ureq(sx)
                            elif execf:
                                try:
                                    exec(sx, globals())
                                except:
                                    print('exec error:%s' % sx)
                                    
                    
                    data=ss[-1]
                else:
                    print('\\n not in data')
                try:
                    if ssx:
                        self.send(cl,ssx)
                except:
                    print('send exc')
                    mon.set_mon_cl(None)
                    cl.close()
                    break
                




    
