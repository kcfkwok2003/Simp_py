from kivy.uix.popup import Popup
from kivy.logger import Logger
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button



class MButDialog(Popup):
    def __init__(self,**kw):
        kw['auto_dismiss']=False
        self.title=kw.get('title','Edit')
        self.message=kw.get('message','')
        self.button_names=kw.get('button_names',['ok','cancel'])
        self.callbacks=kw.get('callbacks',{})
        super(self.__class__,self).__init__(**kw)
        self.content=GridLayout(cols=1, padding=(30,30),spacing=(10,10))
        #lb1=Label(text=self.title,size_hint_y=0.1)
        msg =Label(text=self.message,size_hint_y=0.8)
        #self.content.add_widget(lb1)
        self.content.add_widget(msg)
        #ti = TextInput(text='', size_hint_y=0.3)
        #self.content.add_widget(ti)
        #self.ti=ti
        self.ly=BoxLayout(orientation='horizontal',size_hint_y=0.1)
        self.buts={}
        for button_name in self.button_names:
            if button_name.strip()=='':
                self.ly.add_widget(Label(text=' '))
                continue
            cb =self.callbacks.get(button_name, self.ok)
            btn=Button(text=button_name)
            btn.bind(on_release=cb)
            self.ly.add_widget(btn)
                              
        #self.btn_ok=Button(text=self.button_name)
        #self.btn_ok.bind(on_release=self.ok)
        self.content.add_widget(self.ly)
        blank=Label(text=' ',size_hint_y=0.7)
        self.content.add_widget(blank)

    def ok(self,v):
        self.dismiss()
        


if __name__=='__main__':
    from kivy.app import App
    from kivy.uix.widget import Widget
    class Root(Widget):
        def __init__(self,**kw):
            super(Root,self).__init__(**kw)
            button_names=['ok','cancel','abort']
            callbacks={}
            callbacks['ok']=self.ok
            callbacks['cancel']=self.cancel
            callbacks['abort']=self.abort
            dlg =MButDialog(title='Edit header',message='Error',button_names=button_names,callbacks=callbacks)
            dlg.open()

        def ok(self,v):
            print 'ok'

        def cancel(self,v):
            print 'cancel'
                              
        def abort(self,v):
            print 'abort'
            
    class TestApp(App):
        def build(self):
            return Root()
            
    TestApp().run()
