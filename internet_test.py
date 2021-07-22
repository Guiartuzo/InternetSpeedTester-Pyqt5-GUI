import time
import results_plotter
from datetime import datetime

class InternetTest:

    headers = ['time']
    data = []
    results = results_plotter.Writer()

    def Test(self, download, ping, upload, frequency):
    
        while True:

            if download == False and upload == False and ping == False:
                break

            current_time = datetime.now()
            current_time = time.strftime("%H:%M %d-%m-%y")
            self.data.append(current_time)

            from speedtest import Speedtest
            st = Speedtest()

            if download:  
                self.headers.append("download")
                self.data.append(st.download()/1000000)
    
            if upload: 
                self.headers.append("upload")
                self.data.append(st.upload()/1000000)

            if ping:  
                self.headers.append("ping")
                servernames =[]  
                st.get_servers(servernames)
                self.data.append(st.results.ping)  

            self.results.WriteFile(self.headers,self.data)
            self.data = []
            time.sleep(int(frequency)*60)