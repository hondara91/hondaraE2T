
lista = []
X = int(input("INTRODUCE NÚM AQUÍ: "))

def generar_lista(X):
    for i in range (1, X+1, 2): 
        lista.append (i)
    return lista

print ("lISTADO NÚMEROS IMPARES: ", end = "")
for i in generar_lista(X):
     print(i, end = "|")







