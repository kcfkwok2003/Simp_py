# -*- coding: utf-8 -*-

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

import time
import re
import os
import math
from kivy.clock import Clock
APP_NAME='Simp-py'

RADIO_NAMES=['Scaled and save jpg+py',
             'Scale and save jpg    ',
             'Reserve               ',
             ]

OPERATION_BUTTONS=['PROCESS','BACK']
DATA_PATH='/data/simp_py_dat'

APP_OPERATIONS={
    'PROCESS': 'on_photo_process',
    'BACK': 'on_file_cancel',
    }
class PhotoRoot(BoxLayout):
    def __init__(self, **kwargs):
        global DATA_PATH
        kwargs['orientation']='vertical'        
        filename=kwargs.get('filename','')
        datapath = kwargs.get('datapath',DATA_PATH)
        self.datapath=datapath
        self.filename=filename
        self.file_settings={'filename':filename, 'datapath':datapath}
        super(PhotoRoot, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app_operations = APP_OPERATIONS
        self.layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.title=Label(text='Photo Operator')
        self.layout.add_widget(self.title)
        self.add_widget(self.layout)
        fpath='%s/%s' % (self.datapath, self.filename)
        imgx=Image.open(fpath)
        imgx1 =imgx.resize((320,240))
        imgx1.save('_%s' % self.filename)
        self.imgx1 = imgx1
        self.img = UImage(source='_%s' % self.filename)

        print('img:%s' % self.img)
        self.add_widget(self.img)
        self.blayout = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        for btn_name in OPERATION_BUTTONS:
            btn = Button(text=btn_name)
            btn.bind(on_press= self.on_op)
            self.blayout.add_widget(btn)
        self.status = Label(text='')
        self.blayout.add_widget(self.status)
        self.add_widget(self.blayout)


    def on_photo_process(self,v):
        print('on_photo_process')
        self.status.text=''
        from radio_dlg import MButDialog
        button_names =['OK']
        callbacks={}
        callbacks['OK']= self.on_photo_process_op
        self.dlg = MButDialog(title='Photo operation',message='Please select operation',button_names=button_names,callbacks=callbacks,size_hint=(0.5,0.7),radio_names=RADIO_NAMES)
        self.dlg.open()
        

    def on_photo_process_op(self,v):
        print('on_photo_process_op')
        keys = self.dlg.radios
        for keyx in keys:
            print('%s:%s' % (keyx,self.dlg.radios[keyx].state)) 
            if self.dlg.radios[keyx].state=='down':
                self.on_photo_op(keyx)
                break            
        self.dlg.dismiss()

    def on_photo_op(self,keyx):
        print('on_photo_op %s' % keyx)
        if keyx=='Scaled and save jpg+py':
            self.save_jpg_and_py()
        elif keyx=='Scale and save jpg':
            self.save_jpg()

    def save_jpg_and_py(self):
        self.datapath = DATA_PATH
        fn = self.filename
        if not fn.endswith('_scaled.jpg'):
            fn =self.filename.replace('.jpg','_scaled.jpg')
        fpath='%s/%s' % (self.datapath,fn)
        print('save_jpg_and_py %s' % fpath)
        self.imgx1.save(fpath)
        fn_py='test_' + fn + '.py'
        f=open('%s/%s' % (self.datapath,fn_py),'wb')
        f.write("from simp_py import lcd\nlcd.image(0,0,'%s')\n" % fn)
        f.close()
        print('save_jpg_and_py done')        
        self.status.text ='jpg + py saved'
        self.app.filename=fn
        self.app.datapath=DATA_PATH
        self.app.title='%s [%s] [%s]'  % (APP_NAME,self.app.filename,self.datapath)        
        
    def save_jpg(self):
        self.datapath= DATA_PATH
        fn = self.filename
        if not fn.endswith('_scaled.jpg'):        
            fn =self.filename.replace('.jpg','_scaled.jpg')
        fpath='%s/%s' % (self.datapath,fn)
        self.imgx1.save(fpath)
        self.status.text ='jpg saved' # %s' % fpath
        self.app.filename=fn
        self.app.datapath = DATA_PATH
        self.app.title='%s [%s] [%s]'  % (APP_NAME,self.app.filename,self.datapath)
        
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
        #self.content.clear_widgets()

        
class PhotoScreen(Screen):
    def __init__(self,**kwargs):
        super(PhotoScreen, self).__init__(**kwargs)
        self.photoRoot= PhotoRoot(**kwargs)
        self.add_widget(self.photoRoot)

    def on_pre_enter(self):
        print 'photoScreen on_pre_enter'
        self.photoRoot.refresh()
        

if __name__=='__main__':
    class TestApp(App):
        def build(self):
            self.photoScreen = PhotoScreen(name='photoScreen',data_path=DATA_PATH,filename='20181019_185603.jpg')
            screenManager = ScreenManager(transition=FadeTransition())
            screenManager.add_widget(self.photoScreen)
            return screenManager
        
        def on_new(self,v):
            Logger.info('kcf:app:on_new')
    TestApp().run()        
