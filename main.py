import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder


class MyGrid(Widget):
     pass

class Myapp(App):
     def build(self):
        return MyGrid()
if __name__ == '__main__':
     Myapp().run()