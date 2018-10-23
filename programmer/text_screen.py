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
from kivy.properties import ObjectProperty

class TextRoot(BoxLayout):
    def __init__(self, **kwargs):
        kwargs['orientation']='vertical'
        self.app_operations = kwargs.get('app_operations',{})
        self.operation_buttons=kwargs.get('operation_buttons',[])
        super(TextRoot, self).__init__(**kwargs)
        self.app = App.get_running_app()
        #self.scrollv = ScrollView()
        #self.blayout=BoxLayout()
        self.text_input = TextInput(text='', font_name=FONT_PATH) #, readonly=True)
        self.text_input.bind(focus=self.on_focus)
        self.text_input.bind(on_double_tap=self.on_double_tap)
        #self.blayout.add_widget(self.text_input)
        #self.blayout.bind(minimum_height=self.blayout.setter('height'))
        #self.scrollv.add_widget(self.text_input)
        self.add_widget(self.text_input)
        #self.scrollv.bind(on_scroll_start=self.on_scroll_start)
        #self.scrollv.bind(on_scroll_move=self.on_scroll_move)
        #self.scrollv.bind(on_scroll_stop=self.on_scroll_stop)

        self.slayout=  BoxLayout(orientation='horizontal',size_hint_y=0.1)
        self.status = TextInput(text='', disabled=True)
        self.slayout.add_widget(self.status)
        self.add_widget(self.slayout)
        self.btns_layout = BoxLayout(orientation='horizontal',size_hint_y=0.1)
        self.file_label = Label(text=self.app.filename,size_hint_x=2)
        #self.btns_layout.add_widget(self.file_label)
        for btn_name in self.operation_buttons:
            btn = Button(text=btn_name)
            btn.bind(on_press=self.on_op)
            self.btns_layout.add_widget(btn)
        self.add_widget(self.btns_layout)

    def on_double_tap(self,v):
        Logger.info('kcf: on_double_tag')
        self.status.text='Line:%s' % (self.text_input.cursor[1] + 1)

    def on_focus(self,v1,v2):
        Logger.info('kcf: on_focus')
        
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

    def on_run(self,v):
        self.app.kv_text=self.kv_text
        self.app_on_op(v)

    def on_upload(self,v):
        self.app.on_upload(self.text_input.text)
        
    def refresh(self):
        self.status.text=''
        #self.text_input.text= self.app.kv_text
        
class TextScreen(Screen):
    def __init__(self,**kwargs):
        super(TextScreen, self).__init__(**kwargs)
        self.textRoot= TextRoot(**kwargs)
        self.add_widget(self.textRoot)

    def on_pre_enter(self):
        print 'TextScreen on_pre_enter'
        self.textRoot.refresh()
        
if __name__=='__main__':
    class TestApp(App):
        def build(self):
            self.kv_text= kv_text_for_test
            self.kv_text+='\n%s\n' % FONT_PATH
            self.textScreen = TextScreen(name='textScreen',app_operations=APP_OPERATIONS,operation_buttons=OPERATION_BUTTONS)
            screenManager = ScreenManager(transition=FadeTransition())
            screenManager.add_widget(self.textScreen)
            return screenManager
        def on_new(self,v):
            Logger.info('kcf:app:on_new')
    TestApp().run()        
