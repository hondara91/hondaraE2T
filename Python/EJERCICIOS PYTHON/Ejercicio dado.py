#Haz una clase Dado que simule el lanzamiento de 2 dados (moneda)

import random

class Dado:

    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        lanzamientos = 0
        opciones = []
        for i in range(1, self.caras + 1): opciones.append(i)
        x = random.choice(opciones)
        print("HA SALIDO", x)
        lanzamientos += 1

    def jugar():
        
        while True:
            a = int(input("¿DE CUANTOS LADOS ES EL DADO?: "))
            if a == 2: a = moneda
            elif a == 6: a = dado
            elif a == 12: a = dodecaedro
            elif a == 20: a = icosaedro
            else: print("NO TENEMOS DADOS ASÍ")
            
            for i in range(int(input("\n¿CUÁNTOS LANZAMIENTOS QUIERES HACER?: "))): a.lanzar()

moneda = Dado(2)
dado = Dado(6)
dodecaedro = Dado(12)
icosaedro = Dado(20)

Dado.jugar()