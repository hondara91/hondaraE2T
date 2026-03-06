class Persona:

    def __init__(self, name, age, rank):
        self.nombre = name
        self.edad = age
        self.empleo = rank

antonio = Persona("Antonio", 36, "Sgt1")
ruben = Persona("Ruben", 44, "Sgt1")

ruben.__dict__