import json

def cargar_agenda():
    with open(input("Python/EJERCICIOS PYTHON/agenda.json"), "r") as archivo:
        miagenda = json.load(archivo)
    return miagenda

cargar_agenda()