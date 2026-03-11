class Kart:

    def __init__(self, piloto, velocidad_inicial, velocidad_máxima, aceleración):
        self.pilot = piloto
        self.initvel = velocidad_inicial
        self.maxvel = velocidad_máxima
        self.boost = aceleración

    def acelerar(self):
        try: self.boost = int(input("\nACELERANDO km/h: "))
        except ValueError: return f"INTRODUCE UN NÚMERO, CARBÓN"
        velfin = self.initvel + self.boost
        if velfin >= self.maxvel: velfin = self.maxvel
        resultado = f"\n{str(self.pilot)} SUBE DE {str(self.initvel)} km/h a {str(velfin)} km/h"
        self.initvel = velfin
        return resultado

    def frenar(self):
        try: self.boost = int(input("\nBAJANDO A km/H: "))
        except ValueError: return f"INTRODUCE UN NÚMERO, CARBÓN"
        velfin = self.initvel - self.boost
        if velfin <= 0: velfin = 0
        resultado = f"\n{str(self.pilot)} BAJA DE {str(self.initvel)} km/h a {str(velfin)} km/h"
        self.initvel = velfin
        return resultado

    def datos(self):
        return f"{str(self.pilot)} va a una velocidad de {str(self.initvel)} km/h"
    
Mario = Kart("Mario", 0, 300, 0)
Luigi = Kart("Luigi", 0, 300, 0)
Wario = Kart("Wario", 0, 300, 0)
Tortuga = Kart("Tortuga", 0, 300, 0)

while True: 
    x = int(input("\n------------------------------------------\nSELECCIONA UN PERSONAJE: \n1. MARIO\n2. LUIGI\n3. WARIO\n4. TORTUGA\n\n"))
    if x == 1: x = Mario
    elif x == 2: x = Luigi
    elif x == 3: x = Wario
    elif x == 4: x = Tortuga
    else: ("\nELIGE UN PERSONAJE VÁLIDO")
    y = int(input("\nQUÉ QUIERES HACER: \n1. ACELERAR\n2. FRENAR\n3. VER COMO VA\n\n"))
    if y == 1: print(Kart.acelerar(x))
    elif y == 2: print(Kart.frenar(x))
    elif y == 3: print(Kart.datos(x))
    else: ("\nELIGE UNA OPCIÓN VALIDA")
    
S