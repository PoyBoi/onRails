from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class myLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout, self).__init__(**kwargs)
        # self.layout = BoxLayout(anchor_x='center', anchor_y='center')
        self.add_widget(btn = Button(text = "Name: "))
        layout.add_widget(btn)

class myApp(App): 
    def build(self):
        # return myLayout()
        return myLayout()

myApp().run()