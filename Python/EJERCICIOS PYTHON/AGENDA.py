# Crea un programa que gestione una agenda de contactos
# USANDO DICCIONARIO  donde:
# - La clave es el nombre d ela persona
# - El valor es su numero de teléfono, dirección, empleo
# El programa debe permitir:
# - Añadir un contacto nuevo
# - Buscar un contacto por nombre
# - Mostrar todos los contactos (ordenados alf)


import json

#def cargar_agenda():
    #with open(input("INTRODUZCA NOMBRE DE LA AGENDA QUE QUIERE CARGAR: "), "r") as agenda:
        #a = json.load(agenda)
    #return a

#def guardar_agenda(a):
    #with open("agenda.json", "w") as agenda:
        #json.dump(a, agenda, indent = 4)

#agenda_cargada = cargar_agenda()
#agenda_guardada = guardar_agenda()




class Contacto:

    def __init__(self, nombre, telefono, direccion, empleo):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.empleo = empleo

    def __str__(self):
        return f"\n|Nombre: {self.nombre} \n|Tel: {self.telefono} \n|Dir: {self.direccion} \n|Empleo: {self.empleo}"

class Agenda:

    def __init__(self):
        self.lista = []

    def añadir_contacto(self):
        nombre = input("INTRODUCE NOMBRE: ")
        telefono = int(input("INTRODUCE NÚMERO DE TELÉFONO: "))
        direccion = input("INTRODUCE DIRECCIÓN: ")
        empleo = input("INTRODUCE EMPLEO: ")

        contacto = Contacto(nombre, telefono, direccion, empleo)
        self.lista.append(contacto)
        #self.lista.sort()
        print("Contacto añadido\n")

    def menu(self):
        while True:
            print("\nSeleccione una opción")
            print("1. Para introducir un contacto")
            print("2. Para buscar un contacto")
            print("3. Para editar un contacto")
            print("4. Eliminar contacto")
            print("5. Ver contactos")
            print("6. Para salir")
            try:
                opcion = int(input("\n-----------------------------\nINTRODUCE UNA OPCIÓN: "))
            except ValueError:
                print("Debes introducir un número.\n")
                continue

            if opcion == 1:
                self.añadir_contacto()

            elif opcion == 6:
                break



Agenda().menu()