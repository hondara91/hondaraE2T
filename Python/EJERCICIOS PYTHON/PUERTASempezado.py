import random

class Concurso:

    puertas = [1, 2, 3]

    def __init__ (self, iteraciones):
        self.iteraciones = iteraciones
        self.puertas = [1, 2, 3]

    def concursar (self):
        premio = random.choice(self.puertas)
        jugador = random.choice(self.puertas)

        cambia = random.randit(1, 2)