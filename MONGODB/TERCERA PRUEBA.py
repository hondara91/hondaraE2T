from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = MongoClient('mongodb://localhost:27017')
db = client['mibase']
collection = db['productos']

for producto in collection.find():
    print(producto)