from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 


class Autoriz(Screen):
    #def __init__(self, **kwargs):
     #   super().__init__(**kwargs)
      #  line = BoxLayout(orientation="vertical", size_hint = (0.5, 0.5), pos_hint={"center_x":0.5, "center_y":0.5})
       # txt1 = Label(text="Your name:")
        #line.add_widget(txt1)
    #    self.name1 = TextInput(text="Enter your name", multiline=False)
     #   line.add_widget(self.name1)

      #  txt2 = Label(text="Your password:")
       # line.add_widget(txt2)
        #self.password1 = TextInput(text="Enter your password", multiline=False)
    #    line.add_widget(self.password1)

        #self.buttonOK = Button(text="Login")
       # line.add_widget(self.buttonOK)

        #self.add_widget(line)
        ...

class Main(Screen):
    ...

class LogikaPCApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Autoriz(name="autoriz"))
        sm.add_widget(Main(name="main"))
        return sm

Window.size = (400, 600) 

LogikaPCApp().run()