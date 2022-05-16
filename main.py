import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import smtplib
from kivy.uix.floatlayout import FloatLayout


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('prempatel2445@gmail.com', 'kpmcujdjxvdhdihj')
    # server.login('prempatel2445@gmail.com', 'prempatel22!')
    server.sendmail('prempatel2445@gmail.com', to, content)
    server.close()

class MyGrid(Widget):
    email = ObjectProperty(None)
    context = ObjectProperty(None)
    def btn(self):
        try:
            to  = self.email.text
            content = self.context.text
            sendEmail(to, content)
            print("Sended The Mail to", to)
            self.email.text= ""
            self.context.text= ""
            s_pop()
        except Exception as e:
                print(e)
                return Myapp()


class Myapp(App):
     def build(self):
        return MyGrid()

class p(FloatLayout):
    pass
def s_pop():
    show = p()

    popWindow = Popup(title="Mail Respond", content=show, size_hint=(None,None), size=(400,400))
    popWindow.open()

if __name__ == '__main__':
     Myapp().run()
