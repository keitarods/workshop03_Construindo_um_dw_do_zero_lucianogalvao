import streamlit as st
import openpyxl
import pandas as pd
import os

class CSVCollector:
    def __init__ (self, schema, drive, cell_range):
        self._schema = schema
        self._drive = drive
        self.buffer = None
        self.cell_range = cell_range
        self.localparquet = "../drive/dataapi/"
        return
    
    def start(self, param):
        getData = self.getData(param)
        
        if getData is not None:
            extractData = self.extractData(getData, self.cell_range)
        if extractData is not None:
            validateData = self.validateData(extractData)
            return validateData

    def getData(self, param):
        dados_excel = st.file_uploader("Insira o arquivo Excel", type=["xslx"])

        return dados_excel
    
    def extractData(self, dados_excel, cell_range: str):
        workbook =  openpyxl.load_workbook(dados_excel)
        sheet = workbook.active
        range_cell = sheet(cell_range)

        #Pegando o indice 0 (Cabeçalho)
        headers = [cell.value for cell in range_cell[0]]

        data = []
        for row in range_cell[1:]:
            data.append([cell.value for cell in row])

        dataframe = pd.DataFrame(data, columns = headers)
        return dataframe
    
    def validateData(self, dataframe):
        error = []
        for index, row in dataframe.iterrows():
            try:
                self._schema(**row.to_dict())
            except Exception as e:
                error.apend(f"Erro na linha {index}: {e}")
            if error:
                raise st.error(Exception("\n".join(error)))
            return st.success("Upado com sucesso")
        return dataframe
        
        return
    
    def loadData(self, response):
        return