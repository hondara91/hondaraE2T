#CREA UNA CLASE POKEMON Y REGISTRO POKEMON CAPTURADOS
#POKEMON TENDRÁN NOMBRE, TIPO, NIVEL Y CAPTRUADOS O NO
#CONTADOR DE POKEMONS CAPTURADOS

import random

class Pokemon:

    total = 0

    def __init__(self, name, type, level, captured):
        self.nombre = name
        self.tipo = type
        self.nivel = level
        self.capturado = captured

    def capturar(self):
        x = random.randint(0, 10)
        if x <= 4:
            Pokemon.total += 1
            self.capturado = True
            print(self.nombre, "ha sido capturado!!, Pokemons totales: ", Pokemon.total)
        else: print(self.nombre, "se te ha escapado!!")

pokemon1 = Pokemon("Pikachu", "Eléctrico", 23, False)
pokemon2 = Pokemon("Charmander", "Fuego", 24, False)
pokemon3 = Pokemon("Bulbasur", "Planta", 34, False)
pokemon4 = Pokemon("Eevee", "Normal", 21, False)

listapoke = [pokemon1, pokemon2, pokemon3, pokemon4]

while True:
    y = random.choice(listapoke)
    print("\n\nPokemon", y.nombre , "salvaje apareció")
    S = input("Deseas lanzar una pokeball?? (S/N): ")
    if S == "S": y.capturar()
    else: print("Pokemon", y.nombre, "ha escapado!!")

