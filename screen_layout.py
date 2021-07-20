from kivy.uix.screenmanager import Screen
from internet_test import InternetTest
from multiprocessing import Process

class MainScreen(Screen):

    Internet = InternetTest()
    DownloadTest = False
    PingTest = False
    UploadTest = False
    p = Process()
    
    def BtnStart(self):
        self.p = Process(target= self.Internet.Test, args=(self.DownloadTest, self.PingTest, self.UploadTest, self.ids.frequency.text))
        self.p.start()

    def BtnStop(self):
        if self.p.is_alive:
            self.p.terminate()