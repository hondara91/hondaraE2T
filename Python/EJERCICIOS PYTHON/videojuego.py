#videojuego usando clases
#clase Personaje que tiene nombre, vida y una función de ataque
#jugador y enemigo son personaje y atacan por turnos
#gana quien deje vida del otro a cero

import random

class Personaje:

    def __init__(self, name, life):
        self.nombre = name
        self.vida = life
        

    def atacar(self):
        return random.randint(1, 15)
    

jugador = Personaje("JUGADOR", 50)
enemigo = Personaje("ENEMIGO", 50)

orden = [jugador, enemigo]
while jugador.vida > 0 and enemigo.vida > 0:
    print ("VIDA ENEMIGO", enemigo.vida)
    print ("VIDA JUGADOR", jugador.vida)
    random.shuffle(orden)
    orden[0].vida -= orden[1].atacar()
    if orden[1].atacar() == enemigo.atacar(): print("ENEMIGO ATACA")
    elif orden[0].atacar() == jugador.atacar(): print("JUGADOR ATACA")

if enemigo.vida <= 0: print("Has ganado")
else: print("Has perdido")