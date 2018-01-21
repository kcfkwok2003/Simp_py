
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang.builder import Builder

kv_text='''
BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'horizontal'
        size_hint_y: 0.1
        Label: 
            text: 'Input text'
        textinput:
            text: ''


'''

root=Builder.load_string(kv_text)




if __name__=='__main__':
    class TestApp(App):
        def build(self):
            return root

    TestApp().run()
