# Crea un programa que gestione una agenda de contactos
# USANDO DICCIONARIO  donde:
# - La clave es el nombre d ela persona
# - El valor es su numero de teléfono, dirección, empleo
# El programa debe permitir:
# - Añadir un contacto nuevo
# - Buscar un contacto por nombre
# - Mostrar todos los contactos (ordenados alf)

class Agenda:

    def __init__(self, nombre, telefono, direccion, empleo):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.empleo = empleo

    def __str__(self):
        return f"\nNombre: {self.nombre} \nTel: {self.telefono} \nDir: {self.direccion} \nEmpleo: {self.empleo}"


def añadir_contacto(lista):

    nombre = input("INTRODUCE NOMBRE: ")
    telefono = int(input("INTRODUCE NÚMERO DE TELÉFONO: "))
    direccion = input("INTRODUCE DIRECCIÓN: ")
    empleo = input("INTRODUCE EMPLEO: ")
    contacto = Agenda(nombre, telefono, direccion, empleo)
    lista.append(contacto)
    print("Contacto añadido\n")

lista = []

while True:

    print("\nSeleccione una opción")
    print("1. Para introducir un contacto")
    print("2. Para buscar un contacto")
    print("3. Para editar un contacto")
    print("4. Eliminar contacto")
    print("5. Ver contactos")
    print("6. Para salir")

    opcion = int(input("\n-----------------------------\nINTRODUCE UNA OPCIÓN: "))

    if opcion == 1:
        añadir_contacto(lista)

    if opcion == 2:
        

    elif opcion == 5:
        for contacto in lista:
            print(contacto)

    elif opcion == 6:
        break