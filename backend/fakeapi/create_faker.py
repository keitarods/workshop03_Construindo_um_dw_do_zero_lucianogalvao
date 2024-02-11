import faker as fk
from faker import Faker
from random import randint, uniform
from pandas import DataFrame
import faker_commerce

#Instanciando a classe Faker.
fake = Faker()

#Adicionando o provider com nomes de produtos.
fake.add_provider(faker_commerce.Provider)

list_product = []
i = 0

#Loop para criação de uma lista com 150 produtos aleatórios.
while i <= 150:
    ean = randint(100000000000000,999999999999999)
    name_product = fake.ecommerce_name()
    value = round(uniform(0, 100),2)
    list_product.append([ean,name_product,value])
    i += 1

#Criando Dataframe dos produtos e gerando o arquivo products.csv.
df = DataFrame(list_product, columns=["EAN","NAME","VALUE"])

df.to_csv("backend/fakeapi/products.csv", index = False, lineterminator=None)