# -*- coding: utf-8 -*-
VERSION='1.0.5'
YEAR ='2018'
ABOUT_MSG='''
Simp-py-programmer V%s
Copyright %s TienLink Creation
All rights reserved
''' % (VERSION, YEAR)

from kivy.app import App
from kivy.base import EventLoop
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from font_path import FONT_PATH
from text_screen import TextScreen
from file_screen import FileScreen, DATA_PATH

from mbutdialog import MButDialog
from exc import get_exc_details
from dev_com import DEV_COM
import string
import time
from kivy.clock import Clock
import os
CHR_STX='\x02'
CHR_ETX='\x03'
CHR_EOT='\x04'

MON_KA_TIMEOUT=10

APP_OPERATIONS={
    'Ping': 'on_ping',
    'File': 'on_file',    
    'Set..': 'on_settings',
    'Upld':'on_upload',
    'Rst':'on_reset',
    'Mon': 'on_monitor',
    'Up':'on_cursor_up',
    'Dn':'on_cursor_down',
    'Pup': 'on_page_up',
    'Pdn': 'on_page_down',
    '?' : 'on_about',
    }

OPERATION_BUTTONS=['File','Set..','Ping','Upld','Rst','Mon','Up','Dn','Pup','Pdn','?']

MON_OPERATIONS={
    'Start': 'on_mon_start',
    'Stop': 'on_mon_stop',    
    'Up':'on_mon_cursor_up',
    'Dn':'on_mon_cursor_down',
    'Pup': 'on_mon_page_up',
    'Pdn': 'on_mon_page_down',
    'Back': 'on_mon_exit',
    'Send': 'on_out_msg',
    }

