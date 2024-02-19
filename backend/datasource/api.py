import requests
from contracts.schema import genericschema, Compraschema
import pyarrow.parquet as pq
from typing import List
from pandas import DataFrame
from io import BytesIO
import datetime
import os
import time

class APICollector:
    def __init__ (self, schema, drive):
        self._schema = schema
        self._drive = drive
        self._buffer = None

    def start(self, param):
        response = self.getData(param)
        response = self.extractData(response)
        response = self.transformDf(response)

        self.convertToParquet(response)
        self._drive.upload_dataset(self._buffer, f"{self.fileName()}")

    def getData(self, param):
        response = None
        if param > 1:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compras/{param}').json()
        else:
            response = requests.get(f'http://127.0.0.1:8000/gerar_compra').json()
        
        return response 
    
    def extractData(self, response):
        result: List[genericschema] = []
        for item in response:
            index = {}
            for key, value in self._schema.items():
                if type(item.get(key)) == value:
                    index[key] = item[key]
                else:
                    index[key] = None
                
            result.append(index)

        return result
    
    def transformDf(self, response):
        result = DataFrame(response)

        return result

    def convertToParquet(self, response):
        try:
            self._buffer = BytesIO()
            print("Arquivo transformado com sucesso para formato parquet")
            return response.to_parquet(self._buffer)
        except Exception as e:
            print(f"Erro ao transforma o arquivo para formato parquet")
            self._buffer = None

    def fileName(self):
        data_atual = datetime.datetime.now().isoformat()
        match = data_atual.split(".")
        return f"api_response_compra_{match[0]}.parquet"