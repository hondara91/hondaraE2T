

def generar_lista():
    X = int(input("INSERTE NÚMERO AQUÍ: "))
    print ("LISTADO NÚMEROS IMPARES: ") 
    for i in range (1, X + 1, 2): 
        print (i, end = "|")

generar_lista()