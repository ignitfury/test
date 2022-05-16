import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    equ = ObjectProperty(None)
    def sum(self):
        cal = self.equ.text
        if cal:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.equ.text = str(eval(cal))
            except Exception:
                self.equ.text = "Error"

class Myapp(App):
     def build(self):
        return MyGrid()
if __name__ == '__main__':
     Myapp().run()
