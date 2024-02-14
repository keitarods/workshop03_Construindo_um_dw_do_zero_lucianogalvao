from datasource.api import APICollector
from contracts.schema import Compraschema
from drive.client import DriveClient

schema = Compraschema
drive = DriveClient()

minha_classe = APICollector(schema, drive).start(3)

print(minha_classe) 