MON_BUTTONS=['Start','Stop','Send','Back']
class MainApp(App):
    def build(self):
        self.title='Simp-py-programmer'
        self.filename=''
        Logger.info('kcf: chk_settings_path')
        self.mon_mode=False
        self.mon_rx_cnt=0
        self.mon_tx_cnt=0
        if self.chk_settings_path():
            self.get_settings()
            self.textScreen = TextScreen(name='textScreen',app_operations=APP_OPERATIONS, operation_buttons = OPERATION_BUTTONS)


            self.sm = ScreenManager(transition=FadeTransition())
            self.sm.add_widget(self.textScreen)

            self.sm.current='textScreen'
            self.back = 'textScreen'
            self.dev_com = DEV_COM(self.settings['ip'], self.dev_com_cb)
            return self.sm
        else:
            from msg_dlg import MSG_DLG_KV, MsgDialog 
            from kivy.lang.builder import Builder
            from kivy.factory import Factory
            from kivy.uix.popup import Popup
            Builder.load_string(MSG_DLG_KV)
            Factory.register('MsgDialog',cls=MsgDialog)
            content = MsgDialog(cancel=self.sys_exit, text='No data directory /storage/emulated/0')
            self._popup = Popup(title="Error",content=content,size_hint=(0.9,0.9))
            self._popup.open()
            return self._popup

    def dismiss_popup(self):
        self._popup.dismiss()

    def on_about(self,v):
            from msg_dlg import MSG_DLG_KV, MsgDialog 
            from kivy.lang.builder import Builder
            from kivy.factory import Factory
            from kivy.uix.popup import Popup
            Builder.load_string(MSG_DLG_KV)
            Factory.register('MsgDialog',cls=MsgDialog)
            content = MsgDialog(cancel=self.dismiss_popup, text=ABOUT_MSG)
            self._popup = Popup(title="About",content=content,size_hint=(0.9,0.9))
            self._popup.open()
        
    def dev_com_cb(self,imsg, exc=None):
        Logger.info('kcf: dev_com_cb msg:%s' % imsg)
        current = self.sm.current
        monRoot=None
        settingsRoot=None
        try:
            monRoot=self.sm.get_screen('monScreen').monRoot
        except:
            pass
        try:
            settingsRoot=self.sm.get_screen('settingsScreen').settingsRoot
        except:
            pass
        textRoot=self.sm.get_screen('textScreen').textRoot
        status = textRoot.status
        if current=='monScreen':
            status = monRoot.status
        elif current=='settingsScreen':
            status = settingsRoot.status
            
        if exc is not None:
            exc=str(exc)
            Logger.info('kcf: current:%s exc' % current)
            try:
                status.text=exc
            except:
                exc = get_exc_details()
                Logger.info('exc:%s' % exc)
                status.text = 'Exception'
            return
        lines = imsg.split('\n')
        nlines =[]
        start=False
        done=False
        for line in lines:
            if not start:
                if line==CHR_STX:
                    start=True
                continue
            else:
                if line==CHR_ETX:
                    done=True
                    break
                nlines.append(line)
        Logger.info('kcf: nlines:%s done:%s' % (`nlines`,done))
        if not done:
            return
        
        if nlines[0]=='resp':
            txt = nlines[1]
            tlines = string.split(status.text,'\n')
            Logger.info('kcf: current:%s' % current)
            Logger.info('kcf: tlines;%s' % `tlines`)
            Logger.info('kcf: status:%s' % `status`)
            if len(tlines)>0:
                txt = tlines[-1] +'\n' + txt
                
            if current=='monScreen':
                status.text= txt
                if not self.mon_mode:
                    self.uresped=False
                    Clock.schedule_once(self.timeout_close, 3)
                    #self.dev_com.close()
                else:
                    self.mon_rx_cnt+=1
            elif current=='textScreen':
                status.text=txt
                self.dev_com.close()
            elif current=='settingsScreen':
                status.text=txt
                self.dev_com.close()
            return
        if nlines[0]=='uresp':
            if current=='monScreen':
                txt = nlines[1]
                tlines = string.split(status.text,'\n')
                if len(tlines)>0:
                    txt += tlines[-1] +'\n' + txt
                status.text=nlines[1]
                if not self.mon_mode:
                    self.dev_com.send('\x04\n')
                    self.uresped=True
                    Clock.schedule_once(self.delay_close,0.2)
                    self.dev_com.close()
                else:
                    self.mon_rx_cnt+=1
            return
        if nlines[0]=='mresp':
            if nlines[1][:5]=='_exc:':
                msg = string.join(nlines[1:],'\n')
                monRoot.text_input.text=msg
                return
            if nlines[1]=='hist':
                self.mon_rx_cnt+=1
                msg ='_rx:%d _tx:%d' % (self.mon_rx_cnt,self.mon_tx_cnt) 
                msg += string.join(nlines[2:],'\n')
                monRoot.text_input.text=msg
                status.text='rx:%s' % self.mon_rx_cnt
                Clock.schedule_once(self.nxt_mon_ka, 1)                
                return                
            self.mon_ka_tm=time.time()
            if current=='monScreen':
                self.mon_rx_cnt+=1
                del nlines[0]
                for line in nlines:
                    if line=='':
                        nlines.remove(line)
                nlines.sort()
                nlines.insert(0,'_rx:%d _tx:%d' % (self.mon_rx_cnt,self.mon_tx_cnt)) 
                msg = string.join(nlines,'\n')
                monRoot.text_input.text=msg
                status.text='rx:%s' % self.mon_rx_cnt                
                Clock.schedule_once(self.nxt_mon_ka, 0.3)

    def timeout_close(self,dt):
        if not self.uresped:
            Logger.info('kcf:timeout_close')
            self.dev_com.close()
        
    def delay_close(self,dt):
        Logger.info('kcf: delay_close')
        self.dev_com.close()
        
    def nxt_mon_ka(self,dt):
        # keep alive mon
        if self.mon_mode:
            cont ='\x02\nkamon\n\x03\n'
            self.mon_tx_cnt+=1
            self.dev_com.send(cont,self.settings['ip'])
            
    def on_cursor_up(self,v):
        Logger.info('kcf: on_cursor_up')        
        screen = self.sm.get_screen('textScreen')
        text_input = screen.textRoot.text_input
        text_input.do_cursor_movement('cursor_up')
        text_input.focus=True
        screen.textRoot.status.text='Line:%s' % `text_input.cursor`
        
    def on_cursor_down(self,v):
        Logger.info('kcf: on_cursor_down')
        screen = self.sm.get_screen('textScreen')
        text_input = screen.textRoot.text_input
        text_input.do_cursor_movement('cursor_down')
        text_input.focus=True
        Logger.info('kcf: cusor pos:%s' % `text_input.cursor_pos`)
        screen.textRoot.status.text='Line:%s' % `text_input.cursor`
        
    def on_monitor(self,v):
        if not self.sm.has_screen('monScreen'):
            from mon_screen import MonScreen
            self.monScreen = MonScreen(name='monScreen',app_operations=MON_OPERATIONS,operation_buttons = MON_BUTTONS)
            self.sm.add_widget(self.monScreen)
        self.sm.current='monScreen'

    def on_mon_start(self,v):
        Logger.info('kcf: on_mon_start')
        self.mon_mode=True
        self.mon_rx_cnt=0
        self.mon_tx_cnt=0
        self.mon_ka_tm= time.time()
        monScreen = self.sm.get_screen('monScreen')
        monScreen.monRoot.btns['Back'].disabled=True
        status = monScreen.monRoot.status
        status.text='Monitor start'
        cont ='\x02\nstmon\n\x03\n\x02\nkamon\n\x03\n'
        self.dev_com.send(cont,self.settings['ip'])
        Clock.schedule_once(self.mon_ka_tmo,MON_KA_TIMEOUT)

        
    def mon_ka_tmo(self,dt):
        # keep alive mon check timeout
        if self.mon_mode:
            now = time.time()
            if (now - self.mon_ka_tm) > MON_KA_TIMEOUT:
                monScreen = self.sm.get_screen('monScreen')
                status = monScreen.monRoot.status
                status.text='Monitor timeout'            
            else:
                Clock.schedule_once(self.mon_ka_tmo,MON_KA_TIMEOUT)
                
    def on_mon_stop(self,v):
        Logger.info('kcf: on_mon_stop')
        self.mon_mode=False
        monScreen = self.sm.get_screen('monScreen')
        monScreen.monRoot.btns['Back'].disabled=False        
        status = monScreen.monRoot.status
        status.text='Monitor stop'
        Clock.schedule_once(self.end_mon)

    def end_mon(self,dt):
        monScreen = self.sm.get_screen('monScreen')
        status = monScreen.monRoot.status        
        cont ='\x02\nendmon\n\x03\n\x04\n'
        self.dev_com.send(cont,self.settings['ip'])
        self.wait_resp(status,10)
        
    def on_mon_cursor_up(self,v):
        Logger.info('kcf: on_mon_cursor_up')

    def on_mon_cursor_down(self,v):
        Logger.info('kcf: on_mon_cursor_down')

    def on_mon_page_up(self,v):
        Logger.info('kcf: on_mon_page_up')

    def on_mon_page_down(self,v):
        Logger.info('kcf: on_mon_page_down')

    def on_mon_exit(self,v):
        Logger.info('kcf: on_mon_exit')                        
        self.sm.current='textScreen'

    def on_out_msg(self,v):
        Logger.info('kcf: on_out_msg')
        monRoot = self.sm.get_screen('monScreen').monRoot
        out_msg = monRoot.out_msg.text
        if out_msg !='':
            cont = '\x02\nureq\n%s\n\x03\n' % out_msg
            #if not self.mon_mode:
            #    cont +='\x04\n'
            self.mon_tx_cnt+=1
            monRoot.status.text='Send out msg'
            self.dev_com.send(cont, self.settings['ip'])
        
        # testing
        #if self.mon_mode:
        #    self.mon_mode=False
        #    Clock.schedule_once(self.end_mon,1)
        
    def on_page_up(self,v):
        Logger.info('kcf: on_page_up')        
        screen = self.sm.get_screen('textScreen')
        text_input = screen.textRoot.text_input
        text_input.do_cursor_movement('cursor_pgup')
        text_input.focus=True
        Logger.info('kcf: cusor pos:%s' % `text_input.cursor_pos`)
        screen.textRoot.status.text='Line:%s' % `text_input.cursor`
        
    def on_page_down(self,v):
        Logger.info('kcf: on_page_down')
        screen = self.sm.get_screen('textScreen')
        text_input = screen.textRoot.text_input
        text_input.do_cursor_movement('cursor_pgdown')
        text_input.focus=True
        Logger.info('kcf: cusor pos:%s' % `text_input.cursor_pos`)
        screen.textRoot.status.text='Line:%s' % `text_input.cursor`
        
    def on_start(self):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self,window,key,*largs):
        if key==27:
            # return True for stopping propagation
            if self.sm.current !='textScreen':
                self.sm.current='textScreen'
                return True
            button_names=['Exit','Not Exit']
            callbacks={}
            callbacks['Exit']=self.stop
            dlg = MButDialog(title='Exit App?', message='Press Exit to Exit App',button_names=button_names,callbacks=callbacks)
            dlg.open()
            return True
        
    def on_file(self,v):
        if not self.sm.has_screen('fileScreen'):
            self.fileScreen = FileScreen(name='fileScreen')
            self.sm.add_widget(self.fileScreen)            
        self.sm.current='fileScreen'

    def on_file_cancel(self,v):
        if self.sm.current != 'textScreen':
            self.sm.current='textScreen'

    def on_file_open(self,filename):
        textScreen = self.sm.get_screen('textScreen')
        file_label = textScreen.textRoot.file_label
        self.filename = filename
        file_label.text=filename
        filecont=''
        try:
            f=open('%s/%s' % (self.datapath, self.filename),'rb')
            filecont=f.read()
            f.close()
        except:
            exc = get_exc_details()
            Logger.info('kcf: on_file_open exc:%s' % exc)
            
        self.sm.get_screen('textScreen').textRoot.text_input.text=filecont
        self.sm.get_screen('textScreen').textRoot.text_input.cursor=(0,0)
        self.sm.current='textScreen'

    def on_file_new(self,filename):
        self.filename=filename
        textScreen =self.sm.get_screen('textScreen')
        textScreen.textRoot.file_label.text = filename
        textScreen.textRoot.text_input.text =''
        self.sm.current='textScreen'
        
    def on_file_save(self,filename):
        textScreen = self.sm.get_screen('textScreen')
        file_label = textScreen.textRoot.file_label
        self.filename = filename
        file_label.text=filename
        try:
            f =open('%s/%s' % (self.datapath,self.filename),'wb')
            filecont= self.sm.get_screen('textScreen').textRoot.text_input.text
            f.write(filecont)
            f.close()
        except:
            exc = get_exc_details()
            Logger.info('kcf: on_file_save exc:%s' % exc)
        self.sm.current='textScreen'

    def on_reset(self,v):
        screen_name = self.sm.current
        screen = self.sm.get_screen(screen_name)
        status =None
        if screen_name=='textScreen':
            status = screen.textRoot.status
        elif screen_name=='settingsScreen':
            status = screen.settingsRoot.status
        if status:
            status.text='Sending reset to %s' % self.settings['ip']
            Clock.schedule_once(self.reset_device)
        
    def reset_device(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        cont = '\x02\nreset\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])
        self.wait_resp(status,10)
            
    def on_settings(self,v):
        Logger.info('kcf: on_settings settings:%s' % self.settings)
        if not self.sm.has_screen('settingsScreen'):
            from settings_screen import SettingsScreen
            self.settingsScreen =SettingsScreen(name='settingsScreen',settings=self.settings)
            self.sm.add_widget(self.settingsScreen)            
        self.sm.current ='settingsScreen'

    def cp_examples(self):
        import shutil
        fs = os.listdir('examples')
        if fs:
            for fn in fs:
                Logger.info('kcf: fn:%s' % fn)
                if fn[-4:]=='.pyt':
                    fn1 = fn[:-1]
                    shutil.copyfile('examples/%s' % fn,'%s/%s' % (self.datapath,fn1))
                
    def chk_settings_path(self):
        global DATA_PATH
        Logger.info('chk_settings_path')
        self.datapath=DATA_PATH
        if os.path.isdir(self.datapath):
            return True
        os.makedirs(self.datapath)
        Logger.info('kcf: makedirs %s' % self.datapath)
        if os.path.isdir(self.datapath):
            self.cp_examples()
            return True        
        Logger.info('kcf: makdirs fail')
        return False

    def sys_exit(self):
        import sys
        sys.exit()

    def get_settings(self):
        self.settings={
            'ip': '',
            'STA_ESSID':'',
            'STA_PASSW':'',
            'AP_DEFAULT':'1',
            'AP_PASSW':'12345678',
        }
        try:
            f =open('%s/settings.dat' % self.datapath,'r')
            lines = f.readlines()
            for line in lines:
                ss = line.split(':')
                if len(ss)>1:
                    self.settings[ss[0]]=string.strip(ss[1])

        except:
            exc = get_exc_details()
            Logger.info('kcf: get_settings exc:%s' % exc)
        Logger.info('kcf: get_settings settings:%s ' %  self.settings)

        
    def on_settings_ok(self,settings,text):
        settingsScreen = self.sm.get_screen('settingsScreen')
        self.settings.update(settings)
        try:
            f = open('%s/settings.dat' % self.datapath, 'w')
            f.write(text)
            f.close()
        except:
            exc = get_exc_details()
            Logger.info('kcf: on_settings_ok exc:%s' % exc)
        status = settingsScreen.settingsRoot.status
        status.text='Saved' 
        #self.sm.current=self.back

    def on_settings_cancel(self,v):
        self.sm.current =self.back

    def on_upload(self,cont):
        self.cont=cont
        button_names=['Upload file','Upload as test.py', 'cancel']
        callbacks={}
        callbacks['Upload file']=self.upload_only
        callbacks['Upload as test.py']=self.upload_test
        self.dlg = MButDialog(title='Select Upload option', message='Select upload only and upload and run(will save as test.py', button_names=button_names,callbacks=callbacks)
        self.dlg.open()

    def upload_only(self,v):
        Logger.info('kcf:upload_only')
        self.dlg.dismiss()
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        status.text='Sending content to %s' % self.settings['ip']
        Clock.schedule_once(self.upload_cont_only)
        
    def upload_test(self,v):
        self.dlg.dismiss()
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        status.text='Sending test to %s' % self.settings['ip']
        Clock.schedule_once(self.upload_cont_and_run)

    def on_ping(self,v):
        screen_name = self.sm.current
        screen = self.sm.get_screen(screen_name)
        status =None
        if screen_name=='textScreen':
            status = screen.textRoot.status
        elif screen_name=='settingsScreen':
            status = screen.settingsRoot.status
        if status:
            status.text='Send ping to %s' % self.settings['ip']
            Clock.schedule_once(self.ping)

    def ping(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        cont = '\x02\nping\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])
        self.wait_resp(status, 5)
        
    def wait_resp(self,status, timeout=60):
        return

    def wait_resp_x(self,status, timeout=60):
        cnt =0        
        while 1:
            cnt+=1
            if cnt > timeout:
                status.text='time out'
                self.dev_com.close()
                return            
            time.sleep(1)
            msg = self.dev_com.recv()
            if msg:
                status.text='Got return msg:%s' % msg
                self.dev_com.close()
                return
        
    def upload_cont_and_run(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        f=open('%s/%s' % (DATA_PATH,self.filename),'rb')
        self.cont = f.read()
        f.close()
        cont = '\x02\nsvtest\n'+ self.cont +'\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])
        self.wait_resp(status)

    def upload_cont_only(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        f=open('%s/%s' % (DATA_PATH,self.filename),'rb')        
        self.cont = f.read()
        Logger.info('kcf: cont:%s' % `self.cont`)
        f.close()        
        cont = '\x02\nsvfile:%s\n' % str(self.filename)
        cont += self.cont
        cont +='\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])
        self.wait_resp(status)        
            
    def on_upload_wifi_config(self,v):
        settingsScreen = self.sm.get_screen('settingsScreen')
        status = settingsScreen.settingsRoot.status
        status.text='Sending wifi config to %s' % self.settings['ip']
        Clock.schedule_once(self.upload_wifi_config)

    def upload_wifi_config(self,dt):
        settingsScreen = self.sm.get_screen('settingsScreen')
        status = settingsScreen.settingsRoot.status
        try:
            f=open('wifi_config.py','rb')
            cont = f.read()
            f.close()
            cont = '\x02\nsvwifi\n'+ cont +'\x03\n\x04\n'
            self.dev_com.send(cont, self.settings['ip'])
            self.wait_resp(status,10)
        except:
            exc = get_exc_details()
            status.text='upload_wifi_config error'
            Logger.info('kcf: upload_wifi_config exc:%s' % exc)
            
if __name__=='__main__':
    MainApp().run()        
