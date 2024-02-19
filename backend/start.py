from datasource.api import APICollector
from contracts.schema import Compraschema
from fakeapi.create_faker import criar_products
from drive.client import DriveClient


import time
import schedule

schema = Compraschema
drive = DriveClient()

def apicollector(schema, drive, repeat):
    response = APICollector(schema, drive).start(repeat)
    print("Processo executado")
    return response

criar_products(100)

# Esta parte do código define um agendamento usando a biblioteca schedule. Ele especifica que a função apicollector deve ser executada a cada 1 minuto.
schedule.every(0.1).minutes.do(apicollector, schema, drive, 50)

#Loop que define enquanto for == True, o código será executado baseado no time setado no schedule
while True:
    schedule.run_pending()
    time.sleep(1)