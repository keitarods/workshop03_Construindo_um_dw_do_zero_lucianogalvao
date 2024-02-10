from fastapi import FastAPI
from faker import Faker
import pandas as pd

app = FastAPI()
fake = Faker()



@app.get("/gerar_compra")

def gerar_compra():
    return {
        "cliente": fake.name(),
        "creditcard": fake.credit_card_provider(),
        "ean": "Código de barra do produto",
        "price": "Preço do produto",
        "Store": 11,
        "dateTime" : "Data da compra",
        "ClientePosition" : "Posição do cliente"
        
}