
def generar_lista(lista):
    X = int(input("INTRODUCE NÚMERO AQUÍ: "))
    if X % 2 != 0: lista.append(X) 

Lista = []

while True:
    generar_lista(Lista)
    print(Lista)