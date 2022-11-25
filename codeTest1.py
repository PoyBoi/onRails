from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang.builder import Builder

from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

Builder.load_string('''
<myLayout>:
    anchor_x:'center'
    anchor_y:'top'
    # GridLayout:
    #   cols: 2
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 50
        Button:
            text: 'aaaaa'
            color: [0, 0, 0, 1]
            # background_color: app.color
            on_press: 
        RoundedButton:
            text: 'bbbb'
            color: [0, 0, 0, 1]
            pos_hint: {'center_x': 0.5}
            size_hint: (1, .3)
            # background_color: (48/255, 84/255, 150/255, 1)
            # background_normal: ''
            on_press: 

<RoundedButton@Button>
    background_color: (0, 0, 0, 0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (48/255, 84/255, 150/255, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [58]
 ''')

 
class myLayout(AnchorLayout):
    pass

class deployMain(App):
    color = [10, 7, 5, 90]
    def build(self):
        return myLayout()

deployMain().run()