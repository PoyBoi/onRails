from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder 
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

from kivy.core.window import Window

Window.clearcolor = (238/255, 238/255, 238/255, 1)
#if incorrect password then show pop up that password is incorrect

Builder.load_string('''
<myLayout>:
    username_text_input: user_name
    password_text_input: pass_word
    anchor_x:'center'
    anchor_y:'top'
    # GridLayout:
    #   cols: 2
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 30
        RoundedLabel:
            text: 'Enter Your Username'
            color: [0, 0, 0, 1]
            pos_hint: {'center_x': 0.5}
            size: 200, 50
            size_hint: None, None
            # background_color: app.color
            on_press: 
        RoundedText:
            id: user_name
            hint_text:'Enter Your Username'
            pos_hint: {'center_x': 0.5}
            size: 300, 30
            size_hint: None, None
            halign: 'center'
            multiline: False
            max_length: 5
        RoundedLabel:
            text: 'Enter Your Password'
            color: [0, 0, 0, 1]
            pos_hint: {'center_x': 0.5}
            size: 200, 50
            size_hint: None, None
            # background_color: app.color
            on_press: 
        RoundedText:
            id: pass_word
            hint_text:'Enter Your Password'
            pos_hint: {'center_x': 0.5}
            size: 300, 30
            size_hint: None, None
            halign: 'center'
            multiline: False
        RoundedButton:
            text: 'Login'
            color: [0, 0, 0, 1]
            pos_hint: {'center_x': 0.5}
            size: (70, 40)
            size_hint: None, None
            # background_color: (189/255, 195/255, 199/255, 1)
            # background_normal: ''
            on_press: root.findName()
        Widget:

<RoundedLabel@Button>
    background_color: (0, 0, 0, 0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (218/255, 223/255, 225/255, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [28]

<RoundedText@TextInput>
    background_color: (218/255, 223/255, 225/255, 1)
    background_normal: ''
    # canvas.before:
    #     Color:
    #         #rgba: (0, 0, 0, 1)
    #     RoundedRectangle:
    #         size: self.size
    #         pos: self.pos
    #         radius: [28]

<RoundedButton@Button>
    background_color: (0, 0, 0, 0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: (189/255, 195/255, 199/255, 1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [18]
 ''')


class myLayout(AnchorLayout):
    username_text_input = ObjectProperty()
    password_text_input = ObjectProperty()
    un = StringProperty('')
    ps = StringProperty('')
    def findName(self):
        self.un = self.username_text_input.text
        self.ps = self.password_text_input.text
        print(self.ps, self.un)
        popup = Popup(title='Error', content=Label(text='Incorrect Username and/or Password; Please try again.'), size_hint=(None, None), size=(500, 100))
        if self.ps == self.un:    
            popup.open()

class deployMain(App):
    color = [10, 7, 5, 90]
    def build(self):
        return myLayout()

deployMain().run()