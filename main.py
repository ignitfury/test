from cProfile import label
from pydoc import text
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ygrid(GridLayout):
    def __init__(self, **kwargs):
        super(ygrid, self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter Your Number: "))
        self.numb= TextInput(multiline =False)
        self.inside.add_widget(self.numb)

        # self.inside.add_widget(Label(text="Email: "))
        # self.email = TextInput(multiline =False)
        # self.inside.add_widget(self.email)
        
        # self.inside.add_widget(Label(text="Skill: "))
        # self.skill = TextInput(multiline =False)
        # self.inside.add_widget(self.skill)
        
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press = self.pressed)

        self.add_widget(self.submit)

        
        self.add_widget(self.inside)

    def pressed(self, instance):
        # name = self.name.text
        # email = self.email.text
        # skill= self.skill.text
        numb = str(self.numb.text)
        # print("Name: ", name)
        # print("Email:" , email)
        # print("Skill: ", skill)

        t = eval(numb)
        print(t)
        self.numb.text = ""
        # self.name.text = ""
        # self.email.text = ""
        # self.skill.text = ""

        



class Myapp(App):
    def build(self):
        return ygrid()


if __name__ == '__main__':
    Myapp().run()