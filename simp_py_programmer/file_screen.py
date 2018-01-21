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
import time
import re
import os
import math

r_file_no=r'test(\d+).py'
re_file_no=re.compile(r_file_no)

APP_OPERATIONS={
    'New': 'on_file_new',
    'Open': 'on_file_open',
    'Save': 'on_file_save',
    'Prev': 'on_file_prev',
    'Next': 'on_file_next',
    'Cancel':'on_file_cancel',
    }

OPERATION_BUTTONS=['New','Open','Save','Prev','Next','Cancel']
DATA_PATH ='/storage/emulated/0/data/simp_py_dat'

class FileRoot(BoxLayout):
    def __init__(self, **kwargs):
        global DATA_PATH
        kwargs['orientation']='vertical'
        filename=kwargs.get('filename','')
        datapath = kwargs.get('datapath',DATA_PATH)
        #datapath = kwargs.get('datapath','seve_py_dat')
        self.datapath=datapath
        self.nrec_per_page=20
        self.page=1
        self.file_settings={'filename':filename, 'datapath':datapath}
        super(FileRoot, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.app_operations = APP_OPERATIONS
        self.layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        self.title=Label(text='File Operation', size_hint_x=0.9)
        self.layout.add_widget(self.title)
        self.p_page = Label(text='P', size_hint_x=0.1)
        self.layout.add_widget(self.p_page)
        self.add_widget(self.layout)
        self.content = GridLayout(cols=2,size_hint_y=0.8)
        self.show_file_list()
        self.add_widget(self.content)
        self.layout1 = BoxLayout(orientation='vertical', size_hint_y=0.1)
        self.ti = TextInput(text=filename)
        self.layout1.add_widget(self.ti)
        self.add_widget(self.layout1)
        self.blayout = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        for btn_name in OPERATION_BUTTONS:
            btn = Button(text=btn_name)
            btn.bind(on_press= self.on_op)
            self.blayout.add_widget(btn)
        self.add_widget(self.blayout)


    def on_filename(self,v):
        Logger.info('kcf: on_filename :%s' % v.text)
        self.ti.text = v.text
        
    def ret_data_page(self,records,nrec_per_page,page):
        data_len = len(records)
        start = (page-1) * nrec_per_page
        npages = int(math.ceil(float(data_len) / nrec_per_page))
        r_end = start + nrec_per_page
        r_end = min(r_end, data_len)
        return start, records[start:r_end],npages
    
    def get_files(self,page):
        fxs = os.listdir(self.datapath)
        fs=[]
        for fn in fxs:
            if fn[-3:]=='.py' or fn[-4:]=='.txt':
                fs.append(fn)
        fs.sort()
        return self.ret_data_page(fs, self.nrec_per_page,page)

    def get_files_len(self):
        fxs = os.listdir(self.datapath)
        fs=[]
        for fn in fxs:
            if fn[-3:]=='.py':
                fs.append(fn)
        return len(fs)

    def get_next_page_n(self, data_len, nrec_per_page, page):
        r_end = page * nrec_per_page
        if data_len > r_end:
            return page +1
        return page
    
    def show_file_list(self,  page=1):
        start, recs, npages = self.get_files(page)
        self.page = page
        self.npages=npages
        self.p_page.text = 'P%s/%s' % (page,npages)
        i= 1
        j= (page -1) * self.nrec_per_page +i
        for fn in recs:
            btn= Button(text='%d' % j, size_hint_x=0.1)
            self.content.add_widget(btn)
            btn = Button(text=fn, size_hint_x=0.9)
            btn.bind(on_press=self.on_filename)
            self.content.add_widget(btn)
            i+=1
            j+=1
        while i< self.nrec_per_page:
            btn = Button(text='', size_hint_x=0.1)
            self.content.add_widget(btn)
            btn = Button(text='', size_hint_x=0.9)
            self.content.add_widget(btn)            
            i+=1
        
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

    def on_file_next(self,v):
        Logger.info('kcf: on_file_next')
        all_end = self.get_files_len()
        page = self.get_next_page_n(all_end, self.nrec_per_page, self.page)
        if page > self.page:
            self.content.clear_widgets()
            self.show_file_list(page=page)

            
    def on_file_prev(self,v):
        Logger.info('kcf: on_file_prev')
        if self.page > 1:
            self.content.clear_widgets()
            self.show_file_list(page=self.page-1)
            
    def on_file_new(self,v):
        fnos=[]
        fs = os.listdir(self.file_settings['datapath'])
        for fx in fs:
            m = re_file_no.match(fx)
            if m is not None:
                nox,= m.groups()
                fnos.append(int(nox))
        nx=1
        if fnos:
            nx = max(fnos)+1
        filename='test%d.py' % nx
        Logger.info('kcf:file_new %s' % filename)
        self.ti.text=filename
        self.file_settings['filename']= filename
        self.file_settings['op']='new'
        self.app.on_file_new(filename)

    def on_file_save(self,v):
        self.app.on_file_save(self.ti.text)

    def on_file_open(self,v):
        self.app.on_file_open(self.ti.text)

        
    def file_open(self,v):
        filename = self.ti.text
        self.file_settings['filename']=filename
        self.file_settings['op']='open'
        Logger.info('kcf:file_open %s' % filename)
        if self.screenManager is not None:
            self.screenManager.current=self.app.back    

    def file_change(self,v):
        filename = self.ti.text
        Logger.info('kcf:file_change %s' % filename)
        self.file_settings['filename']=filename
        self.file_settings['op']='change'
        if self.screenManager is not None:
            self.screenManager.current=self.app.back
            
    def file_cancel(self,v):
        try:
            self.app.on_file_cancel(v)
        except:
            pass

    def refresh(self):
        self.content.clear_widgets()
        self.show_file_list()
        
class FileScreen(Screen):
    def __init__(self,**kwargs):
        super(FileScreen, self).__init__(**kwargs)
        self.fileRoot= FileRoot(**kwargs)
        self.add_widget(self.fileRoot)

    def on_pre_enter(self):
        print 'fileScreen on_pre_enter'
        self.fileRoot.refresh()
        
if __name__=='__main__':
    class TestApp(App):
        def build(self):
            #self.kv_text= kv_text_for_test
            #self.kv_text+='\n%s\n' % FONT_PATH
            self.fileScreen = FileScreen(name='fileScreen')
            screenManager = ScreenManager(transition=FadeTransition())
            screenManager.add_widget(self.fileScreen)
            return screenManager
        
        def on_new(self,v):
            Logger.info('kcf:app:on_new')
    TestApp().run()        




