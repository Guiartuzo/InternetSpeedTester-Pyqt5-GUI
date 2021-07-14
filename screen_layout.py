import threading
from kivy.uix.screenmanager import Screen
from internet_test import InternetTest
from multiprocessing import Process

class MainScreen(Screen):

    Internet = InternetTest()
    DownloadTest = False
    PingTest = False
    UploadTest = False
    
    def BtnStart(self):
        p = Process(target= self.Internet.Test, args=(self.DownloadTest, self.PingTest, self.UploadTest, self.ids.frequency.text))
        p.start()

    def BtnStop(self):
        print("Finalizando teste")
