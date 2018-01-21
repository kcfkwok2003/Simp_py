# -*- coding: utf-8 -*-
# simp_py/simp_py_fonts/main.py
# author: C.F.Kwok (TienLink Creation)
# date: 2018-1-17

VERSION='1.0.0'
YEAR ='2018'
ABOUT_MSG='''
Simp-py-fonts V%s
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
from font_path import FONT_PATH
from ch2dat import conv_lines

from exc import get_exc_details
import string
import time
IN_FONT_PATH='/storage/emulated/0/data/simp_py_fonts'
OUT_PATH='/storage/emulated/0/data/simp_py_dat'
TEXT_PATH='/storage/emulated/0/data/simp_py_dat'
APP_OPERATIONS={
    'Load text':'on_load_text',
    'Convert 24x24': 'on_conv_24',
    'Convert 16x16': 'on_conv_16',
    }

OPERATION_BUTTONS=['Load text','Convert 16x16',] # 'Convert 24x24']

class MainRoot(BoxLayout):
    def __init__(self,**kwargs):
        kwargs['orientation']='vertical'
        self.app_operations = APP_OPERATIONS
        self.operation_buttons= OPERATION_BUTTONS
        super(MainRoot,self).__init__(**kwargs)
        self.app=App.get_running_app()
        self.text_input=TextInput(text='',font_name=FONT_PATH, disabled=True)
        self.add_widget(self.text_input)
        self.elayout=BoxLayout(orientation='horizontal',size_hint_y=0.1)
        lb= Label(text='Text file',size_hint_x=0.3)
        self.elayout.add_widget(lb)
        self.textfilename=TextInput(text='ch_intro.txt')
        self.elayout.add_widget(self.textfilename)
        lb= Label(text='Font file', size_hint_x=0.3)
        self.elayout.add_widget(lb)
        self.fontfilename =TextInput(text='GNUUnifont9FullHintInstrUCSUR.ttf')
        self.elayout.add_widget(self.fontfilename)
        self.add_widget(self.elayout)
        self.slayout=BoxLayout(orientation='horizontal',size_hint_y=0.1)
        self.status =TextInput(text='',disabled=True)
        self.slayout.add_widget(self.status)

        self.add_widget(self.slayout)
        self.btns_layout=BoxLayout(orientation='horizontal',size_hint_y=0.1)
        for btn_name in self.operation_buttons:
            btn=Button(text=btn_name)
            btn.bind(on_press=self.on_op)
            self.btns_layout.add_widget(btn)
        self.add_widget(self.btns_layout)

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
        self.title='Simp-py-fonts'        

        self.mainScreen=MainScreen()
        self.status = self.mainScreen.mainRoot.status
        self.textfilename = self.mainScreen.mainRoot.textfilename
        self.fontfilename = self.mainScreen.mainRoot.fontfilename
        self.text_input =  self.mainScreen.mainRoot.text_input
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

    def on_load_text(self,v):
        try:
            fn =self.mainScreen.mainRoot.textfilename.text
            Logger.info('kcf: on_load_text fn:%s' % fn)
            text_path='%s/%s' % (TEXT_PATH, fn)
            f=open(text_path,'rb')
            txt = f.read()
            f.close()
            self.text_input.text = txt
            self.status.text='file %s loaded' % text_path
        except:
            exc = get_exc_details()
            self.status.text = exc
        
    def on_conv_8(self,v):
        Logger.info('kcf: on_conv_8')

    def get_out_fn(self,fn):
        ss= fn.split('.')
        if ss[-1]=='txt':
            return fn[:-4]+'_font.py'
        return fn+'_font.py'
            
    def on_conv_16(self,v):
        Logger.info('kcf: on_conv_16')
        try:
            fn =self.mainScreen.mainRoot.textfilename.text
            text_path='%s/%s' % (TEXT_PATH, fn)
            f=open(text_path,'rb')
            lines = f.readlines()
            f.close()
            font_path = '%s/%s' % (IN_FONT_PATH, self.fontfilename.text)
            
            out_path = '%s/%s' % (OUT_PATH,self.get_out_fn(fn))
            font_metric=16
            draw_metric=(16,18)

            report=conv_lines(lines, out_path,font_path,font_metric,draw_metric)
            self.status.text=report
        except:
            exc = get_exc_details()
            self.status.text=exc
            
if __name__=='__main__':
    MainApp().run()                        
