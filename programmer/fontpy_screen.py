# -*- coding: utf-8 -*-
from kivy.base import EventLoop
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from PIL import Image
from kivy.uix.image import Image as UImage
from kivy.graphics import Color,Callback,Rectangle,Line
from kivy.core.text import Label as CoreLabel
import time
import re
import os
import math
from kivy.clock import Clock

RADIO_NAMES=['Save fontx+py(m5stack)',
             'Save fontx+py(wifikit32)',
             'Save fontx              ',
             'Reserve                  ',]

OPERATION_BUTTONS=['PREV','NEXT','PROCESS']
DATA_PATH='/data/simp_py_dat'

APP_OPERATIONS={
    'PROCESS': 'on_fontpy_process',
    'BACK': 'on_file_cancel',
    }
skip='''
from kivy.core.text import LabelBase
KIVY_FONTS = [
    {
        "name": "RobotoCondensed",
        "fn_regular": "data/fonts/RobotoCondensed-Light.ttf",
        "fn_bold": "data/fonts/RobotoCondensed-Regular.ttf",
        "fn_italic": "data/fonts/RobotoCondensed-LightItalic.ttf",
        "fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
    }
]
    
for font in KIVY_FONTS:
    LabelBase.register(**font)
'''
class FontpyRoot(FloatLayout):
    def __init__(self,**kwargs):
        super(FontpyRoot,self).__init__(**kwargs)
        EventLoop.ensure_window()
        Window = EventLoop.window
        with self.canvas.before:
            self.cb=Callback(self.my_callback)
        self.cb.ask_update()
        
        with self.canvas:
            Color(0.9,0.9,0.9)
            self.rect=Rectangle(pos=(0,0), size=(800,600))
            self.text=CoreLabel(text="hello", font_size=20,pos=(0,100))
            self.text.refresh()
            Color(0,0,0,1)
            print("aaa")
            for i in [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500]:
                self.line=Line(points=[0,i,1600,i])
            for i in [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500]:
                self.line=Line(points=[i,0,i,1600])
            Color(0.2,0.2,0,2)
            self.title_rect=Rectangle(pos=(0,500),size=(800,100))
            print("bbb")

    def my_callback(self,instr):
        with self.canvas.before:
            Color(0,5,0.5,0.9,0)
            Rectangle(pos=(0,0),size=(200,200))

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

    def file_cancel(self,v):
        try:
            self.app.on_file_cancel(v)
        except:
            pass
        
    def refresh(self):
        #self.status.text=''
        pass
    
class FontpyRootxx(BoxLayout):
    def __init__(self, **kwargs):
        global DATA_PATH
        kwargs['orientation']='vertical'        
        filename=kwargs.get('filename','')
        datapath = kwargs.get('datapath',DATA_PATH)
        #datapath = kwargs.get('datapath','seve_py_dat')
        self.datapath=datapath
        self.filename=filename
        self.file_settings={'filename':filename, 'datapath':datapath}
        super(FontpyRoot, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app_operations = APP_OPERATIONS
        self.layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.title=Label(text='Photo Operator')
        self.layout.add_widget(self.title)
        self.add_widget(self.layout)
        fpath='%s/%s' % (self.datapath, self.filename)

        self.blayout = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        for btn_name in OPERATION_BUTTONS:
            btn = Button(text=btn_name)
            btn.bind(on_press= self.on_op)
            self.blayout.add_widget(btn)
        self.status = Label(text='')
        self.blayout.add_widget(self.status)
        self.add_widget(self.blayout)


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

    def file_cancel(self,v):
        try:
            self.app.on_file_cancel(v)
        except:
            pass
        
    def refresh(self):
        self.status.text=''        


class FontpyScreen(Screen):
    def __init__(self,**kwargs):
        super(FontpyScreen, self).__init__(**kwargs)
        self.fontpyRoot= FontpyRoot(**kwargs)
        self.add_widget(self.fontpyRoot)

    def on_pre_enter(self):
        print 'fontpyScreen on_pre_enter'
        self.fontpyRoot.refresh()
        

if __name__=='__main__':
    class TestApp(App):
        def build(self):
            #self.kv_text= kv_text_for_test
            #self.kv_text+='\n%s\n' % FONT_PATH
            self.fontpyScreen = FontpyScreen(name='fontpyScreen',data_path=DATA_PATH,filename='20181019_185603.jpg')
            screenManager = ScreenManager(transition=FadeTransition())
            screenManager.add_widget(self.fontpyScreen)
            return screenManager
        
        def on_new(self,v):
            Logger.info('kcf:app:on_new')
    TestApp().run()                
