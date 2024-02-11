from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random
import os

app = FastAPI()
fake = Faker()

file_name = "backend/fakeapi/products.csv"
df = pd.read_csv(file_name)
df['indice'] = range(1, len(df) +1)
df.set_index('indice', inplace = True)

@app.get("/gerar_compra/{numero_registro}")
def gerar_compra(numero_registro: int):

    if numero_registro <1:
        return{"Error": "O número deve ser maior que 1"}    

    respostas = []
    for _ in range(numero_registro):
        index = random.randint(1, len(df)-1)
        tupla = df.iloc[index]
        compra = {
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tupla["NAME"],
            "ean": int(tupla["EAN"]),
            "price": round(float(tupla["VALUE"])*1.2,2),
            "clientePosition" : fake.location_on_land(),
            "store": 11,
            "dateTime" : fake.iso8601(),
                }
        respostas.append(compra)

    return respostas

