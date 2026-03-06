# Crear clase concurso que calcule el problema monty hall 
# para un número determinado de veces
# Hay 3 puertas y sólo 1 tiene premio
# El programa hará de jugador y presentador de manera automática, 
# eligiendo una puerta al azar, el presentador descarta una de las no elegidas
# y decidiendo d emanera aleatoria si cambiar o no de eleccion
# al final se imprimirá un informe 
# del porcentaje de veces que ganó manteniendo la elección
# y el porcentaje de veces que gano cambiando elección

import random

class concurso:

    def __init__(self, number, prize):
        self.numero = number
        self.premio = prize

    def ronda():

        PREMIADA = random.choice(LISTAPUERTAS)
        print("LA PUERTA PREMIADA ES LA", PREMIADA)

        JUGADOR = random.choice(LISTAPUERTAS)
        print("LA PUERTA ELEGIDA ES LA", JUGADOR)

        LIBRE = []
        ELIMINADA = ""
        DISPONIBLE = ""
        LISTAFINAL = []
        ELECCIONFINAL = ""

        for i in LISTAPUERTAS: 
            if i != JUGADOR: LIBRE.append[i]
        print("QUEDAN SIN ESCOGER LAS PUERTAS", LIBRE)
        
        while ELIMINADA == PREMIADA:
            ELIMINADA = random.choice(LIBRE)
        print("LA PUERTA DESCARTADA POR EL PRESENTADOR ES LA", ELIMINADA)
        DISPONIBLE = LIBRE[0]

        LISTAFINAL = [DISPONIBLE, JUGADOR]
        print("HAY QUE ELEGIR ENTRE", LISTAFINAL)

        ELECCIONFINAL = random.choice(LISTAFINAL)
        print("EL JUGADOR ELIGE", ELECCIONFINAL)



PUERTA1 = concurso("1", False)
PUERTA2 = concurso("2", False)
PUERTA3 = concurso("3", False)

LISTAPUERTAS = [PUERTA1, PUERTA2, PUERTA3]

count = int(input("INTRODUCE NÚMERO DE ITERACIONES: "))

while count != 0:

    PREMIADA = random.choice(LISTAPUERTAS).tienepremio()
    JUGADOR = random.choice(LISTAPUERTAS)
    LIBRE = ""

    for i in PUERTASlist:
        if i == JUGADOR: PUERTASlist.remove[i] 
    
    PRESENTADOR = random.choice(PUERTASlist)

    for j in PUERTASlist:
        if j == PRESENTADOR: 
            PUERTASlist.remove[j]
        else: j == LIBRE

    PUERTASlist.append(JUGADOR, LIBRE)

    JUGADOR2 = random.choice(PUERTASlist)
    if  PUERTASlist[0] == JUGADOR2: print("JUGADOR mantiene su elección")
    else:  print("JUGADOR cambia su elección")

    count -= 1



        
    

        
