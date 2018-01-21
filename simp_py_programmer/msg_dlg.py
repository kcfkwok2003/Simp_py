from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.lang.builder import Builder


MSG_DLG_KV='''
<MsgDialog>:
    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "vertical"
        Label:
            text: root.text

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "OK"
                on_release: root.cancel()    

'''

class MsgDialog(FloatLayout):
    cancel = ObjectProperty(None)
    text =  ObjectProperty(None)
    
if __name__=='__main__':
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.logger import Logger
    from kivy.uix.popup import Popup
    from kivy.base import EventLoop

    Builder.load_string(MSG_DLG_KV)    
    Factory.register('MsgDialog',cls=MsgDialog)

    class TestApp(App):
        def build(self):
            content = MsgDialog(cancel=self.dismiss_popup, text='testing')
            self._popup = Popup(title="Message", content=content,
                                size_hint=(0.9, 0.9))
            self._popup.open()
            return self._popup  #Label(text='Testing')

        def dismiss_popup(self):
            self._popup.dismiss()


        def hook_keyboard(self,window,key,*largs):
            if key==27:
                # return True for stopping the propagation
                return True    

    TestApp().run()            
