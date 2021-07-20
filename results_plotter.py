import pandas
import glob

class Writer:

    def WriteFile(self, header, data):
        
        data_frame = pandas.DataFrame(columns = header)

        data_series = pandas.Series(data, index = data_frame.columns)
        data_frame = data_frame.append(data_series, ignore_index=True)

        index = self.getTestID()

        writer = pandas.ExcelWriter('internet_test_{}.xlsx'.format(index+1), engine='xlsxwriter')
        data_frame.to_excel(writer, sheet_name='Sheet1')
        writer.save()

    def getTestID(self):

        lista = glob.glob('internet_test*.xlsx')
        return len(lista)