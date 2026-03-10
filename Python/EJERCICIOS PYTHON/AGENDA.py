# Crea un programa que gestione una agenda de contactos
# USANDO DICCIONARIO  donde:
# - La clave es el nombre d ela persona
# - El valor es su numero de teléfono, dirección, empleo
# El programa debe permitir:
# - Añadir un contacto nuevo
# - Buscar un contacto por nombre
# - Mostrar todos los contactos (ordenados alf)

class agenda:

    def __init__(self, cellphone, address, rank):
        self.movil = cellphone
        self.direccion = address
        self.empleo = rank
        
    def añadirCONTACTO():
        for i in range(1, 1001):
            i = (input("INTRODUCE NOMBRE: "))
            num = int(input("INTRODUCE NÚMERO DE TELÉFONO: "))
            add = input("INTRODUCE DIRECCIÓN: ")
            rank = input("INTRODUCE EMPLEO: ")
            i = agenda(num, add, rank)
            Contactos = lista.append(i)
            while True:
                x = (input("DESEAS AÑADIR A ALGUIEN MÁS (S/N): ")).lower()
                if x == "N": break
                elif x == "S": continue
                else: print("INTRODUCE UN COMANDO VÁLIDO")

lista = []
Contactos = []
        
while True:

    print("\nSeleccione una opción")
    print("1. Para introducir un contacto")
    print("2. Para buscar un contacto")
    print("3. Para editar un contacto")
    print("4. Eliminar contacto")
    print("5. Para salir")

    opcion = int(input("\n-----------------------------\nINTRODUCE UNA OPCIÓN: "))

    if opcion == 1: agenda.añadirCONTACTO()

    for i in Contactos:
        print(i)
