import B_ClasesCalculadora

class calculadora:

    def __init__(self, value): self.valor = value
    def sumar(): return int(num1.valor) + int(num2.valor)
    def restar(): return int(num1.valor) - int(num2.valor)
    def ver(): return str(num1.valor) + " y " + str(num2.valor)  
    def __str__(self): return str(self.valor)

while True:   
    
    print("\n----------------------------------------------------------------------")

    try:
        num1 = calculadora(int(input("\nINTRODUCE num1: ")))
        num2 = calculadora(int(input("INTRODUCE num2: ")))

        op = int(input("\nQUÉ OPERACIÓN QUIERES HACER: \n\n1. SUMAR\n2. RESTAR\n3. VER NÚMEROS\n\nELIGE UNA OPCIÓN: "))

        if op == 1: print(num1, "+", num2, "\nEL RESULTADO ES: ", calculadora.sumar())
        elif op == 2: print(num1, "-", num2, "\nEL RESULTADO ES: ", calculadora.restar())
        elif op == 3: print("\nLOS NUMEROS ELEGIDOS SON: ", calculadora.ver())
        else: print("\nINTRODUCE NÚMERO VÁLIDO")

    
    except ValueError: (print("\nINTRODUCE SÓLO NÚMEROS, CABRÓN"))

