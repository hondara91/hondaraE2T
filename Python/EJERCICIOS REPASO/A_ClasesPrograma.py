import random

class Personaje:
    def __init__(self, name, race):
        self.nombre = name
        self.raza = race
        self.__nivel = 1

    def setNivel(self, nivel):
        self.__nivel = nivel

    def getNivel(self):
        return self.__nivel


class Enemigo:
    def __init__(self):
        self.__nivel = random.randint(1, 10)