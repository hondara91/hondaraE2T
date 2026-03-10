from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
client = MongoClient('mongodb://localhost:27017')

db = client['mibase']

collection = db['productos']

nombre = input("INTRODUCE NOMBRE DEL ARTÍCULO: ")

try:
    for producto in collection.find({"nombre": nombre} ):
        if producto["precio"] == 20: print("PRODUCTO CORRECTO")
        else: print("ESE NO ES")

except ConnectionFailure: print("ERROR DE CONEXIÓN A MONGODB")


