#Haz una clase Dado que simule el lanzamiento de 2 dados (moneda)

import random

class Dado:

    def lanzar(a):
        lanzamientos = 0
        opciones = []
        for i in range(1, a + 1): opciones.append(i)
        x = random.choice(opciones)
        print("HA SALIDO", x)
        lanzamientos += 1

    def jugar():
        while True:
            a = int(input("\n¿DE CUANTOS LADOS ES EL DADO?: "))
            for i in range(int(input("\n¿CUÁNTOS LANZAMIENTOS QUIERES HACER?: "))): Dado.lanzar(a)

Dado.jugar()