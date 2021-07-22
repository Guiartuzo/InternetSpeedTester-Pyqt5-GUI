import pandas
import glob
import os
from openpyxl import load_workbook


class Writer:

    def __init__(self):
        self.data_frame = pandas.DataFrame()
        self.index = self.getTestID()

    def WriteFile(self, header, data):
        
        self.CreateFile(header)

        data_series = pandas.Series(data, index = self.data_frame.columns)
        self.data_frame = self.data_frame.append(data_series, ignore_index=True)

        book = load_workbook('internet_test_{}.xlsx'.format(self.index+1))
        writer = pandas.ExcelWriter('internet_test_{}.xlsx'.format(self.index+1), engine='openpyxl') 
        writer.book = book

        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        self.data_frame.to_excel(writer, sheet_name='Sheet1')
        writer.save()

    def getTestID(self):

        lista = glob.glob('internet_test*.xlsx')
        return len(lista)

    def CreateFile(self, header):

        if not os.path.exists('internet_test_{}.xlsx'.format(self.index+1)):
            
            self.data_frame = pandas.DataFrame(columns = header)
            writer = pandas.ExcelWriter('internet_test_{}.xlsx'.format(self.index+1), engine='xlsxwriter')
            self.data_frame.to_excel(writer, sheet_name='Sheet1')
            writer.save()
