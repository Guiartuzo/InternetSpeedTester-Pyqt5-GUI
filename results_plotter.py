import csv

class Writer:

    def WriteCSV(self, download = 0, upload = 0, ping = 0):

        header = ['time', 'download', 'country_code2', 'country_code3']
        data = ['Afghanistan', 652090, 'AF', 'AFG']

        with open('countries.csv', 'w', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)