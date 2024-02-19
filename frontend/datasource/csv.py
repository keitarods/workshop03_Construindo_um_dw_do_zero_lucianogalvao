import streamlit as st
from streamlit import cache
import openpyxl
import pandas as pd
import os
import datetime
from io import BytesIO
from drive.client import DriveClient

class CSVCollector:
    def __init__ (self, schema, drive, cell_range):
        self._schema = schema
        self._drive = drive
        self._buffer = None
        self.cell_range = cell_range
        self.localparquet = "./frontend/drive/dataapi/"
        return
    
    def start(self):
        getData = self.getData()
        extractData = None

        if getData is not None:
            extractData = self.extractData(getData, self.cell_range)
        if extractData is not None:
            validateData = self.validateData(extractData)
            if validateData is not None:
                self.convertToParquet(extractData)

                if st.button("Enviar"):
                    print(self._buffer)
                    DriveClient().upload_dataset(self._buffer, f"excel-{self.fileName()}")
                    #self.removeParquet()

    def getData(self):
        dados_excel = st.file_uploader("Insira o arquivo Excel", type=[".xlsx"])
        return dados_excel

    def extractData(self, dados_excel, cell_range: str):
        workbook =  openpyxl.load_workbook(dados_excel) 
        sheet = workbook.active
        range_cell = sheet[self.cell_range]

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
            except BaseException as e:
                error.append(f"Erro na linha {index}: {e}")
            if error:
                raise st.error(BaseException("\n".join(error)))
            return st.success("Upado com sucesso")
        return dataframe
        
    def convertToParquet(self, response):
        try:
            self._buffer = BytesIO()
            print("Arquivo transformado com sucesso para formato parquet")
            return response.to_parquet(self._buffer)
            
        except Exception as e:
            print(f"Erro ao transforma o arquivo para formato parquet", {e})
            self._buffer = None

    def fileName(self):
        data_atual = datetime.datetime.now().isoformat()
        match = data_atual.split(".")
        return f"excel-{match[0]}.parquet"