# -*- coding: utf-8 -*-
from kivy.core.window import Window
Window.clearcolor=(0.6,0.6,0.6,1)
VERSION='1.0.6'
YEAR ='2018'
APP_NAME='Simp-py'
ABOUT_MSG='''
Simp-py-programmer V%s
Copyright %s TienLink Creation
All rights reserved
''' % (VERSION, YEAR)
SEND_EXEC=True
DATA_PATH='/data/simp_py_dat'
EX_PATH ='/data/simp_py_ex/course'

RADIO_FILE_NAMES=['Open Examples',
             'Open         ',
             'Save         ',
             'Save as      ',
             'New file     ',
             'Font py      ',]


RADIO_HELP_NAMES=['Help content        ',
                  'Download GNUFont    ',
                  'Download Course     ',
                  'Clean course        ',
                  'Download Simulator  ',
                  ]
RADIO_UPLOAD_NAMES=['Upload as test.py',
                    'Upload           ',
                    'Upload binary    ',
                    ]
from kivy.app import App
from kivy.base import EventLoop
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from font_path import FONT_PATH
from text_screen import TextScreen
#from file_screen import FileScreen, DATA_PATH
from file_screen1 import FileScreen
import binascii

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
    'File': 'on_file_m',   #'on_file',    
    'Set..': 'on_settings',
    'Upld':'on_upload_m',   #'on_upload',
    'Rst':'on_reset',
    'Mon': 'on_monitor',
    'Up':'on_cursor_up',
    'Dn':'on_cursor_down',
    'Pup': 'on_page_up',
    'Pdn': 'on_page_down',
    'Help' : 'on_help_m',   #'on_about',
    }

OPERATION_BUTTONS=['File','Set..','Ping','Upld','Rst','Mon','Help']

MON_OPERATIONS={
    'Start': 'on_mon_start',
    'Stop': 'on_mon_stop',    
    'Up':'on_mon_cursor_up',
    'Dn':'on_mon_cursor_down',
    'Pup': 'on_mon_page_up',
    'Pdn': 'on_mon_page_down',
    'Back': 'on_mon_exit',
    'Send': 'on_out_msg',
    'Clr': 'on_clr_msg',
    }

