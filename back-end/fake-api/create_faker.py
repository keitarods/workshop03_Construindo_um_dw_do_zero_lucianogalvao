import faker as fk
from faker import Faker
from random import randint, uniform
import pandas as pd

fake = Faker()
list_product = []
i = 0

while i < 500:
    ean = randint(100000000000000,999999999999999)
    name = fake.name()
    value = round(uniform(0, 100),2)
    list_product.append([ean,name,value])
    print(list_product)
    i += 1

df = pd.DataFrame(list_product, columns=["EAN","NAME","VALUE"])

df.to_csv("products.csv", index = False)
