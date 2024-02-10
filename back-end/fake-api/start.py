from fastapi import FastAPI

app = FastAPI()

@app.get("/gerar_compra")

async def gerar_compra():
    return {
        "cliente": "Nome",
        "creditcard": "Tipo do cartão",
        "ean": "Código de barra do produto",
        "price": "Preço do produto",
        "Store": 11,
        "dateTime" : "Data da compra",
        "ClientePosition" : "Posição do cliente"
        
}