MON_BUTTONS=['Start','Stop','Clr','Back']
class MainApp(App):
    def build(self):
        self.title=APP_NAME
        self.filename=''
        Logger.info('kcf: chk_settings_path')
        self.mon_mode=False
        self.mon_rx_cnt=0
        self.mon_tx_cnt=0
        self.download_sim_cont=False
        if self.chk_settings_path():
            self.get_settings()
            self.textScreen = TextScreen(name='textScreen',app_operations=APP_OPERATIONS, operation_buttons = OPERATION_BUTTONS)


            self.sm = ScreenManager(transition=FadeTransition())
            self.sm.add_widget(self.textScreen)

            self.sm.current='textScreen'
            self.back = 'textScreen'
            self.dev_com = DEV_COM(self.settings['ip'], self.dev_com_cb, self.settings)
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

    def on_help_m(self,v):
        from radio_dlg import MButDialog
        button_names =['     ','CANCEL','OK']
        callbacks={}
        callbacks['OK']=self.on_help_m_ok
        callbacks['CANCEL']=self.on_help_m_can
        self.dlg = MButDialog(title='Help operation',message='Please select operation',button_names=button_names,callbacks=callbacks,size_hint=(0.5,0.7),radio_names=RADIO_HELP_NAMES)
        self.dlg.open()

    def on_help_m_ok(self,v):
        print('on_help_m_ok %s' % v)
        keys =self.dlg.radios
        for keyx in keys:
            print('%s:%s' % (keyx,self.dlg.radios[keyx].state)) # dir(self.dlg.radios[keyx])))
            if self.dlg.radios[keyx].state=='down':
                self.on_help_m_op(keyx)
                break
        self.dlg.dismiss()
        
    def on_help_m_can(self,v):
        self.dlg.dismiss()

    def on_help_m_op(self,opx):
        if opx=='Help content':
            self.on_about(opx)
        elif opx=='Download Simulator':
            self.on_download_simulator()
        elif opx=='Download GNUFont':
            self.on_download_gnufont()
        elif opx=='Download Course':
            self.on_download_course()
        elif opx=='Clean course':
            self.on_clean_course()
        else:
            print('on_help_m_op %s not-imp' % opx)
            
    def on_download_simulator(self):
        print('on_download_simulator')
        self.download_sim_cont=False
        sim_path="https://raw.githubusercontent.com/kcfkwok2003/Simp_py/master/simulator/simp_py"
        sim_file_list=sim_path +'/file.list'
        import urllib2
        cont=''
        try:
            response = urllib2.urlopen(sim_file_list)
            cont= response.read()
            print('file.list:%s' % cont)
        except:
            exc = get_exc_details()
            Logger.info('exc:%s' % exc)
            #status.text='Download fail'
            self.textScreen.textRoot.status.text+='..Download fail'
            return
        lib_path = DATA_PATH+'/simp_py'
        if not os.path.isdir(lib_path):
            os.makedirs(lib_path)
        if cont!='':
            downloadings={}
            lines=cont.split('\n')
            for line in lines:
                fname=line.strip()
                urlpath = '%s/%s' % (sim_path, fname)
                savepath ='%s/%s' % (lib_path,fname)
                downloadings[fname]=(urlpath, savepath)
            self.downloadings=downloadings
            self.download_list=self.downloadings.keys()
            self.download_list.sort()
            self.download_total=len(self.download_list)
            self.download_cnt=1
            self.download_idx=0
            fname= self.download_list[self.download_idx]
            self.textScreen.textRoot.status.text='%s/%s %s' % (self.download_cnt, self.download_total,fname)
            self.download_sim_cont=True
            Clock.schedule_once(self.url_download,0.1)


    def on_download_simulator1(self):
        print('on_download_simulator1')
        self.download_sim_cont=False
        sim_path="https://raw.githubusercontent.com/kcfkwok2003/Simp_py/master/simulator"
        sim_file_list=sim_path +'/file.list'
        import urllib2
        cont=''
        try:
            response = urllib2.urlopen(sim_file_list)
            cont= response.read()
            print('file.list:%s' % cont)
        except:
            exc = get_exc_details()
            Logger.info('exc:%s' % exc)
            #status.text='Download fail'
            self.textScreen.textRoot.status.text+='..Download fail'
            return
        lib_path = DATA_PATH
        if not os.path.isdir(lib_path):
            os.makedirs(save_path)
        if cont!='':
            downloadings={}
            lines=cont.split('\n')
            for line in lines:
                fname=line.strip()
                urlpath = '%s/%s' % (sim_path, fname)
                savepath ='%s/%s' % (lib_path,fname)
                downloadings[fname]=(urlpath, savepath)
            self.downloadings=downloadings
            self.download_list=self.downloadings.keys()
            self.download_list.sort()
            self.download_total=len(self.download_list)
            self.download_cnt=1
            self.download_idx=0
            fname= self.download_list[self.download_idx]
            self.textScreen.textRoot.status.text='%s/%s %s' % (self.download_cnt, self.download_total,fname)
            Clock.schedule_once(self.url_download,0.1)            
            
    def on_download_gnufont(self):
        msg = 'Download GNUFont not implemented'
        print(msg)
        self.textScreen.textRoot.status.text=msg

    def on_download_course(self):
        course_code = self.settings['course_code']
        print('on_download_course %s' % course_code)
        course_path="https://raw.githubusercontent.com/kcfkwok2003/Simp_py/master/simp_py_examples/course/" + course_code
        course_file_list = course_path +'/file.list'
        import urllib2
        cont=''
        try:
            response = urllib2.urlopen(course_file_list)
            cont = response.read()
            print('file.list:%s' % cont)
        except:
            exc = get_exc_details()
            Logger.info('exc:%s' % exc)
            #status.text='Download fail'
            self.textScreen.textRoot.status.text+='..Download fail'
            return
        if not os.path.isdir(EX_PATH):
            os.makedirs(EX_PATH)
        if cont!='':
            downloadings={}
            lines=cont.split('\n')
            for line in lines:
                fname=line.strip()
                urlpath = '%s/%s' % (course_path, fname)
                savepath ='%s/%s' % (EX_PATH,fname)
                downloadings[fname]=(urlpath, savepath)
            self.downloadings=downloadings
            self.download_list=self.downloadings.keys()
            self.download_list.sort()
            self.download_total=len(self.download_list)
            self.download_cnt=1
            self.download_idx=0
            fname= self.download_list[self.download_idx]
            self.textScreen.textRoot.status.text='%s/%s %s' % (self.download_cnt, self.download_total,fname)
            Clock.schedule_once(self.url_download,0.1)


    def url_download(self,t):
        import urllib2
        fname= self.download_list[self.download_idx]
        urlpath, savepath = self.downloadings[fname]
        try:
            response=urllib2.urlopen(urlpath)
            contx = response.read()
            f=open(savepath, 'wb')
            f.write(contx)
            f.close()
        except:
            exc = get_exc_details()
            Logger.info('exc:%s' % exc)
            #status.text='Download fail'
            self.textScreen.textRoot.status.text+='..Download fail'
            return
        self.download_cnt+=1
        self.download_idx+=1
        if self.download_cnt > self.download_total:
            self.textScreen.textRoot.status.text='%s files downloaded' % self.download_total
            if self.download_sim_cont:
                self.on_download_simulator1()
            return
        fname= self.download_list[self.download_idx]
        self.textScreen.textRoot.status.text='%s/%s %s' % (self.download_cnt, self.download_total,fname)
        Clock.schedule_once(self.url_download,0.1)        
        
        
    def on_clean_course(self):
        fnames=os.listdir(EX_PATH)
        for fname in fnames:
            fpath ='%s/%s' % (EX_PATH,fname)
            if os.path.isfile(fpath):
                os.remove(fpath)
        self.textScreen.textRoot.status.text='Clean course'
        
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
                devinfo={}
                if nlines[1][:3]=='inf':
                    if nlines[3]=='ok':
                        status.text+='\nok'
                        ss =nlines[1][3:].split(':')
                        devinfo['Board']=ss[0]
                        devinfo['Header']=ss[1]
                        if nlines[2][:3]=='psk':
                            ss=nlines[2][3:].split(':')
                            devinfo['UID']=ss[0]
                            devinfo['Passkey']=ss[1]
                        self.devinfo=devinfo
                        Clock.schedule_once(self.show_devinfo,0.2)
                        self.dev_com.close()
                        return
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
                nlines.insert(0,'_rx:%d' % self.mon_rx_cnt) 
                msg = string.join(nlines,'\n')
                monRoot.text_input.text=msg
                #status.text='rx:%s' % self.mon_rx_cnt                
                Clock.schedule_once(self.nxt_mon_ka, 0.3)

    def show_devinfo__(self,dt):
        print('show_devinfo')
        from msg_dlg import MSG_DLG_KV, MsgDialog 
        from kivy.lang.builder import Builder
        from kivy.factory import Factory
        from kivy.uix.popup import Popup
        Builder.load_string(MSG_DLG_KV)
        Factory.register('MsgDialog',cls=MsgDialog)
        text="Board:%(Board)s\nHeader:%(Header)s\nUID:%(UID)s\nPasskey:%(Passkey)s" % self.devinfo
        content = MsgDialog(cancel=self.dismiss_popup, text=text)
        self._popup = Popup(title="Device info",content=content,size_hint=(0.5,0.5))
        self._popup.open()
        return self._popup

    def get_conn_dev(self):
        conn_dev = '%s/%s' % (self.devinfo.get('Board','---'),self.devinfo.get('UID','---'))
        return conn_dev
    
    def show_devinfo(self,dt):
        print('show_devinfo')
        from confm_dlg import MButDialog
        text="Board:%(Board)s\nHeader:%(Header)s\nUID:%(UID)s\nPasskey:%(Passkey)s" % self.devinfo
        conn_dev = self.get_conn_dev()
        button_names=[' ','OK',' ']

        callbacks={}
        title='Device info'
        print('conn_dev:%s' % conn_dev)
        print("settings['CONN_DEVICE']:%s" % self.settings['CONN_DEVICE'])
        if self.settings['CONN_DEVICE'] !=conn_dev:
            button_names=[' ','CANCEL','SET']            
            title = 'Device not match, set it?'
        callbacks['SET']=self.set_conn_dev
        callbacks['CANCEL']=self.set_can
        callbacks['OK']= self.set_can
        self.dlg = MButDialog(title=title,message=text,button_names=button_names,callbacks=callbacks,size_hint=(0.5,0.7))
        self.dlg.open()

    def set_conn_dev(self,v):
        print('set_conn_dev')
        self.settingsScreen.settingsRoot.tinputs['CONN_DEVICE'].text=self.get_conn_dev()
        self.settings['CONN_DEVICE']= self.get_conn_dev()
        self.dlg.dismiss()
        
    def set_can(self,v):
        print('set_can')
        self.dlg.dismiss()
        
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
        status.text='Start monitoring of device ip: %s' % self.settings['ip']
        monScreen.monRoot.mon_label.text='Monitoring'
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
        status.text='Stop Monitoring'
        monScreen.monRoot.mon_label.text='Not connected'
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

    def on_clr_msg(self,v):
        monRoot = self.sm.get_screen('monScreen').monRoot
        monRoot.out_msg.text=''
        monRoot.status.text=''
        monRoot.text_input.text=''
        
    def on_out_msg(self,v):
        Logger.info('kcf: on_out_msg')
        monRoot = self.sm.get_screen('monScreen').monRoot
        out_msg = monRoot.out_msg.text
        if out_msg !='':
            if SEND_EXEC:
                cont = '\x02\nexec\n%s\n\x03\n\x04\n' % out_msg
            else:
                cont = '\x02\nureq\n%s\n\x03\n' % out_msg
            #if not self.mon_mode:
            #    cont +='\x04\n'
            self.mon_tx_cnt+=1
            monRoot.status.text='Send out msg'
            self.dev_com.send(cont, self.settings['ip'])
        else:
            self.monScreen.monRoot.status.text='No content!'
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

    def on_file_m(self,v):
        self.textScreen.textRoot.status.text=''        
        from radio_dlg import MButDialog
        button_names =[' ','CANCEL','OK']
        callbacks={}
        callbacks['OK']=self.on_file_m_ok
        callbacks['CANCEL']=self.on_file_m_can
        self.dlg = MButDialog(title='File operation',message='Please select operation',button_names=button_names,callbacks=callbacks,size_hint=(0.5,0.7),radio_names=RADIO_FILE_NAMES)
        self.dlg.open()

    def on_file_m_ok(self,v):
        print('on_file_m_ok %s' % v)
        keys =self.dlg.radios
        for keyx in keys:
            print('%s:%s' % (keyx,self.dlg.radios[keyx].state)) # dir(self.dlg.radios[keyx])))
            if self.dlg.radios[keyx].state=='down':
                self.on_file_m_op(keyx)
                break
        self.dlg.dismiss()
        
    def on_file_m_can(self,v):
        self.dlg.dismiss()

    def on_file_m_op(self, opx):
        screen = self.sm.get_screen('textScreen')
        #screen.textRoot.status.text='opening file list...'
        self.m_op_sch=opx
        Clock.schedule_once(self.on_file_m_op_sch)

    def on_file_m_op_sch(self,v):
        handler=None
        title=''
        self.datapath=DATA_PATH
        if self.m_op_sch=='Open':
            handler=self.on_file_open
            title='Simp-py [simp_py_dat]'
            self.datapath=DATA_PATH            
        elif self.m_op_sch =='Open Examples':
            self.datapath=EX_PATH
            handler=self.on_file_open_ex
            title='Simp-py [course]'
        elif self.m_op_sch=='Save':
            self.datapath=DATA_PATH
            self.on_file_save(self.filename)
            return
        elif self.m_op_sch=='Save as':
            self.datapath=DATA_PATH
            self.on_file_save_as(self.filename)
            return
        elif self.m_op_sch=='New file':
            self.datapath=DATA_PATH
            self.on_file_new_m()
            return
        else:
            msg ='%s not implemented' % self.m_op_sch
            self.textScreen.textRoot.status.text=msg
            print('m_op_sch :%s not implemented' % self.m_op_sch)
            return
        if self.sm.has_screen('fileScreen'):
            self.sm.remove_widget(self.fileScreen)
        self.fileScreen=FileScreen(name='fileScreen',datapath=self.datapath,handler=handler,title=title)
        self.sm.add_widget(self.fileScreen)
        self.sm.current = 'fileScreen'

    def on_file_new_m(self):
        from inp_dlg import MButDialog
        button_names=[' ','CANCEL','OK']
        callbacks={}
        callbacks['OK']=self.new_file
        self.dlg=MButDialog(title='New file',message='Input new file name',button_names=button_names,callbacks=callbacks,size_hint=(0.8,0.5))
        self.dlg.open()

    def new_file(self,v):
        self.filename=filename =self.dlg.ti.text        
        textScreen =self.sm.get_screen('textScreen')
        textScreen.textRoot.status.text = 'New file'
        textScreen.textRoot.set_text('')
        #textScreen.textRoot.text_input.text =''
        self.sm.current='textScreen'
        self.dlg.dismiss()
        
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)
        
        
    def on_file_save_as(self,fn):
        from inp_dlg import MButDialog
        button_names=[' ','CANCEL','OK']
        callbacks={}
        callbacks['OK']=self.save_as
        self.dlg=MButDialog(title='Save as',message='Input file name to save',button_names=button_names,callbacks=callbacks,size_hint=(0.8,0.5))
        self.dlg.open()        

    def save_as(self,v):
        fname =self.dlg.ti.text
        self.datapath=DATA_PATH
        print('save as fname:%s' % fname)
        fpath='%s/%s' % (DATA_PATH, fname)
        textScreen = self.sm.get_screen('textScreen')
        try:
            f =open(fpath,'wb')
            filecont= self.sm.get_screen('textScreen').textRoot.text_input.text
            f.write(filecont)
            f.close()
            textScreen.textRoot.status.text='Saved to %s' % (fpath)
        except:
            exc = get_exc_details()
            Logger.info('kcf: save_as exc:%s' % exc)
            textScreen.textRoot.status.text='Save to %s failed' % fpath
            self.sm.current='textScreen'
            self.dlg.dismiss()
            return
        self.sm.current='textScreen'        
        self.dlg.dismiss()
        self.filename=fname
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)
                
    def on_file(self,v):
        print('on_file ...')
        screen = self.sm.get_screen('textScreen')
        #screen.textRoot.status.text='opening file list...'
        Clock.schedule_once(self.on_file_1)

    def on_file_1(self,v):
        if not self.sm.has_screen('fileScreen'):
            self.fileScreen = FileScreen(name='fileScreen')
            self.sm.add_widget(self.fileScreen)
        self.sm.current='fileScreen'

    def on_file_cancel(self,v):
        if self.sm.current != 'textScreen':
            self.sm.current='textScreen'

    def is_jpg(self,filename):
        if filename[-4:].lower()=='.jpg':
            return True
        return False
    
    def on_file_open(self,filename):
        self.filename = filename
        if self.is_jpg(filename):
            Clock.schedule_once(self.on_file_open_jpg_1)
            return
        #fileScreen = self.sm.get_screen('fileScreen')
        #fileScreen.fileRoot.status.text='opening file...'
        Clock.schedule_once(self.on_file_open_1)

    def on_file_open_jpg_1(self,dt):
        from photo_screen import PhotoScreen
        if self.sm.has_screen('photoScreen'):
            photoScreen = self.sm.get_screen('photoScreen')
            self.sm.remove_widget(photoScreen)
        self.photoScreen = PhotoScreen(name='photoScreen',datapath=DATA_PATH,filename=self.filename)
        self.sm.add_widget(self.photoScreen)
        self.sm.current='photoScreen'
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)
        
        
    def on_file_open_1(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        file_label = textScreen.textRoot.file_label
        file_label.text=self.filename
        filecont=''
        try:
            f=open('%s/%s' % (DATA_PATH, self.filename),'rb')
            filecont=f.read()
            f.close()
        except:
            exc = get_exc_details()
            Logger.info('kcf: on_file_open exc:%s' % exc)
            #textScreen.textRoot.text_input.text=filecont
            textScreen.textRoot.set_text(filecont)
            textScreen.textRoot.text_input.cursor=(0,0)
            self.sm.current='textScreen'
            return
        
        #textScreen.textRoot.text_input.text=filecont
        textScreen.textRoot.set_text(filecont)        
        textScreen.textRoot.text_input.cursor=(0,0)
        self.sm.current='textScreen'
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename, self.datapath)
        
    def on_file_open_ex(self,filename):
        self.filename = filename
        fileScreen = self.sm.get_screen('fileScreen')
        #fileScreen.fileRoot.status.text='opening file...'
        if self.is_jpg(filename):
            Clock.schedule_once(self.on_file_open_ex_jpg_1)
            return
        Clock.schedule_once(self.on_file_open_ex_1)

    def on_file_open_ex_jpg_1(self,dt):
        from photo_screen import PhotoScreen
        if self.sm.has_screen('photoScreen'):
            photoScreen = self.sm.get_screen('photoScreen')
            self.sm.remove_widget(photoScreen)
        self.photoScreen = PhotoScreen(name='photoScreen',datapath=EX_PATH,filename=self.filename)
        self.sm.add_widget(self.photoScreen)
        self.sm.current='photoScreen'
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)
        
    def on_file_open_ex_1(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        file_label = textScreen.textRoot.file_label
        file_label.text=self.filename
        filecont=''
        try:
            f=open('%s/%s' % (EX_PATH, self.filename),'rb')
            filecont=f.read()
            f.close()
        except:
            exc = get_exc_details()
            Logger.info('kcf: on_file_open exc:%s' % exc)
            #textScreen.textRoot.text_input.text=filecont            
            textScreen.textRoot.set_text(filecont)
            textScreen.textRoot.text_input.cursor=(0,0)
            self.sm.current='textScreen'
            return
        #textScreen.textRoot.text_input.text=filecont
        textScreen.textRoot.set_text(filecont)        
        textScreen.textRoot.text_input.cursor=(0,0)
        self.sm.current='textScreen'        
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)

        
    def on_file_save(self,filename):
        print('on_file_save %s' % filename)
        textScreen = self.sm.get_screen('textScreen')
        file_label = textScreen.textRoot.file_label
        self.filename = filename
        file_label.text=filename
        try:
            f =open('%s/%s' % (self.datapath,self.filename),'wb')
            filecont= self.sm.get_screen('textScreen').textRoot.text_input.text
            f.write(filecont.encode('utf-8'))
            f.close()
            textScreen.textRoot.status.text='Saved to %s/%s' % (self.datapath,self.filename)
            self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)
        except:
            exc = get_exc_details()
            Logger.info('kcf: on_file_save exc:%s' % exc)
            textScreen.textRoot.status.text='Save to %s/%s failed' % (self.datapath,self.filename)
            self.sm.current='textScreen'
            return
        self.ask_save_test()
        self.sm.current='textScreen'

    def ask_save_test(self):
        button_names=['CANCEL','OK']
        callbacks={}
        callbacks['OK']=self.save_to_test
        self.dlg=MButDialog(title='Also save to test.py',message='Save to test.py?',button_names=button_names,callbacks=callbacks,size_hint=(0.8,0.5))
        self.dlg.open()

    def save_to_test(self,v):
        print('save_to_test')
        textScreen = self.sm.get_screen('textScreen')
        try:
            f =open('%s/%s' % (DATA_PATH,'test.py'),'wb')
            filecont= self.sm.get_screen('textScreen').textRoot.text_input.text
            f.write(filecont)
            f.close()
            textScreen.textRoot.status.text='Saved to %s/test.py' % (self.datapath)
        except:
            exc = get_exc_details()
            Logger.info('kcf: save_to_test exc:%s' % exc)
            textScreen.textRoot.status.text='Save to test.py failed'
            self.sm.current='textScreen'
            self.dlg.dismiss()
            return
        self.sm.current='textScreen'
        self.dlg.dismiss()
        self.title='%s [%s] [%s]'  % (APP_NAME,self.filename,self.datapath)
                
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
            #self.cp_examples()
            return True        
        Logger.info('kcf: makdirs fail')
        return False

    def sys_exit(self):
        import sys
        sys.exit()

    def get_settings(self):
        self.settings={
            'ip': '192.168.4.1',
            'STA_ESSID':'TPLINK',
            'STA_PASSW':'',
            'AP_DEFAULT':'1',
            'AP_PASSW':'12345678',
            'HOST_CODE':'STEM-001',
            'course_code':'S1801',
            'CONN_DEVICE':'uid:-----',
        }
        try:
            f =open('%s/settings.dat' % self.datapath,'r')
            lines = f.readlines()
            for line in lines:
                ss = line.split(':',1)
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

    def on_upload_m(self,cont):
        from radio_dlg import MButDialog
        self.cont=cont
        button_names=[' ','CANCEL','OK']
        callbacks={}
        callbacks['OK']=self.on_upload_m_cont
        callbacks['CANCEL']=self.on_upload_m_can
        self.dlg = MButDialog(title='Upload operation',message='Please select operation',button_names=button_names,callbacks=callbacks,size_hint=(0.5,0.7),radio_names=RADIO_UPLOAD_NAMES)
        self.dlg.open()

    def on_upload_m_cont(self,v):
        print('on_upload_m_cont')
        keys = self.dlg.radios
        for keyx in keys:
            print('%s:%s' % (keyx,self.dlg.radios[keyx].state))
            if self.dlg.radios[keyx].state=='down':
                if keyx=='Upload as test.py':
                    self.upload_test(v)
                elif keyx=='Upload':
                    self.upload_only(v)
                elif keyx=='Upload binary':
                    self.on_upload_binary(v)
                    #msg='Upload binary not implemented'
                    #self.textScreen.textRoot.status.text=msg
                    #print(msg)
                else:
                    msg='%s not implemented' % keyx
                    self.textScreen.textRoot.status.text=msg
                    print(msg)                    
                    #self.on_upload(self.cont)
                break
        self.dlg.dismiss()

    def on_upload_binary(self,v):
        #fpath ='%s/%s' % (self.datapath,self.filename)
        Logger.info('kcf:on_upload_binary')
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        status.text='upload as base64 to %s' % self.settings['ip']
        Clock.schedule_once(self.upload_binary)
        

    def upload_binary(self,v):
        self.dlg.dismiss()
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        f=open('%s/%s' % (self.datapath,self.filename),'rb')        
        contx = f.read()
        #Logger.info('kcf: cont:%s' % `self.cont`)
        f.close()
        b64c = binascii.b2a_base64(contx)
        b64_cont,b64c=b64c[:76],b64c[76:]
        while len(b64c)>76:
            xstr, b64c=b64c[:76],b64c[76:]
            b64_cont+= '\n'+xstr
        b64_cont+= '\n'+b64c
        
        #f=open('test.jpg.b64','wb')
        #f.write(b64_cont)
        #f.close()
        
        cont = '\x02\nsvfile:%s\n' % str(self.filename+'.b64')
        cont += b64_cont
        cont +='\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])
        self.wait_resp(status)        

        
    def on_upload_m_can(self,v):
        self.dlg.dismiss()        
        
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

    def on_devinfo(self,v):
        print('on_devinfo')
        screen_name = self.sm.current
        screen = self.sm.get_screen(screen_name)
        status =None
        if screen_name=='textScreen':
            status = screen.textRoot.status
        elif screen_name=='settingsScreen':
            status = screen.settingsRoot.status
        if status:
            status.text='Send ginfo to %s' % self.settings['ip']
            Clock.schedule_once(self.ginfo)

    def ginfo(self,dt):
        textScreen = self.sm.get_screen('textScreen')
        status = textScreen.textRoot.status
        cont = '\x02\nginfo\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])
        self.wait_resp(status, 5)
        
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
        #cont = '\x02\nhost:%s\n\x03\n' % self.settings['HOST_CODE']
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
        f=open('%s/%s' % (self.datapath,self.filename),'rb')
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
        if self.settings['ip']!='192.168.4.1':
            status.text='Not AP, Sending wifi config to %s rejected' % self.settings['ip']
            return
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
