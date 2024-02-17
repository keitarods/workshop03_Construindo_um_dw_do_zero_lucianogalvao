import faker as fk
import faker_commerce
import os
from faker import Faker
from random import randint, uniform
from pandas import DataFrame


#Instanciando a classe Faker.
fake = Faker()

#Adicionando o provider com nomes de produtos.
fake.add_provider(faker_commerce.Provider)


def criar_products(param: int):
#Loop para criação de uma lista com 150 produtos aleatórios.
    list_product = []
    i = 0
    while i <= param:
        ean = randint(100000000000000,999999999999999)
        name_product = fake.ecommerce_name()
        value = round(uniform(0, 100),2)
        list_product.append([ean,name_product,value])
        i += 1

    #Criando Dataframe dos produtos e gerando o arquivo products.csv.
    df = DataFrame(list_product, columns=["EAN","NAME","VALUE"])

    #Verifica se o arquivo products.csv ja existe
    if not os.path.exists("./backend/fakeapi/products.csv"):
        df.to_csv("./backend/fakeapi/products.csv", index = False, lineterminator=None)
        print("Arquivo products.csv criado")
    else:
        print("O arquivo products.csv ja existe")
