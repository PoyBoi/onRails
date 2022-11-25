from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang.builder import Builder

Builder.load_string('''
<myLayout>:
    anchor_x:'right'
    anchor_y:'top'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'aaaaa'
        Button:
            text: 'bbbb'
''')

class myLayout(AnchorLayout):
    pass

class deployMain(App):
    def build(self):
        return myLayout()

deployMain().run()