class Persona:
    def __init__(self):
        self.pelo = "Moreno"
        self.__sexualidad = "H"

class Animal:
    def __init__(self):
        pass

class Perro(Animal):
    def __init__(self):
        pass


Antonio = Persona()

Antonio.pelo = "rubio"

print(Antonio.__sexualidad)