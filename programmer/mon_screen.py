# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from font_path import FONT_PATH
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty


APP_OPERATIONS={
    'Start': 'on_mon_start',
    'Stop': 'on_mon_stop',    
    'Up':'on_mon_cursor_up',
    'Dn':'on_mon_cursor_down',
    'Pup': 'on_mon_page_up',
    'Pdn': 'on_mon_page_down',
    'Exit': 'on_mon_exit',
    }

#OPERATION_BUTTONS=['Start','Stop','Up','Dn','Pup','Pdn','Exit']
OPERATION_BUTTONS=['Start','Stop','Clr','Back']


class MonRoot(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['orientation']='vertical'
        self.app_operations = kwargs.get('app_operations',{})
        self.operation_buttons=kwargs.get('operation_buttons',[])
        super(MonRoot, self).__init__(**kwargs)
        self.app = App.get_running_app()
        #self.scrollv = ScrollView()
        #self.blayout=BoxLayout()
        self.text_input = TextInput(text='', font_name=FONT_PATH, readonly=True)
        #self.blayout.add_widget(self.text_input)
        #self.blayout.bind(minimum_height=self.blayout.setter('height'))
        #self.scrollv.add_widget(self.text_input)
        self.add_widget(self.text_input)
        #self.scrollv.bind(on_scroll_start=self.on_scroll_start)
        #self.scrollv.bind(on_scroll_move=self.on_scroll_move)
        #self.scrollv.bind(on_scroll_stop=self.on_scroll_stop)
        self.s0layout=  BoxLayout(orientation='horizontal',size_hint_y=0.1, spacing=(20,20),padding=(3,3))
        self.out_msg= TextInput(text='',size_hint_x=0.8)
        self.s0layout.add_widget(self.out_msg)
        self.snd_btn = Button(text='Send',size_hint_x=0.2)
        self.snd_btn.bind(on_press=self.on_op)
        self.s0layout.add_widget(self.snd_btn)
        self.add_widget(self.s0layout)       
        self.slayout=  BoxLayout(orientation='horizontal',size_hint_y=0.1, padding=(3,3))
        self.status = TextInput(text='', disabled=True,size_hint_x=0.8)
        self.slayout.add_widget(self.status)
        self.user_cbox = CheckBox(size_hint_x=0.1,color=(1,1,1,4))
        self.slayout.add_widget(self.user_cbox)
        self.slayout.add_widget(Label(text='User',size_hint_x=0.1))
        self.add_widget(self.slayout)
        
        self.btns_layout = BoxLayout(orientation='horizontal',size_hint_y=0.1,spacing=(3,3))
        self.mon_label = Label(text='Not connected',size_hint_x=2)
        self.btns_layout.add_widget(self.mon_label)
        self.btns={}
        for btn_name in self.operation_buttons:
            btn = Button(text=btn_name)
            btn.bind(on_press=self.on_op)
            self.btns[btn_name]=btn
            self.btns_layout.add_widget(btn)
        self.add_widget(self.btns_layout)

    def on_scroll_start(self,ev1,ev2):
        Logger.info('kcf: on_scroll_start %s %s' % (ev1,ev2))
        
    def on_scroll_move(self,ev1,ev2):
        Logger.info('kcf: on_scroll_move %s %s' % (ev1,ev2))
        dx = ev2.pos[0] - ev2.spos[0]
        dy = ev2.pos[1] - ev2.spos[1]
        if dy >0:
            self.text_input.do_cursor_movement('cursor_up')
        if dy <0:
            self.text_input.do_cursor_movement('cursor_down')

    def on_scroll_stop(self,ev1,ev2):
        Logger.info('kcf: on_scroll_stop %s %s' % (ev1,ev2))

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
        self.status.text=''
        self.text_input.text=''
        self.out_msg.text=''
        
class MonScreen(Screen):
    def __init__(self,**kwargs):
        super(MonScreen, self).__init__(**kwargs)
        self.monRoot= MonRoot(**kwargs)
        self.add_widget(self.monRoot)

    def on_pre_enter(self):
        print 'monScreen on_pre_enter'
        self.monRoot.refresh()
        
if __name__=='__main__':
    class TestApp(App):
        def build(self):
            self.kv_text='\n%s\n' % FONT_PATH
            self.monScreen = MonScreen(name='monScreen',app_operations=APP_OPERATIONS,operation_buttons=OPERATION_BUTTONS)
            screenManager = ScreenManager(transition=FadeTransition())
            screenManager.add_widget(self.monScreen)
            return screenManager
        def on_new(self,v):
            Logger.info('kcf:app:on_new')
    TestApp().run()        
