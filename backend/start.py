from datasource.api import APICollector
from contracts.schema import Compraschema

schema = Compraschema

minha_classe = APICollector(schema).start(2)

print(minha_classe)