# -*- coding: utf-8 -*-
VERSION='1.0.0'
YEAR ='2018'
ABOUT_MSG='''
Simp-py-remote V%s
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
from kivy.uix.label import Label
from dev_com import DEV_COM

from exc import get_exc_details
import string
import time
from kivy.clock import Clock
import os
CHR_STX='\x02'
CHR_ETX='\x03'
CHR_EOT='\x04'

MON_KA_TIMEOUT=10

APP_OPERATIONS={
    'Set': 'on_set',
    'Ping': 'on_ping',
    'Jingle Bell':'on_jingle_bell',
    'Little Lamb': 'on_little_lamb',
    }

OPERATION_BUTTONS=['Set','Ping','Jingle Bell','Little Lamb']
SETTINGS_TITLE={
    'ip': 'Device IP',
    }

SETTINGS_ORDER=['ip']

class MainRoot(BoxLayout):
    def __init__(self,**kwargs):
        kwargs['orientation']='vertical'
        self.app_operations = APP_OPERATIONS
        self.operation_buttons= OPERATION_BUTTONS
        super(MainRoot,self).__init__(**kwargs)
        self.app=App.get_running_app()
        self.settings=self.app.settings
        self.layout0=BoxLayout(orientation='vertical',size_hint_y=0.8)
        layouts={}
        tinputs={}
        for key in SETTINGS_ORDER:
            layouts[key]=BoxLayout(orientation='horizontal',size_hint_y=0.2)
            lb = Label(text=SETTINGS_TITLE[key])
            layouts[key].add_widget(lb)
            tinputs[key] =TextInput(text=self.settings[key])
            layouts[key].add_widget(tinputs[key])
            self.layout0.add_widget(layouts[key])
            
        self.layouts=layouts
        self.tinputs=tinputs
        dummy= Label(text='', size_hint_y=0.8)
        self.layout0.add_widget(dummy)
        self.add_widget(self.layout0)

    
        self.layout1 = BoxLayout(orientation='vertical',size_hint_y=0.1)
        self.status = TextInput(text='', disabled=True)
        self.layout1.add_widget(self.status)
        self.add_widget(self.layout1)        
        self.layoutm = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        self.out_msg = TextInput(text='')
        self.layoutm.add_widget(self.out_msg)
        self.out_msg_btn = Button(text='Send message',size_hint_x=0.2)
        self.out_msg_btn.bind(on_press=self.on_out_msg)
        self.layoutm.add_widget(self.out_msg_btn)
        self.add_widget(self.layoutm)

        self.btns_layout = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        for btn_name in self.operation_buttons:
            btn =Button(text=btn_name)
            btn.bind(on_press=self.on_op)
            self.btns_layout.add_widget(btn)
        self.add_widget(self.btns_layout)

    def on_out_msg(self,v):
        Logger.info('kcf: on_out_msg')
        msg ='%s' %  self.out_msg.text
        self.app.on_out_msg(msg)
        
    def app_on_op(self,v):
        operation = self.app_operations.get(v.text, None)        
        on_op = getattr(self.app, operation, None)
        if callable(on_op):
            on_op(v)
        else:
            Logger.info('kcf:app:%s not implemented' % operation)
            
    def on_op(self,v):
        operation = self.app_operations.get(v.text, None)
        if operation is None:
            Logger.info('kcf:APP_OPERATIONS has no such operation:%s' % v.text)
            return
        on_op = getattr(self, operation,None)
        if on_op is not None:
            on_op(v)
            return
        
        self.app_on_op(v)

    def refresh(self):
        pass
    
class MainScreen(Screen):
    def __init__(self,**kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.mainRoot= MainRoot(**kwargs)
        self.add_widget(self.mainRoot)

    def on_pre_enter(self):
        print 'mainScreen on_pre_enter'
        self.mainRoot.refresh()    
            
        
class MainApp(App):
    def build(self):
        self.title='Simp-py-remote'
        self.settings={
            'ip':'192.168.4.1',
            }
        
        self.dev_com= DEV_COM(self.settings['ip'], self.dev_com_cb)
        self.mainScreen=MainScreen()
        self.status = self.mainScreen.mainRoot.status
        screenManager = ScreenManager(transition=FadeTransition())
        screenManager.add_widget(self.mainScreen)
        return screenManager
        
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

    def dev_com_cb(self,imsg,exc=None):
        Logger.info('kcf: imsg:%s exc:%s' % (imsg,exc))
        if exc is not None:
            try:
                self.status.text=exc
            except:
                self.status.text='Exception'
            return
        lines = imsg.split('\n')
        nlines=[]
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
        if not done:
            return
        if nlines[0]=='resp':
            txt=nlines[1]
            tlines= string.split(self.status.text,'\n')
            if len(tlines)>0:
                txt = tlines[-1]+'\n'+txt
            self.status.text = txt
            return
        if nlines[0]=='uresp':
            txt = nlines[1]
            tlines= string.split(self.status.text,'\n')
            if len(tlines)>0:
                txt = tlines[-1]+'\n'+txt
            self.status.text = txt
            self.dev_com.send('\x04\n')
            time.sleep(0.01)
            self.dev_com.close()
            return
        
    def on_ping(self,v):
        self.status.text='Send ping to %s' % self.settings['ip']
        Clock.schedule_once(self.ping)
        
    def ping(self,dt):
        cont = '\x02\nping\n\x03\n\x04\n'
        self.dev_com.send(cont, self.settings['ip'])


    def on_set(self,v):
        Logger.info('kcf: on_set')
        self.settings['ip']= self.mainScreen.mainRoot.tinputs['ip'].text
        self.status.text= self.settings['ip']

    def on_jingle_bell(self,v):
        msg='jingle bells'
        Logger.info('kcf: on_jingle_bell')
        cont = '\x02\nureq\n%s\n\x03\n' % msg
        self.out_msg(msg,cont)

    def on_out_msg(self,msg):
        cont = '\x02\nureq\n%s\n\x03\n' % msg
        self.out_msg(msg,cont)
        
    def out_msg(self,msg,cont):
        self.status.text='Send out msg:%s' % msg
        self.dev_com.send(cont, self.settings['ip'])
                          
    def on_little_lamb(self,v):
        msg='little lamb'
        Logger.info('kcf: on_little_lamb')
        cont = '\x02\nureq\n%s\n\x03\n' % msg
        self.out_msg(msg,cont)
        
if __name__=='__main__':
    MainApp().run()                
