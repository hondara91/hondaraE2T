import random

ronda = 0

ganacount = 0
pierdecount = 0
nocambiacount = 0
cambiandocount = 0
porcentajevictorias = 0

X = int(input("¿CUÁNTAS RONDAS QUIERES JUGAR?\n"))

for i in range (X):

    LISTAPUERTAS = ["A", "B", "C"]

    print("\n------------------------------------------------------------\n\nEMPIEZA EL JUEGO\n")

    PREMIADA = random.choice(LISTAPUERTAS)
    print("\nLA PUERTA PREMIADA ES LA", PREMIADA)

    JUGADOR = random.choice(LISTAPUERTAS)
    print("LA PUERTA ELEGIDA ES LA", JUGADOR)

    LIBRE = []
    ELIMINADA = ""
    DISPONIBLE = ""
    LISTAFINAL = []
    ELECCIONFINAL = ""

    for i in LISTAPUERTAS: 
        if i != JUGADOR: LIBRE.append(i)
    print("\nQUEDAN SIN ESCOGER LAS PUERTAS", LIBRE)

    while True:
        ELIMINADA = random.choice(LIBRE)
        if ELIMINADA != PREMIADA: 
            LIBRE.remove(ELIMINADA)
            break
    
    print("\nLA PUERTA DESCARTADA POR EL PRESENTADOR ES LA", ELIMINADA)
    if LIBRE[0] != ELIMINADA: DISPONIBLE = LIBRE[0]

    LISTAFINAL = [DISPONIBLE, JUGADOR]
    print("SE LE DA LA OPCIÓN DE CAMBIAR ENTRE", LISTAFINAL)

    ELECCIONFINAL = random.choice(LISTAFINAL)
    print("EL JUGADOR ELIGE LA", ELECCIONFINAL)
    if ELECCIONFINAL != JUGADOR and ELECCIONFINAL == PREMIADA: 
        cambiandocount += 1
        print("CAMBIA OPCIÓN\n\nACERTÓ")
        ganacount += 1
    elif ELECCIONFINAL == JUGADOR and ELECCIONFINAL == PREMIADA: 
        nocambiacount += 1
        print("SE MANTIENE\n\nACERTÓ")
        ganacount += 1
    else: 
        if ELECCIONFINAL == JUGADOR: (print("SE MATIENE\n"))
        else: (print("CAMBIÓ\n"))
        print("LA CAGÓ")
        pierdecount += 1

    ronda += 1

totalvictorias = cambiandocount + nocambiacount
porcentajevictorias = ganacount/ronda*100
porcentajecambiando = cambiandocount/ganacount*100
porcentajeNOcambiando = nocambiacount/ganacount*100

print("\nTOTAL VICTORIAS: ", totalvictorias)
print("PORCENTAJE VICTORIAS: ", porcentajevictorias, "%" )
print("CAMBIANDO ELECCIÓN: ", porcentajecambiando, "%")
print("SIN CAMBIAR ELECCIÓN: ", porcentajeNOcambiando, "%")


