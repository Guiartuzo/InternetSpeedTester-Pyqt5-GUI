import time
import results_plotter
from datetime import datetime
import speedtest

class InternetTest:
    
    st = speedtest.Speedtest()

    headers = ['time']
    data = []
    results = results_plotter.Writer()

    def Test(self, download, ping, upload, frequency):
        
        print("iniciando tester...")
        print(download)
        print(ping)
        print(upload)
        print(frequency)

        while True:

            if download == False and upload == False and ping == False:
                break

            current_time = datetime.now()
            current_time = time.strftime("%H:%M %d-%m-%y")
            self.data.append(current_time)


            if download:  
                self.headers.append("download")
                self.data.append(self.st.download()/1000000)
    
            if upload: 
                self.headers.append("upload")
                self.data.append(self.st.upload()/1000000)

            if ping:  
                self.headers.append("ping")
                servernames =[]  
                self.st.get_servers(servernames)
                self.data.append(self.st.results.ping)  

            self.results.WriteFile(self.headers,self.data)
            self.data = []
            time.sleep(int(frequency)*60)

if __name__ == "__main__":
    internet = InternetTest()
    internet.Test(True, True, True, "50")
