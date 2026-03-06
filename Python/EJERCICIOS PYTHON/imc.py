print ("Hola")

peso = float(input("Introduce peso aquí: "))
altura = float(input("Introduce altura aquí: "))

def calculadoraIMC (peso, altura):
    IMC = round((peso/(altura*altura)), 2)
    print (IMC)
    if IMC < 18.5: return ("BAJO PESO")
    elif 18.5 < IMC < 25: return ("PESO NORMAL")
    elif 25 < IMC < 30: return ("SOBREPESO")
    else: return ("OBESIDAD")

print (calculadoraIMC (peso, altura))


