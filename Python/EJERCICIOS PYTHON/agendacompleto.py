import json

with open("agenda.json", "r") as agenda: 
    a = json.load(agenda)

class Contacto:
    def __init__(self, nombre, telefono, direccion, empleo):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.empleo = empleo

    def __str__(self):
        return f"|Nombre: {self.nombre}\n|Tel: {self.telefono}\n|Dir: {self.direccion}\n|Empleo: {self.empleo}"
    
    def __lt__(self, otro): 
        return self.nombre < otro.nombre


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
        self.lista.sort()
        print("Contacto añadido\n")

    def ver_contactos(self):
        if len(self.lista) == 0:
            print("No hay contactos guardados.\n")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for i, contacto in enumerate(self.lista, start=1):
                print(f"\nContacto {i}")
                print(contacto)
                print()

    def buscar_contacto(self):
        if len(self.lista) == 0:
            print("No hay contactos para buscar.\n")
            return

        nombre_buscar = input("INTRODUCE EL NOMBRE A BUSCAR: ").lower()

        for contacto in self.lista:
            if contacto.nombre.lower() == nombre_buscar:
                print("\nContacto encontrado:")
                print(contacto)
                print()
                return

        print("No se encontró ningún contacto con ese nombre.\n")

    def editar_contacto(self):
        if len(self.lista) == 0:
            print("No hay contactos para editar.\n")
            return

        nombre_editar = input("INTRODUCE EL NOMBRE DEL CONTACTO A EDITAR: ").lower()

        for contacto in self.lista:
            if contacto.nombre.lower() == nombre_editar:
                print("\nContacto actual:")
                print(contacto)

                contacto.nombre = input("NUEVO NOMBRE: ")
                contacto.telefono = int(input("NUEVO TELÉFONO: "))
                contacto.direccion = input("NUEVA DIRECCIÓN: ")
                contacto.empleo = input("NUEVO EMPLEO: ")

                print("Contacto editado correctamente.\n")
                return

        print("No se encontró ningún contacto con ese nombre.\n")

    def eliminar_contacto(self):
        if len(self.lista) == 0:
            print("No hay contactos para eliminar.\n")
            return

        nombre_eliminar = input("INTRODUCE EL NOMBRE DEL CONTACTO A ELIMINAR: ").lower()

        for contacto in self.lista:
            if contacto.nombre.lower() == nombre_eliminar:
                self.lista.remove(contacto)
                print("Contacto eliminado correctamente.\n")
                return

        print("No se encontró ningún contacto con ese nombre.\n")

    def menu(self):
        while True:
            print("Seleccione una opción")
            print("1. Introducir un contacto")
            print("2. Buscar un contacto")
            print("3. Editar un contacto")
            print("4. Eliminar contacto")
            print("5. Ver contactos")
            print("6. Salir")

            try:
                opcion = int(input("\nINTRODUCE UNA OPCIÓN: "))
            except ValueError:
                print("Debes introducir un número.\n")
                continue

            if opcion == 1:
                self.añadir_contacto()

            elif opcion == 2:
                self.buscar_contacto()

            elif opcion == 3:
                self.editar_contacto()

            elif opcion == 4:
                self.eliminar_contacto()

            elif opcion == 5:
                self.ver_contactos()

            elif opcion == 6:
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida.\n")


agenda = Agenda()
agenda.menu()