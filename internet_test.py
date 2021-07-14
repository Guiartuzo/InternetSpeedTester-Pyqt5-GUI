import time

class InternetTest:

    headers = []

    def Test(self, download, ping, upload, frequency):
    
        while True:

            print(frequency)

            from speedtest import Speedtest
            st = Speedtest()

            if download:  
                self.headers.append("download")
                download_speed = st.download()
    
            if upload: 
                self.headers.append("upload")
                upload_speed = st.upload()  

            if ping:  
                self.headers.append("ping")
                servernames =[]  
                st.get_servers(servernames)  
                ping_delay = st.results.ping  

            if download == False and upload == False and ping == False:
                print("Please check one !") 

            print(self.headers)

            time.sleep(int(frequency)*60)