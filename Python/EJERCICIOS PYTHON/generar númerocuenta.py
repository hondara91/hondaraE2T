import random
class numcuenta:
    def __init__(self, username):
        self.nombre = username
        self.iban = self.num_cuenta

    def num_cuenta(self):
        x = ""
        for i in range(20):
            x += str(random.randint(0, 9))
        self.numero = "ES" + x
        return (self.numero)


cuenta1 = numcuenta("Lolomon")
cuenta2 = numcuenta("Mongoton")

print(cuenta1.iban())
