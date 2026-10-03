from kivy.app import App
from kivy.uix.label import Label

class AdemSadikiApp(App):
    def build(self):
        return Label(text='Welcome to Adem Sadiki App!', font_size=32)

if __name__ == '__main__':
    AdemSadikiApp().run()
