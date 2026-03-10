from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
client = MongoClient('mongodb://localhost:27017')
db = client['mibase']
collection = db['productos']

while True:

    print("Seleccione una opción")
    print("1. Para introducir un artículo")
    print("2. Para buscar un artículo")
    print("3. Para actualizar producto")
    print("5. Para salir")

    opcion = int(input("\n-----------------------------\nINTRODUCE UNA OPCIÓN: "))

    if opcion == 1:

        cantidad_productos = int(input("CUÁNTOS PRODUCTOS QUIERES INTRODUCIR: "))

        productos_insertar = []

        for i in range(cantidad_productos):

            nombre = input("INTRODUZCA EL NOMBRE DEL PRODUCTO: ")
            precio = float(input("INTRODUZCA EL PRECIO DEL PRODUCTO: "))
            stock = int(input("Introduzca el stock del producto: "))

            producto_nuevo = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,  
            }

            productos_insertar.append(producto_nuevo)

        #db.productos.insert_one(producto_nuevo)

        db.productos.insert_many(productos_insertar)


    elif opcion == 2:

        articulo_buscar = input("INTRODUZCA EL NOMBRE DEL ARTÍCULO: ")
        articulos = db.productos.find({"nombre": articulo_buscar.lower()})

        for articulo in articulos:
            print(articulo)

    elif opcion == 3:

        articulo_buscar = input("INTRODUZCA EL NOMBRE DEL ARTÍCULO: ")
        precio = float(input("INTRODUCE PRECIO: "))
        db.productos.update_one({"nombre": articulo_buscar.lower()}, {"$set": {"precio": precio}})

    elif opcion == 5: break
