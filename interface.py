from screen_layout import MainScreen
import kivy

kivy.require("2.0.0")
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class InterfaceApp(App):

    ScreenManagerObj = ScreenManager()

    def build(self):
        self.ScreenManagerObj.add_widget(MainScreen(name = 'MainScreen'))
        return self.ScreenManagerObj