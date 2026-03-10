class agenda:

    def __init__(self, cellphone, address, rank):
        self.movil = cellphone
        self.direccion = address
        self.empleo = rank
    
    def __str__(self): return str(self.movil, self.direccion, self.empleo)
        
    def añadirCONTACTO():
        x = input("INTRODUCE NOMBRE: ")
        num = int(input("INTRODUCE NÚMERO DE TELÉFONO: "))
        add = input("INTRODUCE DIRECCIÓN: ")
        rank = input("INTRODUCE EMPLEO: ")
        x = agenda(num, add, rank)
        lista.append(x)
                  
while True:
    lista = []

    print("\nSeleccione una opción")
    print("1. Para introducir un contacto")
    print("2. Para buscar un contacto")
    print("3. Para editar un contacto")
    print("4. Eliminar contacto")
    print("5. Ver contactos")
    print("6. Para salir")

    opcion = int(input("\n-----------------------------\nINTRODUCE UNA OPCIÓN: "))

    if opcion == 1: agenda.añadirCONTACTO()

    if opcion == 5: 
        for i in lista:
            print(i)
