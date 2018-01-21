# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.uix.label import Label
from font_path import FONT_PATH
import string

APP_OPERATIONS={
    'Save': 'on_settings_ok',
    'Ping': 'on_ping',
    'Upload wifi config': 'on_upload_wifi_config',
    'Rst' : 'on_reset',
    'Back': 'on_settings_cancel',
}


OPERATION_BUTTONS =['Save','Ping','Upload wifi config','Rst','Back']

SETTINGS_TITLE={
    'ip':'Device IP',
    'wifi_config':'WIFI Configuration',
    'STA_ESSID': 'WIFI Station ESSID',
    'STA_PASSW': 'WIFI Station password',
    'AP_DEFAULT': 'AP Default',
    'AP_PASSW': 'AP password',
    }

SETTINGS_ORDER=['ip','wifi_config','STA_ESSID','STA_PASSW','AP_DEFAULT','AP_PASSW']

class SettingsRoot(BoxLayout):
    
    def __init__(self,**kwargs):
        self.settings = kwargs['settings']
        kwargs['orientation']='vertical'
        self.app_operations = kwargs.get('app_operations',APP_OPERATIONS)
        self.operation_buttons=kwargs.get('operation_buttons',OPERATION_BUTTONS)
        super(SettingsRoot, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.layout0 = BoxLayout(orientation='vertical',size_hint_y=0.8)
        layouts={}
        tinputs={}
        for key in SETTINGS_ORDER:
            if key=='wifi_config':
                layouts[key]=BoxLayout(orientation='horizontal',size_hint_y=0.1
)
                lb =Button(text=SETTINGS_TITLE[key],disabled=True)
                layouts[key].add_widget(lb)
            else:
                layouts[key]=BoxLayout(orientation='horizontal',size_hint_y=0.2)
                if key=='STA_PASSW':
                    self.show_pwd_btn = ToggleButton(text=SETTINGS_TITLE[key])
                    self.show_pwd_btn.bind(on_press=self.on_show_pwd)
                    layouts[key].add_widget(self.show_pwd_btn)
                elif key=='AP_PASSW':
                    self.show_ap_pwd_btn = ToggleButton(text=SETTINGS_TITLE[key])
                    self.show_ap_pwd_btn.bind(on_press=self.on_show_ap_pwd)
                    layouts[key].add_widget(self.show_ap_pwd_btn)                    
                else:
                    lb = Label(text=SETTINGS_TITLE[key])
                    layouts[key].add_widget(lb)
                if key=='STA_PASSW'  or key=='AP_PASSW':
                    tinputs[key] = TextInput(text=self.settings[key], font_name=FONT_PATH, password=True)
                else:
                    tinputs[key] = TextInput(text=self.settings[key], font_name=FONT_PATH)
                    
                layouts[key].add_widget(tinputs[key])
            self.layout0.add_widget(layouts[key])

        self.layouts=layouts
        self.tinputs=tinputs
        
        label2 = Label(text='')
        self.layout0.add_widget(label2)        
        self.add_widget(self.layout0)

        self.layout1 = BoxLayout(orientation='vertical',size_hint_y=0.1)
        self.status = TextInput(text='',disabled=True)
        self.status.text=''
        self.layout1.add_widget(self.status)
        self.add_widget(self.layout1)
        self.btns_layout = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        for btn_name in self.operation_buttons:
            btn = Button(text=btn_name)
            btn.bind(on_press=self.on_op)
            self.btns_layout.add_widget(btn)
        self.add_widget(self.btns_layout)

    def on_show_pwd(self,v):
        if v.state=='down':
            self.tinputs['STA_PASSW'].password=False
        else:
            self.tinputs['STA_PASSW'].password=True

    def on_show_ap_pwd(self,v):
        if v.state=='down':
            self.tinputs['AP_PASSW'].password=False
        else:
            self.tinputs['AP_PASSW'].password=True            
            
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

    def on_settings_ok(self,v):
        text=''
        for key in SETTINGS_ORDER:
            if key=='wifi_config':
                continue
            vx = self.tinputs[key].text
            text+='%s:%s\n' % (key,vx)
            self.settings[key]=string.strip(vx)
        Logger.info('kcf: on_settings_ok settings:%s' % `self.settings`)
        cont ="STA_ESSID='%s'\nSTA_PASSW='%s'\nAP_DEFAULT=%s\nAP_PASSW='%s'\n" % (self.settings['STA_ESSID'],self.settings['STA_PASSW'],self.settings['AP_DEFAULT'], self.settings['AP_PASSW'])
        f=open('wifi_config.py','wb')
        f.write(cont)
        f.close()
        self.app.on_settings_ok(self.settings, text)
            
    def refresh(self):
        self.status.text=''

    def on_upload_wifi_config(self,v):
        self.on_settings_ok(v)
        self.app.on_upload_wifi_config(v)
        
class SettingsScreen(Screen):
    def __init__(self,**kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.settingsRoot= SettingsRoot(**kwargs)
        self.add_widget(self.settingsRoot)

    def on_pre_enter(self):
        print 'TextScreen on_pre_enter'
        self.settingsRoot.refresh()
        
if __name__=='__main__':
    class TestApp(App):
        def build(self):
            self.settings={
                'ip':'ip',
                'STA_ESSID': 'sta_essid',
                'STA_PASSW': 'sta_pass',
                }
            self.settingsScreen = SettingsScreen(name='settingsScreen',app_operations=APP_OPERATIONS,operation_buttons=OPERATION_BUTTONS,settings=self.settings)
            screenManager = ScreenManager(transition=FadeTransition())
            screenManager.add_widget(self.settingsScreen)
            return screenManager
        def on_new(self,v):
            Logger.info('kcf:app:on_new')

        def on_settings_ok(self,settings,text):
            print 'on_settings_ok'
            print 'settings:',`settings`

            print 'text:', `text`
        def on_upload_wifi_config(self,v):
            print 'on_upload_wifi_config'
            
    TestApp().run()            
