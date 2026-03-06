import random

class cuentabancaria:

    interes = 0.01
    comision_retirada = 1.5
     
    def __init__(self, username, init_amount):
        self.nombre = username
        self.saldo_init = init_amount
        self.iban = self.num_cuenta

    def num_cuenta(self):
        x = ""
        for i in range(20):
            x += str(random.randint(0, 9))
        self.iban = "ES" + x
        return (self.iban)

    def retirar(self):
        retirado = int(input("\nINTRODUCE CANTIDAD A RETIRAR: "))
        if retirado > self.saldo_init: print("SALDO INSUFICIENTE")
        else: 
            c = input("Se va  aplicar una comisión de 1.50 euros, desea continuar? (S/N): ")
            if c == "S": 
                self.saldo_init -= retirado + cuentabancaria.comision_retirada
                print("\n-- SALDO TOTAL", self.saldo_init, "--")
            else: pass
        
    def ingresar(self):
        ingresado = int(input("\nINTRODUCE CANTIDAD A INGRESAR: "))
        self.saldo_init += ingresado
        print("\n-- SALDO TOTAL", self.saldo_init, "--")

cuenta1 = cuentabancaria("Lolomon", 150000)
cuenta2 = cuentabancaria("Mongoton", 300000)

while True:
    o = input("\nDesea realizar una operación? (S/N): ")
    if o == "S":
        print("\n\nMENU CUENTA DEL BANCO\n----------------------")
        CUENTA = int(input("CUENTA1\nCUENTA2\n\nSELECCIONA UNA CUENTA (1, 2): "))
        if CUENTA == 1: print(cuenta1.num_cuenta())
        elif CUENTA == 2: print(cuenta2.num_cuenta())
        OPCION = int(input("\nOPCIÓN 1 RETIRAR DINERO \nOPCIÓN 2 INGRESAR DINERO \nOPCION 3 CONSULTAR SALDO \n\nSELECCIONE UNA OPCION (1, 2, 3): "))
    
        if CUENTA == 1: 
            if OPCION == 1: cuenta1.retirar() 
            elif OPCION == 2: cuenta1.ingresar()
            elif OPCION == 3: print("\n-- SALDO TOTAL", cuenta1.saldo_init, "--")

        elif CUENTA == 2:
            if OPCION == 1: cuenta2.retirar()
            elif OPCION == 2: cuenta2.ingresar()
            elif OPCION == 3: print("\n-- SALDO TOTAL", cuenta2.saldo_init, "--")

    else: 
        print("Hasta pronto!!")
        break


