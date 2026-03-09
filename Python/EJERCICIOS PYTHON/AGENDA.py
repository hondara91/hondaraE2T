# Crea un programa que gestione una agenda de contactos
# USANDO DICCIONARIO  donde:
# - La clave es el nombre d ela persona
# - El valor es su numero de teléfono, dirección, empleo
# El programa debe permitir:
# - Añadir un contacto nuevo
# - Buscar un contacto por nombre
# - Mostrar todos los contactos (ordenados alf)

class agenda:

    def __init__(self, name):
        self.nombre = name

    def datos(self, cellphone, address, rank):
        self.movil = cellphone
        self.direccion = address
        self.empleo = rank
        
    def añadirNOMBRE():
        for i in range(1, 1001):
            i = agenda((input("INTRODUCE NOMBRE: ")))
            x = input("DESEAS AÑADIR A ALGUIEN MÁS (S/N): ")
            if x == "N": break
            elif x == "S": pass
            else: print("INTRODUCE UN COMANDO VÁLIDO")

    def añadirDATOS(self):
        
