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

    def __init__(self, name, phone, address, rank):
        self.nombre = name
        self.telefono = phone
        self.direccion = address
        self.empleo = rank

    def __str__(self):
        return f"\n|Nombre: {self.nombre} \n|Tel: {self.telefono} \n|Dir: {self.direccion} \n|Empleo: {self.empleo}"
    
    def __lt__(self, x: Contacto):
        return self.nombre < x.nombre
    
    def diccionario(self):
        return {"nombre": self.nombre, "telefono": self.telefono, "direccion": self.direccion, "empleo": self.empleo}


class Agenda:

    def __init__(self):
        self.lista: list[Contacto] = []
        self.cargar_agenda()

    def cargar_agenda(self):
        try:
            with open("Python/EJERCICIOS PYTHON/agenda.json", "r") as archivo:
                miagenda = json.load(archivo)
                
                for i in miagenda:
                    contacto = Contacto(i["nombre"], i["telefono"], i["direccion"], i["empleo"])
                    self.lista.append(contacto)
                self.lista.sort()

        except (FileNotFoundError, json.JSONDecodeError):
            print("No se encontró ninguna agenda. Se iniciará una agenda vacía.")
            self.lista = []
        
    def guardar_cambios(self):
        miagenda = []
        for contacto in self.lista: miagenda.append(contacto.diccionario())

        with open("Python/EJERCICIOS PYTHON/agenda.json", "w", encoding="utf-8") as archivo:
            json.dump(miagenda, archivo, indent=4, ensure_ascii=False)

    def añadir_contacto(self):
        nombre = input("INTRODUCE NOMBRE: ")
        telefono = input("INTRODUCE NÚMERO DE TELÉFONO: ")
        direccion = input("INTRODUCE DIRECCIÓN: ")
        empleo = input("INTRODUCE EMPLEO: ")

        contacto = Contacto(nombre, telefono, direccion, empleo)
        self.lista.append(contacto)
        self.lista.sort()
        self.guardar_cambios()
        print("\nContacto añadido\n")

    def ver_contactos(self):
        if len(self.lista) == 0: 
            print("No hay contactos guardados\n")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for i, contacto in enumerate(self.lista, start=1):
                print(f"\nContacto {i}\n{contacto}\n")

    def buscar_contacto(self):
        if len(self.lista) == 0: 
            print("No hay contactos guardados\n")
        
        else: 
            while True: 
                buscar_nombre = input("INTRODUCE NOMBRE PARA BUSCAR: ").lower()
                for contacto in self.lista:
                    if contacto.nombre.lower() == buscar_nombre: 
                        print(f"\nContacto encontrado\n {contacto} \n")
                        break
            
                    else: print("No se encontró ningún contacto con ese nombre.\n")
                break

    def editar_contacto(self):
        if len(self.lista) == 0: 
            print("No hay contactos guardados\n")

        else:
            while True:
                editar_nombre = input("INTRODUCE NOMBRE DEL CONTACTO A EDITAR: ").lower()
                for contacto in self.lista:
                    if contacto.nombre.lower() == editar_nombre:
                        print(f"Contacto actual\n {contacto}\n")
                        
                        contacto.nombre = input("NUEVO NOMBRE: ")
                        contacto.telefono = input("NUEVO TELÉFONO: ")
                        contacto.direccion = input("NUEVA DIRECCIÓN: ")
                        contacto.empleo = input("NUEVO EMPLEO: ")

                        self.lista.sort()
                        self.guardar_cambios()
                        print("Contacto editado correctamente")
                
                    print("No se encontró ningún contacto con ese nombre.\n")
                break

    def eliminar_contacto(self):
        if len(self.lista) == 0: 
            print("No hay contactos guardados\n")

        else:
            while True:
                eliminar_nombre = input("INTRODUCE EL NOMBRE DEL CONTACTO A ELIMINAR: ").lower()
                for contacto in self.lista:
                    if contacto.nombre.lower() == eliminar_nombre:
                        self.lista.remove(contacto)
                        self.guardar_cambios()
                        print("\nContacto eliminado correctamente.\n")
                        break
                
                    else: print("No se encontró ningún contacto con ese nombre.\n")
                break
 
    def menu(self):
        while True:
            print("\n-----------------------------------------\n")
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

Agenda().menu()